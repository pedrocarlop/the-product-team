# Product Team

[Read this in Spanish](./README.es.md)

## Install

From a local checkout:

```bash
./install.sh --target "$PWD"
```

From GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

With Python:

```bash
python3 scripts/install.py --target "$PWD"
```

Validate an installed project:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

Update an installed project later:

```bash
python3 .codex/product-team/scripts/update-install.py
```

## What It Does

Product Team is an installable Codex workflow for repositories that want agent work to behave more like a real product team.

It installs:

- one orchestrator that routes the request
- a split set of specialist roles across business, design, engineering, and review
- a shared `/logs` memory surface for context, deliverables, decisions, and status
- a managed `AGENTS.md` block that makes Product Team the default entrypoint in the target repo

The main operating rule is: use the lightest process that will still do the job well.

That means Product Team does not staff a team for every request. The orchestrator first decides whether the work should stay direct or become coordinated. When coordination helps, it staffs the smallest useful set of roles.

## How The Roles Work

The repo is structured around role-local assets under `agents/<discipline>/<role>/`. Across business, design, and engineering, the roles follow the same pattern:

- one role TOML with the system prompt and execution policy
- one `capabilities.md` card
- one `skill-catalog.md` that must be read first
- a set of role-local `skills/*.md` workflows

The current role topology is:

- Business: `product-lead`, `analyst`, `business-ops`, `go-to-market`
- Design: `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer`
- Engineering: `frontend-engineer`, `backend-engineer`, `platform-engineer`
- Review: `design-reviewer`, `qa-reviewer`
- Support: `orchestrator`, `reference`

What is consistent across the specialist roles:

- they work from orchestrator-issued assignments only
- they read `skill-catalog.md` first and then the assigned `skill_paths`
- they execute a concrete skill workflow, not a generic role summary
- they follow the same fallback rule: `primary MCP -> alternative tool/MCP -> best guess inferred output`
- they label evidence as `sourced`, `fallback`, or `inferred`
- they write deliverables to `knowledge/` and execution records to `logs/active/<project-slug>/`

The design side now has an explicit shared design-system handoff:

- `ui-designer` can seed `knowledge/project-ds-spec.md` for greenfield work
- that seed is built from up to 3 inspiration-only references in the bundled reference design-system library
- for truly blank frontends, that seed can also recommend a spec-backed shadcn/ui foundation instead of leaving primitives undefined
- `design-systems-designer` then turns that shared spec into tokens, primitives, component families, layout/widget rules, governance, and QA guidance

The main discipline boundary is intentional:

- Business and design roles are advisory artifact owners. In coordinated workflows they do not own repo-tracked implementation.
- Engineering roles may edit repo-tracked files only when the orchestrator gives explicit implementation ownership and a bounded `repo_write_scope`.
- `reference` is read-only support for grounding, tracing, reuse, and verification.

## How Requests Flow

1. A request enters through `product-team-orchestrator`.
2. The orchestrator reads its own skill catalog and chooses direct or coordinated execution.
3. If the work is simple and clearly single-role, it may stay direct.
4. If the work is cross-functional or high-risk, the orchestrator staffs the minimum viable set of roles.
5. Staffed roles receive an explicit assignment contract with fields like `skill_paths`, `owned_outputs`, `primary_tools`, `fallback_policy`, `repo_write_owner`, and `evidence_mode`.
6. Work is recorded in `logs/` (execution trail) and `knowledge/` (deliverables) so the state survives beyond chat context. Code outputs go to `app/`.

For new design work, the workflow is intentionally not linear from idea to polish. The design path should diverge before it converges: explore materially different directions first, compare them, and only then move into production design and implementation.

For greenfield product design, that usually means:

1. `ui-designer` explores concept directions and chooses a direction.
2. `ui-designer` seeds `project-ds-spec.md` from the reference design-system kits/library.
3. If the frontend is blank and the spec justifies it, that shared spec can recommend a shadcn/ui baseline with product-specific setup choices.
4. `design-systems-designer` operationalizes that shared spec into the product's own system rules.
5. Later screen and component work inherits from `project-ds-spec.md`, not directly from company references, and engineering may materialize the shadcn recommendation only when it explicitly owns repo writes.

## Installed Layout

The installer keeps Product Team namespaced and idempotent. The main installed paths are:

- `.codex/agents/product-team-<discipline>/<role>/`
- `.codex/product-team/`
- `.codex/product-team/references/project-ds-spec-template.md`
- `.codex/product-team/references/reference-design-systems/`
- `logs/active/` and `logs/archive/`
- `knowledge/` (deliverables, reviews, runs)
- `app/` (code outputs)

It may update workflow-owned files and the managed `AGENTS.md` block, but it should not overwrite unrelated project files.

## Logs And Memory

`logs/README.md` is the contract for persistent project memory.

In practice:

- `context.md` tracks the objective, status, staffed roles, exact `skill_paths`, and done-when criteria
- `deliverables/` holds role deliverables
- `deliverables/project-ds-spec.md` can act as a shared design artifact across `ui-designer` and `design-systems-designer`
- `decisions/` holds durable decisions
- `TIMELINE.md` indexes project work over time

Routing, staffing, and approval happen in context, but the durable project record lives under `/logs`.

## Maintaining This Package

Source of truth:

- `agents/`: role definitions and role-local skills
- `logs/README.md`: runtime `/logs` contract
- `install.sh` and `scripts/install.py`: installer entrypoints
- `assets/AGENTS.fragment.md`: managed `AGENTS.md` block injected into target repos
- `assets/package-README.md`: README copied into installed projects

If you change role structure, prompts, routing, or installer behavior, validate with:

```bash
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Then run a real install into a temporary folder and validate it:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Short Version

Product Team installs a coordinated Codex workflow into another repository. It keeps simple work simple, adds coordination only when it helps, routes through real business/design/engineering roles, and leaves a written operating record in `/logs`.
