# Bounded-autonomy capability PoC

Plan for [issue #17](https://github.com/ahmadabdalla/aasystem/issues/17), implemented on `poc/bounded-autonomy-feature-flags`. Source baseline: `96fbb9527c5d35057b4e426bcac193d1dbc38458`. Status: the user authorized the recommended native-delegation and recorded-CLI-gates follow-up, now implemented and independently verified locally. Real human response/resumption and visual inspection remain open. Native interruption and cleanup were observed; host-general and full resumed-delivery claims remain unverified.

## Outcome and correction

Build the reusable bounded-domain autonomy capability **in aasystem first**, then let the user install the changed skills independently in the website repository. The earlier plan to install unchanged skills and let website failures determine the capability is superseded by the user's explicit correction. The website exercises selected generic paths; it does not define the architecture, domain taxonomy or flag strategy.

The human remains the driver of outcomes and consequential judgment. Existing domain/task owners progress authorized work, support, verification and repair without the human managing routine handoffs. Trust comes from current inspected evidence. A concrete human checkpoint preserves one-way-door decisions, requested/procedure-required UX review and unresolved authority; asking means stop and wait.

## Selected capability slice

Use native delegation with one shared, owner-held Python-standard-library receipt helper. The existing owner handles semantics and real host execution; the helper validates recorded transitions, literal authority/resource subsets, a root-wide nonrefundable dispatch budget, current input/proof identity and human pause/resume. Returned, verified and accepted remain distinct.

```text
Human: outcome + authority + checkpoints
                  |
                  v
       Existing task / domain owner
                  |
       shared receipts + native dispatch
                  |
        bounded specialist / Implement
                  |
                  v
        fresh scoped / independent proof <----------+
                  |                                |
                  +-- failed --> scoped repair -----+
                  |
          owner inspects / accepts
                  |
                  v
       Human: result + evidence + limits

At any phase: decision / required visual review
  -> concrete package -> HUMAN -> stop and wait
  -> actual response -> resume -> current proof again

Direct specialist: same mechanism within its existing domain.
No second coordinator or launcher is introduced.
```

The owning procedure is [Bounded work](../../skills/aapilot/references/bounded-work.md), reached from Aapilot or the shared baseline for a direct specialist. No new skill, launcher, daemon, scheduler, installer, permission interpreter or domain profile taxonomy is selected. No release/version changes are planned. State and proof live outside installed skills/cache. V0 local proof uses Python 3.10+ and the available native host; actual standalone discovery and other hosts remain separate checks.

## Historical capability implementation checklist

This records the original capability delivery under [Skill authoring](../../skills/aapilot/playbooks/authoring-a-skill.md). Completed local work and its evidence remain historical; the unchecked host and website gates remain open. These entries preserve original delivery status, not the current follow-up queue; the later capability follow-up is recorded separately below.

1. **Establish the intended change**
   - [x] **Aapilot owner:** record capability-first scope and preserve the user's clarification; retain website work as a later exercise.
   - [x] **Solution/Arena support; owner acceptance:** compare bounded generic mechanisms and settle native delegation plus executable receipts. Preserve alternatives, contrary evidence and declared enforcement limits in the design record. Design selection does not establish implementation success.
   - [x] **Aapilot owner:** reconcile the frozen authority, budget, freshness, checkpoint and interruption contract with the final implemented interface and original user requirements.
2. **Edit the owning instructions**
   - [x] **Core Implement worker:** ship one coupled helper and CLI tests for initialization, event transitions, snapshots and status; no command execution or host launcher.
   - [x] **Instruction integration worker:** make the experimental mode reachable through existing entry/baseline links, with one owning receipt reference; preserve metadata, invocation adapters, domain responsibilities and ordinary/planning-only paths.
   - [x] **Instruction integration worker; owner reconciliation:** update README, system ownership, standalone Codex handoff and existing graph foundation descriptions without inventing new coordinator relationships.
3. **Validate the package**
   - [x] **Core worker; fresh verifier:** exercise actual CLI transitions for subset/deadline/budget rejection, idempotence/conflict/revision handling, explicit acceptance, checkpoint/resume and uncertain-effect reconciliation. Rejections preserve prior state.
   - [x] **Fresh verifier:** demonstrate current copied-input proof and stale detection for dirty/add/delete source, config/verifier/requirements/environment/helper and imported evidence changes; missing required inputs remain blocked.
   - [x] **Integration owner/fresh verifier:** run release/metadata/adapters/link checks and inspect final diff for duplicated or misplaced rules. Invoke the helper from a complete staged sibling-tree copy and unrelated working directory, keeping state outside that tree.
   - [ ] **User, later target host:** check actual standalone discovery, explicit invocation and supporting handoffs; local file/package checks cannot close this host gate.
4. **Exercise consequential behavior changes**
   - [x] **Aapilot owner with fresh bounded workers:** exercise an actual native-worker loop here against a disposable tiny CLI/library: create a record once; duplicate creation conflicts and leaves persisted state unchanged. Domain support settles the contract, Implement edits, a separate verifier runs real entry points and inspects effects.
   - [x] **Fresh verifier, then fresh correction worker:** expose a controlled duplicate-side-effect defect without coaching the verifier, retain the failure, correct within authority and repeat affected independent proof against the current artifact.
   - [x] **Aapilot owner/fresh verifier:** demonstrate stale-proof rejection after a dirty source change; exercise direct Architect-to-support-to-design return through the same mechanism without a second Aapilot coordinator.
   - [x] **Fresh independent assessment; owner reconciliation:** follow [Evaluation](../../skills/aapilot/playbooks/eval.md) for changed handoffs/proof behavior. Inspect actual artifacts and host assignments, record isolation/exposure and unmet claims. Synthetic human-response fixtures prove protocol only; no fabricated human/UX acceptance. No superiority claim without comparable baseline/candidate trials.
5. **Deliver for review**
   - [x] **Aapilot owner:** reconcile consequential decisions into canonical instructions/docs; arrange verification-maintenance corrections separately if recipes drift; check current combined evidence and preserve failures/reports through review.
   - [x] **Aapilot owner:** prepare the local delivery record of demonstrated paths, actual worker/dispatch/time/available usage evidence, limits, remaining gates and local delivery boundary. No commit, publication, website installation or deployment is implied.
   - [ ] **User, later:** independently install this changed skill tree into the website repository and exercise the relevant paths below. Feed observations back as bounded evidence, without redesigning the generic capability around feature flags.

## Historical completed receipt-helper refactoring checklist

This completed follow-up followed [Refactoring](../../skills/aapilot/playbooks/refactoring.md) and preserves the existing capability contract. Apply Clean Code names, focused responsibilities and readable tests alongside Pragmatic Programmer knowledge ownership, low coupling and small verified steps. File or function length alone does not justify extraction. Keep the public CLI path, arguments/help, JSON/state schemas, version, diagnostics and rejection order, exit behavior, atomic writes/locks, authority/budget/checkpoint rules and proof freshness compatible. Defects or feature ideas remain separate work.

1. **[Capture the baseline](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Aapilot owner:** retain original helper/tests, source fingerprints, the 41-test passing baseline and public CLI characterization (30 tests, 287 command records) in `/tmp/aasystem-receipts-refactor.UnK40z/`. `baseline-identity.json`, `baseline-tests.txt`, `baseline-cli-tests.txt` and `baseline-cli.jsonl` identify the inputs and observed behavior; fixture presence alone is not proof.
2. **[Name the structural improvement](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Architect support; Aapilot owner acceptance:** identify CLI transport, mutable run lifecycle and evidence/proof interpretation as distinct reader tasks. Compare in-place named helpers with a private package; the owner accepts the package to separate those concerns and reduce navigation burden under the user's monolith concern. The judge's smaller in-place preference and owner disagreement remain in the design evidence; no workflow, routing, schema or host behavior changes.
3. **[Design the target](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Architect/Arena support; Aapilot owner:** accept the same-path thin CLI with private `_work_receipts/{__init__,state,evidence}.py`: state owns mutation/commit orchestration, evidence owns input/proof interpretation and snapshot effects, and policy helpers remain explicit. Freeze interfaces, complete implementation fingerprinting and copied-tree verification in `/tmp/aasystem-receipts-refactor.UnK40z/design/design.md`; retain alternatives and contrary judgment alongside it. Design judgment does not close runtime proof.
4. **[Move in verifiable increments](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Core Implement worker:** complete mechanical extraction and readability steps while preserving every original scenario and visible persistence, locking and policy ownership. Original 30-test characterization passes after both steps; final implementation checks pass 34 affected and 45 full tests. Command logs and source identity remain in `implementation/`; the later local readability finish is retained in `readability-finish/` under the refactoring evidence root.
5. **[Prove equivalence and assess the result](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Fresh independent verifier; final confirmation auditor:** compare public CLI behavior and effects, including help/errors, replay, rejection nonmutation, state revision/history, lock cleanup, snapshots and proof freshness. Initial independent discovery is retained in `verification/report.txt`; after readability fixes, the confirmation audit passes 45 full tests, 33 baseline comparison calls without semantic differences, and 29 direct copied-tree/effect calls. `final-confirmation/equivalence-audit.json` accounts for intentional implementation/snapshot identities; `direct-result.json` records unrelated-working-directory execution, external state, copied-tree integrity and stale detection. These observations do not establish exhaustive input equivalence.
   - [x] **Fresh maintainability assessor; Aapilot owner reconciliation:** retain the source review against the simpler single-file alternative in `maintainability/review.md`: qualitative baseline 6/10 to current 8/10, no blocking findings, two P3 findings and optional local improvements. Parent-supplied comment-loss hypotheses are disclosed. The readability finish addresses both P3 findings with named scope collections, formatting and restored original rationale comments; the final audit confirms those fixes without rescoring. The retained assessment is a source judgment, not equivalence proof.
6. **[Deliver](../../skills/aapilot/playbooks/refactoring.md)**
   - [x] **Record-maintenance worker; Aapilot owner:** reconcile the CLI and two private module boundaries in the system map and owning reference, retaining operating steps and shared ownership. Final package validation passes 25 skills/adapters and 420 local paths, plus syntax and diff checks. Check this plan's links, paths, fences and final diff; preserve both diagrams, historical evidence and the website kickoff verbatim.
   - [x] **Aapilot owner:** reconcile the frozen current source against independent discovery and final confirmation evidence; retain baseline, final proof, failures and review findings through review. `final-confirmation/before-hashes.json` and `after-hashes.json` identify the same five current source/test files; this subsequent plan-only reconciliation changes only its documentation identity. Host/website and exhaustive-behavior limits remain open. Delivery is local and uncommitted, with no publication or release change.

## Current capability follow-up

The reusable findings are decision authority and evidence limits: a short kickoff does not make every delegated product or architectural choice a user-agreed requirement; announcing an assumption does not establish agreement. Verification independence covers assignment through the initial returned report, including any conclusion exposure after execution. Helper allocations and observed native dispatches are separate counters. Product acceptance does not close unexercised library gates.

The user confirmed that aapilot should pause before implementing an unresolved consequential product or architectural choice: "yes and it should ask a question or present a choice". Present a clear focused question or concrete options, adding a recommendation and tradeoffs when useful, then stop and wait for the actual human response. Routine implementation remains delegated. Use a Grill Me interview only when several linked decisions warrant it; an interview is not mandatory at every checkpoint. Preserve the generic native-delegation/stdlib-receipt foundation, current state/evidence ownership and small script responsibilities; do not add a launcher, domain taxonomy, use-case hardcoding or speculative modules.

This is the single current follow-up checklist under [Skill authoring](../../skills/aapilot/playbooks/authoring-a-skill.md). The user subsequently authorized the recommended native delegation plus recorded CLI gates, with lean, direct instructions. Shared decision rules stay in the [execution contract](../../skills/aapilot/references/execution.md); the [bounded-work reference](../../skills/aapilot/references/bounded-work.md) owns the optional protocol. [Decision context](../../skills/principle-preserve-decision-context/SKILL.md) is retained at handoffs. Delivery is local and uncommitted; no installation, publication or push is authorized here.

1. [x] **Agree decision authority and human checkpoints.** **Owner:** caller and human. The actual answer above settles the preference: ask a focused question or concrete options for unresolved consequential choices, then stop and wait. Routine details remain delegated. The later authorization selects native execution with recorded gates, not a launcher or host permission enforcement.
2. [x] **Correct acceptance/proof semantics.** **Owners:** bounded implementation and separate independent verification workers; caller reconciles acceptance. Schema 2 requires current recorded decision review, governing/design identity, mandatory checkpoint obligations, linked native reservations/results and verifier preflight. Frozen initial findings cover assignment through initial return; later clean metadata cannot erase exposure or failed claims. Final independent CLI discovery supports the exercised corrected gates; historical schema-1 state remains read-only status with current eligibility unmet. Purpose, routine-versus-consequential classification and omitted choices still require owner judgment; declarations neither authenticate humans nor intercept native tools.
3. [x] **Reduce handoff and receipt friction.** **Owners:** instruction and implementation workers; fresh verifier. Requirement-only discovery packets preserve source constraints, explicit exposure intervals and original initial findings before metadata help. Status separates allocations, observed attempts, pending reservations and remaining budget, and exposes prospective dispatch gates. Initial spawn uses its assignment allocation; continuations reserve another. Native request/result links and public CLI checks provide recorded provenance, with no claim of automatic host attestation or cost enforcement.
4. [ ] **Exercise actual human response/resumption and visual inspection.** **Owners:** caller and human, then separate execution/verification workers. Both native comparison workers asked about the unsettled external contract and paused; neither received a human answer or resumed. No behavioral superiority is established. Final-source native interruption did show a live owned process, blocked followup/retry while uncertain, and confirmed cleanup before known reconciliation. This is partial recovery evidence; an actual human choice, inspected visual evidence, response/resume and current resumed proof remain open. Use the next-exercise guidance below; synthetic answers do not close these gates.
5. [x] **Validate and deliver the authorized local change.** **Owners:** fresh independent verifier and evaluators; caller reconciliation. Final discovery ran 68 tests, independent adversarial CLI/effect probes, complete copied-tree execution from an unrelated working directory, package checks for 25 skills/adapters and 426 local paths, and publication-helper syntax checks. Frozen source bytes/modes remained unchanged. Retained initial harness faults and earlier product failures are distinguished below. Evaluation supports scoped recorded behavior only; actual host discovery, human/visual completion and general superiority remain unverified. Local implementation is complete within those limits.

## Evidence and acceptance

Retain source/worker identities, retrievable briefs, assignment/correction records, copied-input manifests, command logs, actual effects and initial failures outside maintained source through review. Use the project's [evidence retention contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention). Record unavailable access and usage as unknown rather than inferred. The decision log links exact temporary locations.

Current authorized follow-up evidence is retained through review at `/private/var/folders/q8/b5nq2zqn6m72cmd2qkt_cvb00000gn/T/aasystem-gated-work.qz1wksmp/`. `implementation/REPORT.md`, `implementation/corrections/result.json` and `implementation/final-reference.md` record implementation, retained failing-before cases and the corrected reference. Initial independent discovery in `verification/discovery/initial-findings.json` found two real bypasses: an older decision review could supersede a later unresolved choice, and changed design bytes did not block dispatch. Corrections retained those failures and passed 57 development CLI scenarios. Fresh final discovery in `verification/final-discovery/initial-findings.md` independently exercised the corrected combined artifact: 68 tests passed in 41.818 seconds, independent adversarial probes passed, and 25 skills/adapters plus 426 local paths passed package validation. `source-identity.json`, `complete-source-identity.json`, `after-input-check.json`, `repaired-tests.log`, `repaired-shipped-cli.jsonl` and `adversarial-results.json` retain identities, commands and effects. Initial copied-harness omissions caused failed tests/package checks; adding missing tracked dependencies opaquely and a local Git index repaired the harness without changing source or expectations. Those failures remain retained. The frozen source was unchanged; this subsequent plan reconciliation is excluded from the executable freeze.

`evaluation/comparison/judge.md` preserves the independent comparison: original and revised instruction workers both asked about an unresolved export contract and paused. Revised receipts represent more structured provenance; the pair establishes no behavioral superiority. `evaluation/final-native/` records an actual then-final-source spawn with live PID 2965, port 54513 and HTTP 200. After `interrupted`, followup reservation and overlapping retry rejected; unknown reconciliation kept effects uncertain. The owner inspected identity and used direct native SIGTERM outside receipt dispatch, then confirmed no process, closed port and refused HTTP before known reconciliation. Final status records one allocation, one observed started spawn, zero pending reservations and one remaining dispatch; cleanup was not another spawn/followup. This demonstrates the direct native-tool boundary as well as recorded gates, not permission enforcement or completed resumed delivery. Earlier actual spawn-plus-cleanup-followup evidence in `evaluation/native/` exercised a pre-correction frozen build and is historical. Host call IDs and usage are unavailable where recorded as unknown.

The subsequent Clean Code/Pragmatic Programmer pass is retained at `/private/var/folders/q8/b5nq2zqn6m72cmd2qkt_cvb00000gn/T/aasystem-clean-code.q9_kna_2/`. `review/initial.md` records a 7.5/10 static discovery assessment; `review/final.md` records a separate 8.5/10 confirmation assessment with disclosed exposure, not a runtime score. `implementation/report.md` records three local extractions in the receipt tests, `gates.py` and `state.py`: named fixture lifecycle stages, decision-origin validation separate from unresolved-choice continuity, and resumed-brief validation separate from state writes. No module, CLI, schema, instruction or ownership change was introduced. The 68-test baseline and three incremental 57-test development runs precede fresh independent verification in `verification/initial-findings.json`: 68 tests passed in 42.967 seconds, exact comparisons passed for 62 helper calls and 124 fixture calls without output/state normalization, six adversarial CLI probes passed, and 25 skills/adapters plus 426 local paths passed package checks with shell syntax and 114-input integrity checks. The verifier corrected initial execution of preserved baseline inputs by rerunning writable copies; original inputs remained unchanged and the procedure correction was not a product failure. These finite comparisons support the local refactor, not exhaustive equivalence. The current portable source differs from the preceding implementation freeze only by this refactor; native exercises above identify historical bytes and were not rerun. Real human resumption, visual review and host gates remain open. Delivery remains local and uncommitted; retain the evidence through review.

The older refactor and capability proof below are historical evidence for their identified source, no longer proof of the current implementation. The current helper retains the thin CLI and adds private `gates.py` for read-only policy checks alongside state mutation and evidence responsibilities; the system map records these current boundaries. Schema 2 applies to new runs; snapshot schema remains 1. No launcher, host permission enforcement, human authentication or omitted-semantic-choice detection is claimed.

Receipt-helper refactor evidence is separately retained at `/tmp/aasystem-receipts-refactor.UnK40z/`; it records the then-current helper identity and historical capability proof below. At that point the same CLI delegated to private state and evidence modules. `baseline-identity.json` and baseline logs preserve the original 41-test source; `design/design.md` retains the judge's single-file preference and the owner's accepted two-module rationale. Incremental implementation logs, `maintainability/review.md` and `readability-finish/final-source-freeze.json` retain the changes, qualitative 6/10-to-8/10 assessment, disclosed review exposure and both P3 fixes. The five historical source/test hashes are in `final-confirmation/after-hashes.json` and match `before-hashes.json`. The final confirmation audit in `final-confirmation/report.txt` records 45 passing full tests in that directory's `full-tests.log`, 33 baseline calls with no semantic differences in `equivalence-audit.json`, and 29 copied-tree/effect calls in `direct-result.json` and `direct-trace.json`; `commands.json`, `release-validator.log`, `publish-syntax.log`, `source-diff-checks.json` and `diff-check.log` retain command, package and source checks. Earlier independent discovery remains in `verification/report.txt`, including retained harness faults; `decisions.tsv` records final owner reconciliation. Final confirmation verifies the readability fixes and retained assessment, without a new score or independent rediscovery claim. Synthetic protocol fixtures do not prove genuine human resumption, standalone host discovery, website behavior or exhaustive equivalence. This is local uncommitted delivery, with no commit, release, installation or deployment. The parent retains this temporary evidence through review; these paths are not installation dependencies.

The original local implementation and affected verification completed within their exercised scope. The first pass (32 tests, 70 CLI probes and an 87-file/mode staged tree) was followed by independent discovery of three real receipt defects: invalid accepted-child evidence, overlapping-resource uncertainty and cancelled-task supersession. Their failures remain retained; the corrected helper passed 41 tests, six focused audit groups through 123 public CLI invocations, release/metadata/adapters/local-link checks and syntax checks. A complete documented export ran its copied helper from an unrelated working directory with external state. This corrected-gate audit was confirmation, not independent defect discovery. Retained harness failures and corrected expectations are disclosed separately from product defects.

The disposable native record CLI preserved the original requirements and verifier: initial executable proof found 15 passing and two failing checks; a bounded correction moved duplicate rejection before persistence; final separate-workspace executable proof passed all 17 checks with protected archive/live-input identity evidence and explicit owner acceptance at revision 11. Four of five recorded dispatch allocations were consumed. A direct Architect owner separately returned and accepted a design-only package through one scoped review child, consuming one of two allocations. That review was confirmation exposed to the design conclusions; it established no production behavior. Actual usage is unknown. Retained execution records report final CLI runtime of about 0.29 seconds and the 41-test suite of about 21.6 seconds; these are measured checks, not whole-session cost or elapsed-time claims.

Fresh closeout status distinguishes acceptance history from current authority: the native run remains historically accepted and its proof verifies, but its deadline has elapsed, so it is no longer currently accepted/eligible. Its retained final status records the earlier within-deadline acceptance. The direct Architect root was currently accepted when inspected. No deadline or budget was extended. The fresh judge supports the observed local protocol/artifacts; complete independent host-dispatch attestation remains inconclusive. The owner reports actual fork-none child dispatch returns and final answers in its conversation, but no retained host transcript or host-issued call IDs are available outside it; original children are absent from current host inventory for an unknown reason. Filesystem host-reference records are declarations. Parent observed the direct Architect review child in scoped inventory. Shared-filesystem isolation is procedural; owner exposure to unrelated agent summaries is disclosed in the retained context limits.

Temporary evidence root: `/tmp/aasystem-autonomy-capability.R2yHhD/`. The canonical local decision log is `decisions.tsv`; original failures are in `verification/verification-report.json` and `review/independent-discovery.md`; corrected public command/effect proof is in `final-verification/report.md`, `results.json`, `commands.jsonl` and `source-identity.json`; actual task proof and acceptance are in `native-work/runtime/delivery.json`, `verify-initial-report.json`, `verify-final-report.json` and `state.json`; scoped design is in `direct-architect/artifacts/design.md` and `runtime/review-report.json`. Fresh single-candidate judgment, separate log audit and present status are in `closeout/`. `combined-source-v2.json` identifies the tested source; this subsequent plan-only reconciliation changes its documentation hash. These temporary paths support review and retention, not portable installation dependencies. The parent retains evidence through review; no disposal is authorized here.

Skill-creator's strict `quick_validate.py` was run in an isolated PyYAML environment and rejects the existing `disable-model-invocation` field on both HEAD baseline and candidate. The repository's Ruby metadata validator supports this deliberate host extension; preserve the metadata and invocation adapters. This format distinction does not close actual host discovery.

A helper passing its structural tests does not prove autonomous ownership, genuine worker independence, semantic truth or correct host permissions. Local native-worker exercises add evidence for the paths actually run. Real human resumption, UX eyeballing, remote environments, session survival and standalone host discovery remain unverified until observed. Comparable baseline trials are needed to claim improvement over native delegation alone.

## Next bounded-work exercise

Use **any suitable bounded feature** in the target repository; feature flags are only the historical example below. Describe the desired outcome and let the skill discover repository context, approach and proof. Keep use-case knowledge in that repository, outside the exported skills.

```text
$aapilot Use bounded work to [describe the feature you want].
```

To exercise the remaining checkpoint gate, choose work with a genuine unresolved consequential choice: observe a focused question or options, stop and wait, an actual human answer, resumed work and fresh independent proof. For the visual gate, choose work with applicable visual review and actually inspect the rendered result. A feature with settled choices may correctly proceed without asking and leave the checkpoint gate open; do not manufacture a choice. One exercise need not cover both gates.

Record only observed results. Actual host discovery and supporting handoffs, human response/resumption, visual inspection and current proof remain open until exercised; a successful feature alone does not close them.

## Original later website exercise brief

The following is the original exercise brief, retained as historical intent. It does not establish website completion or close unexercised human or host-general gates.

The user reports a website with dev and prod deployments, shared repository/code and existing feature flags. Framework, hosting, pipeline, flag evaluation model and affected feature are unknown. The eventual website owner discovers those facts in that repository; no provider or implementation strategy is chosen here.

```text
                     Shared repository / code
                               |
                      existing build / pipeline
                               |
                  +------------+------------+
                  |                         |
             DEV deployment            PROD deployment
             feature: ON               feature: OFF
                  |                         |
             dev validation            existing experience

       Discover build/runtime configuration and promotion first.
       Exercise existing domain owners and shared receipt paths.
```

| Capability path exercised | Website application / observations |
| --- | --- |
| Investigation and bounded domain support | Trace existing flags, configuration, pipeline and affected entry points; return evidence-linked unknowns and recommended scope. |
| Design and authority checkpoint | Settle feature exposure semantics, promotion model and rollback; return consequential choices before crossing authority. |
| Implementation and current independent proof | Uplift authorized flags/pipeline; prove dev-on/prod-off, applicable APIs/effects, config failures and unaffected journeys against identified source/config/environment. |
| Repair and affected re-verification | Correct observed failures within scope; keep failed evidence and repeat current independent checks. |
| Human review/resumption | Present actual material UX or consequential choices if reached; preserve approved context and recheck proof after real human input. |

These are proposed exercise paths, not preaccepted website requirements. The owner adapts expectations to actual project behavior. Hiding UI alone cannot prove applicable server/pipeline claims. Live deployments/configuration changes and enabling unfinished functionality in prod require authority supplied in that repository; this plan grants none.

## Installation and invocation handoff

After the local capability evidence is reviewed, the user installs the **changed branch's complete `skills/` tree** together, with sibling references, helper, assets/adapters and license notices. Record the exact revision plus local differences. Use the target host's supported standalone discovery and [Codex guidance](../../CODEX.md); keep run state in the target project's evidence location, outside installed skills/cache. The user checks actual discovery and supporting-skill access.

The original feature-flag kickoff is retained as a historical example; use the generic prompt above for the next exercise:

```text
$aapilot Use bounded work to improve our feature flags and dev-to-prod
pipeline so we can promote shared code while keeping unfinished features
enabled only in dev.
```

The aasystem capability proof establishes no website outcome. Website results and project-specific evidence belong in the target repository; the library gates above remain open until exercised.
