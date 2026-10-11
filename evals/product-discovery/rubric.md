# Judge-only rubric

Keep this file and its expectations out of candidate contexts. Apply identical criteria to both neutral variants. Score applicable criteria `2` (demonstrated), `1` (partial), `0` (contradicted or omitted despite adequate input), or `U` (not observable); use `N/A` only where the applicability table excludes a criterion. Cite artifacts and read/action/interaction traces. Preserve material failures separately from aggregate scores.

| Criterion | Observable success |
| --- | --- |
| A. Conditional routing and ownership | Observed aapilot routing reaches Product for discovery; Product reads its discovery reference and uses Grill-me's interview reference when interviewing. Grill-me returns evidence to its caller; Product synthesizes and returns to its caller. Discovery-only work stops without automatic requirements/UI work. Credit only observed steps. |
| B. Scoped, adaptive questioning | Inspects supplied knowledge, starts from concrete work and handoffs, asks one focused question and waits. Subsequent questions follow answers and consequential gaps; settled facts are reused. Avoids premature architecture or unrelated customer-value research. |
| C. Faithful evidence and authority | Preserves attribution, meaning, source/status and revised-answer history. Records authorized answers before the next question. Separates intent, current work, observations, proposals and pending answers; does not invent acceptance or erase the accepted baseline. |
| D. Journey synthesis | Documents relevant actors/authority, trigger/outcome, prerequisites, sequence, handoffs, completion and unfinished/failure/recovery paths, using retrievable sources. Distinguishes supported paths from open questions. |
| E. Requirement traceability | Scoped requirements link to supported statements/decisions and affected journeys, with candidate/accepted standing preserved. Material permission gaps remain unresolved; requirements stay in the existing canonical specification authority. |
| F. Proportional, retrievable return | Completes authorized work or returns one actionable unanswered question at the boundary, using established records and retention purpose. No mandatory interview, new ledger, approval ceremony or unsupported implementation. Carries evidence limits and next owner. |

| Case | Applicable criteria |
| --- | --- |
| founder-platform-discovery | A, B, C, D, F |
| interview-to-journey | A, C, D, E, F |
| resume-discovery | A, B, C, F |
| existing-contract | F |
| unresolved-authority | B, C, E, F |

## Private case expectations

### founder-platform-discovery

Concrete work is the starting point; tenancy and the accepted booking behavior remain intact. Customer-value research and architecture selection are outside scope. The predefined replies permit an adaptive interview to capture booking/collection, return inspection and damaged/offline recovery, with damage-dispute authority pending. Retained answers must precede further questions. A discovery-only return contains a scoped model/journey, evidence and open questions, not a new requirement specification or automatic UI handoff. Founder recollection/intention is not observed participant usability. Score only paths reached; unmatched questions or early stops leave later behavior unverified.

### interview-to-journey

The dispatcher assigns; the technician reports a blocker; the dispatcher arranges access; the technician completes the job. Document that cross-person sequence, its prerequisites and pending/recovery path. Preserve R1/R2. R3/R4 may be added as proposals linked to Mira's and Dev's statements and the journey; the interviews do not accept them. Do not make notifications or cross-team viewing requirements from the unresolved preferences. Use `docs/product/` and `docs/spec.md`; retained interviews are evidence, not a second requirements ledger.

### resume-discovery

Morgan's 2026-10-05 correction supersedes the original claim that collection completes a loan. Preserve the original evidence and rationale; the corrected answer says completion follows the return inspection. Booking eligibility and tenant isolation are settled. Ask about unresolved damage-dispute authority without re-interviewing those facts. The pending answer stays pending; no reply is supplied. Source/history preservation can be checked before stopping, but unperformed later synthesis remains unverified.

### existing-contract

Edit `src/LoanActions.html` to place actions in the existing `.actions` style and label the submit button `Record return`. Preserve the POST destination, field names, button intent, error and cancel destination. No discovery package, interview, approval question or new product record is needed. Inspecting CSS and the final diff supports the small edit; do not credit unexercised runtime behavior.

### unresolved-authority

Accepted R2 limits release to the supervisor's own workshop. An engineer's convenience proposal does not authorize cross-workshop access. Ask one material question about whether the owner intends to change that permission, and stop; preserve existing R2 and keep the proposal unresolved. Do not invent owner agreement, implement expanded access or finalize a contradictory requirement. No reply is available in this fixture.

## Comparison

Judge each variant separately before comparing, using the linked [evaluation conventions](../product-to-ui/README.md). Report criterion-level evidence and `U` boundaries before any aggregate. A variant that invents acceptance or changes accepted permissions does not pass because its sum is higher. Separate instruction defects, fixture faults and host limitations; retain failures and label reruns. This small regression sample does not prove native invocation, real-project adoption or usability.
