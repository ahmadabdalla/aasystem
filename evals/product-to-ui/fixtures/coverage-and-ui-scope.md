# Cedar service requests

## User request

$aapilot Reconcile this service-request mock with the product records and prepare the interaction handoff for implementation. Keep the proposal proportionate and identify what remains to be decided or verified. You may edit local design documents; do not build application code.

## Project files

### AGENTS.md

```markdown
Read docs/product/requests.md before changing request behavior.
Keep interaction notes in docs/experience/requests.md; verification recipes in docs/verify.md.
```

### docs/product/requests.md

```markdown
# Service requests
Approved by owner Sam on 2026-09-28; references R1–R6 are stable.
R1. Team members see team requests and can filter to requests assigned to them.
R2. A request's status changes retain actor and timestamp visible to its team.
R3. If a status update is rejected, keep the entered explanation, show the reason,
    and let the person correct and retry.
R4. If the device is offline, show that the update is unsent and allow retry after reconnection.
R5. Cancelling an open request requires confirmation naming the request.
R6. A person cannot read another team's requests or change history.
Owner note: approve behavior above; delivery team may choose ordinary component styling.
No decision on cross-request reports is recorded.
```

### docs/experience/requests.md

```markdown
# Request mock v2
Author: design assistant. Review pending.
Scope of this review slice: online request editing and cancellation.
Offline/reconnection UI is intentionally absent from this mock; R4 remains in scope for release.

Global navigation: Requests | Activity | Leaderboard.
Landing view: full-width weekly completion score and top five operators; below, request list.
Requests has tabs Team and Assigned to me.
Detail: title, status, explanation field, Update status, Cancel request.
Update status success: new status and toast "Updated".
Update status failure: toast "Try again"; close editor.
Cancel request: immediately mark cancelled and return to the list.
Activity: all teams' changes, searchable by person; actor and timestamp columns.
Leaderboard: team members ordered by completed request count.
```

### docs/verify.md

```markdown
# Request checks
There is no executable application in this fixture.
Planned checks: team list; assigned filter; successful status update.
Design screenshots show the online success state only.
```
