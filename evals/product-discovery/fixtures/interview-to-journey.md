## User request

$aapilot Use our retained interviews to document the dispatch-to-completion journey, including the blocked-access handoff, and gather scoped candidate requirements for that handoff. Preserve sources, authority and unresolved choices. Update the local product records and existing specification; return the result to me for review. Interaction design and implementation are outside this assignment.

## Project files

### AGENTS.md

```markdown
Product model and journeys belong in docs/product/. Interview evidence belongs in docs/discovery/. docs/spec.md is the single requirements authority.
Candidate changes remain proposals until Mira accepts them. Reuse glossary terms and link existing evidence instead of copying interview transcripts.
```

### docs/product/model.md

```markdown
# Field service
Accepted by Mira, product owner, 2026-10-02.
A dispatcher assigns work and coordinates customer access. A technician performs assigned jobs and records completion. One person may hold both responsibilities.
Each job belongs to a service team. Visibility is limited to that team.
```

### docs/product/glossary.md

```markdown
Dispatcher: a person assigning jobs and coordinating access.
Technician: a person carrying out an assigned job.
Blocked access: assigned work cannot proceed because the technician cannot enter the work location.
```

### docs/discovery/dispatch.md

```markdown
# Dispatch and blocked access
Scope: assignment through job completion; retained for journey and requirement review.
Participants: Mira (product owner and dispatcher), Dev (technician), 2026-10-04.

Question: What happens when a technician cannot start an assigned job?
Dev: Yesterday I accepted the entrance-light job, arrived and found the building locked. I texted Mira the job number and the access problem. I left it unfinished; I did not mark it complete.
Mira: I called the site contact, arranged entry and texted Dev when access was available. I want the job to retain the blocker and show who must arrange access, so work does not disappear in messages.
Dev: Once Mira confirmed entry, I returned, replaced the light and recorded the work done. Completion should include the work note.
Status: Attributed recollection and intended behavior; no proposed requirements have been accepted.
Open question: Mira has not chosen whether a blocker should send notifications. A colleague suggested cross-team visibility; Mira has not approved that.
```

### docs/spec.md

```markdown
# Field service requirements
Accepted by Mira, 2026-10-02.
R1: A dispatcher may assign a job to a technician in the same service team.
R2: The assigned technician may record job completion with a work note; team members can see that completion.

# Proposed changes
No proposals yet. New scoped proposals should continue the requirement identifiers here and link their source and affected journey.
```
