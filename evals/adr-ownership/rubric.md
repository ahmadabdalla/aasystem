# Judge-only rubric

Keep this file out of candidate contexts. Score each applicable criterion `2` (demonstrated), `1` (partial), `0` (contradicted or omitted despite adequate input), or `U` (unobservable). Cite actual records, links and available execution evidence. Evaluate each neutral variant before comparing; do not award an improvement from wording alone.

| Criterion | Observable success |
| --- | --- |
| A. Ownership and scope | Classifies the actual commitment by product/design/software rationale separately from system/context scope; technology names do not decide ownership. |
| B. Proportional retention | Applies all three upstream criteria, keeps records concise and avoids ADRs/folders for routine reversible details. |
| C. One canonical decision | Reuses an existing decision, separates genuinely independent choices, and cross-links rather than copying rationale into dimension-specific duplicates. Updates evidence without accumulating another decision; preserves history and supersedes only for an accepted replacement. |
| D. Project conventions and discovery | Preserves established paths, directory-local numbering and lazy creation; uses project-relative pointers and working links so relevant decisions can be found. |
| E. Authority and evidence | Uses retrievable scoped source authority; preserves proposal versus confirmed/delegated choice and keeps design/implementation observations separate. |
| F. Reachable procedure | Uses the assigned entry point and relevant reference with observed read/action evidence; distinguishes manual reading from native host invocation. Candidate claims alone receive `U`. |

Criteria A–F apply to the four ownership cases. For conformance, use the five checks below plus F; ownership and maintenance can be assessed where the task exercises them. `F` can remain unobservable when host traces are unavailable. Do not count `U` as a pass. A small sample using one model does not establish general reliability or model diversity.

## Conformance checks

| Check | Observable success |
| --- | --- |
| G. Rule selection | Chooses documented scoped rules, then established scoped practice, then the framework default; names the source and does not import an unadopted template. |
| H. Authoring | Alpha's new ADR contains the problem, queue choice and intended result, reason, rejected in-memory alternative, costs/limitations and proposed standing with the design-note source; updates the existing index without claiming acceptance or delivery. |
| I. Content review | Accepts complete records under their selected rules; identifies missing required information and cites the selected rule. |
| J. Claim review | Checks supplied claims rather than repeating them; rejects invented headings, default requirements imposed on another convention and unadopted template requirements. |
| K. Conflicts | Identifies contradictory project rules and leaves conformance undecided when no precedence is specified. |

For the framework-default variant, Alpha 0001 passes and 0002 fails for a missing rejected alternative; Beta 0002 and Gamma 0003 pass under their respective table/card conventions. Delta 0002 fails for missing expected effects under its documented rules, which take precedence over the older card. Epsilon 0001 passes; its downloaded template has not been adopted. Zeta remains undecided. All three supplied failure claims are rejected. Alpha's new ADR should be 0003 and remain proposed.

For an earlier instruction variant, distinguish adherence to that variant from coverage of the proposed contract. For example, the original default made alternatives optional, so accepting Alpha 0002 is baseline behavior, not failure to obey the original instructions. Score outputs against the same desired outcomes when comparing coverage; record this difference instead of manufacturing a baseline defect.

## Case expectations

- **dimension-project:** Reuse product ADR 0002, never create a second service-selection ADR. Record the consequential design change at the next design number (0005) and server-adapter choice at the next software number (0008), retaining each decision's actual scope and linking product constraints. Use one existing index. Do not create a software-owned service-choice record solely because Web3Forms is named. Confirmation does not prove delivery.
- **shared-decision:** One new system-wide software ADR 0013 contains the indivisible customer-identity contract and cross-context consequences. Product/design consequences do not justify copies. Button spacing stays in the task outcome; no dimension directories. Update the existing pointer. No implementation pass can be inferred from the accepted decision.
- **context-decision:** The non-reversible refund-window product rule and non-obvious integer-money software choice are independent accepted/delegated decisions in `src/returns/docs/adr/`, numbered 0004 and 0005 in either sensible order. Do not create system ADRs or dimension folders. Link the context pointer and sources; detailed implementation shape can qualify without expanding to an implementation plan. Automated approvals remain an unresolved proposal, not an accepted choice or successor to the manual rule.
- **accumulated-record:** Keep 0006 as the current manual-assessment product decision, adding relevant evidence without changing its choice. Extract the independently consequential queue design and prior email architecture into separate concise records using the existing sequence. The design stays accepted; the former software choice becomes superseded only by the review's accepted durable-outbox replacement, linked both ways with changed evidence and old rationale intact. Extraction alone does not supersede product or design. Preserve original dated authority, trace the extraction, update the existing index/handoff and keep implementation scenarios in the work record. Self-service remains an unresolved proposal; column spacing remains routine. Numbering order can vary; no new taxonomy, duplicate canonical rationale or acceptance from observed incidents.
