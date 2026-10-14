---
name: interrogate
description: Challenge a proposal, design, implementation, or recommendation with adversarial review and evidence. Use to find consequential failure modes, unsupported assumptions, and errors in the framing.
disable-model-invocation: true
---

# Interrogate

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Establish scope and intent, gather adversarial findings, synthesize them, and apply lead judgment. Challenge both the proposal and its framing.

## Prepare and challenge

Identify the actual artifact or diff, surrounding system, intended outcome, constraints, and review criteria. Select the assignment mode and prepare inputs under the [shared review-context rule](../aapilot/references/execution.md#review-context). Reuse the caller's brief after applying the selected review mode's inclusion and exclusion rules; surface only consequential gaps or changed assumptions. Resolve missing intent that would materially change the review before proceeding; ask one question and wait when necessary.

When delegation is available and permitted, run isolated reviewers with the same evidence, artifact, and rubric without each other's findings. Use multiple actual model families when available; different personas do not supply that diversity. Disclose the reviewer setup, unavailable seats, and limitations. Without isolated reviewers, perform a single-agent adversarial review; repeated passes or role labels do not create independence. A required independent gate remains incomplete when only self-review was possible.

Review relevant correctness, boundaries, data ownership, failure paths, verification coverage, and cost. Also inspect frame errors: an untested premise shared by all options, a missing alternative, or a proposed means mistaken for the user's outcome. Respect explicit constraints and identify conflicts instead of silently redefining the goal.

For code or implementation-design assignments where reader burden or change cost matters, give the relevant existing reviewer a bounded [maintainability](../maintainability/SKILL.md) assignment and accessible criterion references. Keep it within the same review setup and selected context mode; do not create a second reviewer pool or supply prior assessments to independent discovery. Respect its explicit invocation policy and disclose an unavailable handoff. The supporting assessment returns findings; Interrogate retains adversarial synthesis and the verdict.

Require a concrete location, condition or execution path, consequence, supporting evidence, and what would resolve uncertainty for each finding. Distinguish a demonstrated issue, an unresolved risk, and a preference. An empty review is valid.

## Apply lead judgment

State the assignment mode and isolation limits in the verdict. Keep initial discovery findings distinguishable from subsequent checks of supplied claims.

Read and deduplicate all findings, retaining disagreements and consequential findings raised by only one reviewer. Check material claims in the actual artifact, call path, source, or [probe](../probe/SKILL.md). Reviewer agreement is a signal to inspect, not proof.

Classify findings as **act on**, **consider**, **noted**, or **dismissed**, with the evidence and reason. Separate inability to verify from a verified defect. Report unresolved risks and the smallest corrective action or experiment. Return the verdict to the calling workflow for incorporation into its decision or design package; present it to the user when invoked directly. Review alone produces a verdict. The calling owner decides and applies fixes within the task's authorization, then reruns affected proof. Apply fixes within this skill only when its explicit assignment includes remediation; keep the review findings and subsequent changes distinguishable.
