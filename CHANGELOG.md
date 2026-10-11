# Changelog

## [0.2.0]

- Rename the main Codex invocation from `$aasystem:aasystem` to `$aasystem:aapilot`, and the Claude Code invocation from `/aasystem:aasystem` to `/aasystem:aapilot`.
- Introduce Ahmad Abdalla's Pilot System branding. Installation remains `aasystem@ahmadabdalla-plugins`.
- The former `aasystem` skill is removed; there is no invocation alias. Direct skill installations use `$aapilot`. Supporting skill names and invocation policies remain unchanged.
- Add package validation and a manual release process that publishes an annotated tag on the exact validated, merged release commit.

Existing `0.1.0` users must refresh their marketplace and update or reinstall the plugin, then start a fresh session. The temporary `0.1.0` SHA install already exposes `aapilot`, but still needs the versioned update once the marketplace adopts `v0.2.0`. See [upgrade instructions](RELEASING.md#upgrade-an-installed-plugin).

This release does not claim full workflow evaluation or universal host compatibility. Its publication notes link the actual host check evidence and any unavailable checks.
