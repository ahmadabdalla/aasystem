# Business state and consistency

Use when a design changes business identity, state ownership, invariant enforcement,
or coordination between meanings that differ across established contexts.
Reuse agreed product rules, glossary terms, and current decisions.

## Name the model

Describe one concrete operation and the facts that make its result valid.
Distinguish stable identity from a value whose meaning comes from its contents.
Define equality, units, transitions, and lifecycle only where they matter.
A database row, class, business context, and deployment unit need not coincide.

When the same term has different meanings, name each context and its translation.
Use [Domain Modeling](../../domain-modeling/SKILL.md) for unsettled meanings and
justified records; Product retains authority over business rules.
Folders and service boundaries alone do not establish business contexts.

## Place the invariant

1. State the rule and identify every writer, including jobs, imports, and retries.
2. Choose the authoritative state owner and the operation that enforces the rule.
3. Identify which reads and writes must succeed together under the accepted contract.
4. Choose transaction, locking, constraint, version, or other enforcement from that need.
5. Explain concurrent attempts, stale reads, duplicate requests, and partial failure.
6. Across owners, name the accepted consistency guarantee and recovery mechanism.
   Events or eventual consistency are choices; they do not follow from object identity.

Use a consistency boundary where it makes the rule enforceable.
Keep independently changing state separate when the contract permits it.
A factory, repository, event, or rich object needs a concrete role in this operation.
Simple records and functions remain viable implementations.

## Carry the proof

Map the rule to observable success, rejection, conflict, and recovery scenarios.
Include competing writes or replay when those could violate the rule.
Name effects that persist after failure and who can observe or repair them.
Carry the cases into the existing verification plan and implementation brief.

Example: reserving the final item needs a defined outcome for concurrent requests.
A method named "reserve" is insufficient; identify the atomic check/write or other
mechanism. If payment is separate, preserve the agreed pending and recovery states
rather than silently promising one transaction or accepting overselling.

Return ownership, consistency, translations, and proof needs in the existing
[design package](design-package.md), reusing project record formats.
