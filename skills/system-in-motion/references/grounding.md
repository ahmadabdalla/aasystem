# Ground the explanation

Read project instructions, overview, runtime declarations and the entry points,
handlers, state models and tests relevant to the chosen journey. Follow dependencies
when a claim needs them; a file inventory alone is not evidence of behavior.

## Choose the slice

Identify who acts, their goal and interaction surface, what initiates work, the
business outcome, and how completion becomes visible. Prefer request-to-outcome
context over an exhaustive component tour. Include a failure, decision or delay
when it changes understanding; split unrelated journeys rather than crowding one map.

## Settle the brief with safe defaults

Reuse the request, project evidence and settled answers first. These are five
coverage areas, not five compulsory questions. For unspecified preferences, use:

| Area | Safe default |
| --- | --- |
| Audience and takeaway | A newcomer spanning product and engineering; understand the outcome and how it happens |
| Journey | One representative source-backed path from trigger to observable outcome |
| Current or proposed | Explain what sources support, distinguishing implementation, proposals and unknowns; never assume deployment |
| Emphasis | The core decision, meaningful failure and independent handoffs needed to understand that path |
| Presentation | Existing project styling if evidenced, otherwise the [white-slide palette](presentation.md#default-palette); readable pacing at the laptop sizes in SKILL.md, with no target scene count |

State the chosen journey and consequential defaults briefly, then proceed without
an interview or extra approval. A complete brief, fictional specification or request
to use judgment can take this path. Defaults fill preferences, never missing system
facts: preserve unknown technology, transport or behavior instead of inventing it.
Do not turn the coverage areas into five new sections or records.

Ask only when an unresolved choice materially changes the requested explanation
and cannot be safely defaulted—for example, a requested current/future comparison
whose future target is unspecified. Ask one focused question for one gap. For
several consequential choices, invoke `$aasystem:grill-me` when available with the
request, evidence, settled/defaulted answers and remaining choices. Delegate only
the bounded explanation brief; use its Grilling procedure for question rounds and
confirmation rather than copying it here. Its return stays in the existing brief; system-in-motion
retains the build and verification. If unavailable, ask the necessary questions
directly. An explicit request for an interview follows that request. Once choices
are settled, reuse their confirmation; do not restart the intake before building.

## Evidence and claims

Keep one ledger in the model's `sources`: retrievable file/line, document section
or permitted URL locators, referenced by components, exchanges and scenes.

| Claim | Support |
| --- | --- |
| Implemented | Reachable code/configuration; tests clarify behavior |
| Planned | Proposal or unimplemented specification |
| Inferred | Partial evidence plus an explicit rationale |
| Unknown | Missing or conflicting evidence and its consequence |

A dependency declaration does not prove participation; a TODO is not implementation;
tests do not prove a running deployment. Support the meaning of each claim, not just
a matching noun. Resolve material contradictions or preserve them explicitly.

## Initiation and observation

Trace each exchange's initiator, recipient, payload/outcome and trigger. Timer,
operator, queue delivery and external callback are distinct initiators. A worker
can change storage without updating a browser; inspect the actual read/response/push
path before showing new actor-visible facts. `observe` denotes a non-calling
relationship, not a concealed causal request. Keep off-map triggers explicit.

Reconstruct a UI only when evidenced, labeling it a simulation. An API may show
request/status/body; a CLI command/output; an event-only service event/outcome.
Do not fabricate a product screen to fill the Experience view.

Use synthetic values where private data is unnecessary. Public examples must be
wholly fictional and portable, without secrets or private project, organization,
account or person identifiers. The bundled equipment journey supplies no evidence
for another project.
