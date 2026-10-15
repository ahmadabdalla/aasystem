# Codex usage

See the [README](README.md#codex-cli) for installation.

## Invoke a skill

Start with `$aasystem:aapilot`. For direct specialist use, type `$aasystem:<skill-name>`, for example `$aasystem:product` or `$aasystem:how`. See the [README](README.md#start-here) for guidance on choosing an entry point.

Direct skill installations omit the plugin prefix, for example `$aapilot` or `$product`.

Keep the complete skill tree together. Follow the host's invocation restrictions and report any unavailable required handoff.

## Experimental bounded-autonomy PoC

Install the changed branch's complete `skills/` tree together through the host's supported standalone discovery, retaining sibling references, scripts, adapters and license notices. Record the installed revision and local differences. No plugin prefix is used for standalone `$aapilot` or `$architect`. Actual discovery and supporting-skill composition must be checked in that host; files on disk do not prove invocation.

Request the mode explicitly, for example `$aapilot Use the bounded-autonomy PoC to carry this authorized task through verification; return at the agreed human checkpoints.` A direct `$architect` assignment can request the same mode for design-only work. Preserve an explicit planning-only boundary when given.

The [bounded-work reference](skills/aapilot/references/bounded-work.md) owns usage and receipt fields. Its helper requires Python 3.10+ with no third-party dependencies and native delegation permitted by the actual host. Runtime state, reports and snapshots belong in the target project's evidence location outside the installed skill tree/cache; resolve the helper from that installed tree, independently of the current working directory. Local helper checks do not establish Codex discovery, worker isolation, automatic recovery or website behavior. The user performs the later website installation/exercise under the [PoC plan](docs/plans/issue-17-feature-flags-poc.md).

## Invocation policy

Every portable skill includes `agents/openai.yaml` with:

```yaml
policy:
  allow_implicit_invocation: false
```

Select skills explicitly; ordinary prompts do not activate them automatically. Codex reads these adapters. This document is documentation only.

Keep each adapter and its skill frontmatter consistent, preserving existing interface and dependency settings. Generated project verifiers retain their own scope and invocation settings.

See the [official invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata) and [system map](SKILL_SYSTEM.md).
