# Boundaries

Judge interfaces and ownership against real or sketched callers. For each concern, compare with the simplest alternative that would work. File counts, layer counts and imagined future callers never justify a finding or an abstraction.

## Trace the contract

- **Caller burden:** What must callers know or coordinate: configuration, ordering, effects, failure modes, resource lifetime? The signature is only part of it.
- **Knowledge:** Which representation or policy does each module own? Trace one likely change: which callers need edits, and why? Group code by the knowledge it owns, not by the order it runs.
- **Generated code:** Tell maintained source from generated output. Check that regeneration keeps customisations made at the supported place.
- **State:** Who writes it and who owns it? Before accepting an idempotence claim, check retries, concurrency, partial failure and visible effects.
- **Invariants:** Name what enforces each rule: a type, a constraint, a runtime check. Validate external input where it enters; an internal assertion doesn't replace that. Derive authoritative values instead of syncing copies by hand.
- **Change and reversal cost:** What would moving to this shape, and later away from it, move in callers, data or operations? How do callers stay compatible meanwhile? An interface alone doesn't make replacement cheap.

## Assess the dependency

If a change adds or moves a boundary, sketch the caller before and after. Name the knowledge the split hides, the obligation it exposes, and why it helps.

- Keep policy with its owner, and let that owner set dependency direction. Translate framework or provider details where they meet the policy. Use existing language and framework features before adding a layer.
- An adapter needs a reason: real variation, external behaviour to contain, or a control point you need.
- Apply the deletion test to a wrapper: if you removed it, would the work vanish or spread across callers? A forwarder earns its place through policy, adaptation or stability.
- Keep test-only controls private, and delete one when its last test goes. A fake proves only the contract it exercises; real integration needs its own check.
- Moving code doesn't move permissions, transaction scope, process isolation or cleanup. Carry them over explicitly.

Example: a payment adapter may hide the provider's response format, but must keep "a timed-out charge may have gone through". Mapping a timeout to "not charged" changes the contract.
