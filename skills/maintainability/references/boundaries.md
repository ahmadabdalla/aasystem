# Boundaries

Evaluate these questions against the project's constraints. Compare concrete consequences and tradeoffs for the supplied code or design.

- **Caller burden:** Does the interface hide useful complexity, or must callers coordinate internal stages? Compare what each shape makes callers know, not just API size.
- **Knowledge and ownership:** Which representation or policy decisions cross module boundaries? Would one change require coordinated edits? Does decomposition follow owned knowledge or merely execution order?
- **Meaningful boundaries:** Do forwarding methods add policy, adaptation, or a stable contract? Are internals accidentally becoming public dependencies? Compare hidden complexity with the indirection the boundary adds.
- **Data and state:** Trace the dominant access patterns. Name each state owner and examine concurrent writers, retries, and partial failure where applicable. Check claims of idempotence through observable effects.
- **Invariants:** What enforces each invariant: a type, runtime boundary, test, or convention? Are authoritative values derived or manually synchronized?
- **Change locality:** Can a contributor make the intended change locally without breaking unseen consumers? Evaluate compatibility and migration requirements explicitly, including the cost of moving responsibility.
- **Verification:** Can the interface be exercised through real callers with an independent expected outcome? Can a failing check distinguish a design error from a broken observation method? Assess whether dependencies can be controlled without replacing the behavior under test.

For each material concern, show the causal path and likely consequence. An adapter, migration path, shared writer, or stage boundary can be justified by the actual contract. Do not import fixed file-count limits, unconditional deletion, or a universal preference for smaller APIs.
