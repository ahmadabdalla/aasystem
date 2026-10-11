# Release aasystem

Prepare a release PR, verify its merged commit, then publish. This repository publishes the plugin; [the marketplace](https://github.com/ahmadabdalla/plugins/issues/38) adopts it separately.

## 1. Prepare the release PR

Create a branch from `main`, then:

1. Use [plugin.json](plugin.json) as the version source. Update [.claude-plugin/plugin.json](.claude-plugin/plugin.json) to match in the same commit. Keep the name `aasystem`.
2. Add a `## [X.Y.Z]` section to [CHANGELOG.md](CHANGELOG.md), including invocation changes and upgrade instructions.
3. Run these checks:

```bash
ruby scripts/validate-release.rb
bash -n scripts/publish-release.sh
python3 -m unittest discover -s tests
```

Open a PR targeting `main`, titled exactly `release: vX.Y.Z`. Get it reviewed and confirm the `validate` check passes before merging. If no check appears, enable GitHub Actions under **Settings → Actions → General**.

Use `X.Y.Z` versions and `vX.Y.Z` tags. Before 1.0, choose the increment deliberately: `0.2.0` records the entry-point change.

The [validator](scripts/validate-release.rb) uses Ruby's standard library. It checks manifests, skill metadata/adapters, package files, local link paths, release notes and the shipped helper. Host behavior, full workflow evaluations, remote links and link anchors need separate checks.

## 2. Verify the merged commit

Find the exact commit to release, replacing `your_pr_number`:

```bash
gh pr view your_pr_number --json mergeCommit --jq .mergeCommit.oid
```

Check out that commit in a separate directory and rerun the checks above. Install it through a temporary local marketplace or a supported local plugin path.

In a fresh session, ask `aapilot` to state its name, purpose and main invocation. Allow reads only, with no edits or delegation. Confirm the run loads the installed skill.

Record the results in a release PR comment:

- Host version, source commit and plugin version
- Installation, discovery and invocation results, with evidence
- Failed or unavailable host checks

## 3. Publish and hand off

After merged-commit validation and host checks, run [Publish release](.github/workflows/publish-release.yml). Replace the placeholders with the PR number and evidence comment URL:

```bash
gh workflow run publish-release.yml --ref main \
  -f release_pr=your_pr_number \
  -f host_evidence=your_host_evidence_comment_url
```

The workflow validates the exact merged commit, then publishes an annotated tag and GitHub Release with the changelog and evidence links.

If publication fails, retry with the same inputs. A retry can finish release creation after its tag was pushed. Existing tags and releases must match; conflicts stop the run. Investigate conflicts without deleting or moving released tags or editing released contents.

Confirm the successful Actions run, release notes and both manifests at the tag. Check its commit with `git rev-parse 'vX.Y.Z^{commit}'`.

## Upgrade an installed plugin

After marketplace adoption, refresh the catalog and update the installed plugin. Start a fresh session afterward.

For Codex, refresh and reinstall:

```bash
codex plugin marketplace upgrade ahmadabdalla-plugins
codex plugin remove aasystem@ahmadabdalla-plugins
codex plugin add aasystem@ahmadabdalla-plugins
codex plugin list --marketplace ahmadabdalla-plugins --json
```

For Claude Code:

```bash
claude plugin marketplace update ahmadabdalla-plugins
claude plugin update aasystem@ahmadabdalla-plugins
```

For Copilot CLI:

```bash
copilot plugin marketplace update ahmadabdalla-plugins
copilot plugin update aasystem@ahmadabdalla-plugins
```

