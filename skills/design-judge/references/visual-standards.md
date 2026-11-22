# Visual standards

These are default standards for a polished, minimal interface. Apply the sections relevant to the assignment.

## Precedence

1. Explicit user instructions and accepted design decisions for the scope.
2. The project's established tokens, component rules and visual identity, including its colour palette.
3. These defaults, where the project has no established value.

Do not rewrite an established project value to match a default. In an audit, report it as a finding when it breaks a standard below with a rendered or geometric effect, such as a non-concentric nested radius; list any other departure as informational. Apply each standard in every supported theme.

## Nested corner radii

Nested corners share one geometric centre. Do not give a child its parent's radius by default.

Measure the **inset** at the corner: the distance from the parent's inner border edge to the child's outer edge. It includes the parent's padding and any child margin or positioned offset. When the horizontal and vertical insets differ, use the smaller one and report the uneven corner gap as its own finding.

1. When the inset is 16px or more, the child uses its own component radius.
2. Otherwise, calculate `inner radius = outer radius − inset − parent border width`. For example, a 12px outer radius minus a 4px inset minus a 1px border gives a 7px inner radius.
3. When the result is zero or less, use a square inner corner. When it is positive but below the smallest radius token, use the nearer of that token and a square corner.

Where the stack supports it, derive inset radii from tokens, for example `max(0px, calc(var(--radius-lg) - var(--space-1) - var(--border-width)))`. A derived value keeps its parent relationship when either token changes. Alternatively, define a named inset token.

Typical nested pairs: cards, popovers, dropdowns, menus, dialogs, inputs with buttons or chips, segmented controls and navigation panels, with the items or surfaces inside them.

## Spacing and distancing

- Use a 4px/8px spacing scale; prefer existing spacing tokens.
- Give containers predictable padding of 12–16px, scaled down for dense controls.
- Keep icon-to-text gaps at 6–8px.
- Keep related elements close together and separate distinct sections with 16–24px.

## Alignment

Measure visible ink: glyph and icon bounds, and a control's box only when it has a fill, full border or shadow.

- Give each container one text line (labels, headings, values, bare icons), at most one box line (buttons, inputs, selects, chips) and one trailing line. Start a control's box on the text line, the label line (where text after a leading icon or avatar starts), or the box line (the text line minus the box's horizontal padding, so its label continues the text line).
- Where the project records no line, take the line of a neighbour sharing the edge, otherwise the line most rows already sit on. Move the outliers, not the majority.
- Position each row on an edge or centre it, never between. An item within 1px of its line passes; more than 1px off is a miss.
- In lists and sidebars, put icons on one column, centring icons of different widths. Start labels on one text line after it, section headers on the icon column's leading edge, and nested items exactly one column in.
- In bars and toolbars, centre every item on one horizontal line. Start the first item on the container's text or box line; end the last on its trailing line or centre it on the trailing centre. Panels that share an edge share its line.
- Correct optically: align content rather than affordances (put a chevron before a label that must end on a line), count invisible borders and icon viewBox padding, align tabs by their label rather than their hit area, and let round shapes overhang a line by about 1px.
- Fix a miss in the container's padding or a shared inset token, not with a margin on one item.
- Keep grid columns and container widths consistent across equivalent layouts.

## Typography and iconography

- Use a small set of font sizes, weights and line heights with a clear heading hierarchy.
- Keep icon sizes and stroke weights consistent, and treat icon-only actions the same way everywhere.
- Align numbers, units and labels consistently; use tabular figures for compared values.

## Colour

- Use subtle neutral surfaces, soft borders and restrained accents.
- Reserve strong colour for meaningful states, such as success, approval, warning, error and selection.
- Keep text and controls at readable contrast in every theme.
- Express colour through existing palette tokens. Do not introduce a new palette.

## Visual consistency

- Standardise border radii and component dimensions, such as control heights, icon containers, avatars and badges, across equivalent components. Keep touch targets at or above the platform's minimum.
- Avoid rounding so large that a component turns into an unintended pill or a child looks detached from its container. Small elements such as tooltips and badges use a small radius proportional to their size. Circles and intentional pills keep their shape.
- Replace hard-coded values with existing tokens. Propose a new token only when several components share an unnamed value or a nested relationship needs one.
- Within one container, make buttons and fields either all rounded rectangles or all pills, except one deliberate special control; circles such as avatars and icon buttons count toward neither.
- Keep one implementation per component, and remove radius, size and spacing variants that do not express a real difference in component role.

## States and motion

- Communicate hover, selected and expanded states with subtle background changes.
- Where a state change animates, use smooth transitions of about 300ms with an ease-out or ease-in-out curve for hover, expansion and state changes.
- Avoid abrupt changes and decorative animation that does not explain a change.
- Respect reduced-motion settings by removing or minimising non-essential motion.
- Prefer animating opacity and transforms over properties that cause layout shifts.
