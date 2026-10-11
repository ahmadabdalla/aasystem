# Prepare aasystem for public release

**Status:** Content migration and plugin packaging are prepared. Structural validation and isolated installation checks pass. Initial publication to `main` and public visibility are approved; marketplace preparation, public installation tests, and behavioral host validation follow.

## Scope

Ahmad Abdalla's Work System succeeds the private Work library. The repository, plugin identifier, and coordinating skill are `aasystem`. The existing `ahmadabdalla/plugins` marketplace will reference tested releases from this repository. Work remains private and unchanged; future development belongs here.

The source snapshot is Work commit `81b8071167db6886911e5a907d3c8613984684f2`. All 125 tracked files were exported and checked for matching contents and executable modes before migration edits. No Git history, branches, tags, or objects were imported. This repository was created independently for a fresh root commit.

## Intentional differences

| Surface | Change |
| --- | --- |
| Orchestrator | `skills/work/` moved to `skills/aasystem/`; metadata name, heading, and invocation examples renamed |
| Callers | Relative links and ownership references updated; specialist names and skill procedures preserved |
| Evaluations | Entry prompts and orchestration references renamed; private issue links replaced with the behavioral scope they describe |
| System graph | Public name, orchestrator label, source paths, and trace labels updated; internal node IDs and CSS selectors retained |
| Packaging | Root Agent Plugins 1.0 manifest and Claude compatibility manifest added with identity `aasystem`, version `0.1.0` |
| Licensing | MIT license for Ahmad Abdalla's original contributions added; both upstream notices and source attribution preserved |
| Documentation | README install guide, public branding, package export boundary, and this preparation context added |

The display name is **Ahmad Abdalla's Work System**. The proposed first release is `v0.1.0`. Preserve all invocation policies and specialist boundaries. Retained graph identifiers such as `work` are implementation details, not the installed orchestrator identity.

## Migration checks

- [x] Copy the complete tracked tree and verify the baseline before editing.
- [x] Use an independent private repository and exclude Work's history.
- [x] Rename the coordinating skill and update its callers, fixtures, and graph sources.
- [x] Add plugin manifests, MIT licensing, upstream attribution, and the README install guide.
- [x] Compare final files against the baseline with an explicit list of permitted changes; investigate every other difference.
- [x] Parse all skill frontmatter, invocation adapters, and manifests; validate local links and export contents.
- [x] Confirm both upstream notices match exactly, all 23 skills remain, and helpers and invocation policies are unchanged.
- [x] Inspect the graph overview, orchestrator trace, supporting route, and source links.
- [x] Validate marketplace registration, installation, enabled version, and packaged skill contents in isolated configurations for all three hosts.

Record observed checks separately from unexercised behavior. Native installation and metadata loading do not establish complete workflow correctness.

### Observed preparation checks

Checks on 2026-10-11 used an isolated local marketplace named `aasystem-validation`, with both native Codex and Claude-compatible catalogs. Personal host configurations were not used for installation.

| Host | Installed client | Result |
| --- | --- | --- |
| Codex CLI | `0.161.0` | Plugin `0.1.0` installed and enabled; `skills/list` discovers all 23 skills with no loading errors, including `aasystem:aasystem` |
| Claude Code | `2.1.251` | Marketplace added; plugin `0.1.0` installed and enabled |
| GitHub Copilot CLI | `1.0.84-8` | Marketplace added; plugin `0.1.0` enabled; installer reports 23 skills |

Installed skill trees match the candidate in all three hosts. Codex and Claude copy the package into their isolated caches; Copilot loads this local test source live.

The final tree retains all 125 source files under the renamed path mapping. There are 53 intentional identity/documentation edits, 72 unchanged files, and four added licensing, packaging, or preparation files. Skill procedures match the source after normalizing only the documented identity/reference changes. Original file modes are preserved.

The portable manifest passes the Agent Plugins 1.0 schema; the compatibility manifest passes `claude plugin validate .`. All 23 skill frontmatter records and Codex invocation adapters parse and retain explicit-only policies. All 386 local documentation links resolve after the README and Codex guide review, excluding two intentional template placeholders and links inside embedded example-project code blocks.

Both upstream notices match the source byte-for-byte. Python and shell helpers, YAML adapters, and graph CSS are unchanged. Disposable helper checks cover decision-log append/sanitization/header rejection and the verification-output check's clean-index and staged-output outcomes. Graph checks cover the overview, Feature selection and trace, an Architect supporting route, and source links; no JavaScript console errors were observed.

The baseline inventory, final migration diff, structural report, host installation transcripts, and Codex discovery response are retained locally outside the repository for review. Runtime workflow behavior, Claude/Copilot invocation behavior, refresh behavior, and fresh public marketplace installation remain unverified.

## Behavioral host validation

Use isolated installations so old personal skills cannot hide missing package content. Keep source/candidate identity, host version, exact prompt, actual reads/actions, results, and limitations with temporary test evidence through review.

For Codex, Claude Code, and GitHub Copilot CLI, exercise:

1. Explicit use of the coordinating skill and a directly selected specialist, confirming actual installed invocation names.
2. Supporting composition through a playbook, shared execution contract, principle index, and specialist references.
3. An unrelated ordinary prompt, checking the preserved explicit-only invocation policy.
4. A bounded investigation and a disposable implementation path with equivalent baseline/successor inputs and observed verification.
5. Plugin refresh/update behavior, confirming the loaded package version.

Use the existing [evaluation packages](evals/) and [evaluation playbook](skills/aasystem/playbooks/eval.md) for broader behavioral claims. Retain independent candidates and judging when required by that playbook. Existing fixtures do not prove that a run passed.

- [ ] Codex behavioral checks pass, with evidence and material limits recorded.
- [ ] Claude Code behavioral checks pass, with evidence and material limits recorded.
- [ ] GitHub Copilot CLI behavioral checks pass, with evidence and material limits recorded.

## Release and marketplace handoff

1. Publish the reviewed and approved successor to `main`; verify the new root commit has no Work ancestry.
2. Make `ahmadabdalla/aasystem` public for distribution testing, following the user's approved sequence. Behavioral host validation remains pending.
3. Prepare `aasystem` in `ahmadabdalla/plugins` using `https://github.com/ahmadabdalla/aasystem.git`, pinned to the published commit for initial installation tests. Keep manifest and catalog versions consistent. Tag a tested release as `v0.1.0` after validation.
4. Add or adapt the Codex-native `.agents/plugins/marketplace.json` catalog if required by tested clients. Preserve the marketplace identity `ahmadabdalla-plugins`.
5. Verify fresh public marketplace installs in all three hosts and remove the README's pending-installation notice once the advertised commands work.
6. Switch personal installations and future development to aasystem after replacement succeeds. Decide separately whether Work needs archiving or a private deprecation notice.

Later releases update the plugin version here, test and tag a new commit, then update the marketplace selector. Keep existing release tags immutable. Rollback during preparation uses the unchanged private Work library or the verified source snapshot; avoid maintaining two active copies after transition.

## References

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Claude plugin manifests](https://code.claude.com/docs/en/plugins-reference)
- [Claude plugin installation](https://code.claude.com/docs/en/plugins/install)
- [Copilot plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
