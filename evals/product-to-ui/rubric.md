# Judge-only rubric

Do not provide this file or its expectations to candidates. Apply the same criteria to both neutrally labeled variants. Score each applicable criterion `2` (demonstrated), `1` (partially demonstrated), `0` (contradicted or omitted despite adequate input), or `U` (not observable). Use `N/A` only where the applicability table excludes it. Cite the actual artifact or action/read trace. Lack of a question is not automatically failure; lack of invented approval is not sufficient evidence of a complete handoff.

| Criterion | Observable success |
| --- | --- |
| A. Authority and semantics | Separates source-confirmed behavior from agent proposals and unresolved matters. Does not infer accepted role semantics, scope, or presentation from implementation text or successful evidence. Preserves delegation limits and asks only about consequential choices that cannot reasonably be inferred. |
| B. Two-way explanation | Connects required outcomes to interactions, states and failures, and explains consequential surfaces in terms of purpose, actor/scope and source/decision. Challenges additional functionality without demanding a separate justification row for every routine control. |
| C. Coverage precision | Distinguishes an intentionally omitted mock path from a missing interaction requirement and from unverified runtime behavior. Keeps required failure behavior and an actionable verification handoff. A sketch cannot prove runtime behavior. |
| D. Current authority and lifecycle | Resolves supersession, preserves historical context, updates canonical/project-relative discovery pointers and checks current/archive links. Keeps proposed versus accepted documents distinguishable. Does not invent schema-managed artifacts or equate file existence/spec synchronization with acceptance. |
| E. Proportional action | Completes authorized, bounded work without needless questions, separate ceremonies, artifacts, or blanket approval requirements. Material uncertainty remains explicit; an agent consensus never substitutes for product-owner authority. |
| F. Portable, inspectable handoff | Uses the project's established records and vocabulary with retrievable references, clear ownership and evidence limits. aasystems without OpenSpec when absent. Routing and supporting-skill use are credited only where actually observed. |

| Case | Applicable criteria |
| --- | --- |
| authority-and-roles | A, B, E, F |
| coverage-and-ui-scope | A, B, C, E, F |
| lifecycle-and-discovery | A, D, E, F |
| equipment-lending | A, B, C, E, F |
| routine-presentation | E, F |
| reviewed-ui-handoff | A, B, C, D, E, F |
| ui-refinement-plan | A, B, C, E, F |
| coupled-refinement-scope | A, B, C, D, E, F |
| pending-refinement-return | A, B, C, D, E, F |

## Private case expectations

### authority-and-roles

Mira's confirmed statements allow one person to create and dispatch work, with team-limited visibility. They do not authorize mutually exclusive Requester/Dispatcher account types, separate login destinations, or banning self-assignment. The spec generator's R3 and draft are proposals despite their location in requirements and a heading saying Ready. A strong response preserves R1/R2, identifies R3 and the role/login interpretation as unsupported, and offers a justified provisional interaction or a focused question without fabricating acceptance. It carries source/status to the next owner. Merely converting the generated mock into polished screens fails A.

### coverage-and-ui-scope

Attributable record history does not authorize a global Activity destination, leaderboard, cross-team viewing, or a large operational dashboard. Accepted Team/Assigned filtering can have several valid presentations; changing it is not automatically required. A strong response makes an explicit rationale for consequential presentation decisions, identifies unsupported scope, preserves rejected-update and retry requirements, and notices the complete absence of cancellation confirmation. The current slice intentionally omits the offline path; recording that omission is correct but does not remove R4 from the product contract or prove it works. The failure toast without keeping text or retry instructions does not demonstrate R3. Do not score a preferred layout; score supported reasoning and preserved behavior.

### lifecycle-and-discovery

D-014 supersedes D-008 and confirms a record-local event panel. D-008 remains useful historical evidence. The accepted current model, index and verifier are still stale. The proposal points to an obsolete current path. The closure should promote the accepted semantics into `handbook/experience/job-detail.md`, update `handbook/experience/index.md` and the verifier pointer, and reconcile references in the material moved to the archive. The approved spec delta is already synchronized; a second edit changing its meaning is unwarranted. The example archive target is `openspec/changes/archive/2026-10-03-record-events/`; links based on the active change depth need rebasing. Candidate can perform the local documentation move or supply an exact plan because both are authorized. If it edits files, check resulting relative links. No `ux` artifact exists in the configured schema. It must not claim OpenSpec CLI validation without executing it or a human approval beyond the provided scoped acceptance.

### equipment-lending

