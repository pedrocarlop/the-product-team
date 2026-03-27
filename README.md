# Product Team

Product Team is an installable multi-agent workflow for Codex projects.

It packages this repository's orchestrator, specialist roles, shared references, and `/logs` contract so you can install them into any project folder and use them from Codex while preserving the source role-folder structure.

## What It Installs

- `.codex/agents/product-team-<discipline>/<role>/<role>.toml` for the namespaced role definitions
- `.codex/agents/product-team-<discipline>/<role>/skills/*.md` for each role's bundled local skills
- `.codex/product-team/` for package docs, shared references, manifest data, and install validation
- `logs/active/` and `logs/archive/`
- A managed `Product Team for Codex` block inside `AGENTS.md`
- `logs/README.md` if the target project does not already have one

## Install

Install directly from GitHub into the repository you are currently in:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/product-team/main/install.sh | bash -s -- --target "$PWD"
```

Install into the repository you are currently in:

```bash
./install.sh --target "$PWD"
```

Install into another existing local project folder:

```bash
./install.sh --target "$HOME/Projects/my-app"
```

You can also run the Python entrypoint directly:

```bash
python3 scripts/install.py --target "$PWD"
```

Use a real folder path. Do not pass placeholder values such as `/path/to/project` or `<project-path>`.

## Validate

After installation, validate the installed scaffold from the target repository root:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Source Layout

- `agents/` is the source of truth for all workflow roles and role-local skills.
- `logs/README.md` is the source of truth for the runtime `/logs` contract.
- `assets/AGENTS.fragment.md` is the managed `AGENTS.md` block injected during install.
- `assets/package-README.md` is copied into the installed package.
- `scripts/install.py` preserves the source role-folder structure inside the target repo's Codex layout.

## Notes

- The installer is idempotent for workflow-owned namespaced files.
- It does not overwrite unrelated files in the target repository.
- If the target repo already has `logs/README.md`, the installer keeps it and still creates the required `logs/active/` and `logs/archive/` directories.
