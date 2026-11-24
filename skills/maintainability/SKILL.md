---
name: maintainability
description: Assess how hard supplied code or a design is to understand, change and verify. Use for module design reviews, structural assessments of a design or diff, and finding tests that guard no behaviour.
disable-model-invocation: true
---

# Maintainability

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Find what makes the work hard to understand, change and verify. Return findings to whoever asked. Don't choose the design or edit code.

## Select the assessment

- If asked for a module design review, or how maintainable existing code is, follow [Module design review](references/module-design-review.md).
- If asked which tests guard no behaviour, check each test in scope against the needed-test rule in [Local code](references/local-code.md)'s **Verification clarity**. List each test that fails it, with the clause it fails, one line each.
- Otherwise (a design, a diff or a narrow question), follow the steps below.

## Assess

1. **Gather.** Get the artifact and its revision, the intended change, the constraints and the callers. If something missing could change a finding, say so. A caller you can't read still exists.
2. **Read the criteria.** [Local code](references/local-code.md) and [Boundaries](references/boundaries.md). For a design with no code yet, Boundaries alone.
3. **Trace.** Follow each concern through a real use or a likely change.

## Return a bounded assessment

One entry per finding that could change the caller's design, verdict or plan:

```text
<location> [demonstrated | risk | preference]: <what it costs a reader or a change> → <fix>. Tradeoff: <cost of the fix>. Evidence: <what you traced or ran>. Verify: <check that would settle it>.
```

**demonstrated:** you traced it in this code or saw it in a run. **risk:** plausible, not shown. **preference:** a style choice.

No findings is a valid result. Say what you inspected and what you didn't.
