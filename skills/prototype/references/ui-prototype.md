# UI prototype

Render one contextual candidate when refining specified presentation, or contextual alternatives when a consequential navigation, information hierarchy or interaction choice needs to be inspected. Use [logic prototype](logic-prototype.md) when the uncertainty is the business-state model itself.

## Establish a comparable context

Carry the page's purpose, actors and scopes, authoritative requirements, existing interaction decisions, and the unresolved question into each variant. Identify what observations distinguish the alternatives. A presentation alternative must not quietly change required business behavior or add product scope; mark those differences as proposals and return them to their owner.

Inspect the surrounding application: navigation, component vocabulary, realistic content density, and the routes or journeys entering and leaving the surface. Prefer mounting alternatives in a copy of the relevant page or application shell inside an isolated checkout. For a new surface, use the intended surrounding shell or explain which context is unavailable. A blank standalone page can hide navigation and density problems.

Use representative fixtures with the same data, actor, scope and starting state across variants. Stub mutations and isolate data access; reproducing the application's appearance does not authorize its live connections. For a permitted read-only dependency, document its identity and variability. Do not count mock results as evidence of backend behavior.

## Render and refine a specified candidate

When the assignment is to make requirements and explicit visual instructions inspectable, use one candidate unless alternatives answer a real question. Preserve the caller's presentation constraints and relevant component definitions. Show the actual rendered result, including states and viewports needed for the review. Use the [interaction contract's visual-reference guidance](../../interaction-design/references/interaction-contract.md#preserve-an-inspectable-visual-reference-when-needed) for handoff contents. Preserve an identifiable source revision and useful rendered views after refinements; a changing local URL alone cannot identify what was reviewed.

## Construct distinct alternatives

Choose enough alternatives to discriminate the actual question. Two materially different structures can be sufficient; do not manufacture variants for routine visual adjustments. Preserve established constraints and component conventions while varying the consequential structure: grouping, placement, primary action, navigation or disclosure. Color and copy changes alone do not explore those decisions.

For a consequential unsettled interaction where independent candidates would help, use [arena](../../arena/SKILL.md) for candidate generation and synthesis. Keep its bounded question and comparable fixtures intact. Delegate variant files with nonoverlapping ownership; reserve shared wiring for one owner. Human preference remains a human decision even when agents agree.

Make the alternatives easy to inspect together. A local route with a stable `?variant=` key or an equivalent selector can preserve the current choice across reloads and give each variant a reproducible address. Label each alternative by its structure and keep the prototype controls visually separate from the proposed interface. Avoid obscuring the content being compared. If keyboard switching is useful, preserve input editing and normal focus behavior.

Keep scenario reset available. Switching variants should restore equivalent fixture state or explicitly preserve comparable state, rather than inadvertently making one variant appear more complete. Wire the interactions needed to answer the question; clearly label unimplemented behavior and intentional omissions. Cosmetic click handlers must not masquerade as working flows.

## Inspect and hand back

Drive the same representative journey through each variant, including consequential failure or empty states and relevant viewports. Inspect navigation, action discoverability, information visibility and the result of the interaction. Check the selector and reset themselves before comparing. Capture useful views alongside interaction observations and record intentional coverage omissions.

Distinguish observed operation, an agent's design assessment and actual participant feedback. Do not claim usability acceptance from screenshots, a self-authored score or model consensus. When authorized feedback selects a base and combines elements, recheck the resulting composition; the original variants' observations do not automatically validate it.

Return the variant addresses or artifact paths, launch/reset instructions, comparison evidence, rationale, actual feedback and unresolved decisions under the [skill's handoff contract](../SKILL.md#observe-and-return). Keep the artifact out of production delivery; even a preferred variant requires the normal implementation and verification workflow.
