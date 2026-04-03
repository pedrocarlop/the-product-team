# Role Catalog

This is the canonical staffed-role catalog for Product Team orchestration decisions.

- Route by real job function, not by abstract discipline labels alone.
- Staff the right-sized team — include every role whose absence would degrade the outcome, not just the smallest possible set. Assign exact `skill_paths` instead of vague domain ownership.
- `reference` remains a helper role for grounding, tracing, reuse, and verification; it is not a staffed specialist.
- Every staffed role is skill-first and MCP-first: primary MCP -> alternative tool/MCP -> best guess inferred output.

## Business Roles

- `product-lead` (Product Lead, executor) — Why: Own problem framing, product specification, prioritization, and decision communication for cross-functional delivery. Owns: problem framing, product specification, prioritization. Repo writes: never in staffed workflows.
- `analyst` (Analyst, executor) — Why: Own metric definition, funnel diagnosis, forecasting, experiment readouts, and data storytelling for product decisions. Owns: metric frameworks, funnel diagnosis, forecasting. Repo writes: never in staffed workflows.
- `go-to-market` (Go-To-Market, executor) — Why: Own positioning, launch planning, campaign briefs, sales enablement, partner strategy, and customer-signal synthesis. Owns: positioning, launch execution, campaign planning. Repo writes: never in staffed workflows.
- `business-ops` (Business Ops, executor) — Why: Own process mapping, operating cadence, tooling design, and execution tracking for cross-functional operations. Owns: process design, operating cadence, tooling workflows. Repo writes: never in staffed workflows.

## Design Roles

- `ux-researcher` (UX Researcher, executor) — Why: Own research planning, participant screeners, interview guides, competitor benchmarking, synthesis, and insight readouts. Owns: research planning, participant recruiting artifacts, interview and workshop synthesis. Repo writes: never in staffed workflows.
- `product-designer` (Product Designer, executor) — Why: Own problem framing, journeys, flows, wireframes, interaction specifications, and validation-ready handoffs for product experiences. Owns: problem framing for design, journey and flow design, wireframes. Repo writes: never in staffed workflows.
- `ui-designer` (UI Designer, executor) — Why: Own visual concept direction, screen production design, responsive/state specs, component design, and final visual polish. Owns: visual concept direction, screen design, responsive and state specifications. Repo writes: never in staffed workflows.
- `content-designer` (Content Designer, executor) — Why: Own microcopy systems, state messaging, naming, guidance, localization preparation, and product content reviews. Owns: microcopy design, state messaging, naming systems. Repo writes: never in staffed workflows.
- `design-systems-designer` (Design Systems Designer, executor) — Why: Own system audits, token architecture, spacing scales, atomic libraries, component governance, design-code mapping, and system QA. Owns: design system audits, token architecture, spacing systems. Repo writes: never in staffed workflows.

## Engineering Roles

- `frontend-engineer` (Frontend Engineer, executor) — Why: Own implementation from design, stateful UI behavior, responsive refinement, component implementation, browser debugging, and frontend verification. Owns: UI implementation, component behavior, responsive behavior. Repo writes: only when explicitly assigned implementation ownership for a bounded repo scope.
- `backend-engineer` (Backend Engineer, executor) — Why: Own API implementation, domain models, integration flows, backend observability, and backend verification. Owns: API implementation, domain logic, integration flows. Repo writes: only when explicitly assigned implementation ownership for a bounded repo scope.
- `platform-engineer` (Platform Engineer, executor) — Why: Own schema migrations, pipeline orchestration, infrastructure releases, performance investigation, security hardening, and CI/CD governance. Owns: schema and migration design, platform pipelines, infrastructure changes. Repo writes: only when explicitly assigned implementation ownership for a bounded repo scope.

## Review Roles

- `design-reviewer` (Design Reviewer, reviewer) — Why: Validate visual fidelity, usability, accessibility, copy quality, and design-system compliance before release. Owns: design fidelity validation, usability review, accessibility review. Repo writes: never in staffed workflows.
- `qa-reviewer` (QA Reviewer, reviewer) — Why: Validate requirements traceability, test plans, runtime behavior, regressions, and release readiness. Owns: requirements traceability review, test plan review, runtime and network audit. Repo writes: never in staffed workflows.

## Common Team Patterns

