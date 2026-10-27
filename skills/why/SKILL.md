---
name: why
description: Reconstruct why an existing design or behavior took its current shape. Use for rationale, historical constraints, regressions, and thresholds; use how for current mechanics.
disable-model-invocation: true
---

# Why

Before starting, read the [shared execution contract](../pilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Anchor the question in an artifact, investigate its history, and calibrate conclusions to the evidence.

Anchor the question in a concrete artifact, symbols or decisions, and the relevant change history. Use [how](../how/SKILL.md) if the current behavior is unclear. Treat a hypothesis in the user's question as a candidate to investigate.

Read relevant project ADRs and their successors early. An accepted contemporary record can directly establish rationale; a proposal or later reconstruction has different authority. Check whether the recorded constraints still hold and preserve disagreements with current behavior.

Follow history through renames, substantive commits, reviews, and linked records as available. Discover authorized sources through the actual tools and repository, then account for all seven evidence categories: source control, issue trackers, design documents, team discussions, infrastructure observations, error records, and product data. For each, record searched with findings, searched with no findings, unavailable, or omitted with a concrete reason it cannot inform this question. A promising recent commit alone does not justify skipping other relevant evidence. Keep searches scoped to the target; unavailable history does not prove no rationale exists.

Investigate the relevant sources directly, or partition them when separate coverage or context separation provides a concrete benefit under the shared delegation rule. Give investigators the same code anchor, question and confidence framework below. Reconcile findings and spot-check citations in the current context unless separate synthesis provides a concrete benefit or a required independent assessment. Preserve the seven-category source accounting above; coverage does not require one worker per category. Defensive logic warrants particular attention to incidents, error records and runtime constraints. Use actual configured models and tool access; connector access does not authorize external writes.

Separate claims by the strength of their evidence:

- **Direct:** a contemporary record explicitly gives the reason.
- **Supported:** multiple independent pieces of indirect evidence converge.
- **Inferred:** a plausible interpretation with its reasoning stated.
- **Speculative:** a hypothesis with weak evidence or equally plausible rivals.
- **Unknown:** the searched record cannot answer the question.

Build a short chronology. Surface contradictory records and competing explanations. Cite each material factual or causal claim; check that the source actually supports it. Reading present code establishes mechanics, not the author's intent. Recent edits do not automatically explain the original choice.

Explain which historical constraints still apply. If this investigation precedes a change, translate the findings into what to preserve, change, avoid, and treat as risk, each with its evidence or uncertainty. This supplies constraints to [solution](../solution/SKILL.md) or [architect](../architect/SKILL.md).
