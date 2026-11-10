# Explanation model, version 1

Read while authoring or adapting a model. `scripts/build.py` validates references
and generates standalone HTML; it cannot establish whether a claim matches source.
Use UTF-8 JSON. Strings are plain text, never HTML or executable instructions.

## Shape

```json
{
  "version": 1,
  "title": "A project journey",
  "summary": "The bounded behavior being explained.",
  "basis": "repository",
  "sources": [{"id": "source", "label": "Request handler", "location": "src/requests.py:12"}],
  "lanes": [{"id": "operator", "label": "Operator actions", "initiator": "A person submits a request"}],
  "components": [{
    "id": "api", "label": "Accept request", "technology": "HTTP service",
    "responsibility": "Validate input and persist a pending request",
    "kind": "service", "lane": "operator", "row": 1, "column": 1,
    "status": "implemented", "evidence": ["source"]
  }],
  "edges": [],
  "scenes": [{
    "id": "received", "title": "Request received", "description": "The service validates the submitted request.",
    "trigger": "A client submits input", "duration": 6,
    "status": "implemented", "evidence": ["source"],
    "activeComponents": ["api"], "activeEdges": [],
    "experience": {
      "actor": "Client", "surface": "HTTP response", "layout": "terminal",
      "state": "Accepted", "title": "Request accepted", "body": "Processing is pending.",
      "fields": [{"label": "Status", "value": "202 Accepted"}], "actions": []
    },
    "behind": [{"component": "api", "action": "Store the pending request"}]
  }]
}
```

`basis` is `repository` or `synthetic`; the latter explicitly identifies a fictional
reference. The renderer always presents an explanation/simulation, never live actions.

## Components and layout

Kinds: `person`, `interface`, `service`, `process`, `queue`, `store`, `external`.
`label` expresses a business capability or recognizable actor; `technology` names
the implementation, and `responsibility` connects them. Use source vocabulary.
Split a component only when the distinction changes understanding. Avoid an icon
inventory of infrastructure that does not participate in the selected journey.

Each component belongs to a lane and a unique positive `row`/`column` pair within
that lane. Use up to six columns. Lanes follow array order; desktop cells follow
their coordinates. Preserve causal reading order across the supported laptop
layouts. A lane caption states its initiator or explains its
shared role; it does not imply that every node in that lane calls every other node.

Start with a small, representative slice (usually 6-15 components); split long
journeys when comprehension degrades. These are design criteria, not numeric gates.

## Exchanges and scenes

Each edge has `id`, `from`, `to`, `label`, `kind`, `status`, `evidence`.
Edge kinds: `request`, `event`, `read`, `write`, `response`, `observe`.
Direction describes that particular exchange. Do not reverse calls to beautify a
route. Use a separate response edge only when that exchange matters to the story.
`observe` expresses a non-calling relationship; it must not imply that a background
write starts an unrelated browser request.

Scenes are ordered, with duration in seconds (2-30). A scene names its actual trigger,
and may provide `short` for a concise numbered timeline label. It names its
experience state and backstage work. `activeComponents` highlights relevant nodes;
`activeEdges` animates only exchanges occurring in that scene. A component appearing
in a scene is not evidence that all its connections execute. Every `behind` item maps
an action to a component, so the renderer can show its business role and technology.
Include both endpoints of each active exchange and every current backstage component
in `activeComponents`; the builder rejects inconsistent highlights.

Experience layouts: `message`, `pipeline`, `workbench`, `review`, `dispatch`,
`register`, `list`, `record`, `terminal`. They represent distinct visual scenes,
not identical cards with changed text. Use the richer fields below when appropriate.
Actions are illustrative labels, never requests to a live system. Use a terminal
for an API/CLI and do not invent a product dashboard.

## Reference-pattern presentation fields

Optional top-level `presentation`:

```json
{
  "name": "ServiceFlow",
  "mark": "SF",
  "navigation": ["Intake", "Requests", "Review", "History"],
  "boundary": {"label": "Application boundary", "detail": "Logical grouping / synthetic example"},
  "accent": "#1d4ed8"
}
```

The renderer supplies the demonstrated shell even when this object is absent.
`accent` is an optional six-digit hex color; other styling is adaptable in a copied
template. A boundary is logical unless source supports a deployment boundary.

Components may add `placement: inside|outside` and a positive `step` referring to a
scene number for a primary story badge. Outside actors/services use column1 on
desktop; reserve columns2-6 for inside components. Defaults classify person/external
as outside and other kinds as inside. Do not invent a hosting boundary to fill space.
Optional `icon` selects a semantic outline symbol: `person`, `browser`, `service`,
`process`, `queue`, `store`, `message`, `external`; defaults follow kind. An external
inventory adapter is not a mailbox merely because both are outside the system.

Experience may add:

- `mode`: `observed` (default) or `explanation`; an explanation is visibly labeled
  system-processing content and is not claimed to be the actor's received screen.
- `nav`: active navigation label from `presentation.navigation`.
- `items`: `[{"title":"Request R-1042","detail":"Portable projector","state":"Needs review"}]`;
  used as workbench selection, review checks or an outbound package list.
- `stages`: `[{"label":"Accept","detail":"HTTP service"}]` for a processing
  pipeline; `packet` supplies its traveling-object label, such as `REQUEST`.
- `columns`: an array of plain column labels and `rows`: an array of plain string
  arrays of the same length, for review/register tables.
