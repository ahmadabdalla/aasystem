---
name: aapilot
description: Carry a requested outcome from product ideation through design, engineering delivery, and verification using the relevant procedures. Use for product discovery and definition, investigations, bug fixes, features, refactoring, prototypes, and skill work; supporting skills remain available directly.
disable-model-invocation: true
---

# aapilot

Before starting, read the [shared execution contract](references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own framing through verification: select procedures, coordinate contributors,
inspect results and deliver under the execution contract.

For substantial, multi-stage or delegated work, read and follow
[task continuity](references/task-continuity.md) in full. It owns the durable brief,
increment loop and recovery; an outcome request needs no repeated role assignments.

## Select the path

Read the request, project instructions and evidence. Establish
[scope and proof](references/execution.md#scope-and-proof): reuse an adequate brief
and sizing, or replay and assess new/materially changed scope. Select the relevant
procedures below. Follow [decision authority](references/execution.md#decision-authority);
a replay alone requires no approval. Preserve explicit stopping boundaries.

Apply relevant [principle leaves](../principles/INDEX.md); carry their scope and exceptions with the brief. Borrowed workflow requirements do not establish personal preferences.

| Task                                                                                                                  | Procedure                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Discover product structure, people and journeys, or define product behavior, business rules, and acceptance scenarios | [Product](../product/SKILL.md)                                                                                             |
| Translate product outcomes into navigation, interactions, information visibility, and justified UI choices            | [Interaction design](../interaction-design/SKILL.md)                                                                       |
| Independently assess an existing rendered interface for visual and interaction friction                               | [Interaction Design: independent rendered UX assessment](../interaction-design/SKILL.md#select-the-assignment)             |
| Work through a plan with the user and record agreed terms and decisions when authorized                               | [Grill me](../grill-me/SKILL.md)                                                                                           |
| Clarify project terminology or record a consequential product, design or software decision                            | [Domain modeling](../domain-modeling/SKILL.md)                                                                             |
| Explain current behavior or investigate a question without changing the product                                       | [Investigation](playbooks/investigation.md)                                                                                |
| Decide what solution should exist while direction, ownership, or constraints remain open                              | [Solution](../solution/SKILL.md)                                                                                           |
| Assess how a decision or design holds up under plausible growth                                                       | [10x](../10x/SKILL.md)                                                                                                     |
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

For production delivery needing UI refinement, select Feature with supporting UI Refinement scope. Design/prototype-only requests can route directly to UI Refinement.

Within an assigned continuation, preserve the caller's scope and [task ownership](references/execution.md#ownership-and-handoffs); selecting a playbook does not start another coordinator.

Read the selected procedure in full and use its applicable steps. For OpenSpec projects, follow the [OpenSpec reference](references/openspec.md). Keep one task list for substantial work, reusing the active change's list and durable brief; do not copy full playbooks into it. Choose specialist work and proof at the assessed scale; reuse settled Product, interaction and architecture inputs. Keep coupled tasks with one owner and revise the route when evidence changes the task. A prescribed [eligible presentation edit](references/execution.md#owner-presentation-eligibility) needs only its relevant checks.

For authorized unattended work in a supported active session, apply [bounded autonomy](references/execution.md#bounded-autonomy). Dedicated procedures for performance tuning, hillclimbing, forensics, general-purpose visual parity, PR babysitting, shipping, scheduling, persistent unattended programs, session recovery and worktree cleanup are not bundled. Disclose that limit. Use figure-it-out only for a bounded, credible procedure within the request; otherwise name the missing capability. Generic procedures do not establish specialized coverage.

## Coordinate and finish

For retained implementation, follow the [verification contract](references/verification-contract.md): identify the work, obtain required independent checks, resolve findings and present the result. Research and design stop at their requested outputs.

Follow the [delegation procedure](references/execution.md#delegation), including invocation restrictions and unavailable handoffs. The selected playbook owns the task: Architect supplies design, [Implement](../implement/SKILL.md) supplies production edits and development checks, and a separate worker supplies [acceptance proof](references/execution.md#independent-implementation-verification) when required. Standalone specialist continuations join this same task with settled inputs and requested checkpoints.

Apply the [completion check](references/execution.md#completion), retaining decisions
and evidence in existing records. Use [Show Me Your Work](../show-me-your-work/SKILL.md)
when a later reviewer needs the trail. Report the outcome, consequential choices,
proof, limits and remaining work; distinguish completed, failed and unverified claims.
