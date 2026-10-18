# Interaction contract

Use these phases for the assigned journey or surface. Reuse sufficient existing records; the contents below are decision aids, not mandatory headings or separate documents.

## 1. Ground the experience and its authority

Read product intent, scoped requirements and acceptance scenarios, their sources and status, relevant glossary and decisions, existing journeys and screens, project constraints, and the verifier's affected recipes when available. Inventory existing specifications and mocks before proposing replacements. Distinguish current implementation, current accepted design, proposed changes, and historical evidence.

For consequential claims whose provenance is missing, retain that uncertainty instead of treating an agent-authored specification or a polished mock as acceptance. Review material assumptions before depending on them; preserve established artifacts and avoid reopening every incidental detail. Inspect observable facts first. If a material human choice is needed to complete the assigned outcome and cannot reasonably be inferred or resolved within delegated scope, ask one focused question and wait. A proposal or review can instead record an unresolved choice, its affected behavior and next owner when the requested result can remain conditional.

Use the existing [decision-record convention](../../domain-modeling/references/adr.md) to preserve authority, scope, sources, rationale, unresolved choices, and evidence limits. Link to the owning record; do not repeat its status in a second registry. An accepted requirement does not authorize every possible presentation of it. Evidence that a prototype works and evidence that a person accepted a decision answer different questions.

For example, retaining attributable changes can be an agreed requirement. Showing that history beside a record is a presentation proposal. Adding an application-wide Activity destination introduces a further scope and navigation choice. Justify those interpretations separately and check their authority.

## 2. Model people, journeys, and states

Use the project's vocabulary; clarify consequential ambiguity through [domain-modeling](../../domain-modeling/SKILL.md). Keep these concepts distinguishable without forcing them into the data model:

- A person is an individual; a persona describes a useful pattern of goals or circumstances.
- A role describes responsibilities in a context; permissions describe allowed actions, and scopes bound the information or resources those permissions cover.
- One person may hold several roles. A role distinction alone does not justify separate accounts, applications, tabs, or experiences.

Features, stories, journeys, and requirements are related views of outcomes, not a compulsory hierarchy. A journey may cross several features and requirements; one requirement may constrain many journeys. Reuse the product's map and link relevant views. Keep it distinct from the verifier's operational map of runnable checks.

For the affected journeys, identify entry points, prerequisites, actions, state transitions, completion and failure outcomes. Follow handoffs to their recipient, discovery path, information scope, and next action, including interrupted work and later sessions. Represent relevant empty, unavailable, forbidden, recovery, and pending states according to the product contract. Return missing business rules to product rather than filling them with an unmarked default.

## 3. Propose purposeful structure

Choose navigation, grouping, information prominence, and interactions that support those journeys. Apply relevant approved principles with their scope and exceptions. Use existing components and patterns where they fit; routine styling and established controls retain normal design discretion.

Explain consequential surfaces and groups of controls in the smallest useful form. For each, make these relationships inspectable:

| Content | Decision it supports |
| --- | --- |
| Purpose and linked outcome | Why the surface or control group belongs |
| Actor, role, permissions, and information scope | Who can see or act, and in what context |
| Actions, states, and failure paths | What happens and how unfinished or failed work is handled |
| Requirement and scenario references | Which intended behavior it expresses |
| Presentation rationale and alternatives | Why this navigation, grouping, or prominence is suitable |
| Owning decision and evidence references | What supports the choice and what remains unsettled |
| Verification path or gap | How the relevant outcome could be observed |

Related routine controls may share a parent interaction's rationale. Do not invent a product requirement for every control merely to populate a traceability table. A defensible presentation choice can derive from an outcome, usability evidence, a constraint, or an established pattern; make that derivation clear.

When a consequential interaction remains unsettled, compare structurally different alternatives, using the entry skill's Arena route when independent candidates could supply evidence that changes the choice. Keep alternatives within the same behavior contract unless proposed semantic differences are explicit. Use a prototype when rendering or exercising it can answer the assigned interaction or presentation question. Record the selected base, incorporated strengths, tradeoffs, remaining disagreement, and conditions for reconsideration. Independent candidates and reviewer consensus do not confer product-owner acceptance.

### Preserve an inspectable visual reference when needed

For requested UI refinement or explicit presentation constraints, treat the rendered experience as a reviewable design artifact. Carry explicit user instructions alongside behavior requirements; a property does not become discretionary because it is cosmetic. Preserve the affected component, placement relative to its surrounding layout, applicable viewport/state and relevant style tokens or values. Reuse existing component definitions rather than maintaining a second style catalog. Treat established shared tokens and component rules as constraints. Prototype overrides remain local proposals; changes to shared design-system definitions need a caller-assigned owner and review of affected consumers before production adoption.

Words such as “blue” or “right corner” may still admit different interpretations. Use existing project conventions or render a labeled proposal that the human can inspect. If an unresolved interpretation prevents the requested outcome, follow the existing focused-question rule. Do not claim an inferred shade, container or dimension was specified or accepted.

Link an identifiable prototype revision and useful rendered views to the owning interaction/design record, with relevant component/style sources. Preserve the scope and source of acceptance or delegation, fixed constraints, unresolved properties, responsive behavior and states inspected. Do not infer acceptance of unseen states or viewports. Exact dimensions belong here only when specified, established by the project, or accepted through review; other properties retain the agreed discretion.

The reviewed artifact is the scoped appearance reference, and the behavior contract remains the behavioral authority. Record conflicts and changes through the existing decision convention. For coupled prototype-led review and refinement, [UI Refinement](../../ui-refinement/SKILL.md) owns the bounded cycle and returns the reviewed inputs to its caller.

## 4. Check coverage in both directions

Trace each relevant requirement and acceptance scenario forward to its interaction, including failures and permission boundaries. Identify absent required behavior even if the happy path looks complete. Some requirements are enforced outside the UI; link their technical or verification owner rather than inventing a screen.

Trace consequential UI choices backward to their purpose, requirement or other rationale, and decision authority. Look for added functionality, misleading role boundaries, unexplained prominence, or navigation that claims more scope than the product contract.

State the scope of each sketch or mock and intentional omissions. Distinguish behavior intentionally absent from a particular mock, behavior absent from the proposed product, and implemented behavior that has not been verified. A limited mock cannot silently remove a requirement or prove the full product satisfies it.

## 5. Record and hand off

Use the caller's designated document or an existing canonical section. Create a project UX document only when its audience and future use warrant one under the shared retention rules. A read-only request returns proposed content. Link canonical requirements and decisions instead of copying their authority into a new system.

For projects using OpenSpec, follow the [OpenSpec reference](../../aapilot/references/openspec.md) for document ownership, proposed/current records, reconciliation, and archive links. Other projects use their existing requirements and documentation conventions. Updating a mock does not accept a proposal or supersede a decision.

Give the technical owner the interaction model, reviewed visual reference and component/style sources when present, constraints, requirement links, consequential rationale, mock scope, and unresolved decisions. Give the verification owner affected scenarios, concrete user actions and expected observable outcomes, relevant states/scopes, supporting prototype evidence, and gaps. Link the existing verifier rather than starting implementation from a design-only assignment.

Separate structural review and traceability from human acceptance, observed usability, and runtime correctness. Record what was actually inspected or exercised, its source identity and limits. Deliver unresolved decisions to their owner with the smallest next action needed.
