# Refactoring moves

Use for an agreed structural improvement within Implement's assigned scope.
Reuse the caller's baseline, compatibility requirements, and affected checks.
A move across responsibility or state owners needs Architect's settled target.

## Select the move

Name the reader or change burden the move removes; retaining the code is valid.
Use Maintainability's [local-code](../../maintainability/references/local-code.md)
and [boundary criteria](../../maintainability/references/boundaries.md).

- **Rename:** inspect callers, string lookup, persisted names, generated inputs,
  and public contracts before treating a domain-name correction as internal.
- **Extract or inline:** extract a meaningful operation that reduces mental work;
  inline a hop that adds none. Preserve evaluation order, effects, and lifetime.
- **Move responsibility:** migrate behavior and callers to the settled knowledge
  owner; retain forwarding only for a real policy or compatibility obligation.
- **Introduce a value:** group values sharing a rule or lifecycle. Preserve units,
  equality, validation, serialization, and compatibility at existing edges.
- **Simplify a branch:** preserve condition order, short-circuiting, defaults,
  and failures. Choose guards, a table, or polymorphism from actual variation.
- **Share or separate:** trace which rule must change together; weigh the coupling
  introduced by sharing against the synchronization burden it removes.

## Apply and check

Identify the smallest move and the observable behavior it could disturb.
Check indirect consumers and maintained source before editing generated output.
Apply the move, migrate affected callers, and remove only owned obsolete paths.
Run the caller's affected baseline checks and inspect the diff for contract drift.
Classify a changed result before further edits; preserve failures and others' work.
Return scope or design contradictions to the caller rather than changing expectations.

For a staged public migration, name who still needs the old path, how callers move,
and the removal condition. A compatibility layer needs an actual consumer.
Use the same expectation for old and new paths where equivalence is intended.

Example: extracting eligibility calculation must preserve when inventory is read
and whether an external reservation occurs; equal return values alone are insufficient.

Return the move, resulting improvement, compatibility impact, and development evidence
in the caller's record. The playbook owns final equivalence and acceptance.
