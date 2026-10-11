# Meridian record events

## User request

$aasystem Prepare closure of the accepted record-events change from these local files. Update the documentation and references needed for another engineer to find the current interaction model after archive. You may edit or move these documentation files, or provide an exact file-level closure plan. Do not change product behavior or create a new schema. The archive destination is openspec/changes/archive/2026-10-03-record-events/.

## Project files

### AGENTS.md

```markdown
Current interaction entry point: handbook/experience/index.md.
Decision records: handbook/decisions/. Verifier: handbook/verify.md.
Use the existing OpenSpec spec-driven schema and established handbook layout.
```

### openspec/config.yaml

```yaml
schema: spec-driven
context: |
  Current interaction model is indexed in handbook/experience/index.md.
  Decisions are recorded in handbook/decisions/.
```

### handbook/decisions/D-008.md

```markdown
# D-008: Change stream
Status: superseded by [D-014](D-014.md).
Previously accepted 2026-08-20: show a global Change stream for team events.
Retained to explain the original prototype's navigation.
```

### handbook/decisions/D-014.md

```markdown
# D-014: Record-local events
Status: accepted by owner Lee on 2026-10-02; supersedes [D-008](D-008.md).
Events belong in each job's detail panel, within the job's existing team permissions.
Remove the global Change stream destination. Actor, timestamp and changed value remain required.
Lee reviewed and accepted the interaction model in
[the change note](../../openspec/changes/record-events/experience.md).
This acceptance covers that interaction, not unrelated reports or permission changes.
```

### handbook/experience/index.md

```markdown
# Experience index
Current job workflow: [Job detail](job-detail.md).
Event design: [Change stream](change-stream.md), governed by [D-008](../decisions/D-008.md).
```

### handbook/experience/job-detail.md

```markdown
# Job detail — current
Title, assignee and status appear in the detail panel.
Navigation: Jobs | Change stream.
See [D-008](../decisions/D-008.md) for the event destination.
```

### handbook/verify.md

```markdown
# Verification map
Job events: required actor, timestamp, changed value, team isolation.
Interaction reference: [Change stream](experience/change-stream.md).
Recipe: open job; change status; open event destination; inspect actor/time/value;
try another team's job using its URL.
The executable app is not part of this closure exercise; no run result is recorded.
```

### openspec/specs/jobs/spec.md

```markdown
# Jobs
## Requirement: attributable events
Each job shows its events in its detail panel to members of its team.
Each event includes actor, timestamp and changed value.
Scenario: another team's member cannot read a job's events.
Synchronized from record-events on 2026-10-03; source: D-014.
```

### openspec/changes/record-events/proposal.md

```markdown
# Record events
Move events into job detail under [D-014](../../../handbook/decisions/D-014.md).
Current model: [Change stream](../../../handbook/experience/change-stream.md).
Supporting design: [Experience](experience.md).
```

### openspec/changes/record-events/experience.md

```markdown
# Record-events interaction
Accepted by Lee 2026-10-02, recorded in [D-014](../../../handbook/decisions/D-014.md).
Jobs remains the navigation destination. Job detail includes a collapsible Events
panel with actor, timestamp and changed value; visibility follows job team access.
The global Change stream destination is removed.
No events: show "No changes yet" in the panel. Loading failure: retain job details
and offer Retry within the Events panel.
This is a supporting handbook draft linked by design, not a schema artifact.
```

### openspec/changes/record-events/design.md

```markdown
# Design
Use the existing job-events endpoint and permission check.
Interaction: [Experience](experience.md).
Decision: [D-014](../../../handbook/decisions/D-014.md).
```

### openspec/changes/record-events/tasks.md

```markdown
# Tasks
- [x] Implement record-local panel and remove global destination.
- [x] Run application verification (record retained in the consuming project).
- [x] Synchronize jobs spec.
- [ ] Reconcile current handbook, verifier links and supporting documents for archive.
```
