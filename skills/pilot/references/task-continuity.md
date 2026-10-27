# Task continuity and incremental orchestration

Preserve intent through delivery and recovery. Use the [effort rubric](effort.md)
for sizing, the [entry skill](../SKILL.md#select-the-path) for routing, and the
[execution contract](execution.md) for authority, handoffs, proof and stopping
conditions. No fixed specialist chain or extra approval step is required.

## Preserve the task

Before substantial, multi-stage or delegated work, keep one durable brief in the
project's existing task record. Link authoritative inputs instead of copying
them or keeping an action log. Conversation can suffice for a short S task in one
context; persist it before a handoff or reset makes that inadequate. Preserve
project formats and read-only scope; use an owned external location when needed.

Keep these inputs retrievable:

- Original request, outcome, constraints and stopping boundary.
- User decisions and corrections, their sources and standing; separate proposals
  from agreements.
- S/M/L rationale, consequence-driven checks, principles and exceptions.
- Selected procedures, dependencies, current increment and expected results.
- Task-wide requirements, evidence/gaps, material findings and deferred findings
  with reasons and return checkpoints.
- Status, next action, artifact identity and owned resources.

Update this record as steering or evidence changes. Preserve original intent and
decision history; summaries and worker returns cannot override user constraints.
Recover inaccessible inputs or expose the affected gap before dependent work.

Give each intent its own identity and stopping boundary. A session can hold
several intents; an intent can resume elsewhere. Reconcile corrections with the
current intent. Before switching to independent work, checkpoint or hand off the
previous intent; another invocation must not replace unfinished work. Clarify
scope ambiguity when it changes that choice.

## Choose and execute the next increment

1. **Reload and size.** Use the current brief and applicable rules; reload missing
   or changed inputs. Reconcile new findings. Reassess size when uncertainty,
   coupling, consequence or proof needs change; otherwise inherit it.
2. **Select needed work.** Reuse capabilities and settled inputs. Missing product
   meaning or acceptance scenarios calls for Product; unsettled interactions for
   Interaction Design or UI Refinement; changed implementation boundaries for
   Architect. Investigations, experiments and skill work retain their procedures.
   Keep S work brief; sequence L work into verifiable increments.
3. **Bound assignments.** Follow [handoff requirements](execution.md#ownership-and-handoffs).
   Specialists join this task and return to its owner; they do not restart global
   coordination or edit shared coordination state. Delegate only when useful or
   required and supported by the host.
4. **Inspect and prove.** Compare artifacts and observations with the original
   requirements and current increment. Apply the selected procedure's proof,
   including real journeys/persisted effects and independent verification where
   required. A worker's completion message, populated record or build is insufficient.
5. **Resolve and continue.** Correct material findings and recheck affected proof
   before dependent expansion. Update coverage, evidence identity, deferred
   checkpoints and next action. Continue authorized work without repeated role
   assignments; pause for unresolved human decisions under the execution contract.

Honor research-only and design-only boundaries. Blocked prerequisites and human
decisions permit truthful pauses, not completion claims.

## Recover and finish

After compaction, interruption or owner handoff, reread the brief, original
request, latest steering and relevant procedure. Inspect actual artifacts and
owned processes; cancelled workers may leave processes running. Reconcile stale
proof and unsettled inputs before resuming. Workers reload their bounded assignment.

At the requested boundary, reconcile **every original requirement and subsequent
correction** with the result, evidence or explicit gap. Check identity, findings,
authority and affected documentation under the [completion rules](execution.md#completion).
Finishing the last increment alone does not finish the task.

Use one owned temporary area for disposable coordination and verification output,
including plugin-directed agent files. Before retirement, stop/reconcile workers,
retain intent and necessary proof in the authorized record, and verify both are
readable without scratch. Delete only known disposable contents. Failed handoffs
preserve recoverable state and an explicit gap. Pending review evidence and native
harness transcripts retain their existing owners and lifetimes.

## Optional mechanical support

The [local Codex adapter](../assets/codex/README.md) adds context restoration and
recorded completion checks after separate setup and trust. Unavailable or
untrusted hooks leave orchestration instruction-driven; retain the portable brief
and disclose the limit. Checks do not choose obligations, authenticate approvals
or reviewers, prove semantic correctness, or intercept every stage transition.
