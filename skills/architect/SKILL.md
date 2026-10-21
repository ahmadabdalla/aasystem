---
name: architect
description: Design caller usage, types, signatures, module boundaries, and a verification plan; revise the design when evidence contradicts it. Use for changes to interfaces, state ownership, or responsibilities between functions, or when a playbook requests design; use solution for overall direction.
disable-model-invocation: true
---

# Architect

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own implementation design, rationale, and revision. Compare code shapes and deliver a design with a verification plan. Integrate supporting artifacts into the package; report material changes and verification gaps. The caller owns implementation and acceptance.

Every assignment is design-only. For a standalone design-and-build request, return the same package and authorized continuation to [aapilot](../aapilot/SKILL.md) for the change playbook, preserving one owner, settled grounding, requested checkpoints, and implementation scope. Reuse a settled package unless material changes or evidence gaps require revision.

## Design trigger

Use Architect when a proposed change alters an interface between functions or reallocates state ownership or responsibilities between them. Editing multiple function bodies alone does not require this route. An explicit task or calling playbook may also request design.

## Ground and define proof

Read the agreed product contract and its requirement sources when present. Carry its invariants and scenarios into the technical design: identify how important rules are enforced and exercised. Return a proposed behavior change or unresolved product rule to the caller, or use [product](../product/SKILL.md) within a standalone assignment’s scope. Preserve the requirement until its authority is resolved.

Read relevant project glossary entries and current ADRs, including for standalone work. Carry their constraints and evidence limits into the design. Use [domain-modeling](../domain-modeling/SKILL.md) for ambiguous concepts or qualifying implementation decisions within the authorized document scope; link its records from the design package. Explain changed evidence before reopening an accepted decision. Translate agreed meanings and decisions into observable expectations below.

Read the [solution](../solution/SKILL.md) decision record and its supporting evidence when present; a standalone request can supply the same brief. Carry forward its constraints, evidence limits, unresolved assumptions, and conditions for reconsideration. Reuse the settled brief and state implementation-specific gaps that change the work. For a new brief, state the intended deliverable and unresolved choices; inspect observable facts. Apply [decision authority](../aapilot/references/execution.md#decision-authority) to unresolved consequential choices and preserve proposed versus agreed status in the design package.

Trace affected behavior with [how](../how/SKILL.md); use [why](../why/SKILL.md) when changing ownership or layering. For greenfield work, ground in real callers, dependencies, and integration constraints. Preserve the strategic decision; reopen it when contradictory evidence or changed requirements warrant it, and explain why.

Read the project verifier and feature map when present. Identify affected outcomes, alternate entry points, and dependent callers; preserve documented coverage gaps. Record missing verification capability in the plan and return the prerequisite to the caller; designing a proof does not establish observed implementation behavior.

For seed/fixture design or representative state needed by the proof plan, read [Seed scenarios](references/seed-scenarios.md).

In the verification plan, map each important requirement to a concrete input or action, expected observable result, the real surface used to exercise it, and evidence to retain. Include failure, retry, concurrency, or migration cases when they carry the design risk. Derive expected results from the contract, independently of the implementation. Check that the project can actually support this proof; name missing access or infrastructure as a verification gap.

## Sketch and compare

For user-facing scope, consume the project's interaction model when present, using the [interaction contract](../interaction-design/references/interaction-contract.md) to check the handoff, including decision authority and mock omissions. If a consequential interaction is unsettled, return it to the caller or use [interaction-design](../interaction-design/SKILL.md) within a standalone assignment. Reconcile proposed technical changes with the interaction owner; changing business behavior still returns to Product.

Write realistic caller usage before types. Sketch data shapes, signatures, ownership, invariants, and the main flow. Compare structurally different sketches when an unresolved choice could materially change ownership, boundaries, data shape or proof. Use [arena](../arena/SKILL.md) when independent candidates could supply evidence that changes the choice under the shared delegation rule. For Arena, supply the same brief, grounding artifacts, proof criteria, and [design-package.md](references/design-package.md) as the candidate and synthesis contract. Alternatives explore implementation shapes within the chosen solution; reopen the solution only when evidence warrants it. Preserve arena's disclosure when independent candidates or judging are unavailable.

Read Maintainability's [boundary criteria](../maintainability/references/boundaries.md) when evaluating these sketches and supply that reference to Arena candidates; add its [local-code criteria](../maintainability/references/local-code.md) only when local structure matters to the choice. Apply the criteria in the comparison, including the simplest viable shape; justify each new boundary against present callers, enforced invariants, and concrete change cost. Reading criteria does not require a separate specialist. When Arena is used, check its synthesized design package and selection rationale against the contract and adopt it unless a material gap requires revision. Use a bounded [maintainability](../maintainability/SKILL.md) assessment when unresolved reader burden, ownership, or change cost could change the choice; reuse a settled assessment when its artifact and evidence remain current. Use [interrogate](../interrogate/SKILL.md) on a contested design before delivery. Incorporate supported findings and retain unresolved risks in the package.

Before settling a consequential implementation design, use [10x](../10x/SKILL.md); carry its findings into the rationale and verification plan.

Write the design package into the caller’s designated artifact when supplied, preserving solution rationale and links to canonical decisions. Deliver usage, sketch, rationale, alternatives, and the verification plan; clearly state that implementation is unverified.

## Return and reconsider

Return the package, source identity, settled constraints, risks, and implementation prerequisites to the owner for [Implement](../implement/SKILL.md) and [independent verification](../aapilot/references/execution.md#independent-implementation-verification).

Investigate repeated workarounds, special cases, type escapes, or callers learning internals reported by implementation or verification. Trace the mismatch; resketch or compare again when material. Update the package with the reason and affected proof; the caller assigns corrections and verification. A single edge case need not invalidate the design. Do not weaken acceptance criteria to fit the design.
