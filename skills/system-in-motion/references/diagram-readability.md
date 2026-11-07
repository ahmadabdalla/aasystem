# Make the architecture traceable

Use before layout and on the exported diagram. This owns connection planning,
visual decoding and causal motion; [verification](verification.md) owns who checks
it and what evidence is required. The reference establishes composition, not a
readability guarantee for its own or a denser topology.

## Plan topology and routes together

Choose the smallest truthful graph. Add a separate return edge when its direction
or timing explains an actor's observation; do not duplicate every protocol reply.
Keep the real response/read/push evidenced in the scene even if one labeled
relationship represents a round trip. Never remove a meaningful webhook, initiator
or observation boundary to simplify the picture.

Identify crowded hubs, reverse pairs, long routes and simultaneous exchanges before
placing nodes. Arrange related components and reserve distinct ports/corridors
around the whole node, including its caption. Prefer short direct clear paths.
Before accepting a bend, check whether aligning the connected nodes or adjusting
their ports would produce a straight, unobstructed connector. Preserve distinct
docks and separation from other routes; recheck affected connections after changes.

Separate substantial parallel runs and arrowheads. For 7–10px heads, roughly
16–24px between tracks is a starting point, not certification. Brief fan-out at a
shared node can be reasonable; coincident unrelated runs must not imply a bus or
junction absent from source. Distinct incoming arrows need distinct docks.

Do not cure congestion with unrelated perimeter loops, shrunken labels, reversed
calls, invented components or dropped relationships. A current-path focus is
optional, but must retain access to a connected visual full overview that passes
the same trace checks. A text list or hidden wires cannot substitute for that map.

The starter routes each edge around node/text obstacles independently; it does not
reserve space against other routes. Its caption-bottom dock can also be shared.
When these cause congestion, adapt port/corridor allocation in the copied template
or revise the truthful relationship representation. Coordinates or color changes
alone may not address the mechanism.

## Account for rendered content and laptop space

Measure actual icons, captions, headings and relationship labels, including HTML
and SVG in the same coordinate space. Wrapping, padding, stacking and theme affect
bounds. Wires cannot disappear behind opaque text, and labels must clear unrelated
wires as well as other text. Moving a label cannot leave its route concealed.

Audit helper selectors against the custom renderer: zero matched captions or old
numeric-label selectors are coverage gaps. Node-only geometry, correct edge counts
and no routing errors do not establish readable connections.

Use the laptop dimensions in SKILL.md. Repeat full-map and busiest-phase checks
when available canvas space changes. Do not add phone/tablet reflow work. A labeled
pan/scroll canvas is acceptable if controls, boundaries and every relationship
remain discoverable by keyboard and pointer. Keep readable scale; scrolling does
not excuse avoidable detours. A helper assuming every node fits in the browser
needs appropriate reachability checks for an intentional scrollable map.

When a trace is ambiguous, measure all relevant pairs' long coincident/near-parallel
segments and crowded endpoints. Record the worst pair/gap and any justified short
fan-out exception for each layout. Measurements diagnose; they do not decide
whether a newcomer understands the picture.

## Keep meaning visible without motion

Choose diagram background/current/context colors for contrast, independently of
brand accents. Current work must be identifiable without a moving dot; context
must remain traceable without competing equally. Inspect small badges and heads.

Playback chronology and claim provenance are separate. Planned work can be current
in a hypothetical story. Preserve its standing through explicit evidence/status
without dashing everything into an indistinguishable network. Legend samples must
match actual combined states; never imply proof of deployment.

Use nearby purpose/direction cues for calls, events and returns. Keep the legend
and current-exchange explanation available with the map being read; prose below
a tall graph cannot be its only decoder. Opposite directions must be clear paused.

## Make motion explain dependencies

Distinguish ordered work from independent branches. Requests precede results;
commits precede acknowledgements where source requires it. `activeEdges` is scene
membership, not timing or array-order semantics. The starter runs active packets
concurrently; adapt the output template with explicit phases when that would imply
false order. Choose scene splits using [story boundaries](presentation.md#one-story-one-clock),
not one scene per technical exchange. Preserve genuinely parallel work and the shared clock.

Budget readable result time as well as transitions. A result briefly flashed at a
scene's end fails the explanation. Inspect actual playback and paused selection;
shorten transitions, hold the received state or split processing from observation.
Do not expose actor-visible state before its evidenced response/read/push.

## Inspect and revise the export

Open the actual HTML at normal zoom, both laptop sizes and supported themes. Use
stable readable frames plus real motion: early, busiest, reverse-direction and
prerequisite-bearing scenes, including paused/reduced-motion states.

1. Judge whole-map composition before individual geometry. Can a newcomer follow
   the business flow and distinguish user actions from background initiators?
   Trace the longest detour and busiest hub; report avoidable bends, loops or
   crossings even when every line clears text.
2. Find current work, then trace source, destination, direction and purpose with
   dots stopped. Repeat with the connected full overview, not only focused paths.
   Check both ends of every connector against visible node boundaries or ports.
   A small consistent gap is acceptable only when attachment is unambiguous;
   an endpoint aligned to an invisible container but detached from the visible
   node is a material defect, even when obstacle-clearance checks pass.
3. Follow the closest parallel pair and heads through their entire shared region,
   including captions. Inspect crowded endpoints and simultaneous branches. Use
   measurements and nonzero selector coverage where ambiguous, at both sizes.
4. Read the legend literally against current, earlier and planned/uncertain lines.
   Watch a dependent handoff: the result must follow its prerequisite.
5. Select a scene using real controls. Selection must reveal its title and relevant
   activity, with keyboard focus and complete map access preserved.

When a trace fails, revise the owning model/template and regenerate. Correct the
cause, not just one elbow. Recheck sibling routes/states after port, node, label,
color or routing changes. Preserve the presentation anchors. An automated pass
cannot override an observed trace failure; unresolved ambiguity is a delivery gap.
