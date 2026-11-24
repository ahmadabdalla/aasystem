# Logic prototype

One self-contained HTML file that lets a domain expert drive a state model by clicking. Use it when a rule looks fine on paper but needs pushing through real cases. If the question is how something should look, use [ui-prototype.md](ui-prototype.md).

## 1. State the question

Put the question, the rules you're modelling and your assumptions in a visible intro at the top of the page. If the brief only proposes a rule, mark it proposed; running it doesn't accept it.

## 2. Pick the cases

Use the smallest fixtures that answer the question. Include:

- the normal journey
- an awkward sequence where two readings of the rules disagree
- a forbidden action

If the question depends on who acts, vary the people and their roles. One person can hold more than one role.

## 3. Keep the rules in a pure module

Write the rules in one `<script>` block as a reducer, a state machine or a few functions, with no DOM code. The free-play buttons and the guided steps both call it, so they can't disagree.

If the answer depends on a real runtime or integration, build the smallest runnable form that uses it, and say what an HTML simulation would have missed.

## 4. Build the page

Plain HTML, CSS and JS, all inline, so it opens by double-click. Label actions in the business's words ("Return equipment"), not event names. Top to bottom:

1. **Title and question.**
2. **Current state** as labelled fields, not a JSON dump, re-rendered after every click.
3. **Free-play buttons**, one per action, plus **Reset** to the starting fixtures.
4. **Guided scenarios**, one per tab. Each says what it sets up and what to watch for. Each step is a button that runs the real action. Starting a scenario resets to its starting state.

If an action is rejected, show why and show that the state didn't change. If you add debug controls, keep them visibly apart from the product's actions.

## 5. Exercise it

Run every scenario from reset and check the state after each step, not just at the end. Check that free play and the guided steps call the same module. Try the forbidden action and one out-of-order sequence. If a subtle error would flip the answer, add one focused assertion. Record each action, the expected state and the actual state.

Then follow [Observe and return](../SKILL.md#observe-and-return).
