---
name: architect
description: Design caller usage, types, signatures, and module boundaries before implementation, then verify and reconsider the shape. Use for changes to interfaces, state ownership, or responsibilities between functions, or when a playbook requests design; use solution for overall direction.
disable-model-invocation: true
---

# Architect

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Ground the problem, sketch alternatives, implement the chosen shape, and redesign when evidence contradicts it. Verification shapes the design from the start and tests it throughout implementation.

Own the implementation design and its explanation. Integrate returned artifacts into the design package instead of repeating reports or restarting completed phases. Surface material changes and verification gaps as work proceeds.

Establish whether this assignment owns design only or design plus implementation. A supporting feasibility/design assignment stays design-only unless the caller explicitly assigns implementation; authorization of the larger task does not expand this assignment. A calling playbook that retains execution receives the design package and resumes its own implementation phase. A standalone implementation request continues through proof. Reuse a current grounded package when the design is already settled; reopen it only for a material change or evidence gap.

## Design trigger

Use Architect when a proposed change alters an interface between functions or reallocates state ownership or responsibilities between them. Editing multiple function bodies alone does not require this route. An explicit task or calling playbook may also request design.

## Ground and define proof

Read the agreed product contract and its requirement sources when present. Carry its invariants and scenarios into the technical design: identify how important rules are enforced and exercised. Return a proposed behavior change or unresolved product rule to the caller, or use [product](../product/SKILL.md) within a standalone assignment’s scope. Preserve the requirement until its authority is resolved.

Read relevant project glossary entries and current ADRs, including for standalone work. Carry their constraints and evidence limits into the design. Use [domain-modeling](../domain-modeling/SKILL.md) for ambiguous concepts or qualifying implementation decisions within the authorized document scope; link its records from the design package. Explain changed evidence before reopening an accepted decision. Translate agreed meanings and decisions into observable expectations below.

Read the [approved-principle index](../principles/INDEX.md) while grounding the design, including standalone requests. Use its matching, application, and handoff instructions for relevant judgments.

Read the [solution](../solution/SKILL.md) decision record and its supporting evidence when present; a standalone request can supply the same brief. Carry forward its constraints, evidence limits, unresolved assumptions, and conditions for reconsideration. Reuse the settled brief and state only implementation-specific gaps or assumptions that change the work. For a new brief, state the intended deliverable, consequential gaps, and assumptions before substantial execution. Inspect facts you can observe. Ask one focused question only when a missing preference or constraint could materially change the work and cannot reasonably be assumed; if you ask, stop and wait. Otherwise proceed.

Trace affected behavior with [how](../how/SKILL.md); use [why](../why/SKILL.md) when changing ownership or layering. For greenfield work, ground in real callers, dependencies, and integration constraints. Preserve the strategic decision; reopen it when contradictory evidence or changed requirements warrant it, and explain why.

Read the project verifier and feature map when present. Identify affected outcomes, alternate entry points, and dependent callers; preserve documented coverage gaps. When implementation is authorized and the affected scope has no usable verification procedure, use [bootstrap-verification](../bootstrap-verification/SKILL.md) to discover and establish it within the task scope. Design-only work records missing capability in its verification plan.

Before coding, map each important requirement to a concrete input or action, expected observable result, the real surface used to exercise it, and evidence to retain. Include failure, retry, concurrency, or migration cases when they carry the design risk. Derive expected results from the contract, independently of the implementation. Check that the project can actually support this proof; name missing access or infrastructure as a verification gap.

## Sketch and compare

For user-facing scope, consume the project's interaction model when present, using the [interaction contract](../interaction-design/references/interaction-contract.md) to check the handoff, including decision authority and mock omissions. If a consequential interaction is unsettled, return it to the caller or use [interaction-design](../interaction-design/SKILL.md) within a standalone assignment. Reconcile proposed technical changes with the interaction owner; changing business behavior still returns to Product.

Write realistic caller usage before types. Sketch data shapes, signatures, ownership, invariants, and the main flow. Use [arena](../arena/SKILL.md) to compare at least two structurally different sketches before selecting a new design. Supply the same brief, grounding artifacts, proof criteria, and [design-package.md](references/design-package.md) as the candidate and synthesis contract. These candidates explore implementation shapes within the chosen solution; reopen the solution only when evidence warrants it. Preserve arena's disclosure when independent candidates or judging are unavailable.

Read Maintainability's [boundary criteria](../maintainability/references/boundaries.md) when evaluating these sketches and supply that reference to Arena candidates; add its [local-code criteria](../maintainability/references/local-code.md) only when local structure matters to the choice. Arena returns one synthesized design package with its selection rationale; check its fit against the contract and adopt it unless a material gap requires revision. Use a bounded [maintainability](../maintainability/SKILL.md) assessment when unresolved reader burden, ownership, or change cost could change the choice; reuse a settled assessment when its artifact and evidence remain current. If the host cannot invoke a supporting skill under its explicit invocation policy, report that handoff limitation rather than treating a link as permission to bypass it. Use [interrogate](../interrogate/SKILL.md) on a contested design before delivery. Incorporate supported findings and retain unresolved risks in the package.

Write the design package into the caller’s designated artifact when supplied, preserving solution rationale and links to canonical decisions. For design-only work, deliver usage, sketch, rationale, alternatives, and the verification plan; clearly state that implementation is unverified. If implementation is authorized, continue unless the user requested a checkpoint.

## Implement, verify, reconsider

Implement against the synthesized design package, building in units that can be checked against its contract. A reviewed sketch still has unverified implementation behavior. Use the project's verification procedure or the smallest credible way to drive the real public surface: UI, CLI, API, or library entry point. Observe results and relevant side effects. A passing build or a mocked dependency cannot establish an unexercised integration claim. If a real boundary cannot be exercised, report the remaining gap.

Keep the command or interaction, expected result, actual observation, environment, and tested revision or source identity with the evidence. Update affected feature recipes when intended behavior changes, retaining the authority for changed expectations. Use [maintain-verification](../maintain-verification/SKILL.md) for procedure drift; distinguish harness faults from product regressions. Verify the final combined artifact after material changes. Report pass, fail, and unverified behavior separately.

Repeated workarounds, special cases, type escapes, or callers learning internals are evidence to investigate. Trace the mismatch, update the mental model, resketch, compare again, and rerun the affected proof. A single edge case need not invalidate the architecture. Do not silently weaken acceptance criteria to make a design pass.
