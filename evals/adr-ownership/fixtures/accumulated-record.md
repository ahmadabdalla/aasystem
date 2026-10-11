# Supplier application

## User request

Use domain-modeling to reconcile the accumulated onboarding ADR with the dated decisions and latest review. You may edit local decision documents, their discovery pointers and the work handoff. Preserve rationale and provenance for continuing and replaced choices. Do not implement code, contact anyone or decide the unanswered policy proposal.

## Project files

### AGENTS.md

```markdown
This single supplier application has no separate established business contexts.
System-wide ADRs live in docs/adr with one shared numbering sequence.
Read docs/adr/index.md before changing onboarding. Requirements and verification
plans live in docs/work/onboarding.md. Keep dated review sources intact.
```

### docs/adr/index.md

```markdown
# Decisions
- [Supplier onboarding](0006-supplier-onboarding.md)
```

### docs/adr/0006-supplier-onboarding.md

```markdown
# Supplier onboarding

Accepted decisions for the whole application, accumulated after successive
reviews in [decision history](../reviews/onboarding.md).

## Assessment policy, 2026-09-10
Nia, product owner, confirmed manual assessment before activation rather than
automatic acceptance. Exceptions require judgement; accept operating costs
and published onboarding commitments that make reversal consequential.

## Assessment interface, 2026-09-17
Nia confirmed a persistent assessment queue rather than modal-only review.
Reviewers resume work across sessions; accept navigation complexity. Reversing
the shared queue requires retraining the team and redesigning the workflow.

## Notification architecture, 2026-09-24
Nia delegated architecture to engineering. The team selected best-effort email
sent directly after saving an assessment instead of a durable outbox, accepting
possible notification loss to avoid persistence and worker operations. Existing
integrations depend on the flow; reversing it requires migration.

## Work details appended later
Assessment requires an approve/reject action. Build the notification adapter,
then test restart after save and check failed delivery. Queue columns have 8px
spacing; the designer recommends changing to the existing 12px token.
```

### docs/reviews/onboarding.md

```markdown
# Onboarding decision history

2026-09-10, Nia, product owner: confirmed manual assessment before activation
instead of automatic acceptance because exceptions need judgement. Operating
costs are accepted; published commitments make changing the policy costly.

2026-09-17, Nia: confirmed a persistent assessment queue instead of modal-only
review so reviewers can resume across sessions. Navigation complexity is
accepted; retraining and workflow redesign make reversal costly.

2026-09-24: Nia explicitly delegated notification architecture to engineering.
The team chose direct best-effort email after saving rather than a durable
outbox, accepting possible loss to avoid persistence and worker operations.
Integrations depend on this shape, so later change requires migration.

2026-10-09 review:
- Nia confirms manual assessment and the queue remain the current choices.
  New operating evidence: the team handled 40 assessments in the first month;
  four required exception judgement. This supports the original policy rationale.
- Two observed notification losses changed engineering's architecture judgment.
  Within Nia's delegation, the team now accepts a durable transactional outbox
  instead of direct best-effort email. Reliability outweighs the extra storage
  and worker operations; migration of existing integrations is required.
  The replacement is agreed, but not implemented or verified.
- An engineer proposes allowing suppliers to activate through self-service.
  Nia has not resolved this policy proposal; manual assessment still applies.
- The designer's column-spacing change is routine styling within the existing
  component; it is trivial to reverse and changes no behavior or workflow.
```

### docs/work/onboarding.md

```markdown
# Onboarding work
Approved/rejected assessment outcomes must follow the current product decision
in [the decision index](../adr/index.md).
Architecture implementation is pending. Design and exercise restart after save,
notification delivery failure and recovery using the accepted notification shape.
No running application, verifier or runtime evidence is supplied for this task.
```
