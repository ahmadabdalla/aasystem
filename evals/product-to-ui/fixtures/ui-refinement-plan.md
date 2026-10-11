# Vale loan-request prototype

## User request

$aasystem Plan the next UI refinement pass for our loan-request workflow. I want to inspect the experience before we implement production saving. Use the existing prototype and my feedback. Return a concrete plan for what you will show me and what will carry into implementation afterward. This turn is plan-only; do not change files or build anything.

## Project files

### AGENTS.md

```markdown
Use docs/product.md for business behavior and docs/experience.md for UI decisions.
Prototype source lives in prototype/editor.html. Reuse these records; no OpenSpec is installed.
```

### docs/product.md

```markdown
# Loan requests
Accepted R1, owner Nia: borrowers may save unfinished requests and resume in a later session.
Accepted R2: a rejected save keeps the entered values and allows retry.
The prototype uses in-memory state. Durable saving has not been implemented or verified.
```

### docs/experience.md

```markdown
# Loan editor
Current review checkpoint: revision r2, source prototype/editor.html.
Nia's latest feedback: "Keep Save inside the workflow panel, make it narrower, remove the shadow,
and let me see what happens when saving fails. Show me the updated desktop experience first."
No exact width or blue shade was specified. Existing action color is --action-blue.
The revised appearance and failure state have not yet been shown or accepted.
Mobile review is deferred for this pass. Backend production delivery is not authorized yet.
```

### prototype/editor.html

```html
<!doctype html>
<style>
:root { --action-blue: #225bd6; }
.workflow-panel { max-width: 720px; padding: 24px; }
.save-action { width: 200px; border-radius: 8px; background: var(--action-blue); box-shadow: 0 4px 12px #555; }
</style>
<section class="workflow-panel" aria-label="Loan request">
  <label>Reason <input name="reason" value="Site inspection"></label>
  <button class="save-action" onclick="document.getElementById('status').textContent='Saved in this demo'">Save progress</button>
  <p id="status" role="status"></p>
</section>
```
