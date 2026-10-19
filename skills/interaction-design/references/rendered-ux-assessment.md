# Independent rendered UX assessment

Use for an assigned assessment of an existing rendered interface, including a prototype or production candidate. Return evidence-backed findings about the person's task. An approved visual reference is optional. This procedure owns the assessment setup and reconciliation; the caller retains the task and delivery.

## Prepare the two assignments

Reuse the actor, current job, intended behavior, requirements, accepted presentation constraints, shared components and review scope. Retrieve existing context and preserve material unknowns under the [execution contract](../../aapilot/references/execution.md#scope-and-proof). Identify the source revision and running instance using the project's preview/verifier, readiness and reset procedures. Pause source edits during assessment.

Choose discriminating states from expected use: empty, representative and mature collections; long or repeated labels; validation; selection changes; and navigation away and back. Assess finding and understanding records at scale as well as adding them. Assign relevant narrow layouts, supported themes, keyboard and motion settings proportionally. Fixture quantities are illustrative, not fixed thresholds or proof of capacity.

Launch **exactly two fresh assessors in parallel**, separate from every producer of the assessed work:

| Assessor | Assignment and rubric | Responsibility boundary |
| --- | --- | --- |
| Visual composition | [Visual assessment](visual-assessment.md) | Hierarchy, balance, alignment, spacing, typography, useful content, visual meaning, contrast and responsive composition. |
| Interaction and continuity | [Interaction assessment](interaction-assessment.md) | Affordances and control states, feedback, motion, stable controls, retrieval, navigation, keyboard continuity and reduced motion. |

Use [independent-discovery inputs](../../aapilot/references/execution.md#review-context). Give each assessor the grounded scope, authoritative sources, accepted constraints, source/instance identity, access and reset instructions, assigned states, applicable principle leaves, its own domain reference, the boundary table above and the evidence/return section below. Withhold producer discussion, proposed findings and the other assessor's conclusions. Each assessor applies its own rubric; it does not coordinate another assessment, edit the interface or redesign another domain.

Give each assessor a separate browser session and isolated mutable fixture state, using synthetic data and existing project facilities. Disjoint fixture records may suffice; separate tabs alone do not isolate a shared backend. Confirm their actions and resets cannot interfere. Source files remain shared and read-only; do not create full workspace copies just for these assignments.

If two separate nonproducer contexts, safe parallel access or required rendering tools are unavailable, return the missing prerequisite and mark the assessment incomplete. Do not replace either assessor with the producer or label sequential work parallel. Static evidence can support a scoped visual result, while unexercised interaction coverage remains unverified.

## Evidence and return

This section applies to both assessors. Use the caller's existing report/evidence format and [retention rules](../../bootstrap-verification/references/project-contract.md#evidence-and-retention).

For each finding, identify the surface, state and action; expected basis; observation; user impact and priority; supporting evidence; recommendation; and responsible owner. Distinguish an observed defect, a reasoned design concern and an unverified question. A concern may challenge an accepted design without becoming an authorized change. An empty findings list is valid; do not manufacture defects or aesthetic scores.

Assess shared components and affected sibling surfaces before recommending a local patch. Countercheck tradeoffs: stabilizing a control must not hide content, obscure overflow or disrupt task/keyboard continuity. Put observations belonging to the other domain in a separate handoff note; the caller routes them without expanding this assignment.

Report actual source/instance identity, actions and states exercised, viewport/theme/data volumes, omitted coverage, access and independence limits, evidence locations and owned-resource disposition. Screenshots establish visible composition; motion, hover, focus return, saving and navigation require exercised observations. A build or screenshot match does not establish qualitative clarity. Model agreement does not establish participant usability or human preference.

## Reconcile and hand back

Preserve both initial reports before sharing findings or editing summaries. Inspect material claims against the identified artifact and evidence. Deduplicate related findings while preserving their domain observations; resolve conflicting recommendations against the person's task and accepted constraints rather than counting votes. Record dispositions and unresolved questions in the caller's existing record.

Return changed business meaning to Product and interaction/presentation choices to Interaction Design through the caller. Assessors recommend; the caller owns decisions and authorized remediation. Keep required human checkpoints and [independent implementation verification](../../aapilot/references/execution.md#independent-implementation-verification). This assessment does not itself establish production correctness or human acceptance.

After authorized fixes, recheck the changed combined result in affected domains, using separate nonproducer assessors. Label a recheck receiving earlier findings a confirmation audit. A new complete independent assessment still follows the two parallel assignments above; targeted rechecks do not inherit unexercised coverage. Follow shared completion and resource/evidence rules when returning to the caller.
