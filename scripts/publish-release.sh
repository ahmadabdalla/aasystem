#!/usr/bin/env bash
# Adapted from Azure Cost Calculator's create-tag-and-release.sh and
# extract-changelog.sh; see docs/ops/releasing.md for attribution and operating steps.
set -euo pipefail

fail() { echo "FAIL: $*" >&2; exit 1; }

version="${1:?Usage: $0 <version> <merged-commit> <release-pr-url>}"
release_sha="${2:?Merged release commit is required}"
release_pr_url="${3:?Release PR URL is required}"
: "${GH_REPO:?Repository is required}"
: "${GH_TOKEN:?GitHub token is required}"
[[ "$version" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]] || fail 'Use a stable X.Y.Z version'
[[ "$release_sha" =~ ^[0-9a-f]{40}$ ]] || fail 'Expected a full merged commit SHA'
[[ "$release_pr_url" == "https://github.com/$GH_REPO/pull/"* ]] || fail 'Release PR must link to this repository'
[[ "$(git rev-parse HEAD)" == "$release_sha" ]] || fail 'Checkout differs from merged release commit'
git merge-base --is-ancestor "$release_sha" origin/main
git diff --exit-code HEAD -- . > /dev/null
python3 scripts/validate-release.py
[[ "$(jq -r .version plugin.json)" == "$version" ]] || fail 'PR version differs from manifest'

export RELEASE_TAG="v$version"
notes_file=$(mktemp)
trap 'rm -f "$notes_file"' EXIT
awk -v heading="## [$version]" '
  $0 == heading { found=1; next }
  /^## \[/ { if (found) exit }
  found { print }
' CHANGELOG.md > "$notes_file"
[[ -s "$notes_file" ]] || fail 'No changelog section for release version'
printf '\nValidated commit: `%s`\n\nRelease PR: %s\n' "$release_sha" "$release_pr_url" >> "$notes_file"

# API errors fail the run; an empty successful listing means no release exists.
existing=$(gh api --paginate "repos/$GH_REPO/releases?per_page=100" --jq '.[] | select(.tag_name == env.RELEASE_TAG)')
remote_tag=$(git ls-remote --tags origin "refs/tags/$RELEASE_TAG" "refs/tags/$RELEASE_TAG^{}")
if [[ -n "$remote_tag" ]]; then
  git fetch origin "refs/tags/$RELEASE_TAG:refs/tags/$RELEASE_TAG"
  [[ "$(git cat-file -t "refs/tags/$RELEASE_TAG")" == tag ]] || fail 'Existing tag is not annotated'
  [[ "$(git rev-parse "$RELEASE_TAG^{commit}")" == "$release_sha" ]] || fail 'Existing tag targets another commit'
elif [[ -n "$existing" ]]; then
  echo 'Release exists without its tag; refusing to recreate released contents.' >&2
  exit 1
else
  if git show-ref --verify --quiet "refs/tags/$RELEASE_TAG"; then
    [[ "$(git cat-file -t "refs/tags/$RELEASE_TAG")" == tag ]] || fail 'Local tag is not annotated'
    [[ "$(git rev-parse "$RELEASE_TAG^{commit}")" == "$release_sha" ]] || fail 'Local tag targets another commit'
  else
    git -c user.name='github-actions[bot]' -c user.email='41898282+github-actions[bot]@users.noreply.github.com' \
      tag -a "$RELEASE_TAG" "$release_sha" -m "Release $RELEASE_TAG"
  fi
  git push origin "refs/tags/$RELEASE_TAG"
fi

if [[ -n "$existing" ]]; then
  jq -e --arg title "$RELEASE_TAG" --rawfile notes "$notes_file" \
    '.name == $title and .body == $notes and .draft == false and .prerelease == false and (.assets | length) == 0' <<< "$existing" > /dev/null
  echo "PASS: $RELEASE_TAG already published with matching contents; nothing changed."
else
  gh release create "$RELEASE_TAG" --repo "$GH_REPO" --verify-tag --title "$RELEASE_TAG" --notes-file "$notes_file"
fi
printf 'Release: https://github.com/%s/releases/tag/%s\nCommit: %s\n' "$GH_REPO" "$RELEASE_TAG" "$release_sha"
