---
name: pilot
description: Carry a requested outcome from product ideation through design, engineering delivery, and verification using the relevant procedures.
---

# Pilot

If you're resuming earlier work, such as from a task brief or after compaction, read [task continuity](references/task-continuity.md) before anything else. Before starting, read the [execution contract](references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You own the request until it's verified and delivered. Pick the procedures and workers yourself; the user names only the outcome.

If the work is long or has stages, or goes to other agents, read [task continuity](references/task-continuity.md) before starting.

## Start

1. Reuse the existing brief and sizing if they still fit; otherwise restate the scope.
2. If you can't say who it's for, what they'll be able to do and what done looks like, call the Skill tool with "product" ([product](../product/SKILL.md)) first. Don't design or edit until the user answers.
3. Ask the user questions through Grill Me: call the Skill tool with "grill-me" ([grill-me](../grill-me/SKILL.md)).
4. If a rule comes from a borrowed workflow, don't treat it as the user's preference.
5. Pick the [procedures](#procedures) that fit, read each in full and use the steps that apply. If another owner handed you this work, keep their scope; you're not the coordinator.
6. For an OpenSpec project, follow the [OpenSpec reference](references/openspec.md).
7. Keep one task list for substantial work. Reuse the existing list and brief, and link playbooks rather than copying them in.
8. Size specialist work and proof to the assessed effort, and reuse settled Product, interaction and architecture inputs, including from specialists the user ran directly. A prescribed presentation edit that [qualifies](references/verification-contract.md#owner-presentation-eligibility) needs only its relevant checks.

Before your first edit, post the brief: scope, size, and each procedure with the skill it calls. Name any step you skip and say why.

## Procedures

Product and design:

- Discover product structure, people and journeys, or define behaviour, business rules and acceptance scenarios: call the Skill tool with "product" ([product](../product/SKILL.md))
- Turn product outcomes into navigation, interactions, what's visible and justified UI choices: call the Skill tool with "interaction-design" ([interaction-design](../interaction-design/SKILL.md))
- Independently assess a rendered interface for visual and interaction friction: invoke the [`interaction-design`](../interaction-design/SKILL.md#select-the-assignment) skill for its rendered UX assessment
- Audit design tokens, components or UI code for visual consistency (radii, spacing, alignment, type, colour, motion): call the Skill tool with "design-judge" ([design-judge](../design-judge/SKILL.md))
- Refine an inspectable UI or UX with human feedback and keep a reviewed visual reference: call the Skill tool with "ui-refinement" ([ui-refinement](../ui-refinement/SKILL.md)). For production delivery, pick Feature and use UI Refinement within it. To settle a decision with a throwaway prototype, use Prototype instead.

Understand and decide:

- Work through a plan with the user: call the Skill tool with "grill-me" ([grill-me](../grill-me/SKILL.md))
- Clarify project terms, or record a product, design or software decision that matters: call the Skill tool with "domain-modeling" ([domain-modeling](../domain-modeling/SKILL.md))
- Explain a behaviour, change or finding, or investigate a question, without changing the product, in prose or a diagram: [Investigation](playbooks/investigation.md)
- Assess module design or code maintainability, including tests that guard no behaviour: invoke the [`maintainability`](../maintainability/SKILL.md#select-the-assessment) skill
- Decide what solution should exist while direction, ownership or constraints are open: call the Skill tool with "solution" ([solution](../solution/SKILL.md))
- Design implementation boundaries, interfaces and state ownership without building: call the Skill tool with "architect" ([architect](../architect/SKILL.md))
- Test how a decision or design holds up under plausible growth: call the Skill tool with "10x" ([10x](../10x/SKILL.md))
- Challenge a proposal, design or change adversarially, including PR merge risk and detection gaps: call the Skill tool with "interrogate" ([interrogate](../interrogate/SKILL.md))
- Settle a decision with a throwaway experiment: [Prototype](playbooks/prototype.md)

Change code:

- Fix a reported defect: [Bug fix](playbooks/bug-fix.md)
- Add or deliberately change behaviour: [Feature](playbooks/feature.md)
- Change structure without changing behaviour, including pruning tests that guard no behaviour: [Refactoring](playbooks/refactoring.md)

Skills, verification and delivery:

- Create or change a skill: [Skill authoring](playbooks/authoring-a-skill.md)
- Test whether an instruction or skill change improves behaviour: [Evaluation](playbooks/eval.md)
- Open a pull request when asked: [Opening a PR](playbooks/opening-a-pr.md)
- Set up verification for a project that has none: call the Skill tool with "bootstrap-verification" ([bootstrap-verification](../bootstrap-verification/SKILL.md))
- Audit project verification, including recipes that no longer work: call the Skill tool with "maintain-verification" ([maintain-verification](../maintain-verification/SKILL.md))
- Capture a lesson or a stated judgment: call the Skill tool with "reflect" ([reflect](../reflect/SKILL.md))
- Change several coupled phases at once: call the Skill tool with "figure-it-out" ([figure-it-out](../figure-it-out/SKILL.md))

If no procedure fits, tell the user there's no dedicated procedure for it. If you can build a bounded procedure you can prove within the request, call the Skill tool with "figure-it-out" ([figure-it-out](../figure-it-out/SKILL.md)). If you can't, stop and say what's missing.

## Coordinate

Code you keep follows the [verification contract](references/verification-contract.md). If the change doesn't [qualify](references/verification-contract.md#owner-presentation-eligibility) as owner-presentation, an agent that edited none of it must verify it, however small; your own checks don't count. If that check didn't run, the work is incomplete: say so in your report, and why.

Hand off as [Delegation](references/delegation.md) describes. If you can't start a required worker, say so. The playbook decides who does what: Architect gives the design, [Implement](../implement/SKILL.md) gives the edits and development checks, and when required, a separate worker briefed with [Engineering Verification](references/engineering-verification.md) gives the [acceptance proof](references/verification-contract.md#independent-implementation-verification).

When the evidence changes the task, change the route.

## Finish

Run the execution contract's [finish check](references/execution.md#finish). Also report the choices that mattered and what's left, and keep completed, failed and unverified claims apart.
