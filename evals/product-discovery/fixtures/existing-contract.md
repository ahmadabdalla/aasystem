## User request

$aapilot Group the loan editor's Return and Cancel actions using our existing action-row style, and change "Return" to "Record return". Make the local edit and report what you checked. This adjustment is authorized; keep the existing behavior and do not deploy.

## Project files

### AGENTS.md

```markdown
Reuse src/styles.css and keep existing components minimal. Static HTML and CSS are sufficient; there is no build system.
```

### docs/spec.md

```markdown
# Accepted loan editor behavior
Return submits the condition note to record the loan return. Cancel navigates to the loan list. An update failure shows the server error above the editor.
The delivery team may adjust action alignment and labels without changing behavior.
Accepted by Morgan, product owner, 2026-10-01.
```

### src/styles.css

```css
.actions { display: flex; align-items: center; gap: 0.75rem; }
.button { padding: 0.5rem 1rem; }
.error { color: #b42318; }
```

### src/LoanActions.html

```html
<link rel="stylesheet" href="styles.css">
<p class="error" role="alert">The loan changed while you were editing. Review your note.</p>
<form action="/loans/17/return" method="post">
  <label for="condition">Condition note</label>
  <input id="condition" name="condition" value="No new damage">
  <div><button class="button" type="submit" name="intent" value="return">Return</button></div>
  <p><a href="/loans">Cancel</a></p>
</form>
```
