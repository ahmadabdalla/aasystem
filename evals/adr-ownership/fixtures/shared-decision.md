# Customer identity project

## User request

Use domain-modeling to record the accepted customer-identity decision and explain what to do with the component-spacing note. Update local documents only. Do not implement code or contact anyone.

## Project files

### AGENTS.md

```markdown
System decisions live in docs/adr; start from docs/adr/index.md.
Ordering and Billing are established business contexts under src/ordering and
src/billing. Context-local records belong inside those contexts.
```

### docs/adr/index.md

```markdown
# System decisions
- [Context boundaries](0012-context-boundaries.md)
```

### docs/adr/0012-context-boundaries.md

```markdown
# Keep Ordering and Billing separate
Accepted system-wide software decision. Separate the contexts because their
invariants evolve independently; agree explicit contracts for shared identity.
```

### docs/identity-review.md

```markdown
# Identity review
Sam, decision owner, 2026-10-08, confirmed:
"Ordering and Billing will reference the same opaque CustomerId. Neither can
reassign an existing ID. We chose a shared identity contract over translating
IDs per context because reconciliation errors would break account continuity.
Changing it later requires migrating existing references in both contexts."
This is one agreed identity contract. It constrains product account continuity,
design's account-switching presentation, and software integration boundaries.
It does not determine the actual account-switching interaction.
Implementation and verification have not started.

Component note, already within the team's routine styling remit:
Change button spacing from 8px to 12px using existing tokens. It is trivial to
reverse and introduces no new interaction, behavior or consequential tradeoff.
```
