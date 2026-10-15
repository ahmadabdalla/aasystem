# Bounded autonomous work — experimental v0

Use this procedure when the user explicitly requests bounded autonomous work or the bounded-autonomy PoC. Select the existing task procedure first; it retains phase ownership and scope. A directly invoked specialist owns this same loop within its domain, without an extra Aapilot coordinator. Architect remains design-only. Ordinary tasks retain their existing route, and a plan-only request ends before implementation.

The [execution contract](execution.md) owns delegation, review context, independent production verification and completion. This reference owns the experimental receipt protocol used alongside those rules. The [decision-context principle](../../principle-preserve-decision-context/SKILL.md) applies: preserve the information a receiving owner needs, using references only when it can retrieve them.

## Operating loop

```text
Human: outcome, authority and checkpoints
                  |
                  v
       Existing task / domain owner
                  |
        bounded native assignments
                  |
                  v
          inspect returned work <------------------+
                  |                                |
                  v                                |
       current scoped / independent proof          |
                  |                                |
                  +-- fail --> authorized repair --+
                  |
            owner acceptance
                  |
                  v
       Human: result + evidence + limits

Any required checkpoint -> decision package -> HUMAN
                         stop and wait -> resume / recheck

Shared receipt helper records and checks this loop.
Host tools execute work; the owner judges its meaning.
```

