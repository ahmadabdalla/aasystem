# Local code

Evaluate the effort needed to follow the actual code and make the intended change. Tie each concern to a reader task, change, or observable consequence.

- **Intent:** Do names and data shapes reveal domain meaning, units, and effects, or must a reader reconstruct them from usage? Prefer existing project terminology; a new abstraction name needs a meaning beyond its mechanics.
- **Responsibilities and flow:** Can a reader follow the main operation, decisions, and failure paths without tracking unrelated work? Extraction helps when it names a meaningful operation or isolates a responsibility; moving a few lines behind another name can add a hop without removing mental work.
- **Failure meaning:** Can callers distinguish expected absence, invalid input, dependency failure, and a broken invariant where the contract requires it? Check that handling preserves useful context, exposes partial effects, and does not turn a failure into apparent success. Follow the language and project error conventions; exceptions, result values, and optional values each need a concrete contract.
- **Effects and state:** Are writes, dependency calls, and order-sensitive behavior visible where they matter? Trace mutation and lifetime across helpers; use the [boundary criteria](boundaries.md) when ownership or invariant enforcement is at issue.
- **Duplication:** Does repeated code represent one rule that must change together, or independent cases that happen to look alike? Compare synchronization cost with the coupling and branching introduced by sharing it.
- **Explanations:** Do comments and adjacent documentation preserve rationale, contracts, or constraints a reader cannot recover from the code? Flag a misleading or stale explanation with its consequence; deleting a comment or extracting a helper is useful only when the needed meaning survives.
- **Verification clarity:** Can a test name and its inputs explain the behavior, with an expectation derived from the contract? Check whether assertions observe useful results or mirror private steps, and whether a failure helps locate the broken rule.

Use the project's constraints to resolve competing concerns. Function length, nesting, comments, or exception use alone do not establish a defect. Prefer a recommendation whose reduction in reader effort or change risk can be explained concretely.
