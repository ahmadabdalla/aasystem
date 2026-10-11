# Linden equipment library

## User request

$aapilot Prepare the interaction proposal for equipment checkout and return using these project records. Keep it usable by the engineer building the next version, with source links and outstanding decisions. You may update the local experience document. Do not implement software or change our documentation system.

## Project files

### AGENTS.md

```markdown
This project uses Markdown requirements, not OpenSpec.
Product: product/requirements.md. Experience: experience/checkout.md.
Decisions: product/decisions.md. Verification: checks/README.md.
```

### product/requirements.md

```markdown
# Equipment lending
Owner Priya confirmed R1–R6 on 2026-09-30.
R1. A member can reserve an available item, check it out and return it.
R2. Equipment maintainers mark an item under maintenance; such items cannot be checked out.
R3. A person can be both member and maintainer. Jules currently does both.
R4. If someone else reserved the item first, explain the conflict and preserve the requested dates.
R5. Borrowing history is visible only to the borrower and library coordinators.
R6. Show the due date and overdue state. A return records condition and relevant maintenance notes.
```

### product/decisions.md

```markdown
# Decisions
2026-09-30 — Priya: condition history belongs to the item and helps decide availability.
Routine layout and use of existing components are delegated to the delivery team.
2026-10-01 — Engineer proposal, owner has not responded: block new reservations
whenever a member has any overdue equipment.
```

### experience/checkout.md

```markdown
# Checkout sketch
Draft by implementation assistant.
First visit: choose Borrower or Maintainer account; selection cannot be changed.
Navigation: Catalogue | My loans | Feed.
Catalogue card: availability, Reserve. Confirm reservation: generic success screen.
Item detail: condition notes and maintenance status; Check out always enabled.
My loans: item, due date, overdue badge, Return.
Return: condition, maintenance note, Submit; automatically post return to Feed.
Public profile: all historic returns and dates.
Overdue member: Reserve disabled for every item.
```

### checks/README.md

```markdown
# Check plan
No implementation is included here.
Planned walkthrough: reserve, check out, return; maintainer changes availability.
Use requirement IDs when handing off additional checks.
```
