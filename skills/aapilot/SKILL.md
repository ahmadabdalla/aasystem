---
name: aapilot
description: Coordinate an engineering task through a selected playbook, supporting skills, and evidence of completion. Use for product discovery and definition, investigations, bug fixes, features, refactoring, prototypes, and skill work; supporting skills remain available directly.
disable-model-invocation: true
---

# aapilot

Before starting, read the [shared execution contract](references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own framing through verification. Select the procedure, coordinate contributors, inspect results and explain the outcome. Consolidate results under the execution contract's ownership and retention rules.

## Select the path

Read the request, project instructions and task evidence. State the outcome, consequential assumptions and selected path. Inspect observable unknowns. Ask one focused question only for a material choice you cannot reasonably infer; then stop and wait. Preserve plan-only, research-only and explicit checkpoints.

Apply relevant [principle leaves](../principles/INDEX.md); carry their scope and exceptions with the brief. Borrowed workflow requirements do not establish personal preferences.

| Task                                                                                                                  | Procedure                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Discover product structure, people and journeys, or define product behavior, business rules, and acceptance scenarios | [Product](../product/SKILL.md)                                                                                             |
| Translate product outcomes into navigation, interactions, information visibility, and justified UI choices            | [Interaction design](../interaction-design/SKILL.md)                                                                       |
| Interview the user to resolve consequential choices in a plan                                                         | [Grill me](../grill-me/SKILL.md)                                                                                           |
| Clarify project terminology or record a consequential product, design or software decision                            | [Domain modeling](../domain-modeling/SKILL.md)                                                                             |
| Explain current behavior or investigate a question without changing the product                                       | [Investigation](playbooks/investigation.md)                                                                                |
| Decide what solution should exist while direction, ownership, or constraints remain open                              | [Solution](../solution/SKILL.md)                                                                                           |
| Correct a reported defect                                                                                             | [Bug fix](playbooks/bug-fix.md)                                                                                            |
| Add or intentionally change behavior                                                                                  | [Feature](playbooks/feature.md)                                                                                            |
| Change structure while preserving behavior                                                                            | [Refactoring](playbooks/refactoring.md)                                                                                    |
| Refine an inspectable UI/UX with human feedback and preserve a reviewed visual reference                              | [UI refinement](../ui-refinement/SKILL.md)                                                                                 |
| Resolve a decision through a throwaway experiment                                                                     | [Prototype](playbooks/prototype.md)                                                                                        |
| Create or change a skill                                                                                              | [Skill authoring](playbooks/authoring-a-skill.md)                                                                          |
| Assess whether an instruction or skill change improves behavior                                                       | [Evaluation](playbooks/eval.md)                                                                                            |
| Deliver an authorized repository change as a pull request                                                             | [Opening a PR](playbooks/opening-a-pr.md)                                                                                  |
| Establish or audit project verification                                                                               | [Bootstrap verification](../bootstrap-verification/SKILL.md) or [maintain verification](../maintain-verification/SKILL.md) |
| Capture learning or a stated judgment                                                                                 | [Reflect](../reflect/SKILL.md)                                                                                             |
| No bundled procedure fits, or a change spans several coupled phases                                                   | [Figure it out](../figure-it-out/SKILL.md)                                                                                 |

For production delivery needing UI refinement, select Feature with a supporting UI Refinement assignment. Design/prototype-only requests can route directly to UI Refinement.

Read the selected procedure in full. For OpenSpec projects, follow the [OpenSpec reference](references/openspec.md). Keep one implementation task list: reuse the active change's list, retaining playbook steps as headings or untracked notes. Otherwise copy numbered steps into the checklist before task-specific details. Keep inapplicable steps with reasons. For saved steps, rebase links or link the source procedure with plain step labels; validate links from the saved location. Direct skill routes use that skill's phases. Include applicable closing assignments under the [completion rules](references/execution.md#completion) before execution starts. Keep coupled tasks with one owner. Identify defects discovered during refactoring as separate bug-fix tasks; empirical unknowns may use bounded prototypes. Update the route when evidence changes the task, retaining completed grounding.

Dedicated procedures for performance tuning, hillclimbing, forensics, general-purpose visual parity, PR babysitting, shipping, unattended programs, session recovery and worktree cleanup are not bundled. Disclose that limit. Use figure-it-out only for a bounded, credible procedure within the request; otherwise name the missing capability. Generic procedures do not establish specialized coverage.

## Coordinate and finish

When the user explicitly requests bounded autonomous work or the bounded-autonomy PoC, follow [Bounded work](references/bounded-work.md) alongside the selected procedure. It adds shared work receipts for authority, budget, current proof and human checkpoints; the existing owner retains execution and acceptance.

Follow the [delegation procedure](references/execution.md#delegation), including invocation restrictions and unavailable handoffs. The selected playbook owns the task: Architect returns design, [Implement](../implement/SKILL.md) returns production edits and development checks, and a separate worker supplies [acceptance proof](references/execution.md#independent-implementation-verification) when required. Standalone specialist continuations join this same task with settled inputs and requested checkpoints.

For substantial, multi-phase or unattended work, use [show-me-your-work](../show-me-your-work/SKILL.md) from the first consequential decision. The log links detailed solution records, design packages and evidence.

Apply the [completion check](references/execution.md#completion), then report the outcome, consequential choices, proof and limits, and remaining work. Distinguish completed, failed and unverified claims. Research may end with supported or conditional recommendations. Implementation requires observed behavior; blocked or inconclusive proof remains a gap.
