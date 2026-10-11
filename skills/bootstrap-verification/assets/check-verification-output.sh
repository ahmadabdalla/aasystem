#!/bin/sh
# Set this to the project's repository-relative temporary run directory.
temporary_runs='.verification/runs/'

if ! indexed=$(git -c core.quotePath=true ls-files --cached --full-name -- ":(top,literal)$temporary_runs"); then
    printf '%s\n' 'Cannot inspect temporary verification output in Git.' >&2
    exit 2
fi

if [ -n "$indexed" ]; then
    printf '%s\n' "Temporary verification output is in Git's index:" "$indexed" >&2
    printf '%s\n' 'Review retention and links before moving or untracking these files.' >&2
    exit 1
fi

printf '%s\n' 'PASS: no temporary verification output in Git index.'
