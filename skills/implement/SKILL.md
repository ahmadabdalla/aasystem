---
name: implement
description: Make bounded production edits and run development checks against a supplied contract or settled design. Use for assigned implementation, corrections, and mechanical refactoring; return artifact and evidence to the caller. Architect owns design; the caller owns acceptance.
disable-model-invocation: true
---

# Implement

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own assigned edits and development evidence; the caller owns integration, acceptance, and [independent verification](../aapilot/references/execution.md#independent-implementation-verification). Return into the caller’s task without starting another coordinator.

## Establish the assignment

Use the assigned brief and retrieve its linked inputs before editing: behavior contract, settled design when needed, source identity, file ownership, invariants, compatibility, permitted effects, checks, and evidence destination. Return material conflicts or missing prerequisites to the owner; a routine local correction needs no architecture package.

Before choosing local structure, read Maintainability's [local-code criteria](../maintainability/references/local-code.md); read its [boundary criteria](../maintainability/references/boundaries.md) when the assignment touches callers, owned knowledge, or invariant enforcement. Use the relevant criteria in the edits and return material tradeoffs with the rationale. This consumes shared criteria within Implement's scope; it does not start another assessment workflow or reopen settled design.

For an assigned structural improvement, read [Refactoring moves](references/refactoring-moves.md) and use the relevant move within the settled target. Return its compatibility impact and development evidence to the caller.

For a direct invocation meeting [owner-presentation eligibility](../aapilot/references/execution.md#owner-presentation-eligibility), own the request, execute it directly and return the actual diff/preview checks and limitations under the [verification contract](../aapilot/references/verification-contract.md); no coordinator wrapper or worker is required. For other direct invocations without an execution assignment, the invoking lead remains the sole coordinator: select the change playbook through [aapilot](../aapilot/SKILL.md), execute or assign Implement under the shared delegation rule, then arrange verification and acceptance. An assigned worker executes and returns to its owner; it starts neither another workflow nor another Implement wrapper. Follow the contract’s [delegation and invocation rules](../aapilot/references/execution.md#delegation).

## Execute and return

Apply the caller’s decomposition: [swarm](../swarm/SKILL.md) for independent slices, [arena](../arena/SKILL.md) for unsettled alternatives selected under the shared comparison rule. Preserve other contributors’ work and project formats. Return material design contradictions to the owner for [architect](../architect/SKILL.md) revision; report discovered defects separately instead of changing scope or behavior. Before returning, inspect the actual diff against the assignment and remove owned speculative abstractions, unrelated cleanup, and investigation-only changes; return any needed scope expansion to the owner before making it.

Run assigned checks after meaningful units, including the refactoring baseline or failing reproduction for corrections. Follow [project verification and evidence rules](../aapilot/references/execution.md#verification-through-the-project) for observations, source identity, failure classification, and unchanged expectations.

Return the changed artifact and final source identity, change rationale, executed checks and evidence paths, failures, unverified boundaries, and design concerns. Development passes do not satisfy a required independent gate.
