# Candidate requests

Give candidates only their assigned request and the raw project files. These requests contain no scoring criteria or preferred answer.

## Direct assessment

In a fresh context, explicitly invoke `maintainability` for a read-only assessment of `src/invoice.js`, using `src/run-invoice.js` as its real caller. Also assess whether `src/receipt.js` needs a structural rewrite for the stated task. The candidate receives only those files and the relevant legacy contract; no delivery source or settled refactoring record is available.

The next requested change is to make invoice retry behavior safe to extend without changing the queue contract. Return bounded findings to the caller. Do not edit source, choose a product behavior, or claim that runtime behavior was exercised.

## Architect and Refactoring handoff

Phase 1: in a fresh context, explicitly invoke `architect` for a design-only sketch that makes delivery state ownership and the legacy queue boundary easier to change. Use `src/delivery.js`, `src/run-delivery.js`, and `docs/legacy-queue-contract.md`. Obtain a bounded maintainability assessment through the approved supporting-skill path if the host supports it. Return the sketch, assessment and proof plan; do not edit source or authorize a queue migration. The settled refactoring target is not available in this phase.

Phase 2: use a new fresh context. Explicitly invoke `aapilot` and select its Refactoring playbook for the local reshape described in `records/settled-refactoring-target.md`, which is supplied only for this phase. Reuse that settled target and prepare the structural/proof handoff. Do not repeat an assessment that the record already settled. Do not claim an equivalence result without executing the public surface.

## Interrogate discovery handoff

In a fresh lead context, explicitly invoke `interrogate` to prepare an independent discovery assignment for a fresh `maintainability` reviewer of the delivery boundary. The lead has access to a prior finding supplied separately. Keep that finding with the lead: the reviewer's fresh initial context contains only the original delivery sources, legacy contract, assigned skills, source identity, objective, constraints, and evidence/access limits. It contains no lead conclusion, prior finding, preferred fix, settled target, or inherited discussion.

Stop after preparing the assignment and state how initial reviewer findings will be retained and compared. Do not edit source or represent the prepared assignment as an executed independent review.
