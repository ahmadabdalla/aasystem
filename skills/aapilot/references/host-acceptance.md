# Host acceptance contract

Read this only when implementing, assessing or claiming host-enforced verification or acceptance. It defines portable requirements each host integration must demonstrate; it does not ship an integration. Skill instructions and local receipts alone do not enforce them.

## Register authority and artifact

The host registers governing requirements, required assessments and decision authority before assessed work proceeds. Reject unauthorized weakening or removal of obligations, including through changed configuration or a replacement run. Preserve existing history and unresolved gates when a linked new run is required.

Bind the work and every result to the exact artifact, governing inputs, verifier/configuration and environment identity. Reuse the existing [brief, snapshot and receipt formats](verification-contract.md); a commit name or owner declaration alone is insufficient.

## Obtain independent evidence

Apply the [domain assessment and delegation rules](execution.md#delegation), [review-context rules](execution.md#review-context) and relevant specialist procedures. For retained production engineering, apply [engineering verification](engineering-verification.md).

The host launches a verifier separate from every producer of the assessed work and directly captures its actual identity, original findings and execution results. The verifier cannot change the assessed work or expectations; execution uses a separate workspace under the existing [input identity rules](verification-contract.md#input-identity-and-limits).

Protect authoritative state, captured results and credentials from the owner's effective write access. The same protection must cover the integration and configuration governing launch, capture and acceptance; an owner-editable enforcement path cannot establish this guarantee.

## Gate acceptance at the consumer

Reuse the current [proof, checkpoint and acceptance gates](verification-contract.md#events-and-reports). Missing, failing or inconclusive required proof blocks acceptance. An owner disposition cannot turn a failed result into a pass. Corrections require current affected verification.

Authenticate any mandatory human response and bind it to the exact pending question, artifact and authority. Preserve [human decision authority](execution.md#decision-authority); matching receipt fields alone cannot supply that response.

Keep eligible [owner-presentation proof](execution.md#owner-presentation-eligibility) labeled owner-checked; it never establishes independence.

Require an explicit owner acceptance request and satisfied gates, binding acceptance to the exact artifact. The actual consumer of the accepted work must reject forged, missing, substituted or stale results. A local owner receipt cannot substitute for the host's authoritative result.

## Demonstrate the integration

Exercise the actual host permissions, result channel and acceptance consumer together, retaining observed results for:

- Fabricated results or verifier identities, unauthorized state edits and substituted local receipts.
- Weakened or removed obligations, replacement-run bypass and stale or substituted source.
- Failed or unavailable verifiers, missing or inconclusive required proof and pending mandatory human approval.
- Owner-presentation labeling and attempts to present owner checks as independent proof.
- Genuine success with current independent evidence, required human responses and an explicit acceptance request for the exact artifact.

Structural helper rejection alone does not demonstrate these boundaries. Report the exercised host, configuration, artifact and evidence; disclose unsupported or unexercised guarantees. Success in one host does not establish another host's enforcement.
