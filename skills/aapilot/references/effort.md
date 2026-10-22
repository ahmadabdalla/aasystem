# Effort

Briefly inspect the ask, affected behavior, existing evidence and checks before sizing it. Reuse sufficient discovery.

Resolve observable unknowns through investigation. Ask one focused question for a consequential human choice; use [Grill Me](../../grill-me/SKILL.md) for a discovery interview or several interdependent choices needing the user's judgment. Follow the execution contract's [decision authority](execution.md#decision-authority).

## Size the work

| Size | Fits when | Execution conditions |
| --- | --- | --- |
| S | One localized outcome with understood requirements, mechanism and proof. | Work directly where practical; reuse design and checks; keep planning brief. |
| M | One bounded outcome spans components or needs dependency and design decisions. | Establish contracts and proof; sequence dependencies; test consequential integration assumptions early. |
| L | Coupled outcomes or unresolved choices require staged discovery, design or delivery. | Define stages, shared contracts and verifiable increments; maintain one integrated plan. |

Size reflects uncertainty and coupling, not file count alone. Use a provisional size when missing evidence could change it; an undefined scope does not automatically mean L or require an interview.

## Account for consequence

Separately identify consequences such as unauthorized access, privacy exposure, financial error, data loss or service disruption. Name the affected invariants and required scrutiny and proof, using relevant project or specialist criteria.

An S permission fix can require strong security checks. Increase size when addressing the consequence exposes broader work. Size scales planning and coordination; it never waives required procedures, verification or human decisions.

## Carry the approach forward

State the size, reason, scope and execution conditions in the existing brief or scope replay. Include consequence-driven checks and resource needs; create no separate sizing report or routine approval step. Follow [ownership and handoffs](execution.md#ownership-and-handoffs) for inheritance and reassessment.

Follow the existing [local execution rules](verification-contract.md#local-execution) for workspace and resource decisions.
