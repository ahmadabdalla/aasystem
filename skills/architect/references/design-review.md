# Review a design sketch

Evaluate these design questions against the project's constraints. Use the answers to compare concrete consequences and tradeoffs.

- **Caller burden:** Does the interface hide useful complexity, or must callers coordinate internal stages? Compare what each candidate makes callers know, not just API size.
- **Knowledge and ownership:** Which representation or policy decisions cross module boundaries? Would one change require coordinated edits? Does decomposition follow owned knowledge or merely execution order?
- **Meaningful boundaries:** Do forwarding methods add policy, adaptation, or a stable contract? Are internals accidentally becoming public dependencies?
- **Data and state:** Trace the dominant access patterns. Name each state owner and examine concurrent writers, retries, and partial failure where applicable. Check claims of idempotence through observable effects.
- **Invariants:** What enforces each invariant: a type, runtime boundary, test, or convention? Are authoritative values derived or manually synchronized?
- **Change cost:** Can a contributor make the intended change locally without breaking unseen consumers? Evaluate compatibility and migration requirements explicitly.
- **Proof:** Can the proposed interface be exercised through real callers with an independent expected outcome? Can a failing check distinguish a design error from a broken observation method?

For each material concern, show the causal path and likely consequence. An adapter, migration path, shared writer, or stage boundary can be justified by the actual contract. Do not import fixed file-count limits, unconditional deletion, or a universal preference for smaller APIs.
