#!/usr/bin/env python3
"""Owner-held bounded work receipts (Python 3.10+, state schema 2).

Records declarations and retained evidence; never executes native tools, controls
permissions, or authenticates humans. Keep state outside the installed skill tree.
init --brief FILE --state FILE; apply --state FILE --event FILE;
snapshot --state FILE --task ID --out NEW_DIRECTORY; status --state FILE.
Schema1 state is read-only historical status; snapshots retain separate schema1.

Brief: existing objective, authority/source/environment, actions/resources, budget,
claims/proof fields plus mandatory purpose: implementation|verification|other;
checkpoint_obligations:[{id,before:implementation|acceptance}] references allowed
checkpoints. required_review_mode defaults independent-discovery for production.
Child assignments also require purpose. Implementation needs decision_review ID
and inputs containing that review's exact artifact_refs. Verification needs
review:{target,mode:independent-discovery|confirmation-audit,claims:[IDs]}.

Events retain id,expected_revision,type,actor,task,source_ref plus payload:
decision_review: resources,artifact_refs,coverage,authority_revision,decisions,
unresolved,rationale. Decisions:{id,question,selected,classification,origin}.
Classification:product|architecture|routine. Origin: source {ref,locator,status:
accepted}; human {instruction_ref} or {checkpoint_event,resume_event,selected_option
only for choice}; delegated (routine only). Every accept needs decision_review.
assign:assignment (reserves one spawn, attempt_id=assignment.id).
dispatch_reserved:attempt_id,operation:followup,reason,worker_id (one extra charge).
dispatch:attempt_id,operation:spawn|followup,request_ref,host_ref,
outcome:started|failed|unknown,worker_id (required if started; no extra charge).
review_preflight:snapshot,environment,mode,context,host_request_ref, before dispatch.
initial_findings:preflight_event,dispatch_event,findings,context,context_evidence_refs.
Exactly one frozen initial report per verification assignment, before returned.
Context:{fresh,prior_conclusions,exposure,isolation_limits:[strings],exposures:
[{kind:prior-conclusions|other,stage:before-execution|during-execution|
after-execution-before-initial-findings,source_ref,description}]}.
Initial and final context also require interval_complete:true. Discovery forbids
prior conclusions throughout that interval. Final report initial_findings_event
references the frozen original; changed claims, commands, tested source or proof
facts need a fresh assignment, never an upgraded summary.

checkpoint:checkpoint_id,package,reason,decision. Package JSON:{question_id,
question,artifact_refs,decision_ids,options(optional)}. Free-text questions need
no invented options. Choice requires >=2 distinct {id,label,consequences} options
and recommendation. resume:checkpoint_id,authority_revision,human_response,
updated_brief(optional, no authority/budget widening). Response JSON:
{checkpoint_event,question_id,package_hash:SHA256,authority_revision,answer,
source_ref,selected_option(choice only)}. Human response source is retained.
returned:report; verification:target,verifier_task,report;
accept:decision_review,rationale,evidence_refs; interrupted:intended_effects,
last_worker_ref,observations; reconciled:evidence_refs,worker_active:false,
outcome:known|unknown,observations; cancelled:reason. No allocations are refunded.
Reports retain identity, native producer/host, source snapshot/environment/verifier,
claims/status/observations, commands/effects, evidence/artifacts, coverage/limits.
All paths are absolute nonsymlink regular local files. Production proof requires
successful executable checks by the started fresh noneditor worker, current source,
matching frozen first findings and the target's required review mode.
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
