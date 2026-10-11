## User request

$aapilot Help me, Morgan the founder, explore how our workshop platform is organized and how people book, collect and return tools. Interview me about concrete work and handoffs, then document what we know and the open questions. This is discovery only: exclude customer-value research, architecture selection and requirements writing. Retain attributable interview answers under docs/discovery/ so I can resume later. Keep the accepted baseline intact.

## Project files

### AGENTS.md

```markdown
Product records live in docs/product/. Discovery interviews selected for retention live in docs/discovery/. Existing requirements live in docs/spec.md.
Use existing glossary terms. No deployment or external contact is authorized.
```

### docs/product/model.md

```markdown
# Workshop platform
Accepted baseline, Morgan (founder), 2026-10-01.
A workshop is a tenant. Each workshop owns its tools and bookings; other workshops cannot see them.
People may hold several responsibilities. Do not assume account types are mutually exclusive.
We have two workshops: North and South. The product should capture tool work currently spread across a spreadsheet, paper and conversations.
Collection, return inspection and unavailable-tool handling have not yet been documented as journeys.
```

### docs/product/glossary.md

```markdown
Workshop: the organization owning an inventory and its bookings.
Crew member: a person booking or using tools for a repair crew.
Counter attendant: a person handling tool collection and return inspection.
Repair technician: a person assessing and repairing unavailable tools.
```

### docs/spec.md

```markdown
# Accepted requirements
R1: A crew member can book an available tool in their workshop for a time interval.
R2: A booking must not overlap another confirmed booking for that tool.
R3: Inventory and booking visibility is confined to the person's workshop.
Accepted by Morgan, 2026-10-01. These remain the current baseline during discovery.
```
