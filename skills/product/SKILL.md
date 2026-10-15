---
name: product
description: Discover product structure and user journeys, then define product behavior, business rules, invariants, and acceptance scenarios. Use for exploratory product definition or missing, ambiguous, or changing behavior; reuse an adequate existing contract.
disable-model-invocation: true
---

# Product

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own product discovery and the product behavior contract for the assigned scope. Return the result to the caller, which retains the larger task. Discovery-only work ends with the documented model, journeys and unresolved questions; a specification request ends with the contract and unresolved decisions.

## Ground

Read the request, existing requirements, relevant glossary and ADRs, and any active change identified by the project instructions or caller. Preserve agreed behavior and reuse sufficient specifications. Distinguish intended behavior from what the implementation currently does; observed behavior alone does not authorize a requirement.

For exploratory product definition or redefinition, follow [Discovery](references/discovery.md), reusing sufficient existing knowledge. For discovery-only work, finish at the requested checkpoint and proceed to Record and hand off; otherwise use the supported outcomes in Define and Challenge.

Use [how](../how/SKILL.md) for existing behavior and [why](../why/SKILL.md) for consequential rationale. On a new product, ground in intended users, real constraints, and available evidence. State material assumptions and inspection limits.

## Define

Distinguish manual prerequisites, product capabilities and later automation; assigning an actor responsibility does not establish a requirement for a product workflow.

When leaving an existing feature out of a replacement product, explain how people will handle the work it supports.

Identify actors, their intended outcomes, main journeys, business rules, and invariants. Include relevant access, state transitions, failure outcomes, and observable quality constraints. Set scope and non-goals; for a new app, select a first usable journey while preserving constraints that apply across the product.

Define each delivery increment by an observable user workflow and delivered prerequisites; it may span capabilities.

Give important requirements a concrete scenario: preconditions, action or event, expected outcome, and consequential side effects. Cover the failure, retry, concurrency, or recovery cases that could break its rules. Keep implementation choices in the technical design. Record the source of agreed requirements; label proposed defaults, assumptions, and unresolved choices separately.

When rewriting, preserve who bears each obligation, whether an action is permitted or required, and its qualifying conditions.

## Challenge

Trace journeys backward to who establishes their prerequisites and forward across roles and later sessions to the owner, discovery path and next action for unfinished work, including after a coordinating request closes.

Check for missing outcomes, contradictory rules, and terms that admit different interpretations. Use [domain-modeling](../domain-modeling/SKILL.md) for consequential ambiguity, [probe](../probe/SKILL.md) when evidence could settle an assumption, and [interrogate](../interrogate/SKILL.md) for contested or consequential contracts.

Resolve consequential choices under [decision authority](../aapilot/references/execution.md#decision-authority). Helpers return findings to this assignment; they do not launch implementation. A technical feasibility concern goes to the caller for solution analysis; retain the affected requirement and tradeoff until its authority is resolved.

## Record and hand off

Follow the project's specification format and assigned artifact paths. Save discovery outcomes in the project's product records or one behavior contract in its specification format, within the authorized document scope and linking canonical terms and decisions. A read-only request returns proposed content. Record intentional changes against existing requirements and their authority; do not weaken a rule to match a failing implementation.

Return the scoped discovery result or behavior contract to the caller, preserving sources and status, material assumptions, unresolved decisions and the next step. For a behavior contract, include requirements, invariants and acceptance scenarios, preserving what the technical owner needs to design enforcement and proof. These are required contents, not mandatory headings or separate files. Review establishes clarity and consistency; implementation remains unverified until exercised.

The caller owns any subsequent [interaction-design](../interaction-design/SKILL.md) assignment, using the returned behavior contract when that phase is in scope. Product retains business meaning; acceptance of a requirement does not accept every presentation derived from it. Use the [decision authority convention](../domain-modeling/references/adr.md) for consequential choices without requiring an ADR for every requirement.
