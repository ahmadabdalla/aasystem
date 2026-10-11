# Logic prototype

Use an interactive state walkthrough when a business model is easier to judge by acting on it than by reading its specification. For layout or navigation alternatives, use [UI prototype](ui-prototype.md).

## Make the question inspectable

Identify the modeled entities, actions, invariants and consequential unknown. Preserve the source and status of supplied rules: a proposed rule may be demonstrated, but running it does not make it accepted. Place the question and material assumptions where the recipient can see them.

Choose the smallest representative fixtures. Include the normal journey, an awkward sequence that distinguishes competing interpretations, and a forbidden transition relevant to the question. Vary actor identities, responsibilities and scopes when the question depends on those distinctions; do not assume each responsibility belongs to a separate person.

## Build a domain-language walkthrough

Prefer a self-contained HTML file that the intended reader can open directly when a local simulation can answer the question. Use a different minimal runnable form when the question depends on a real runtime or integration, and identify what the simulation would miss. Keep business transitions separate from presentation so state changes can be inspected without reading button wiring. A reducer, explicit state machine or small module is sufficient; this separation does not establish production readiness.

Provide:

- A short statement of the question and simulated boundaries.
- The relevant current state in readable domain terms, updated after each action; expose details needed to understand the result without relying on a raw JSON dump.
- Free-play actions and a reset to known fixtures, allowing exploration beyond the scripted order.
- Guided scenarios explaining the situation and what to inspect. Each step must execute the actual action and display its result; starting a scenario resets to its documented initial state.
- Visible explanations of rejected actions and the unchanged state where appropriate. Let the reader inspect a forbidden attempt without silently permitting it or hiding why it fails.

Use labels such as “Return equipment” instead of internal event names. Distinguish the acting person, active responsibility and information scope when they affect the question. Keep diagnostic controls visibly separate from the proposed product interaction. Prefer grouping and labelled controls to repetitive explanatory prose, retaining text that explains restrictions or prevents mistakes.

Keep state in memory unless persistence is itself under investigation. Use clearly identified scratch storage for that case, with reset and cleanup scoped to owned data. Simulated permission checks demonstrate the proposed rules; they do not establish backend enforcement.

## Exercise and interpret

Run each discriminating scenario from reset, checking intermediate states as well as the final result. Try the forbidden action and one meaningful out-of-order sequence. Verify that free play and guided steps use the same transition behavior. Use focused assertions where a subtle model error would invalidate the conclusion; avoid building a production test system for a throwaway question.

Record the action, expected state, actual state and observed rejection or failure. If the demo cannot reliably express the intended rule, repair the harness before interpreting the outcome. Separate a demonstrated transition from an inference about whether that transition matches the business.

Make the file and walkthrough instructions available to the intended reviewer. Incorporate actual feedback when supplied, identifying its source; if the remaining question is a human judgment, return it as unresolved instead of supplying imagined feedback. Return through the [skill's observation and handoff contract](../SKILL.md#observe-and-return).
