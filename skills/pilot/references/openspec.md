# Working with OpenSpec

OpenSpec holds the change record. Your playbook still decides the work and the proof.

## 1. Find the change

1. Check a command with `openspec <command> --help` before relying on it.
2. Pick the change from the request and `openspec list`. If more than one could fit, ask the user which before writing.
3. If the work only touches the supporting docs in section 3, don't create a change. Otherwise run `openspec new change <name>`.
4. Before writing an artifact, run `openspec instructions <artifact> --change <name> --json` from the project root. Write to its `resolvedOutputPath` and follow its `context`, `rules` and `template`. Pass that output to any worker who writes an artifact.
5. Read every artifact in its `dependencies` first. A `done` status doesn't mean anyone agreed to it.

If a command fails, report the exact command and error, carry on with work that doesn't need it, and label what you wrote as unvalidated.

Initialise OpenSpec only if the task asks, with `openspec init --scope project`. Without the flag, init installs skills machine-wide.

## 2. Write the artifacts

Owners in the default schema:

- `proposal.md` and `tasks.md`: the task owner
- change `specs/`: [Product](../../product/SKILL.md)
- `design.md`: Solution, then Architect

Write only the artifact you own.

Only the schema defines artifacts. If the change folder holds a file `openspec status --change <name>` doesn't list, such as `interaction.md`, don't edit it as an artifact: tell the user it's outside the schema. If you need another artifact, add it to a schema forked with `openspec schema fork spec-driven <name>`, and check `status` lists it.

Pilot's one task list is `tasks.md`. Put the playbook's phases in it as headings, and give each task its completion check. Don't add archiving as a task: `openspec archive` stops on unticked tasks.

## 3. Keep supporting docs in their homes

Link these from the change; don't copy them in. Use the project's own paths, per the [project instructions](../../bootstrap-verification/references/project-instructions.md).

- Terms and decisions: [Domain Modeling](../../domain-modeling/SKILL.md), the glossary and ADRs. Add a new term to the glossary now, not in a later task.
- Interactions and UI rationale: [Interaction Design](../../interaction-design/SKILL.md), such as `docs/ux/<journey>.md`. Put a proposed revision in `docs/ux/changes/<change>.md`; the journey doc stays current until it's accepted.
- Verifier recipes and run evidence: the [project contract](../../bootstrap-verification/references/project-contract.md).

Skill reports don't go in the change folder; follow the [execution contract](execution.md#finish).

To point artifact authors at these docs, list them in `context` in `openspec/config.yaml` and check `openspec instructions` shows them.

## 4. When a decision changes

1. Supersede it under the [ADR rules](../../domain-modeling/references/adr.md#changing-an-adr).
2. Update everything that carried it: spec deltas, design, tasks (reopen ticked ones), UX docs, glossary, verifier recipes.
3. If two records disagree and nobody decided which wins, report the conflict. Don't pick the newest file.
4. If only the implementation changed, keep the requirements.

## 5. Prove, then archive

1. Map each added or changed scenario to a verifier recipe and run it. Ticked tasks and `done` artifacts don't show it works.
2. Run `openspec validate <name> --strict` and fix what it reports.
3. If another change touched the same capability, read the main spec with your delta applied and check they don't contradict.
4. In your reply, give each its own line: validation, each scenario and its check, Product's acceptance (never yours to give), observed usability, and runtime results (pass, fail, unverified).
5. Archive only if the request covers it and every agreed check passed.
6. Whether you archive or stop, name each link that moving the change to `changes/archive/YYYY-MM-DD-<name>/` will break: relative links in delta specs and `design.md`, and links from docs and recipes into the change.
7. Run `openspec archive <name>`. If it asks only to confirm the spec update, rerun with `--yes`. If it reports unticked tasks, stop. It merges spec deltas only; promote the accepted UX revision into `docs/ux/<journey>.md` yourself.
8. Run `openspec validate --specs --strict` and replace any placeholder Purpose archive wrote. Fix every broken link, and point current docs at the main spec, not the archive.
