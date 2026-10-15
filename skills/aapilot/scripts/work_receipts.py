#!/usr/bin/env python3
"""Owner-held bounded work receipts (Python 3.10+, schema 1).

No commands, agents, permissions or human identities are authenticated/executed.
init --brief FILE --state FILE; apply --state FILE --event FILE;
snapshot --state FILE --task ID --out NEW_DIRECTORY; status --state FILE.
All JSON paths are absolute local regular files/directories, never symlinks.
Source: {mode: git|roots, roots: [paths], exclude: [paths], required: [files]}.
Git mode selects tracked working-tree and nonignored untracked files. Roots mode
is explicitly scoped. The state directory is a visible automatic exclusion and
must not contain any required input. Snapshots live inside that runtime directory;
its archive is protected input, not a writable verification workspace.

Brief: id, owner, project_root, objective, requirements, decisions, procedures,
principles (file lists), authority_source (file), actions, resources (ID->absolute
path or named:VALUE), checkpoints (IDs), budget {dispatches, deadline_utc}, claims,
proof_kind (scoped|production), source, environment (nonsecret JSON descriptor),
constraints, expected_outputs, next_action. Child assignment: id,parent,owner,
objective,procedure(file),actions,resources(IDs),claims,proof_kind,inputs(files),
expected_artifacts, optional deadline_utc,required(default true),supersedes.

Events: id,expected_revision,type,actor,task,source_ref(file), plus:
assign: assignment; returned: report(file); verification: target,verifier_task,
report(file); accept: rationale,evidence_refs(files); checkpoint: checkpoint_id,
package(file),reason,decision; resume: checkpoint_id,authority_revision,
human_response(file), updated_brief(optional complete brief); interrupted:
intended_effects,last_worker_ref,observations; reconciled: evidence_refs(files),
worker_active(false),outcome(known|unknown),observations; cancelled: reason.
Resume forbids grant/budget/deadline widening in v0; new authority needs a new run.

Report: id,task,producer,host_ref(file),editors(list),review_mode,
context {fresh,prior_conclusions,exposure,isolation_limits}, snapshot(manifest),
environment(file),verifier(file),artifacts(files),evidence(files),claims
{claim:{status:pass|fail|unverified,observations}},commands
[{command,exit_code}],effects,coverage,limitations. Production proof additionally
needs executable:true, fresh:true, prior_conclusions:false, a distinct producer
from ALL declared editors and artifact producers, and actual command metadata.
These are declarations; actual execution, source completeness and semantic truth
remain owner/verifier responsibilities. Reports without proof metadata can return
artifacts, but cannot verify claims. Every imported file is retained by hash;
report JSON bytes are retained in state. IDs are immutable and retries idempotent.
"""
from __future__ import annotations

import argparse
import json
import sys

# Installed helpers must not write bytecode into the portable skill tree.
sys.dont_write_bytecode = True

from _work_receipts import state
from _work_receipts.evidence import Rejected


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subcommands = parser.add_subparsers(dest='command', required=True)
    for name in ('init', 'apply', 'snapshot', 'status'):
        command_parser = subcommands.add_parser(name)
        command_parser.add_argument('--state', required=True)
        if name == 'init':
            command_parser.add_argument('--brief', required=True)
        if name == 'apply':
            command_parser.add_argument('--event', required=True)
        if name == 'snapshot':
            command_parser.add_argument('--task', required=True)
            command_parser.add_argument('--out', required=True)
    return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        result = state.execute_command(args)
        print(json.dumps({'ok': True, **result}, sort_keys=True))
        return 0
    except (Rejected, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, sort_keys=True))
        return 1

if __name__ == '__main__':
    sys.exit(main())
