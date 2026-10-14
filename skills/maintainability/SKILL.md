---
name: maintainability
description: Assess the effort needed to understand, change, and verify supplied code or an implementation design. Use for bounded structural assessments, refactoring targets, and code review; the caller retains design choices and implementation.
disable-model-invocation: true
---

# Maintainability

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract's baseline requirements, delegation procedure, and review-context rule.

Assess the supplied artifact against the intended change and project constraints. Return findings to the current owner; this assignment does not select a workflow, choose the design, or authorize edits.

## Establish and inspect

Use the caller's artifact path and revision, assignment phase, intended behavior, accepted constraints, relevant callers, and evidence limits. Preserve existing compatibility requirements and known defects. Identify missing evidence that could change the assessment; do not treat an inaccessible caller as absent. Reuse a settled assessment for unchanged scope and evidence.

Read only the criteria relevant to the assignment:

- [Local code](references/local-code.md) for names, function responsibilities, control flow, effects, duplication, and test clarity.
- [Boundaries](references/boundaries.md) for caller burden, knowledge and state ownership, invariants, abstraction, change locality, and verification through interfaces.

Trace material concerns through concrete usage or a likely change. Compare the current or proposed structure with a plausible simpler alternative, including the cost of that alternative. Assess consequences rather than accumulating smells; a wrapper, long function, shared writer, or repeated expression can be justified by the actual contract. A design assessment identifies expected consequences; observed implementation behavior needs separate proof.

## Return a bounded assessment

For each material finding, return **location → causal reader or change burden → recommendation → tradeoff → verification needed**, with supporting evidence and its limits. Distinguish a demonstrated issue, an unresolved risk, and a preference. An empty assessment is valid.

Return in the caller's working record or conversation; follow the execution contract's retention rules rather than creating a report by default. The caller decides which findings change its design, review verdict, or implementation plan and owns final verification.
