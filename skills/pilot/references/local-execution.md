# Local execution

## Workspaces and cleanup

If the task's edits must stay out of the main checkout, give the task one worktree and reuse it for every correction round. Give each parallel worker its own. A new worktree lacks another checkout's uncommitted and ignored files, so pass required inputs on purpose.

A worktree or copy isn't a sandbox: it still shares databases, ports and services, so give each run its own fixtures or run those checks one at a time.

Copy the project only for a check that can't run in the working directory. List every input the copy needs, not just the changed files, and check the disk has room. If the project has its own isolation, use it.

Stop and delete only what you or your workers started. If you're unsure, leave it and report it. Never use recursive checkout deletion or forced worktree removal as routine cleanup. A worktree with changes waiting for review is a deliverable.

## Tested identity

You choose which inputs matter. A matching hash shows only that they didn't change, not that the running instance uses them; check that too.

Use the project's identity check if it has one. If not, use the read-only [input identity helper](../scripts/input_identity.py); `--help` gives usage. Keep its output outside the checked inputs. It refuses directories, symlinks, submodules and special files; those need a project procedure.

If tests generate source, reset it before you take the first fingerprint.
