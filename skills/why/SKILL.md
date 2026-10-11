---
name: why
description: Reconstruct why an existing design or behavior took its current shape. Use for rationale, historical constraints, regressions, and thresholds; use how for current mechanics.
disable-model-invocation: true
---

# Why

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Anchor the question in an artifact, investigate its history, and calibrate conclusions to the evidence.

Anchor the question in a concrete artifact, symbols or decisions, and the relevant change history. Use [how](../how/SKILL.md) if the current behavior is unclear. Treat a hypothesis in the user's question as a candidate to investigate.

Read relevant project ADRs and their successors early. An accepted contemporary record can directly establish rationale; a proposal or later reconstruction has different authority. Check whether the recorded constraints still hold and preserve disagreements with current behavior.

Follow history through renames, substantive commits, reviews, and linked records as available. Discover authorized sources through the actual tools and repository, then account for all seven evidence categories: source control, issue trackers, design documents, team discussions, infrastructure observations, error records, and product data. For each, record searched with findings, searched with no findings, unavailable, or omitted with a concrete reason it cannot inform this question. A promising recent commit alone does not justify skipping other relevant evidence. Keep searches scoped to the target; unavailable history does not prove no rationale exists.

When delegation is supported and permitted, give each available relevant source a separate investigator with the same code anchor, question, and confidence framework below. Default to this source coverage, then use a separate synthesizer to reconcile findings and spot-check citations. Defensive logic warrants particular attention to incidents, error records, and runtime constraints. A trivial case may be answered inline after checking why the other categories would be redundant. Without independent investigators or a synthesizer, perform the available searches directly and disclose the limitation. Use actual configured models and tool access, without treating a worker's ability to query a connector as permission to write to it.

Separate claims by the strength of their evidence:

- **Direct:** a contemporary record explicitly gives the reason.
- **Supported:** multiple independent pieces of indirect evidence converge.
- **Inferred:** a plausible interpretation with its reasoning stated.
- **Speculative:** a hypothesis with weak evidence or equally plausible rivals.
- **Unknown:** the searched record cannot answer the question.

Build a short chronology. Surface contradictory records and competing explanations. Cite each material factual or causal claim; check that the source actually supports it. Reading present code establishes mechanics, not the author's intent. Recent edits do not automatically explain the original choice.

Explain which historical constraints still apply. If this investigation precedes a change, translate the findings into what to preserve, change, avoid, and treat as risk, each with its evidence or uncertainty. This supplies constraints to [solution](../solution/SKILL.md) or [architect](../architect/SKILL.md).
