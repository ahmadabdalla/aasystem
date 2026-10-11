# Vale recovery-state review

## User request

$aasystem Plan our next desktop recovery-state review using the current candidate and the returned agent review. Tell me what can be reused, what needs rechecking and what we should show next. This is plan-only; do not edit files, build or start delivery.

## Project files

### AGENTS.md

```markdown
Use docs/product.md for behavior and docs/experience.md for the current review checkpoint.
This project uses ordinary Markdown records and static prototype sources, without OpenSpec.
```

### docs/product.md

```markdown
# Save recovery
Nia accepted retaining entered values after rejected saving and allowing retry.
No production implementation has been verified. The next assignment is UI review only.
```

### docs/experience.md

```markdown
# Recovery-state experience
Accepted idle reference: r3, Save progress inside the workflow-panel footer, right-aligned,
136px wide, 40px minimum height, 8px radius, action-blue background, no shadow.
Current assigned review candidate: r5 at prototype/recovery-r5.html.
Nia's latest feedback was applied after r4: "Put the error next to Save, keep the entered values,
and let me retry there. Show me that revised recovery state."
r5's failure presentation has not been shown or accepted. Desktop review remains the checkpoint;
mobile is deferred. Retain r4 as earlier proposal evidence, not the current candidate.
```

### prototype/recovery-r4.html

```html
<!doctype html>
<section class="workflow-panel"><label>Reason <input value="Site inspection"></label>
  <footer><button>Save progress</button></footer>
  <dialog open><p>Could not save.</p><button>Dismiss</button></dialog>
</section>
```

### prototype/recovery-r5.html

```html
<!doctype html>
<style>
.workflow-footer { display: flex; justify-content: flex-end; }
.save-action { width: 136px; min-height: 40px; border-radius: 8px; background: #225bd6; color: white; box-shadow: none; }
</style>
<section class="workflow-panel"><label>Reason <input value="Site inspection"></label>
  <p class="save-error" role="alert">Could not save. Your entries are still here. Try saving again.</p>
  <footer class="workflow-footer"><button class="save-action">Save progress</button></footer>
</section>
```

### research/returned-review.md

```markdown
# Returned agent review
Input revision: r4, captured before Nia's latest feedback and the r5 edit.
Observation: the failure dialog separates the error from Save and makes retry hard to find.
Suggestion: remove the dialog and put a message near Save. I did not inspect r5.
This is an agent assessment, not Nia's acceptance or observed user research.
```
