# Product Team Package

This repository has the Product Team Codex workflow installed.

The workflow is direct-first: the orchestrator routes work cheaply, executes directly when the task is single-domain and implementation-heavy, and only escalates into multi-agent coordination when the coordination payoff is worth the cost. When orchestration is justified, the orchestrator staffs the minimum viable team, asks for specialist planning only when it is genuinely useful, requires execution-grade role plans when it does ask, reads the relevant staffed-role skills, authors one lossless merged implementation plan, and then coordinates execution. If execution is paused for approval, the orchestrator must summarize the plan, reference the active log files, and explicitly ask "Do you want to proceed?" Material replanning should happen through a new full cycle, not by repeated mid-flight rework.

Route by domain before staffing. Consult only the relevant discipline slice of `.codex/product-team/references/role-catalog.md` when the task is clearly single-domain; read the full catalog only for ambiguous or cross-functional work.

The workflow is organized around a small set of archetypes. Each archetype routes internally across its own discipline groups, so `designer` can cover research → UX → UI → content in one staffed role and `engineer` can cover frontend → backend → fullstack work without extra same-domain handoffs.
When an archetype is staffed, it first scans its own role-local `skill-catalog.md`, reads only the matching local skill files, and reports those reads in its closing handoff. If the orchestrator requests a role plan, that plan should be detailed enough that another strong practitioner in the same domain could execute it without guesswork, should name the role-local skills consulted, and should expose the best-practice implications pulled from those skills. Before writing `03_unified-plan.md`, the orchestrator should read the matching staffed-role skills too, then combine all non-conflicting role-plan detail, deduplicate true overlap, and resolve conflicts explicitly instead of flattening the plan.

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

The updater reuses the recorded install source. If the original source checkout is still available, it updates from that checkout. Otherwise it falls back to the recorded remote archive.

## Usage Examples

### Simple request (direct execution)

> "Fix the typo on the login page"

The orchestrator sees this is simple, self-contained work. It routes to direct execution — no specialists needed. It creates `00_routing.md` and `01_intake.md`, fixes the typo, and updates `status.md`.

### Single-domain build (still direct)

> "Build a markdown editor"

The orchestrator sees this is substantial but still narrow, implementation-first, and unlikely to benefit from cross-functional negotiation. It routes to direct execution, records the reasoning in `00_routing.md`, and starts building without staffing specialists or creating planning ceremony.

### Cross-functional request (2-role orchestration)

> "Add dark mode support to the dashboard"

The orchestrator identifies this needs a **designer** (to define theme tokens, states, copy, and motion behavior) and an **engineer** (to implement the toggle and theme switching). It staffs only those archetypes, asks for written specialist advice only if the design and implementation sequencing is unclear, reads the relevant design and engineering skills, preserves the must-carry details in a unified plan, points you to `03_unified-plan.md`, `04_approval.md`, `status.md`, and `context.md`, asks "Do you want to proceed?", and then coordinates execution in sequence after approval: design first, then engineering.

### Complex request (full team)

> "Redesign the checkout flow to reduce drop-off by 20%"

The orchestrator staffs a full team: **product-lead** (to define scope and success metrics), **designer** (to redesign the flow), **engineer** (to implement), and **reviewer** (to validate). It may request written advice from those archetypes if tradeoffs or sequencing are unclear, then authors one execution path that preserves the must-carry details from each role plan, adds best practices drawn from the relevant role-local skills, resolves overlap explicitly, gets approval, and coordinates the work stage by stage. All artifacts, decisions, and reviews are logged in `logs/active/`.

## Notes

- `AGENTS.md` contains a managed Product Team block that the installer keeps up to date.
- `logs/README.md` is created only when the target repo does not already have one.
- Installed roles stay grouped by discipline so the target repo mirrors the source package structure.
- Shared workflow references, including the role catalog and `/logs` contract, live under `.codex/product-team/references/`.
- `.codex/product-team/manifest.json` records enough source metadata for installed repos to self-update later.
