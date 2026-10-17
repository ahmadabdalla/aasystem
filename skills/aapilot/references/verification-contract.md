# Verification contract

Use this common contract by default for retained production changes through the existing task procedure. Keep one root owner and run; supporting specialists return into it within their assigned scope rather than initializing another run. A direct eligible Implement request needs no Aapilot wrapper. Architect remains design-only. Read-only answers and design work retain scoped evidence without production ceremony; a plan-only request ends before implementation.

The [execution contract](execution.md) owns decision authority, delegation, review context, independent production verification and completion. This reference owns the shared receipt procedure used alongside those rules. The minimum is a sourced request and authority, scope, current artifact identity, nonempty specific claims, observed checks with results/evidence/limits, and explicit owner acceptance. The [decision-context principle](../../principle-preserve-decision-context/SKILL.md) applies: preserve the information a receiving owner needs, using references only when it can retrieve them.

## Operating loop

1. **Frame one retrievable brief.** Carry requirements/status, authority, scope, settled decisions, expected outputs, proof claims, relevant procedures/principles and mandatory checkpoints. Record actual host/access limits. Resource IDs and actions describe authority; they do not configure host permissions.
2. **Choose the proof obligation.** Apply [owner-presentation eligibility](execution.md#owner-presentation-eligibility) before editing. Eligible work uses the owner-presentation path below; other retained production work follows [engineering verification](engineering-verification.md) for required claims, assessment and execution. Keep the existing task owner and route. A later broader effect must follow the same shared escalation rule before acceptance.
3. **Initialize or reuse one run.** Resolve [work_receipts.py](../scripts/work_receipts.py) from the installed skill tree; use Python 3.10+ and its standard library. Keep inputs, state, reports, snapshots and evidence outside the installed tree/cache under project [evidence conventions](../../bootstrap-verification/references/project-contract.md#evidence-and-retention). Diagnose and repair missing Python/helper access within authority, or report validation unmet; never silently bypass it. The root owner writes state; specialists return artifacts and proposed events.
4. **Review decisions and perform the work.** Retain a current `decision_review` against governing/design sources and resource scope; owner-presentation `init` generates its routine review from the explicit eligibility declaration. Preserve sourced requirements, routine delegated details and actual human agreement distinctly. Unresolved consequential choices block implementation. Record mandatory `checkpoint_obligations`; omission does not waive them. Use owner execution, the owner-presentation proof path or native assignments below as applicable; execution placement does not determine the proof requirement.
5. **Return required human decisions.** Present and record the concrete checkpoint package under [decision authority](execution.md#decision-authority): identifiable artifact, checked/unverified limits and a focused question or concrete options. For visuals, provide an inspectable preview or retained rendered views. Stop the whole process and wait. Resume only from actual matching human input; preserve its source. Structural response validation does not authenticate a person. Resume retains consumed budget and requires current decision review/proof; changed immutable root identity requires a linked new run.
6. **Reconcile and accept.** Inspect actual artifacts, side effects and current proof. Apply [engineering finding reconciliation](engineering-verification.md#reconcile-and-accept) when required. Retain interruptions, reconcile uncertain effects, resolve mandatory checkpoints, complete canonical-record and retention work, then record explicit `accept` with rationale and inspected evidence. Report the actual proof basis and limits; receipt acceptance is not independent verification.

### Owner execution with independent proof

For owner implementation, use the full root brief with `verification_requirement: independent` and the required engineering claims. Retain a current decision review before editing and identify the root owner as an editor. Apply the selected procedures and retain development evidence in the existing project locations.

The root may submit an artifact and development report using `returned`, with the root task ID and actual root owner as `producer`. A native `host_ref` is unnecessary for that root report; report actual checks, evidence, effects and limits. This return is development evidence, not independent proof. Do not label it owner-presentation or invent a worker dispatch.

Assign a fresh separate verifier targeting the root under the native independent-proof procedure. Preserve preflight, original findings, executable observations, current artifact identity and finding reconciliation before root acceptance. The root owner cannot verify its own production change.

### Owner-presentation path

Read the single [eligibility and escalation rule](execution.md#owner-presentation-eligibility). Record its pre-edit basis in the root brief, perform the prescribed edit and inspect the actual diff afterward. Reuse the request, existing project evidence and owner report; generate routine metadata with the same helper. Use only relevant source roots and required dependencies rather than copying the whole repository by default. Keep governing requirements, helper/procedures, verifier and environment in identity where applicable.

Before editing, run `init` with `verification_requirement: owner-presentation` and the eligibility declaration below. Keep request, scope, authority, environment, budget and nonempty claims explicit. The helper generates routine owner-path fields, an initial input manifest and decision review; it does not decide semantic eligibility or supply human agreement. After editing and checking, take a root snapshot, return the owner report below, then accept against that current report. Owner-path `accept` may omit `decision_review` to reuse the generated review. No native assignment, dispatch, verifier preflight or frozen initial-findings packet is required; zero native dispatches is valid.

The owner report retains actual source/diff checks and an available preview, observations/evidence, post-diff eligibility review and unexercised limits. Keep this proof labeled owner-presentation. A later return reopens prior owner acceptance. A newer failed or stale report blocks acceptance; do not fall back to an older pass or omit claims. If broader effects appear within existing authority/resources and remaining budget, record `verification_escalated` and obtain independent proof. Otherwise stop for authorized continuation under the shared rule; preserve history and consumed budget.

### Native assignments and independent proof

1. **Reserve, dispatch and retain native receipts.** `assign` reserves the initial spawn allocation. Immediately before each native call, inspect `status.tasks[task_id].dispatch_eligible_now` and `dispatch_gates`. Invoke the native tool, then record `dispatch` with its exact request/result and worker identity. Each followup needs `dispatch_reserved` before the call; fresh retries need fresh assignments. Nested work, failed launches, continuations and abandoned reservations consume the same nonrefundable root budget. Unknown outcomes require reconciliation before retry.
2. **Freeze findings before importing independent proof.** Assign a fresh verifier, snapshot its inputs and record `review_preflight` before native dispatch. Exercise project recipes in a separate materialized workspace. Record `initial_findings` over the full context interval before lead formatting/metadata help, preserving original bytes. Import `returned` and `verification` reports linked to those findings. Exposure, missing receipts, failed checks or stale inputs leave the relevant gate unmet. New observations need a fresh review attempt.
3. **Repair within authority.** Use the shared correction-continuity rule; preserve failed evidence. A replacement assignment names the superseded assignment and keeps the original parent, action/resource scope, claims and proof strength. Unrelated claimless work cannot waive obligations or uncertain effects. Repeat affected independent proof against the current combined artifact.

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

Put immutable required references and child assignment inputs outside `runtime/`; the state-file parent is automatically excluded from source identity. Mutable run records belong inside it. Prepare `inputs/brief.json` using the fields below. For the native-worker path, also prepare `runtime/assign.json`, then run:

```sh
python3 "$HELPER" init --brief "$RUN/inputs/brief.json" --state "$RUN/runtime/state.json"
python3 "$HELPER" apply --state "$RUN/runtime/state.json" --event "$RUN/runtime/assign.json"
python3 "$HELPER" snapshot --state "$RUN/runtime/state.json" --task design --out "$RUN/runtime/input-1"
python3 "$HELPER" status --state "$RUN/runtime/state.json"
```

Here `assign.json` creates the child ID `design` with `purpose: other`; the owner separately dispatches its real worker with native host tools and imports the native `dispatch` receipt. Implementation assignments additionally require a current decision review. Assign the verifier before taking its snapshot and recording preflight so its procedure and inputs join the tested identity. The helper never launches a worker. One owner imports returned files and writes state.

`init` creates state schema 3; snapshot archives retain schema 1. State schemas 1 and 2 remain historical read-only status with no current eligibility. `apply` and `snapshot` require a new schema-3 run; never invent historical decisions, native attempts or clean review intervals. Existing snapshot archives retain their integrity contract.

`init` creates versioned run state from the root brief. `apply` validates/imports one event and updates state atomically under a local exclusive lock and expected revision. A rejection exits nonzero without replacing prior state. `snapshot` records copied, hashed inputs for proof and returns the manifest path and identity without advancing the state revision. Its output must be a new directory below the state-file parent. `status` exposes recorded/historical acceptance versus current eligibility, remaining dispatches, checkpoints, unsettled work, uncertain effects and missing/stale evidence. Concurrent owners are unsupported; inspect stale locks before recovery rather than blindly deleting them.

### Owner-presentation commands and report

Prepare the explicit brief fields below, then use the existing commands. Replace `actual-root-id-from-brief` with the brief's `id`; prepare the two event files using the common envelope and payload table.

```sh
python3 "$HELPER" init --brief "$RUN/inputs/brief.json" --state "$RUN/runtime/state.json"
# Make the prescribed edit and retain actual diff/check evidence.
python3 "$HELPER" snapshot --state "$RUN/runtime/state.json" --task "actual-root-id-from-brief" --out "$RUN/runtime/owner-input"
python3 "$HELPER" apply --state "$RUN/runtime/state.json" --event "$RUN/runtime/returned.json"
python3 "$HELPER" apply --state "$RUN/runtime/state.json" --event "$RUN/runtime/accept.json"
python3 "$HELPER" status --state "$RUN/runtime/state.json"
```

`returned.json` references the absolute owner report path in `report`. The owner report requires:

| Fields | Required content |
| --- | --- |
| `id`, `task`, `producer`, `proof_basis` | Report ID, root task ID, actual root owner, literal `owner-presentation` |
| `snapshot`, `environment` | New root snapshot's manifest path and the brief's environment descriptor |
| `claims` | Each declared ID maps to `status: pass`, `fail` or `unverified` and specific `observations` |
| `commands` | Nonempty actual checks as `{command, exit_code}`; each passing-proof exit code is integer `0` |
| `diff_ref`, `eligibility_review` | Retained actual diff file and the owner's post-diff eligibility judgment |
| `evidence`, `coverage`, `effects`, `limitations` | Nonempty readable evidence paths, checked scope and observed effects; include unexercised limits (the limitations field is required) |

No native host, verifier, review-context, preflight or frozen-findings fields are needed. `accept.json` carries owner `rationale` and inspected `evidence_refs`. The helper preserves report/evidence hashes and checks current identities; it cannot authenticate the diff or judge its meaning. Changed relevant inputs outside declared components block owner proof.

### Root brief

For the owner-presentation path, explicitly supply `id`, `owner`, `project_root`, `objective`, `authority_source`, `environment`, `actions`, `resources`, `budget`, nonempty `claims`, `verification_requirement` and `presentation_eligibility`. `init` defaults `purpose` to `implementation`, `proof_kind` to `production`, requirements to the authority source, context/output/next-action to the eligibility basis/prescription, empty optional reference/checkpoint lists and source roots to the declared components. Provide additional relevant dependencies through `source.required`; explicit full fields override defaults and are validated.

Other runs supply the complete brief:

| Field | Meaning |
| --- | --- |
| `id`, `owner`, `project_root`, `objective`, `purpose` | Run/task identity, current owner, local project root and explicit `implementation`, `verification` or `other` purpose |
| `constraints`, `expected_outputs`, `next_action` | Required task context and expected result |
| `requirements`, `decisions`, `procedures`, `principles` | Lists of absolute readable file references; retain decision status/constraints in the brief |
| `authority_source`, `actions`, `resources`, `checkpoints` | Actual authority reference, literal action set, immutable resource-ID map, named human gates |
| `checkpoint_obligations` | Mandatory `{id, before: implementation or acceptance}` entries referencing declared checkpoint IDs |
| `budget` | Root-wide `dispatches` and `deadline_utc`; no refunds or nested reset |
| `claims`, `proof_kind`, `required_review_mode` | Required claim IDs (nonempty for retained production), `scoped` or `production` proof, and required independent review mode (default `independent-discovery`) |
| `verification_requirement` | `independent` by default; explicit `owner-presentation` only for an eligible root |
| `presentation_eligibility` | For the owner path: `classification: prescribed-presentation`, absolute governing `request_ref`, nonempty `locator`, exact requested `prescription`, eligibility `basis` and `components` listing existing absolute component files |
| `source`, `environment` | Source specification and absolute nonsecret environment-descriptor path |

Map the [engineering verification obligations](engineering-verification.md) into existing fields: the required assessment ID goes in root `claims`, its bounded scope and completion condition in `constraints` or `expected_outputs`, and the same ID in the verification assignment's `claims` and `review.claims`. Its report `claims` entry records review completion, findings, and limits in `observations`, with supporting artifacts in `evidence`. Keep executable results under their own claim IDs and `commands`. The helper checks claim presence/status and provenance; it does not judge review substance or finding dispositions.

`source` has `mode` (`git` or `roots`), `roots` (absolute paths for roots mode), optional `exclude` (absolute paths), and optional `required` (additional absolute files). `environment` is an absolute path to a nonsecret JSON descriptor. The helper executable and all Python files in its private `_work_receipts` package are included automatically. Keep the complete exported tree available; declare relevant loaded procedures and other required inputs so the source identity covers the actual decision/proof dependencies. The shipped runtime CLI and private package require no repository test files or evaluation fixtures.

Resource IDs map to canonical existing absolute local paths or `named:<name>` nonpath resources. Children select existing IDs; they cannot redefine mappings. Reject unsupported path traversal, symlink/special-file ownership inputs and unreadable required inputs. Action/resource lists are declarations, not a shell permission language. The host still controls tools and actual permissions; the owner must check that the declared scope matches the user's grant.

### Events and reports

Every event includes `id`, `expected_revision`, `type`, `actor`, `task`, `source_ref` (an absolute readable file) and its type-specific payload. Identical retry IDs/content are idempotent; conflicting repeated content rejects.

| Event | Required purpose / payload |
| --- | --- |
| `decision_review` | Current `authority_revision`, resource IDs, exact `artifact_refs`, nonempty `coverage` and `rationale`, classified `decisions` and `unresolved` choices |
| `assign` | `assignment`: child `id`, `parent`, `owner`, `objective`, `procedure`, `purpose` (`implementation`, `verification`, `other`), literal `actions`/`resources`, `claims`/`proof_kind`, `inputs`/`expected_artifacts`, optional `deadline_utc`, `required` and `supersedes`; implementation binds a current `decision_review` |
| `dispatch_reserved` | Before a followup: unique `attempt_id`, `operation: followup`, existing `worker_id` and the permitted continuity or live-state rationale in `reason` |
| `dispatch` | Reserved `attempt_id`, `operation` (`spawn`, `followup`), exact `request_ref`, actual native `host_ref`, `outcome` (`started`, `failed`, `unknown`) and `worker_id`; initial spawn attempt ID is the assignment ID |
| `review_preflight` | On a verification assignment, before dispatch: `snapshot`, `environment`, `mode`, `context`, exact `host_request_ref` |
| `initial_findings` | After started dispatch, before return: `preflight_event`, `dispatch_event`, original `findings`, complete `context` and `context_evidence_refs`; one immutable initial record per attempt |
| `returned` | `report` file and retained outputs/evidence; native child returns bind a started producer; root owner returns need no native host, with distinct development and owner-presentation proof obligations |
| `verification_escalated` | Root owner strengthens to `requirement: independent`, with `reason` and `evidence_refs`; authority, resources, consumed budget and stronger obligations remain intact |
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

### Native attempts and independent review evidence

Retain the exact native request and actual result/failure. Started attempts require a worker ID; a failed or missing launch cannot return work. Returns bind their producer to the started worker. Followups target that same worker and require the additional reservation before invocation. Identical replay consumes no extra allocation; another event cannot reuse a reservation. New reservations require remaining budget. A previously charged pending reservation can remain dispatch eligible at `remaining_dispatches: 0`; eligibility also checks current decision review, checkpoints, deadline, uncertain effects and verifier preflight as applicable. Already running work still needs native inspection/stop.

Per-task `status` exposes prospective `dispatch_eligible_now` and `dispatch_gates`, separately from acceptance eligibility; a pending reservation is required, and historical schema 1/2 is always ineligible. Failed/unknown actual call receipts remain recordable after prospective gates close. If a known started call’s receipt rejects, retain its actual request/result, record `interrupted` with actual effects, inspect/stop the worker and reconcile; never relabel that call as failed or unknown to obtain a receipt.

`status` distinguishes `allocated_dispatches`, `observed_attempts`, started/failed/unknown attempts, `pending_reservations` and `remaining_dispatches`. An allocation is not an observed call. Pending receipts block acceptance. Report host provenance and usage as known or unknown; declaration fields cannot authenticate a dispatch, actor or human.

Verification assignments bind `review: {target, mode, claims}`. The preflight snapshot must identify the verification task. Preflight and initial context include `fresh`, `prior_conclusions`, explanatory `exposure`, nonempty `isolation_limits` and typed `exposures` with kind, stage, original source and description. Stages cover before execution, during execution, and after execution before initial findings. Initial context requires `interval_complete: true` over assignment through returned initial findings. Missing/unknown completeness or prior-conclusion exposure cannot pass discovery, even if a final summary declares clean context. Preserve the original first findings before metadata help; later comparison cannot replace them. Use a new assignment for new discovery proof. A qualified audit remains retained evidence and satisfies only an authorized audit obligation; it cannot satisfy required discovery.

Root artifact/development returns do not enter the independent proof set. Independent/native reports wrap the existing domain artifact rather than imposing universal report prose. The owner supplies assigned workers the artifact/evidence return requirements relevant to their task and imports receipt metadata; workers need not administer the root run. Final review reports bind `initial_findings_event`; the frozen original needs no self-reference. Final task, producer, snapshot, environment, verifier, claims, commands, effects, executable flag and review mode must equal the frozen original; new observations require a fresh attempt. Use `id`, `task`, actual `producer`, `host_ref` file, `editors` list, `review_mode` (`scoped`, `independent-discovery` or `confirmation-audit`), `context` (`fresh`, `prior_conclusions`, `exposure`, `isolation_limits`), `snapshot` manifest path, `environment` descriptor path, `verifier` file, `artifacts`/`evidence` file lists, and `claims` mapping each claim ID to `status` (`pass`, `fail` or `unverified`) plus `observations`. Include actual `commands` (`command`/`exit_code`), `effects`, `coverage` and `limitations`. Production reports additionally require `executable: true`. Returns lacking proof metadata can record artifacts but cannot verify claims. The verifier assignment must itself return before its proof becomes eligible. Imported content is hashed. Native request/result linkage and retained evidence strengthen recorded provenance; their meaning and actual worker isolation still require inspection. Actor IDs and human-source IDs remain declarations, not authentication.

`returned` records arrival, not acceptance. Per-task status exposes `verification_requirement`, `actual_proof_basis` (`none`, `owner-presentation` or `independent`) and `checked_now`. Passing current owner-presentation proof has `proof_status: owner-checked` and `verified_now: false`; it never claims independence. For other proof, `verified_now` requires nonempty claims and eligible passing current reports; `proof_status` is `verified`, `unverified` or `no_claims` as applicable. Historical schema-1/2 runs retain status for inspection without current eligibility. These fields are derived projections, not saved state.

`no_claims` certifies neither correct scope nor approval; scoped claimless work cannot bypass production obligations. `accepted` additionally requires an explicit owner decision and resolved gates; even current passing proof can have a pending checkpoint. Scoped design/research review cannot satisfy production execution claims. Except for eligible owner-presentation proof, retained production proof requires a verifier separate from every editor, fresh worker provenance and the required review-context/executable observations. Cancelling required verification cannot make the run complete.

## Input identity and limits

Default Git snapshots include tracked working-tree inputs, missing paths/modes and nonignored untracked files; HEAD alone is insufficient. Explicit recursive roots support local scoped artifacts. Declare additional required ignored/external inputs, requirements, loaded procedures/helper, verifier/configuration and a nonsecret environment descriptor. Exclude only evidence/output locations; never silently exclude a required input. Retain a sorted SHA-256 manifest, copied bytes and before/after copy checks.

To materialize a test workspace, read `manifest.json`: `inputs` maps original absolute paths to hashes/modes (or `missing: true`), and `copies` maps each present original path to its archive-relative `files/...` copy. For each project file, copy from the archive to the same path relative to `project_root` in a separate writable workspace and restore the recorded mode. Preserve absent tracked files as absent; preserve the relationships of required external inputs through an explicit mapping. Do not execute or edit the protected archive. Before the run, compare the workspace's input bytes, paths and modes to the manifest. After the run, compare them again, retain intended generated effects separately and explain any input changes. Check the archive before and after execution too; workspace mutations cannot silently inherit its identity.

Final root acceptance requires current proof of the combined live artifact: live inputs, protected copied inputs and imported report/evidence bytes must match the tested identities. Source additions/deletions, dirty edits, changed requirements, environment, helper/procedure or verifier/configuration stale earlier current proof. Inspect changed-path diagnostics and reverify the affected current artifact. Scope/dependency completeness and actual runtime environment remain owner/verifier judgments; hashing a descriptor cannot prove where a command ran.

An accepted child's source snapshot may predate later implementation; its historical acceptance can satisfy its subordinate obligation while final integrated root proof covers the current artifact. Its imported reports, evidence, acceptance references and protected archive must still retain their recorded hashes. Invalid historical receipts block ancestors. Historical acceptance is not current integrated proof, and resume invalidates all proof, including that history's eligibility, until rechecked.

This protocol supports local filesystem proof. Remote services, browser/deployment instances and external effects require their own observations or stay unverified. It does not enforce worker permissions, authenticate actors, launch/cancel workers, guarantee filesystem atomic snapshots, detect omitted semantic choices, transient/undeclared changes or direct tool bypass, survive chat closure automatically, or protect against fabricated declarations/tampering. Exercise actual host behavior to assess those limits; structural CLI rejection is not a hard lock on native tools. Never report declared budgets as measured token/cost limits; record available host usage or `unknown`. This mechanism adds no launcher, daemon, coordinator, installer or new domain taxonomy.
