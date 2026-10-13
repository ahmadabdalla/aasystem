# Decision records across projects

## User request

Use domain-modeling to write a proposed system software ADR for Alpha's delivery
queue from its design note. Then review the listed records and supplied review
claims. For each record, identify the rules used, give a verdict and explain any
failure with the rule and the missing information or format error. Check the
claims against those same rules. Do not edit the reviewed records, implement
code, contact anyone or settle conflicting project rules in this exercise.

Review these records:

- `alpha/docs/adr/0001-event-times.md`
- `alpha/docs/adr/0002-delivery-retries.md`
- `beta/docs/adr/0002-storage.md`
- `gamma/docs/adr/0003-backups.md`
- `delta/docs/adr/0002-storage.md`
- `epsilon/docs/adr/0001-event-times.md`
- `zeta/docs/adr/0001-storage.md`

Each directory is a separate project. Do not use one project's rules in another.

## Project files

### alpha/AGENTS.md

```markdown
System decisions live in docs/adr; start from docs/adr/index.md.
This new project has no established ADR convention. The existing files are
drafts under review, not examples of an adopted convention.
```

### alpha/docs/adr/index.md

```markdown
# Decisions
- [Event times](0001-event-times.md)
- [Delivery retries](0002-delivery-retries.md)
```

### alpha/docs/design-note.md

```markdown
# Delivery queue
Mina, software decision owner, 2026-10-12, proposes storing delivery jobs in a
durable queue so restarts do not lose scheduled deliveries. An in-memory queue
was considered and rejected because restarting discards pending jobs. Durable
storage adds writes and operations work; jobs may be delivered twice, so
handlers must accept duplicates. Reversing the choice requires migrating queued
jobs. This is a proposal; no acceptance or implementation evidence exists.
```

### alpha/docs/adr/0001-event-times.md

```markdown
# Store event times in UTC
To sort events across regions, store UTC timestamps rather than local times
because daylight-saving changes make local ordering ambiguous. UTC gives a
consistent order but loses the original timezone, which callers must store
separately if needed. Proposed system software decision; acceptance authority
is unknown.
```

### alpha/docs/adr/0002-delivery-retries.md

```markdown
# Retry failed deliveries
To recover temporary delivery errors, retry failed jobs up to three times so
transient failures do not immediately discard deliveries. Retrying increases
traffic and delays the final failure notification. Proposed system software
decision; acceptance authority is unknown.
```

### beta/AGENTS.md

```markdown
Use docs/adr and its index.md. Each ADR uses a two-column table with exactly
these fields: Status, Choice, Reason, Source. Those four fields are the complete
content requirement. Source must link to the decision owner's recorded choice.
```

### beta/docs/adr/index.md

```markdown
# Decisions
- [Storage](0002-storage.md)
```

### beta/docs/storage-review.md

```markdown
2026-10-12: Inez, software decision owner, accepted object storage for exports
because exports outgrow the application disk. No implementation was reviewed.
```

### beta/docs/adr/0002-storage.md

```markdown
# Export storage
| Field | Value |
| --- | --- |
| Status | Accepted system software decision |
| Choice | Store exports in object storage |
| Reason | Exports outgrow the application disk |
| Source | [Storage review](../storage-review.md) |
```

### beta/docs/review-claim.md

```markdown
The storage record fails because every ADR must list a rejected alternative
and expected costs, even when the project's rules do not require those fields.
```

### gamma/AGENTS.md

```markdown
Use docs/adr and its index.md for system software decisions.
```

### gamma/docs/adr/index.md

```markdown
# Decisions
- [Daily backups](0001-daily-backups.md)
- [Separate region](0002-separate-region.md)
- [Keep backups](0003-backups.md)
```

### gamma/docs/backup-review.md

```markdown
2018-06-01: Sol, software decision owner, accepted daily backups stored in a
separate region. 2026-10-12: Sol accepted retaining backups for thirty days to
cover errors reported several weeks later. The team has continued using the
decision-card format shown in records 0001 and 0002; no replacement convention
has been adopted. This note records choices, not implementation evidence.
```

