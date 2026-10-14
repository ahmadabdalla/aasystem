# Maintainability evaluation

This package exercises bounded assessment of local code and module boundaries, plus the handoffs from Architect, Refactoring, and Interrogate. Follow the [evaluation playbook](../../skills/aapilot/playbooks/eval.md) and the [runner and evidence conventions](../product-to-ui/README.md). It has no runner and does not establish runtime behavior, native skill discovery, or improvement over a baseline.

## Revised-only run

1. Save the complete revised skill tree and its referenced dependencies outside the working checkout. Record its source identity, dirty diff and content hashes. A revised-only run can support only the exercised behavior; do not describe it as an improvement without a separately preserved baseline under comparable conditions.
2. Materialize a separate, fresh writable project for every candidate phase. Copy only the phase's listed files from [fixtures/project.md](fixtures/project.md):
   - Direct assessment: `src/invoice.js`, `src/run-invoice.js`, `src/receipt.js`, and `docs/legacy-queue-contract.md`. Exclude delivery sources and `records/settled-refactoring-target.md`.
   - Architect phase 1: `src/delivery.js`, `src/run-delivery.js`, and `docs/legacy-queue-contract.md`. Exclude the settled target.
   - Refactoring phase 2: `src/invoice.js`, `src/run-invoice.js`, `src/delivery.js`, `src/run-delivery.js`, `docs/legacy-queue-contract.md`, and `records/settled-refactoring-target.md`. Supply the settled target only in this phase.
   - Interrogate lead: `src/delivery.js`, `src/run-delivery.js`, `docs/legacy-queue-contract.md`, and [fixtures/lead-only-prior-finding.md](fixtures/lead-only-prior-finding.md). The fresh reviewer copy contains only the original delivery sources and contract, plus the assigned skills; it excludes the lead-only finding, settled target, and inherited conversation.

   Give each fresh context only its request, raw project, revised snapshot, and the same tools and action limits. Keep this README, [rubric.md](rubric.md), other requests, outputs, and judge expectations outside its context.
3. Use the intended entry point stated by each phase: explicitly invoke `maintainability` for the direct assessment; invoke `architect` for the design-only sketch; invoke `aapilot` and select its Refactoring playbook for the already-settled local target; invoke `interrogate` for the lead's discovery-assignment preparation. Explicit use tests application of that entry point, not automatic discovery.
4. For the Interrogate phase, retain the lead-only finding with the lead. Run the prepared assignment in a separate fresh `maintainability` context using only the reviewer copy defined above. Preserve the reviewer's initial findings before the lead compares them with the prior finding. If the host cannot enforce those limits, record the exposed paths and inherited history.
5. Preserve actual prompts, source identities, accessible paths, context inheritance, reads/actions, candidate artifacts, questions, and failures outside this reusable package. Give a fresh judge the raw fixture, neutrally labelled outputs, available traces and [rubric.md](rubric.md). Judge each output before comparing phases. Do not infer a read, supporting invocation, isolation, or implementation behavior from a candidate's claim.

The Architect phase stops at a design package. The Refactoring phase receives the settled assessment and prepares the structural/proof handoff without repeating that assessment. The Interrogate phase stops at a prepared assignment; only the separately recorded reviewer execution can demonstrate discovery behavior.

## Requests

| Request | Candidate work |
| --- | --- |
| [Direct assessment](fixtures/requests.md#direct-assessment) | Assess a local operation through its real caller, distinguish state/effect burden from the clear counterexample, and return bounded findings. |
| [Architect and Refactoring handoff](fixtures/requests.md#architect-and-refactoring-handoff) | Assess an ownership sketch through Architect, then use its settled assessment in a local Refactoring phase without duplicating it. |
| [Interrogate discovery handoff](fixtures/requests.md#interrogate-discovery-handoff) | Prepare an isolated Maintainability discovery assignment while retaining a prior finding with the lead. |

Record evidence using the retention rules in the shared execution contract. A small, revised-only sample does not establish general reliability, model diversity, adoption by a consuming project, or comparative improvement.
