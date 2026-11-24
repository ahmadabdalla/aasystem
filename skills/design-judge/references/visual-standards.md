# Visual standards

Default rules for building and judging UI. Use the sections your task touches, in every supported theme.

## Precedence

1. The user's explicit instructions and accepted design decisions for the scope.
2. The project's established tokens, component rules, palette and visual identity.
3. These defaults, where the project has no established value.

A value is **established** if it's a token, a documented decision, or what most equivalent components use. A one-off hard-coded value isn't. Keep an established value even when it differs from a default.

## Tokens

Use existing tokens for every value. Propose a new token only when several components share an unnamed value or a nested radius needs one. Don't add a palette.

## Nested corner radii

A child inside a rounded parent is concentric with it, so it needs a smaller radius than the parent.

Measure the **inset** at the corner: from the parent's inner border edge to the child's outer edge, including the parent's padding and any child margin or offset. If the horizontal and vertical insets differ, use the smaller one and treat the uneven gap as a separate problem.

1. If the inset is 16px or more, the child keeps its own component radius.
2. Otherwise, `inner radius = outer radius − inset − parent border width`. A 12px outer radius, 4px inset and 1px border give 7px.
3. If the result is 0 or less, square the corner. If it's positive but below the smallest radius token, use whichever of that token and 0 is nearer.

Where the stack allows, derive the inner radius from tokens, e.g. `max(0px, calc(var(--radius-lg) - var(--space-1) - var(--border-width)))`, or propose a named inset token.

This includes parts inside a control, such as a button or chip in an input and the thumb in a segmented control.

## Spacing and distancing

- Use a 4px/8px scale.
- Pad containers 12–16px; less for dense controls.
- Leave 6–8px between an icon and its text.
- Keep related elements close. Separate sections by 16–24px.

## Alignment

A **line** is a vertical guide that items start or end on. Measure visible ink: glyph and icon bounds, and a control's box only when it's painted (fill, full border or shadow).

Each container has:

- one **text line**, where labels, headings, values and bare icons start
- at most one **box line**, where painted controls (buttons, inputs, selects, chips) start: the text line minus the control's horizontal padding, so its label continues the text line
- one **trailing line**, where trailing items end

A painted control starts on the text line, the box line or the **label line** (where text after a leading icon or avatar starts).

1. If the project records no line, take the line of the neighbour sharing the edge. If there's none, take the line most rows sit on. Move the outliers, not the majority.
2. Put each row on a line or centre it, never between. Within 1px of its line passes; more is a miss.
3. In lists and sidebars, put icons in one **icon column**, centring icons of different widths. Start labels on one line after it, section headers on the icon column's leading edge, and nested items exactly one column in.
4. In bars and toolbars, centre every item on one horizontal line. Start the first item on the text or box line. End the last on the trailing line, or centre it on the trailing centre. Panels that share an edge share its line.
5. Correct optically. Align content, not affordances: put a chevron before a label that must end on a line. Count invisible borders and icon viewBox padding. Align tabs by their label, not their hit area. Let round shapes overhang a line by about 1px.
6. Fix a miss in the container's padding or a shared inset token, not with a margin on one item.
7. Keep grid columns and container widths the same across equivalent layouts.

## Typography and iconography

- Use few font sizes, weights and line heights, with a clear heading hierarchy.
- Keep icon sizes and stroke weights consistent. Treat icon-only actions the same everywhere.
- Align numbers, units and labels the same way throughout. Use tabular figures for compared values.

## Colour

- Save strong colour for primary actions and meaningful states, such as success, warning, error and selection.
- Keep text and controls at readable contrast.
- Use palette tokens, not hard-coded colours.

## Visual consistency

- Give equivalent components the same radius and dimensions: control heights, icon containers, avatars and badges. Keep touch targets at or above the platform minimum.
- Keep rounding small enough that a component doesn't become an unintended pill and a child doesn't look detached. Give small elements, such as tooltips and badges, a radius in proportion to their size. Circles and intentional pills keep their shape.
- Within one container, make buttons and fields all rounded rectangles or all pills, except one deliberate special control. Circles, such as avatars and icon buttons, don't count.
- Give each component one implementation, and add a radius, size or spacing variant only when it marks a different role.

## States and motion

- Show hover, selected and expanded states with a subtle background change, transitioned over about 300ms with ease-out or ease-in-out.
- Add other motion only to explain a change.
- Animate opacity and transforms, not properties that shift layout such as width or height.
- Under reduced motion, remove or minimise non-essential motion.
