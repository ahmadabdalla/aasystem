# Codex usage

See the [README](../../README.md#codex-cli) for installation.

## Invoke a skill

Start with `$aasystem:aapilot`. For direct specialist use, type `$aasystem:<skill-name>`, for example `$aasystem:product` or `$aasystem:how`. See the [README](../../README.md#start-here) for guidance on choosing an entry point.

Direct skill installations omit the plugin prefix, for example `$aapilot` or `$product`.

Keep the complete skill tree together. Follow the host's invocation restrictions and report any unavailable required handoff.

## Verification contract

The contracts are host-independent. There is no demonstrated Codex integration satisfying the conditional [host acceptance contract](../../skills/aapilot/references/host-acceptance.md); ordinary skill invocation does not establish host-enforced acceptance.

Use the existing entry skill with the desired outcome; retained production changes use the [verification contract](../../skills/aapilot/references/verification-contract.md) by default. No special activation phrase is required. Read-only and design-only assignments keep their scoped boundaries. Direct Implement can own a request meeting [owner-presentation eligibility](../../skills/aapilot/references/execution.md#owner-presentation-eligibility); other production work retains separate verification and applicable human checkpoints.

Keep the complete [export tree](../design/skill-system.md#export-boundary), including runtime CLI, private Python package, references, adapters and license notices. The CLI ships with the skills; repository tests and temporary evaluation evidence stay outside that export. For standalone discovery, record the installed revision and local differences; invoke `$aapilot` or the relevant specialist without a plugin prefix. Check actual discovery and supporting-skill composition in that host; files on disk do not prove invocation.

The helper requires Python 3.10+ with no third-party dependencies. Resolve it from the installed tree independently of the working directory. Diagnose and repair missing Python/helper access within authority, or report validation unmet; do not silently bypass the receipt. State, reports and snapshots belong in the target project's evidence location outside the installed tree/cache. Native delegation requires actual host permission when needed. Applying a supporting skill in the current context does not dispatch a worker; retained owner implementation still requires a separate fresh verifier except under existing owner-presentation eligibility. Bounded unattended work requires an active supported session and explicit scope, authority, proof and stopping bounds. Local helper checks do not establish scheduling, worker isolation, session survival, automatic recovery or website behavior. Read [How Aapilot works](../design/verification-contract.md) for the operating design and its limits.

## Invocation policy

Every portable skill includes `agents/openai.yaml` with:

```yaml
policy:
  allow_implicit_invocation: false
```

Select skills explicitly; ordinary prompts do not activate them automatically. Codex reads these adapters. This document is documentation only.

Keep each adapter and its skill frontmatter consistent, preserving existing interface and dependency settings. Generated project verifiers retain their own scope and invocation settings.

See the [official invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata) and [system map](../design/skill-system.md).
