# Engineering verification

Use for [independent implementation verification](execution.md#independent-implementation-verification). One fresh noneditor can assess related domains and run the checks; no standing review pool is required. The narrow [owner-presentation exception](execution.md#owner-presentation-eligibility) remains owner-checked.

## Assign

Give the verifier the authorised expectations, constraints, combined artifact and baseline/diff, tested input scope, relevant project recipes, owned fixture/resources, evidence destination and access limits. Include [local-code](../../maintainability/references/local-code.md) criteria and [boundary](../../maintainability/references/boundaries.md) criteria when interfaces or invariant ownership are affected. Criteria consumption does not require another specialist.

Follow [review context](execution.md#review-context): independent discovery starts without lead conclusions or development pass claims; confirmation audits may receive claims. Preserve original findings and disclose context/isolation limits. Give the assignment a practical work/time bound and a specific return requirement.

## Assess and exercise

Inspect the actual diff for authorised scope, concrete defects and maintainability risks. Run the affected project checks against the identified artifact through the [local execution procedure](verification-contract.md#local-execution). Exercise the reported surface and relevant side effects; a unit test alone does not prove an unexercised API or UI path.

Do not change product code or expectations while verifying. Return harness faults for bounded repair and leave blocked observations unverified. Record actual commands, observed results, tested identity, findings, evidence and limitations. Keep qualitative review distinct from executable outcomes; no universal report schema is required.

## Correct and deliver

The owner inspects original findings and the work. Correct material defects within authority or obtain an explicit evidenced disposition; do not silently dismiss them. Repeat affected independent assessment and runtime checks after changes. A targeted confirmation may use the original verifier with disclosed earlier context; new independent discovery uses a fresh context.

Confirm that final source identity still matches the tested inputs and that owned resources are stopped, removed or deliberately retained. Missing, failing or inconclusive required checks block a completion claim. Return a concise result and evidence for human review; do not substitute the agent's completion decision for human approval.
