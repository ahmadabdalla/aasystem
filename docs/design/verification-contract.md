# How Aapilot works

Aapilot helps turn an idea into an inspectable, agreed outcome, then carries authorised work through design, delivery and verification. One owner works directly or brings in domain specialists. You can stop at research, a design, local changes or a PR.

```text
Human request + constraints + delivery boundary
                      |
               Aapilot owns the task
                      |
          Replay / investigate / clarify
                      |
       Inspectable proposal when decisions need it
                      |
           Design / implement / research
                      |
            Independent assessment
                      |
             +--------+--------+
             |                 |
       Issues / decisions    Satisfied
             |                 |
       Correct / ask you       v
             +--------> Result + evidence + limits
                               |
                         Human review
```

An unresolved consequential decision or required visual review pauses the whole task for your answer. Agreement does not require a checkpoint for every routine step. The [execution contract](../../skills/aapilot/references/execution.md) owns that distinction, handoffs, delegation and completion.

## Expertise without mandatory agent chains

The [effort rubric](../../skills/aapilot/references/effort.md) sets S/M/L execution conditions, carried through assignments under the shared [handoff rules](../../skills/aapilot/references/execution.md#ownership-and-handoffs).

The selected playbook provides the procedure. Product owns behaviour and acceptance scenarios; Interaction Design owns interactions; Solution compares approaches; Architect designs implementation boundaries; Implement makes bounded edits. Aapilot can apply these procedures itself or delegate for useful expertise, parallel work or context separation.

The [continuity loop](../../skills/aapilot/references/task-continuity.md) keeps one
retrievable brief: original intent, decisions, sizing, requirements and proof.
The owner reloads it before stages and after context resets, selects needed work,
checks results and resolves findings. Changed scope/proof needs trigger reassessment;
research, design and implementation retain their own routes and stopping boundaries.

Specialists return bounded artifacts and observations to the existing owner. [Swarm](../../skills/swarm/SKILL.md) partitions independent work; [Arena](../../skills/arena/SKILL.md) compares alternatives with separate judging. Neither is mandatory for ordinary delivery. The [system map](skill-system.md) records the complete ownership and source inventory.

## Verification and correction

Retained implementation normally requires a fresh noneditor to inspect the combined diff and execute affected project checks under [Engineering Verification](../../skills/aapilot/references/engineering-verification.md). Development checks help find defects but do not establish independent verification. Review findings and runtime observations remain distinct; an API check does not prove an unexercised UI.

The verifier receives requirements, constraints and runnable procedures. Independent discovery withholds prior conclusions until initial findings; a confirmation audit can check supplied claims with that exposure disclosed. Preserve original findings. The owner resolves material issues and obtains affected verification on the corrected work before declaring completion.

The narrow [owner-presentation exception](../../skills/aapilot/references/execution.md#owner-presentation-eligibility) allows prescribed low-impact appearance edits with diff/preview checks. Label them owner-checked. Research and design retain sources, reasoning and limits rather than pretending to have executable product proof.

## Persistent local work

Use the current checkout for sequential work, or one task worktree for useful separation. Reuse it across correction rounds. Pause source editing during verification, identify required configuration and other runtime inputs, and check tested identity before/after verification and at delivery.

The [input identity helper](../../skills/aapilot/scripts/input_identity.py) is a read-only fallback when project facilities are insufficient. It hashes selected working-tree inputs without copying them. It detects endpoint differences, not arbitrary concurrent or transient writes. Complete input scope, actual runtime identity and stopping other writers remain owner/verifier responsibilities.

Separate worktrees do not isolate ports, databases or external services. Use owned fixtures or serial execution for those resources. Additional execution copies need a specific check requirement and known cost/ownership; full repository archives are not the default.

## Evidence and human review

Reuse project task/PR records for the request, agreed expectations, tested identity, actual verifier, observed checks, findings and limitations. Deterministic project checks and identity comparisons support the process; this library does not authenticate people, sandbox processes, intercept tools or provide host-enforced acceptance.

The optional [local Codex adapter](../ops/codex.md#durable-orchestration-hooks)
adds recovery and recorded completion checks after explicit setup/trust. Checked
handoff preserves the task before retiring scratch; resume retains intent identity
and requires owner reconstruction. These checks do not establish semantic
fulfillment or reviewer independence. Other hosts and ordinary invocation remain
instruction-driven. Completion reconciles the original request and all later steering.

Clean up only owned processes and disposable output. Preserve pending changes and useful evidence through review or investigation. After the review boundary, retire unneeded artifacts without breaking durable evidence references. The [project evidence contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns lifetime rules.

Agent completion is a delivery assessment, not your approval to commit, merge or release. The final report gives the result, evidence and remaining limitations at your requested boundary.
