# Execution contract

**Baseline.** Before acting, read this contract in full, the [approved-principle index](../../principles/INDEX.md) and relevant principle leaves. Apply them within your assigned role and authorized scope. Reuse instructions already in context; every fresh worker loads its own baseline.

## Ownership and handoffs

Supporting skills return findings to the current owner. That owner consolidates requirements, terminology, consequential decisions and unresolved risks into canonical project records within scope, preserving sources, authority, rationale and evidence limits. Route reusable learning through [reflect](../../reflect/SKILL.md). Working records may stay in conversation; skill invocation alone requires no separate report. Follow the selected workflow's artifact requirements, including [show-me-your-work](../../show-me-your-work/SKILL.md)'s local log and retention rules.

Retain a separate supporting artifact only when canonical records inadequately serve an identified future reader and decision, operating procedure, verification need or audit obligation. Reuse project locations and link rather than copy evidence. Other notes and review transcripts are temporary. This does not authorize deleting existing records or evidence needed to substantiate results.

Keep owner, objective, constraints, evidence and limits, applicable principles, expected results and next action in one brief. Reuse settled grounding. Give each contributor a bounded deliverable, a work or time budget, accessible evidence and artifact paths, write ownership and a verification method; specify what it must return. Every worker, including nested delegates, must load the baseline and read its procedure and relevant project instructions before work. Give workers accessible paths, the current brief and later corrections; restrict execution to the assigned phase. Workers return out-of-scope findings to the caller with evidence and a proposed assignment; they do not start that workflow. Helpers may compose bounded support under the same caller and checkpoint.

The lead owns framing, assignments, integration, acceptance, final proof and design decisions within its recorded authority.

## Delegation

1. **Check capability.** At workflow start, identify the agent tool, delegation restrictions and access workers need. Check supporting procedures too. Use configured or permitted inherited models; do not invent diversity.
2. **Assign execution.** Delegate investigation, design, implementation and record maintenance using the selected procedures. Workers execute their assigned scope; supporting delegation follows their procedure. The lead executes directly only under an explicit procedure exception or a concrete delegation limitation. Name the exception, missing tool, delegation restriction, denied access or failed dispatch.
3. **Structure the work.** For nontrivial implementation, record blocking prerequisites, independent workstreams, shared mutable state and the smallest safe decomposition. Explain any choice to use one worker; revisit the structure at phase changes. Complete blockers first. Give coupled work to one worker; parallelize independent ready assignments within actual limits. Sequence work when slots are occupied. Workers unable to spawn return required supporting assignments to their caller.
4. **Accept results.** Inspect returned artifacts and evidence against completion criteria before advancing. Assign corrections with the updated brief. Self-review cannot satisfy a required independent gate; keep it incomplete when independence cannot be achieved.

Route large documents, verbose outputs, screenshots and broad exploration to bounded subagents. Give them artifact pointers and the consolidated brief; request concise findings, evidence paths and gaps. Without delegation, narrow reads and save bulky output to files.

