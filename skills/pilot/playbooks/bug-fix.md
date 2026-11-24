# Bug fix

Keep only changes that fix the confirmed cause, plus diagnostics worth keeping on their own. Undo the rest, including failed experiments.

1. **Reproduce it.** Before changing product code, record the expected behaviour, trigger, actual failure, environment and revision. Reproduce it on the affected surface yourself.
   - If it doesn't reproduce, tighten the conditions, build a representative trigger or add instrumentation. Report a stand-in as a stand-in.
   - If you can't reach the action, record what blocks you and what you tried, then ask the user to do it and wait.

   Done when you've seen it fail there, or recorded why you can't.

2. **Find the cause.** Trace the path with [How](../../how/SKILL.md). If it worked before, find what changed with [Why](../../why/SKILL.md). Name the candidate causes, then pick observations that rule them out. If state is unclear, use [Probe](../../probe/SKILL.md) and runtime instrumentation. If the evidence isn't enough, stop and report the diagnosis as unresolved, with the next observation that would settle it. Done when runtime evidence confirms one cause. Design or fix nothing before that.

3. **Fix it.**
   - If the fix meets the [Architect design trigger](../../architect/SKILL.md#design-trigger), give Architect the confirmed cause first.
   - If a regression test is cheap and local, or the user asked for tests, write the failing test first with [TDD](../../tdd/SKILL.md). Agree who owns the test and whether they also own the fix.
   - Make the fix with [Implement](../../implement/SKILL.md).

4. **Replay the failure.** However small the fix, an agent that edited none of it must replay the same surface, trigger and conditions on the fixed code. Brief it as [independent verification](../references/verification-contract.md#independent-implementation-verification) describes. It checks the original result, side effects, the regression test if any, and nearby paths the fix affects. Your own test run doesn't count. Wrong-surface or inconclusive evidence isn't a pass. A unit test doesn't prove the integration bug is gone.

5. **Deliver.** If commits are in scope, commit the failing reproduction before the fix unless the project forbids it. Report the confirmed cause, or what's still uncertain, with short failing and passing output or links, without secrets.
