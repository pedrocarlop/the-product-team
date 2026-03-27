# Product Team Package

This repository packages an installable Codex workflow called `Product Team`.

## Source Of Truth

- The role definitions and role-local skills live under `agents/`.
- The runtime `/logs` contract lives in `logs/README.md`.
- The installer entrypoints are `install.sh` and `scripts/install.py`.
- The managed `AGENTS.md` block injected into target repositories lives at `assets/AGENTS.fragment.md`.
- The installed package readme lives at `assets/package-README.md`.

## Package Rules

- Keep the package project agnostic and Codex specific.
- Keep installed assets namespaced under `.codex/product-team/` and `.codex/agents/product-team-*`.
- Preserve the current source layout as the authoring surface; do not create a second hand-maintained template tree.
- Keep installer behavior idempotent. It may update workflow-owned namespaced files and the managed `AGENTS.md` block, but it must not overwrite unrelated target-project files.
- If you add, remove, or rename a role, update the installer transforms, managed docs, and install validator together.

## Validation

- Run `scripts/validate-orchestrator-contract.sh` after source-structure changes.
- Run `python3 scripts/check-orchestrator-scenarios.py` after prompt or routing changes.
- Run a real install into a temporary folder and then run `python3 .codex/product-team/scripts/validate-install.py`.
- Treat validation failures as blockers.
