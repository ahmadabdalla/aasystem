---
name: 10x
description: Assess a decision or design under plausible growth, exposing its first constraints, tradeoffs, verification needs, and reconsideration triggers. Use within domain design or as a bounded independent challenge.
disable-model-invocation: true
---

# 10x

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Assess how growth affects the supplied decision or options. The caller owns the decision and integrates the findings. Use the same method for an independent assignment; invocation alone requires no additional agent.

## Assess the decision

Read the intended outcome, options, constraints, existing rationale and evidence. Reuse a current assessment; extend it only for changed assumptions or constraints. Routine edits that preserve the decision need no new assessment.

Identify the growth dimensions that could change the choice: collection size, request rate, concurrency, workflow complexity, cost or operating effort. State the current baseline and a plausible larger scenario. Use 10× as a prompt; choose another factor when it better tests the decision and explain why. Label assumed quantities and unknown baselines. Separate data volume from request rate and concurrency; do not infer proportional latency or measured capacity from a multiplier.

For each material scenario, return:

- **Scenario:** What grows, from what baseline to what level, and why it matters to this outcome.
- **First constraint:** What becomes slow, confusing, costly or unreliable first, why, and what must remain true. Cite supporting evidence or mark the claim as an estimate or unresolved assumption.
- **Decision:** What to accommodate now, what to defer, and why. Compare the supplied options where this changes their ranking. Added complexity needs a concrete benefit; hypothetical growth alone is insufficient.
- **Proof and trigger:** The input or action and expected observable result needed to check a consequential assumption, what remains unverified, and an observable condition for reconsidering the decision. Mark proposed targets separately from accepted requirements. Link detailed checks in the existing verification plan.

If no relevant growth scenario changes the decision, give the reason briefly. Do not invent a bottleneck or a capacity guarantee.

## Return to the caller

Keep findings in the caller's existing rationale or return them for integration. Reuse canonical findings across solution, interaction and technical design; assess only newly exposed constraints. An assessment does not require a separate report or ADR.

Carry accepted constraints and required checks into the design and verification handoff, with their sources and evidence limits. A deferred growth target is not a release requirement. Return changes to scope or required behavior through the caller under the shared decision-authority rules. Design reasoning does not establish observed capacity; run checks only within the assigned scope.
