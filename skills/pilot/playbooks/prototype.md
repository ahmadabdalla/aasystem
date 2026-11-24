# Prototype

A prototype is **throwaway work that settles one decision**. You return evidence and a recommendation, not production code. If the request already describes a feature to ship, use [Feature](feature.md) instead.

1. **Write the decision.** Name the alternatives and what you'd see that tells them apart, as the [`probe`](../../probe/SKILL.md) skill describes.
2. **Look before you build.** If the question is visual or about interaction, read the requirements and look at prior art.
3. **Build the smallest experiment, outside the product.** If it's a state model to click through or UI alternatives, brief a worker to invoke the [`prototype`](../../prototype/SKILL.md) skill with the question, scope and where the evidence goes. Otherwise invoke the `probe` skill. Keep it in a scratch directory or worktree.
4. **Run it on the surface the question is about.** Drive the UI, read the output, or time it on the project's real data. Check you measured what the decision depends on, not an easier stand-in.
5. **Recommend.** Return the alternatives, what you saw, the decision or "inconclusive", the scratch path, and what it can't show, such as production reliability. If building it is also asked for, take the direction to the change playbook, through Architect if it changes interfaces, state ownership or module boundaries. Otherwise stop.
