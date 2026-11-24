---
name: maintain-verification
description: Audit and repair a project's verifier and feature map against its source and live behaviour.
disable-model-invocation: true
---

# Maintain verification

Before starting, read the [execution contract](../pilot/references/execution.md), the [approved-principle index](../principles/INDEX.md) and [the project contract](../bootstrap-verification/references/project-contract.md), unless already in context.

You bring a project's verifier and feature map back in line with the project. If there's no verifier, use [Bootstrap Verification](../bootstrap-verification/SKILL.md) instead.

## Rules

- **Never change an expected result to make a check pass.** Expected results come from a requirement, a published contract, an accepted decision, the task or the user. Changed code and commit messages aren't authority.
- **Only a live run proves coverage.** Reading the code or an old pass doesn't count.
- **Edit only the verifier, its helpers and map, and the instruction entry that points to it.** Report product defects; fix product code only if the task includes it.

## Steps

1. **Scope.** Say whether this is task-scoped (the change and what depends on it) or a full audit (every mapped feature, plus a search for unmapped entry points).
2. **Compare.** Check the map's entry points against the code, docs, tests and recent changes. Trace unclear flows with [How](../how/SKILL.md).
3. **Run** every in-scope feature through the verifier. If the harness crashes, fix the crash first so every check reports.
4. **Classify** each finding:
   - Authorised change: update the expectation, cite the authority, rerun.
   - Unauthorised change: keep the old expectation on its old entry point, check the new behaviour only as characterization, and ask the user.
   - Drift that changes no behaviour, such as a moved script or dead link: fix it and rerun.
   - New entry point: add it to the map. Write its recipe if it's in scope; otherwise list a gap.
   - The product breaks an expectation: recheck the build and fixture, then report a regression.
   - The check can't drive a product that works: fix how it drives, never what it expects.
   - Missing access: record the prerequisite and what stays unverified.
5. **Report** results as the contract's [Readiness](../bootstrap-verification/references/project-contract.md#readiness) section describes. Call a full audit clean only when coverage is complete and nothing failed.

Done when every in-scope feature has run or is listed as unverified, every repair is rerun, and `features/README.md` matches the feature files.
