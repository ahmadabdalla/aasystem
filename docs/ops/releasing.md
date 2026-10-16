# Release aasystem

Merging a manually prepared release PR into `main` automatically creates its tag and GitHub Release after validation, then opens or updates a reviewed adoption PR in `ahmadabdalla/plugins`. The package layout and installation identity stay unchanged. `main` accumulates work between releases; marketplace installs use immutable published tags.

## Maintainer setup

Use Python 3.10+, Git, Bash, a POSIX shell and `jq` for repository checks. Publication also needs the authenticated GitHub CLI (`gh`). Create a virtual environment and install the pinned development dependencies from [requirements-dev.txt](../../requirements-dev.txt):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
. .venv/bin/activate
```

PyYAML provides real YAML parsing for the release validator and workflow tests. It is a development dependency only; the shipped work-receipts helper still uses Python 3.10+ and the standard library without third-party dependencies. Neither repository checks nor installed skills require Ruby.

For a cloud environment, make Python (including `venv`), Git, Bash, a POSIX shell and `jq` available in the base image. Use these install instructions after checkout, adjusting the checkout path if needed:

```bash
cd /workspace/aasystem
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Use these start instructions for each session so subprocesses also use the environment's Python:

```bash
cd /workspace/aasystem
. .venv/bin/activate
python3 scripts/validate-release.py
bash -n scripts/publish-release.sh
python3 -m unittest discover -s tests
```

## Prepare and merge

1. Choose the version in `plugin.json`, then set the same version in `.claude-plugin/plugin.json`. Keep the name `aasystem`.
2. Add a `## [X.Y.Z]` section to `CHANGELOG.md` describing the changes and any upgrade steps.
3. Run the checks below and test installation plus a read-only `aapilot` invocation in each available host. Put results and any gaps in the PR.
4. Open a PR titled exactly `release: vX.Y.Z`, targeting `main`. Review it and wait for the `validate` check to pass, then merge.

```bash
python3 scripts/validate-release.py
bash -n scripts/publish-release.sh
python3 -m unittest discover -s tests
```

Choose major, minor or patch in the PR; the workflow doesn't guess. `plugin.json` is the version source. Use patch versions for compatible fixes, minor versions for new capabilities, and major versions for breaking changes once at 1.0. Before 1.0, put breaking changes in a minor release and describe migration steps. Ordinary PR merges don't publish releases. Keep upcoming notes under `Unreleased`, then collect them into the chosen version's section when preparing a release.

PR CI requires a version change to have the exact matching release title, target `main`, increase the version from the PR base, keep both manifests in sync and include nonempty versioned notes. A release-titled PR without an increase also fails. Title edits rerun validation. Require the `validate` status check with branches up to date in branch protection; workflow checks alone cannot prevent a bypassed merge.

The workflow checks the exact merged commit, runs the tests and package validator, then publishes an annotated `vX.Y.Z` tag. The release notes include the changelog, commit and PR. These package checks don't claim full host or workflow correctness.

Confirm the **Publish release** run succeeded and the tag points to the merged commit. Its `marketplace` job validates the catalog and opens or updates one PR on `automation/aasystem-release`, including the version, tag, exact commit, release URL and check results. Review that PR and record available host checks before merging. A successful package release is not yet marketplace adoption, and catalog adoption does not update installed plugins.

Previously, maintainers copied the release evidence and edited the marketplace version, ref and README in a second repository. Now they prepare and merge the release PR, then review and merge the generated catalog PR. Consumer steps below stay the same. No package relocation, new marketplace identity or host source-layout migration is involved.

## Marketplace automation setup

Merge the linked marketplace validation PR before enabling the handoff. It adds `scripts/validate-marketplace.py --base` and PR CI. Require its `validate` check with branches up to date before catalog merges.

Create a GitHub App installed only on `ahmadabdalla/plugins`, with repository **Contents: read and write** and **Pull requests: read and write** permissions (Metadata read is implicit). In aasystem Actions settings, set repository variable `MARKETPLACE_APP_ID` and secret `MARKETPLACE_APP_PRIVATE_KEY`. The workflow requests a short-lived token scoped to that repository and those permissions. This App token, unlike the source repository's default `GITHUB_TOKEN`, can write the sister repository and trigger its PR CI. Do not grant workflow or administration write access.

Missing App configuration fails the marketplace job visibly after publication. Configure it and rerun the failed job; do not republish or change the released version. Newer adoptions replace the same pending PR. Older retries skip an already adopted or newer pending version. Conflicting tags or release contents still stop publication and are preserved.

## Retry a failed or missed release

Rerun the failed Actions job. For a release PR merged before automation was enabled, run this on `main`, replacing `your_pr_number`:

```bash
gh workflow run publish-release.yml --ref main -f release_pr=your_pr_number
```

Retries use the same PR and commit, including a successful matching publication retry before marketplace handoff. Marketplace preparation uses the workflow's exact commit, so it does not drift with `main` and can still adopt older releases that lack the preparation helper. Conflicting tags or release contents stop publication; never move a released tag or overwrite its contents.

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

