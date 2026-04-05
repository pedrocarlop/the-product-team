# Product Team Package

This repository packages an installable Codex workflow called `Product Team`. It contains TOML-defined roles organized by discipline, each with role-local skills, and an orchestrator that routes work across the team.

## Agent Roster

<!-- AGENT_ROSTER:START -->

| Role | Display Name | Discipline | Kind | Skills | Repo Writes | Description |
| ---- | ------------ | ---------- | ---- | -----: | ----------- | ----------- |
| `orchestrator` | Orchestrator | Orchestrator | orchestrator | 9 | direct | Route work cheaply, assign exact skill workflows, enforce MCP-first execution with fallback, and coordinate staffed specialists only when needed |
| `product-lead` | Product Lead | Business Roles | executor | 6 | never | Own problem framing, product specification, prioritization, and decision communication for cross-functional delivery using AI-first discovery and framing methods |
| `analyst` | Analyst | Business Roles | executor | 5 | never | Own metric definition, funnel diagnosis, forecasting, experiment readouts, and data storytelling for product decisions |
| `go-to-market` | Go-To-Market | Business Roles | executor | 6 | never | Own positioning, launch planning, campaign briefs, sales enablement, partner strategy, and customer-signal synthesis |
| `business-ops` | Business Ops | Business Roles | executor | 5 | never | Own process mapping, operating cadence, tooling design, and execution tracking for cross-functional operations |
| `ux-researcher` | UX Researcher | Design Roles | executor | 8 | never | Own research planning, participant screeners, interview guides, competitor benchmarking, synthesis, and insight readouts |
| `product-designer` | Product Designer | Design Roles | executor | 6 | never | Own problem framing, journeys, flows, wireframes, interaction specifications, and validation-ready handoffs for product experiences |
| `ui-designer` | UI Designer | Design Roles | executor | 6 | never | Own visual concept direction, screen production design, responsive/state specs, component design, and final visual polish |
| `content-designer` | Content Designer | Design Roles | executor | 6 | never | Own microcopy systems, state messaging, naming, guidance, localization preparation, and product content reviews |
| `design-systems-designer` | Design Systems Designer | Design Roles | executor | 7 | never | Own system audits, token architecture, spacing scales, atomic libraries, component governance, design-code mapping, and system QA |
| `frontend-engineer` | Frontend Engineer | Engineering Roles | executor | 7 | scoped | Own implementation from design, stateful UI behavior, responsive refinement, component implementation, browser debugging, and frontend verification |
| `backend-engineer` | Backend Engineer | Engineering Roles | executor | 5 | scoped | Own API implementation, domain models, integration flows, backend observability, and backend verification |
| `platform-engineer` | Platform Engineer | Engineering Roles | executor | 6 | scoped | Own schema migrations, pipeline orchestration, infrastructure releases, performance investigation, security hardening, and CI/CD governance |
| `reference` | Reference | Engineering Roles | reference | 4 | never | Ground decisions in the real repo, trace implementation paths, reuse approved patterns, and verify claims before specialists commit to a direction |
| `design-reviewer` | Design Reviewer | Review Roles | reviewer | 5 | never | Validate visual fidelity, usability, accessibility, copy quality, and design-system compliance before release |
| `qa-reviewer` | QA Reviewer | Review Roles | reviewer | 5 | never | Validate requirements traceability, test plans, runtime behavior, regressions, and release readiness |

<!-- AGENT_ROSTER:END -->

## Common Team Patterns

- **Research-heavy discovery**: `ux-researcher` -> `product-designer` -> `product-lead`
- **Greenfield visual concept**: `product-designer` -> `ui-designer` -> `frontend-engineer` -> `design-reviewer`
- **Feature delivery**: `product-lead` -> `product-designer` or `ui-designer` -> `frontend-engineer` or `backend-engineer` -> `qa-reviewer`
- **Design system work**: `design-systems-designer` -> `frontend-engineer` -> `design-reviewer`
- **Platform change**: `platform-engineer` -> `qa-reviewer`
- **Go-to-market launch**: `product-lead` + `go-to-market` + `analyst`

### Sequencing Rules

- Product framing before downstream execution when requirements are still ambiguous.
- Research before product/UI design when the user problem is not yet well grounded.
- Product/UI/content design before frontend implementation when user-facing behavior is still open.
- Backend and platform work may run in parallel only with disjoint ownership and explicit contracts.
- Design review and QA review happen after executor outputs exist; reviewers do not fix the work themselves.
- Only one explicit repo implementation owner exists per stage by default.

## Source Of Truth

- The role definitions and role-local skills live under `agents/`.
- The runtime `/logs` contract lives in `logs/README.md`.
- The installer entrypoints are `install.sh` and `scripts/install.py`.
- The managed `AGENTS.md` block injected into target repositories lives at `assets/AGENTS.fragment.md`.
- The installed package readme lives at `assets/package-README.md`.

## Package Rules

- Keep the package project agnostic and Codex specific.
- Keep installed assets namespaced under `.codex/product-team/` and `.codex/agents/product-team-*`.
- Preserve the source discipline/role folder structure in installed role assets when materializing into `.codex/agents/`.
- Preserve the current source layout as the authoring surface; do not create a second hand-maintained template tree.
- Keep installer behavior idempotent. It may update workflow-owned namespaced files and the managed `AGENTS.md` block, but it must not overwrite unrelated target-project files.
- If you add, remove, or rename a role, update the installer transforms, managed docs, and install validator together.

## Validation

- Run `scripts/validate-orchestrator-contract.sh` after source-structure changes.
- Run `python3 scripts/check-orchestrator-scenarios.py` after prompt or routing changes.
- Run `python3 scripts/render_agents_md.py --check` to verify the agent roster is current.
- Run a real install into a temporary folder and then run `python3 .codex/product-team/scripts/validate-install.py`.
- Treat validation failures as blockers.
