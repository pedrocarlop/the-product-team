# Role Catalog

This is the canonical archetype catalog for orchestrator staffing decisions when orchestration is actually warranted.

- Route by domain first.
- If the task is clearly single-domain, consult only the relevant discipline slice before staffing.
- Read the full catalog only when the work is ambiguous, cross-functional, or the right team is genuinely unclear.
- `orchestrator` and `reference` are intentionally excluded because they are workflow support roles, not staffed archetypes.
- Each archetype organizes skills into discipline groups and routes internally, so one staffed role can cover multiple specialties without handoff.
- Generated from the managed archetype TOMLs under `agents/`. Refresh with `python3 scripts/render_role_catalog.py --write`.

## Business Roles

- `product-lead` (Product Lead, executor) — Why: Own product vision, strategy, discovery, prioritization, requirements authoring, and delivery coordination. Owns: product vision and strategy, product discovery and prioritization, and requirements authoring and PRD. Repo writes: never in staffed workflows.
- `analyst` (Analyst, executor) — Why: Transform data into decisions through metrics analysis, financial modeling, forecasting, and revenue operations. Owns: data analysis and metrics, financial modeling and forecasting, and revenue operations and pipeline. Repo writes: never in staffed workflows.
- `go-to-market` (Go-to-Market, executor) — Why: Drive growth, marketing, positioning, partnerships, customer success, sales engineering, and go-to-market execution. Owns: growth and acquisition funnel, marketing and demand generation, and positioning and GTM strategy. Repo writes: never in staffed workflows.
- `business-ops` (Business Ops, executor) — Why: Own business analysis, process mapping, operational systems design, and coordination mechanisms. Owns: business analysis and requirements elicitation, process mapping and gap analysis, and operational systems design. Repo writes: never in staffed workflows.

## Design Roles

- `designer` (Designer, executor) — Why: Own all design execution from research through visual delivery — UX flows, UI surfaces, content, motion, accessibility, information architecture, localization, and service design. Owns: UX flows and interaction models, UI surfaces and visual design, and content and microcopy. Repo writes: never in staffed workflows.
- `design-systems` (Design Systems, executor) — Why: Build and govern the design system — token architecture, component library, prototyping, design tooling, and quality standards. Owns: token architecture, component library specs, and design-system governance. Repo writes: never in staffed workflows.

## Engineering Roles

- `engineer` (Engineer, executor) — Why: Own all implementation from UI components through backend services, mobile apps, and ML systems. Owns: frontend component architecture, backend services and business logic, and fullstack feature implementation. Repo writes: only when explicitly assigned implementation ownership for a bounded repo scope.
- `platform-engineer` (Platform Engineer, executor) — Why: Own API design, database, data pipelines, DevOps, performance, security, architecture, and engineering leadership. Owns: API contract design, database systems, and data pipelines and warehousing. Repo writes: only when explicitly assigned implementation ownership for a bounded repo scope.

## Review Roles

- `reviewer` (Reviewer, reviewer) — Why: Validate work across all disciplines — requirements, UX flows, usability, copy, design system, engineering, and quality assurance. Owns: requirements review, UX flow validation, and usability review. Repo writes: never in staffed workflows.

## Common Team Patterns

These patterns help the orchestrator staff teams for frequent task types. They are starting points, not rigid requirements — always assess actual role needs. Each archetype routes internally to the right discipline group, so a single `designer` handles research → UX → UI → content without separate handoffs.

- **UI Feature**: `designer` → `engineer` (+ `reviewer` for complex flows)
- **API Feature**: `engineer` + `platform-engineer` (+ `reviewer`)
- **Full Feature**: `product-lead` → `designer` → `engineer` (+ `reviewer`)
- **Design System Update**: `design-systems` (+ `reviewer`)
- **Data Pipeline**: `platform-engineer` (+ `reviewer`)
- **Growth Initiative**: `go-to-market` + `analyst` + `product-lead`
- **Infrastructure Change**: `platform-engineer` (+ `reviewer`)
- **Mobile Feature**: `designer` → `engineer` (+ `reviewer`)
- **Content Update**: `designer` (content/ + localization/ discipline groups)
- **Strategy**: `product-lead` + `analyst`

## Sequencing Rules

- Product-lead before design: designers need approved requirements as input.
- Design before engineering: engineers implement from approved design, not the reverse.
- Engineering before review: the reviewer is staffed after executors produce artifacts.
- Reviewers do not execute: the reviewer validates and recommends, it does not fix or reauthor.
- Repo-tracked app code has one explicit implementation owner per stage; parallel repo writers need disjoint scopes.
- Each archetype chains discipline groups internally — no handoff needed within a single role.

## Skill Routing

Each archetype organizes skills into discipline groups. The archetype routes internally to the right group:

- `designer`: research/ → ux/ → ui/ → content/ → motion/ → accessibility/ → architecture/ → localization/ → service/
- `design-systems`: system/ → technology/ → direction/ → operations/
- `product-lead`: strategy/ → product/ → portfolio/ → requirements/
- `analyst`: data/ → financial/ → revenue/
- `go-to-market`: growth/ → marketing/ → product-marketing/ → partnerships/ → customer-success/ → sales/
- `business-ops`: analysis/ → operations/
- `engineer`: frontend/ → backend/ → fullstack/ → mobile/ → ml/ → implementation/
- `platform-engineer`: api/ → database/ → data/ → devops/ → performance/ → security/ → architecture/ → leadership/
- `reviewer`: requirements/ → ux-flow/ → usability/ → copy/ → design-system/ → engineering/ → qa/

## Conflict Resolution

When archetypes produce conflicting advice or deliverables:

1. Both positions are documented in `decisions/<topic>.md` with rationale.
2. The orchestrator consults the archetype whose ownership area covers the disputed scope.
3. The orchestrator makes a binding decision and records the resolution in `decisions/`.
4. Overruled archetypes acknowledge the decision and align their work accordingly.
