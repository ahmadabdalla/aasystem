#!/usr/bin/env python3
"""Optional local Codex checkpoints. Records are evidence pointers, not proof of intent."""

import argparse
from contextlib import contextmanager
import hashlib
import fcntl
import json
import os
from pathlib import Path
import re
import shlex
import sys
import stat
import uuid


INVOCATION = re.compile(r"^\s*\$(?:aasystem:)?aapilot(?:\s|$)")
EVENTS = ("SessionStart", "UserPromptSubmit", "SubagentStart", "Stop")
STATUSES = {"active", "waiting", "blocked", "complete", "cancelled"}
CONTINUATION = "[aapilot checkpoint] "


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, name):
    require(isinstance(value, str) and bool(value.strip()), f"{name} must be nonempty text")
    return value


def string_list(value, name, nonempty=False):
    require(isinstance(value, list), f"{name} must be a list")
    if nonempty:
        require(bool(value), f"{name} must not be empty")
    for item in value:
        text(item, name)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    require(path.is_file() and not path.is_symlink(), f"Evidence must be a regular, nonsymlink file: {path}")
    require(path.stat().st_size > 0, f"Evidence is empty: {path}")
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            result.update(chunk)
    return result.hexdigest()


def regular_owned(path):
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid() and info.st_nlink == 1,
            f"Expected an owned regular nonsymlink file: {path}")


