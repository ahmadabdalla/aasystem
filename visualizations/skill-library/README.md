# Ahmad Abdalla's Pilot System Graph

Open `index.html` directly, or serve this directory with any static HTTP server.

Read [How Aapilot works](../../docs/design/verification-contract.md) for the operating design behind these routes, handoffs, human decisions, and verification paths. The guide explains the model; the linked skill instructions own its procedures.

The map is a curated semantic view of the current skill library rather than an automatic Markdown-link graph. It distinguishes:

- routes selected by `aapilot`;
- conditional supporting calls, which may apply a procedure in the current context or dispatch a bounded worker;
- direct consumption of shared assessment criteria;
- ownership handoffs and feedback;
- shared execution and principle foundations;
- agent roles that execute project-owned procedures without adding portable skills.

Hover or select a node to suppress unrelated lines and inspect its incoming and outgoing interactions in the inspector. Use **Hide details** when the graph needs the full width. Focused paths are painted above the background network. To prevent labels from visually breaking dense arrows, on-canvas relationship labels appear only for a traced path. **Trace from aapilot** highlights a shortest directed path from the entry skill to the selected node and frames that route. Use the visible zoom controls, the scroll wheel, or pan the canvas for close inspection; **Fit map** restores the full overview. The URL hash preserves the selected node for later discussion.

The map intentionally does not draw a foundation edge from every procedural skill to the execution contract and principle index. Their system-wide scope is recorded on the foundation nodes without obscuring task flows.

The execution contract owns [decision authority](../../skills/aapilot/references/execution.md#decision-authority), including the inspectable human checkpoint handoff and stop/wait rule, [delegation](../../skills/aapilot/references/execution.md#delegation), [completion](../../skills/aapilot/references/execution.md#completion) and [review context](../../skills/aapilot/references/execution.md#review-context). Aapilot applies or assigns execution and checks results under those shared rules; bounded unattended work preserves the whole-process human-checkpoint stop; review context distinguishes independent discovery from confirmation/evidence audits and preserves initial findings before reporting assistance.

UI refinement owns the [rendering assignment rules](../../skills/ui-refinement/references/refinement-loop.md#rendering-assignments) for coupled Interaction Design and Prototype work. Existing role ownership, caller delivery and required independent reviews and production verification remain in place.

The shared foundation links the standard [verification contract](../../skills/aapilot/references/verification-contract.md) for retained production changes: one root owner retains scope, current evidence, limits and acceptance; specialists contribute to that same run. Feature and direct Implement expose the [owner-presentation path](../../skills/aapilot/references/execution.md#owner-presentation-eligibility), whose owner proof needs no worker. That exception cannot waive independent engineering review required by the user, project, or task. Read-only and design work keep scoped obligations. Existing owners and handoffs remain in place; no coordinator or skill node is added.

Architect owns design and verification planning only. Feature, Bug Fix, Refactoring, and Figure It Out call Implement for bounded edits and development checks, then assign a separate verification agent when required under the execution contract. The agent uses the project-owned verifier; it is labeled **Agent role** and is excluded from the skill count. Caller handoffs return design contradictions to Architect, which returns revised design packages to those callers. There is no Architect-owned implementation runtime.

The project verifier is a procedure; the existing verification agent assesses the actual diff and executes affected checks under [engineering verification](../../skills/aapilot/references/engineering-verification.md). Required independent assessments name affected domains, criteria and evidence under [Delegation](../../skills/aapilot/references/execution.md#delegation); one capable verifier can cover related domains separately from their producers. Qualitative findings and executable observations remain separate claims in one run and report. The caller owns integration, material-finding dispositions and acceptance requests based on current proof. Interrogate supplies adversarial review. The execution contract owns owner-presentation eligibility and escalation; that proof is explicitly distinct from independent verification.

The conditional [host acceptance contract](../../skills/aapilot/references/host-acceptance.md) defines requirements for a future demonstrated integration. The graph adds no runtime role for it; local receipts do not establish host enforcement.

Maintainability owns reusable criteria. Implement and the independent verifier have explicit criteria-consumption relationships to it; these edges do not dispatch another worker. Architect also reads the criteria during design. A deeper Maintainability assessment remains conditional support for Architect, Refactoring, and Interrogate, returning findings to the decision owner; it is not an aapilot route.

Bug Fix and Refactoring use the [Architect design trigger](../../skills/architect/SKILL.md#design-trigger) for their design assignments. Architect owns that criterion; editing several function bodies alone does not select the route.

## Maintain the map

- Edit node titles, descriptions, source links, and positions in the `nodes` array in `app.js`.
- Keep the five main columns about 449 SVG units apart. If the outer columns move, update `lanes` and `fullView` together so the overview retains its margins.
- Add or remove a relationship with `connect(from, to, type, label)`. Use `route`, `support`, `handoff`, or `governance`.
- Keep nodes inside the four `lanes`; widen or move a lane only when the overview no longer fits cleanly.
- Do not hand-tune individual arrow curves. Connections are assigned ordered ports on each card so dense routes separate consistently.
- After structural changes, inspect the full overview, a dense selected node such as Feature, and a traced path from aapilot.
