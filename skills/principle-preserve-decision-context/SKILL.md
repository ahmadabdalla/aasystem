---
name: principle-preserve-decision-context
description: Preserve the information needed for decisions when simplifying a workflow or changing a handoff between skills, agents, or teams. Use when removing repetition or replacing supplied context with references.
disable-model-invocation: true
---

# Preserve decision context at handoffs

When simplifying a workflow that crosses skills, people, or agent contexts, judge the change by whether the receiving stage can still make the intended decision. Trace the path before deleting repeated guidance. Keep the constraints, evidence limits, and acceptance criteria that the next stage needs. A reference is sufficient only if that stage can retrieve and use it.

The tradeoff is local brevity versus reliable decisions across the whole workflow. Within a shared context where the information is already available, remove redundant restatement. This does not justify copying an entire transcript into every task.
