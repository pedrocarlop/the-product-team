# Product Team

[Read this in Spanish](./README.es.md)

## Install

### Codex (default)

From a local checkout:

```bash
./install.sh --target "$PWD"
```

From GitHub:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrocarlop/the-product-team/main/install.sh | bash -s -- --target "$PWD"
```

### Claude Code

```bash
./install.sh --platform claude --target "$PWD"
```

Or with the shortcut wrapper:

```bash
./install-claude.sh --target "$PWD"
```

### Antigravity

```bash
./install.sh --platform antigravity --target "$PWD"
```

Or with the shortcut wrapper:

```bash
./install-antigravity.sh --target "$PWD"
```

### With Python directly

```bash
python3 scripts/install.py --target "$PWD"
python3 scripts/install.py --platform claude --target "$PWD"
python3 scripts/install.py --platform antigravity --target "$PWD"
```

### Validate and update

```bash
python3 .codex/product-team/scripts/validate-install.py
python3 .codex/product-team/scripts/update-install.py
```

## What It Does

Product Team is an installable workflow for repositories that want agent work to behave more like a real product team.

It installs:

- one orchestrator that routes each request
- a set of specialist roles across business, design, engineering, and review
- three output surfaces: `/logs` (execution trail), `/knowledge` (deliverables), `/app` (code)
- a managed block in `AGENTS.md`, `CLAUDE.md`, or `ANTIGRAVITY.md` that makes Product Team the default entrypoint

The main operating rule is: **use the lightest process that will still do the job well.**

Product Team does not staff a team for every request. The orchestrator first decides whether the work should stay direct or become coordinated. When coordination helps, it staffs the smallest useful set of roles.

## How The Roles Work

The repo is structured around role-local assets under `agents/<discipline>/<role>/`. Each role follows the same pattern:

- one `.toml` file with the system prompt and execution policy
- one `capabilities.md` card
- one `skill-catalog.md` that must be read first
- a set of `skills/*.md` workflows

The current role topology (16 specialists + 1 orchestrator + 1 reference helper = 18 total):

| Discipline | Roles |
|---|---|
| Business | `product-lead`, `analyst`, `business-ops`, `go-to-market` |
| Design | `ux-researcher`, `product-designer`, `ui-designer`, `content-designer`, `design-systems-designer` |
| Engineering | `frontend-engineer`, `backend-engineer`, `platform-engineer` |
| Review | `design-reviewer`, `qa-reviewer` |
| Support | `orchestrator`, `reference` |

What is consistent across specialist roles:

- they work from orchestrator-issued assignments only
- they read `skill-catalog.md` first and then the assigned `skill_paths`
- they execute a concrete skill workflow, not a generic role summary
- they follow the same fallback rule: `primary MCP -> alternative tool/MCP -> best guess inferred output`
- they label evidence as `sourced`, `fallback`, or `inferred`
- they write deliverables to `knowledge/` and execution records to `logs/active/<project-slug>/`

The main discipline boundary is intentional:

- **Business and design** roles are advisory artifact owners. In coordinated workflows they do not own repo-tracked implementation.
- **Engineering** roles may edit repo-tracked files only when the orchestrator gives explicit implementation ownership and a bounded `repo_write_scope`.
- **Reference** is read-only support for grounding, tracing, reuse, and verification.

## Assignment Contract

When the orchestrator staffs specialists, every assignment includes:

| Field | Purpose |
|---|---|
| `run_id` | Unique identifier for the current execution stage |
| `assignment_mode` | `primary_executor`, `lean_input`, or `peer_reviewer` |
| `owned_outputs` | Paths in `knowledge/` this agent will write |
| `reads_from` | Paths in `knowledge/` this agent must read (including prior projects) |
| `repo_write_owner` | Role name that owns repo writes, or null |
| `repo_write_scope` | Path in `app/` for code outputs, or null |
| `return_expected` | Brief description of expected deliverable |
| `skill_paths` | Exact skill workflows to execute |
| `primary_tools` | Required MCP servers/tools |
| `fallback_policy` | Alternative tool or `best guess inferred output` |
| `evidence_mode` | `sourced`, `fallback`, or `inferred` |

The global fallback rule is: `primary MCP -> alternative tool/MCP -> best guess inferred output`.

## How Requests Flow

1. A request enters through `product-team-orchestrator`.
2. The orchestrator reads its own skill catalog and chooses direct or coordinated execution.
3. If the work is simple and clearly single-role, it may stay direct.
4. If the work is cross-functional or high-risk, the orchestrator staffs the minimum viable set of roles.
5. Staffed roles receive an explicit assignment contract.
6. Each specialist reads `skill-catalog.md`, opens the assigned `skill_paths`, and executes that workflow.
7. Deliverables go to `knowledge/` (canonical + snapshot in `knowledge/runs/<run-id>/`). Code goes to `app/`. Execution records go to `logs/`.

For new design work, the workflow is intentionally not linear. The design path should **diverge before it converges**: explore materially different directions first, compare them, and only then move into production design and implementation.

## Knowledge System

`knowledge/README.md` is the contract for persistent business intelligence. Knowledge is organized as a **persistent, compounding wiki** — compiled once and kept current, not rediscovered on each query.

Key rules:

- **Flat organization**: No project slug nesting so agents can find relevant knowledge across all projects.
- **Wiki index** (`knowledge/index.md`): Topic-oriented catalog of all deliverables, organized by domain. The orchestrator reads this first to find relevant knowledge without scanning every file.
- **Changelog** (`knowledge/changelog.md`): Append-only log of every knowledge mutation (`created`, `updated`, `superseded`, `archived`). Lets the orchestrator see what changed since the last project.
- **Deliverable headers**: Every file starts with YAML frontmatter (`role`, `project`, `run_id`, `confidence`, `inputs_used`, `evidence_mode`, `related`). The `related` field creates cross-reference trails between deliverables.
- **Mandatory TL;DR**: Every deliverable includes a `## TL;DR` section (1-3 sentences) immediately after the header, enabling fast scanning without reading full files.
- **Entity pages** (`knowledge/entities/`): Cross-cutting concepts (competitors, personas, patterns, decisions) get dedicated pages that aggregate findings from multiple deliverables.
- **Lossless history**: When updating a deliverable, agents write to `knowledge/runs/<run-id>/` first, then may update the canonical file. Previous versions are never overwritten. Every mutation appends to `changelog.md`.
- **Progressive scan order**: (1) `index.md` for domain categories, (2) `changelog.md` tail for recent changes, (3) TL;DR sections of relevant files, (4) full files only when directly needed, (5) `related` links for context.
- **Knowledge continuity**: Before every assignment, the orchestrator follows the progressive scan order and includes relevant files in `reads_from`. Decisions compound across projects.
- **Lint** (`lint-knowledge` skill): Periodic health check detecting stale files, contradictions, orphans, missing cross-references, knowledge gaps, and entity drift. Results go to `knowledge/orchestrator-lint.md`.
- **Mandatory reflection**: Every deliverable ends with a `## Reflection` section (What worked, What didn't, Next steps).

## Design System Workflow

For greenfield product design:

1. `ui-designer` explores concept directions and chooses a direction.
2. `ui-designer` seeds `project-ds-spec.md` from up to 3 inspiration-only references in the bundled reference design-system library (40+ company design systems including Airbnb, Stripe, Notion, Figma, and others).
3. If the frontend is blank and the spec justifies it, the shared spec can recommend a shadcn/ui baseline.
4. `design-systems-designer` operationalizes the shared spec into tokens, primitives, component families, layout/widget rules, governance, and QA guidance.
5. Later screen and component work inherits from `project-ds-spec.md`, not directly from company references.
6. Engineering may materialize the shadcn recommendation only when it explicitly owns repo writes.

The template for `project-ds-spec.md` is at `references/project-ds-spec-template.md`.

## Installed Layout

The installer keeps Product Team namespaced and idempotent:

```
target-repo/
  AGENTS.md | CLAUDE.md | ANTIGRAVITY.md   # Managed block (platform-dependent)
  logs/
    README.md                               # Execution trail contract
    TIMELINE.md                             # Chronological project index
    active/                                 # Active project records
    archive/                                # Completed projects
  knowledge/                                # (Codex only)
    README.md                               # Knowledge contract
    assets/                                 # Visual artifacts
    reviews/                                # Review deliverables
    runs/                                   # Lossless history
  app/                                      # (Codex only) Code outputs
  .codex/
    product-team/
      README.md                             # Package docs
      manifest.json                         # Install metadata
      references/
        role-catalog.md                     # Canonical staffing reference
        project-ds-spec-template.md         # Design system spec template
        reference-design-systems/           # 40+ company design systems
      scripts/
        validate-install.py                 # Installation validator
        update-install.py                   # Incremental updater
        lib/                                # Shared Python utilities
      auto-improve/                         # Self-improvement system
    agents/
      product-team-business/<role>/         # Business role definitions
      product-team-design/<role>/           # Design role definitions
      product-team-engineer/<role>/         # Engineering role definitions
      product-team-review/<role>/           # Review role definitions
```

Claude and Antigravity installs skip `knowledge/` and `app/` directories.

## Logs And Memory

`logs/README.md` is the contract for persistent project memory.

Each project lives at `logs/active/<project-slug>/` (format: `YYYYMMDD-kebab-case-objective`):

- **`context.md`** — YAML header (`slug`, `objective`, `confidence_score`, `status`, `current_run_id`) plus goal, constraints, done-when criteria, staffed roles, skill_paths, status, and key decisions.
- **`runs/<run-id>-<YYYYMMDD-HHMM>/`** — One directory per execution stage:
  - `prompt.md` — The exact assignment given to the agent.
  - `trace.md` — Agent reasoning, tool usage, key decisions, deliverable paths.
  - `feedback.md` — User feedback or review notes.
- **`TIMELINE.md`** — Chronological index of all projects with date, slug, objective, roles, and status.

Completed projects move from `active/` to `archive/`. See `logs/archive/sample-20260101-onboarding-flow/` for a worked example.

## Fragment Template System

The managed block injected into target repositories is generated from a shared template:

- **Template**: `assets/product-team.fragment.template.md` (uses `{{PLATFORM}}` placeholder)
- **Generator**: `scripts/generate-fragments.sh`
- **Outputs**: `assets/AGENTS.fragment.md`, `assets/CLAUDE.fragment.md`, `assets/ANTIGRAVITY.fragment.md`

Edit the template, then run `scripts/generate-fragments.sh` to regenerate all three fragments.

## Validation

Source-structure validation:

```bash
scripts/validate-orchestrator-contract.sh
```

This runs all checks:

- TOML structure validation for every role
- Role catalog freshness (`scripts/render_role_catalog.py --check`)
- Skill catalog freshness (`scripts/render_skill_catalogs.py --check`)
- Role prompt freshness (`scripts/render_role_prompts.py --check`)
- Agent roster freshness (`scripts/render_agents_md.py --check`)
- Orchestrator scenario validation (`scripts/check-orchestrator-scenarios.py`)

Skill validation:

```bash
python3 scripts/check_skill_validation_scenarios.py
```

Installed project validation:

```bash
python3 .codex/product-team/scripts/validate-install.py
```

## Auto-Improve System

Located at `assets/auto-improve/`, this is a hill-climbing loop for continuous skill refinement:

1. **Benchmark** (`benchmark.py`) — Prepares a scenario with a skill under test and captures the expected artifact.
2. **Judge** (`judge.py`) — Scores the produced artifact using structural rubrics (deterministic) or LLM-as-judge (for nuanced evaluation).
3. **Meta-Optimizer** (`meta_optimizer.py`) — Analyzes failures and generates optimization prompts. With `--apply`, modifies the skill file directly.
4. **Cron Trigger** (`scripts/cron-trigger.sh`) — Orchestrates the full cycle. Auto-commits improvements when scores increase.

Available scenarios (under `assets/auto-improve/scenarios/`):

- `modern-saas-dashboard` — Design: visual concept for a SaaS dashboard
- `engineering-frontend-component` — Engineering: React component implementation
- `business-product-prd` — Business: product requirements document
- `ux-research-plan` — Research: user research plan
- `content-microcopy-flow` — Content: checkout flow microcopy
- `design-system-audit` — Design systems: system audit
- `go-to-market-launch` — Go-to-market: launch plan
- `backend-api-implementation` — Backend: REST API design
- `platform-schema-migration` — Platform: schema migration plan
- `design-usability-review` — Review: usability evaluation
- `qa-release-gate` — QA: release readiness assessment

A CI template for GitHub Actions is at `assets/auto-improve/templates/self-improvement-ci.yml`.

## Skill Authoring

`skill-authoring-guide.md` defines the production standard for creating skills. Core principles:

- **Method over prompt** — Skills encode real expert workflows, not generic instructions.
- **Evidence over opinion** — Outputs grounded in observable input or explicitly stated assumptions.
- **Structure over prose** — Outputs are structured, scannable, and reusable.
- **Reproducibility** — Another agent should follow the same process and reach similar conclusions.

Every skill includes: frontmatter (execution contract), purpose, required inputs, evidence path, tool stack, model building step, core method execution, structured findings, prioritization logic, pattern detection, recommendations, coverage map, limits, and lossless run logging.

## Maintaining This Package

Source of truth:

- `agents/`: role definitions and role-local skills
- `logs/README.md`: runtime `/logs` contract
- `knowledge/README.md`: knowledge contract
- `install.sh` and `scripts/install.py`: installer entrypoints
- `assets/product-team.fragment.template.md`: managed block template
- `assets/package-README.md`: README copied into installed projects
- `references/specialist-baseline.md`: shared prompt template for all specialists
- `references/role-catalog.md`: canonical staffing reference
- `skill-authoring-guide.md`: production skill standards

After changing role structure, prompts, or routing:

```bash
# Regenerate managed files
python3 scripts/render_role_catalog.py --write
python3 scripts/render_skill_catalogs.py --write
python3 scripts/render_role_prompts.py --write
python3 scripts/render_agents_md.py --write
scripts/generate-fragments.sh

# Validate
scripts/validate-orchestrator-contract.sh
python3 scripts/check-orchestrator-scenarios.py
```

Then test a real install:

```bash
python3 scripts/install.py --target /tmp/test-install
python3 /tmp/test-install/.codex/product-team/scripts/validate-install.py
```

## Short Version

Product Team installs a coordinated workflow into another repository. It keeps simple work simple, adds coordination only when it helps, routes through real business/design/engineering roles, uses skill-first MCP workflows with fallback, preserves lossless knowledge across projects, and leaves a written operating record in `/logs`.
