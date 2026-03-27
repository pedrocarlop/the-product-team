# Product Team Package

This repository has the Product Team Codex workflow installed.

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
- Shared business and engineering source lists live under `.codex/product-team/references/`.