### gamma/docs/adr/0001-daily-backups.md

```markdown
# Daily backups
Choice: Back up once per day.
Reason: Limit data lost after a failure to one day.
Standing: Accepted by Sol in the [backup review](../backup-review.md).
```

### gamma/docs/adr/0002-separate-region.md

```markdown
# Separate region
Choice: Store backups in a separate region.
Reason: Recover when the application region is unavailable.
Standing: Accepted by Sol in the [backup review](../backup-review.md).
```

### gamma/docs/adr/0003-backups.md

```markdown
# Keep backups for thirty days
Choice: Retain backups for thirty days.
Reason: Recover errors reported several weeks later.
Standing: Accepted by Sol in the [backup review](../backup-review.md).
```

### gamma/docs/review-claim.md

```markdown
Record 0003 fails because older decision cards must be rewritten with Context,
Decision and Consequences headings before they can pass review.
```

### delta/AGENTS.md

```markdown
Use docs/adr and its index.md. Every record being created or reviewed must state
context, choice, reason, a rejected alternative, expected effects, standing and
a link to the decision owner's recorded choice. Section names are optional.
```

### delta/docs/adr/index.md

```markdown
# Decisions
- [Earlier storage choice](0001-storage.md)
- [New storage choice](0002-storage.md)
```

### delta/docs/storage-review.md

```markdown
2020-03-01: Inez, software decision owner, accepted application-disk storage
while exports remained small. 2026-10-12: Inez accepted object storage because
exports now outgrow that disk, rejecting a larger application disk because it
still couples export capacity to the application host. No delivery was reviewed.
```

### delta/docs/adr/0001-storage.md

```markdown
# Store exports on the application disk
Choice: Use the application disk.
Reason: Exports remain small.
Standing: Superseded by [0002](0002-storage.md); originally accepted by Inez in
the [storage review](../storage-review.md).
```

### delta/docs/adr/0002-storage.md

```markdown
# Store exports in object storage
Choice: Use object storage because exports outgrow the application disk.
Reason: A larger application disk still couples export capacity to the host.
Standing: Accepted by Inez in the [storage review](../storage-review.md),
superseding [0001](0001-storage.md).
```

### epsilon/AGENTS.md

```markdown
System decision drafts live in docs/adr. This new project has not adopted an ADR
convention. Files in docs/reference are downloaded reading material.
```

### epsilon/docs/adr/0001-event-times.md

```markdown
# Store event times in UTC
To sort events across regions, store UTC timestamps rather than local times
because daylight-saving changes make local ordering ambiguous. UTC gives a
consistent order but loses the original timezone, which callers must store
separately if needed. Proposed system software decision; acceptance authority
is unknown.
```

### epsilon/docs/reference/template.md

```markdown
# External ADR template
This template requires YAML fields status and decision-makers, followed by
Context, Decision Drivers, Considered Options and Decision Outcome headings.
```

### epsilon/docs/review-claim.md

```markdown
The event-times record fails because it omits the YAML fields and headings
required by docs/reference/template.md.
```

### zeta/AGENTS.md

```markdown
System ADRs live in docs/adr. Both docs/rules-a.md and docs/rules-b.md apply to
all ADRs. Neither document overrides the other.
```

### zeta/docs/rules-a.md

```markdown
Each ADR must use Context, Decision and Consequences section headings.
```

### zeta/docs/rules-b.md

```markdown
Each ADR must contain a title and one paragraph. Section headings are forbidden.
```

### zeta/docs/adr/0001-storage.md

```markdown
# Use object storage
## Context
Exports outgrow the application disk.
## Decision
Use object storage rather than a larger application disk to keep export
capacity independent of the application host. This is a proposal; acceptance
authority is unknown.
## Consequences
Accept network access and storage charges in exchange for independent capacity.
```
