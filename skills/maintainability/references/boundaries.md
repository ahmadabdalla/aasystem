# Boundaries

Evaluate the supplied code or design against real callers and project constraints.
Compare the current shape with the simplest viable alternative.

## Trace the contract

- **Caller burden:** Include configuration, ordering, effects, failure modes, and
  resource lifetime, not just signatures. What must callers coordinate themselves?
- **Knowledge:** Identify the representation or policy each module owns. Trace a
  credible change: which callers would need coordinated edits, and why?
  Check grouping by owned knowledge rather than merely by execution order.
- **Source ownership:** Distinguish maintained inputs from generated output.
  Check that regeneration preserves customizations at the supported boundary.
- **State:** Trace access patterns, writers, and owners. Inspect retries, concurrency,
  partial failure, and observable effects before accepting an idempotence claim.
- **Invariants:** Identify the type, constraint, runtime boundary, or other mechanism
  enforcing each rule. Check external input at its trust boundary; an internal
  assertion does not replace required validation.
  Check whether authoritative values are derived or manually synchronized.

## Assess the dependency

When choosing a boundary, sketch the caller before and after the change.
Name the knowledge hidden, the obligation exposed, and the reason to separate it.

- Keep policy with its owner; translate framework or provider details where their
  meanings cross into that policy. Trace imports, calls, and data formats together.
- Choose dependency direction from that ownership. Use existing language and
  framework mechanisms before adding another layer.
- Justify an adapter through actual variation, external behavior, or a needed
  control point. Adapter count alone does not establish value or needless complexity.
- Ask what removing a wrapper would do: eliminate work or redistribute it among
  callers? Forwarding can earn its place through policy, adaptation, or stability.
- Keep internal test controls private unless production callers need them.
  Substitutes prove their exercised contract; real integration needs its own checks.
- Moving code does not automatically move permissions, transaction scope, process
  isolation, or cleanup responsibility. Preserve those obligations explicitly.

Example: a payment adapter may hide provider response formats, but it must preserve
whether a timed-out request might have charged the customer. Mapping that uncertainty
to "not charged" changes the contract rather than merely simplifying it.

## Judge the result

Assess change locality, compatibility, migration, and concrete reversal cost:
what would replacing this choice require moving in callers, data, or operations?
An interface does not by itself make replacement cheap.

Identify checks through real callers with independently derived expectations.
Distinguish a design defect from a faulty observation method.
Trace material concerns to a causal burden, recommendation, tradeoff, and proof need.
Apply project constraints; file counts, fixed layer counts, and hypothetical future
consumers alone do not justify a finding or an abstraction.
