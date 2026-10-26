# Engineering verification

Use for [independent implementation verification](execution.md#independent-implementation-verification). One fresh noneditor can assess related domains and run the checks; no standing review pool is required. The narrow [owner-presentation exception](execution.md#owner-presentation-eligibility) remains owner-checked.

## Assign

Give the verifier the authorised expectations, constraints, combined artifact and baseline/diff, tested input scope, relevant project recipes, owned fixture/resources, evidence destination and access limits. Select criteria for the affected work:

- Apply [local-code criteria](../../maintainability/references/local-code.md) to changed production code.
- Add [boundary criteria](../../maintainability/references/boundaries.md) when interfaces, dependencies, or invariant ownership are affected.
- For business-state changes, include the accepted identity, ownership, consistency, and failure guarantees and required cases from the design handoff. Read [Business state and consistency](../../architect/references/business-state.md) when interpreting or checking that coverage needs its procedure.

Reuse criteria already in context. These are inputs to the same verifier, not additional specialist assignments or a requirement to load upstream manuals.

Follow [review context](execution.md#review-context): independent discovery starts without lead conclusions or development pass claims; confirmation audits may receive claims. Preserve original findings and disclose context/isolation limits. Give the assignment a practical work/time bound and a specific return requirement.

## Assess and exercise

Inspect the actual diff for authorised scope, concrete defects and maintainability risks. Run the affected project checks against the identified artifact through the [local execution procedure](verification-contract.md#local-execution). Exercise the reported surface and relevant side effects; a unit test alone does not prove an unexercised API or UI path.

Derive affected checks from the authorised contract and actual changes as well as the design handoff. Exercise rejection, competing writes, replay, partial failure, or recovery where they threaten those guarantees; passing existing tests does not cover a missing case. Keep structural findings separate from observed contract failures.

Assess concrete gaps in changed-behaviour coverage; use targeted mutation checks or specialist review only for a named risk. Confirm the supplied owner, rules and checks are reachable from the project's normal entry point; report unrelated gaps separately without starting a wider audit.

For decisions assessed with [10x](../../10x/SKILL.md), exercise the required growth checks from the design handoff and report the actual volumes, rates or concurrency tested. Keep deferred targets separate from acceptance requirements; missing required proof remains a gap.

Do not change product code or expectations while verifying. Return harness faults for bounded repair and leave blocked observations unverified. Record actual commands, observed results, tested identity, findings, evidence and limitations. Keep qualitative review distinct from executable outcomes; no universal report schema is required.

## Correct and deliver

The owner inspects original findings and the work. Follow the [working loop](verification-contract.md#working-loop) for correction scope, proof reuse and stopping limits; required rechecks remain independent. A targeted confirmation may use the original verifier with disclosed earlier context; new independent discovery uses a fresh context.

Return missing or stale project recipes to the owner for scoped [verification maintenance](../../maintain-verification/SKILL.md), then re-exercise the affected path after repair. Preserve intended expectations and record unavailable required checks as gaps; an unchanged recipe needs no permanent edit.

Confirm that final source identity still matches the tested inputs and that owned resources are stopped, removed or deliberately retained. Missing, failing or inconclusive required checks block a completion claim. Return a concise result and evidence for human review; do not substitute the agent's completion decision for human approval.
