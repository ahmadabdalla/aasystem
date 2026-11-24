---
name: implement
description: Make bounded production edits and run development checks against a supplied contract or settled design.
user-invocable: false
---

# Implement

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

The caller owns the design, acceptance and [independent verification](../pilot/references/verification-contract.md#independent-implementation-verification).

No brief? Make wording or styling changes yourself under [owner-presentation eligibility](../pilot/references/verification-contract.md#owner-presentation-eligibility). For anything else, call the Skill tool with "pilot" ([pilot](../pilot/SKILL.md)) before editing.

1. Read the brief and everything it links, and apply [Be ready to deliver and prove](../principle-deliver-and-prove/SKILL.md) to it. The brief should give:
   - the behaviour to build, the settled design with its named data structures, and any reviewed visual reference
   - which files you own
   - invariants, failure behaviour, compatibility and allowed effects
   - the checks to run and where evidence goes

   If the design or file ownership is missing or contradictory, ask the owner before editing.
2. Write code to Maintainability's [local-code criteria](../maintainability/references/local-code.md).
   - When you touch callers, shared code or invariants, also read its [boundary criteria](../maintainability/references/boundaries.md).
   - For UI, read Design Judge's [visual standards](../design-judge/references/visual-standards.md).
   - For refactors, read [Refactoring moves](references/refactoring-moves.md).
3. Edit in small units. After each unit, run the assigned checks: the failing reproduction for a fix, the baseline for a refactor. Never change an expected result to make a check pass.
4. Stay in scope. Report bugs and design problems you find to the owner, and send back changes to shared design tokens or files you don't own; don't make them yourself. Before returning, remove anything speculative, unrelated or left over from investigating.
5. Return:
   - the diff, and the commit or files it applies to
   - why you made each change, including tradeoffs you weighed
   - the checks you ran, their results and where the evidence is
   - anything unverified
   - for a refactor, any compatibility impact
   - what logging or monitoring the change adds or loses ([signal effects](../pilot/references/execution.md#signal-effects))