Use [swarm](../../swarm/SKILL.md) for partitioned work or coverage and [arena](../../arena/SKILL.md) for competing alternatives and synthesis. Use a fresh worker for every new assignment, including fixes and retries. Resume a worker only when its live process, local changes or costly state is necessary. Transfer the consolidated brief and corrections; select review inputs under the [review-context rule](#review-context). Tell workers they share the codebase, must preserve others' changes and return actual artifacts and evidence. Give parallel writers separate artifacts or explicitly nonoverlapping sections; serialize shared canonical sections. Before integration, check each returned brief and source revision against current task/project records, including the latest assigned proposal. Preserve proposed versus accepted status; recheck stale or conflicting findings.

Workflow configuration does not authorize unavailable tools or external actions.

## Review context

Label review assignments as independent discovery or confirmation/evidence audit. An open search for weaknesses uses discovery; checking specified claims uses an audit.

For independent discovery, supply the objective, authoritative requirements, accepted constraints, source identity, original artifacts, and evidence/access limits. Exclude lead conclusions, suggested answers, earlier reviewer findings, and inherited discussion. Keep these inputs and the original artifact intact. If the artifact or host exposes prior assessments, identify that exposure in the review report.

Start each reviewer without the parent conversation. If the host cannot exclude it, report which prior context the reviewer receives. Do not share findings between reviewers until all initial reports return. Then compare the reports against evidence. A fresh worker or different model alone does not establish independent discovery. Report isolation limits.

For a confirmation/evidence audit, supply claims and sources, authoritative requirements and original evidence. Treat claims as hypotheses. Derive expected results from requirements, examine supporting and contradictory evidence, and report supported, contradicted, or inconclusive results. Audit agreement does not establish independent discovery.

For independent corroboration of a lead conclusion, collect and retain initial discovery reports before revealing it. A confirmation/evidence audit needs no preceding discovery review. Model diversity is optional.

## Verification through the project

Read authoritative product requirements and any active change; preserve sources, status, invariants and unresolved decisions. For OpenSpec projects or requested adoption, read the [OpenSpec reference](openspec.md) within your role.

Read the relevant project glossary and current ADRs. Carry accepted constraints and unresolved assumptions into the task brief; surface contradictions before changing behavior. Use [domain-modeling](../../domain-modeling/SKILL.md) to clarify or record them when needed.

Before product changes, locate the verifier and feature map; identify affected outcomes, alternate entry points, dependent callers and coverage gaps. If no usable proof path exists, use [bootstrap-verification](../../bootstrap-verification/SKILL.md) within scope. A scoped verifier can suffice without whole-project setup. Prescribed low-impact presentation edits may use existing source/diff checks and an available preview; a missing formal verifier alone does not require scaffolding. Unexercised appearance and behavior remain unverified. For design-only work, record missing proof without starting implementation.

Before editing, derive expected results from requirements or the contract. Exercise the real UI, CLI, API or library entry point and inspect side effects. Follow verifier readiness, instance identity, isolation, reset, evidence and cleanup procedures. Recheck health and reset state before interpreting surprising results. Mocks, builds and worker summaries cannot prove unexercised boundaries.

Follow project evidence procedures and the [evidence contract](../../bootstrap-verification/references/project-contract.md#evidence-and-retention) for claim strength, run locations, review retention and disposal. Distinguish harness faults, product defects and missing access. Use [maintain-verification](../../maintain-verification/SKILL.md) for recipe drift. Never change expectations to hide regressions; record authority for intentional changes. Update and recheck affected feature recipes when behavior or procedure changes; unchanged runs need no permanent map edit.

Verify each meaningful unit and the final combined artifact under the [independent implementation verification procedure](#independent-implementation-verification) when applicable. Clean up only owned resources; confirm evidence survives. Identify unverified claims in partial results.

## Independent implementation verification

For production implementation, the owner dispatches a fresh verifier separate from product editors; development checks cannot satisfy this gate. The [prescribed presentation exception](#verification-through-the-project) may stay with the lead; record why it applies and any unexercised claims. Design-only and throwaway experiments retain their own evidence scope.

Follow [Delegation](#delegation) and [Review context](#review-context). Include the combined artifact’s exact revision or source identity, relevant baseline or reproduction, project verifier and affected recipes, surface and side-effect expectations, environment/access limits, evidence destination, and cleanup ownership. For discovery, exclude implementation conclusions and development pass claims until the initial report; retain original requirements, constraints, contracts, and runnable recipes. Audits may receive claims and sources; disclose that mode and its limits.

The verifier follows [project verification](#verification-through-the-project) against the actual artifact and returns each claim's pass, fail, or unverified result, observations and evidence, tested source identity, coverage and isolation limits. It changes neither product code nor expectations. It returns harness drift for separate [Maintain Verification](../../maintain-verification/SKILL.md) correction; blocked product claims remain unverified.

The owner reconciles the report, assigns product corrections through the change workflow, and reruns affected independent proof on the current combined artifact after material changes. Acceptance requires evidence for the current artifact. Missing delegation, runtime access, or usable proof leaves the gate unmet. [Interrogate](../../interrogate/SKILL.md) provides adversarial review, not executable verification.

## Completion

Plan applicable decision reconciliation, verification maintenance and evidence retention in the existing task list, with owners and completion criteria. Delegate under the procedure above.

Before reporting completion, check required results, reconcile consequential findings into canonical records, and verify affected references. Report incomplete assignments and unmet gates within the requested scope and delivery boundary.

## Delivery

Follow the requested delivery boundary and repository conventions. Local edits, commits, PR creation, monitoring and merging are distinct actions. Use [Opening a PR](../playbooks/opening-a-pr.md) when authorized. For commits, retain failing-before evidence and verifiable change order; never rewrite shared history to manufacture it. Read-only work ends with its answer.
