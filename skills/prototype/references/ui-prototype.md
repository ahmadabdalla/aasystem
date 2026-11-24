# UI prototype

Render the UI inside the real app so a human can judge it in context. If the question is about business rules, use [logic-prototype.md](logic-prototype.md).

- If the brief fixes the presentation, build **one candidate**.
- If a choice about navigation, layout, information hierarchy or primary action is open, build **variants**.

## 1. Set up the context

Mount the prototype in a copy of the real page or app shell, with real navigation, components and content density, inside your isolated checkout. If the surface is new, put it in the shell it will live in. If you can't, say what context is missing. A blank page hides navigation and density problems.

Give every variant the same fixtures: the same data, user, role and starting state. Cut live connections unless the brief permits a read-only source, and record which one you used; copying the app's look doesn't license calling its backend. Results from mocks aren't evidence of backend behaviour.

## 2a. One candidate

Follow the brief's visual instructions and the components it names. Render the states and viewports the review needs. Record what the [interaction contract's visual-reference rules](../../interaction-design/references/interaction-contract.md#preserve-an-inspectable-visual-reference-when-needed) ask for. After each round of changes, keep the source revision and screenshots; a local URL that keeps changing doesn't identify what was reviewed.

## 2b. Variants

Build as many as the question needs; two can be enough. Variants differ in structure: grouping, placement, primary action, navigation or disclosure. If they differ only in colour or copy, they don't answer the question. Keep the project's components and constraints.

If independent candidates could change the choice, invoke the [`arena`](../../arena/SKILL.md) skill to generate and combine them, with the same question and fixtures. Give each worker its own variant files, and keep the shared wiring with one owner.

Switch variants with a stable `?variant=` key, or the framework's equivalent, so each one has a reloadable address. Label each by its structure, for example `B (sidebar nav)`. Keep the switcher visibly separate from the design, and don't let it cover what's being compared. If arrow keys switch variants, don't intercept them while an input has focus. Switching restores the same fixture state, so no variant looks more complete than another.

Wire the interactions the question needs. Label anything you didn't wire; a button that does nothing must not pass for a working flow.

## 3. Exercise it

Check the switcher and reset first. Then drive the same journey through every variant, including empty and failure states and the relevant viewports. Keep screenshots with notes on what you did, and note what you didn't cover.

If a human picks a base and borrows from others ("the header from B with the sidebar from C"), build the combination and check it again; the original variants' results don't carry over.

Then follow [Observe and return](../SKILL.md#observe-and-return).
