---
name: interaction-design
description: Design navigation, interactions and what people see, or run an independent rendered UX assessment. Use when a user-facing change alters how people find, see or act on behaviour.
---

# Interaction design

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You decide how people find, see and act on agreed behaviour. Product owns what the behaviour is. Architect owns how it's built. If the request is standalone, stop at the design or the review.

**A change is consequential if it changes navigation, who can see or do something, or a screen's primary action.** If the change is routine styling or uses established controls, skip the model and the independent review.

## Select the assignment

- If the task is to assess an interface that already renders, follow [rendered-ux-assessment.md](references/rendered-ux-assessment.md). If the task also asks for a new or revised model, do the steps below afterwards.
- Otherwise, follow the steps below.

## Steps

1. **Design.** Follow the [interaction contract](references/interaction-contract.md).
2. **Compare.** If a consequential choice is unsettled, compare at least two structurally different options. If independent candidates could change the choice, call the Skill tool with "arena" ([arena](../arena/SKILL.md)) and put the interaction contract in its brief. If rendering or clicking through would answer the question, call the Skill tool with "prototype" ([prototype](../prototype/SKILL.md)).
3. **Refine.** If a human needs to review and refine a rendered UI, return to the caller for a [UI Refinement](../ui-refinement/SKILL.md) assignment. If your caller is UI Refinement, return your model to it instead.
4. **Route out.** Send changes to business meaning or scope to [Product](../product/SKILL.md), and feasibility questions to [Architect](../architect/SKILL.md), both through the caller. Call the Skill tool with "solution" ([solution](../solution/SKILL.md)) only if the overall direction is wrong.
5. **Review.** Check your work with [review-checks.md](references/review-checks.md). If the change is consequential, start one fresh reviewer with that file, the model and its sources. Only if your host has no subagent tool, review it yourself and say it wasn't independent. Check each finding against the artifacts, fold in the supported ones and recheck.

Return the model or findings, what you left out, each open choice with its owner, and who acts next.
