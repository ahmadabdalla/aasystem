# Execution contract

**Baseline.** Read this contract, the [principle index](../../principles/INDEX.md), relevant principle leaves and project instructions. Reuse settled context. These rules guide agents; they do not grant tool permissions or provide a sandbox.

## Ownership and handoffs

One owner carries the request through the agreed delivery boundary. Keep the outcome, constraints, agreed decisions, open questions, expected results and evidence in the existing task brief; conversation can suffice. Specialists contribute to that task rather than starting another coordinator.

Each assignment needs accessible inputs, a bounded deliverable, write ownership, relevant constraints and checks, and what to return. Workers preserve others' edits and project formats, and return out-of-scope findings to the owner. Keep decision context retrievable under the [handoff principle](../../principle-preserve-decision-context/SKILL.md).

## Scope and proof

Replay a new or materially changed request: what to achieve, what must remain true, uncertainties and next action. A clear authorised request proceeds; replay is not an approval ceremony. Respect research-only, design-only and other explicit stopping points.

Inspect observable unknowns before depending on them. Reuse project requirements, accepted decisions and verification procedures. Distinguish sourced facts, proposals, human agreements and observations. A design proposal is not permission to build; model agreement is not evidence of correctness.

Match proof to the task. Research needs sources and limits; design needs rationale and an inspectable proposal; implementation needs observed behaviour. An unavailable prerequisite leaves the affected result unverified. Use the [verification contract](verification-contract.md) for retained implementation.

## Decision authority

Routine details within settled scope proceed. An unresolved choice changing product meaning, architecture, trust boundaries, permissions, external effects or required visual review returns to the human before dependent work. Check existing authority first; do not repeatedly ask for settled permission.

At a checkpoint, show the concrete proposal or result, what was checked and remains uncertain, the decision needed and the next action after it. Provide a usable visual preview when the decision is visual. Ask a focused question, then stop the whole process and wait. Record the actual answer with the decision; neither an agent's recommendation nor its inspection supplies human approval.

## Delegation

The owner may do the work or delegate for useful expertise, independent ready work or context separation. A skill is a procedure, not a requirement to launch another agent. Check actual tools, permissions and capacity; use configured models without inventing diversity.

For parallel work, give workers separate write ownership and identify shared resources. Use [Swarm](../../swarm/SKILL.md) for partitioned coverage and [Arena](../../arena/SKILL.md) for competing approaches when their evidence can change an unresolved choice. Preserve required independent candidates, judging and verification. Keep coupled work with one owner.

Inspect returned artifacts and observations against the assignment before relying on them. Resolve contradictions, stale inputs and material findings. A worker's return is not automatic acceptance. Unavailable required delegation must be disclosed; owner checks cannot be relabelled independent.

## Review context

Initial implementation verification defaults to independent discovery; correction rechecks may use confirmation audits.

Start required independent reviewers separately from every producer, without inherited discussion when the host permits. Give requirements, accepted constraints, original artifacts, source identity, relevant criteria and runnable procedures. For independent discovery, withhold prior conclusions until initial findings return. A confirmation audit may receive claims and sources; label it accordingly.

Preserve original findings before editing summaries or sharing other assessments. Disclose inherited context, exposure to earlier conclusions and other isolation limits. A different agent or model alone does not establish independent discovery.

## Verification through the project

Find the project verifier and affected feature recipes before changing behaviour. Use [Bootstrap Verification](../../bootstrap-verification/SKILL.md) for a missing usable path and [Maintain Verification](../../maintain-verification/SKILL.md) for recipe drift, within the authorised setup scope.

Derive expected results from the request or contract. Exercise the relevant UI, API, CLI or library entry point and inspect consequential effects. Check instance identity, readiness and fixture reset before interpreting surprising results. Builds, mocks and worker summaries prove only the boundaries they exercise. Never change an expectation merely to hide a failure.

Use the [local execution and evidence rules](verification-contract.md#local-execution) for working directories, tested identity and cleanup. Preserve failing-before evidence for bug fixes and baseline observations for refactoring. Update affected recipes; an unchanged run needs no permanent map edit.

## Owner-presentation eligibility

An exact prescribed, low-impact presentation edit may be made and checked by the owner when meaning, behaviour, data, contracts, permissions, dependencies and deployment remain unchanged and decisions are settled. This cannot waive independent review required by the user or project. A billing or consent wording change does not qualify merely because it is short.

State the eligibility basis, inspect the final diff and available preview, and report this as owner-checked. If broader effects appear, obtain the required independent verification or report the gap. No separate coordinator or full feature checklist is needed.

## Independent implementation verification

Other retained implementation requires a fresh verifier separate from every editor to assess the combined diff and execute affected checks. Read [Engineering Verification](engineering-verification.md) for the assignment and correction loop. Development checks do not replace this assessment. [Interrogate](../../interrogate/SKILL.md) supplies adversarial review, not executable proof.

## Completion

Before delivery, reconcile material findings and decisions, check the final artifact against current evidence, update affected project records and resolve owned resources. Report what changed, actual checks and outcomes, unverified scope, evidence location and anything deliberately retained. Follow the [evidence lifetime](../../bootstrap-verification/references/project-contract.md#evidence-and-retention); retain bulky artifacts only for an identified need.

For substantial or unattended work, keep consequential decisions and their evidence with the existing task record; use [Show Me Your Work](../../show-me-your-work/SKILL.md) when a later reader needs that trail. Do not create parallel logs or routine action transcripts.

## Bounded autonomy

Before unattended work, establish scope, permitted effects, required evidence, practical work/time limits and stopping conditions. Honour actual user and host limits across retries; do not restart a task to evade them. A duration such as overnight grants no extra authority or session-survival capability.

Stop for required human decisions, exhausted limits, unavailable mandatory proof or uncertain external effects. After interruption, inspect actual owned work before retrying; cancelling an agent does not prove its processes stopped. Resolve uncertainty before overlapping work or claiming completion. Report completed work and the precise remaining prerequisite.

## Delivery

Respect the requested boundary. Local edits, commits, PRs, merging and release are separate actions. Leave uncommitted work available when human review is requested. Use [Opening a PR](../playbooks/opening-a-pr.md) when authorised. Read-only work ends with its answer.
