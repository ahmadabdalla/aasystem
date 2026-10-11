---
name: grill-me
description: Interview the user to discover product activities and journeys or resolve consequential choices. Use for discovery interviews, an explicit grilling request, or several choices needing the user's judgment; a single missing detail needs only a focused question.
disable-model-invocation: true
---

# Grill me

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Conduct a bounded discovery or decision interview. For discovery assignments, read [Discovery interviews](references/discovery-interview.md) and follow that procedure instead of the decision-resolution steps below.

1. **Set the scope.** Reuse the caller's brief, settled choices, and evidence. Identify the decision being made and which choices depend on others. Keep a short working record of settled, open, and deferred choices; revisit a settled choice only when new evidence changes it. Reserve questions for consequential choices; propose routine defaults within delegated authority, and reset scope if questions proliferate.
2. **Find the facts.** Inspect relevant code, project terminology, decision records, and available primary sources before asking the user. Separate observations from assumptions and preferences. If a necessary fact is inaccessible, name the gap and ask for the minimum missing input.
3. **Ask the next question.** Choose the most consequential open choice whose prerequisites are settled. Ask one question, with a recommended answer and its main tradeoff when the evidence supports one. Stop and wait for the answer before further investigation or action. Keep dependent questions for later.
4. **Update the brief.** Incorporate the answer, its rationale, and any new constraint. Surface contradictions with earlier answers or evidence. Repeat only while choices needed for this scope remain unresolved; leave unrelated branches outside the interview.
5. **Return the result.** Summarize settled choices, consequential assumptions, explicitly deferred questions, and observable success criteria. An unresolved choice that could change the outcome makes the brief conditional. Return to the calling workflow; a standalone interview ends with this brief. Preserve any requested checkpoint before implementation.

Use [domain-modeling](../domain-modeling/SKILL.md) when agreed project terms or qualifying decisions need recording. Respect the assignment's document-editing scope; a read-only interview returns proposed notes. The caller reuses the brief instead of restarting the interview.
