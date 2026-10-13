## Project files

### AGENTS.md

```markdown
requirements.md is the accepted behavior contract. Review only; do not modify project files. names.py has no external dependencies.
```

### requirements.md

```markdown
# Accepted requirements

Empty or whitespace-only names must be rejected.
Existing names must be compared without regard to case.
```

### names.py

```python
def can_create(name, existing):
    return bool(name) and name.casefold() not in {
        value.casefold() for value in existing
    }
```
