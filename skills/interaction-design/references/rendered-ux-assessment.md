# Independent rendered UX assessment

Assess an interface that already renders, such as a prototype or a release candidate, for friction in the person's task. You set up two assessors and reconcile their reports. The caller keeps the task and decides what to fix.

## Prepare

1. Gather the actor, their job, the intended behaviour, requirements, accepted visual constraints, shared components and the review scope. An approved visual reference is optional.
2. Pin the source revision and start the running instance with the project's preview steps. Check it loads and its reset works before you launch anyone. Don't edit source until both reports are back.
3. Pick the states to assess: empty, typical and mature collections; long or repeated labels; validation errors; selection changes; leaving and coming back. Include finding and reading existing records at scale, not just adding them. Add narrow layouts, supported themes, keyboard use and reduced motion where they apply.
4. Give each assessor its own browser session and its own synthetic data, using the project's fixtures. Separate records can be enough; separate tabs on one backend aren't. Source files stay shared and read-only.

If your host has no subagent tool or can't run two isolated sessions in parallel, stop and return the assessment as incomplete, naming what's missing. Never fill a seat yourself or with anyone who produced the work. If only the rendering tools are missing, the visual assessor may work from static captures, and every interaction lens is unverified.

## Launch

Start **exactly two fresh assessors in parallel**. Neither may have produced the work.

| Assessor | Brief | Owns |
| --- | --- | --- |
| Visual composition | [visual-assessment.md](visual-assessment.md) | Hierarchy, balance, alignment, spacing, typography, content, visual meaning, contrast and responsive composition |
| Interaction and continuity | [interaction-assessment.md](interaction-assessment.md) | Control states, feedback, motion, stable controls, finding records, navigation, keyboard and reduced motion |

Brief each one as an [independent discovery](../../pilot/references/delegation.md#reviews) review. Give it the scope, sources, accepted constraints, revision and instance, access and reset steps, assigned states, relevant principle leaves, its own brief, the table above and the Evidence and return section. Give neither the producer's discussion, draft findings or the other assessor's report.

## Evidence and return

Both assessors follow this section. Use the caller's report format if there is one, and the [retention rules](../../bootstrap-verification/references/project-contract.md#evidence-and-retention).

Write one block per finding:

```
### <surface> / <state> / <action>
Kind: <defect | concern | question>
Expected: <basis and its source>
Observed: <what happened>
Impact: <effect on the person's task>
Evidence: <capture path or action log>
Recommendation:
```

A defect was observed. A concern is reasoned; it can challenge an accepted design but doesn't authorise a change. A question is unverified. An empty list is a valid result. Report only what you observed or can tie to the person's task.

Before recommending a local patch, check the shared component and sibling surfaces. If a fix costs something else, such as a pinned control hiding content or breaking keyboard flow, say so.

End with:

```
Revision and instance:
Exercised: <actions, states, viewports, themes, data volumes>
Not covered:
Independence and access limits:
Evidence location:
Resources left in place:
Outside my lenses: <for the lead to route>
```

## Reconcile and hand back

1. Check each claim that could change a recommendation against the artifact and its evidence.
2. Merge duplicates and each assessor's out-of-lens notes, keeping each domain's observation. Settle conflicting recommendations by the person's task and the accepted constraints, not by vote.
3. Record each finding's disposition (fix, defer or reject, with the reason) and the open questions in the caller's record.
4. Send business-meaning changes to [Product](../../product/SKILL.md) through the caller. This assessment isn't [implementation verification](../../pilot/references/verification-contract.md#independent-implementation-verification).

After fixes, recheck the changed result with fresh assessors who didn't produce the fix. A recheck covers only what it exercises; a new full assessment uses the two parallel assessors above.
