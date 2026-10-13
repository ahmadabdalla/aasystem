# Project decision records

Before writing or reviewing an ADR, choose its rules in this order: documented project rules for the record's scope, the convention used by existing ADRs in that scope, then the framework default below. This includes older formats the project still uses. Use an external template only if the project explicitly adopted it. If the sources conflict and specify no precedence, identify the conflict and leave conformance undecided.

## Decide whether to record

Create an ADR only when all three apply:

- Changing the choice later has meaningful cost.
- A future reader would need context to understand it.
- Genuine alternatives involved a consequential tradeoff.

Otherwise keep the choice in its task or design record, unless an ADR is explicitly requested. Reuse an existing decision rather than create another account of it.

## Choose owner and scope

Ownership follows the decisive tradeoff:

- **Product:** outcomes, business rules and operating commitments.
- **Design:** interaction, navigation and information presentation.
- **Software:** implementation structure and technical boundaries.

Scope is independent: system-wide or contained within an established business context. A technology name does not determine ownership; a feature or dimension does not establish a context.

Keep one decision per ADR, including choices spanning dimensions; several consequences do not make several decisions. Cross-link related records. Read relevant decisions across dimensions and scopes, and resolve conflicts at the owning scope before adopting a contradictory choice.

## Follow project placement

Use the project's locations, numbering and discovery pointers. Otherwise store decisions at the narrowest scope containing their consequences:

- `docs/adr/` for system-wide choices and agreements between contexts.
- `<context>/docs/adr/` for context-local choices.

Create directories lazily, when a qualifying record is needed. Default to `NNNN-short-title.md`, using the next unused number in the chosen directory. The location need not encode dimension; state owner and scope briefly when useful. Link the record from the project's existing index or instructions.

## Maintain one decision

Before writing, reread the relevant records and classify the change using the rules below. Before delivery, check the diff against that classification.

- **Update:** correct, clarify or add evidence for the same decision without changing its choice.
- **Separate:** an independent choice meeting the ADR threshold gets its own linked record; other choices stay in their task or design record.
- **Supersede:** explain the changed evidence or constraint for a materially different accepted choice, then create a successor linked both ways. Preserve the old rationale and mark the old record superseded only when the replacement is accepted.

When splitting an overloaded ADR, preserve each decision's sources, standing, rationale and historical links. Extraction alone does not supersede an accepted choice.

## Write a small record

The framework default requires a title and prose stating:

- The problem or constraint.
- The decision and intended result.
- Why the decision was chosen.
- At least one alternative considered and why it was rejected.
- Expected effects, including costs and limitations.

State standing and authority using the rules below. Aim for 1–3 sentences; use more to cover the required information. Headings and simple ASCII flows are optional.

Authors and reviewers use the same selected rules. For each failure, cite the rule and identify the missing information or format error. Require specific headings only when project rules require them. Link sources and substantial evidence; keep requirements, implementation steps and detailed verification scenarios in their owning documents.

Make standing and authority clear using the project's format:

- **User-confirmed:** the user's recorded decision covers this choice; link its source.
- **Explicitly delegated:** a source grants decision authority within stated boundaries.
- **Proposed:** a choice awaiting the necessary decision.
- **Unresolved:** no settled choice or sufficient authority is known; missing provenance stays unknown.

An authoritative project record can supply the basis without inventing user confirmation. Authority is separate from evidence: a proposal, generated document or working implementation does not establish acceptance; acceptance does not prove implementation. Acceptance of one choice does not authorize additional scope or presentation. Preserve these distinctions in consequential task/design choices below the ADR threshold too, without creating another approval register or requiring approval for routine choices already within scope.

Return affected constraints and observable expectations to the caller. Link verification evidence when useful; an implementation failure does not authorize rewriting the intended contract.