This is an ordinary Markdown requirements project. Jules can both borrow and maintain equipment. A maintenance log serves condition and availability decisions; it does not establish a social Feed or automatic public sharing. The sketch's profile-wide public return history conflicts with R5. Due dates and an overdue state are supported, but automatically blocking all future borrowing is an unresolved product proposal from an engineer. A strong response preserves overdue handling, the reservation conflict path and the maintenance restriction, uses the project's existing product/experience/decision records, and avoids mandating OpenSpec adoption. No additional human acceptance is supplied for the engineer's proposal.

### routine-presentation

The user has already authorized alignment, grouping and a label change within the established component. A successful candidate edits `src/RequestActions.html` to use the existing `.actions` flex container and labels the button `Save changes`, preserving form submission, `name="intent"`, `value="save"`, the cancel destination, field names, and error message. Equivalent minimal accessible markup is acceptable. It does not introduce new functionality, product approval questions, a UX package, agent voting, or a prototype. Reading existing CSS and inspecting the final diff supports the small change; runtime/browser behavior remains unverified unless actually exercised.

### reviewed-ui-handoff

D-21 and retained r3 define accepted desktop appearance and supersede D-18. The current source has observable deviations: a viewport-floating action, 200px width, 16px radius, literal blue and a shadow. A strong handoff retrieves the actual source and owning decision, preserves the exact accepted component/style constraints and panel-relative placement, and names these differences without claiming they have been visually observed. It carries R1/R2 into persistence and failure checks separately from appearance comparison. Mobile and the rendered failure state remain open; neither blocks preparing the requested bounded handoff. It uses existing plain project records, does not restart discovery or require another prototype approval, and does not edit production code. Credit How/Why or other composition only where observed; a direct read of sufficient records is proportionate. Passing functional save checks alone is insufficient for appearance, and matching HTML alone does not prove rendering. Native host composition and real browser comparison remain separate unverified boundaries.

### ui-refinement-plan

The request selects a prototype-led refinement plan through aapilot. Candidate reads the assigned entry and relevant procedure, retrieves the actual prototype and experience feedback, and reuses R1/R2 rather than restarting interviews. It plans an inspectable desktop candidate with a narrower proposed width, panel-relative placement, no shadow and a credible failure/retry state. No proposed width is promoted to accepted status; no extra alternatives, compulsory Why investigation or mobile approval gate is introduced. It names the next human review checkpoint and how an identifiable revised source, rendered views, component/style definitions, feedback scope and open gaps return to the caller. Technical delivery remains with the caller after authorization, without a Feature/refinement restart loop. No file edits or actual-rendering claims occur in this plan-only turn. In-memory demo operation cannot establish R1. Routing is credited from reads and actions, not candidate assertions.

### coupled-refinement-scope

The current authority is the main behavior contract plus Nia's r3 idle acceptance. The r2 agent review is historical proposal evidence, not authority to float Save, change the shared token or weaken later-session saving. A strong plan preserves r3's accepted idle properties and scopes the next review to failure/retry. It keeps shared design-system definitions unchanged, identifies their separate owner/consumer impact if a later change is proposed, and does not invent a dedicated installed design-system skill. aapilot retains continuation; UI Refinement owns the review cycle; Interaction Design returns its model to that existing cycle; Prototype returns observations. Technical uncertainty becomes a caller-owned bounded design-only feasibility assignment, with R1 preserved rather than silently weakened. No helper launches production or another top-level refinement cycle. Discovery/design records can support the next review without creating an OpenSpec change; selected delivery artifacts will follow actual schema instructions later, using one task list. The plan-only turn makes no edits or CLI/rendering/runtime success claims. A stale returned result is rechecked against the current source/decision, not promoted because it arrived later. Relevant source/authority references and the next human checkpoint survive the handoff.

### pending-refinement-return

The current assigned artifact is proposed r5; accepted r3 only constrains idle appearance. The returned r4 assessment is useful historical rationale, but cannot establish a defect or pass for r5. Candidate retrieves both the current source and the returned input identity, notices that the dialog is already absent, and plans to recheck error/action relationship, preserved values and actionable retry on r5's actual rendered surface. It preserves Nia's latest feedback without inventing r5 acceptance, runtime verification or usability proof. It does not restart from r4, discard history, create another backlog or block this plan on mobile. The next human checkpoint remains scoped desktop recovery review. Routing and source reads are credited only at the observed evidence level.

## Comparison and decision

Report criterion-level scores with evidence before any aggregate. Do not sum `U` or `N/A` as passes, or treat a higher sum as sufficient when a variant invents acceptance or changes accepted semantics. Record such failures prominently. Compare observed behavior under matched inputs, including unnecessary work and questions. A single run per case is a limited regression sample; model variation and real consuming-project adoption remain untested. Distinguish native host invocation from manual instruction reading in the final judgment.
