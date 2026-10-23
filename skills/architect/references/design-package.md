# Design package

Use this contract for a candidate sketch and the final synthesized design. Keep it in the current working record or a linked artifact when substantial; these are required contents, not mandatory reply headings.

When retaining a separate project design artifact, keep it discoverable through an existing owning record or design index within the authorized document scope. A link only in a transient handoff reply does not establish project discovery; do not create a second index.

## Candidate inputs and output

Each candidate receives the task, settled constraints, relevant grounding artifacts, evidence limits, applicable principle leaves with their scope, proof criteria, design review questions, and its own output location. A candidate produces one sketch and rationale; it does not run another competition or implement the design.

- **Problem and constraints:** The intended behavior, relevant existing boundaries, accepted solution decisions, non-goals, and assumptions still needing evidence. Preserve sources and their limits.
- **Caller usage:** Realistic calls or interactions written before the types. Reconcile the sketch to this usage.
- **Interaction inputs, when relevant:** Link the project's actual interaction model, following the [interaction contract](../../interaction-design/references/interaction-contract.md), and its decisions, unresolved choices, alternate paths and intentional mock omissions. When present, retrieve the identifiable reviewed visual revision, component/style sources and scoped presentation constraints; preserve them in the implementation brief and verification plan. Preserve these limits in the implementation and verification scope; technical feasibility does not confer product acceptance.
- **Shape:** Data, signatures, module responsibilities, state ownership, invariants, and main flow. Identify how important invariants will be enforced.
- **Rationale:** Consequential choices, accepted tradeoffs, and concrete alternatives considered within this candidate. Compare its shape with the simplest viable option under Architect's [comparison procedure](../SKILL.md#sketch-and-compare); identify the present caller, invariant, or change burden that warrants added structure. Explain effects on callers and credible changes, including the choice an applied principle changed and any consequential exception.
- **Verification plan:** Map important requirements to inputs or actions, independent expected results, real surfaces, and evidence to retain. For affected business state, carry accepted identity/context meanings, ownership, consistency and failure guarantees, and required rejection, concurrency, replay or recovery cases into implementation and independent verification. Select cases by the actual risk. Link the project verifier and affected feature-map entries when present, including alternate paths and dependent callers. Identify required environment or access, missing verification capability, and what remains unverified.
- **Open risks and next step:** Unresolved questions, assumptions that could invalidate the design, and the first implementation step.

## Synthesis ownership

Arena adds the selected base and reason, compatible additions with their source candidates, rejected ideas, and comparison limits. It reconciles usage, shape, constraints, and the verification plan into one package. Candidate alternatives and the selection among candidates are distinct parts of the rationale.

Architect checks and returns the package under its [handoff and revision rules](../SKILL.md#return-and-reconsider), including the standalone design-and-build route. A supported design choice does not establish observed implementation behavior.
