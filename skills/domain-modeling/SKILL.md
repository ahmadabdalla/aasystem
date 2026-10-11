---
name: domain-modeling
description: Clarify project concepts and preserve agreed terminology or consequential decisions in a glossary and ADRs. Use when meanings or relationships are ambiguous, or when recording or revising a project decision.
disable-model-invocation: true
---

# Domain modeling

Before starting, read the [shared execution contract](../aasystem/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Keep the project's meaning and decision rationale available to future work.

## Discover and clarify

Read project instructions and relevant system-wide and context-specific records. Follow an existing glossary map and reuse the project's locations, formats, and context boundaries. The references below guide placement of new records. Create a file only when there is agreed content to save.

Identify the ambiguous term, relationship, or decision. Test the meaning with a concrete scenario, including a consequential edge case. Compare claims about existing behavior with code or observed evidence. Preserve discrepancies between intended and implemented behavior. Ask one question and wait when a material meaning or preference cannot be established; use [grill-me](../grill-me/SKILL.md) only if several dependent choices need an interview.

## Preserve the result

- For agreed project vocabulary, read [glossary.md](references/glossary.md).
- Before creating or editing a project decision record, read [adr.md](references/adr.md) for qualification, ownership, scope and maintenance. Routine choices stay in their requirement or task record.

Apply document edits already authorized by the task. Research-only or read-only work returns proposed wording and its destination. When creating or revising records, reuse or update the smallest project instruction pointer to read relevant terms and decisions before changing the affected area. For ADRs, ensure it directs edits and final diff review to accessible project-owned maintenance rules. Use actual project-relative paths; records, rules and pointer must work without this toolbox. Preserve unrelated instructions.

Return the resolved meaning or decision, its record path when saved, evidence limits, and affected acceptance criteria to the caller. Link the canonical record from the relevant requirements, solution or design record instead of maintaining duplicate decision text. Changes to intended behavior feed the verification plan and affected feature recipes; an accepted ADR does not establish that the implementation passes. Personal principles remain the responsibility of [reflect](../reflect/SKILL.md).
