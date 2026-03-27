# Product Team Package

This repository has the Product Team Codex workflow installed.

The workflow runs in phases: the orchestrator decides solo/direct vs multi-agent work, gathers one advisory planning pass from the selected specialists, merges that advice into a single approved work plan, and then coordinates execution. Material replanning should happen through a new full cycle, not by repeated mid-flight rework.

Before the orchestrator narrows the team, it should read the full canonical role catalog in `.codex/product-team/references/role-catalog.md`.

## Installed Layout

- `.codex/agents/product-team-<discipline>/<role>/<role>.toml`
- `.codex/agents/product-team-<discipline>/<role>/skills/*.md`
- `.codex/product-team/references/`
- `.codex/product-team/scripts/validate-install.py`
- `.codex/product-team/manifest.json`
- `logs/active/`
- `logs/archive/`

## Validate

Run this from the project root:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Notes

- `AGENTS.md` contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` is created only when the target repo does not already have one.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- Shared workflow references, including the role catalog and `/logs` contract, live under `.codex/product-team/references/`.
