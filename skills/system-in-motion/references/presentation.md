# Present the journey

This owns composition and scene meaning. The model contract owns data fields;
[diagram readability](diagram-readability.md) owns connection design;
[verification](verification.md) owns inspection and delivery decisions.

## One story, one clock

Storyboard each meaningful change: trigger, actor-visible state, backstage action
and participating technology. Explain the outcome first, then how it happens.
Component captions pair business responsibility with technology; use the project's
vocabulary and expand unfamiliar terms once.

Choose scene boundaries before laying out the timeline. There is no preferred scene
count: each scene should teach a meaningful outcome, decision or change of focus.
Related request/response or write/acknowledgement steps usually belong in ordered
animation phases within one scene. Split when combining would obscure a meaningful
change of initiator, delay, failure or observation boundary, or leave too little
reading time. Ask what each new scene teaches beyond the previous one; merge those
that merely expose another transport step while preserving causal order. Let the
timeline adapt to the story; never pad or split scenes to reach a target count or
fill a grid row. See [phase timing](diagram-readability.md#make-motion-explain-dependencies).

In an `observed` scene, retain each actor's last received state until an evidenced
response, deliberate read or push supplies new information. A background write
alone cannot update that actor's screen, including in planned flows. Use a visibly
labeled `explanation` scene for narrator-visible processing or stored facts instead.

Both views must retain the scene, elapsed time and pause state when switched.
Back/Next and scene selection update captions, highlights and visible state together.
Check seeking only when a custom template provides it; the starter progress bar is
display-only. Hold results long enough to read. Illustrative actions cannot perform
real requests or suggest that the explanation is a live control panel.

## Reference composition

Build and open the reference using SKILL.md. Preserve these anchors while changing
project content, styling and evidenced topology:

- Compact masthead, one upper-right view switch, and current
  scene heading, narrative and counter above the visual.
- Wide application window with header/persona, local navigation and stage body;
  a narrow open backstage rail beside it, rather than a second equal-sized card.
- Scene-specific surfaces and meaningful object motion: an arriving message/request,
  processing handoff, workbench/list/detail, review/decision, outbound package or
  register/audit as the journey warrants. A repeated key-value card or progress bar
  alone does not explain the journey.
- Playback controls below the visual, then a numbered clickable scene strip.
- One icon-and-caption architecture canvas with meaningful boundaries, outside
  actors where applicable and separate initiators. Use a connected visual map,
  not large component cards with a separate prose ledger as its only explanation.
- Evidence and claim uncertainty remain available without dominating the scene.

Choose each scene form for its meaning: a pipeline conveys processing; a review
shows the relevant facts and decision; a register shows stored outcome and history.
An API/CLI uses its actual request/response or terminal surface in the same shell.
Do not invent product capabilities merely to exercise every scene type.

Group architecture components by meaningful responsibility, initiator or evidenced
boundary, not a provider's reference topology. A lane caption explains what starts
work or what the group shares; placement alone does not imply calls between nodes.
Preserve causal reading order across the supported laptop layouts.

### Business map

The business profile replaces Architecture with horizontal responsibility lanes,
not a third view. Lane headers show an outline performer icon, role and short
caption. Rounded activities, diamond decisions and pill outcomes remain connected
throughout playback, including branches, exits and rework. Lane membership identifies
the performer. Derive scene badges and selection from node scene IDs; unlinked
outcomes have no badge. Show the model's labeled state dimensions directly below
the scene description. Use orthogonal directed routes with labeled alternatives
and distinct incoming ports. Keep planned nodes and paths dashed and explicitly
labeled during focus; explain inferred/unknown work. The nearby legend distinguishes
focus, progression, planned work and prerequisites. A prerequisite is not a call.

Experience keeps the wide scene surface and narrow responsibility rail, choosing
the existing forms by scene meaning. Vertical scrolling is acceptable; the bundled
business reference fits both laptop widths without horizontal page scrolling.
For larger journeys, label an intentionally scrollable canvas and retain readable
labels rather than shrinking the map to fit. The fictional source defines reference
topology, not limits on lane, node or scene counts.

No domain, cloud or palette is intrinsic to this pattern. Use the requested or
evidenced design system; keep copy focused on actions and outcomes, with source
excerpts in evidence locators. Diagram contrast may need different tokens from
product branding. Do not require remote fonts, icons or images for playback.

For custom templates, preserve safe plain-text insertion, offline operation and
shared playback state; never interpolate model strings as executable HTML.

## Default palette

Use explicit user styling first, then an evidenced project design system. When
neither supplies a palette, use this white-slide fallback in both views. Start in
light mode regardless of the computer's theme so screenshots sit naturally on a
white PowerPoint slide. The starter implements this default; alternate themes are
optional and must be checked separately if offered.

| Role | Color |
| --- | --- |
| Page, canvas and panels | `#FFFFFF` |
| Soft grouping surface | `#F1F5F9` |
| Main text | `#162544` |
| Secondary text | `#526176` |
| Active path, focus and accent text | `#1D4ED8` |
| Accent background | `#EFF6FF` |
| Inactive connectors and arrowheads | `#64748B`, opaque |
| Decorative borders | `#D9DCE1` |
| Success text / background | `#23684C` / `#E7F2EC` |

Use white text on solid blue highlights. Pale borders are for grouping, never the
only visible connection or control boundary. Keep inactive wires visible; express
current activity with blue, weight and motion, and provenance with labels/dashes.
Check text and arrowheads on their actual backgrounds, including paused screenshots.
A user accent override does not automatically provide suitable contrast for every
role: adapt the template's related tokens as needed. Do not add a slide-export tool
or change the story just to use this palette.

## Plain process language

Write for the brief's audience. Prefer a named actor and concrete verb: who does
what, what changes, and when the user learns it. Keep the business outcome in the
heading; put necessary technology names in the supporting caption. Expand unfamiliar
terms once. Keep exact state names when they matter, explaining them in plain words.

Remove AI-style filler, sales claims and stock framing: “seamlessly”, “powerful”,
“leverage”, “it's worth noting”, repeated summaries and “not X, but Y” constructions
that add no meaning. Replace abstract noun chains with actions. For example,
“Orchestrate seamless fulfilment via asynchronous persistence” becomes “The worker
saves the order in the background” only when the source supports that actor/action.
“Accepted” must not become “Delivered”; keep failure conditions, independent triggers,
observation delays and planned/unknown qualifiers. Simplification cannot invent
certainty or erase a distinction needed to understand the process.

## Compare the exported result

Compare representative arrival, processing, workbench/review, completion and
architecture states with the built reference at matching width, theme and stable
playback positions. Inspect geometry and meaningful motion as well as semantics.
Preserve these anchors while correcting mismatches; do not reproduce reference
routing weaknesses or redesign the composition during a parity correction.
Keep private before/after views outside the public package.
