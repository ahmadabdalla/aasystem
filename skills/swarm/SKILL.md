---
name: swarm
description: Coordinate independent work slices or declared races and return one evidence-backed coverage report. Use for parallel investigation, implementation partitions, or coverage; use arena to compare and synthesize competing designs or artifacts.
disable-model-invocation: true
---

# Swarm

Before starting, read the [shared execution contract](../pilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Frame the work, run bounded workers, account for every required result, and return one report. Delegation requires actual host capability and authorization.

## Frame

Reuse the caller's brief and name the completion predicate and required artifact. Choose partitioned coverage, a race, or a mixture. Declare the race rule before results: first verified pass, rank all, or select best. For ranking or selecting the best, include the comparison criteria in that declared rule. For candidates that need comparison and grafting, use [arena](../arena/SKILL.md).

Build a small coverage table with each slice, owner, inputs, writable location, expected result, and proof method. Complete blocking prerequisites before fan-out. Assign separate writable outputs or worktrees; serialize genuinely shared mutable state. The lead integrates results and proves the combined artifact.

## Run

Give each worker a self-contained brief: goal, scope, constraints, accessible raw artifacts, applicable principles, exact version or source identity, ownership, and verification/reporting requirements. Tell workers they share the codebase and must preserve others' changes. Measurement briefs specify method, units, sample conditions, and comparison order.

Use available configured models and independent contexts; do not hard-code unavailable models or fabricate diversity. Launch independent ready slices concurrently within limits. Keep coupled work with one owner. If delegation is unavailable, perform the slices serially, account for the same coverage, and label the loss of independence and parallel execution.

Require each result to distinguish **pass**, **issues**, and **blocked**, with artifacts, evidence, and source identity. An evidence-backed defect is a useful result. A worker's assurance alone is insufficient.

## Aggregate and report

Read every result and inspect material claims in the artifacts. Reject a result missing required source identity or method; request one bounded repair where supported, then preserve the gap. A dropout is not a pass. Coverage completes only when every required slice has an adequate result; races follow the declared rule. Stop outstanding race workers only when the rule permits it and preserve their owned work and resources.

Reconcile conflicts, integrate authorized changes, and recheck the combined artifact through the project verifier when code changed. Return one compact coverage table, consequential findings, evidence links, dropouts, and unresolved gaps to the caller. Do not silently convert partial coverage into a completed audit.
