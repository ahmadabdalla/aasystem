# Release aasystem

Merging a release PR into `main` automatically creates its tag and GitHub Release after validation.

## Maintainer setup

Use Python 3.10+, Git, Bash, a POSIX shell and `jq` for repository checks. Publication also needs the authenticated GitHub CLI (`gh`). Create a virtual environment and install the pinned development dependencies from [requirements-dev.txt](requirements-dev.txt):

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

Choose major, minor or patch in the PR; the workflow doesn't guess. `plugin.json` is the version source. Ordinary PR merges don't publish releases.

The workflow checks the exact merged commit, runs the tests and package validator, then publishes an annotated `vX.Y.Z` tag. The release notes include the changelog, commit and PR. These package checks don't claim full host or workflow correctness.

Confirm the **Publish release** run succeeded and the tag points to the merged commit. Give the marketplace owner the version, tag, commit, release URL and check results for a separate catalog PR.

## Retry a failed or missed release

Rerun the failed Actions job. For a release PR merged before automation was enabled, run this on `main`, replacing `your_pr_number`:

```bash
gh workflow run publish-release.yml --ref main -f release_pr=your_pr_number
```

Retries use the same PR and commit. Conflicting tags or release contents stop publication; never move a released tag or overwrite its contents.

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

