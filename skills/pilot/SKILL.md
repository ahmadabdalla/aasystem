---
name: pilot
description: Carry a requested outcome from product ideation through design, engineering delivery, and verification using the relevant procedures.
disable-model-invocation: true
---

# Pilot

If you're resuming earlier work, such as from a task brief or after compaction, read [task continuity](references/task-continuity.md) before anything else. Before starting, read the [execution contract](references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You own the request until it's verified and delivered. Pick the procedures and workers yourself; the user names only the outcome.

If the work is long or has stages, or goes to other agents, read [task continuity](references/task-continuity.md) before starting.

## Start

1. Reuse the existing brief and sizing if they still fit; otherwise restate the scope.
2. If a rule comes from a borrowed workflow, don't treat it as the user's preference.
3. Pick the [procedures](#procedures) that fit, read each in full and use the steps that apply. If another owner handed you this work, keep their scope; you're not the coordinator.
4. For an OpenSpec project, follow the [OpenSpec reference](references/openspec.md).
5. Keep one task list for substantial work. Reuse the existing list and brief, and link playbooks rather than copying them in.
6. Size specialist work and proof to the assessed effort, and reuse settled Product, interaction and architecture inputs, including from specialists the user ran directly. A prescribed presentation edit that [qualifies](references/verification-contract.md#owner-presentation-eligibility) needs only its relevant checks.

Start is done when the brief states the scope, size and the procedures you'll run.

## Procedures

Product and design:

- Discover product structure, people and journeys, or define behaviour, business rules and acceptance scenarios: [Product](../product/SKILL.md)
- Turn product outcomes into navigation, interactions, what's visible and justified UI choices: [Interaction Design](../interaction-design/SKILL.md)
- Independently assess a rendered interface for visual and interaction friction: Interaction Design's [rendered UX assessment](../interaction-design/SKILL.md#select-the-assignment)
- Audit design tokens, components or UI code for visual consistency (radii, spacing, alignment, type, colour, motion): [Design Judge](../design-judge/SKILL.md)
- Refine an inspectable UI or UX with human feedback and keep a reviewed visual reference: [UI Refinement](../ui-refinement/SKILL.md). For production delivery, pick Feature and use UI Refinement within it. To settle a decision with a throwaway prototype, use Prototype instead.

Understand and decide:

- Work through a plan with the user: [Grill Me](../grill-me/SKILL.md)
- Clarify project terms, or record a product, design or software decision that matters: [Domain Modeling](../domain-modeling/SKILL.md)
- Explain a behaviour, change or finding, or investigate a question, without changing the product, in prose or a diagram: [Investigation](playbooks/investigation.md)
- Assess module design or code maintainability, including tests that guard no behaviour: [Maintainability](../maintainability/SKILL.md#select-the-assessment)
- Decide what solution should exist while direction, ownership or constraints are open: [Solution](../solution/SKILL.md)
- Design implementation boundaries, interfaces and state ownership without building: [Architect](../architect/SKILL.md)
- Test how a decision or design holds up under plausible growth: [10x](../10x/SKILL.md)
- Challenge a proposal, design or change adversarially, including PR merge risk and detection gaps: [Interrogate](../interrogate/SKILL.md)
- Settle a decision with a throwaway experiment: [Prototype](playbooks/prototype.md)

Change code:

- Fix a reported defect: [Bug fix](playbooks/bug-fix.md)
- Add or deliberately change behaviour: [Feature](playbooks/feature.md)
- Change structure without changing behaviour, including pruning tests that guard no behaviour: [Refactoring](playbooks/refactoring.md)

Skills, verification and delivery:

- Create or change a skill: [Skill authoring](playbooks/authoring-a-skill.md)
- Test whether an instruction or skill change improves behaviour: [Evaluation](playbooks/eval.md)
- Open a pull request when asked: [Opening a PR](playbooks/opening-a-pr.md)
- Set up verification for a project that has none: [Bootstrap Verification](../bootstrap-verification/SKILL.md)
- Audit project verification, including recipes that no longer work: [Maintain Verification](../maintain-verification/SKILL.md)
- Capture a lesson or a stated judgment: [Reflect](../reflect/SKILL.md)
- Change several coupled phases at once: [Figure It Out](../figure-it-out/SKILL.md)

If no procedure fits, tell the user there's no dedicated procedure for it. If you can build a bounded procedure you can prove within the request, use [Figure It Out](../figure-it-out/SKILL.md). If you can't, stop and say what's missing.

## Coordinate

Code you keep follows the [verification contract](references/verification-contract.md). If the change doesn't [qualify](references/verification-contract.md#owner-presentation-eligibility) as owner-presentation, an agent that edited none of it must verify it, however small; your own checks don't count. If that check didn't run, the work is incomplete: say so in your report, and why.

Hand off as [Delegation](references/delegation.md) describes. The `disable-model-invocation` flag is never a reason to skip a handoff, except for skills reserved for the user, which you offer instead of running. If you can't start a required worker, say so. The playbook decides who does what: Architect gives the design, [Implement](../implement/SKILL.md) gives the edits and development checks, and when required, a separate worker briefed with [Engineering Verification](references/engineering-verification.md) gives the [acceptance proof](references/verification-contract.md#independent-implementation-verification).

When the evidence changes the task, change the route.

## Finish

Run the execution contract's [finish check](references/execution.md#finish). Also report the choices that mattered and what's left, and keep completed, failed and unverified claims apart.
