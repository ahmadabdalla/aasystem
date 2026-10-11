# Independent requests

Each request starts from its own copy of `notes-project/`. Use the assigned skill snapshot and actual CLI, confining edits and commands to that project and its owned temporary resources. Do not publish, contact others or delegate nested work. Make reasonable assumptions; ask only for genuinely missing material information and stop if asking. Retain your actual output and a concise handoff in `OUTCOME.md` in the parent case directory, outside the project.

## Creation change

Use bootstrap-verification from the assigned snapshot to adopt the existing verifier where needed. Change single-note creation to trim surrounding whitespace before storing the title, preserving increasing IDs and fresh-process readback. Stay within this change; blank-title validation is a separate known bug. Verify the changed behavior, then repeat the same verification on unchanged source. The evidence is for this task's local review; the task owner will dispose of it after that review. Update operating instructions where necessary and report observations and remaining gaps.

## Failed verification

Use maintain-verification from the assigned snapshot for a task-scoped audit of blank-title rejection and its creation/readback dependency. The contract requires rejecting a blank title without changing the store. Investigate using the actual CLI and report the result; product fixes are outside this audit. The defect investigation remains open after delivery, with the task owner responsible for its evidence. Make the existing verifier usable if needed and report covered and unverified paths.

## Migration evidence

Use bootstrap-verification from the assigned snapshot to adopt the existing verifier for the v1-to-v2 store migration. Exercise a representative store containing multiple IDs and labels; establish that migration preserves IDs/text as titles and that another invocation reads the migrated data. The reviewer needs a durable before/after trail in another checkout to approve the migration approach. Use the project's existing `docs/migrations/` location for that selected evidence and account, keeping ordinary driving output available through review under the task owner's responsibility. Review the existing tracked legacy proof and its inbound link; propose any necessary migration without removing it during this exercise. This is a verification task, not permission to migrate a real user's data.
