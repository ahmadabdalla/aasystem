# Verification contract

For retained implementation, connect the request and agreed expectations to the actual artifact, observed checks, findings and delivery status. Reuse the project's task, PR or evidence format. Research and design retain their own sources and rationale.

The [execution contract](execution.md) owns authority, delegation, human checkpoints and verification exceptions. [Engineering Verification](engineering-verification.md) owns independent assessment. These instructions and local checks do not authenticate agents or humans, intercept tool use or establish host-enforced acceptance.

## Working loop

1. Establish expected results and the project checks before editing. In the existing brief, map required outcomes to checks and set a total acceptance-verification time limit, including diagnosis, repairs and rechecks. The owner chooses it within user limits; carry remaining allowance across handoffs and retries.
2. Implement and run development checks within settled scope.
3. Pause source editing and give a fresh noneditor verifier the combined artifact, requirements and runnable checks.
4. Preserve findings; distinguish product, harness, environment and unsettled-expectation failures, keeping unknown causes explicit. For each correction, name the failure, changed inputs and checks needed; retain earlier proof only with an explicit unaffected-input/outcome rationale. Include dependent integration checks when shared production inputs change.
5. The owner inspects the work and evidence, resolves required decisions and owned resources, and presents it at the requested delivery boundary. Agent completion does not replace human review or authorise a commit.

If a failure recurs after correction, pause reruns and reassess shared causes and related test assumptions. Retry only with new evidence or a materially different hypothesis and a check that distinguishes it. Once required outcomes have current passing proof and material findings are resolved, finish without unrelated checks. Otherwise, at the total limit stop verification and repairs; report incomplete scope, retained failures, consumed allowance and the prerequisite for resuming. Do not extend or reset the limit without human agreement. Update the brief with changes and evidence links rather than repeating settled context.

## Local execution

Use the current checkout for sequential work. Use one task worktree when concurrent edits or separation require it; reuse it through correction rounds. Git worktrees share repository storage but have separate checked-out files. A new worktree does not include another checkout's uncommitted or ignored files; provide required inputs deliberately. Neither a worktree nor a copied directory is a process sandbox.

Implementer and verifier take turns in a shared working directory. Identify and stop other source writers before verification; unknown activity leaves the result inconclusive. Separate directories do not isolate shared databases, ports or external services: allocate owned fixtures or run those checks serially.

Additional execution copies require a concrete check that cannot use the working directory. Before creating them, identify complete required inputs, storage cost and cleanup ownership. Do not default to full archives, changed-files-only proof or copying dependencies just because they exist. Reuse project-native isolation facilities where available.

Keep test data and disposable output separate from source and retained evidence. Stop only owned processes. Delete only resources whose ownership and boundary are established; uncertainty means leave them and report it. Never use recursive checkout deletion or forced worktree removal as routine cleanup. A worktree containing pending review changes remains a deliverable.

## Tested identity

Record which inputs were checked, including relevant uncommitted/new files, verifier/configuration and required ignored or external inputs. A branch name or HEAD commit alone is insufficient for dirty work. The owner and verifier remain responsible for complete semantic input selection and the actual runtime instance.

Use a project identity check when adequate. Otherwise the read-only [input identity helper](../scripts/input_identity.py) needs Python 3.10+ and Git:

```sh
python3 /installed/skills/pilot/scripts/input_identity.py --root /project --required /project/local-config.json > /outside/project/before.json
# Run verification with source editing paused.
python3 /installed/skills/pilot/scripts/input_identity.py --root /project --required /project/local-config.json --check /outside/project/before.json
```

It streams hashes of Git-tracked working-tree files and nonignored new files, plus explicitly required files; it creates no source copies. Keep its output outside selected inputs. Required directories, symlinks, submodules and special files need a project-specific identity procedure; the helper refuses them rather than silently omitting their contents.

Check identity before and after verification and again at delivery. Relevant changes invalidate affected results; reverify instead of selecting an older pass. Fingerprints detect endpoint differences, not transient writes or malicious interference. Tests that intentionally generate source need an explicit preparation/reset procedure before the checked interval.

A fingerprint identifies content but cannot reconstruct it. Preserve a Git reference and necessary patch/fixtures only when replay is required; do not archive the repository merely to keep an identity.

## Result and retention

Keep the request/authority, expected outcomes, tested identity and environment, actual verifier, commands/observations, pass/fail/unverified results, material findings/dispositions and limitations in the existing result record. Link original evidence rather than duplicating it. No fixed report headings or metadata envelope are required.

Required missing or failing checks leave the work incomplete. An owner disposition cannot turn a failed observation into a pass; expose any accepted limitation with its actual authority. Scope review and runtime observations are distinct: review completion is not proof that every behaviour works.

Retain original findings and useful evidence through human review or investigation. Follow the [project evidence lifecycle](../../bootstrap-verification/references/project-contract.md#evidence-and-retention) for disposal and durable references. Keep only artifacts with a stated future purpose beyond that boundary.
