# Working with OpenSpec

Use this when the target project uses OpenSpec or the task requests its adoption. Keep the current task owner and assigned phase. OpenSpec supplies change records and artifact instructions; the cookbook supplies the reasoning, execution, and proof requirements.

## Locate the change

Read project instructions and configuration. Identify the project root and selected change from the brief and available changes; resolve an ambiguous target before writing change artifacts. Reuse existing artifacts. Discovery/design work confined to supporting project records does not require creating a change. When writing change artifacts or entering delivery, locate the selected change and follow its actual schema dependencies. For requested setup, use the installed version's supported initialization and project conventions.

For setup or change-artifact work, check the installed CLI version and supported commands. For a selected change, use `openspec status --change <name> --json` and `openspec instructions <artifact> --change <name> --json` from the intended project to obtain the actual schema, dependencies, paths, templates, and project rules. Use `openspec new change` for an authorized new change. Follow returned locations, including any explicitly configured planning location, rather than assuming the default layout.

Read the relevant dependency files; a path or completed artifact status does not establish that its contents are understood or agreed. Give workers the selected change, requirement sources, assigned artifact paths, and applicable instructions with their brief. Every worker retains the shared baseline.

If required tooling or an instruction lookup is unavailable, report the exact blocked operation. Continue independently useful reading or analysis, distinguishing proposed output from validated artifacts. Do not fabricate CLI results, claim synchronization, or fall back to a second planning system. Adoption and installation stay within the task's authorized scope.

## Write into the shared record

For the default schema, assign ownership as follows; adapt to the project's returned artifact instructions:

| Artifact | Owner and content |
| --- | --- |
| `proposal.md` | Task owner: purpose, scope, affected capabilities, and impact, informed by product and solution findings. |
| Change `specs/` | Product owner: behavioral requirements, invariants, and scenarios; explicit additions, modifications, or removals. |
| `design.md` | Solution and architecture owners: approach, alternatives, implementation shape, and proof plan, written in sequence under the task owner. |
| `tasks.md` | Task owner: implementation and verification work against the agreed contract. |

The active schema defines the change artifacts and their paths; supporting-skill invocation does not add artifacts to it. Use the supporting-document ownership below and link those records from the change. Apply the shared execution contract's retention rules; the change directory is not a default destination for skill reports.

Respect the schema's dependencies and intentional omissions. A prescribed implementation or structural refactor can reuse an existing behavior contract. Resolve an unclear product rule through [product](../../product/SKILL.md); use the selected playbook for subsequent work. Each skill updates only its assigned content and preserves the others' decisions. Link durable project ADRs rather than duplicating them.

Use one implementation task list. Preserve the playbook's phases as headings or untracked workflow notes; do not make a second backlog. Each task states its completion check. Keep archive itself and post-archive work outside tracked implementation tasks. Reconcile affected artifacts when authorized decisions change, retaining the reason and preserving agreed requirements when only the implementation changes.

## Supporting project knowledge

Reuse the project's locations and formats. These defaults illustrate ownership, not a requirement to create every file:

| Content | Owner and example location |
| --- | --- |
| Product purpose, scope and feature/story/journey map | Product; `docs/product/overview.md`, linking requirements rather than copying them. |
| Behavioral requirements, invariants and scenarios | Product contract; main specs plus active change deltas. |
| Vocabulary and consequential decisions | [Domain modeling](../../domain-modeling/SKILL.md); existing glossary and decision records with their authority. |
| Navigation, interactions, UI rationale and linked sketches/assets | [Interaction design](../../interaction-design/SKILL.md); `docs/ux/<journey>.md` and project assets. |
| Traceability and decision standing | References on the owning requirement/interaction record; link the canonical decision rather than maintaining another authority register. |
| Technical approach and implementation work | `design.md` and the single `tasks.md`, as above. |
| Operating/verification recipes and dated observations | Project verifier's operational feature map and separate run evidence under the [project contract](../../bootstrap-verification/references/project-contract.md). |

Keep proposed changes distinct from accepted project knowledge. For example, `docs/ux/changes/<change-id>.md` can hold a proposed interaction revision while `docs/ux/<journey>.md` remains the current model. A section in an existing document can suffice. Give retained sketches and observations a source revision; temporary scratch paths cannot be the only evidence for a durable decision.

Use supported project configuration to point artifact authors at these canonical records and relevant obligations. For example, project `context` can identify the glossary and UX index; a `design` rule can require linking the affected interaction decision. Read the actual enriched instructions to confirm configuration is applied. Context and rules guide agents; they do not enforce acceptance. Generated project pointers follow the [project instruction guidance](../../bootstrap-verification/references/project-instructions.md) and remain usable without this cookbook.

Existing artifacts plus linked documents are sufficient when the handoff stays discoverable. A custom schema is an alternative when a separate interaction artifact and dependency materially improve the workflow; it adds distribution, version and migration responsibilities. Inspect and validate that selected schema before claiming a custom artifact exists. Placing `interaction.md` in a change folder alone does not register it, and artifact existence does not establish product-owner acceptance. In projects without OpenSpec, use the same ownership through their existing requirements, design and task records.

## Revise and retain

When a consequential decision changes, preserve its source and rationale under the [decision supersession convention](../../domain-modeling/references/adr.md). Reconcile affected requirements, interaction links, assets, implementation tasks and verifier expectations; retain unresolved conflicts rather than silently choosing the latest file. Reopen only decisions whose meaning or authority is affected.

Spec synchronization merges the selected spec deltas; it does not promote supporting UX proposals or update arbitrary project documents. At the authorized transition, update the accepted interaction model and related canonical records explicitly. Retain change-specific alternatives only for an identified future decision or evidence need, clearly marked historical or superseded. Historical snapshots may preserve a decision's context but are not competing current authorities.

Before sync/archive, identify references whose targets or relative bases will move. Afterwards, follow links from the main specs, current project documents and archived change; repair broken references and check that each points to the intended current decision or historical revision. A resolving link to a superseded decision can still be wrong for current work. Keep enough immutable evidence to explain old choices while pointing new work to their accepted successors.

## Prove and complete

Map important requirement scenarios to the project verifier and feature recipes. Keep actionable expected results in recipes with links to their requirement authority; keep dated observations in run evidence. Planned behavior stays unverified until exercised. Establish the first usable procedure when a new app can run.

Run supported document validation and review implementation against requirements and design. These checks supplement the execution contract's real-surface verification. Artifact status, task checkboxes, and an advisory review cannot establish that behavior passed. Retain pass, fail, and unverified results with the tested artifact identity.

For sequential changes, review the cumulative contract after each increment; reconcile later exceptions with earlier rules rather than relying on merge validity.

Report schema/structure validation, requirement and UI traceability review, product-owner acceptance, observed usability and runtime verification separately. A pass in one dimension cannot supply a missing result in another.

The task owner completes sync and archive only within the requested delivery scope and after the agreed completion criteria are met. Use the installed workflow's supported operations and required confirmations; instruction lookup alone performs no sync or archive. Inspect the resulting main specs and archived change, and preserve resolving evidence links. A blocked proof remains a reported gap.
