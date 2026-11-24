# Harness adapter boundary

Adapters translate a host's protocol. The [continuity procedure](../references/task-continuity.md) owns task policy; an adapter adds no coordinator or delivery rules.

## Folder contract

Put each delivered integration in `assets/<harness>/`: setup, supported versions and surfaces, configuration and protocol translation. The [Codex folder](codex/README.md) holds its guide; its helper stays at [`scripts/orchestration.py`](../scripts/orchestration.py) so existing commands keep working.

Each adapter owns:

- Explicit invocation and capturing the raw request and corrections.
- Session, workspace and parent-worker identity, and namespacing its own state.
- Lifecycle inputs and the context needed for recovery and handoff.
- What the host shows for completion, a truthful pause, a bounded retry and a failure.
- Reviewable configuration, installation and trust. An adapter never activates itself.

If a second verified integration needs the same persistence, revision, evidence or completion rules, extract only what both need. Keep host invocation syntax out of shared rules. There is no shared runtime API yet: `orchestration.py` mixes state checks and Codex protocol. Split them only alongside a verified second integration. Adding a folder must not register or trust hooks.

## Consumer data lifecycle

Document adapter state and plugin-directed agent files separately from the caller's proof and the host's own transcripts and caches. Reuse existing task records instead of adding event logs, revision archives or copied evidence. Follow the [evidence lifecycle](../../bootstrap-verification/references/project-contract.md#evidence-and-retention) for review retention.

Before delivery, measure:

- growth from repeated tasks;
- teardown after normal ends and failures;
- recovery from an interrupted write.

Document retention and manual recovery. Cleanup must keep active work and pending review; sweeping by age or prefix, or relying on OS temp expiry, isn't enough. See the [Codex lifecycle](codex/README.md#storage-and-retention).

## Delivery gate

Deliver an integration only after it works in its real host. Until then, keep it a proposal: no adapter code, placeholder folder, manifest entry or support claim. Claude Code and GitHub Copilot use the portable instructions with no adapter.

In that host, establish the exact version and surface, then verify invocation and corrections, recovery and compaction, worker handoffs, rejected completion, truthful pauses, bounded retries, stale evidence and unavailable state or configuration. Inspect the context the agent receives and the failures the user sees. If a required native check is missing, don't deliver; another host, generated JSON or a local CLI run can't stand in for it.

Use [independent verification](../references/engineering-verification.md) and report what you tested and its limits.
