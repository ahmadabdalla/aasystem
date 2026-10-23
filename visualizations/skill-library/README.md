# Ahmad Abdalla's Pilot System Graph

The [system map](index.html) shows which skills Aapilot calls, how they support each other, and where results return for review. Open `index.html` directly, or serve this directory with a static HTTP server.

For why I built the plugin and how to use it, start with the [main README](../../README.md). [How Aapilot works](../../docs/design/verification-contract.md) explains the workflow behind the map.

## Read the map

The map shows the relationships that matter to the workflow. It is maintained by hand, so it doesn't draw every link between Markdown files.

The connections represent:

- Routes: the skills and playbooks Aapilot selects for a task
- Support: instructions, criteria, or help used for part of the work
- Handoffs: results or unresolved decisions returned to the agent responsible for the next step
- Governance: the shared execution contract and principles

A connection doesn't necessarily mean another agent is started. An agent can read and apply a skill's instructions in its own context. Nodes marked **Agent role** represent agents assigned to do checks; they aren't counted as skills.

The execution contract and principles apply across the library. Their foundation nodes describe that scope without drawing a line to every skill.

## Explore a route

Select a node to see its incoming and outgoing connections in the details panel. Hovering over a node also highlights its connections.

- Use **Trace from aapilot** to follow a shortest directed path to the selected node. Relationship labels appear on that traced path.
- Use **Hide details** to give the map more room.
- Zoom with the controls or scroll wheel, and pan to move around. **Fit map** restores the overview.
- Copy the page URL to share a selected node. The selection is saved in the URL hash.

## Understand the relationships

See [System structure and sources](../../docs/design/skill-system.md) for the full responsibilities and adaptations. A few distinctions help when reading the graph:

- Architect designs the implementation and plans verification. Delivery playbooks call Implement to make the changes. If implementation reveals a design problem, it returns through the playbook to Architect.
- The verification agent reviews the changes and runs the relevant project checks. Aapilot brings the findings together and checks whether the agreed work is complete. Interrogate contributes adversarial review findings. The [verification contract](../../skills/aapilot/references/verification-contract.md) explains the required checks and exceptions.
- Interaction Design can assign two separate agents to assess a rendered interface: one for visual composition and one for interactions. UI Refinement can use that assessment within its [review loop](../../skills/ui-refinement/references/refinement-loop.md). These checks support the required human review and production verification.
- Maintainability supplies shared criteria for design, implementation, and verification. Reading those criteria doesn't start another worker. The [engineering adaptations](../../docs/design/skill-system.md#maintainability) describe the related boundary, refactoring, and business-state references and how their checks reach the verifier.
- 10x supports growth assessments during design and can be called directly through Aapilot. The [growth assessment design](../../docs/design/skill-system.md#growth-assessment) explains how callers use its findings.
- Grill Me uses Domain Modeling to record agreed terms and qualifying decisions when edits are authorized. The [Grilling procedure](../../skills/grill-me/references/grilling.md) explains the question rounds and records.

## Maintain the map

Update the graph when routes, handoffs, or responsibilities change:

- Edit node titles, descriptions, source links, and positions in the `nodes` array in `app.js`.
- Keep the five main columns about 449 SVG units apart. If the outer columns move, update `lanes` and `fullView` together so the overview retains its margins.
- Add or remove a relationship with `connect(from, to, type, label)`. Use `route`, `support`, `handoff`, or `governance`.
- Keep nodes inside the four `lanes`; widen or move a lane only when the overview no longer fits cleanly.
- Do not hand-tune individual arrow curves. Connections are assigned ordered ports on each card so dense routes separate consistently.
- After structural changes, inspect the full overview, a dense selected node such as Feature, and a traced path from aapilot.
