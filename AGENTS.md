# Maintain this library

This file defines the rules for changing the repository.

## Read before editing

- **Project entry:** [`README.md`](README.md)
- **System structure and sources:** [`SKILL_SYSTEM.md`](SKILL_SYSTEM.md)
- **Skill authoring:** [`skills/aapilot/playbooks/authoring-a-skill.md`](skills/aapilot/playbooks/authoring-a-skill.md)
- **Codex invocation:** [`CODEX.md`](CODEX.md)

## Edit skills

- Edit portable skills only in [`skills/`](skills/)
- Keep each rule in one owning file
- Link to shared guidance instead of copying it
- Preserve project-owned formats when a skill writes into another repository
- Follow the authoring playbook for every skill change

## Update documentation

- Update `README.md` when entry points or repository navigation change
- Update `SKILL_SYSTEM.md` when skills, playbooks, relationships, sources, or adaptations change
- Update `CODEX.md` when Codex invocation settings change
- Update the [system graph](visualizations/skill-library/README.md) when routes, handoffs, or ownership change

## Validate changes

- Run the checks required by the owning playbook
- Check every changed link and file path
- Check skill metadata and invocation adapters together
- Inspect the final diff for duplicated or misplaced guidance
- Do not treat fixture presence as a passing evaluation
