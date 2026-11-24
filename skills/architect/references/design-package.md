# Design package

What Architect hands over for implementation and independent verification. Use the project's format, not these headings.

- **Problem:** the intended behaviour, accepted decisions and non-goals, each with its source.
- **Caller usage:** realistic calls, including existing callers the change alters.
- **Shape:** data, signatures, state ownership, invariants and how each is enforced, and the main flow.
- **Rationale:** why this shape beats the simplest one that works, and what you rejected.
- **Verification plan:** one line per requirement the change adds or alters:

  ```text
  requirement → input → expected result (from the contract, not the design) → entry point → verifier recipe, or "none" → evidence
  ```

  Link the project verifier and the feature-map entries the change affects; if the project has none, say so. If business state changes, add the rejection, concurrency, replay and recovery cases from [Business state](business-state.md#carry-the-proof). Name what stays unverified.
- **Open risks:** unsettled questions with their owner, and the first implementation step.

If the change is user-facing, link the [interaction handoff](../../interaction-design/references/interaction-contract.md#5-record-and-hand-off).

Keep the package in the task record unless the caller names a file. A link only in your reply doesn't count.

An [Arena](../../arena/SKILL.md) candidate writes one package. It doesn't build or start its own comparison.
