# Optional local Codex checkpoints

This adapter keeps a Pilot task's record across Codex sessions and blocks a stop until the record's completion checks pass. The [continuity procedure](../../references/task-continuity.md) owns the brief and recovery. Pilot and its execution contract own routing, human decisions and proof.

## One-time setup

Requires Python 3.10+, a local POSIX filesystem with `flock`, and Codex command hooks for `SessionStart`, `UserPromptSubmit`, `SubagentStart` and `Stop` ([hook reference](https://learn.chatgpt.com/docs/hooks)). Windows, network filesystems, several machines and hosted ChatGPT are unsupported.

1. Pick absolute paths: a stable library install, and a state directory you own outside any source tree. If Codex runs sandboxed, let it write to the state directory.
2. Generate the hooks. This prints JSON and changes nothing:

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state config > /local/pilot-hooks.json
   ```

3. Merge its `hooks` entries into `~/.codex/hooks.json` or a trusted project's `.codex/hooks.json`, then review and trust them in `/hooks`. If a path or definition changes, regenerate and review again. Installing the skills doesn't enable the hooks.
4. Run one helper version per state directory. Stop older writers before upgrading. If you're upgrading from aapilot, follow the [migration steps](../../../../docs/ops/releasing.md#upgrade-from-aapilot-to-pilot) and keep the existing state directory.
5. Start a task with `$aasystem:pilot <outcome>`, or `$pilot <outcome>` for a direct install, at the very start of the prompt. Any other form gets the portable instructions only. Check that the events actually arrive.

## Coordinator protocol

What the hooks do:

- `UserPromptSubmit` creates the record: an `intent_id` and the exact `original_request`, bound to the session and working directory. Every later root prompt, including another `$pilot`, is appended to `inputs`, bumps the revision, sets status to `active` and clears `reconciliation`. To start independent work, hand off first.
- `SessionStart` (startup, resume, after compaction) and `SubagentStart` return the record path, the CLI prefix and a summary. The host may cut the summary short, so read the full record with `show` before dependent work. A subagent gets the record only if the event carries the parent's session ID and the same working directory. A worker in another worktree needs the record path passed to it.
- Only the coordinator updates the record. Workers return results to it.

Each increment:

1. Read the record. `show` returns `version`, `intent_id`, `original_request`, the binding, `revision`, `inputs` (`text`, `turn_id`) and the body:

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state --session SESSION --cwd /project show
   ```

2. Write the full body with the latest revision, on stdin (`update --file -`). For `--file PATH`, put the file in the directory `workdir` returns. Example for a research task:

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

   | Field | Rule |
   | --- | --- |
   | `acknowledged_inputs` | Must equal the number of `inputs`. It says you reconciled them all. |
   | `effort`, `route` | Size S, M or L with a reason; `route` lists at least one procedure. |
   | `obligations` | At least one. Each has a unique `id`, `description`, `stage`, `status` (`pending` or `passed`) and `evidence`. A passed one needs evidence. Keep every obligation until the end. |
   | `findings` | `description`, `material`, `resolved` (booleans) and `return_checkpoint`. An unresolved material finding blocks every check. A deferred minor one needs a `return_checkpoint`. |
   | `status` | `active`, `waiting`, `blocked`, `complete` or `cancelled`. A pause or cancellation needs a `reason`. |
   | `reconciliation` | Needed for `complete`: how the result meets the original request. Research and design need their own proof, not an implementation. |

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state --session SESSION --cwd /project \
     update --file -
   ```

   A failed update leaves the record unchanged. If the revision is stale, read again. Setting `complete` runs the final check at once.

3. Reference evidence. This prints `{"path", "sha256"}` for each nonempty regular file (not a symlink):

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state evidence /local/proof/findings.md
   ```

   Every update, checkpoint and handoff rehashes passed evidence. If a file changed, set the obligation back to `pending`, record the blocker and verify again. A matching hash says the file is unchanged, not that the work is right; use the [tested identity procedure](../../references/verification-contract.md#tested-identity).

4. Before moving to the next increment, check the current one:

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state --session SESSION --cwd /project \
     checkpoint --expected-revision 2
   ```

   It passes when every input is acknowledged, no material finding is open, and at least one obligation has `stage` equal to `current_increment` and all of those have passed. It changes nothing. Then update `current_increment`; completion checks every obligation. Hooks don't see planning or edits, so you must call checkpoints yourself.

## Handoff and resume

Hand off once status is `complete`, `waiting`, `blocked` or `cancelled`; an active task can't hand off. A paused or cancelled task can stop without a handoff, but its state stays until you hand it off.

1. Pick an existing local UTF-8 task file in the project's format: nonempty, a regular file you own with one hard link, outside the state directory. If there is none you may write to, keep the state and say mechanical handoff is unavailable.
2. Write these strings into it unchanged: `intent_id`, `original_request`, every string in the body (list items included), each obligation's `id`, `description`, `stage`, `status` and evidence `path` and `sha256`, and each finding's `description` and `return_checkpoint`. `handoff` checks each appears verbatim, so don't wrap or reformat them.
3. Move evidence outside the state directory and refresh its references. Evidence inside the state directory blocks handoff, and so does any other file in the task folder besides `task.json` and `work/`.
4. Stop or reconcile anything using `workdir`. Read the task file back, hash it with `evidence`, and don't touch it again before:

   ```sh
   python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
     --state-dir /local/pilot-state --session SESSION --cwd /project \
     handoff --record /project/existing-task.md --expected-revision N \
     --expected-record-sha256 HASH --workers-stopped
   ```

   `--workers-stopped` is required if a work directory exists. It is your word that its users stopped; the helper can't check. Success removes only this task's state. The task file and evidence stay.

To resume in a new session, the intent must be handed off first:

```sh
python3 /installed/aasystem/skills/pilot/scripts/orchestration.py \
  --state-dir /local/pilot-state --session NEW_SESSION --cwd /project \
  resume --record /project/existing-task.md --intent-id INTENT_ID \
  --original-request 'The exact original request'
```

Resume keeps the intent ID with an empty body. Read the whole task file and rebuild the body before dependent work; reconcile any source changes. Only version 2 records work; older ones are refused and left in place.

## Stop behavior and limits

- Stop asks for one more turn if the body is missing, inputs are unreconciled, the task is still `active`, or it is `complete` but fails the final check or hasn't been handed off. If the gap remains on the next stop, Stop ends with an incomplete warning.
- A waiting, blocked or cancelled task stops with a "not complete" message.
- Sessions without a task are ignored. If a task folder has a missing or corrupt record, it's reported incomplete, not recreated.
- Malformed events, missing Python or state, untrusted hooks, host errors and timeouts can stop enforcement. Hooks don't sandbox anything or prove approval, review or that the work is right.

To run the helper's tests from the library root:

```sh
python3 -m unittest discover -s tests -p test_orchestration.py
```

They cover the CLI and state handling only. Real host callbacks need checking in Codex.

## Storage and retention

```text
state root/
  bindings.json                 active ownership; initial records and handoff receipts until they finish
  <sha256(cwd, session)>/
    task.json                   current intent and body
    work/                       optional disposable output

handoff -> task file and evidence outside the state root
        -> removes this task's folder and binding
nothing active -> bindings.json only (empty: 3 bytes)
```

There are no event logs, revision archives or history of finished tasks, and no size cap. Inputs and evidence grow while a task is active. Put disposable files, including plugin-directed agent files, in `workdir`. Keep evidence a review needs outside the state root under the [evidence lifecycle](../../../bootstrap-verification/references/project-contract.md#evidence-and-retention).

Interrupted writes and handoffs are recovered on the next helper run. If ownership or evidence is unclear, the helper keeps the state and reports the gap to that task. A failure in another task doesn't block this one, but a corrupt `bindings.json` blocks every task. Nothing cleans up while no helper runs: there's no sweep, daemon or `SessionEnd` handler. Task files, evidence, generated config and Codex transcripts stay with their owners.
