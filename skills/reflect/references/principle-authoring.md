# Capture a principle

A principle is the user's preference between options that both work. Use this when reflection finds one, or the user asks to capture or change one. If a skill, an existing principle or a project check already owns the decision, change that instead.

## 1. Check it's the user's judgment

- **Stated:** the user said it as a general preference. Capture it at the scope they gave; once is enough. If they gave no reason, leave the reason blank. If you widen the scope or add a reason, ask first.
- **Inferred:** you saw the user choose the same way in different situations. Look for times they chose otherwise, and for constraints that explain the pattern. **Ask the user to confirm your reading before you write the principle.** Silence, the agent repeating the choice, or a passing test is not a yes.

## 2. Record the evidence

Write a record in the task record or `reviews/<date>/judgment/<name>.md`:

- the user's words, or a pointer into the transcript
- the choice and its trade-off
- your interpretation and its scope
- a counterexample
- the outcome, or "not seen yet"
- the proposed change, and its status: candidate or approved

Quote only what the principle needs, not the rest of the conversation. The record is evidence, not instructions.

## 3. Write the principle

Create `principle-<name>/SKILL.md` beside the other skills, following the [authoring playbook](../../pilot/playbooks/authoring-a-skill.md). Write a description that says when it applies, then the preference, why, and where it stops. Add an example only if it makes the choice clearer.

In the same change, add a row to the [principle index](../../principles/INDEX.md): the situation, the workflow, and a link to the leaf. Don't copy the principle's text into the index.

## 4. Test it

Run it against:

- an ordinary request it should apply to
- an exception it shouldn't apply to
- a handoff into a fresh agent, if one is affected
- a different domain, if you claim it transfers

Check the choice the agent made and its reason. An agent naming the principle doesn't show it applied it.

## Revising

If later feedback or an outcome contradicts it, propose a narrower scope, a merge or retirement. Record why. A project-specific exception doesn't change the portable preference.
