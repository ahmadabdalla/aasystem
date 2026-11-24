# Refactoring

You own the behaviour contract while you change structure. If you find a defect, send it to [Bug fix](bug-fix.md). If intended behaviour changes, send it to [Feature](feature.md). Neither counts toward the equivalence claim.

1. **Capture the baseline.** Invoke the [`how`](../../how/SKILL.md) skill to read the affected code. Before moving anything, run a characterisation test, snapshot or equivalence harness through the relevant public surface. Record inputs, outputs, side effects, the revision and known defects. Compiling and linting don't capture behaviour. If the refactor prunes tests, the baseline can't rest only on the tests you'll prune. Done when the baseline has run and its results are recorded.

2. **Name the improvement.** Say which ownership, data shape or dependency changes, and how that makes the code easier to understand or extend. If it's a large coupled migration, invoke the [`figure-it-out`](../../figure-it-out/SKILL.md) skill.

3. **Design the target.** If the reshape meets the [Architect design trigger](../../architect/SKILL.md#design-trigger), invoke the `architect` skill with the baseline and compatibility constraints.

4. **Move in small, checked steps.** Invoke the [`implement`](../../implement/SKILL.md) skill to make the mechanical edits. If you're pruning tests, invoke the [`prune-tests`](../../prune-tests/SKILL.md) skill with the scope and baseline.

5. **Prove equivalence.** Get [independent verification](../references/verification-contract.md#independent-implementation-verification) comparing old and new behaviour on the real artifact: side effects, affected entry points and intended source or config differences. It also checks that the diff delivers the improvement you named, even if Architect settled the target. For pruned tests, it also checks Prune Tests' coverage account.
   - If the verifier can't settle a structural concern, invoke the [`maintainability`](../../maintainability/SKILL.md) skill.
   - If an edit doesn't deliver the improvement, revise or drop it.

6. **Deliver.** Report the improvement, the contract you preserved and any behaviour changes you split off.
