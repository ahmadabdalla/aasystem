# Codex usage

See the [README](README.md#codex-cli) for installation.

## Invoke a skill

Start with `$aasystem:aasystem`. For direct specialist use, type `$aasystem:<skill-name>`, for example `$aasystem:product` or `$aasystem:how`. See the [README](README.md#start-here) for guidance on choosing an entry point.

Direct skill installations omit the plugin prefix, for example `$aasystem` or `$product`.

Keep the complete skill tree together. Follow the host's invocation restrictions and report any unavailable required handoff.

## Invocation policy

Every portable skill includes `agents/openai.yaml` with:

```yaml
policy:
  allow_implicit_invocation: false
```

Select skills explicitly; ordinary prompts do not activate them automatically. Codex reads these adapters. This document is documentation only.

Keep each adapter and its skill frontmatter consistent, preserving existing interface and dependency settings. Generated project verifiers retain their own scope and invocation settings.

See the [official invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata) and [system map](SKILL_SYSTEM.md).
