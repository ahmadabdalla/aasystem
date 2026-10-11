# Vale equipment-loan editor

## User request

$aapilot Prepare the technical-design handoff for our loan editor using the existing reviewed UI. Explain what the implementer must preserve and how we should check the delivered result. Read the existing files; do not edit the UI, restart discovery, or begin implementation.

## Project files

### AGENTS.md

```markdown
Product requirements live in docs/product.md. Experience decisions live in docs/experience.md.
This is a plain HTML/CSS project without OpenSpec. Use existing records.
```

### docs/product.md

```markdown
# Loan editor
Accepted R1: A borrower can save an unfinished loan request and resume it in a later session.
Accepted R2: A failed save preserves the entered values and offers retry.
Product owner: Nia. The existing implementation has not been exercised for persistence.
```

### docs/experience.md

```markdown
# Loan editor experience
D-21: Nia accepted reference r3 for the desktop editor at 1280 x 800.
The Save progress action sits in the workflow panel footer, right-aligned within the panel.
It uses .save-action: 136px width, 40px minimum height, 8px radius,
background var(--action-blue), and no shadow. Do not replace it with a floating viewport button.
Reference: references/loan-editor-r3.html. This source file is retained unchanged as r3.
D-21 supersedes D-18, which placed the action in the page header. Nia moved it to keep it grouped with the workflow.
Desktop idle placement and appearance are accepted. Failure content follows R2; it was not reviewed visually.
Mobile placement remains open. This acceptance does not cover other widths, states or backend operation.
```

### references/loan-editor-r3.html

```html
<!doctype html>
<style>
:root { --action-blue: #225bd6; }
.workflow-panel { max-width: 720px; padding: 24px; }
.workflow-footer { display: flex; justify-content: flex-end; margin-top: 24px; }
.save-action { width: 136px; min-height: 40px; border: 0; border-radius: 8px; background: var(--action-blue); color: white; box-shadow: none; }
</style>
<section class="workflow-panel" aria-label="Loan request">
  <label>Reason <input name="reason" value="Site inspection"></label>
  <footer class="workflow-footer"><button class="save-action">Save progress</button></footer>
</section>
```

### src/loan-editor.html

```html
<!doctype html>
<style>
.save { position: fixed; top: 16px; right: 16px; width: 200px; border-radius: 16px; background: blue; box-shadow: 0 4px 12px #555; }
</style>
<form action="/loans/draft" method="post">
  <label>Reason <input name="reason" value="Site inspection"></label>
  <button class="save" type="submit">Save progress</button>
</form>
```
