---
name: tdd
description: Establish a focused failing-before regression check and verify it after a correction. Use when explicitly requested or when a bug has a clear cheap local test path; avoid unrelated harness construction for an impractical test.
disable-model-invocation: true
---

# TDD

Before starting, read the [shared execution contract](../aasystem/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Make the intended behavior executable before the product edit. Preserve the surrounding workflow's reproduction and confirmed mechanism; do not restart diagnosis.

1. Identify the intended result, current failure, affected public path, and smallest useful check. Prefer the existing test facility nearest the behavior. A unit test can pin the mechanism while the calling bug-fix workflow retains responsibility for the original user-facing reproduction.
2. Add a focused regression test expressing the contract independently of the implementation. Run it before the fix and confirm that it fails for the intended reason. A test that passes, fails to launch, or fails for an unrelated reason has not established the regression. Preserve the output and source identity.
3. Implement the smallest correction within the assigned scope and rerun the regression test. If called in a test-only role, return the failing check, command, and evidence to the fix owner; do not edit product code. If the same worker owns test and fix, retain the ordered failing-before and passing-after runs.
4. Check affected nearby contracts and return the exact observations. Do not weaken assertions to fit an incorrect implementation. A genuine change to expected behavior needs its authority recorded.

If a useful new test requires broad infrastructure, brittle mocks, production-only state, or unrelated fixture churn, explain that constraint. Use the closest credible executable check, such as a reproduction command, focused script, browser interaction, or log assertion. Keep missing failing-before evidence explicit. An explicit request for a test remains unmet if no suitable check was established.

For flaky behavior, control the causal condition when possible and record remaining variability. Do not promote one successful rerun into proof that the reported intermittent failure is gone. Return evidence to the calling workflow for verification on the affected surface.
