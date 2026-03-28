# Product Team Package

This repository has the Product Team Codex workflow installed.

The workflow is direct-first: the orchestrator routes work cheaply, executes directly when the task is single-domain and implementation-heavy, and only escalates into multi-agent coordination when the coordination payoff is worth the cost. When orchestration is justified, the orchestrator staffs the minimum viable team, asks for specialist planning only when it is genuinely useful, authors one approved work plan, and then coordinates execution. Material replanning should happen through a new full cycle, not by repeated mid-flight rework.

Route by domain before staffing. Consult only the relevant discipline slice of `.codex/product-team/references/role-catalog.md` when the task is clearly single-domain; read the full catalog only for ambiguous or cross-functional work.

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

## Usage Examples

### Simple request (direct execution)

> "Fix the typo on the login page"

The orchestrator sees this is simple, self-contained work. It routes to direct execution — no specialists needed. It creates `00_routing.md` and `01_intake.md`, fixes the typo, and updates `status.md`.

### Single-domain build (still direct)

> "Build a markdown editor"

The orchestrator sees this is substantial but still narrow, implementation-first, and unlikely to benefit from cross-functional negotiation. It routes to direct execution, records the reasoning in `00_routing.md`, and starts building without staffing specialists or creating planning ceremony.

### Cross-functional request (2-role orchestration)

> "Add dark mode support to the dashboard"

The orchestrator identifies this needs a **product-designer** (to define the theme tokens and component states) and a **frontend-engineer** (to implement the toggle and theme switching). It staffs only those roles, asks for written specialist advice only if the design and implementation sequencing is unclear, authors a unified plan, asks for your approval, and then coordinates execution in sequence: design first, then engineering.

### Complex request (full team)

> "Redesign the checkout flow to reduce drop-off by 20%"

The orchestrator staffs a full team: **product-manager** (to define success metrics and scope), **product-designer** (to redesign the flow), **frontend-engineer** (to implement), and **qa-engineer** (to validate). It may request written advice from those roles if tradeoffs or sequencing are unclear, then authors one execution path, gets approval, and coordinates the work stage by stage. All artifacts, decisions, and reviews are logged in `logs/active/`.

## Notes

- `AGENTS.md` contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` is created only when the target repo does not already have one.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- Shared workflow references, including the role catalog and `/logs` contract, live under `.codex/product-team/references/`.
