# Returns project

## User request

Use domain-modeling to preserve the settled Returns decisions and hand back any unsettled policy from the local review. You may update local decision documents and pointers; do not change code or contact anyone. Do not settle the review's unanswered proposal.

## Project files

### AGENTS.md

```markdown
Returns and Sales are established contexts. System-wide decisions live in
docs/adr, local decisions in src/<context>/docs/adr. Read each context's README
for its decision links; preserve this convention.
```

### src/returns/README.md

```markdown
# Returns context
Handles after-sales refunds; Sales does not own return eligibility.
Decisions: [Manual review](docs/adr/0003-manual-review.md).
```

### src/returns/docs/adr/0003-manual-review.md

```markdown
# Review refunds manually
Confirmed Returns product decision. Human review remains necessary because
exceptions cannot yet be reliably classified; automation is deferred.
```

### src/returns/docs/review.md

```markdown
# Returns review
Lee, product owner, 2026-10-08:
"Confirmed: eligibility ends 30 days after delivery. We rejected a shorter
window because customers need time to discover faults, accepting additional
operating costs. Published commitments make later reductions costly. This
applies only to Returns, not to Sales price or order rules."
Lee delegated storage representation to the engineering team.
The team's settled choice is to store refund money as integer minor units
with currency, not binary floating-point. It is non-obvious to future engineers
because existing reporting uses floating-point, but exact reconciliation wins
over convenience. Altering persisted money later requires a data migration.
It is contained in Returns; this review does not change other contexts.

An engineer proposed automatically approving small refunds. Lee has not
resolved that proposal; manual review remains the current accepted rule.
No implementation or live verification evidence exists for the new choices.
```
