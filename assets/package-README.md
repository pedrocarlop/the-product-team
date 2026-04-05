# Product Team Package

## Validate

Run this from the project root:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Update

Run this from the project root:

```bash
python3 .codex/product-team/scripts/update-install.py
```

## What This Installed Workflow Does

This repository has the Product Team workflow installed.

Every request in this repository should go through `product-team-orchestrator` by default. Only an explicit user opt-out for the current request should bypass Product Team. The orchestrator may still choose direct execution, but that decision is made inside the workflow.

Product Team turns this repository into a routed product workflow with:

- an orchestrator that decides direct versus coordinated work
- specialist roles grouped by business, design, engineering, and review
- a shared memory surface: `/logs` for execution trail, `/knowledge` for deliverables, `/app` for code outputs
- strict assignment contracts so staffed work is explicit instead of improvised

## Role Topology

- Business: `product-lead`, `analyst`, `business-ops`, `go-to-market`
- Design: `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer`
- Engineering: `frontend-engineer`, `backend-engineer`, `platform-engineer`
- Review: `design-reviewer`, `qa-reviewer`
- Support: `orchestrator`, `reference`

## Shared Execution Contract

When the orchestrator staffs specialists, it assigns work with:

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

All staffed specialists follow the same operating model:

- read `skill-catalog.md` first
- open the assigned `skill_paths`
- execute the role-local skill workflow directly
- follow the fallback rule `primary MCP -> alternative tool/MCP -> best guess inferred output`
- label evidence as `sourced`, `fallback`, or `inferred`

Shared role deliverables use skill-owned anchors in the form `## Skill: <skill-name>` and preserve one trailing `## Reflection` footer for the role.

For greenfield product design, `ui-designer` seeds `knowledge/project-ds-spec.md` from up to 3 inspiration-only reference design-system kits in `.codex/product-team/references/reference-design-systems/`. For truly blank frontends, that same shared spec may also recommend a product-specific shadcn/ui foundation. `design-systems-designer` then expands the shared spec into tokens, atomic primitives, component families, widget/layout rules, governance, and QA guidance, and engineering may materialize the shadcn recommendation only when it is the explicit repo-write owner.

## Discipline Boundaries

- Business and design roles own advisory outputs in `/knowledge`; they do not own repo-tracked implementation in staffed workflows.
- Engineering roles may edit repo-tracked files only when they are the explicit `repo_write_owner` for that stage and the `repo_write_scope` is bounded.
- `reference` is read-only support for grounding, tracing, reuse, and verification.

For new design work, the design flow must diverge before it converges. `ui-designer` should explore multiple materially different high-level directions first, compare them explicitly, and only then move into `screen-production-design`.

## Installed Layout

- `.codex/agents/product-team-<discipline>/<role>/<role>.toml`
- `.codex/agents/product-team-<discipline>/<role>/capabilities.md`
- `.codex/agents/product-team-<discipline>/<role>/skill-catalog.md`
- `.codex/agents/product-team-<discipline>/<role>/skills/*.md`
- `.codex/product-team/references/`
- `.codex/product-team/references/project-ds-spec-template.md`
- `.codex/product-team/references/reference-design-systems/`
- `.codex/product-team/scripts/validate-install.py`
- `.codex/product-team/scripts/update-install.py`
- `.codex/product-team/scripts/lib/`
- `.codex/product-team/manifest.json`
- `logs/active/` and `logs/archive/`
- `knowledge/` (deliverables, reviews, runs)
- `app/` (code outputs)

## Notes

- AGENTS.md contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` and `knowledge/README.md` are created only when the target repo does not already have them.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- `.codex/product-team/manifest.json` records enough source metadata for installed repos to self-update later.
