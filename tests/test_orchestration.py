"""Exercise the shipped CLI and Codex event protocol at their public boundaries."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/aapilot/scripts/orchestration.py"


class OrchestrationTest(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix="aapilot-orchestration-")
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        self.cwd = self.root / "project"
        self.cwd.mkdir()
        self.state = self.root / "state"
        self.session = "task-123"
        self.counter = 0

    def cli(self, *arguments, payload=None, session=None, cwd=None, success=True):
        command = [sys.executable, str(SCRIPT), "--state-dir", str(self.state),
                   "--session", session or self.session, "--cwd", str(cwd or self.cwd), *arguments]
        run = subprocess.run(command, input=json.dumps(payload) if payload is not None else None,
                             text=True, capture_output=True, timeout=10)
        if success:
            self.assertEqual(run.returncode, 0, run.stderr)
            return json.loads(run.stdout)
        self.assertNotEqual(run.returncode, 0, run.stdout)
        return run

    def hook(self, kind="UserPromptSubmit", prompt="$aapilot Explain today's import behavior; stop at findings.", **fields):
        self.counter += 1
        event = {"hook_event_name": kind, "session_id": self.session, "cwd": str(self.cwd),
                 "turn_id": f"turn-{self.counter}", **fields}
        if kind == "UserPromptSubmit":
            event["prompt"] = prompt
        return self.cli("hook", payload=event)

    def state_path(self):
        return next(self.state.glob("*/task.json"))

    def body(self, status="active", size="S", route=None):
        return {"acknowledged_inputs": len(self.cli("show")["inputs"]),
                "outcome": "Explain import behavior with sources and limits",
                "constraints": ["Do not edit product files"], "decisions": ["Stop at research findings"],
                "effort": {"size": size, "reason": "A bounded investigation with an established entry point"},
                "route": route or ["investigation"], "boundary": "Research findings only",
                "current_increment": "research", "next_action": "Present findings with sources",
                "obligations": [{"id": "sources", "description": "Trace actual import behavior",
                                 "stage": "research", "status": "pending", "evidence": []}],
                "findings": [], "status": status, "reason": "", "reconciliation": ""}

    def update(self, body, revision=None, success=True):
        change = self.root / "update.json"
        change.write_text(json.dumps({"expected_revision": revision if revision is not None else self.cli("show")["revision"],
                                      "body": body}))
        return self.cli("update", "--file", str(change), success=success)

    def evidence(self, name="findings.txt", content="Observed entry point and behavior; unsupported cases remain gaps."):
        path = self.root / name
        path.write_text(content)
        return {"path": str(path), "sha256": hashlib.sha256(content.encode()).hexdigest()}

    def completed(self):
        body = self.body(status="complete")
        body["obligations"][0].update(status="passed", evidence=[self.evidence()])
        body["reconciliation"] = "The original research question is answered with sources and limits; no product changes."
        return body

    def test_nonparticipating_session_is_noop_and_creates_no_state(self):
        self.assertEqual(self.hook(prompt="Explain the import code."), {})
        self.assertEqual(self.hook(kind="SessionStart", source="startup"), {})
        self.assertEqual(self.hook(kind="Stop"), {})
        self.assertFalse(self.state.exists())

    def test_explicit_invocation_captures_verbatim_and_is_recoverable(self):
        prompt = "$aasystem:aapilot Add search, preserve filters, and stop at local changes."
        context = self.hook(prompt=prompt)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("root coordinator alone", context)
        self.assertEqual(self.cli("show")["inputs"][0]["text"], prompt)
        self.assertIn(str(self.state_path()), context)

    def test_invocation_quoted_in_normal_prose_does_not_activate(self):
        self.assertEqual(self.hook(prompt="Would `$aapilot change imports` work?"), {})
        self.assertFalse(self.state.exists())

    def test_compaction_and_subagent_handoff_restore_same_contract_without_writing(self):
        self.hook()
        body = self.body(size="L", route=["product", "interaction-design", "architect", "feature"])
        self.update(body)
        before = self.state_path().read_bytes()
        for kind, fields in [("SessionStart", {"source": "compact"}), ("SubagentStart", {"agent_id": "worker-1"})]:
            result = self.hook(kind=kind, **fields)["hookSpecificOutput"]["additionalContext"]
            self.assertIn("interaction-design", result)
            self.assertIn("Do not edit product files", result)
            self.assertEqual(self.state_path().read_bytes(), before)

    def test_research_and_design_can_complete_without_implementation_obligation(self):
        for route in (["investigation"], ["product", "interaction-design", "architect"]):
            with self.subTest(route=route):
                if not self.state.exists():
                    self.hook()
                body = self.completed()
                body["route"] = route
                self.update(body)
                self.assertIn("handoff", self.hook(kind="Stop")["reason"])

    def test_current_increment_checkpoint_permits_future_pending_work(self):
        self.hook()
        body = self.completed()
        body["status"] = "active"
        body["effort"]["size"] = "L"
        body["route"] = ["product", "interaction-design", "architect", "implement", "verification"]
        body["obligations"].append({"id": "behavior", "description": "Verify retained behavior",
                                    "stage": "delivery", "status": "pending", "evidence": []})
        saved = self.update(body)
        self.assertEqual(self.cli("checkpoint", "--expected-revision", str(saved["revision"]))["checkpoint"], "passed")
        body["status"] = "complete"
        self.assertIn("pending", self.update(body, success=False).stderr)

    def test_checkpoint_rejects_stale_revision_and_unreconciled_user_input(self):
        self.hook()
        saved = self.update(self.completed())
        self.hook(prompt="Also cover malformed rows; still no edits.")
        self.assertIn("Stale checkpoint", self.cli("checkpoint", "--expected-revision", str(saved["revision"]), success=False).stderr)
        current = self.cli("show")["revision"]
        self.assertIn("reconciled", self.cli("checkpoint", "--expected-revision", str(current), success=False).stderr)

    def test_new_input_reopens_complete_task_and_preserves_original(self):
        self.hook()
        self.update(self.completed())
        original = self.cli("show")["inputs"][0]
        self.hook(prompt="Correction: cover malformed rows and preserve all saved settings.")
        task = self.cli("show")
        self.assertEqual(task["inputs"][0], original)
        self.assertEqual(task["body"]["status"], "active")
        self.assertEqual(task["body"]["reconciliation"], "")
        self.assertIn("unreconciled", self.hook(kind="Stop")["reason"])

    def test_repeated_explicit_invocation_keeps_prior_contract_for_reconciliation(self):
        self.hook()
        self.hook(prompt="$aapilot Now implement a replacement importer.")
        task = self.cli("show")
        self.assertEqual(len(task["inputs"]), 2)
        self.assertIn("stop at findings", task["inputs"][0]["text"])

    def test_duplicate_prompt_event_is_idempotent(self):
        prompt = "$aapilot Explain current imports; stop at findings."
        self.hook(prompt=prompt, turn_id="stable-turn")
        before = self.cli("show")
        self.hook(prompt=prompt, turn_id="stable-turn")
        self.assertEqual(self.cli("show"), before)

    def test_different_input_in_same_turn_is_preserved(self):
        self.hook(turn_id="steered-turn")
        self.hook(prompt="Also preserve cancellation behavior.", turn_id="steered-turn")
        self.assertEqual(len(self.cli("show")["inputs"]), 2)

    def test_subagent_prompt_does_not_capture_or_modify_root_record(self):
        self.hook()
        before = self.cli("show")
        self.assertIn("hookSpecificOutput", self.hook(prompt="implement assigned slice", agent_id="worker-1"))
        self.assertEqual(self.cli("show"), before)

    def test_stop_continuation_is_preserved_for_reconciliation(self):
        self.hook()
        reason = self.hook(kind="Stop")["reason"]
        self.hook(prompt=reason)
        task = self.cli("show")
        self.assertEqual(len(task["inputs"]), 2)
        self.assertEqual(task["inputs"][-1]["text"], reason)
        self.update(self.completed())
        self.assertIn("handoff", self.hook(kind="Stop")["reason"])

    def test_user_correction_with_checkpoint_prefix_reopens_completed_task(self):
        self.hook()
        self.update(self.completed())
        correction = "[aapilot checkpoint] Correction: preserve empty imports too."
        self.hook(prompt=correction)
        task = self.cli("show")
        self.assertEqual(task["inputs"][-1]["text"], correction)
        self.assertEqual(task["body"]["status"], "active")
        self.assertIn("unreconciled", self.hook(kind="Stop")["reason"])

    def test_malformed_turn_id_preserves_valid_record_and_does_not_activate_new_task(self):
        self.hook()
        before = self.state_path().read_bytes()
        for turn_id in (None, 17, [], {}):
            with self.subTest(turn_id=turn_id):
                result = self.hook(prompt="Preserve original behavior", turn_id=turn_id)
                self.assertIn("Invalid input turn id", result["systemMessage"])
                self.assertEqual(self.state_path().read_bytes(), before)
                self.assertEqual(len(self.cli("show")["inputs"]), 1)
        result = self.cli("hook", payload={"hook_event_name": "UserPromptSubmit", "session_id": "new-invalid",
                                          "cwd": str(self.cwd), "turn_id": None, "prompt": "$aapilot Investigate"})
        self.assertIn("Invalid input turn id", result["systemMessage"])
        self.assertEqual(len(list(self.state.glob("*/task.json"))), 1)

    def test_stop_retries_once_then_marks_incomplete(self):
        self.hook()
        first = self.hook(kind="Stop")
        self.assertEqual(first["decision"], "block")
        second = self.hook(kind="Stop", stop_hook_active=True)
        self.assertIs(second["continue"], False)
        self.assertIn("incomplete", second["stopReason"])
        self.assertIsNone(self.cli("show")["body"])

    def test_waiting_blocked_and_cancelled_are_truthful_stopping_points(self):
        self.hook()
        for status in ("waiting", "blocked", "cancelled"):
            body = self.body(status=status)
            body["reason"] = "Need the user's decision on data retention"
            body["next_action"] = "Wait for that decision before dependent changes"
            body["findings"] = [{"description": "Retention remains unsettled", "material": True,
                                 "resolved": False, "return_checkpoint": ""}]
            self.update(body)
            result = self.hook(kind="Stop")
            self.assertIn(f"{status} (not complete)", result["systemMessage"])
            self.assertNotIn("decision", result)

    def test_complete_requires_reconciliation_and_resolved_material_findings(self):
        self.hook()
        body = self.completed()
        body["reconciliation"] = ""
        self.assertIn("reconciliation", self.update(body, success=False).stderr)
        body["reconciliation"] = "Addressed original question"
        body["findings"] = [{"description": "Observed material contradiction", "material": True,
                             "resolved": False, "return_checkpoint": "next review"}]
        self.assertIn("material", self.update(body, success=False).stderr)

    def test_deferred_minor_findings_require_a_return_checkpoint(self):
        self.hook()
        body = self.completed()
        body["findings"] = [{"description": "Optional additional source", "material": False,
                             "resolved": False, "return_checkpoint": ""}]
        self.assertIn("return_checkpoint", self.update(body, success=False).stderr)
        body["findings"][0]["return_checkpoint"] = "Next importer change"
        self.update(body)

    def test_missing_or_changed_evidence_blocks_completion_and_preserves_previous_state(self):
        self.hook()
        self.update(self.body())
        before = self.state_path().read_bytes()
        body = self.completed()
        path = Path(body["obligations"][0]["evidence"][0]["path"])
        path.write_text("Contradictory changed observation")
        self.assertIn("Evidence changed", self.update(body, success=False).stderr)
        self.assertEqual(self.state_path().read_bytes(), before)
        path.unlink()
        self.assertIn("regular", self.update(body, success=False).stderr)

    def test_evidence_changed_after_completion_is_caught_by_stop(self):
        self.hook()
        body = self.completed()
        self.update(body)
        Path(body["obligations"][0]["evidence"][0]["path"]).write_text("Changed after checkpoint")
        self.assertIn("Evidence changed", self.hook(kind="Stop")["reason"])

    def test_wrong_binding_corrupt_or_missing_record_never_passes_as_complete(self):
        self.hook()
        path = self.state_path()
        task = self.cli("show")
        task["session_id"] = "different-session"
        path.write_text(json.dumps(task))
        self.assertIn("binding", self.hook(kind="Stop")["reason"])
        path.write_text("{")
        self.assertEqual(self.hook(kind="Stop")["decision"], "block")
        path.unlink()
        self.assertEqual(self.hook(kind="Stop")["decision"], "block")
        self.hook(prompt="$aapilot Do not replace a missing original task")
        self.assertFalse(path.exists())

    def test_stale_update_is_rejected_without_losing_captured_correction(self):
        self.hook()
        body = self.body()
        revision = self.cli("show")["revision"]
        self.hook(prompt="Preserve the cancellation rule too.")
        self.assertIn("Stale update", self.update(body, revision=revision, success=False).stderr)
        self.assertEqual(len(self.cli("show")["inputs"]), 2)

    def test_strict_booleans_and_revision_types_are_rejected(self):
        self.hook()
        body = self.body()
        body["acknowledged_inputs"] = True
        self.assertIn("acknowledged_inputs", self.update(body, success=False).stderr)
        body["acknowledged_inputs"] = 1
        self.assertIn("Stale update", self.update(body, revision=True, success=False).stderr)
        body["findings"] = [{"description": "Check", "material": "false", "resolved": True, "return_checkpoint": ""}]
        self.assertIn("booleans", self.update(body, success=False).stderr)

    def test_two_sessions_in_same_workspace_remain_isolated(self):
        def invoke(session):
            payload = {"hook_event_name": "UserPromptSubmit", "session_id": session, "cwd": str(self.cwd),
                       "turn_id": "first", "prompt": f"$aapilot Explain {session}; no edits."}
            return self.cli("hook", payload=payload)
        with ThreadPoolExecutor(max_workers=2) as pool:
            list(pool.map(invoke, ["first-session", "second-session"]))
        first = self.cli("show", session="first-session")
        second = self.cli("show", session="second-session")
        self.assertNotEqual(first["inputs"], second["inputs"])
        self.assertEqual(len(list(self.state.glob("*/task.json"))), 2)

    def test_simultaneous_corrections_are_both_preserved(self):
        self.hook()
        def correction(number):
            event = {"hook_event_name": "UserPromptSubmit", "session_id": self.session, "cwd": str(self.cwd),
                     "turn_id": f"correction-{number}", "prompt": f"Preserve constraint {number}."}
            return self.cli("hook", payload=event)
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(correction, [1, 2]))
        self.assertTrue(all("hookSpecificOutput" in result for result in results))
        task = self.cli("show")
        self.assertEqual(len(task["inputs"]), 3)
        self.assertEqual({item["text"] for item in task["inputs"][1:]},
                         {"Preserve constraint 1.", "Preserve constraint 2."})

    def test_traversal_session_and_relative_configuration_paths_are_rejected(self):
        self.assertIn("Invalid session", self.cli("show", session="../../foreign", success=False).stderr)
        run = subprocess.run([sys.executable, str(SCRIPT), "--state-dir", "relative", "config"], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)

    def test_configuration_only_prints_reviewable_hooks_and_quotes_paths(self):
        self.state = self.root / "state with spaces and $literal"
        config = self.cli("config")
        self.assertEqual(set(config["hooks"]), {"SessionStart", "UserPromptSubmit", "SubagentStart", "Stop"})
        command = config["hooks"]["Stop"][0]["hooks"][0]["command"]
        run = subprocess.run(command, shell=True, input=json.dumps({"hook_event_name": "Stop", "cwd": str(self.cwd),
                                                                  "session_id": "inactive"}),
                             text=True, capture_output=True, timeout=10)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout), {})
        self.assertFalse(self.state.exists())

    def test_public_evidence_command_hashes_file_without_executing_filename(self):
        evidence = self.evidence(name="proof $(never-execute).txt")
        self.assertEqual(self.cli("evidence", evidence["path"]), [evidence])

    def canonical(self, name="task.md"):
        task = self.cli("show")
        values = []
        def strings(value):
            if isinstance(value, str):
                values.append(value)
            elif isinstance(value, dict):
                for item in value.values():
                    strings(item)
            elif isinstance(value, list):
                for item in value:
                    strings(item)
        strings({"intent": task["intent_id"], "request": task["original_request"], "body": task["body"]})
        path = self.cwd / name
        path.write_text("# Existing project task\n\n" + "\n\n".join(values) + "\n")
        return path

    def retire(self, record=None, success=True, **options):
        record = record or self.canonical()
        arguments = ["handoff", "--record", str(record), "--expected-revision",
                     str(options.get("revision", self.cli("show")["revision"])),
                     "--expected-record-sha256", options.get("sha256", hashlib.sha256(record.read_bytes()).hexdigest())]
        if options.get("workers_stopped"):
            arguments.append("--workers-stopped")
        return self.cli(*arguments, success=success)

    def test_handoff_removes_only_owned_state_and_preserves_canonical_proof(self):
        self.hook()
        body = self.completed()
        self.update(body)
        proof = Path(body["obligations"][0]["evidence"][0]["path"])
        record = self.canonical()
        before = record.read_bytes(), proof.read_bytes()
        self.assertEqual(self.retire(record)["handoff"], "retired")
        self.assertEqual(list(self.state.iterdir()), [self.state / "bindings.json"])
        self.assertEqual(json.loads((self.state / "bindings.json").read_text()), {})
        self.assertEqual((record.read_bytes(), proof.read_bytes()), before)
        self.assertEqual(self.hook(kind="Stop"), {})
        self.assertEqual(self.cli("handoff", "--record", str(record), "--expected-revision", "2",
                                  "--expected-record-sha256", hashlib.sha256(record.read_bytes()).hexdigest())["handoff"],
                         "already absent")

    def test_handoff_rejects_stale_missing_changed_and_incomplete_canonical(self):
        self.hook()
        self.update(self.completed())
        record = self.canonical()
        before = self.state_path().read_bytes()
        self.assertIn("Stale", self.retire(record, success=False, revision=1).stderr)
        self.assertIn("changed", self.retire(record, success=False, sha256="0" * 64).stderr)
        record.write_text("Only a title")
        self.assertIn("retain", self.retire(record, success=False).stderr)
        self.assertEqual(self.state_path().read_bytes(), before)
        record.unlink()
        self.assertIn("No such", self.cli("handoff", "--record", str(record), "--expected-revision", "2",
                                          "--expected-record-sha256", "0" * 64, success=False).stderr)

    def test_handoff_requires_reconciliation_or_truthful_pause(self):
        self.hook()
        self.update(self.body())
        self.assertIn("truthful pause", self.retire(success=False).stderr)
        body = self.body(status="waiting")
        body["reason"] = "Need user review"
        self.update(body)
        record = self.canonical()
        self.hook(prompt="Correction still must be reconciled")
        self.assertIn("reconciled", self.retire(record, success=False).stderr)

    def test_evidence_inside_any_state_scope_blocks_handoff(self):
        self.hook()
        work = Path(self.cli("workdir")["path"])
        proof = work / "proof.txt"
        proof.write_text("Necessary retained evidence")
        body = self.completed()
        body["obligations"][0]["evidence"] = self.cli("evidence", str(proof))
        self.update(body)
        self.assertIn("inside scratch", self.retire(success=False, workers_stopped=True).stderr)
        self.assertTrue(proof.exists())

    def test_workdir_cleanup_requires_assertion_and_rejects_unknown_or_symlink_entries(self):
        self.hook()
        self.update(self.completed())
        work = Path(self.cli("workdir")["path"])
        (work / "nested").mkdir()
        (work / "nested" / "output.txt").write_text("Disposable result")
        self.assertIn("workers-stopped", self.retire(success=False).stderr)
        sentinel = self.cwd / "sentinel.txt"
        sentinel.write_text("Foreign data")
        link = work / "external"
        link.symlink_to(sentinel)
        self.assertIn("nonsymlink", self.retire(success=False, workers_stopped=True).stderr)
        self.assertEqual(sentinel.read_text(), "Foreign data")
        link.unlink()
        unknown = work.parent / "unknown.txt"
        unknown.write_text("Not registered scratch")
        self.assertIn("Unknown", self.retire(success=False, workers_stopped=True).stderr)
        unknown.unlink()
        self.retire(workers_stopped=True)
        self.assertFalse(work.exists())
        self.assertTrue(sentinel.exists())

    def test_new_intent_in_same_session_and_cross_session_resume_preserve_original(self):
        self.hook()
        first = self.cli("show")
        self.update(self.completed())
        record = self.canonical()
        self.retire(record)
        self.hook(prompt="$aapilot A distinct second task")
        second = self.cli("show")
        self.assertNotEqual(first["intent_id"], second["intent_id"])
        self.assertEqual(second["original_request"], "$aapilot A distinct second task")
        result = self.cli("resume", "--record", str(record), "--intent-id", first["intent_id"],
                          "--original-request", first["original_request"], session="resuming-session")
        resumed = self.cli("show", session="resuming-session")
        self.assertEqual(resumed["intent_id"], first["intent_id"])
        self.assertEqual(resumed["original_request"], first["original_request"])
        self.assertIsNone(resumed["body"])
        self.assertIn("entire canonical", result["context"])
        self.assertEqual(resumed["canonical"]["sha256"], hashlib.sha256(record.read_bytes()).hexdigest())
        self.assertNotEqual(resumed["original_request"], record.read_text())
        self.assertIn("active binding", self.cli("resume", "--record", str(record), "--intent-id", first["intent_id"],
                      "--original-request", first["original_request"], session="other", success=False).stderr)
        self.assertIn("before rebinding", self.cli("resume", "--record", str(record), "--intent-id", first["intent_id"],
                      "--original-request", first["original_request"], success=False).stderr)

    def test_resume_requires_exact_identity_request_and_exposes_selected_source_version(self):
        record = self.cwd / "existing.md"
        intent_id = "a" * 32
        record.write_text(intent_id + "\nOriginal request text\n")
        self.assertIn("verbatim", self.cli("resume", "--record", str(record), "--intent-id", intent_id,
                                          "--original-request", "different request", success=False).stderr)
        self.cli("resume", "--record", str(record), "--intent-id", intent_id,
                 "--original-request", "Original request text")
        record.write_text(record.read_text() + "Changed before reconstruction")
        self.assertIsNone(self.cli("show")["body"])
        self.assertNotEqual(self.cli("show")["canonical"]["sha256"], hashlib.sha256(record.read_bytes()).hexdigest())
        body = self.body(status="blocked")
        body["reason"] = "Canonical source changed; reread and reconcile it"
        self.update(body)
        self.assertEqual(self.cli("show")["body"]["status"], "blocked")

    def test_canonical_symlink_inside_state_and_foreign_task_ownership_are_rejected(self):
        self.hook()
        self.update(self.completed())
        record = self.canonical()
        link = self.cwd / "link.md"
        link.symlink_to(record)
        self.assertIn("nonsymlink", self.retire(link, success=False).stderr)
        inside = self.state / "canonical.md"
        inside.write_bytes(record.read_bytes())
        self.assertIn("outside scratch", self.retire(inside, success=False).stderr)
        task = self.cli("show")
        task["owner"] = "b" * 32
        self.state_path().write_text(json.dumps(task))
        self.assertIn("ownership", self.cli("show", success=False).stderr)

    def test_unsupported_development_records_are_preserved_and_block_completion(self):
        self.hook()
        self.update(self.completed())
        path = self.state_path()
        task = self.cli("show")
        task["version"] = 1
        for key in ("intent_id", "original_request", "owner"):
            del task[key]
        path.write_text(json.dumps(task))
        original = path.read_bytes()
        self.assertIn("Unsupported task record version", self.cli("show", success=False).stderr)
        self.assert_recovery_hook_failure_is_bounded("Unsupported task record version")
        record = self.cwd / "legacy.md"
        record.write_text("Preserve legacy data")
        self.assertIn("Unsupported task record version", self.cli(
            "handoff", "--record", str(record), "--expected-revision", str(task["revision"]),
            "--expected-record-sha256", hashlib.sha256(record.read_bytes()).hexdigest(), success=False).stderr)
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(record.read_text(), "Preserve legacy data")

    def test_update_accepts_stdin_without_caller_file(self):
        self.hook()
        self.cli("update", "--file", "-", payload={"expected_revision": 1, "body": self.body()})
        self.assertFalse((self.root / "update.json").exists())
        self.assertEqual(self.cli("show")["revision"], 2)

    def crash_before_task_replace(self, prompt):
        code = """import importlib.util, os, signal, sys
