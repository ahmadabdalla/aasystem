# Local code

Use when writing or reviewing code. Tie every finding to a reader task, a likely change or a consequence someone can observe. Length, nesting, comment count or exception use alone is not a finding.

- **Names:** Do names and data shapes say the domain meaning, units and effects? Use the project's terms. A new abstraction's name says what it means, not how it works.
- **Flow:** Can a reader follow the main path, its decisions and its failure paths without tracking unrelated work? Extract a helper only when it names a real operation. A helper that just moves lines adds a hop.
- **Failures:** Where the contract needs it, can callers tell expected absence, invalid input, dependency failure and a broken invariant apart? Handling keeps context, exposes partial effects and never turns a failure into success. Follow the project's error style.
- **Effects:** Are writes, dependency calls and order-sensitive steps visible where they happen? If ownership or invariant enforcement is in question, use [boundaries](boundaries.md).
- **Duplication:** Share code only when the copies are one rule that must change together. Code that looks alike but changes for different reasons stays separate.
- **Comments:** Comments keep the reasons, contracts and constraints the code can't show. Flag a stale or misleading comment with what it would mislead a reader into doing.
- **Verification clarity:** A needed test fails when its behaviour regresses, and only then. It doesn't exercise only framework or type guarantees, assert a mock it configured, repeat another test through the same entry point, or assert an absence no current contract requires. A needed test can still need a rewrite. Check:
  - The name and inputs say which behaviour it guards.
  - The expected value comes from the contract, not recomputed the way the code computes it.
  - Assertions check results callers see, not private steps.
  - It runs alone from its own setup, with time, randomness and shared state controlled.