- `audit`: `[{"label":"Request received","detail":"Pending state recorded"}]`
  for the register's vertical event history.

Existing `fields` remain plain label/value pairs. Select a visual form because the
moment needs it, not to exercise every type. See [presentation](presentation.md)
for the preserved geometry, meaningful motion and screenshot comparison contract.

## Evidence and uncertainty

Status: `implemented`, `planned`, `inferred`, `unknown`. Components, edges and scenes
require this status and an `evidence` array of source IDs. Non-unknown claims need
at least one source. `inferred` and `unknown` also require a short `note` explaining
the uncertainty. A design document supports planned behavior, not proof of running
production. `location` is a retrievable file/line, document section or permitted URL;
the HTML displays it as text and performs no network request.

Collect source support first, then author the model. Mark synthetic examples as
synthetic throughout. A valid model proves structural consistency, not causal truth,
human acceptance, completeness or deployment health. No secrets or real personal
data belong in a distributable example.

Identifiers use lowercase letters, digits and hyphens, beginning with a letter,
and must be unique within their collection. Self-edges are unsupported; show work
inside a component through `scene.behind`. Every lane, endpoint, active
element, backstage component and evidence ID must resolve. Preserve unknowns rather
than manufacturing relationships to make a more complete-looking picture.

## Business-workflow profile

Set `presentation.profile` to `"business-workflow"`. Omitted or `"technical"`
preserves the contract above, existing models and default Experience view. Unknown
profiles fail validation. Business map uses the same `components`, `edges`, `scenes`,
source ledger, experience forms and provenance rules; it does not add a second
renderer-owned meaning model. See the complete valid
[business model](../examples/business-workflow.json) and its
[fictional source](../examples/business-workflow-source.md).

| Field | Business contract |
| --- | --- |
| `lanes[]` | `id`, `label`, `initiator` (responsibility caption), `performer`: `human`, `software` or `external`; `layout: {y, height}` |
| `components[]` | `id`, `label`, `kind`: `activity`, `decision` or `outcome`, exactly one `lane`, `status`, `evidence`, optional plain `detail`; uncertainty also needs `note` |
| Node navigation | `scene` references one scene ID and is required except on outcomes. The referenced scene highlights the node. Multiple nodes may share a scene; badges derive from scene order. No parallel `step`, `row`, `column` or `placement` |
| Node geometry | `layout: {x, y, width, height}` places the complete shape inside its canonical lane; it cannot override label, performer, status or scene |
| `edges[]` | Existing identity/endpoints/label/evidence, with `kind`: `sequence`, `branch` or `prerequisite`. Branches also require a readable `condition`; `label` is the visible concise caption. A decision label is a complete question ending in `?` with at least two distinctly conditioned branches |
| Relationship geometry | `layout: {points: [[x,y], ...], label: {x,y}}`; ordered orthogonal points include source and target ports; the label coordinates locate the canonical caption |
| `stateDimensions` | Nonempty ordered declarations `[{id, label}]`; each scene's `states` supplies a nonempty string for every declared ID, with no undeclared IDs |
| Scene timing | Optional `phases: [{edges: [edgeId, ...]}, ...]` declares ordered groups; every `activeEdges` member appears exactly once and all endpoints are in `activeComponents`. Omission gives one phase. Multiple phases must be nonempty. Prerequisites can highlight but never animate a traveling object |

Business nodes do not require technical `technology` or `responsibility` fields.
Scene `trigger`, `behind`, active participants and Experience retain their existing
requirements. Explain the actual human/external trigger even when a prerequisite
permits an activity. A sequence shows business progression, not a network event.

The bundled map requires `presentation.canvas: {width, height}` and the layout
objects above. Width is 400–10000 and height 200–10000 map units. Lanes are at
least 60 units high and cannot overlap; nodes are at least 40×30 units. All
coordinates are finite numbers (not booleans), within the canvas and, for nodes,
their lane. Routes have 2–100 distinct consecutive orthogonal points. Layout
objects accept only their documented keys. These bounds establish model validity;
rendered text fit, docking, label clearance and unobstructed routes still need
browser checks. Layout cannot silently change canonical responsibility/navigation.

For example, a scene can include staff saving input followed by a software check:

```json
{
  "activeComponents": ["complete-request", "check-stock", "plan-allocation"],
  "activeEdges": ["save-details", "calculate"],
  "phases": [{"edges": ["save-details"]}, {"edges": ["calculate"]}],
  "states": {"request": "Details checked", "plan": "Draft", "reservation": "Not submitted", "collection": "Unrecorded"}
}
```

This is a scene fragment within a model declaring those IDs and dimensions, not
a standalone model. Invalid variants fail with a field-specific error:

| Invalid edit to the valid fixture | Reason |
| --- | --- |
| `presentation.profile: "business"` | Unknown profile |
| Node `lane: "missing"`, `scene: "missing"` or `evidence: ["missing"]` | Unresolved reference |
| Add node `step: 4` or `layout.scene: "approve"` | Duplicate navigation or semantic layout override |
| Remove a scene state or add `states.invoice` | Missing/undeclared dimension |
| Remove a branch condition or leave a decision with one alternative | Incomplete decision |
| Put a non-active relationship in `phases`, repeat one or omit an active one | Inconsistent ordered activity |
| Put a node outside its lane or use a non-finite/diagonal route | Invalid layout |

Validation cannot decide whether an activity mixes performers or whether a label
answers a reader's question. Follow the source and map-only reader review in
[verification](verification.md#source-and-model).
