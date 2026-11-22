---
name: tdd
description: Establish a focused failing-before regression check and verify it after a correction. Use when explicitly requested or when a bug has a clear cheap local test path; avoid unrelated harness construction for an impractical test.
disable-model-invocation: true
---

# TDD

Before starting, read the [execution contract's baseline](../pilot/references/execution.md#baseline) and the sections it names for this task, and the [approved-principle index](../principles/INDEX.md), unless already in context. Follow the contract’s baseline requirements.

Make the intended behavior executable before the product edit. Preserve the surrounding workflow's reproduction and confirmed mechanism; do not restart diagnosis. When invoked directly with no calling workflow, establish the failing check, then hand the correction to [pilot](../pilot/SKILL.md)'s Bug fix playbook as fix owner.

1. Identify the intended result, current failure, affected public path, and smallest useful check. Prefer the existing test facility nearest the behavior. A unit test can pin the mechanism while the calling bug-fix workflow retains responsibility for the original user-facing reproduction.
2. Add a focused regression test expressing the contract independently of the implementation. Run it before the fix and confirm that it fails for the intended reason. A test that passes, fails to launch, or fails for an unrelated reason has not established the regression. Preserve the output and source identity.
3. Return the failing check, command, and evidence to the fix owner; do not edit product code. When the assignment also gives this worker the fix, make the smallest correction through [Implement](../implement/SKILL.md), rerun the regression test, and retain the ordered failing-before and passing-after runs.
4. Check affected nearby contracts and return the exact observations. Do not weaken assertions to fit an incorrect implementation. A genuine change to expected behavior needs its authority recorded.

If a useful new test requires broad infrastructure, brittle mocks, production-only state, or unrelated fixture churn, explain that constraint. Use the closest credible executable check, such as a reproduction command, focused script, browser interaction, or log assertion. Keep missing failing-before evidence explicit. An explicit request for a test remains unmet if no suitable check was established.

For flaky behavior, control the causal condition when possible and record remaining variability. Do not promote one successful rerun into proof that the reported intermittent failure is gone. Return evidence to the calling workflow for verification on the affected surface.
