---
name: solution
description: Explore what solution should exist and why. Use while the problem, ownership, trust model, or overall approach is open; use architect once the direction is chosen.
---

# Solution

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You own the decision and the one decision record that explains it; leave library and code-shape choices to [Architect](../architect/SKILL.md). Fold returned findings into that record; don't paste reports end to end.

You're done when the recommendation answers the actual decision, each viable option has its strongest failure case and the evidence against it, and every open assumption has a next step.

## Check the brief

- Turn a proposed technology or an either/or into the decision actually being made.
- Treat feature scope, production readiness, evaluation purpose and rollout scale as separate decisions. "MVP" alone settles none of them.
- Reopen a settled brief, ADR or decision only if new evidence changes it, and say why.

## Ground and research

- Read the project before you recommend anything: its README, the code the decision touches and how it runs today. Base the recommendation on what you find, not on a typical setup. Then establish the desired properties, non-goals, actors, ownership, trust boundaries and operational burden that bear on the choice. Invoke the [`how`](../how/SKILL.md) skill to trace behaviour and the [`why`](../why/SKILL.md) skill for existing rationale.
- Read the product contract and keep its agreed behaviour and invariants. If behaviour is missing from it, invoke the [`product`](../product/SKILL.md) skill. If feasibility changes the product choices, return the requirement, evidence and tradeoff to the caller; never quietly redefine the outcome.
- If the user asks for an interview, or several consequential choices need their judgment, invoke the [`grill-me`](../grill-me/SKILL.md) skill.
- Read the relevant glossary entries and current ADRs. If a meaning is unclear or a decision needs a record, invoke the [`domain-modeling`](../domain-modeling/SKILL.md) skill and link its records from the decision record.
- Check external claims in primary sources, and cite the passage, version and date. Mark a vendor's claim as documented, not observed, until you've seen it in this deployment.
- Look for evidence against the approach you prefer. If an observation could change the decision, invoke the [`probe`](../probe/SKILL.md) skill. A cited answer to an advisory question doesn't need a prototype.
- If you're choosing or reconsidering the stack or hosting, read [technology-direction.md](references/technology-direction.md).

## Compare and challenge

- If an approach depends on navigation, workflow or what users can see, invoke the [`interaction-design`](../interaction-design/SKILL.md) skill for a bounded comparison.
- Before adding components, check whether keeping or reusing what exists, a config change, deleting a step or a direct implementation meets the outcome. Include the viable ones.
- If an open choice could materially change the outcome or commitment, develop a structurally different approach and compare them.
- Judge options on criteria from this problem, such as ownership, authority, failure modes, cost and reversibility.
- If independent candidates could change a consequential choice, invoke the [`arena`](../arena/SKILL.md) skill, with the brief, the evidence and the decision record below as its output contract. Check that its recommendation answers the actual decision.
- For each viable option, name what must be true, its strongest failure case, the evidence against it and who bears the cost. If scale or a breached account or component matters to the brief, test each option against it.
- For an assumption that changes the ranking or locks in a costly commitment, name the evidence needed, the cost of reversing, and the observable condition for reconsidering or exiting. If it changes the ranking, make the recommendation conditional on that evidence. Tell a real rollback apart from a hoped-for migration.
- If you propose a first version and a later target, name what triggers the move.
- Before settling a consequential approach, invoke the [`10x`](../10x/SKILL.md) skill, then the [`interrogate`](../interrogate/SKILL.md) skill, including on the framing.

## Decide and hand off

Write the record into the caller's artifact if they named one. It holds:

- the outcome, the chosen approach and why
- constraints, non-goals and accepted tradeoffs
- decisive sources and their limits, with each claim marked as documented, observed, inferred or a value judgment
- rejected alternatives
- open assumptions, each with who settles it, what must be established and when it blocks
- conditions for reconsidering, and observable success criteria where known

In the reply, lead with the recommendation and what it depends on, and keep it short. The record's contents aren't headings every reply needs.

- If [Pilot](../pilot/SKILL.md) called you, return the record and its sources to it.
- If the user asked for design only, invoke the [`architect`](../architect/SKILL.md) skill with the record.
- If the user asked you to build, pass the record to Pilot for the change playbook.
