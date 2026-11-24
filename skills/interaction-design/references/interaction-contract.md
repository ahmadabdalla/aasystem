# Interaction contract

Work through these five phases for the assigned journey or surface. Write the results in the project's own format.

## 1. Ground

1. Read the product contract and its scenarios, the glossary, decisions, existing screens and mocks, and the verifier's recipes if there are any.
2. Label everything you rely on as built, accepted, proposed or history. If you can't find who accepted it, label it proposed, even if it's a polished mock or an agent-written spec marked approved.
3. If the result can stay conditional on a human choice, record the open choice, what it affects and its owner.

An agreed requirement doesn't approve every way of showing it. "Keep a history of changes" may be agreed. Showing that history beside the record is a presentation proposal. A new app-wide Activity page is a further scope and navigation choice. Check the authority for each one separately.

Record authority, sources, rationale and open choices with the [decision-record convention](../../domain-modeling/references/adr.md). Link the record; don't copy its status.

## 2. Model people, journeys and states

Use the project's terms. If one is unclear, call the Skill tool with "domain-modeling" ([domain-modeling](../../domain-modeling/SKILL.md)).

One person can hold several roles. A role alone doesn't justify a separate account, app, tab or experience. Keep roles (responsibilities), permissions (allowed actions) and scopes (the data those actions cover) distinct.

For each affected journey, list its entry points, prerequisites, actions, state changes, and how it finishes or fails. For each handoff, name who receives it, how they find it, what they can see and what they do next, including work picked up in a later session. Show the empty, unavailable, forbidden, pending and recovery states the product contract defines. If a business rule is missing, return it to Product; never fill it with an unmarked default.

## 3. Propose structure

Choose navigation, grouping, prominence and interactions that serve those journeys. Apply the relevant approved principles. Reuse existing components and patterns.

For each consequential surface or group of controls (one that changes navigation, who can see or do something, or a screen's primary action), give its purpose, who can see and act on it, its actions and states including failure, the requirements it serves, why this shape beat the alternatives, the record that decided it (or "open"), and how its outcome can be observed.

Routine controls share their parent's entry. A rationale can come from an outcome, usability evidence, a constraint or an established pattern. Never invent a requirement to fill the field.

If you compare alternatives, keep them on the same behaviour contract unless a semantic difference is stated.

Before settling a consequential model, call the Skill tool with "10x" ([10x](../../10x/SKILL.md)) and carry its findings into the rationale and how the outcome is observed.

### Preserve an inspectable visual reference when needed

Use this when the request is UI refinement or the user gave explicit presentation instructions.

- Treat explicit visual instructions as requirements. Being cosmetic doesn't make them optional.
- Record the component, its placement in the surrounding layout, the viewport and state, and the tokens or values that apply. Link component definitions; don't keep a second style catalogue.
- Shared tokens and component rules are constraints. A prototype override is a local proposal. Changing a shared definition needs an owner named by the caller and a check of everything that uses it.
- If an instruction like "blue" or "top right" is ambiguous, use the project's convention or render a labelled proposal for the human. Never claim an inferred shade or size was specified.
- Link the prototype revision and rendered views from the design record. Note who accepted what, the fixed constraints, open properties, and which states and viewports were inspected. Uninspected states and viewports aren't accepted. Record exact dimensions only if they were specified, already exist in the project, or were accepted in review.

The reviewed artifact is the reference for appearance. The behaviour contract stays the reference for behaviour. Record conflicts with the decision convention. If the work is a review-and-refine cycle, [UI Refinement](../../ui-refinement/SKILL.md) owns it.

## 4. Check coverage both ways

- **Forward:** trace every requirement and scenario, including failures and permission limits, to an interaction. If a requirement is enforced outside the UI, link its technical or verification owner instead of inventing a screen.
- **Backward:** trace every consequential UI choice to a purpose and an authority. Flag added features, misleading role boundaries, unexplained prominence and navigation that promises more than the contract.

For each sketch or mock, state its scope and what it leaves out. Say which of three each missing behaviour is: left out of this mock, left out of the product, or built but unverified.

## 5. Record and hand off

Write into the caller's document or an existing canonical section. Create a new UX doc only if someone will use it later. If there's no document to write into, or the work is read-only, put the model in your reply, never only in a scratch file. Put the design in the document; keep sources, review notes and evidence limits in your reply. If the project uses OpenSpec, follow the [OpenSpec reference](../../pilot/references/openspec.md).

Give the technical owner the model, the visual reference and component sources if there are any, the mock's scope, and open decisions with their owners.

Give the verification owner each affected scenario as user actions and the result they should see, the states and roles to cover, what any prototype actually exercised, and the gaps.

Don't start implementation from a design-only assignment.
