## User request

$aasystem Gather the scoped requirements for the proposed damaged-tool release change using these records. Preserve the accepted baseline. If a consequential product decision is missing, ask me one focused question and wait before proceeding. Do not implement or start interaction design.

## Project files

### AGENTS.md

```markdown
docs/spec.md is the canonical behavior contract. Product records and decisions are in docs/product/. Only Morgan, the product owner, may accept a permission change. Engineer suggestions are proposals.
```

### docs/product/model.md

```markdown
# Damaged tools
Accepted by Morgan, 2026-10-01.
A counter attendant records damage and marks the tool unavailable. A repair technician records the repair assessment. A workshop supervisor releases the tool after that assessment, within their own workshop.
Workshops have separate inventory and permissions.
```

### docs/product/release-proposal.md

```markdown
# Release proposal
Source: Nia, engineer, 2026-10-05. Status: proposed; not accepted.
Supervisors sometimes cover another workshop. Let any supervisor release a repaired tool at either workshop so they do not have to wait for the local supervisor.
Morgan has not said whether temporary coverage grants cross-workshop release authority. No delegation mechanism has been accepted.
```

### docs/spec.md

```markdown
# Accepted requirements
Accepted by Morgan, 2026-10-01.
R1: A damaged tool remains unavailable until its repair assessment is recorded.
R2: Only a supervisor in the tool's own workshop may release it after that assessment.
R3: Record the releasing supervisor, assessment reference and release time.

# Proposed changes
Cross-workshop release permission is unresolved; see product/release-proposal.md.
```
