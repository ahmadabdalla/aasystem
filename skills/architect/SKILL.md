---
name: architect
description: Design caller usage, types, module boundaries and a verification plan without building. Use solution first if the direction is still open.
---

# Architect

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You design and revise; you never build. The caller owns implementation and acceptance. Every package follows [design-package.md](references/design-package.md); read it before you start. If the user asked for design and build, invoke the [`pilot`](../pilot/SKILL.md) skill with the package for the change playbook.

You're done when the package has caller usage, shape, a rationale against the simplest viable option, and a verification plan that maps every changed requirement to an independent expected result and a real surface.

## Design trigger

Use Architect when a change alters an interface between functions, or moves state ownership or responsibilities between them. Editing several function bodies doesn't count on its own.

## Ground the design

- Read the agreed product contract. If the design needs a behaviour change or a product rule is unsettled, return it to the caller; in a standalone assignment, invoke the [`product`](../product/SKILL.md) skill. Design against the requirement as written until its owner settles it.
- Read the relevant glossary entries, current ADRs and any [Solution](../solution/SKILL.md) record. If a concept is ambiguous or a decision qualifies for a record, invoke the [`domain-modeling`](../domain-modeling/SKILL.md) skill and link its records from the package.
- Invoke the [`how`](../how/SKILL.md) skill to trace affected behaviour. If ownership or layering changes, also invoke the [`why`](../why/SKILL.md) skill. For greenfield work, read the docs and limits of the dependencies and integrations the design will call.
- If the project has a verifier or feature map, use it to find the affected outcomes, alternate entry points and dependent callers, and carry its documented coverage gaps into the verification plan.
- Reopen a settled package, accepted decision, ADR or solution only if new evidence or changed requirements justify it, and say why.
- If the proof needs seed or fixture state, read [Seed scenarios](references/seed-scenarios.md).
- If the design changes business identity, invariant enforcement, state ownership or coordination across business contexts, read [Business state and consistency](references/business-state.md).

## Plan the proof

Map each requirement the change adds or alters to an input or action, the expected result, the real surface that exercises it and the evidence to keep. Take expected results from the contract, not from how the code will work. Add failure, retry, concurrency or migration cases where they carry the risk, and the [signal effects](../pilot/references/execution.md#signal-effects) you'll check. If the project can't support a check, record the gap and return the prerequisite to the caller.

## Sketch and compare

- If the change is user-facing, check the interaction handoff with the [interaction contract](../interaction-design/references/interaction-contract.md). If a consequential interaction is unsettled, return it to the caller; in a standalone assignment, invoke the [`interaction-design`](../interaction-design/SKILL.md) skill. Agree any technical change to it with its owner.
- Write realistic caller usage before types. Then sketch data shapes, signatures, ownership, invariants and the main flow.
- If an open choice could materially change ownership, boundaries, data shape or proof, compare structurally different sketches, including the simplest viable one.
- Judge sketches with Maintainability's [boundary criteria](../maintainability/references/boundaries.md), and its [local-code criteria](../maintainability/references/local-code.md) only if local structure matters. Apply them yourself.
- If independent candidates could change the choice, invoke the [`arena`](../arena/SKILL.md) skill. Give every candidate the inputs [design-package.md](references/design-package.md) lists, plus the boundary criteria. Check Arena's package and rationale against the contract, and adopt it unless a material gap needs revision.
- If the boundary criteria don't separate your sketches, invoke the [`maintainability`](../maintainability/SKILL.md) skill for a bounded assessment of those sketches.
- Before settling a consequential design, invoke the [`10x`](../10x/SKILL.md) skill, and carry its findings into the rationale and the verification plan.
- If the user or a reviewer disputes the design, invoke the [`interrogate`](../interrogate/SKILL.md) skill before delivering it, and fold in supported findings.

## Return and reconsider

Write the package into the caller's artifact if they named one. Return the package and the revision it was designed against to the owner for [Implement](../implement/SKILL.md) and [independent verification](../pilot/references/verification-contract.md#independent-implementation-verification).

If implementation or verification reports repeated workarounds, special cases, type escapes or callers learning internals, trace the mismatch. If it's material, resketch or compare again, and update the package with the reason and the affected proof. One edge case doesn't have to invalidate the design. Never weaken acceptance criteria to fit the design.
