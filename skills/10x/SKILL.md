---
name: 10x
description: Assess a decision or design under plausible growth, exposing its first constraints, tradeoffs, verification needs, and reconsideration triggers. Use within domain design or as a bounded independent challenge.
disable-model-invocation: true
---

# 10x

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Test whether a decision still holds when something grows. The caller owns the decision.

1. **Read what exists.** Read the decision, its options and constraints, and the existing rationale. If a current assessment exists, extend only the part whose assumption or constraint changed. If an edit keeps the decision, stop.
2. **Pick what grows.** Name each growth that could change the choice: stored data, request rate, concurrency, workflow complexity, cost or operating effort. For each, give today's baseline and a plausible larger level. Start from 10× of what can actually grow. If a factor is fixed, leave it out. If another factor tests the decision better, use it and say why. Mark each number as measured, with its source, or assumed. If a baseline is missing, say so.
3. **Find the first constraint.** For each scenario, name what gets slow, costly, confusing or unreliable first, and why. Treat data volume, request rate and concurrency as separate scenarios. Cite the code or measurement that shows it, or label the claim an estimate. Reasoning and multipliers give estimates, not measured latency or capacity.
4. **Decide now or later.** Say what to accommodate now, what to defer, and why. If growth changes how the options rank, give the level where the pick flips. Add complexity only for a concrete benefit at a plausible level.
5. **Name the check and the trigger.** For each assumption the decision rests on, give the input or action and the result you expect to see. Give an observable condition, with a threshold, that reopens the decision. If the verification plan already has the check, link it. Mark targets you propose apart from accepted requirements.

If no growth changes the decision, say why in one line.

Return each scenario as **Scenario**, **First constraint**, **Now / defer**, **Check and trigger**. Add it to the caller's rationale or return it to the caller; it needs no separate report. A deferred target is not a release requirement. Run checks only if your assignment includes them.
