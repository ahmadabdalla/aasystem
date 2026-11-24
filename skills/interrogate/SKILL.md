---
name: interrogate
description: Challenge a proposal, design, change or recommendation. Use to find weak assumptions, failure modes and framing errors, to assess a PR's merge risk, or to find operational and security detection gaps.
---

# Interrogate

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Find what's wrong with the work, and with the question it answers.

## Steps

1. **Brief.** Reuse the caller's brief, or write one as [Reviews](../pilot/references/delegation.md#reviews) says.
2. **Review.** Start three reviewers in parallel on the same brief. Only if your host has no subagent tool, review it yourself and say it wasn't independent. Each reviewer checks:
   - correctness, boundaries, data ownership, failure paths, verification coverage and cost
   - **the frame:** a premise every option shares that nobody tested, a missing alternative, a means mistaken for the user's goal, a constraint that conflicts with the goal
   - if the question is detection gaps, each scenario in [Signal assessment](references/signal-assessment.md)
   - if reader burden or change cost could change the verdict, the [Maintainability](../maintainability/SKILL.md) criteria
3. **Check.** Merge duplicates. Keep disagreements and findings only one reviewer raised. Check each finding that could change the verdict in the code or source, or by calling the Skill tool with "probe" ([probe](../probe/SKILL.md)).
4. **Report.** Lead with the verdict, then one line on whether the review was independent and what the reviewers were given. Mark each finding **act on**, **consider**, **noted** or **dismissed**:

   ```text
   <location> [demonstrated | risk | preference]: <condition> → <consequence>. Evidence: <what you saw>. Fix: <smallest change or experiment>.
   ```

   Defects outside the question go under **noted**, one line each. For each thing you couldn't verify, say what would settle it.

   If it's a PR or diff, report in [Merge risk](references/merge-risk.md)'s format exactly as written, with every finding under its category and no other findings section. If you used Signal assessment, its blocks are the report. Don't rate proposals or designs with Merge risk.
