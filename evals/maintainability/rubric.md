# Judge-only rubric

Keep this file and its expectations out of candidate contexts. Score each applicable criterion `2` (demonstrated), `1` (partial), `0` (contradicted or omitted despite adequate input), or `U` (unobservable). Cite project artifacts and read/action traces. Judge each neutrally labelled candidate and phase independently before comparison; candidate assertions do not prove reads, skill invocation, context isolation, or behavior.

| Criterion | Observable success |
| --- | --- |
| A. Local reader and change burden | Grounds findings in `src/invoice.js` and `src/run-invoice.js`; identifies concrete name/control-flow burden and the shared `latestInvoice` state or `channel.send` effects with a causal consequence for a real caller. Gives a proportionate recommendation, tradeoff and proof needed instead of a smell list. |
| B. Boundary ownership and adaptation | Traces caller-visible representation leakage or competing writers in the delivery sketch; identifies a state owner and a change-local boundary. Retains the required legacy adapter as an explicit translation boundary rather than removing it because it is a wrapper. |
| C. Proportionate negative result | Leaves `receiptLabel` without a forced rewrite, or explains a concrete supplied change burden before recommending one. Does not use line count, nesting, or wrapper count alone as a defect. |
| D. Caller handoff and reuse | Architect returns a design-only assessment to its caller. Refactoring uses the supplied settled target, compatibility constraints and proof plan without commissioning a duplicate maintainability assessment; it does not claim equivalence without executing it. |
| E. Independent discovery handoff | The Interrogate lead labels the task independent discovery, preserves source identity, objective, constraints and evidence limits, and withholds the prior finding from the reviewer's initial context. The prepared assignment can later be compared only after initial findings return; actual isolation limitations are reported. |

| Request | Applicable criteria |
| --- | --- |
| Direct assessment | A, C |
| Architect and Refactoring handoff | B, D |
| Interrogate discovery handoff | E |

## Private case expectations

The direct assessment should connect `applyInvoice`'s vague values and branching to the caller's need to understand when delivery occurs. `latestInvoice` is shared mutable process state: a dry run records an ID, and a later call can alter what `retryInvoice` does for a different caller. It should not present source inspection as proof of runtime behavior. The short receipt formatter is already readable and has no supplied change pressure.

The sketch exposes the delivery representation to callers and lets both the service and caller write its state. A useful boundary can make delivery state transitions owned by one module while keeping `toLegacyQueueMessage` because the supplied external queue requires its different shape. The task does not prescribe a single API or prove a migration.

The settled Refactoring target already records the relevant assessment. A repeat assessment is duplicate work; a sound handoff instead carries forward the target, constraints and required public-surface proof. In the discovery case, the lead-only finding argues for deleting the adapter. It is intentionally not a reviewer input. A correct prepared assignment alone does not establish that the fresh reviewer avoided anchoring.

Do not count `U` as a pass. Report criterion evidence before any aggregate. A revised-only run cannot support an improvement claim, and a prepared assignment cannot prove reviewer behavior, context separation, or native host composition without the recorded follow-on execution.
