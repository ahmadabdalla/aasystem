# Engineering verification

How a fresh verifier checks code you keep, for [independent implementation verification](verification-contract.md#independent-implementation-verification).

## Assign

As the owner, brief the verifier as [review context](delegation.md#reviews) describes, and also give it:

- the combined change, with its baseline or diff
- the inputs in scope and the project recipes
- the fixtures and resources it owns, where evidence goes and its access limits
- a work and time limit, and what to return
- what it must apply, with the absolute path of each criteria file:
  - For changed production code, the [local-code criteria](../../maintainability/references/local-code.md).
  - If interfaces, dependencies or invariant ownership change, including a callable's new or changed parameters, add the [boundary criteria](../../maintainability/references/boundaries.md).
  - For business-state changes, add the accepted identity, ownership, consistency and failure guarantees, and the required cases from the design. If the design doesn't say how to check a guarantee, add [Business state and consistency](../../architect/references/business-state.md).

One verifier applies all of these; don't spawn a specialist per criteria file.

## Assess and exercise

As the verifier:

1. Read the actual diff for scope, real defects and maintainability risks.
2. Run the affected project checks on the tested inputs, as [local execution](verification-contract.md#local-execution) describes.
3. Exercise the reported surface and its side effects. A unit test doesn't prove an API or UI path it never ran. Confirm each rule in the brief runs from the project's normal entry path, in the code that owns it, not only from its tests.
4. Derive checks from the agreed contract and the actual change, not just the design or the existing tests. If rejection, competing writes, replay, partial failure or recovery threaten a guarantee, exercise them.
5. Check the affected [signal effects](execution.md#signal-effects). Say what you observed, what you inferred, and which findings are review opinion.
6. Report concrete gaps in coverage of the changed behaviour. Use targeted mutation checks or a specialist only for a named risk. Report unrelated gaps separately; don't start a wider audit.
7. If a decision was assessed with [10x](../../10x/SKILL.md), run its required growth checks and report the volumes, rates or concurrency you tested. Keep deferred targets apart from acceptance requirements.

Don't change product code or expectations while verifying. If the harness is broken, send it back for a bounded repair, and leave blocked observations unverified. Record the commands, results, tested identity, findings, evidence and limits. If project recipes are missing or stale, report that to the owner; don't fix them.

