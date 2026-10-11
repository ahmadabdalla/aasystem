# Harbor request editor

## User request

$aapilot Align the request editor's Save and Cancel actions using our existing action-row style, and change the Save label to "Save changes". Keep the existing form behavior. Make the local edit and report what you checked. This presentation adjustment is authorized; no deployment is requested.

## Project files

### AGENTS.md

```markdown
Reuse styles in src/styles.css. Prefer minimal changes for existing components.
The fixture contains static HTML and CSS; no build system is required.
```

### docs/product.md

```markdown
# Request editor
Accepted behavior: Save submits the editor; Cancel navigates to the request list.
Show the server's error message above the editor when an update fails.
The delivery team may adjust alignment and button labels without changing behavior.
```

### src/styles.css

```css
.actions { display: flex; align-items: center; gap: 0.75rem; }
.button { padding: 0.5rem 1rem; }
.error { color: #b42318; }
```

### src/RequestActions.html

```html
<link rel="stylesheet" href="styles.css">
<p class="error" role="alert">The request was updated by someone else. Review your changes.</p>
<form action="/requests/17" method="post">
  <label for="title">Title</label>
  <input id="title" name="title" value="Replace entrance light">
  <div><button class="button" type="submit" name="intent" value="save">Save</button></div>
  <p><a href="/requests">Cancel</a></p>
</form>
```
