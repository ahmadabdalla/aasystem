# Codify personal judgment

Use this when reflection finds a transferable preference between viable choices, or the user asks to capture or revise one. First check whether an existing procedure, principle, or project mechanism already owns the decision.

## Establish what is authorized

- **Stated judgment:** a clearly expressed general preference can be captured within its stated scope when the request authorizes it. Recurrence is not required. Keep unknown rationale unknown; review any expanded scope or inferred rationale before adopting it.
- **Inferred judgment:** choices across distinct situations can support a candidate. Inspect contrary choices and constraints that might explain the pattern. Confirm the proposed interpretation with the user before activation unless they have already approved it. Silence, agent repetition, and synthetic tests do not establish endorsement.

Use a current working record or `reviews/<date>/judgment/` for the source statement or scoped transcript pointer, the decision and tradeoff, your interpretation, scope, counterexample, observed outcome or its absence, proposed change, and adoption status. Record enough evidence to review the interpretation without copying unrelated conversation. Candidate records are evidence, not operating instructions.

## Write and connect the principle

Follow the environment's skill-authoring instructions when available. Store an approved leaf at `principle-<name>/SKILL.md` beside the workflow skills. Give it a discriminating description, a decision preference, rationale, and limits. Include an example only where it clarifies the choice. Keep source history and evaluation reports in the review record. Use `disable-model-invocation: true` for the leaf and, when this toolbox carries Codex adapters, add `agents/openai.yaml` with `policy.allow_implicit_invocation: false`. The index owns deliberate selection of relevant principles.

Update the [approved-principle index](../../principles/INDEX.md) with its situation trigger, relevant workflow, and relative leaf link in the same change. The index routes to the leaf; it should not restate its instructions. aasystem, solution, architect, and figure-it-out consume the index. Check the affected path when another workflow also needs deliberate activation.

A principle can guide the choice of a project mechanism while that mechanism enforces a concrete property. Keep those responsibilities distinct. Avoid a new principle that merely repeats an existing procedure.

## Check meaning and use

The user's statement or confirmation establishes fidelity to their judgment. Test activation separately with an ordinary matching request, a meaningful exception, and any affected handoff into a fresh context. Include a different domain when claiming transfer. Compare against the previous workflow where useful. Examine the actual choice and its rationale; mentioning a principle does not demonstrate application.

Validate skill structure and links. Software produced under a principle still needs project verification. A successful replay neither proves that the principle is universally useful nor supplies missing user endorsement.

On later feedback or contrary outcomes, propose a scoped revision, merge, or retirement. Update the index and affected references together, preserving the reason in the review record. A project-specific exception need not change the portable preference. Apply changes within existing authorization; if confirmation is needed, ask one question and wait.
