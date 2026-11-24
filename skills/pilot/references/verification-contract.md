# Verification contract

How to prove code you keep.

## Verification through the project

Before changing behaviour, find how the project verifies it: its verifier and the recipes for the feature you're touching. No usable way to verify? Use [Bootstrap Verification](../../bootstrap-verification/SKILL.md). Recipes out of date, or a verifier reports them missing or stale? Fix them with [Maintain Verification](../../maintain-verification/SKILL.md), then rerun the affected check.

Take expected results from the request or contract, not from the code. Test through the real entry point (UI, API, CLI or library call) and check what it actually did: stored data, outgoing calls and output. If a result surprises you, first check you're testing the right instance, that it's ready and that fixtures were reset. Never change an expected result to make a check pass.

For a bug fix, keep the failing run from before the fix. For a refactor, keep the baseline run. Update the recipes the change affects.

## Owner-presentation eligibility

The owner can make and check a small, exactly specified wording, styling or layout change alone. It qualifies only when meaning, behaviour, data, contracts, permissions, dependencies and deployment all stay the same and nothing is left to decide. Billing or consent wording doesn't qualify just because it's short. If a test's expected value has to change, it's behaviour, not presentation. It never overrides independent review the user or project asks for.

Say why it qualifies, check the final diff and any preview, and report it as **owner-checked**. If wider effects turn up, get independent verification or report the gap.

## Independent implementation verification

Every other change you keep needs a **fresh verifier**: an agent that edited none of it, checking the combined diff and running the affected checks. Read [Engineering Verification](engineering-verification.md) before briefing it. Your own development checks don't count. [Interrogate](../../interrogate/SKILL.md) gives adversarial review, not proof that the code works.

## Working loop

1. Before editing, map each required outcome to a check in the brief. Set one time limit for acceptance verification, covering diagnosis, repairs and rechecks, within the user's limits. Carry what's left across handoffs and retries.
2. Implement and run development checks.
3. Pause source edits and brief a fresh verifier as [Engineering Verification](engineering-verification.md#assign) describes.
4. Label each failure: product (fix the code), harness or environment (bounded repair; blocked observations stay unverified), unsettled expectation (ask the human) or unknown (diagnose before fixing). For each fix, name the failure, the inputs it changes and the checks it needs. Reuse earlier proof only if you can say why the fix doesn't affect it; if the fix touches shared code, config or schema, rerun the integration checks that depend on it. Any source edit after an independent pass goes back to step 3, including Interrogate or PR-review fixes and removed experiments.
5. Deliver as the execution contract's [finish check](execution.md#finish) describes.

If a failure comes back after a fix, stop rerunning and look for a shared cause or a wrong test assumption. Retry only with new evidence or a materially different hypothesis, and a check that tells them apart. If you hit the time limit, stop and report what's incomplete, the failures, the time used and what's needed to resume. Extend or reset the limit only if the human agrees.

## Local execution

The implementer and verifier take turns in one directory. Before verifying, stop every other source writer. If you can't tell whether something else is writing, the result is inconclusive. If you use a worktree or a copy, share databases, ports or services, or clean up after a run, read [local execution](local-execution.md) first.

## Tested identity

Record the inputs you checked: uncommitted and new files, the verifier and its configuration, and any ignored or external inputs it needs. For uncommitted work, a branch or HEAD commit isn't enough. Check identity before and after verification, and again at delivery. If relevant inputs changed, reverify; don't fall back to an older pass. `A matching hash shows only that the inputs you picked didn't change, not that the running instance uses them; check that too. If the project has no identity check, use the read-only [input identity helper](../scripts/input_identity.py); `--help` gives usage. Keep its output outside the checked inputs. If tests generate source, reset it before the first fingerprint.`

## Result and retention

Keep these in the project's existing result record (task, PR or evidence file): the request and its authority, expected outcomes, tested identity and environment, who verified, commands and results (pass, fail, unverified), material findings and what you did about each, and limits.

A missing, failing or inconclusive required check leaves the work incomplete. An owner's decision can't turn a failure into a pass. Show any accepted limitation and who accepted it. Keep findings and evidence through human review or investigation.