def sync_directory(path):
    descriptor = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_write(path, value):
    # A single reserved replacement is recovered under the root directory lock.
    temporary = path.parent / (".task.pending" if path.name == "task.json" else ".bindings.pending")
    descriptor = os.open(temporary, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    sync_directory(path.parent)


@contextmanager
def root_lock(state_dir):
    # Supported boundary: one local POSIX filesystem, one exclusively owned root.
    require(not state_dir.is_symlink(), "State directory must not be a symlink")
    state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor = os.open(state_dir, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        require(os.fstat(descriptor).st_uid == os.getuid(), "State directory has a foreign owner")
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        yield
    finally:
        os.close(descriptor)


def bindings(state_dir):
    path = state_dir / "bindings.json"
    pending = state_dir / ".bindings.pending"
    if pending.exists() or pending.is_symlink():
        regular_owned(pending)
        if path.exists():
            regular_owned(path)
            validate_bindings(read_json(path))  # Preserve recovery copies when committed state is corrupt.
            pending.unlink()
        elif pending.stat().st_size:
            candidate = read_json(pending)
            validate_bindings(candidate)
            os.replace(pending, path)
        else:
            pending.unlink()  # Interrupted first write; no task directory was admitted.
        sync_directory(state_dir)
    if not path.exists():
        return {}
    regular_owned(path)
    result = read_json(path)
    return validate_bindings(result)


def validate_bindings(value):
    require(isinstance(value, dict), "Invalid task bindings")
    for key, entry in value.items():
        require(re.fullmatch(r"[0-9a-f]{64}", key) and isinstance(entry, dict), "Invalid task binding")
        require(re.fullmatch(r"[0-9a-f]{32}", entry.get("owner", "")), "Invalid task owner")
        require(re.fullmatch(r"[0-9a-f]{32}", entry.get("intent_id", "")), "Invalid intent identity")
        require(isinstance(entry.get("cwd"), str) and isinstance(entry.get("session"), str), "Invalid binding identity")
        require(hashlib.sha256((entry["cwd"] + "\0" + entry["session"]).encode()).hexdigest() == key,
                "Binding registration key differs from workspace/session")
        if "retiring" in entry:
            receipt = entry["retiring"]
            require(isinstance(receipt, dict) and isinstance(receipt.get("path"), str)
                    and Path(receipt["path"]).is_absolute()
                    and isinstance(receipt.get("sha256"), str)
                    and re.fullmatch(r"[0-9a-f]{64}", receipt["sha256"])
                    and isinstance(receipt.get("evidence"), list), "Invalid retirement receipt")
    return value


def save_bindings(state_dir, value):
    atomic_write(state_dir / "bindings.json", value)


def recover_task(path, cwd, session):
    pending = path.parent / ".task.pending"
    if pending.exists() or pending.is_symlink():
        regular_owned(pending)
        if path.exists():
            load_task(path, cwd, session)
            pending.unlink()
        else:
            load_task(pending, cwd, session)
            os.replace(pending, path)
        sync_directory(path.parent)


def task_path(state_dir, cwd, session):
    text(session, "session")
    require(len(session) <= 256 and not any(c in session for c in "/\\\x00"), "Invalid session id")
    workspace = Path(cwd)
    require(workspace.is_absolute() and workspace.is_dir(), "cwd must be an existing absolute directory")
    workspace = str(workspace.resolve())
    key = hashlib.sha256((workspace + "\0" + session).encode()).hexdigest()
    return state_dir / key / "task.json", workspace


def load_task(path, cwd, session):
    require(not path.parent.is_symlink(), "Task directory must not be a symlink")
    regular_owned(path)
    task = read_json(path)
    require(isinstance(task, dict) and type(task.get("version")) is int and task["version"] == 2,
            "Unsupported task record version")
    require(task.get("session_id") == session and task.get("cwd") == cwd, "Task session/workspace binding differs")
    require(type(task.get("revision")) is int and task["revision"] >= 1, "Invalid task revision")
    inputs = task.get("inputs")
    require(isinstance(inputs, list) and bool(inputs), "Task has no captured request")
    for item in inputs:
        require(isinstance(item, dict), "Invalid captured input")
        text(item.get("text"), "captured input")
        require(isinstance(item.get("turn_id"), str), "Invalid input turn id")
    require(re.fullmatch(r"[0-9a-f]{32}", task.get("intent_id", "")), "Invalid intent identity")
    text(task.get("original_request"), "original_request")
    require(inputs[0]["text"] == task["original_request"], "Original request differs from captured input")
    owners = bindings(path.parent.parent)
    owner = owners.get(path.parent.name)
    require(owner is not None and owner["owner"] == task.get("owner")
            and owner["intent_id"] == task["intent_id"], "Task ownership differs from registration")
    source = task.get("canonical")
    if source is not None:
        require(isinstance(source, dict) and isinstance(source.get("path"), str)
                and Path(source["path"]).is_absolute()
                and not Path(source["path"]).resolve().is_relative_to(path.parent.parent)
                and isinstance(source.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", source["sha256"]),
                "Invalid canonical recovery reference")
    require("body" in task, "Task body is missing")
    if task["body"] is not None:
        validate_body(task["body"], len(inputs), check_evidence=False)
    return task


def validate_evidence(items):
    require(isinstance(items, list) and bool(items), "Passed obligation needs evidence")
    for item in items:
        require(isinstance(item, dict), "Evidence must contain path and sha256")
        path = Path(text(item.get("path"), "evidence path"))
        require(path.is_absolute(), "Evidence path must be absolute")
        expected = item.get("sha256")
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "Invalid evidence sha256")
        require(digest(path) == expected, f"Evidence changed; reverify: {path}")


def validate_body(body, input_count, check_evidence=True):
    require(isinstance(body, dict), "Task body must be an object")
    for name in ("outcome", "boundary", "current_increment", "next_action"):
        text(body.get(name), name)
    for name in ("constraints", "decisions"):
        string_list(body.get(name), name)
    string_list(body.get("route"), "route", nonempty=True)
    effort = body.get("effort")
    require(isinstance(effort, dict) and effort.get("size") in {"S", "M", "L"}, "effort requires size S/M/L")
    text(effort.get("reason"), "effort reason")
    ack = body.get("acknowledged_inputs")
    require(type(ack) is int and 0 <= ack <= input_count, "Invalid acknowledged_inputs")
    status = body.get("status")
    require(status in STATUSES, "Unknown task status")
    require(isinstance(body.get("reason"), str), "reason must be text")
    require(isinstance(body.get("reconciliation"), str), "reconciliation must be text")
    if status in {"waiting", "blocked", "cancelled"}:
        text(body["reason"], "pause/cancellation reason")
    obligations = body.get("obligations")
    require(isinstance(obligations, list) and bool(obligations), "At least one task-selected obligation is required")
    ids = set()
    for obligation in obligations:
        require(isinstance(obligation, dict), "Invalid obligation")
        for name in ("id", "description", "stage"):
            text(obligation.get(name), f"obligation {name}")
        require(obligation["id"] not in ids, "Duplicate obligation id")
        ids.add(obligation["id"])
        require(obligation.get("status") in {"pending", "passed"}, "Obligation status must be pending/passed")
        require(isinstance(obligation.get("evidence"), list), "obligation evidence must be a list")
        if obligation["status"] == "passed" and check_evidence:
            validate_evidence(obligation["evidence"])
    findings = body.get("findings")
    require(isinstance(findings, list), "findings must be a list")
    for finding in findings:
        require(isinstance(finding, dict), "Invalid finding")
        text(finding.get("description"), "finding description")
        require(type(finding.get("material")) is bool and type(finding.get("resolved")) is bool,
                "finding material/resolved must be booleans")
        require(isinstance(finding.get("return_checkpoint"), str), "finding return_checkpoint must be text")
        if not finding["resolved"] and not finding["material"]:
            text(finding["return_checkpoint"], "deferred finding return_checkpoint")
    return body


def check_checkpoint(task, final=False):
    body = validate_body(task["body"], len(task["inputs"]))
    require(body["acknowledged_inputs"] == len(task["inputs"]), "New user inputs must be reconciled first")
    require(not any(f["material"] and not f["resolved"] for f in body["findings"]),
            "Unresolved material findings block progression/completion")
    selected = body["obligations"] if final else [
        item for item in body["obligations"] if item["stage"] == body["current_increment"]
    ]
    require(bool(selected), "Current increment has no selected obligations")
    require(all(item["status"] == "passed" for item in selected), "Required obligations remain pending")
    if final:
        text(body["reconciliation"], "original-request reconciliation")


def register_task(path, cwd, session, prompt, turn_id, intent_id=None, canonical=None):
    owners = bindings(path.parent.parent)
    require(path.parent.name not in owners and not path.parent.exists(),
            "An existing task binding must be handed off before rebinding")
    intent_id = intent_id or uuid.uuid4().hex
    require(not any(entry["intent_id"] == intent_id for entry in owners.values()),
            "Intent already has an active binding; hand it off before resuming")
    owner = uuid.uuid4().hex
    task = {"version": 2, "session_id": session, "cwd": cwd, "revision": 1,
            "intent_id": intent_id, "original_request": prompt, "owner": owner,
            "inputs": [{"text": prompt, "turn_id": turn_id}], "body": None}
    if canonical is not None:
        task["canonical"] = canonical
    owners[path.parent.name] = {"owner": owner, "intent_id": intent_id, "cwd": cwd,
                                "session": session, "initial": task}
    save_bindings(path.parent.parent, owners)
    path.parent.mkdir(mode=0o700)
    sync_directory(path.parent.parent)
    return task


def publish_task(path, task):
    atomic_write(path, task)
    owners = bindings(path.parent.parent)
    entry = owners.get(path.parent.name)
    if entry is not None and "initial" in entry:
        del entry["initial"]
        save_bindings(path.parent.parent, owners)


def capture(path, cwd, session, event):
    prompt = text(event.get("prompt"), "prompt")
    if event.get("agent_id"):
        return
    turn_id = event.get("turn_id", "")
    require(isinstance(turn_id, str), "Invalid input turn id")
    explicit = bool(INVOCATION.match(prompt))
    existed = path.parent.exists()
    if not existed and not explicit:
        return
    if not path.exists():
        require(not existed, "Missing active record; inspect state before recovery")
        task = register_task(path, cwd, session, prompt, turn_id)
    else:
        task = load_task(path, cwd, session)
        if turn_id and any(item["turn_id"] == turn_id and item["text"] == prompt for item in task["inputs"]):
            return
        # Explicit invocation is a correction until the previous intent is handed off.
        task["inputs"].append({"text": prompt, "turn_id": turn_id})
        task["revision"] += 1
        if task["body"]:
            task["body"]["status"] = "active"
            task["body"]["reconciliation"] = ""
    publish_task(path, task)


def recovery_context(path, task, state_dir):
    command = shlex.join([sys.executable, str(Path(__file__).resolve()), "--state-dir", str(state_dir),
                          "--session", task["session_id"], "--cwd", task["cwd"]])
    body = task["body"]
    summary = {"original_request": task["original_request"], "latest_input": task["inputs"][-1]["text"],
               "revision": task["revision"], "intent_id": task["intent_id"], "canonical": task.get("canonical"),
               "input_count": len(task["inputs"]), "body": body}
    rendered = json.dumps(summary, ensure_ascii=False)
    if len(rendered) > 6500:
        rendered = rendered[:6500] + "… [summary truncated; read the full record]"
    guide = Path(__file__).resolve().parents[1] / "assets/codex/README.md"
    return (f"Aapilot durable task: {path}\nRead the complete record before dependent work. "
            "The root coordinator alone updates it; subagents return evidence to that owner. "
            "Restore original intent, decisions, sizing and selected procedures; honor research/design boundaries. "
            f"CLI: {command} show; update --file -; checkpoint --expected-revision N. "
            f"Schema and lifecycle: {guide}. "
            "Before final stopping, preserve intent, decisions and necessary proof in an authorized existing task file, "
            "read it back, then handoff --record PATH --expected-revision N --expected-record-sha256 HASH. "
            "Use workdir for disposable files; stop/reconcile all workers before --workers-stopped. "
            "Resume: reread the entire canonical file and reconstruct the body before checkpoints; "
            "its hash names the selected version, not ongoing proof. Stop is not SessionEnd cleanup.\n" + rendered)


def incomplete(message, event):
    reason = CONTINUATION + message + ". Reconcile the durable task and required evidence, or record a truthful waiting/blocked state with reason and next action."
    if event.get("stop_hook_active"):
        return {"continue": False, "stopReason": "Aapilot remains incomplete", "systemMessage": reason}
    return {"decision": "block", "reason": reason}


def handle_hook(state_dir, event):
    require(isinstance(event, dict), "Hook payload must be an object")
    kind = event.get("hook_event_name")
    require(kind in EVENTS, "Unsupported hook event")
    path, cwd = task_path(state_dir, event.get("cwd", ""), event.get("session_id"))
    recover_state(state_dir, path.parent.name)
    if kind == "UserPromptSubmit":
        capture(path, cwd, event["session_id"], event)
    if not path.parent.exists():
        return {}
    task = load_task(path, cwd, event["session_id"])
    if kind == "Stop":
        body = task["body"]
        require(body is not None, "Task is not yet sized and recorded")
        require(body["acknowledged_inputs"] == len(task["inputs"]), "New user inputs remain unreconciled")
        if body["status"] in {"waiting", "blocked", "cancelled"}:
            return {"systemMessage": f"Aapilot {body['status']} (not complete): {body['reason']}. Next: {body['next_action']}"}
        require(body["status"] == "complete", "Task is still active")
        check_checkpoint(task, final=True)
        return incomplete("Completed intent still has disposable state; write/read back the authorized canonical record, "
                          "then run handoff --record PATH --expected-revision N --expected-record-sha256 HASH before stopping", event)
    return {"hookSpecificOutput": {"hookEventName": kind,
                                   "additionalContext": recovery_context(path, task, state_dir)}}


def hook_config(state_dir):
    command = shlex.join([sys.executable, str(Path(__file__).resolve()), "--state-dir", str(state_dir), "hook"])
    return {"hooks": {event: [{"hooks": [{"type": "command", "command": command,
                                            "timeout": 10, **({"additionalContextLimit": 2500} if event != "Stop" else {})}]}]
                      for event in EVENTS}}


def canonical_text(path):
    require(path.is_absolute(), "Canonical record path must be absolute")
    regular_owned(path)
    data = path.read_bytes()
    rendered = data.decode("utf-8")
    text(rendered, "canonical record")
    require("\x00" not in rendered, "Canonical record must be a local UTF-8 text file")
    return rendered, hashlib.sha256(data).hexdigest()


def task_scope(path):
    require(not path.parent.is_symlink() and path.parent.is_dir()
            and path.parent.stat().st_uid == os.getuid(), "Invalid owned task directory")
    allowed = {"task.json", ".task.pending", "work"}
    require(all(item.name in allowed for item in path.parent.iterdir()),
            "Unknown files in task directory; refusing retirement")
    entries = []
    def visit(directory):
        require(directory.lstat().st_uid == os.getuid() and not directory.is_symlink(),
                f"Foreign or symlinked scratch directory: {directory}")
        for item in directory.iterdir():
            info = item.lstat()
            if stat.S_ISDIR(info.st_mode):
                visit(item)
            else:
                regular_owned(item)
                entries.append(item)
        entries.append(directory)
    for item in path.parent.iterdir():
        if item.name == "work":
            require(item.is_dir() and not item.is_symlink(), "Invalid work directory")
            visit(item)
        else:
            regular_owned(item)
            entries.append(item)
    entries.append(path.parent)
    return entries


def finish_retirement(state_dir, key, owners):
    entry = owners[key]
    receipt = entry["retiring"]
    require(canonical_text(Path(receipt["path"]))[1] == receipt["sha256"],
            "Retirement destination changed; preserving remaining scratch")
    if receipt["evidence"]:
        validate_evidence(receipt["evidence"])
    path = state_dir / key / "task.json"
    if path.parent.exists() or path.parent.is_symlink():
        if path.exists():
            load_task(path, entry["cwd"], entry["session"])
        for item in task_scope(path):
            if item.is_dir():
                item.rmdir()
            else:
                item.unlink()
        sync_directory(state_dir)
    del owners[key]
    save_bindings(state_dir, owners)


def recover_state(state_dir, selected_key):
    owners = bindings(state_dir)
    for key in list(owners):
        try:
            entry = owners[key]
            if "retiring" in entry:
                finish_retirement(state_dir, key, owners)
            elif "initial" in entry:
                path = state_dir / key / "task.json"
                require(not path.parent.is_symlink(), "Task directory is a symlink")
                path.parent.mkdir(mode=0o700, exist_ok=True)
                pending = path.parent / ".task.pending"
                if not path.exists():
                    if pending.exists() or pending.is_symlink():
                        regular_owned(pending)
                        pending.unlink()  # The committed registration retains the full initial request.
                    atomic_write(path, entry["initial"])
                recover_task(path, entry["cwd"], entry["session"])
                load_task(path, entry["cwd"], entry["session"])
                del entry["initial"]
                save_bindings(state_dir, owners)
            elif (state_dir / key).exists():
                require(not (state_dir / key).is_symlink(), "Task directory is a symlink")
                require((state_dir / key).stat().st_uid == os.getuid(), "Foreign task directory")
                recover_task(state_dir / key / "task.json", entry["cwd"], entry["session"])
            else:
                raise ValueError(f"Registered task is missing: {state_dir / key}; preserving ownership")
        except (OSError, ValueError, TypeError, KeyError):
            # Failed peer state stays recoverable without blocking this task.
            if key == selected_key:
                raise


def retained_text(task):
    body = task["body"]
    values = [task["intent_id"], task["original_request"]]
    values.extend(body[name] for name in ("outcome", "boundary", "current_increment", "next_action", "status"))
    values.extend(body["constraints"] + body["decisions"] + body["route"])
    values.extend([body["effort"]["size"], body["effort"]["reason"]])
    values.extend(body[name] for name in ("reason", "reconciliation") if body[name])
    for obligation in body["obligations"]:
        values.extend(obligation[name] for name in ("id", "description", "stage", "status"))
        for evidence in obligation["evidence"]:
            values.extend((evidence["path"], evidence["sha256"]))
    for finding in body["findings"]:
        values.extend([finding["description"], finding["return_checkpoint"]])
    return values


def handoff(state_dir, path, task, args):
    require(args.expected_revision == task["revision"], "Stale handoff revision")
    body = validate_body(task["body"], len(task["inputs"]))
    require(body["acknowledged_inputs"] == len(task["inputs"]), "Handoff requires reconciled inputs")
    require(body["status"] in {"complete", "waiting", "blocked", "cancelled"},
            "Record completion or a truthful pause before handoff")
    if body["status"] == "complete":
        check_checkpoint(task, final=True)
    record = args.record
    rendered, hashed = canonical_text(record)
    require(hashed == args.expected_record_sha256, "Canonical record changed; reread before handoff")
    require(not record.resolve().is_relative_to(state_dir), "Canonical record must be outside scratch state")
    require(all(value in rendered for value in retained_text(task)),
            "Canonical record must retain intent ID, original request, decisions, constraints and recovery/proof fields verbatim")
    retained_evidence = []
    for obligation in body["obligations"]:
        for evidence in obligation["evidence"]:
            require(isinstance(evidence, dict), "Invalid retained evidence reference")
            evidence_path = Path(text(evidence.get("path"), "evidence path"))
            require(evidence_path.is_absolute(), "Evidence path must be absolute")
            require(not evidence_path.resolve().is_relative_to(state_dir),
                    "Referenced evidence is inside scratch; persist and reverify it before handoff")
            if obligation["status"] == "passed":
                validate_evidence([evidence])
                retained_evidence.append(evidence)
    require(not (path.parent / "work").exists() or args.workers_stopped,
            "Stop/reconcile all scratch users and assert --workers-stopped before handoff")
    task_scope(path)  # Validate the entire exact scope before recording retirement.
    owners = bindings(state_dir)
    owners[path.parent.name]["retiring"] = {"path": str(record), "sha256": hashed,
                                            "revision": task["revision"], "evidence": retained_evidence}
    save_bindings(state_dir, owners)
    finish_retirement(state_dir, path.parent.name, owners)
    return {"handoff": "retired", "intent_id": task["intent_id"], "record": str(record), "sha256": hashed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, required=True)
    parser.add_argument("--session")
    parser.add_argument("--cwd")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("config", help="Print optional Codex hooks JSON; changes no settings")
    commands.add_parser("hook", help="Handle one Codex JSON event on stdin")
    commands.add_parser("show")
    checkpoint = commands.add_parser("checkpoint", help="Check the current increment; does not advance it")
    checkpoint.add_argument("--expected-revision", type=int, required=True)
    update = commands.add_parser("update", help="Validate and atomically save the coordinator's task body")
    update.add_argument("--file", type=Path, required=True)
    commands.add_parser("workdir", help="Create/return the exact owned disposable work directory")
    retirement = commands.add_parser("handoff", help="Verify canonical retention and retire exact owned scratch")
    retirement.add_argument("--record", type=Path, required=True)
    retirement.add_argument("--expected-revision", type=int, required=True)
    retirement.add_argument("--expected-record-sha256", required=True)
    retirement.add_argument("--workers-stopped", action="store_true")
    resume = commands.add_parser("resume", help="Resume an existing canonical text record; owner reconstructs its body")
    resume.add_argument("--record", type=Path, required=True)
    resume.add_argument("--intent-id", required=True)
    resume.add_argument("--original-request", required=True)
    evidence = commands.add_parser("evidence", help="Print SHA-256 references for existing evidence files")
    evidence.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    require(args.state_dir.is_absolute(), "state-dir must be absolute and outside maintained source")
    require(not args.state_dir.is_symlink(), "State directory must not be a symlink")
    require(not any(parent.is_symlink() for parent in args.state_dir.parents),
            "State directory ancestors must not be symlinks")
    state_dir = args.state_dir.resolve()
    event = json.load(sys.stdin) if args.command == "hook" else None
    activate = (isinstance(event, dict) and event.get("hook_event_name") == "UserPromptSubmit"
                and isinstance(event.get("prompt"), str) and INVOCATION.match(event["prompt"])
                and not event.get("agent_id"))
    try:
        if args.command in {"config", "evidence"} or (args.command == "hook" and not state_dir.exists() and not activate):
            execute(args, state_dir, event)
        else:
            with root_lock(state_dir):
                execute(args, state_dir, event)
    except (OSError, ValueError, TypeError, KeyError) as error:
        if args.command != "hook":
            raise
        result = incomplete(str(error), event) if isinstance(event, dict) and event.get("hook_event_name") == "Stop" else {
            "systemMessage": f"Aapilot hook failed: {error}. Task state is unverified."}
        print(json.dumps(result, ensure_ascii=False))


def execute(args, state_dir, event):
    if args.command == "config":
        result = hook_config(state_dir)
    elif args.command == "hook":
        result = handle_hook(state_dir, event)
    elif args.command == "evidence":
        result = [{"path": str(path.absolute()), "sha256": digest(path.absolute())} for path in args.paths]
    else:
        require(args.cwd is not None, "--cwd is required")
        path, cwd = task_path(state_dir, args.cwd, args.session)
        recover_state(state_dir, path.parent.name)
        if args.command == "resume":
            rendered, hashed = canonical_text(args.record)
            require(not args.record.resolve().is_relative_to(state_dir), "Canonical record must be outside scratch state")
            require(re.fullmatch(r"[0-9a-f]{32}", args.intent_id), "Invalid intent identity")
            text(args.original_request, "original_request")
            require(args.intent_id in rendered and args.original_request in rendered,
                    "Canonical record must contain the supplied intent ID and original request verbatim")
            task = register_task(path, cwd, args.session, args.original_request, "", args.intent_id,
                                 {"path": str(args.record), "sha256": hashed})
            publish_task(path, task)
            result = {"path": str(path), "intent_id": task["intent_id"], "canonical": task["canonical"],
                      "context": "Read the entire canonical record and reconstruct the body before dependent work"}
        elif args.command == "show":
            result = load_task(path, cwd, args.session)
        elif args.command == "checkpoint":
            task = load_task(path, cwd, args.session)
            require(args.expected_revision == task["revision"], "Stale checkpoint revision; reread the task")
            check_checkpoint(task)
            result = {"checkpoint": "passed", "revision": task["revision"],
                      "scope": "current increment's recorded obligations"}
        elif args.command == "workdir":
            task = load_task(path, cwd, args.session)
            work = path.parent / "work"
            require(not work.is_symlink(), "Work directory must not be a symlink")
            work.mkdir(exist_ok=True, mode=0o700)
            result = {"path": str(work), "intent_id": task["intent_id"]}
        elif args.command == "handoff":
            if not path.parent.exists():
                rendered, hashed = canonical_text(args.record)
                require(hashed == args.expected_record_sha256, "Canonical record changed")
                result = {"handoff": "already absent", "record": str(args.record), "sha256": hashed}
            else:
                result = handoff(state_dir, path, load_task(path, cwd, args.session), args)
        else:
            task = load_task(path, cwd, args.session)
            change = json.load(sys.stdin) if str(args.file) == "-" else read_json(args.file)
            require(isinstance(change, dict) and type(change.get("expected_revision")) is int
                    and change["expected_revision"] == task["revision"],
                    "Stale update revision; reread captured inputs before updating")
            body = validate_body(change.get("body"), len(task["inputs"]))
            require(body["acknowledged_inputs"] == len(task["inputs"]), "Update must acknowledge every captured input")
            task["body"] = body
            if body["status"] == "complete":
                check_checkpoint(task, final=True)
            task["revision"] += 1
            atomic_write(path, task)
            result = {"path": str(path), "revision": task["revision"], "status": body["status"]}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError) as error:
        sys.exit(f"Aapilot: {error}")