1. **Frame one retrievable brief.** Carry the objective, authoritative requirements and their status, accepted decisions, constraints and exclusions, applicable procedures/principles, expected outputs, next action, proof obligations and review checkpoints. Inspect observable unknowns. Record the actual host/delegation/access limits. Choose literal declared action names and resource IDs for this assignment; they describe authority and do not configure host permissions.
2. **Initialize one run.** Resolve [work_receipts.py](../scripts/work_receipts.py) from the loaded skill tree and use Python 3.10+ with only its standard library. Keep brief, state, reports, environment descriptor, snapshots and run evidence outside the installed skill tree/cache. Follow project [evidence conventions](../../bootstrap-verification/references/project-contract.md#evidence-and-retention). One owner writes the state; workers return artifacts and reports for that owner to import.
3. **Record and dispatch bounded work.** Apply an `assign` event before native dispatch. Give each child its actual accessible brief, procedure, source inputs, authority, write ownership, expected outputs and proof method. Record actual worker/host assignment identity on return. Nested dispatches and fresh repair attempts consume the same root budget. A failed launch consumes its allocation; record its outcome rather than retrying invisibly. Follow existing invocation restrictions; the receipt does not invoke a skill or worker.
4. **Inspect returns and current proof.** Import each `returned` report. Inspect the actual artifact; arrival is not acceptance. Use `snapshot` for the target's local input identity, then assign the appropriate fresh review/verifier. For production, the separate verifier materializes and checks a writable test workspace using the snapshot recipe below, exercises the actual project recipe and checks effects. Import its `verification` report. Missing access, failed checks, exposed review context or stale inputs leave the relevant gate unmet.
5. **Repair within authority.** Assign a fresh bounded correction naming the work it supersedes; preserve failed evidence. A replacement must keep the original parent, remain within its action/resource scope, cover its claims and retain its proof strength. Unrelated claimless work cannot waive a required obligation, and replacement cannot bypass uncertain effects. Repeat affected independent proof against the current combined artifact. The helper rejects widening, exhausted dispatches and stale evidence; the owner remains responsible for semantic scope, real freshness and evidence completeness.
6. **Return human decisions and resume.** At an applicable checkpoint, record a package containing the concrete artifact, options, consequences, recommendation and exact decision sought; present it and stop and wait. Use native tools to stop or inspect already running work. Resume only from actual matching human input, retaining approved decisions/artifacts and consumed budget. The helper checks response structure, not authenticity or authority. V0 invalidates all current proof on resume; recheck it under the resumed brief. Resume cannot widen grants, reset/increase the budget or extend the deadline; changed root identity, resources, source or environment require a new run.
7. **Reconcile interruptions before retry.** Record uncertain effects with `interrupted`. Inspect processes, partial files and side effects through real host tools. Import `reconciled` observations; unknown outcomes remain blocked, including retries under a new task ID on affected resources. Cancellation neither reverses effects nor refunds work. Do not infer safe retry from silence or session closure.
8. **Accept explicitly.** The owner inspects current evidence and meaning, applies `accept` with rationale and inspected evidence references, then reports the result, proof and limits. Follow the baseline completion and canonical-record rules. A structural success alone cannot establish semantic correctness.

## Commands and receipts

The helper offers four commands. Read [the installed helper's](../scripts/work_receipts.py) `--help` for its JSON field contract and each command's `--help` for arguments. After creating the chosen evidence directory, replace these two example paths with the actual complete installed skill tree and evidence directory:

```sh
INSTALLED_SKILLS="$(cd "/absolute/path/to/installed/skills" && pwd -P)"
HELPER="$INSTALLED_SKILLS/aapilot/scripts/work_receipts.py"
RUN="$(cd "/absolute/path/to/run-evidence" && pwd -P)"
mkdir -p "$RUN/inputs" "$RUN/artifacts" "$RUN/runtime"
```

All helper paths must be absolute physical paths, including paths inside JSON. Resolve aliases before recording them: macOS `/tmp` and `/var` usually resolve under `/private`, and passing the alias itself rejects because an ancestor is a symlink. `pwd -P` resolves an existing directory; use its result when constructing child paths. Do not supply symlinked files or directory ancestors.

Use this layout outside the installed skill tree/cache:

```text
RUN/
  inputs/     brief.json, requirements, authority, environment.json, handoff inputs
  artifacts/  design or implementation outputs needed by later assignments
  runtime/    state.json, events, reports, execution evidence, snapshots, test workspaces
```

Put immutable required references and child assignment inputs outside `runtime/`; the state-file parent is automatically excluded from source identity. Mutable run records belong inside it. Prepare `inputs/brief.json` and `runtime/assign.json` using the fields below, then run:

```sh
python3 "$HELPER" init --brief "$RUN/inputs/brief.json" --state "$RUN/runtime/state.json"
python3 "$HELPER" apply --state "$RUN/runtime/state.json" --event "$RUN/runtime/assign.json"
python3 "$HELPER" snapshot --state "$RUN/runtime/state.json" --task design --out "$RUN/runtime/input-1"
python3 "$HELPER" status --state "$RUN/runtime/state.json"
```

Here `assign.json` creates the child ID `design`; the owner separately dispatches its real worker with native host tools. Assign the verifier before taking its proof snapshot so its procedure and inputs join the tested identity. The helper never launches that worker. One owner imports returned files and writes state.

`init` creates versioned run state from the root brief. `apply` validates/imports one event and updates state atomically under a local exclusive lock and expected revision. A rejection exits nonzero without replacing prior state. `snapshot` records copied, hashed inputs for proof and returns the manifest path and identity without advancing the state revision. Its output must be a new directory below the state-file parent. `status` exposes recorded/historical acceptance versus current eligibility, remaining dispatches, checkpoints, unsettled work, uncertain effects and missing/stale evidence. Concurrent owners are unsupported; inspect stale locks before recovery rather than blindly deleting them.

### Root brief

Supply these JSON fields:

| Field | Meaning |
| --- | --- |
| `id`, `owner`, `project_root`, `objective` | Run/task identity, current owner and local project root |
| `constraints`, `expected_outputs`, `next_action` | Required task context and expected result |
| `requirements`, `decisions`, `procedures`, `principles` | Lists of absolute readable file references; retain decision status/constraints in the brief |
| `authority_source`, `actions`, `resources`, `checkpoints` | Actual authority reference, literal action set, immutable resource-ID map, named human gates |
| `budget` | Root-wide `dispatches` and `deadline_utc`; no refunds or nested reset |
| `claims`, `proof_kind` | Required claim IDs and `scoped` or `production` proof |
| `source`, `environment` | Source specification and absolute nonsecret environment-descriptor path |

`source` has `mode` (`git` or `roots`), `roots` (absolute paths for roots mode), optional `exclude` (absolute paths), and optional `required` (additional absolute files). `environment` is an absolute path to a nonsecret JSON descriptor. The helper executable and all Python files in its private `_work_receipts` package are included automatically.

Resource IDs map to canonical existing absolute local paths or `named:<name>` nonpath resources. Children select existing IDs; they cannot redefine mappings. Reject unsupported path traversal, symlink/special-file ownership inputs and unreadable required inputs. Action/resource lists are declarations, not a shell permission language. The host still controls tools and actual permissions; the owner must check that the declared scope matches the user's grant.

### Events and reports

Every event includes `id`, `expected_revision`, `type`, `actor`, `task`, `source_ref` (an absolute readable file) and its type-specific payload. Identical retry IDs/content are idempotent; conflicting repeated content rejects.

| Event | Required purpose / payload |
| --- | --- |
| `assign` | `assignment`: child `id`, `parent`, `owner`, `objective`, `procedure`, literal `actions`, resource IDs, `claims`, `proof_kind`, accessible `inputs`, `expected_artifacts`, optional `deadline_utc`, `required` (defaults true) and `supersedes` for repair |
| `returned` | `report`: actual child return; imports/hashes report and referenced outputs/evidence |
| `verification` | `target`, budgeted `verifier_task`, `report`: observed scoped claim results |
| `accept` | Owner `rationale` and inspected `evidence_refs`, checked against current gates and unresolved required descendants |
| `checkpoint` | Named `checkpoint_id`, concrete package, reason and decision sought; pauses the whole run |
| `resume` | `checkpoint_id`, current `authority_revision`, `human_response` file and optional complete `updated_brief` object within v0 narrowing limits; invalidates all current proof |
| `interrupted` | Intended effects, last worker/process reference and observations |
| `reconciled` | `evidence_refs` files, `worker_active` boolean, `outcome` (`known` or `unknown`) and `observations`; known requires worker inactive |
| `cancelled` | Owner reason; required proof obligations and uncertain effects remain visible |

Reports wrap the existing domain artifact rather than imposing universal report prose. Use `id`, `task`, actual `producer`, `host_ref` file, `editors` list, `review_mode` (`scoped`, `independent-discovery` or `confirmation-audit`), `context` (`fresh`, `prior_conclusions`, `exposure`, `isolation_limits`), `snapshot` manifest path, `environment` descriptor path, `verifier` file, `artifacts`/`evidence` file lists, and `claims` mapping each claim ID to `status` (`pass`, `fail` or `unverified`) plus `observations`. Include actual `commands` (`command`/`exit_code`), `effects`, `coverage` and `limitations`. Production reports additionally require `executable: true`. Returns lacking proof metadata can record artifacts but cannot verify claims. The verifier assignment must itself return before its proof becomes eligible. Imported content is hashed. Actor IDs, claimed worker freshness and human-source IDs remain declarations: inspect actual host dispatch and original execution evidence.

`returned` records arrival. `verified` means required scoped claims have eligible passing current reports. `accepted` additionally requires an explicit owner decision. Scoped design/research review cannot satisfy production execution claims. Production proof requires a declared verifier separate from every editor, fresh worker provenance and appropriate review-context limits, plus the actual executable observations required by the baseline. Cancelling required verification cannot make the run complete.

## Input identity and limits

Default Git snapshots include tracked working-tree inputs, missing paths/modes and nonignored untracked files; HEAD alone is insufficient. Explicit recursive roots support local scoped artifacts. Declare additional required ignored/external inputs, requirements, loaded procedures/helper, verifier/configuration and a nonsecret environment descriptor. Exclude only evidence/output locations; never silently exclude a required input. Retain a sorted SHA-256 manifest, copied bytes and before/after copy checks.

To materialize a test workspace, read `manifest.json`: `inputs` maps original absolute paths to hashes/modes (or `missing: true`), and `copies` maps each present original path to its archive-relative `files/...` copy. For each project file, copy from the archive to the same path relative to `project_root` in a separate writable workspace and restore the recorded mode. Preserve absent tracked files as absent; preserve the relationships of required external inputs through an explicit mapping. Do not execute or edit the protected archive. Before the run, compare the workspace's input bytes, paths and modes to the manifest. After the run, compare them again, retain intended generated effects separately and explain any input changes. Check the archive before and after execution too; workspace mutations cannot silently inherit its identity.

Final root acceptance requires current proof of the combined live artifact: live inputs, protected copied inputs and imported report/evidence bytes must match the tested identities. Source additions/deletions, dirty edits, changed requirements, environment, helper/procedure or verifier/configuration stale earlier current proof. Inspect changed-path diagnostics and reverify the affected current artifact. Scope/dependency completeness and actual runtime environment remain owner/verifier judgments; hashing a descriptor cannot prove where a command ran.

An accepted child's source snapshot may predate later implementation; its historical acceptance can satisfy its subordinate obligation while final integrated root proof covers the current artifact. Its imported reports, evidence, acceptance references and protected archive must still retain their recorded hashes. Invalid historical receipts block ancestors. Historical acceptance is not current integrated proof, and resume invalidates all proof, including that history's eligibility, until rechecked.

V0 supports local filesystem proof. Remote services, browser/deployment instances and external effects require their own observations or stay unverified. It does not enforce worker permissions, authenticate actors, launch/cancel workers, guarantee filesystem atomic snapshots, detect transient/undeclared changes, survive chat closure automatically or protect against bypass/tampering. Never report declared budgets as measured token/cost limits; record available host usage or `unknown`. This experimental mechanism adds no launcher, daemon, coordinator, installer or new domain taxonomy.
