# Platform Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
It lists only the role-local skills in this folder and keeps descriptions short so you can scan cheaply.
Open only the matching skill files under `skills/`, then end your closing handoff with `Read <skill-paths> skills for this task.`

## api/

- `api/document` — Document API contracts clearly in OpenAPI, examples, and supporting artifacts so consumers can understand and use the interface without extra explanation.
- `api/shape` — Shape API contracts so resources, endpoints, methods, and schemas are consistent, consumer-friendly, and ready for implementation.
- `api/validate` — Validate API contracts for HTTP semantics, error handling, pagination, auth, and consumer safety before they are treated as final.
- `api/version` — Define API versioning, compatibility, and deprecation strategy so contract changes are deliberate and consumer impact is controlled.

## database/

- `database/index` — Choose and validate database indexes that improve the right queries without introducing unnecessary write overhead or maintenance risk.
- `database/migrate` — Plan and author database migrations so schema changes deploy safely, backfill cleanly, and remain reversible where possible.
- `database/recover` — Restore database service after failures by diagnosing impact, choosing a safe recovery path, and validating the system is healthy again.
- `database/schema` — Design and review database schemas so tables, columns, constraints, and relationships stay correct, queryable, and evolvable.

## data/

- `data/govern` — Define and enforce data governance for privacy, access, retention, lineage, quality controls, and auditability.
- `data/ingest` — Design and operate reliable data ingestion from source systems into raw or landing zones with clear contracts, observability, and backfill safety.
- `data/model` — Design warehouse and transformation models that produce correct, documented, testable, and analysis-ready datasets.
- `data/orchestrate` — Design and operate data workflow coordination, dependency management, retries, backfills, and alerting for reliable pipeline execution.

## devops/

- `devops/observe` — Verify infrastructure and service health using logs, metrics, traces, alerts, and deployment checks after a change ships to production.
- `devops/pipeline` — Design and maintain CI/CD pipelines that build, test, scan, and promote infrastructure or delivery changes safely.
- `devops/release` — Plan and execute safe releases, rollouts, and rollback paths for infrastructure and platform changes.
- `devops/stabilize` — Reduce operational risk during incidents or fragile changes by hardening failure modes, recovery paths, and support readiness.

## performance/

- `performance/budget` — Define and encode performance budgets that prevent regressions from shipping.
- `performance/isolate` — Narrow a performance issue to the browser, network, backend, or dependency causing it.
- `performance/profile` — Measure real-user and lab performance to identify the bottleneck before optimizing.
- `performance/verify` — Prove a performance change improved the target metric and did not regress other constraints.

## security/

- `security/remediate` — Turn security findings into targeted fixes, tests, and follow-up work without widening scope unnecessarily.
- `security/review` — Inspect implemented code, configuration, and architecture for security weaknesses before merge or release.
- `security/threat-model` — Map attack surface, trust boundaries, and realistic threats before implementation so security decisions are explicit instead of implicit.
- `security/verify` — Prove that a security fix actually blocks the issue and does not introduce a new regression.

## architecture/

- `architecture/choose` — Compare architecture options, vendors, and patterns, then select the best fit using explicit tradeoffs, risks, and decision criteria.
- `architecture/decompose` — Break ambiguous business problems into architectural requirements, bounded decisions, dependencies, constraints, and risks.
- `architecture/govern` — Set architecture standards, review paths, exception handling, and decision records that keep solutions safe, consistent, and supportable.
- `architecture/integrate` — Design how systems connect through APIs, events, data contracts, sequencing, migration paths, and failure handling.

## leadership/

- `leadership/mentor` — Coach engineers through technical decisions, reviews, and pairing so the team gets stronger over time.
- `leadership/review` — Review code and designs for correctness, architecture fit, tests, risk, and mentoring value.
- `leadership/sequence` — Break technical work into the right order, surface dependencies, and plan the safest path to delivery.
- `leadership/steer` — Set technical direction, frame tradeoffs, and align teams on the simplest architecture that solves the actual problem.
- `leadership/calibrate` — Align expectations for performance, growth, promotion, and team health so people decisions are consistent and evidence-based.
- `leadership/plan` — Turn an engineering objective into an execution plan with sequencing, owners, milestones, and measurable success criteria.
- `leadership/staff` — Shape team staffing, role scope, and headcount choices so engineering capacity matches the work that matters most.
- `leadership/unblock` — Remove delivery blockers by clarifying ownership, negotiating tradeoffs, and escalating only when the team cannot solve the issue locally.
