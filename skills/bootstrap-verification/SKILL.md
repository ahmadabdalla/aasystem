---
name: bootstrap-verification
description: Establish project verification through discovery, a feature map, and a proved local procedure. Use when onboarding the toolbox to a project or when the affected behavior has no usable verification path.
disable-model-invocation: true
---

# Bootstrap verification

Before starting, read the [shared execution contract](../aasystem/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Leave the project with a procedure another agent can run, evidence of which paths work, and explicit coverage gaps. Adopt existing verification facilities before creating new ones. Installing instructions alone does not establish readiness.

## Discover before choosing the method

Identify the target project, existing instructions, intended setup scope, and available environment. Reuse the settled brief. State consequential assumptions; investigate observable unknowns. Ask one focused question only for a material preference or constraint that cannot reasonably be assumed, then wait.

Start with a bounded survey across documentation, executable entry points, tests, configuration, and automation. Reconcile these sources: documentation can omit working paths, and tests can preserve incorrect behavior. Identify:

- Actors, user outcomes, alternate entry points, and background or integration paths.
- State ownership, persistence, dependencies, and access boundaries that affect those outcomes.
- Existing launch commands, driving tools, fixtures, assertions, and CI checks.
- Existing glossary and ADR locations, their relevant terms and decisions, and the authority behind intended outcomes. Link applicable records from feature expectations; setup alone does not require creating new records.
- What was inspected, conflicting evidence, inaccessible areas, and areas not inspected.

Use [how](../how/SKILL.md) to trace relevant paths, [why](../why/SKILL.md) when a historical constraint affects the procedure, and [probe](../probe/SKILL.md) for a consequential observable unknown. Follow critical and task-relevant paths deeply; record why that scope was selected. Do not treat a sample as an exhaustive inventory.

Separate intended behavior and its authority from current observations. When they disagree, retain both and identify the unresolved contract or defect. A proposed requirement remains proposed until grounded in the user's request or another authoritative contract.

## Adopt or build the project procedure

Read [the project contract](references/project-contract.md) before writing outputs. Extend an existing verifier in its established location when it can serve the project. Otherwise use the host's project skill convention; `.agents/skills/verify-<project>/` is the default. Keep commands, recipes, and evidence locations local to the project. The generated skill must work without this authoring conversation or the portable toolbox installed.

For a new map, create `features/README.md` inside the project verifier and one file per identified user-facing feature. Read [the feature-map example](references/feature-map-example/README.md) for the index and recipe shape; the project contract defines their contents. Preserve an established equivalent map instead of creating a second one. Link the map from the generated verifier and write detailed recipes for the selected scope, recording the remaining gaps. Reuse existing tests and tools by reference; add helpers only where they provide a missing repeatable operation or check. Keep reusable source findings with the procedure and temporary tracing with task evidence.

Establish build identity, readiness checks, isolated data, observation, reset, and cleanup before driving the app. Generate project-local evidence locations and retention instructions using the contract's [evidence lifecycle](references/project-contract.md#evidence-and-retention). Follow the project's actual permission and environment limits. Repair scoped setup or harness faults; record unrelated product defects. If required access or infrastructure is unavailable, preserve discovery and mark the affected procedure partial or blocked.

For a greenfield project, map proposed behavior as planned. Prove the first runnable slice when it exists; do not invent commands, observed coverage, or a successful setup for an app that cannot yet run.

## Prove and connect

Run every distinct procedure advertised as usable: launch, check the instance and build, drive a selected real path, inspect the result and relevant side effects, retain evidence, and clean up. Recheck health or reset after a surprising result. Cleanup targets only resources the run owns, including failed attempts, and preserves evidence. Confirm that evidence exists after cleanup.

Record the sampled feature and entry point for a shared procedure. Unexercised features stay unverified. A procedure can be usable while exposing a product failure; distinguish verifier readiness from behavior passing. Report readiness per surface, together with checks performed, failures, and remaining prerequisites. Stop widening the run when the agreed scope is established and the gaps are recorded.

Connect ordinary project work using [the project instruction guidance](references/project-instructions.md). Reuse existing routing or add a narrow entry in the project's established instruction file; preserve other instructions. Point to the actual local verifier and feature map. Suitable executable checks may use existing CI conventions when that integration is in scope; prose routing alone is not mechanical enforcement.

Return links to the discovery/map, local verifier, demonstrated readiness, and remaining gaps to the calling owner. Architect incorporates them into its design package; an aasystem playbook uses them for its reproduction, baseline, or acceptance checks. A setup run exposing a product defect supplies evidence to that owner and does not silently redefine the expected result. Use [maintain-verification](../maintain-verification/SKILL.md) for subsequent drift; no recurring schedule is implied.
