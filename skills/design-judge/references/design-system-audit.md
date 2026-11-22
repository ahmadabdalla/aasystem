# Design-system audit

Use this procedure to audit a project's tokens and UI components against the [visual standards](visual-standards.md). The result is an actionable report.

## 1. Scope the audit

Confirm which dimensions to assess: corner radii, spacing, alignment, typography and iconography, colour, consistency, motion or all of them. Confirm the surfaces too: the whole design system, named components or one area. Use the request; otherwise audit every dimension across the design system and state that assumption under Coverage.

## 2. Ground the system

Identify the styling stack, such as CSS custom properties, Tailwind or theme configuration, CSS-in-JS themes, a component library or platform styles. List the existing radius, spacing, border, colour, motion, typography, icon-size and dimension tokens, their values in every supported theme, and where they are defined. Inventory shared components and their implementations. Read existing design decisions and style guidance; they override the defaults under [precedence](visual-standards.md#precedence).

## 3. Inspect components by impact

Work in this order:

1. Token definitions and theme files
2. Shared primitives: buttons, inputs and other controls
3. Shared containers: cards, popovers, dropdowns, menus, dialogs, modals, navigation panels and tooltips
4. Page-local or one-off styling

Resolve each component's effective values through tokens, variants and overrides, including theme-specific ones. Compare only the dimensions in scope:

- **Corner radii:** record radius, inset and border values; compare nested pairs with [nested corner radii](visual-standards.md#nested-corner-radii).
- **Spacing:** [spacing and distancing](visual-standards.md#spacing-and-distancing).
- **Alignment:** [alignment](visual-standards.md#alignment).
- **Typography and iconography:** [typography and iconography](visual-standards.md#typography-and-iconography).
- **Colour:** [colour](visual-standards.md#colour).
- **Consistency:** [visual consistency](visual-standards.md#visual-consistency), including duplicate implementations of one component.
- **States and motion:** [states and motion](visual-standards.md#states-and-motion).

Search for hard-coded values that bypass tokens, and for near-duplicate values doing one job, such as 6px, 7px and 8px radii.

When a runnable preview is available, check High-priority findings in the rendered interface across the affected states and themes. Source values can prove a geometric mismatch; back claims about visual balance or rendered alignment with rendered evidence, or mark them source-only.

When alignment is in scope:

- **Capture:** run [capture.mjs](../scripts/capture.mjs) (usage in its header), passing `--schemes` for every supported theme and a prep script for each menu, popover and dialog in scope. Where a theme does not follow `prefers-color-scheme`, switch it in the prep script and confirm it in the capture. Install Playwright outside the project, in `PLAYWRIGHT_DIR`; keep captures outside the repository under the project's evidence rules.
- **Read:** have a fresh agent that did not run the capture confirm each miss in its capture, under [delegation](../../pilot/references/execution.md#delegation); then cite the page, state, measured pixels and capture path as its location. A miss marked `xN` repeats down one table or list; report it once. An unmeasured container's edge lines were not checked; still report any misses listed under it.
- **Limits:** only edge lines (text, box, label, icon column, trailing) and centring in bars are measured, per container, so compare sibling panels and middle columns by eye. Text is measured by line boxes and icons by element boxes, so allow for side bearings and viewBox padding before reporting a miss. The scripts do not enter shadow DOM or iframes; an inner scroller shorter than half the viewport is measured only where visible.

When the audit covers a runnable app's full interface, include Interaction Design's [independent rendered UX assessment](../../interaction-design/references/rendered-ux-assessment.md): run it as its caller when you own the request; otherwise list it under Next action for your caller.

## 4. Report

Keep the report concise. Start with a one-paragraph summary of the overall state and the highest-impact problems. Then list findings ordered by priority:

| Priority | Component | Location | Issue | Current | Recommended |
| --- | --- | --- | --- | --- | --- |
| High | Menu item in dropdown | `path/to/file.css:42` | Item corners not concentric with the 12px menu | `12px` | `7px`, from 12 − 4 padding − 1 border, or a derived token |

- **Priority:** High, Medium or Low by reach (number of consumers or usage sites) and visibility. Where reach cannot be measured, use the inspection order above.
- **Location:** a file path and line, or the token name.
- **Issue:** the visual problem in one short sentence, plus its root cause where identifiable, for example a missing token, duplicate implementation or page override. Mark source-only findings, and changes to an established project value with the decision behind it.
- **Recommended:** a specific value or token and its derivation where one applies.

After the findings, add:

- **Informational departures:** established project values that differ from the defaults, without a recommendation.
- **Token proposals:** new, renamed, derived or removed tokens, each with the components it would affect.
- **Theme notes:** differences between light and dark themes, or confirmation that none were found.
- **Acceptance criteria:** measurable checks for the recommended standards, for example "no hard-coded radii outside token files", that later reviews or automation can apply.
- **Coverage:** the token and component inventory inspected, what was not inspected, and any rendered checks performed.
- **Next action:** the remediation to authorize, smallest high-impact change first, with its [signal effects](../../pilot/references/execution.md#signal-effects).

Return the report in chat unless the user names a destination.
