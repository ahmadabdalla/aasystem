---
name: product
description: Discover product structure and user journeys, or define behaviour, business rules and acceptance scenarios. Use when behaviour is missing, ambiguous or changing.
---

# Product

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

You decide what the product should do, not how to build it. If the task is to explore who uses a product and how, follow [Discovery](references/discovery.md) instead.

**What the code does isn't a requirement until someone agrees to it.** If code breaks an agreed rule, report the code; never weaken the rule.

## Steps

1. **Ground.** Read the existing specs, glossary and ADRs. Keep agreed behaviour. Call the Skill tool with "how" ([how](../how/SKILL.md)) for how it works now.
2. **Define** the actors, what each wants, the journeys, business rules, invariants and non-goals. Give each rule a given/when/then scenario with its side effects, plus the failure, retry, concurrency and recovery cases that could break it.
   - If someone is responsible for a step, don't assume the product needs a feature for it.
   - If a replacement drops a feature, say how people will do that work.
   - Slice delivery by journeys a user can finish, not by component.
   - When rewording a requirement, keep who must act, whether it's allowed or required, and the conditions.
3. **Challenge.** For each journey, check who sets up what it needs. If work is left unfinished, who picks it up, how do they find it, and what do they do next? Look for missing outcomes, contradictory rules and terms two people could read differently. For an unclear term, call the Skill tool with "domain-modeling" ([domain-modeling](../domain-modeling/SKILL.md)). When evidence could settle an assumption, call the Skill tool with "probe" ([probe](../probe/SKILL.md)). For a contested contract, call the Skill tool with "interrogate" ([interrogate](../interrogate/SKILL.md)).
4. **Decide.** Label every rule agreed (with its source), proposed default, assumption or open. If any rule isn't agreed, call the Skill tool with "grill-me" ([grill-me](../grill-me/SKILL.md)) with the draft and those rules. Don't ask them yourself. If a rule looks hard to build, send it to the caller with the tradeoff, and keep it until the user decides.
5. **Record** one behaviour contract, with its labels and open decisions, in the project's spec format and location.

Return the contract, open decisions and next step. If it's user-facing, the caller passes it to [Interaction Design](../interaction-design/SKILL.md).
