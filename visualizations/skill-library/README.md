# Ahmad Abdalla's Pilot System Graph

Open `index.html` directly, or serve this directory with any static HTTP server.

The map is a curated semantic view of the current skill library rather than an automatic Markdown-link graph. It distinguishes:

- routes selected by `aapilot`;
- conditional supporting calls;
- ownership handoffs and feedback;
- shared execution and principle foundations;
- agent roles that execute project-owned procedures without adding portable skills.

Hover or select a node to suppress unrelated lines and inspect its incoming and outgoing interactions in the inspector. Use **Hide details** when the graph needs the full width. Focused paths are painted above the background network. To prevent labels from visually breaking dense arrows, on-canvas relationship labels appear only for a traced path. **Trace from aapilot** highlights a shortest directed path from the entry skill to the selected node and frames that route. Use the visible zoom controls, the scroll wheel, or pan the canvas for close inspection; **Fit map** restores the full overview. The URL hash preserves the selected node for later discussion.

The map intentionally does not draw a foundation edge from every procedural skill to the execution contract and principle index. Their system-wide scope is recorded on the foundation nodes without obscuring task flows.

The execution contract owns [delegation](../../skills/aapilot/references/execution.md#delegation), [completion](../../skills/aapilot/references/execution.md#completion) and [review context](../../skills/aapilot/references/execution.md#review-context). Aapilot assigns execution and checks results under those shared rules; review context distinguishes independent discovery from confirmation/evidence audits.

Architect owns design and verification planning only. Feature, Bug Fix, Refactoring, and Figure It Out call Implement for bounded edits and development checks, then assign a separate verification agent under the execution contract. The agent uses the project-owned verifier; it is labeled **Agent role** and is excluded from the skill count. Caller handoffs return design contradictions to Architect, which returns revised design packages to those callers. There is no Architect-owned implementation runtime.

The project verifier is a procedure, the verification agent executes it, and Interrogate supplies adversarial review. The caller owns integration and acceptance. Existing prescribed low-impact presentation exceptions remain in the execution contract.

Maintainability is a conditional supporting assessment for Architect, Refactoring, and Interrogate. It returns findings to its caller, which retains the design, review, or implementation decision; it is not an aapilot route.

Bug Fix and Refactoring use the [Architect design trigger](../../skills/architect/SKILL.md#design-trigger) for their design assignments. Architect owns that criterion; editing several function bodies alone does not select the route.

## Maintain the map

- Edit node titles, descriptions, source links, and positions in the `nodes` array in `app.js`.
- Keep the five main columns about 449 SVG units apart. If the outer columns move, update `lanes` and `fullView` together so the overview retains its margins.
- Add or remove a relationship with `connect(from, to, type, label)`. Use `route`, `support`, `handoff`, or `governance`.
- Keep nodes inside the four `lanes`; widen or move a lane only when the overview no longer fits cleanly.
- Do not hand-tune individual arrow curves. Connections are assigned ordered ports on each card so dense routes separate consistently.
- After structural changes, inspect the full overview, a dense selected node such as Feature, and a traced path from aapilot.
