# Product Team Package

This repository has the Product Team Codex workflow installed.

Requests in this repository should go through `product-team-orchestrator` by default. Only an explicit user opt-out for the current request should bypass Product Team. Simple work can still stay direct, but that choice is made inside the orchestrator.

The workflow is direct-first: the orchestrator routes work cheaply, executes directly when the task is single-domain and implementation-heavy, and only escalates into multi-agent coordination when the payoff is worth the cost. Orchestration, routing, staffing, and planning happen in the context window — only project context and deliverables are persisted to `/logs`.

Route by domain before staffing. Consult only the relevant discipline slice of `.codex/product-team/references/role-catalog.md` when the task is clearly single-domain; read the full catalog only for ambiguous or cross-functional work.

The workflow is organized around a small set of archetypes. Each archetype routes internally across its own discipline groups, so `designer` can cover research → UX → UI → content in one staffed role and `engineer` can cover frontend → backend → fullstack work without extra same-domain handoffs.

## Installed Layout

- `.codex/agents/product-team-<discipline>/<role>/<role>.toml`
- `.codex/agents/product-team-<discipline>/<role>/skill-catalog.md`
- `.codex/agents/product-team-<discipline>/<role>/skills/<discipline-group>/*.md`
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

The updater reuses the recorded install source. If the original source checkout is still available, it updates from that checkout. Otherwise, it falls back to the recorded remote archive.

## Usage Examples

### Simple request (direct execution)

> "Fix the typo on the login page"

The orchestrator sees this is simple, routes to direct execution, creates `context.md`, fixes the typo, and updates the context.

### Single-domain build (still direct)

> "Build a markdown editor"

The orchestrator sees this is substantial but narrow and implementation-first. It routes to direct execution and starts building without staffing specialists.

### Cross-functional request (2-role orchestration)

> "Add dark mode support to the dashboard"

The orchestrator identifies this needs a **designer** and an **engineer**. It staffs only those archetypes, presents the plan in conversation, asks "Do you want to proceed?", and coordinates execution after approval.

### Complex request (full team)

> "Redesign the checkout flow to reduce drop-off by 20%"

The orchestrator staffs a full team: **product-lead**, **designer**, **engineer**, and **reviewer**. It presents the plan, gets approval, and coordinates work stage by stage. Context and deliverables are logged in `logs/active/`.

## Notes

- `AGENTS.md` contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` is created only when the target repo does not already have one.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- Shared workflow references live under `.codex/product-team/references/`.
- `.codex/product-team/manifest.json` records enough source metadata for installed repos to self-update later.
