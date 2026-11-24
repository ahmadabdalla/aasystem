---
name: grill-me
description: Grill the user on a plan, decision or idea in question rounds until you share an understanding. Use when they want their thinking tested, or say grill.
---

# Grill Me

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

If a caller sent you, start from its scope and evidence.

Grill the user on any plan, decision or idea. Only follow [Discovery interviews](references/discovery-interview.md) when you're asking someone how they work today and they aren't the one deciding.

1. **Map the design tree.** List the decisions the plan needs. Each answer can open more decisions. Leave out branches outside the scope. Leave out any decision the user, the caller or an accepted record already settled.
2. **Find the facts yourself.** Read the code, docs, glossary and ADRs before you ask anything. Never ask the user for a fact you can look up. If a lookup is slow, hand it to an explorer under the [delegation rules](../pilot/references/delegation.md). Ask the questions that don't need its answer now. If you can't reach a fact, say so and ask for the least you need.
3. **Ask the frontier.** The frontier is every open decision whose prerequisites are settled. Ask all of it in one round. If a question depends on another open question, list it under "Waits on Qn" for a later round. Number each question and give your recommended answer.

   ```text
   Q1. Should we <your recommended answer>?
   Recommendation: <answer>, because <main trade-off>.
   ```

4. **Stop.** End your turn after the round and wait for the answers.
5. **Record and recompute.** Record each answer, with its reason, in the task brief. If an answer is unclear, keep the question open. If it contradicts an earlier answer or the evidence, say so in the next round. When a term or a hard-to-reverse decision settles, call the Skill tool with "domain-modeling" ([domain-modeling](../domain-modeling/SKILL.md)) to record it now. If the work is read-only, return the proposed text and its file instead. Then recompute the frontier and ask the next round.
6. **Finish.** When the frontier is empty, summarise the decisions, reasons, assumptions, what was deferred and how success will be checked. Ask the user to confirm you share the same understanding. Don't act on the plan until they do.

If a caller sent you, return the decisions and the paths of any records you saved.
