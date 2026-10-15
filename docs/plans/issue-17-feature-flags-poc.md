# Bounded-autonomy capability PoC

Plan for [issue #17](https://github.com/ahmadabdalla/aasystem/issues/17), implemented on `poc/bounded-autonomy-feature-flags`. Source baseline: `96fbb9527c5d35057b4e426bcac193d1dbc38458`. Status: reusable capability implemented and locally exercised; review evidence retained with the limits below. Actual standalone host discovery, genuine human/UX resumption and website installation/behavior remain unverified.

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

## Capability implementation checklist

This records the original capability delivery under [Skill authoring](../../skills/aapilot/playbooks/authoring-a-skill.md). Completed local work and its evidence remain historical; the unchecked host and website gates remain open. The active structural follow-up is recorded below.

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

## Active receipt-helper refactoring checklist

This follow-up follows [Refactoring](../../skills/aapilot/playbooks/refactoring.md) and preserves the existing capability contract. Apply Clean Code names, focused responsibilities and readable tests alongside Pragmatic Programmer knowledge ownership, low coupling and small verified steps. File or function length alone does not justify extraction. Keep the public CLI path, arguments/help, JSON/state schemas, version, diagnostics and rejection order, exit behavior, atomic writes/locks, authority/budget/checkpoint rules and proof freshness compatible. Defects or feature ideas remain separate work.

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

## Evidence and acceptance

Retain source/worker identities, retrievable briefs, assignment/correction records, copied-input manifests, command logs, actual effects and initial failures outside maintained source through review. Use the project's [evidence retention contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention). Record unavailable access and usage as unknown rather than inferred. The decision log links exact temporary locations.

Receipt-helper refactor evidence is separately retained at `/tmp/aasystem-receipts-refactor.UnK40z/`; it supersedes the earlier helper identity for current code while preserving the historical capability proof below. The same CLI now delegates to private state and evidence modules. `baseline-identity.json` and baseline logs preserve the original 41-test source; `design/design.md` retains the judge's single-file preference and the owner's accepted two-module rationale. Incremental implementation logs, `maintainability/review.md` and `readability-finish/final-source-freeze.json` retain the changes, qualitative 6/10-to-8/10 assessment, disclosed review exposure and both P3 fixes. The current five source/test hashes are in `final-confirmation/after-hashes.json` and match `before-hashes.json`. The final confirmation audit in `final-confirmation/report.txt` records 45 passing full tests in that directory's `full-tests.log`, 33 baseline calls with no semantic differences in `equivalence-audit.json`, and 29 copied-tree/effect calls in `direct-result.json` and `direct-trace.json`; `commands.json`, `release-validator.log`, `publish-syntax.log`, `source-diff-checks.json` and `diff-check.log` retain command, package and source checks. Earlier independent discovery remains in `verification/report.txt`, including retained harness faults; `decisions.tsv` records final owner reconciliation. Final confirmation verifies the readability fixes and retained assessment, without a new score or independent rediscovery claim. Synthetic protocol fixtures do not prove genuine human resumption, standalone host discovery, website behavior or exhaustive equivalence. This is local uncommitted delivery, with no commit, release, installation or deployment. The parent retains this temporary evidence through review; these paths are not installation dependencies.

Local implementation and affected verification are complete within the exercised scope. The first pass (32 tests, 70 CLI probes and an 87-file/mode staged tree) was followed by independent discovery of three real receipt defects: invalid accepted-child evidence, overlapping-resource uncertainty and cancelled-task supersession. Their failures remain retained; the corrected helper passed 41 tests, six focused audit groups through 123 public CLI invocations, release/metadata/adapters/local-link checks and syntax checks. A complete documented export ran its copied helper from an unrelated working directory with external state. This corrected-gate audit was confirmation, not independent defect discovery. Retained harness failures and corrected expectations are disclosed separately from product defects.

The disposable native record CLI preserved the original requirements and verifier: initial executable proof found 15 passing and two failing checks; a bounded correction moved duplicate rejection before persistence; final separate-workspace executable proof passed all 17 checks with protected archive/live-input identity evidence and explicit owner acceptance at revision 11. Four of five recorded dispatch allocations were consumed. A direct Architect owner separately returned and accepted a design-only package through one scoped review child, consuming one of two allocations. That review was confirmation exposed to the design conclusions; it established no production behavior. Actual usage is unknown. Retained execution records report final CLI runtime of about 0.29 seconds and the 41-test suite of about 21.6 seconds; these are measured checks, not whole-session cost or elapsed-time claims.

Fresh closeout status distinguishes acceptance history from current authority: the native run remains historically accepted and its proof verifies, but its deadline has elapsed, so it is no longer currently accepted/eligible. Its retained final status records the earlier within-deadline acceptance. The direct Architect root was currently accepted when inspected. No deadline or budget was extended. The fresh judge supports the observed local protocol/artifacts; complete independent host-dispatch attestation remains inconclusive. The owner reports actual fork-none child dispatch returns and final answers in its conversation, but no retained host transcript or host-issued call IDs are available outside it; original children are absent from current host inventory for an unknown reason. Filesystem host-reference records are declarations. Parent observed the direct Architect review child in scoped inventory. Shared-filesystem isolation is procedural; owner exposure to unrelated agent summaries is disclosed in the retained context limits.

Temporary evidence root: `/tmp/aasystem-autonomy-capability.R2yHhD/`. The canonical local decision log is `decisions.tsv`; original failures are in `verification/verification-report.json` and `review/independent-discovery.md`; corrected public command/effect proof is in `final-verification/report.md`, `results.json`, `commands.jsonl` and `source-identity.json`; actual task proof and acceptance are in `native-work/runtime/delivery.json`, `verify-initial-report.json`, `verify-final-report.json` and `state.json`; scoped design is in `direct-architect/artifacts/design.md` and `runtime/review-report.json`. Fresh single-candidate judgment, separate log audit and present status are in `closeout/`. `combined-source-v2.json` identifies the tested source; this subsequent plan-only reconciliation changes its documentation hash. These temporary paths support review and retention, not portable installation dependencies. The parent retains evidence through review; no disposal is authorized here.

Skill-creator's strict `quick_validate.py` was run in an isolated PyYAML environment and rejects the existing `disable-model-invocation` field on both HEAD baseline and candidate. The repository's Ruby metadata validator supports this deliberate host extension; preserve the metadata and invocation adapters. This format distinction does not close actual host discovery.

A helper passing its structural tests does not prove autonomous ownership, genuine worker independence, semantic truth or correct host permissions. Local native-worker exercises add evidence for the paths actually run. Real human resumption, UX eyeballing, remote environments, session survival and standalone host discovery remain unverified until observed. Comparable baseline trials are needed to claim improvement over native delegation alone.

## Later website exercise

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

The website kickoff names the capability and desired outcome; the skill handles repository discovery, approach and proof:

```text
$aapilot Use bounded work to improve our feature flags and dev-to-prod
pipeline so we can promote shared code while keeping unfinished features
enabled only in dev.
```

No website outcome is claimed by this aasystem PoC.