spec = importlib.util.spec_from_file_location('adapter', sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
replace = os.replace
def interrupt(source, destination):
    if str(destination).endswith('/task.json'):
        print('ready', flush=True)
        os.kill(os.getpid(), signal.SIGSTOP)
    return replace(source, destination)
os.replace = interrupt
sys.argv = [sys.argv[1], *sys.argv[2:]]
module.main()
"""
        event = {"hook_event_name": "UserPromptSubmit", "session_id": self.session,
                 "cwd": str(self.cwd), "turn_id": "killed-turn", "prompt": prompt}
        run = subprocess.Popen([sys.executable, "-c", code, str(SCRIPT), "--state-dir", str(self.state), "hook"],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            run.stdin.write(json.dumps(event))
            run.stdin.close()
            self.assertEqual(run.stdout.readline().strip(), "ready")
            run.kill()
            run.wait(timeout=5)
        finally:
            if run.poll() is None:
                run.kill()
                run.wait(timeout=5)
            run.stdout.close()
            run.stderr.close()

    def test_killed_first_capture_recovers_request_and_releases_kernel_lock(self):
        prompt = "$aapilot Preserve the only original request through a crash"
        self.crash_before_task_replace(prompt)
        self.assertEqual(len(list(self.state.glob("*/.task.pending"))), 1)
        # Deliberately truncate the interrupted first write: committed registration is authoritative.
        next(self.state.glob("*/.task.pending")).write_text("{")
        task = self.cli("show")
        self.assertEqual(task["original_request"], prompt)
        self.assertFalse(list(self.state.glob("*/.task.pending")))
        self.assertFalse(list(self.state.rglob("*.lock")))
        self.assertNotIn("initial", next(iter(json.loads((self.state / "bindings.json").read_text()).values())))

    def test_killed_replacement_preserves_prior_record_and_next_correction_succeeds(self):
        self.hook()
        original = self.cli("show")
        self.crash_before_task_replace("Correction interrupted before commit")
        self.assertEqual(self.cli("show"), original)
        self.hook(prompt="Correction replayed after crash")
        self.assertEqual(len(self.cli("show")["inputs"]), 2)
        self.assertFalse(list(self.state.glob("*/.task.pending")))

    def test_retirement_receipt_finishes_on_next_use_and_preserves_changed_destination(self):
        self.hook()
        self.update(self.completed())
        record = self.canonical()
        registry_path = self.state / "bindings.json"
        owners = json.loads(registry_path.read_text())
        entry = next(iter(owners.values()))
        entry["retiring"] = {"path": str(record), "sha256": hashlib.sha256(record.read_bytes()).hexdigest(), "revision": 2,
                             "evidence": self.cli("show")["body"]["obligations"][0]["evidence"]}
        registry_path.write_text(json.dumps(owners))
        before = record.read_text()
        record.write_text(before + "changed")
        self.assertIn("destination changed", self.cli("show", success=False).stderr)
        self.assertTrue(self.state_path().exists())
        record.write_text(before)
        self.assertEqual(self.hook(kind="Stop"), {})
        self.assertFalse(list(self.state.glob("*/task.json")))
        self.assertEqual(json.loads(registry_path.read_text()), {})

    def test_truthful_pause_can_handoff_stale_external_pending_history(self):
        self.hook()
        body = self.completed()
        proof = Path(body["obligations"][0]["evidence"][0]["path"])
        self.update(body)
        proof.unlink()
        body["status"] = "blocked"
        body["reason"] = "Prior external proof is missing; reverify before completion"
        body["obligations"][0]["status"] = "pending"
        self.update(body)
        record = self.canonical()
        self.assertEqual(self.retire(record)["handoff"], "retired")
        self.assertIn(str(proof), record.read_text())
        self.assertFalse(proof.exists())

    def test_retirement_recovery_rechecks_passed_proof_even_after_task_deleted(self):
        self.hook()
        self.update(self.completed())
        record = self.canonical()
        task = self.cli("show")
        proof = Path(task["body"]["obligations"][0]["evidence"][0]["path"])
        original = proof.read_bytes()
        owners_path = self.state / "bindings.json"
        owners = json.loads(owners_path.read_text())
        next(iter(owners.values()))["retiring"] = {
            "path": str(record), "sha256": hashlib.sha256(record.read_bytes()).hexdigest(),
            "revision": task["revision"], "evidence": task["body"]["obligations"][0]["evidence"]}
        owners_path.write_text(json.dumps(owners))
        self.state_path().unlink()
        proof.write_text("Changed after retirement receipt")
        self.assertIn("Evidence changed", self.cli("show", success=False).stderr)
        self.assertTrue(list(self.state.glob("*/")))
        proof.write_bytes(original)
        self.assertEqual(self.hook(kind="Stop"), {})
        self.assertEqual(json.loads(owners_path.read_text()), {})

    def test_kill_during_exact_cleanup_finishes_on_next_hook(self):
        self.hook()
        self.update(self.completed())
        work = Path(self.cli("workdir")["path"])
        (work / "output.txt").write_text("Disposable temporary output")
        record = self.canonical()
        task = self.cli("show")
        code = """import importlib.util, os, signal, sys
spec = importlib.util.spec_from_file_location('adapter', sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rmdir = module.Path.rmdir
def interrupt(path, *args, **kwargs):
    if str(path).endswith('/work'):
        print('ready', flush=True)
        os.kill(os.getpid(), signal.SIGSTOP)
    return rmdir(path, *args, **kwargs)
module.Path.rmdir = interrupt
sys.argv = [sys.argv[1], *sys.argv[2:]]
module.main()
"""
        command = [sys.executable, "-c", code, str(SCRIPT), "--state-dir", str(self.state),
                   "--cwd", str(self.cwd), "--session", self.session, "handoff", "--record", str(record),
                   "--expected-revision", str(task["revision"]), "--expected-record-sha256",
                   hashlib.sha256(record.read_bytes()).hexdigest(), "--workers-stopped"]
        run = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            self.assertEqual(run.stdout.readline().strip(), "ready")
            run.kill()
            run.wait(timeout=5)
        finally:
            if run.poll() is None:
                run.kill()
                run.wait(timeout=5)
            run.stdout.close()
            run.stderr.close()
        self.assertTrue(work.exists())
        self.assertIn("retiring", next(iter(json.loads((self.state / "bindings.json").read_text()).values())))
        self.assertEqual(self.hook(kind="Stop"), {})
        self.assertEqual(list(self.state.iterdir()), [self.state / "bindings.json"])
        self.assertTrue(record.exists())

    def assert_recovery_hook_failure_is_bounded(self, message):
        first = self.hook(kind="Stop")
        self.assertEqual(first["decision"], "block")
        self.assertIn(message, first["reason"])
        second = self.hook(kind="Stop", stop_hook_active=True)
        self.assertIs(second["continue"], False)
        self.assertIn("incomplete", second["stopReason"])
        self.assertIn(message, second["systemMessage"])
        warning = self.hook(kind="SessionStart")
        self.assertIn(message, warning["systemMessage"])
        self.assertIn("unverified", warning["systemMessage"])
        self.assertIn(message, self.cli("show", success=False).stderr)

    def test_corrupt_bindings_return_bounded_stop_json_and_recovery_warning(self):
        self.hook()
        task_path = self.state_path()
        original = task_path.read_bytes()
        registry_path = self.state / "bindings.json"
        registry_path.write_text("{")
        self.assert_recovery_hook_failure_is_bounded("Expecting property name")
        self.assertEqual(registry_path.read_text(), "{")
        self.assertEqual(task_path.read_bytes(), original)

    def test_missing_registered_directory_returns_bounded_stop_json_and_recovery_warning(self):
        self.hook()
        task_path = self.state_path()
        registry_path = self.state / "bindings.json"
        original = registry_path.read_bytes()
        task_path.unlink()
        task_path.parent.rmdir()
        self.assert_recovery_hook_failure_is_bounded("Registered task is missing")
        self.assertEqual(registry_path.read_bytes(), original)
        self.assertFalse(task_path.parent.exists())

    def test_100_handed_off_intents_retain_only_fixed_metadata(self):
        proof = self.evidence()
        for number in range(100):
            # Ten sessions include repeated same-session intents and fresh-session reuse.
            self.session = f"session-{number % 10}"
            self.hook(prompt=f"$aapilot Logical intent {number}")
            body = self.body(status="complete")
            body["obligations"][0].update(status="passed", evidence=[proof])
            body["reconciliation"] = "Completed the original intent with retained sources"
            self.cli("update", "--file", "-", payload={"expected_revision": 1, "body": body})
            self.retire(self.canonical(f"task-{number}.md"))
        self.assertEqual(list(self.state.iterdir()), [self.state / "bindings.json"])
        self.assertEqual((self.state / "bindings.json").read_text(), "{}\n")
        self.assertEqual(len(list(self.cwd.glob("task-*.md"))), 100)


if __name__ == "__main__":
    unittest.main()