- **Research-heavy discovery**: `ux-researcher` -> `product-designer` -> `product-lead`
- **Greenfield visual concept**: `product-designer` -> `ui-designer` -> `frontend-engineer` -> `design-reviewer`
- **Feature delivery**: `product-lead` -> `product-designer` or `ui-designer` -> `frontend-engineer` or `backend-engineer` -> `qa-reviewer`
- **Design system work**: `design-systems-designer` -> `frontend-engineer` -> `design-reviewer`
- **Platform change**: `platform-engineer` -> `qa-reviewer`
- **Go-to-market launch**: `product-lead` + `go-to-market` + `analyst`
- **Content-heavy feature**: `content-designer` -> `product-designer` or `ui-designer` -> `frontend-engineer` -> `design-reviewer`
- **Data-driven decision**: `analyst` -> `product-lead` -> relevant executor
- **Research-to-design**: `ux-researcher` -> `product-designer` -> `ui-designer` -> `design-reviewer`
- **Full product lifecycle**: `product-lead` -> `ux-researcher` -> `product-designer` -> `ui-designer` -> `content-designer` -> `frontend-engineer` -> `design-reviewer` -> `qa-reviewer`
- **Operations improvement**: `business-ops` -> `analyst` -> `product-lead`
- **Design system evolution**: `design-systems-designer` -> `ui-designer` -> `frontend-engineer` -> `design-reviewer`
- **Launch preparation**: `product-lead` -> `go-to-market` -> `content-designer` -> `analyst`

## Sequencing Rules

- Product framing before downstream execution when requirements are still ambiguous.
- Research before product/UI design when the user problem is not yet well grounded.
- Product/UI/content design before frontend implementation when user-facing behavior is still open.
- Backend and platform work may run in parallel only with disjoint ownership and explicit contracts.
- Design review and QA review happen after executor outputs exist; reviewers do not fix the work themselves.
- Only one explicit repo implementation owner exists per stage by default.

## Signal-Based Role Triggers

Before defaulting to a common team pattern, scan the request for these signals. If a signal is present, the associated role SHOULD be included unless there is an explicit reason to exclude it.

| Signal in request | Consider role | Why |
|---|---|---|
| Metrics, KPIs, data, funnel, conversion, A/B test, experiment | `analyst` | Metric definition, funnel diagnosis, experiment design |
| Process, operations, workflow, tooling, cadence, tracking | `business-ops` | Process mapping, operating cadence, tooling audits |
| Launch, positioning, campaign, sales enablement, GTM, market | `go-to-market` | Positioning, launch planning, campaign briefs |
| Copy, microcopy, naming, taxonomy, error messages, empty states, tone | `content-designer` | Microcopy systems, state messaging, naming |
| Design system, tokens, spacing scale, component library, governance | `design-systems-designer` | System audits, token architecture, component governance |
| Research, interviews, usability testing, user feedback, personas | `ux-researcher` | Research planning, synthesis, competitor benchmarking |
| Journey, flow, wireframe, interaction, prototype | `product-designer` | Journey/flow design, wireframes, interaction specs |
| Visual direction, concept, screen design, responsive spec, polish | `ui-designer` | Visual concepts, screen production, responsive specs |
| API, backend, domain model, integration, webhook | `backend-engineer` | API implementation, domain models, integrations |
| Schema, migration, pipeline, infrastructure, CI/CD, security | `platform-engineer` | Migrations, pipelines, infra releases |
| Accessibility, usability review, design fidelity, handoff quality | `design-reviewer` | Fidelity review, accessibility, compliance |
| Test plan, regression, release gate, runtime audit | `qa-reviewer` | Test plans, regression triage, release readiness |
| PRD, requirements, prioritization, roadmap, stakeholder | `product-lead` | Problem framing, specs, prioritization |
| Frontend, UI implementation, components, responsive, browser | `frontend-engineer` | UI implementation, components, responsive behavior |

## Skill Routing

- Roles are selected first by job function, then by exact `skill_paths`.
- Do not assign a role without also assigning the core action it must execute.
- Use `ui-designer` for Paper-first concept work (with stitch for reference browsing only) and for seeding `project-ds-spec.md` from company references, `design-systems-designer` for operationalizing that spec into token/library governance, `ux-researcher` for research operations and synthesis, and `qa-reviewer` for release readiness.
