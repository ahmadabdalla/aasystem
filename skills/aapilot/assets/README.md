# Harness adapter boundary

The [continuity procedure](../references/task-continuity.md) owns portable task
policy. Adapters translate host protocols; they add no coordinator or delivery policy.

## Folder contract

Use `assets/<harness>/` for each delivered integration's setup, supported versions
and surfaces, configuration, protocol translation and resources. The current
[Codex folder](codex/README.md) holds its guide; the executable remains at
[`scripts/orchestration.py`](../scripts/orchestration.py) for command compatibility.

Each adapter owns:

- Explicit invocation, raw request and correction capture.
- Session/workspace/parent-worker identity and harness-specific state namespacing.
- Lifecycle inputs and accessible recovery/handoff context.
- Host outputs for completion, truthful pause, bounded continuation and visible failure.
- Reviewable configuration, installation, trust and availability; no self-activation.

Share persistence, revision, evidence and completion invariants through the
smallest extraction a verified second integration needs. Keep host invocation
syntax out of shared record-validity rules and link portable instructions.

This folder contract supplies no dynamic loader or stable shared runtime API.
The current helper combines state/check logic and Codex protocol handling;
separating them requires implementation and proof with the second integration.
Adding a folder must not register or trust hooks automatically.

## Consumer data lifecycle

Inventory adapter state, output and plugin-directed agent files/context separately
from caller-owned proof and native host transcripts/caches. Reuse existing task
records; avoid per-event logs, revision archives and duplicate evidence. Follow
the [evidence lifecycle](../../bootstrap-verification/references/project-contract.md#evidence-and-retention)
for review retention and retirement.

Acceptance must measure repeated-intent growth, normal/failure teardown and
interrupted-write recovery. Document retention and manual recovery. Housekeeping
must preserve active work and pending review; age/prefix sweeps or OS expiry are
insufficient.

The [Codex lifecycle](codex/README.md#storage-and-retention) uses temporary session
bindings, checked handoff and exact-owned retirement, with next-use recovery.
It keeps no completed-intent archive. Uncertain ownership/proof preserves named
state. There is no hard cap, background collector or cleanup while nothing runs;
active inputs, added host context and review proof still consume space.

## Delivery gate

Deliver and verify an integration in its actual target host before retaining
adapter code, placeholder folders, manifest registration or support claims.
Until then, keep it a proposal. Claude Code and GitHub Copilot currently use
portable instructions without mechanical adapters.

Establish the exact host version/surface, capabilities, durable state and runnable
native checks. Verify actual invocation/corrections, supported recovery/compaction
and worker handoffs, completion rejection, truthful pauses, bounded retries,
stale evidence and unavailable state/configuration. Inspect received context and
visible failures. Missing required native proof blocks delivery; another host or
generated JSON cannot substitute. Local CLI proof does not establish cloud/IDE support.

Use [independent verification](../references/engineering-verification.md). Report
tested capabilities and limits; the [Codex guide](codex/README.md#stop-behavior-and-limits)
also requires host observation. Its presence does not prove every installed
host's lifecycle behavior. Ordinary invocation remains instruction-driven without
a verified mechanical integration.
