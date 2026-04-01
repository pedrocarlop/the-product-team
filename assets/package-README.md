# Product Team Package

This repository has the Product Team Codex workflow installed.

Every request in this repository should go through `product-team-orchestrator` by default. Only an explicit user opt-out for the current request should bypass Product Team. The orchestrator may still choose direct execution, but that choice is made inside the workflow.

The workflow is now role-split and skill-first:

- Business: `product-lead`, `analyst`, `business-ops`, `go-to-market`
- Design: `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer`
- Engineering: `frontend-engineer`, `backend-engineer`, `platform-engineer`
- Review: `design-reviewer`, `qa-reviewer`
- Support: `orchestrator`, `reference`

## Skill-First MCP Execution

When the orchestrator staffs specialists, it assigns work with an explicit contract:

- `assignment_mode`
- `owned_outputs`
- `reads_from`
- `repo_write_owner`
- `repo_write_scope`
- `return_expected`
- `skill_paths`
- `primary_tools`
- `fallback_policy`
- `evidence_mode`

Specialists execute the assigned skill workflow directly. They do not ask whether to use the skill's required toolchain first.

Global fallback rule:

`primary MCP -> alternative tool/MCP -> best guess inferred output`

Deliverables must label the actual evidence path as:

- `sourced`
- `fallback`
- `inferred`

Repo-tracked app code is stricter: one explicit implementation owner per stage by default.

## Installed Layout

- `.codex/agents/product-team-<discipline>/<role>/<role>.toml`
- `.codex/agents/product-team-<discipline>/<role>/skill-catalog.md`
- `.codex/agents/product-team-<discipline>/<role>/skills/*.md`
- `.codex/product-team/references/`
- `.codex/product-team/scripts/validate-install.py`
- `.codex/product-team/scripts/update-install.py`
- `.codex/product-team/manifest.json`
- `logs/active/`
- `logs/archive/`

## Validate

Run this from the project root:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Update To The Latest Package

Run this from the project root:

```bash
python3 .codex/product-team/scripts/update-install.py
```

## Example Routing

- Greenfield visual concept: `product-designer` -> `ui-designer` -> `frontend-engineer` -> `design-reviewer`
- Research-heavy discovery: `ux-researcher` -> `product-designer` -> `product-lead`
- API/platform delivery: `backend-engineer` or `platform-engineer` -> `qa-reviewer`

## Notes

- `AGENTS.md` contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` is created only when the target repo does not already have one.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- `.codex/product-team/manifest.json` records enough source metadata for installed repos to self-update later.
