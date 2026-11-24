# How Pilot works

Pilot helps turn an idea into an inspectable, agreed outcome, then carries authorised work through design, delivery and verification. One owner works directly or brings in domain specialists. You can stop at research, a design, local changes or a PR.

```text
Human request + constraints + delivery boundary
                      |
               Pilot owns the task
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

An unresolved consequential decision or required visual review pauses the whole task for your answer. Agreement does not require a checkpoint for every routine step. The [execution contract](../../skills/pilot/references/execution.md) owns that distinction, handoffs and completion; [Delegation](../../skills/pilot/references/delegation.md) owns delegation and review context.

## Expertise without mandatory agent chains

The selected playbook sets the procedure and the [effort rubric](../../skills/pilot/references/effort.md) sizes the work. Product owns behaviour, Interaction Design interactions, Solution the approach, Architect the implementation design and Implement the edits. Pilot applies these itself or delegates when it needs expertise, parallel work or a clean context. Specialists return their results to the task's owner.

The [continuity brief](../../skills/pilot/references/task-continuity.md) holds the original intent, decisions, sizing, requirements and proof, so the owner can reload it after a context reset. [Swarm](../../skills/swarm/SKILL.md) and [Arena](../../skills/arena/SKILL.md) are there for parallel work and comparisons; ordinary delivery needs neither. The [system map](skill-system.md) records every owner and source.

## Verification and correction

Retained implementation needs a fresh agent that didn't edit it to inspect the combined diff and run the affected project checks, under [Engineering Verification](../../skills/pilot/references/engineering-verification.md). Development checks find defects but don't count as that verification. Review findings and runtime observations stay separate: an API check doesn't prove an unexercised UI. The owner fixes material issues and gets the corrected work verified again before calling it done.

The narrow [owner-presentation exception](../../skills/pilot/references/verification-contract.md#owner-presentation-eligibility) lets the owner check prescribed low-impact appearance edits itself, labelled owner-checked. Research and design keep their sources, reasoning and limits instead of claiming executable proof.

## Local work

Work happens in the current checkout, or in one task worktree reused across correction rounds. Worktrees don't isolate ports, databases or external services. [Local execution](../../skills/pilot/references/local-execution.md) owns workspaces, cleanup and checking that the tested artifact is the delivered one.

## Evidence and human review

Evidence goes in the project's existing task and PR records: the request, agreed expectations, what was tested, who verified it, what was observed and the limits. The [project evidence contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns how long it's kept. This library doesn't authenticate people, sandbox processes, intercept tools or enforce acceptance. The optional [Codex adapter](../ops/codex.md#durable-orchestration-hooks) adds recovery and recorded completion checks once you set it up; other hosts rely on the instructions alone.

Completion reconciles the original request and every later correction. It's a delivery assessment, not your approval to commit, merge or release. The final report gives the result, evidence and remaining limits at the boundary you asked for.
