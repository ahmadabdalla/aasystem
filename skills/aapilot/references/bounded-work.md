# Bounded autonomous work — experimental v0

Use this procedure when the user explicitly requests bounded autonomous work or the bounded-autonomy PoC. Select the existing task procedure first; it retains phase ownership and scope. A directly invoked specialist owns this same loop within its domain, without an extra Aapilot coordinator. Architect remains design-only. Ordinary tasks retain their existing route, and a plan-only request ends before implementation.

The [execution contract](execution.md) owns decision authority, delegation, review context, independent production verification and completion. This reference owns the experimental receipt protocol used alongside those rules. The [decision-context principle](../../principle-preserve-decision-context/SKILL.md) applies: preserve the information a receiving owner needs, using references only when it can retrieve them.

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

1. **Frame one retrievable brief.** Carry requirements and their status, accepted decisions, constraints, applicable procedures/principles, expected outputs, proof obligations and mandatory checkpoints. Apply [decision authority](execution.md#decision-authority). Record actual host/delegation/access limits. Literal action names and resource IDs describe authority; they do not configure host permissions.
2. **Initialize one run.** Resolve [work_receipts.py](../scripts/work_receipts.py) from the loaded skill tree; use Python 3.10+ and its standard library. Keep inputs, state, reports, snapshots and evidence outside the installed tree/cache under project [evidence conventions](../../bootstrap-verification/references/project-contract.md#evidence-and-retention). One root owner writes state; nested workers return proposed events and artifacts to it.
3. **Review decisions before implementation.** Record a current `decision_review` over the governing sources, exact design/contract artifacts and resource scope. Distinguish accepted sources, actual human instructions/answers and delegated routine details. Unresolved consequential choices block implementation. Declare mandatory `checkpoint_obligations`; omitting a checkpoint event does not waive its obligation.
4. **Reserve, dispatch and retain native receipts.** `assign` reserves the initial spawn allocation. Immediately before each actual native call, check that task’s `status.tasks[task_id].dispatch_eligible_now` is true and inspect `dispatch_gates`. Invoke the native tool, then record `dispatch` with its request/result and worker identity. Each followup requires `dispatch_reserved` before the call; a fresh retry requires a fresh assignment. Initial spawn plus its receipt costs one allocation. Nested work, failed launches, continuations and abandoned reservations consume the same nonrefundable root budget. Unknown outcomes require reconciliation before retry.
5. **Freeze findings before importing proof.** Inspect returned artifacts. For a fresh verifier, assign it, snapshot its inputs and record `review_preflight` before native dispatch. Exercise the project recipe in a separate materialized workspace. Record `initial_findings` with the full context interval before lead formatting/metadata assistance; preserve its original bytes. Import `returned` and `verification` reports linked to those findings. Discovery exposure, missing receipts, failed checks or stale inputs leave the relevant gate unmet. A final report cannot improve the frozen observations, claim results or source identity; new proof needs a fresh review attempt.
6. **Repair within authority.** Use a fresh bounded correction naming the superseded assignment; preserve failed evidence. Replacement keeps the original parent, action/resource scope, claims and proof strength. Unrelated claimless work cannot waive obligations, and replacement cannot bypass uncertain effects. Repeat affected independent proof against the current combined artifact.
7. **Return human decisions and resume.** Record and present the concrete checkpoint package: a focused question or concrete options, artifact and exact decision sought. Stop and wait. Stop or inspect already running work through native tools. Resume only from actual matching human input bound to that package; retain its original source. Structural response validation does not authenticate a human. Resume preserves or narrows authority under the existing limits, retains consumed budget and invalidates current proof; record a new decision review and recheck proof. Changed root identity/resources/source/environment require a new run.
8. **Reconcile and accept.** Record interruptions and inspect actual processes, partial files and side effects. Unknown effects block affected work; cancellation refunds nothing. Before `accept`, reconcile a current decision review for the combined scope, mandatory checkpoints, native attempts and current proof. Inspect actual artifacts and evidence; record rationale and evidence references. Complete canonical-record and retention work, then report results, proof and limits.

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

Here `assign.json` creates the child ID `design` with `purpose: other`; the owner separately dispatches its real worker with native host tools and imports the native `dispatch` receipt. Implementation assignments additionally require a current decision review. Assign the verifier before taking its snapshot and recording preflight so its procedure and inputs join the tested identity. The helper never launches a worker. One owner imports returned files and writes state.

`init` creates state schema 2; snapshot archives retain schema 1. Legacy state schema 1 is readable as historical status only, with `legacy_unrecorded_gates` and no current eligibility. `apply` and `snapshot` require a new schema-2 run; never invent historical decisions, native attempts or clean review intervals. Existing schema-1 snapshot archives retain their integrity contract.

`init` creates versioned run state from the root brief. `apply` validates/imports one event and updates state atomically under a local exclusive lock and expected revision. A rejection exits nonzero without replacing prior state. `snapshot` records copied, hashed inputs for proof and returns the manifest path and identity without advancing the state revision. Its output must be a new directory below the state-file parent. `status` exposes recorded/historical acceptance versus current eligibility, remaining dispatches, checkpoints, unsettled work, uncertain effects and missing/stale evidence. Concurrent owners are unsupported; inspect stale locks before recovery rather than blindly deleting them.

### Root brief

Supply these JSON fields:

| Field | Meaning |
| --- | --- |
| `id`, `owner`, `project_root`, `objective`, `purpose` | Run/task identity, current owner, local project root and explicit `implementation`, `verification` or `other` purpose |
| `constraints`, `expected_outputs`, `next_action` | Required task context and expected result |
| `requirements`, `decisions`, `procedures`, `principles` | Lists of absolute readable file references; retain decision status/constraints in the brief |
| `authority_source`, `actions`, `resources`, `checkpoints` | Actual authority reference, literal action set, immutable resource-ID map, named human gates |
| `checkpoint_obligations` | Mandatory `{id, before: implementation or acceptance}` entries referencing declared checkpoint IDs |
| `budget` | Root-wide `dispatches` and `deadline_utc`; no refunds or nested reset |
| `claims`, `proof_kind`, `required_review_mode` | Required claim IDs (nonempty for `production`), `scoped` or `production` proof, and required review mode (default `independent-discovery`) |
| `source`, `environment` | Source specification and absolute nonsecret environment-descriptor path |

`source` has `mode` (`git` or `roots`), `roots` (absolute paths for roots mode), optional `exclude` (absolute paths), and optional `required` (additional absolute files). `environment` is an absolute path to a nonsecret JSON descriptor. The helper executable and all Python files in its private `_work_receipts` package are included automatically.

Resource IDs map to canonical existing absolute local paths or `named:<name>` nonpath resources. Children select existing IDs; they cannot redefine mappings. Reject unsupported path traversal, symlink/special-file ownership inputs and unreadable required inputs. Action/resource lists are declarations, not a shell permission language. The host still controls tools and actual permissions; the owner must check that the declared scope matches the user's grant.

### Events and reports

Every event includes `id`, `expected_revision`, `type`, `actor`, `task`, `source_ref` (an absolute readable file) and its type-specific payload. Identical retry IDs/content are idempotent; conflicting repeated content rejects.

| Event | Required purpose / payload |
| --- | --- |
| `decision_review` | Current `authority_revision`, resource IDs, exact `artifact_refs`, nonempty `coverage` and `rationale`, classified `decisions` and `unresolved` choices |
| `assign` | `assignment`: child `id`, `parent`, `owner`, `objective`, `procedure`, `purpose` (`implementation`, `verification`, `other`), literal `actions`/`resources`, `claims`/`proof_kind`, `inputs`/`expected_artifacts`, optional `deadline_utc`, `required` and `supersedes`; implementation binds a current `decision_review` |
| `dispatch_reserved` | Before a followup: unique `attempt_id`, `operation: followup`, existing `worker_id` and live-state necessity in `reason` |
| `dispatch` | Reserved `attempt_id`, `operation` (`spawn`, `followup`), exact `request_ref`, actual native `host_ref`, `outcome` (`started`, `failed`, `unknown`) and `worker_id`; initial spawn attempt ID is the assignment ID |
| `review_preflight` | On a verification assignment, before dispatch: `snapshot`, `environment`, `mode`, `context`, exact `host_request_ref` |
| `initial_findings` | After started dispatch, before return: `preflight_event`, `dispatch_event`, original `findings`, complete `context` and `context_evidence_refs`; one immutable initial record per attempt |
| `returned` | `report` file and retained outputs/evidence, bound to a started native producer |
| `verification` | `target`, budgeted `verifier_task`, `report` file referencing its `initial_findings_event` |
| `accept` | Current `decision_review` for the accepting task, owner `rationale` and inspected `evidence_refs`; requires current proof, resolved obligations and settled native attempts |
| `checkpoint` | Named `checkpoint_id`, concrete `package` file, `reason` and exact `decision` sought; pauses the whole run |
| `resume` | `checkpoint_id`, `authority_revision`, original `human_response` file with exact question/package/source binding; optional complete narrowed `updated_brief`; invalidates proof |
| `interrupted` | Intended effects, last worker/process reference and observations |
| `reconciled` | Evidence files, `worker_active` boolean, `outcome` (`known`, `unknown`) and observations; known requires inactive worker |
| `cancelled` | Owner reason; required obligations and uncertain effects remain visible |

### Decision records

A review decision carries `id`, `question`, `selected`, `classification` (`product`, `architecture`, `routine`) and `origin`. Source origins use `{kind: source, ref, locator, status: accepted}`. Human origins use `{kind: human, instruction_ref}` for an original explicit instruction or `{kind: human, checkpoint_event, resume_event, selected_option}` for an answered choice; omit `selected_option` for free-text. The decision ID/question must match the package and `selected` must equal the actual response `answer`. Only routine decisions may use `kind: delegated`. A model proposal is not an accepted source. Unresolved entries carry ID, question and reason; they block implementation and acceptance. Retain each known unresolved ID and question in later overlapping reviews until that same question is resolved by actual human input or an accepted source; an empty review or delegated routine decision cannot erase it.

Review authority/source/design bytes are hashed. Implementation resources must fit the review and assignment inputs must contain its exact design artifacts. Code edits implementing that design do not stale it; changed design or governing input does. The latest review is determined by event revision for each task and overlapping resource scope, including ancestor decisions and subordinate decisions at acceptance. Final acceptance requires a current reconciled review for combined work, preserving later decisions.

A checkpoint package binds the exact question, artifact references and decision IDs. Use a focused free-text question when sufficient; a choice package includes at least two distinct concrete option IDs and their consequences. The response contains `checkpoint_event`, `question_id`, `package_hash` (the SHA-256 string), `authority_revision`, `answer` and original `source_ref`. A choice response adds a valid `selected_option`; a free-text response must omit it. Changed questions/options require a new package and answer. Matching JSON does not prove authorship or that the cited answer resolves the question. Unknown/ambiguous answers remain pending.

### Native attempts and review evidence

Retain the exact native request and actual result/failure. Started attempts require a worker ID; a failed or missing launch cannot return work. Returns bind their producer to the started worker. Followups target that same worker and require the additional reservation before invocation. Identical replay consumes no extra allocation; another event cannot reuse a reservation. New reservations require remaining budget. A previously charged pending reservation can remain dispatch eligible at `remaining_dispatches: 0`; eligibility also checks current decision review, checkpoints, deadline, uncertain effects and verifier preflight as applicable. Already running work still needs native inspection/stop.

Per-task `status` exposes prospective `dispatch_eligible_now` and `dispatch_gates`, separately from acceptance eligibility; a pending reservation is required, and legacy schema 1 is always ineligible. Failed/unknown actual call receipts remain recordable after prospective gates close. If a known started call’s receipt rejects, retain its actual request/result, record `interrupted` with actual effects, inspect/stop the worker and reconcile; never relabel that call as failed or unknown to obtain a receipt.

`status` distinguishes `allocated_dispatches`, `observed_attempts`, started/failed/unknown attempts, `pending_reservations` and `remaining_dispatches`. An allocation is not an observed call. Pending receipts block acceptance. Report host provenance and usage as known or unknown; declaration fields cannot authenticate a dispatch, actor or human.

Verification assignments bind `review: {target, mode, claims}`. The preflight snapshot must identify the verification task. Preflight and initial context include `fresh`, `prior_conclusions`, explanatory `exposure`, nonempty `isolation_limits` and typed `exposures` with kind, stage, original source and description. Stages cover before execution, during execution, and after execution before initial findings. Initial context requires `interval_complete: true` over assignment through returned initial findings. Missing/unknown completeness or prior-conclusion exposure cannot pass discovery, even if a final summary declares clean context. Preserve the original first findings before metadata help; later comparison cannot replace them. Use a new assignment for new discovery proof. A qualified audit remains retained evidence and satisfies only an authorized audit obligation; it cannot satisfy required discovery.

Reports wrap the existing domain artifact rather than imposing universal report prose. Final review reports bind `initial_findings_event`; the frozen original needs no self-reference. Final task, producer, snapshot, environment, verifier, claims, commands, effects, executable flag and review mode must equal the frozen original; new observations require a fresh attempt. Use `id`, `task`, actual `producer`, `host_ref` file, `editors` list, `review_mode` (`scoped`, `independent-discovery` or `confirmation-audit`), `context` (`fresh`, `prior_conclusions`, `exposure`, `isolation_limits`), `snapshot` manifest path, `environment` descriptor path, `verifier` file, `artifacts`/`evidence` file lists, and `claims` mapping each claim ID to `status` (`pass`, `fail` or `unverified`) plus `observations`. Include actual `commands` (`command`/`exit_code`), `effects`, `coverage` and `limitations`. Production reports additionally require `executable: true`. Returns lacking proof metadata can record artifacts but cannot verify claims. The verifier assignment must itself return before its proof becomes eligible. Imported content is hashed. Native request/result linkage and retained evidence strengthen recorded provenance; their meaning and actual worker isolation still require inspection. Actor IDs and human-source IDs remain declarations, not authentication.

`returned` records arrival. `verified` means required scoped claims have eligible passing current reports. `accepted` additionally requires an explicit owner decision. Scoped design/research review cannot satisfy production execution claims. Production proof requires a declared verifier separate from every editor, fresh worker provenance and appropriate review-context limits, plus the actual executable observations required by the baseline. Cancelling required verification cannot make the run complete.

## Input identity and limits

Default Git snapshots include tracked working-tree inputs, missing paths/modes and nonignored untracked files; HEAD alone is insufficient. Explicit recursive roots support local scoped artifacts. Declare additional required ignored/external inputs, requirements, loaded procedures/helper, verifier/configuration and a nonsecret environment descriptor. Exclude only evidence/output locations; never silently exclude a required input. Retain a sorted SHA-256 manifest, copied bytes and before/after copy checks.

To materialize a test workspace, read `manifest.json`: `inputs` maps original absolute paths to hashes/modes (or `missing: true`), and `copies` maps each present original path to its archive-relative `files/...` copy. For each project file, copy from the archive to the same path relative to `project_root` in a separate writable workspace and restore the recorded mode. Preserve absent tracked files as absent; preserve the relationships of required external inputs through an explicit mapping. Do not execute or edit the protected archive. Before the run, compare the workspace's input bytes, paths and modes to the manifest. After the run, compare them again, retain intended generated effects separately and explain any input changes. Check the archive before and after execution too; workspace mutations cannot silently inherit its identity.

Final root acceptance requires current proof of the combined live artifact: live inputs, protected copied inputs and imported report/evidence bytes must match the tested identities. Source additions/deletions, dirty edits, changed requirements, environment, helper/procedure or verifier/configuration stale earlier current proof. Inspect changed-path diagnostics and reverify the affected current artifact. Scope/dependency completeness and actual runtime environment remain owner/verifier judgments; hashing a descriptor cannot prove where a command ran.

An accepted child's source snapshot may predate later implementation; its historical acceptance can satisfy its subordinate obligation while final integrated root proof covers the current artifact. Its imported reports, evidence, acceptance references and protected archive must still retain their recorded hashes. Invalid historical receipts block ancestors. Historical acceptance is not current integrated proof, and resume invalidates all proof, including that history's eligibility, until rechecked.

This experimental protocol supports local filesystem proof. Remote services, browser/deployment instances and external effects require their own observations or stay unverified. It does not enforce worker permissions, authenticate actors, launch/cancel workers, guarantee filesystem atomic snapshots, detect omitted semantic choices, transient/undeclared changes or direct tool bypass, survive chat closure automatically, or protect against fabricated declarations/tampering. Exercise actual host behavior to assess those limits; structural CLI rejection is not a hard lock on native tools. Never report declared budgets as measured token/cost limits; record available host usage or `unknown`. This experimental mechanism adds no launcher, daemon, coordinator, installer or new domain taxonomy.
