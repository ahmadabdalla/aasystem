# Module design review

Apply [boundaries](boundaries.md). Add [local code](local-code.md) when reading effort inside a module matters. This review is read-only: read tests, and run them only if the caller allowed it.

## 1. Pick the scope

- **Named module:** the module, plus the callers and dependencies needed to understand its contract.
- **Named workflow:** one entry point through the modules that handle it.
- **Whole project:** up to 3 representative workflows. Say why you chose each: usage, ownership or change risk. With no signal, label the choice an assumption.
- **Unclear:** pick a bounded scope and state it.

Record the revision and any uncommitted changes you read. A sample is not a verdict on the whole project.

## 2. Trace

For each module or workflow:

1. Find the entry point, interface, implementation, callers, dependencies and tests. Trace one behaviour: where its rule is defined, called and tested. Mark evidence you couldn't reach.
2. Pick one plausible change to that behaviour, from the request or the contract. Label it **hypothetical**. List the modules that would change and why, and the callers that wouldn't.
3. Dig deeper only where a conclusion depends on it. Cite `file:line` for every material claim.

A hypothetical change shows expected change cost, not a runtime failure. A structural finding doesn't need wrong output.

## 3. Assess five dimensions

| Dimension | Look at |
| --- | --- |
| Depth | What the module hides, and what callers still coordinate |
| Interface | Inputs, outputs, failure meaning, effects, lifetime, compatibility |
| Locality | Who owns the traced rule; what the hypothetical change touches |
| Leverage | Duplication the module saves, against the coupling sharing adds |
| Seams | How the traced behaviour can actually be tested or varied, including setup and cleanup |

- **Leverage:** judge present callers. One caller isn't a weakness; future callers don't justify generalising.
- **Seams:** check how dependencies are actually supplied. An interface alone doesn't make a seam.
- **Locality:** count touched modules with their reasons. Justified coordination isn't poor locality.

### Scores, only if asked

Score each dimension 1-5, or **not assessed** when evidence is thin, with evidence beside each score. Don't score from file length or test count. Give no overall project score.

## 4. Report

If the caller has a record format, use it. Otherwise:

```markdown
## Scope
<what you reviewed, why, revision, uncommitted inputs>

## Assessment
- <dimension>: <conclusion> [<score>]. Evidence: <file:line>. For a maintainer: <what it costs or saves>.
- Findings in the [bounded format](../SKILL.md#return-a-bounded-assessment).

## Change trace
<hypothetical change> → <each module touched, and why>

## Priority
1. <investigation or fix>: <benefit>; <risk or tradeoff>
(up to 3; none is fine)

## Limits
<what you didn't inspect>; tests read vs tests run, with commands and results; the scope the conclusions apply to
```
