---
name: solution
description: Explore what solution should exist and why. Use while the problem, ownership, trust model, or overall approach is open; use architect once the direction is chosen.
disable-model-invocation: true
---

# Solution

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Reach a defensible decision through research, alternatives, and analysis.

Own the solution decision and its explanation. Use returned findings in the decision record; do not restart the brief or concatenate reports. Surface changed assumptions, consequential findings, and decisions that need the user's input as work proceeds.

## Check the brief

Treat feature scope, production readiness, evaluation purpose and rollout scale as separate decisions; infer none from the label MVP alone.

Before substantial work, briefly state the intended outcome, consequential gaps, and assumptions you will use. Reframe a proposed technology or either/or choice into the actual decision. Investigate observable unknowns; ask one focused question when a missing preference or constraint could materially change the outcome and cannot reasonably be assumed. If you ask, stop and wait for the answer. Otherwise proceed with the stated assumptions. Do not repeat this check after the brief is settled unless new evidence changes it.

## Ground and research

Consume the product contract when present. Preserve agreed behavior and invariants while comparing approaches. Use [product](../product/SKILL.md) for material gaps in the behavior contract within the assigned scope. When feasibility changes the available product choices, return the requirement, evidence, and tradeoff to the caller or user for resolution; do not silently redefine the outcome. An adequate brief needs no separate product exercise.

Use [grill-me](../grill-me/SKILL.md) when the user requests an interview or several consequential choices need their judgment. Reuse its returned brief and continue the solution decision; a single missing detail uses the focused question above.

Read relevant project glossary entries and current ADRs, following project instructions and context maps. Preserve their scope and status. Use [domain-modeling](../domain-modeling/SKILL.md) when meanings need clarification or a qualifying decision needs recording within the authorized document scope. Link saved records from the decision record; preserve the reason when new evidence warrants revisiting one.

Read the [approved-principle index](../principles/INDEX.md) while grounding the decision. Use its matching, application, and handoff instructions for relevant judgments.

Establish the current system, desired properties, non-goals, actors, ownership, trust boundaries, and operational burden where relevant. Use [how](../how/SKILL.md) for behavior and [why](../why/SKILL.md) for existing rationale. Use existing project discovery and feature-map evidence when available, preserving its inspection boundaries and observed-versus-intended distinctions. Research current external claims in primary sources; cite the relevant passage or artifact, version, and date where these affect the decision.

Distinguish established facts, imposed constraints, testable assumptions, and value judgments. Check evidence that could contradict the preferred approach. A product claim or documentation promise does not establish behavior in this deployment. Use [probe](../probe/SKILL.md) when an observation could change the decision; a cited advisory answer does not require building a prototype.

When choosing or reconsidering the stack or hosting approach, read [technology-direction.md](references/technology-direction.md). Use its findings in the existing comparison and decision record.

## Compare and challenge

When an approach depends on navigation, workflow or information visibility, use [interaction-design](../interaction-design/SKILL.md) for a bounded comparison within this assignment. Consume its rationale and unresolved product choices; reuse settled interaction decisions rather than requiring another UX phase for every solution.

Develop the strongest plausible approach and at least one structurally different alternative, including the current approach when viable. Use [arena](../arena/SKILL.md) for a consequential comparison, supplying the brief, grounding evidence, and the decision record described below as the output contract. Arena owns candidate comparison and synthesis. Check that its returned recommendation answers the actual decision; reopen the comparison only for a material gap, contradictory evidence, or changed criteria. Define the criteria from this problem: ownership, authority, failure modes, cost, feasibility, reversibility, or other decisive forces.

For each viable option, identify what must be true, the strongest failure case, evidence against it, and who bears the cost. Apply scale or compromise scenarios when they matter. Use [interrogate](../interrogate/SKILL.md) for a contested or consequential decision, including a challenge to the framing. Model agreement does not establish a fact.

## Decide and hand off

Use the caller’s designated artifact for the solution rationale, preserving other contributors’ content and linking canonical decisions. Maintain one decision record containing the outcome, chosen approach and rationale, constraints, non-goals, decisive sources and their limits, accepted tradeoffs, rejected alternatives, unresolved assumptions, and conditions for reconsideration. Include observable success criteria where known. Preserve whether a claim is documented, observed, inferred, or a value judgment. Distinguish an initial version from a target state only with concrete transition triggers. If uncertainty changes the ranking, make the recommendation conditional and identify the discriminating evidence. Present the recommendation and what affects its acceptance; link to supporting detail when substantial. The record's contents need not become separate headings in every reply.

When called by [aapilot](../aapilot/SKILL.md), return the decision record and its source artifacts to that owner, which selects the appropriate change playbook if implementation is authorized. For a standalone request that includes implementation design, pass the same record to [architect](../architect/SKILL.md). A research-only request ends with the recommendation. Business value and preference may remain judgments. Research supports the recommendation; it does not prove a future implementation works.
