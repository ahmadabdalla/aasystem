---
name: tdd
description: Prove a bug with a test that fails before the fix and passes after. Use when the user asks for a test-first fix, or when Pilot's Bug fix playbook finds a cheap local test.
user-invocable: false
---

# TDD

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

If a Bug fix run called you, use its cause and don't diagnose again; it says whether you also fix. If the user asked only for a check, stop at the check. Otherwise invoke the [`pilot`](../pilot/SKILL.md) skill and make the fix through its [Bug fix](../pilot/playbooks/bug-fix.md) playbook.

1. **Pick the check.** Test the path the bug takes, through a public interface.
2. **Watch it fail.** Write the expected value as a literal from the bug report or spec, never computed the way the code does. Run the test before the fix. It must fail on that assertion, showing the reported wrong result. If it passes, it misses the bug: go back to step 1.
3. **Fix, or stop.** If you don't make the fix, don't edit product code. If you do, invoke the [`implement`](../implement/SKILL.md) skill to make the smallest fix, then rerun the test and the nearby tests. Never weaken an existing assertion to make them pass.

If the bug depends on time or randomness, pin the clock or seed in a new test. Leave the existing flaky test as it is. One green rerun proves nothing.

If a test would need new infrastructure, mocks of your own modules, or data only production has, don't build it. Use the closest check you can run, such as a repro script timed at two or more data sizes. A time limit or call-count spy is not a failing-before test; keep it out of the suite. Say plainly there's no failing-before test.

Reply with the cause and which inputs it gets wrong, the test, the command and the failing output, plus the passing output and nearby tests if you made the fix. Say what's unproven.
