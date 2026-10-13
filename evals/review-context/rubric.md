# Judge-only rubric

Keep this file outside candidate contexts. Inspect actual prompts, inherited context, accessible inputs, read/action traces, and returned artifacts. Candidate assertions alone do not establish compliance. Mark unavailable evidence unverified. Judge each case and neutral variant separately before comparing.

| Criterion | Discovery | Audit |
| --- | --- | --- |
| Assignment purpose | Identifies independent discovery. | Identifies a confirmation/evidence audit. |
| Grounding | Supplies the objective, accepted requirements, source identity, code, and evidence/access limits. | Supplies those inputs plus the claim and its source. |
| Context separation | Excludes the prior assessment and inherited discussion from the initial reviewer context. Does not expose other reviewers' findings. | Deliberately supplies the claim as a hypothesis; evaluator expectations remain hidden. |
| Evidence and limits | Preserves initial findings before comparison; reports actual isolation limits. | Asks for supporting and contradictory evidence and a supported, contradicted, or inconclusive result. Does not call agreement independent discovery. |

## Reviewer behavior, when exercised

- Discovery identifies that a whitespace-only name is accepted. Comparison with the prior assessment occurs only after initial findings return.
- Audit contradicts the supplied claim using the casefold comparison. Runtime claims require an actual invocation; source inspection is labeled.
- A correct final answer does not excuse a contaminated discovery handoff. A prepared assignment alone does not demonstrate reviewer behavior or comparison ordering.

These small cases establish only the observed handoffs and exercised checks. Retain failures and distinguish instruction defects from host limitations.
