# Prototype

Own the decision the experiment resolves. The output is evidence and a recommendation; the scratch artifact is not the production implementation.

1. **Define the decision.** State the alternatives and the observation that could distinguish them using [probe](../../probe/SKILL.md). If the request already specifies a production feature, route to Feature instead of disguising it as an experiment.
2. **Gather relevant references.** For an open visual or interaction question, inspect prior art and requirements. Resolve a material user preference only when it cannot be inferred; ask one question and wait if necessary.
3. **Build the smallest credible experiment.** For an inspectable business-state model or contextual UI alternatives, build or assign the artifact using [prototype](../../prototype/SKILL.md), supplying the question, authority, scope and evidence destination. For other experiments, continue with Probe's method. This playbook retains the decision and handoff; the supporting skill returns evidence without starting production work.
4. **Observe on the matching surface.** Drive the interaction, inspect the output, or measure the relevant behavior. Check that the method measures the claimed thing. Capture inputs, environment, observations, and limits. A prototype does not establish production reliability or integration readiness.
5. **Recommend and hand off.** Return the alternatives, evidence, decision or inconclusive result, and scratch path. For authorized production work, return the direction and limits to the owner for the change playbook and Architect design when needed; otherwise end with the decision.
