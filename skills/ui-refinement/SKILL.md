---
name: ui-refinement
description: Render a user-facing flow, refine it with human feedback, and keep the reviewed version as its visual reference. Use when the user wants to see the UI before it's built, or how it looks is still open.
---

# UI Refinement

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You produce a reviewed visual reference. Your caller keeps the task and builds the product, so don't edit production code.

1. **Reuse what's reviewed.** If a reference names the human who reviewed it, its revision and its screenshots, and it covers the request, return it and stop.
2. **Frame the slice.** List the screens and states the human needs to see. If the mechanics are unclear, call the Skill tool with "how" ([how](../how/SKILL.md)). If a past choice matters and no record explains it, call the Skill tool with "why" ([why](../why/SKILL.md)). If a business rule is missing or the request changes one, return it to [Product](../product/SKILL.md) through the caller and render only what's settled.
3. **Design it.** Call the Skill tool with "interaction-design" ([interaction-design](../interaction-design/SKILL.md)) for the interactions that change.
4. **Render it.** Call the Skill tool with "prototype" ([prototype](../prototype/SKILL.md)). Put the path to Design Judge's [visual standards](../design-judge/references/visual-standards.md) in the brief. Do steps 3 and 4 yourself unless the [delegation rule](../pilot/references/delegation.md) says to split them.
5. **Look at it.** Open the candidate with realistic content (a long title, an empty list, a full list) at the viewports the project supports, and save screenshots. Reading the markup isn't looking. If you can't render, say so and stop.
6. **Assess it, if asked.** If the brief asks for an independent assessment, run the [rendered UX assessment](../interaction-design/references/rendered-ux-assessment.md) before the human sees it.
7. **Ask the human.** Show the screenshots and ask one question, as [Ask the human](../pilot/references/execution.md#ask-the-human) says. If no human is reachable, end your reply with that question.
8. **Apply the feedback.** Apply presentation changes and repeat steps 5 to 7 until the human accepts. Send business-rule changes to Product through the caller. Don't apply them, and don't write them into Product's files; note them in your checkpoint. Record decisions with the [decision-record convention](../domain-modeling/references/adr.md).
9. **Record a checkpoint.** In the project's existing task or design record, write the revision, the screenshots, who accepted what, open feedback with its owner and the next action, as the [interaction contract](../interaction-design/references/interaction-contract.md#5-record-and-hand-off) says.

Return the revision and screenshots, the records you wrote, open items with their owners, and what the prototype can't show. End on the one question from step 7.
