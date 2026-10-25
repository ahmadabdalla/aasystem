# Optional local Codex checkpoints

This adapter restores task context and checks recorded completion requirements.
The [continuity procedure](../../references/task-continuity.md) owns sizing,
routing, human decisions and proof; the [adapter boundary](../README.md) owns
future integrations.

Requires Python 3.10+, a local POSIX filesystem supporting `flock`, and local
Codex command hooks for `SessionStart`, `UserPromptSubmit`, `SubagentStart` and
`Stop`. Commands use POSIX shell quoting. Run only one helper version per state
root; stop older writers before upgrading. Windows, network filesystems,
cross-machine coordination and automatic hosted ChatGPT/Work integration are
unsupported. See the [Codex hook reference](https://learn.chatgpt.com/docs/hooks).

## One-time setup

Choose absolute paths: a stable library installation and an exclusively owned,
persistent state directory outside maintained source. Permit coordinator writes
and session reads there. Generate configuration:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state config > /local/aapilot-hooks.json
```

This prints JSON without installing hooks or creating task state. Review and
merge its `hooks` entries into your existing `~/.codex/hooks.json` or trusted
project's `.codex/hooks.json`. Review/trust the exact definitions through `/hooks`;
regenerate and review after path or definition changes. Shared plugin manifests
do not register this adapter; portable skill installation does not activate it.

Start with `$aasystem:aapilot <outcome>` or `$aapilot <outcome>` for direct installs.
Activation requires either spelling at the raw prompt's start after optional
whitespace. Quoted examples and other invocation forms use portable instructions
unless the host supplies that explicit prompt. Verify actual event delivery.

## Captured request and ownership

`UserPromptSubmit` creates an `intent_id` and immutable `original_request`, bound
temporarily to the root session and working directory. Later inputs append
verbatim and clear completion, requiring owner reconciliation. Identical
turn-ID/text replays are idempotent. No reliable sender marker distinguishes Stop
continuations, so prompt text never filters possible corrections.

Another explicit invocation remains input to the current intent. Hand off before
switching to independent work; the next invocation can then create a new intent.
The coordinator alone updates state; workers return results. `SubagentStart`
restores the parent record when supplied its documented parent session ID and
same working directory. Workers in another worktree need an explicit accessible
record path; the adapter does not search other workspaces.

`SessionStart` supplies startup/resume/post-compaction context. Hooks return the
record path, CLI prefix and a bounded summary: read the full record before
dependent work. Captured prompts, filenames and evidence are never executed.

### Storage and retention

```text
state root/
  bindings.json                 active ownership / interrupted handoff receipts
  <sha256(cwd, session)>/
    task.json                   current intent and reconciled brief
    work/                       optional registered disposable output

checked handoff -> existing task file + necessary proof outside state root
                -> remove owned task/work folder and binding
all intents retired -> bindings.json only (empty: 3 bytes)
```

There are no per-event logs, revision archives or retired-intent history.
Active inputs and review proof can grow; there is no hard cap. Use `workdir` for
disposable updates/intermediates, including plugin-directed agent files. Stop or
reconcile scratch users before retirement. Retain necessary proof outside the
entire state root under the [evidence lifecycle](../../../bootstrap-verification/references/project-contract.md#evidence-and-retention).

The coordinator invokes handoff. Kernel directory locking releases on process
exit; fixed pending replacements and ownership receipts support next-use recovery
of committed initial writes or verified interrupted retirement. Uncertain
ownership, canonical proof or filesystem safety preserves state and reports a
gap to the affected task. Recovery failures in other tasks do not block the
current hook or CLI command; safe leftovers still recover on next use. A malformed
shared ownership index remains a root-wide failure. There is no age/prefix
sweep, daemon, `SessionEnd` handler or cleanup while
nothing runs. Task records, retained proof, generated configuration and native
host transcripts/caches remain with their owners; added host context still counts
toward the plugin's footprint.

## Coordinator protocol

Use the hook-provided session, working directory and CLI prefix. `show` returns
`version`, `intent_id`, `original_request`, session binding, `cwd`, `revision`,
verbatim `inputs` (`text`, `turn_id`) and the agent-owned body:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state --session SESSION --cwd /project show
```

Prepare an update with the latest `expected_revision` and full body. This research
example selects its own route and obligations:

```json
{
  "expected_revision": 1,
  "body": {
    "acknowledged_inputs": 1,
    "outcome": "Explain the importer using observed sources and limits",
    "constraints": ["Do not edit product files"],
    "decisions": ["User requested findings only"],
    "effort": {"size": "S", "reason": "One bounded, understood investigation"},
    "route": ["investigation"],
    "boundary": "Supported findings; no implementation",
    "current_increment": "research",
    "next_action": "Trace the import entry point",
    "obligations": [
      {
        "id": "import-findings",
        "description": "Explain actual import behavior with sources and limits",
        "stage": "research",
        "status": "pending",
        "evidence": []
      }
    ],
    "findings": [],
    "status": "active",
    "reason": "",
    "reconciliation": ""
  }
}
```

| Field | Required meaning/check |
| --- | --- |
| `acknowledged_inputs` | Count of **all** current inputs reconciled by the owner; an assertion, not authenticated understanding. |
| `effort`, `route` | Existing S/M/L assessment and task-selected procedures. |
| `obligations` | Unique `id`, expected `description`, increment `stage`, `status` (`pending`/`passed`) and `evidence`. Retain required obligations through final reconciliation. |
| `findings` | `description`, boolean `material`/`resolved`, string `return_checkpoint`. Unresolved material findings block successful checks; deferred minor findings need a return checkpoint. |
| `status` | `active`, `waiting`, `blocked`, `complete` or `cancelled`. Pauses/cancellation require `reason` and retain `next_action`. |
| `reconciliation` | For completion: compare with the original request, acknowledge all inputs, pass all obligations with matching proof and resolve material findings. Research/design need their own proof, not implementation. |

Send the JSON on stdin with the same prefix:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state --session SESSION --cwd /project \
  update --file -
```

For `update --file PATH`, obtain the directory with `workdir` and reuse one file.
Failed updates leave prior state intact;
malformed events are rejected before writing. Reread after revision conflicts.

Generate references for nonempty regular nonsymlink evidence files:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state evidence /local/proof/findings.md
```

References use `{"path": "/absolute/file", "sha256": "64 lowercase hex digits"}`.
Updates, checkpoints and completion recheck passed evidence, including during
pauses. If stale/missing, retain the obligation, reset it to `pending`, record the
blocker and reverify before passing it again. Historical pending references may
remain. File hashes cannot prove source/runtime freshness, sufficient obligations,
independent review or semantic correctness; use the [tested identity procedure](../../references/verification-contract.md#tested-identity).

Before advancing an increment, reread and check the current revision:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state --session SESSION --cwd /project \
  checkpoint --expected-revision 2
```

This checks obligations matching `current_increment`, returns the revision and
changes no state. Future stages may remain pending. Update to select the next
increment while retaining earlier obligations; completion checks them all.
The coordinator must call checkpoints; hooks do not intercept internal planning
or edits. A populated record or nonempty evidence file alone does not prove work.

## Handoff and resume

Use an existing authorized, stable local UTF-8 task file in its project format.
It must be nonempty, owned by the current user, regular/nonsymlink, have one hard
link and sit outside the state root. The helper reads it without writing another
archive or accepting remote PR URLs. If unavailable, retain recoverable state and
disclose the missing mechanical handoff capability.

For a completed or truthfully paused intent:

1. Reconcile inputs and update the body. Persist intent ID, exact original request,
   outcome, constraints, decisions/corrections, sizing/route, boundary, increment,
   status, next action, obligations, findings and necessary evidence references in
   the task file. Exact retained strings are checked; owner/verifier judge meaning.
   A full transcript is unnecessary.
2. Retain proof outside the state root and refresh references/hashes. Any reference
   inside disposable state blocks handoff; passed evidence must still match.
3. Stop/reconcile scratch users, read the task file back, get its hash with
   `evidence`, then run:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state --session SESSION --cwd /project \
  handoff --record /project/existing-task.md --expected-revision N \
  --expected-record-sha256 HASH --workers-stopped
```

`--workers-stopped` is required if a work area exists. It is the coordinator's
assertion that scratch users have stopped or been reconciled; the helper does
not discover detached processes. Locking serializes helper operations only.
Unknown files, symlinks, foreign ownership, stale revisions or changed required
text/proof block retirement. Success removes only registered disposable scope;
the task file and proof remain unchanged.

In the receiving session, resume with the record's ID and exact original request:

```sh
python3 /installed/aasystem/skills/aapilot/scripts/orchestration.py \
  --state-dir /local/aapilot-state --session NEW_SESSION --cwd /project \
  resume --record /project/existing-task.md --intent-id INTENT_ID \
  --original-request 'The exact original request'
```

Resume preserves identity in a new binding but leaves the body unset. Read the
entire record and reconstruct decisions, obligations and next action before
dependent work. It does not parse project prose; the captured canonical hash is
selected-version metadata, not continuing semantic proof. Reconcile source changes.

Only the current version 2 format is supported. Older development records are
rejected and preserved; no compatibility reader or automatic migration is shipped.

## Stop behavior and limits

Version 2 completion requires checked handoff before closing. Missing body/sizing,
corrupt state, unreconciled inputs, pending obligations, missing reconciliation or
stale evidence requests one corrective continuation. If `stop_hook_active` is
already true and the gap remains, Stop ends with an explicit incomplete warning.
Waiting/blocked/cancelled states may stop truthfully with a “not complete” warning.
No endless retries or conversion of gaps into passes.

Inactive sessions are no-ops. A missing/corrupt record in an existing task folder
is incomplete, not recreated over lost intent. Malformed events, unavailable
Python/state, untrusted/disabled hooks, host errors/timeouts and unsupported events
can prevent enforcement. Hooks neither sandbox processes nor authenticate approval,
reviewers or semantic fulfillment.

Run CLI/event regression checks from the library root:

```sh
python3 -m unittest discover -s tests -p test_orchestration.py
```

These prove their exercised subprocess/state boundary. Actual host callbacks,
skill discovery and specialist composition require separate native observation.
