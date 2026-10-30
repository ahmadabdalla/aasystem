# Module design review

Assess selected existing code using the shared [boundary criteria](boundaries.md).
Add [local-code criteria](local-code.md) when reader burden within an owner matters.
Preserve the caller's review-only boundary; this procedure does not authorize
edits, product workflow execution, or shared-state changes. Inspect tests by
default; execute checks only within the caller's authorized scope.

## Select the scope

- For a named module, inspect that module and the callers and dependencies needed
  to understand its contract.
- For a named workflow, trace one entry point through the responsible modules.
- For a project assessment, select up to three representative workflows. Explain
  the selection using observable usage, ownership, or change risk; label selection
  assumptions when those signals are unavailable.
- For unclear scope, choose a bounded scope supported by the request and state it.

Reuse the caller's settled scope and constraints. State the reviewed revision and
relevant uncommitted inputs. Sampling does not establish a whole-project verdict.

## Collect evidence

For each selected module or workflow:

1. Identify the relevant entry point, public contract, implementation, callers,
   dependencies, and tests. Trace one concrete behavior: where its rules are
   defined, called, and checked. Mark missing or inaccessible evidence explicitly.
2. Select one plausible change to that behavior, grounded in the request or the
   observed contract. Label it **hypothetical**. List the owners that would change,
   why each would change, and which callers could remain unchanged.
3. Deepen inspection where a conclusion depends on it; do not inventory every
   module in the project. Cite file paths and line numbers for material claims.

A hypothetical edit list establishes an expected change burden, not an observed
runtime failure. Apply the [bounded-finding contract](../SKILL.md#return-a-bounded-assessment)
to distinguish demonstrated structural burden, behavioral defects, unresolved
risks, and preferences. A structural finding need not involve incorrect output.

## Assess the dimensions

Use these lenses to organize the shared boundary criteria, keeping the underlying
criteria in their owning reference:

| Dimension | Evidence to trace using the boundary criteria |
| --- | --- |
| Depth | Knowledge hidden by the module and obligations its callers still coordinate |
| Interface | Inputs, outputs, failure meaning, effects, lifetime, and compatibility expectations visible to callers |
| Locality | Ownership of the selected rule and coordinated edits required by the hypothetical change |
| Leverage | Rule or setup duplication avoided by the boundary, weighed against the coupling introduced by sharing |
| Seams | Existing control points through which the selected behavior can be tested or varied, including setup and cleanup |

For leverage, assess legitimate present usage; one caller is not a weakness by
itself, and hypothetical future callers do not justify generalization. For seams,
observe how dependencies are actually supplied or controlled; an interface alone
does not establish replacement capability. Count touched owners only with their
reasons: justified coordination or migration is not automatically poor locality.

### Optional scores

Use qualitative assessments by default. If the user or caller requests scores,
score each dimension from 1 to 5, or use **not assessed** when evidence is
insufficient. Include supporting evidence and its limits beside each score.

| Score | Meaning within the selected scope |
| --- | --- |
| 1 | Multiple concrete examples of substantial friction |
| 2 | One or more significant, evidenced obstacles |
| 3 | Strengths and obstacles both supported by evidence |
| 4 | Evidence supports the dimension; limitations remain |
| 5 | Evidence supports the dimension across multiple representative cases, including inspection of how those cases are checked |

A single positive example does not justify a 5. Scores are scoped judgments,
not calibrated comparisons between projects. Do not use file length, test count,
or interface-to-implementation size as a score. Test inspection supports claims
about available checks; execution supports only the behavior actually exercised.
Neither alone proves broad maintainability, and execution is not required to
raise a score.

## Report

Use the caller's working record or conversation and preserve its format. Include:

1. **Scope:** What was reviewed, selection reasons, revision, and relevant dirty
   inputs.
2. **Assessment:** Each dimension's conclusion (and score when requested), file
   evidence, and implication for a maintainer. Mark unsupported dimensions not
   assessed. Material findings follow the linked bounded-finding contract.
3. **Change trace:** The hypothetical change, owners touched, and reasons.
4. **Priority:** Up to three investigations or improvements, each with expected
   benefit and risk or tradeoff. An empty recommendation list is valid.
5. **Limits:** What was not inspected; tests inspected versus executed, actual
   commands and outcomes when run; and the scope to which conclusions apply.

Do not calculate an overall project score from a limited sample. If explicitly
requested, label it provisional and explain its evidence limits.
