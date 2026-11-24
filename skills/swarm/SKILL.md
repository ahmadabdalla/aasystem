---
name: swarm
description: Coordinate independent work slices or declared races and return one evidence-backed coverage report. Use for parallel investigation, implementation partitions, or coverage; use arena to compare and synthesize competing designs or artifacts.
disable-model-invocation: true
---

# Swarm

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Pick the mode.** In a **partition**, each slice covers a different part of the work. In a **race**, several workers attempt the same goal. If candidates need judging and combining, use [Arena](../arena/SKILL.md) instead. For a race, write the rule before any worker starts: first verified pass, rank all, or pick the best. If you rank or pick, write the criteria with the rule.
2. **Draw the coverage table.** Give each slice a row: owner, inputs, files it may write, expected result and how you'll check it. Done when every part of the request has a row. If two slices write the same file or state, run them in order. If a slice needs something that doesn't exist yet, build it before you start any worker.
3. **Brief each worker.** Brief each under the [delegation rule](../pilot/references/delegation.md) and name the exact version to work from. For a measurement, also give the method, units, conditions and comparison order. Each result is **pass**, **issues** or **blocked**, with its evidence.
4. **Start the ready slices at once.** If you can't start separate agents, run the slices yourself in turn and say the results weren't independent.
5. **Check every result.** If a result lacks its evidence or method, ask for one fix. If it still lacks them, the row stays uncovered. An **issues** result with evidence covers its row. A missing or blocked result doesn't. In a race, apply the rule you wrote. Stop the other workers only when the rule allows it. Keep their work until you report.
6. **Combine.** Settle conflicts and merge the changes. If code changed, run the project's verification on the merged result.

Return the table with each row's result, the findings that matter, evidence links, dropouts and gaps. In a race, give the rule, the criteria and why each loser lost. If any row isn't covered, open with "Coverage: partial" and name the row.
