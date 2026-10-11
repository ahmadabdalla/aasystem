# Release aasystem

This repository publishes the plugin. [The marketplace](https://github.com/ahmadabdalla/plugins/issues/38) selects the published release in a separate reviewed PR.

`plugin.json` owns the version. Update `.claude-plugin/plugin.json` to match in the same release commit; `ruby scripts/validate-release.rb` rejects drift. Keep the installation name `aasystem` unchanged. Use stable `X.Y.Z` versions and annotated `vX.Y.Z` tags. Before 1.0, choose the increment deliberately; `0.2.0` records the entry-point change.

## Prepare and review

1. Create a branch from current `main`. Update both manifest versions and add a `## [X.Y.Z]` section to [CHANGELOG.md](CHANGELOG.md). Keep release notes, upgrade guidance and invocation examples coherent.
2. Run the checks below. Open a PR titled exactly `release: vX.Y.Z` targeting `main`. Include validation results and host evidence. Review and merge it through normal repository policy. No `dev` branch or automated release PR is needed.

```bash
ruby scripts/validate-release.rb
bash -n scripts/publish-release.sh
python3 -m unittest discover -s tests
```

The validator uses Ruby's standard library. It checks manifest JSON and identity/version agreement, all skill metadata and Codex adapters, inventory/export completeness, local Markdown link paths, current release notes and the shipped verification helper. Deliberate `disable-model-invocation` metadata remains supported. Link anchors, remote links, host discovery and full behavioral evaluations are separate checks. CI runs these commands on PRs and `main`.

GitHub Actions must be enabled under Settings → Actions → General. Confirm the PR has a successful `validate` check before merging; no check result means CI has not run.

## Check the merged artifact

Resolve the merged PR's `mergeCommit.oid` with `gh pr view NUMBER --json mergeCommit`. Check out that exact commit in a separate directory and rerun validation. A later `main` commit is not the release target.

Install that checkout through a temporary local marketplace or the host's supported local plugin path. Keep unrelated plugin configuration intact. For each available host, record:

- Host version, source commit and manifest version.
- Actual installation/discovery result and the discovered `aapilot` skill.
- A fresh-session read-only invocation: ask `aapilot` to state its name, purpose and main invocation, with no edits or delegation. Inspect the run to confirm it loads the installed skill.
- Evidence location and any missing host access or failed checks.

Record this evidence in a release PR comment, including the merged commit identity. A successful file check or documentation lookup is not an invocation result. A bounded smoke check is not a full engineering workflow evaluation. Marketplace fresh-install and existing-user upgrade verification remains owned by [plugins#38](https://github.com/ahmadabdalla/plugins/issues/38).

## Publish

After review, merge, successful merged-commit validation and host checks, run [Publish release](.github/workflows/publish-release.yml) on `main` with the merged PR number and host evidence comment URL:

```bash
gh workflow run publish-release.yml --ref main \
  -f release_pr=NUMBER \
  -f host_evidence=https://github.com/ahmadabdalla/aasystem/pull/NUMBER#issuecomment-ID
```

The workflow resolves the merged PR, verifies its title and destination, checks out its exact merge commit, and validates it again. Only its publication job has `contents: write`; it also has `pull-requests: read` to resolve the PR. It creates the annotated tag and GitHub Release with the changelog section, commit and evidence URL. It never uses a later branch head as the tag target.

Retry with the same inputs after a failure. An existing tag must be annotated and target the same commit. An existing release must have exactly the same title, notes and publication state, with no added assets. Conflicts fail; retries never move tags or edit releases. If the tag was pushed but release creation failed, rerunning finishes creation. API failures stop publication. Never delete or move a released tag to repair a retry; investigate the conflict first.

Confirm the successful Actions run, GitHub Release, both manifests at the tag and `git rev-parse 'vX.Y.Z^{commit}'`. Give the marketplace owner the version, tag, exact commit, release URL/notes, Actions run URL and host evidence. Keep [aasystem#2](https://github.com/ahmadabdalla/aasystem/issues/2) open until `v0.2.0` is published and those details reach plugins#38. This release PR alone does not complete the issue.

## Upgrade an installed plugin

These commands apply after the marketplace adopts the release. Marketplace refresh and installed-plugin update are distinct steps; start a fresh session afterward.

Codex CLI currently supports refresh and reinstall:

```bash
codex plugin marketplace upgrade ahmadabdalla-plugins
codex plugin remove aasystem@ahmadabdalla-plugins
codex plugin add aasystem@ahmadabdalla-plugins
codex plugin list --marketplace ahmadabdalla-plugins --json
```

Claude Code supports:

```bash
claude plugin marketplace update ahmadabdalla-plugins
claude plugin update aasystem@ahmadabdalla-plugins
```

Copilot CLI supports:

```bash
copilot plugin marketplace update ahmadabdalla-plugins
copilot plugin update aasystem@ahmadabdalla-plugins
```

Confirm the selected tag/commit, installed version and a read-only `aapilot` invocation. CLI help establishes available commands, not successful upgrades. The temporary Codex `0.1.0` SHA reinstall was [previously exercised](https://github.com/ahmadabdalla/plugins/issues/39#issuecomment-6106029360); the `0.2.0` upgrade matrix is pending marketplace adoption. Claude Code and Copilot upgrade results remain unverified until recorded there.

## Sources

The publication helper adapts Azure Cost Calculator's [tag/release helper](https://github.com/ahmadabdalla/azure-cost-calculator/blob/main/.github/scripts/release/create-tag-and-release.sh) and [changelog extraction](https://github.com/ahmadabdalla/azure-cost-calculator/blob/main/.github/scripts/release/extract-changelog.sh). Its `dev` staging, automated PR creation, pricing and scheduling machinery are unnecessary here. This adaptation adds exact commit selection and safe retries.

See [GitHub token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token), [Codex packaging and marketplace commands](https://developers.openai.com/plugins/build/plugins), and [Claude version/update behavior](https://code.claude.com/docs/en/plugins/host-marketplace#release-a-new-version).
