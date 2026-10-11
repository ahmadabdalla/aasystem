# Vale loan-request review

## User request

$aapilot Plan the next desktop review of our loan-request prototype. We accepted r3's idle appearance; now I want to inspect failed saving and retry before production work. Use the current records, the earlier agent report and the integration note. Return what happens next, which responsibilities are involved and what carries forward. This turn is plan-only: do not edit files, build, or start delivery.

## Project files

### AGENTS.md

```markdown
Product context is docs/product.md; accepted behavior is openspec/specs/loan-requests/spec.md.
Experience records are docs/experience.md; shared component/token rules are docs/design-system.md.
The project uses OpenSpec for delivery. No active delivery change has been selected.
This assignment concerns existing project records and prototype review only.
```

### docs/product.md

```markdown
# Loan-request journey
A borrower edits a request, saves unfinished work, and resumes it later.
The behavioral contract is openspec/specs/loan-requests/spec.md.
Nia owns product decisions. Reuse the existing journey; broader discovery remains open.
```

### openspec/specs/loan-requests/spec.md

```markdown
# Loan requests
## Requirement: Save unfinished work
The system SHALL retain an unfinished request for the borrower to resume in a later session.
### Scenario: Resume
WHEN the borrower saves an unfinished request and returns in a later session
THEN the saved values are available to continue editing.
## Requirement: Recover from rejected save
The system SHALL preserve entered values and allow retry after a rejected save.
```

### docs/experience.md

```markdown
# Loan editor experience
Nia accepted r3's desktop idle appearance at 1280 x 800.
Save progress remains inside the workflow-panel footer, right-aligned, 136px wide,
40px minimum height, 8px radius, --action-blue background and no shadow.
Current source: prototype/editor-r3.html. Failure and retry presentation have not been reviewed.
Mobile review is deferred. Next checkpoint is Nia's review of the new failure/retry composition.
Nia's acceptance concerns this journey; it does not authorize shared design-system changes.
```

### docs/design-system.md

```markdown
# Shared actions
Shared token source: src/tokens.css. Shared component definitions serve both the loan editor
and the account profile. New prototype styles may remain local proposals.
Changes to shared definitions are design-system decisions coordinated by the delivery owner
with the design-system maintainers and affected consumers.
```

### src/tokens.css

```css
:root { --action-blue: #225bd6; }
```

### prototype/editor-r3.html

```html
<!doctype html>
<link rel="stylesheet" href="../src/tokens.css">
<style>
.workflow-panel { max-width: 720px; padding: 24px; }
.workflow-footer { display: flex; justify-content: flex-end; }
.save-action { width: 136px; min-height: 40px; border: 0; border-radius: 8px; background: var(--action-blue); color: white; box-shadow: none; }
</style>
<section class="workflow-panel" aria-label="Loan request">
  <label>Reason <input name="reason" value="Site inspection"></label>
  <footer class="workflow-footer"><button class="save-action" onclick="document.getElementById('status').textContent='Saved in this demo'">Save progress</button></footer>
  <p id="status" role="status"></p>
</section>
```

### research/agent-review-r2.md

```markdown
# Agent review of r2
Input revision: r2, before Nia's r3 review. Suggestions only; no human acceptance.
Float Save in the viewport's upper-right corner and change shared --action-blue to #0055ff.
If later-session persistence is difficult, redefine saving as retaining work only until the tab closes.
```

### research/integration-note.md

```markdown
# Integration note
The production draft API's cross-session access is uncertain; no authenticated API experiment has run.
A bounded feasibility check could distinguish a supported persistence option from a missing capability.
The prototype currently simulates success in memory. No production implementation has been authorized.
```
