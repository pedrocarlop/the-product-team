---
name: schema-migration
description: Plan and execute schema changes through engine-native DDL, versioned migration tooling, and rollback-aware rollout sequencing before touching persistent data.
trigger: When persistent data models must change safely.
analysis_framework: schema-change modeling with compatibility-window, rollback, and lock-risk analysis
primary_mcp: repository, logs
fallback_tools:
  - reference/trace
  - search_query
required_inputs:
  - the exact schema change request and owning system
  - current schema, migration history, and deployment path
  - target database engine and version when known
  - data volume, lock sensitivity, and rollback constraints
  - whether the change is backward compatible or requires a staged rollout
recommended_passes:
  - schema model and ownership inventory
  - migration shape and lock-risk review
  - compatibility window planning
  - rollback and recovery planning
  - verification and follow-up
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: []
  migration:
    primary: [engine-native-ddl, atlas]
    secondary: [flyway, liquibase, golang-migrate, alembic, prisma-migrate]
  online-schema-change:
    mysql: [gh-ost, pt-online-schema-change, skeema, bytebase]
    postgres: [pgroll, reshape]
  lightweight:
    primary: [dbmate, golang-migrate, schemachange]
  fallback:
    primary: [reference/trace, search_query]
tool_routing:
  - if: the live schema, migrations, or deployment scripts are in the repository
    use: [repository]
  - if: recent deploys, lock waits, failures, or rollback signals matter
    use: [logs]
  - if: the change can be expressed safely with engine-native DDL
    use: [engine-native-ddl]
  - if: the repo uses declarative schema diffing, linting, or pre-approval
    use: [atlas]
  - if: the repo uses versioned migration files and audit history matters
    use: [flyway, liquibase]
  - if: the stack is Go-based and migration simplicity matters
    use: [golang-migrate]
  - if: the stack is Python/SQLAlchemy
    use: [alembic]
  - if: the stack is Node.js/TypeScript using Prisma ORM
    use: [prisma-migrate]
  - if: MySQL table is large and cannot tolerate write locks during DDL
    use: [gh-ost, pt-online-schema-change]
  - if: MySQL schema is managed declaratively and OSC integration is needed
    use: [skeema]
  - if: Postgres table is large and zero-downtime multi-version coexistence is required
    use: [pgroll]
  - if: migration tooling needs to be language-agnostic and lightweight
    use: [dbmate]
  - if: the data warehouse is Snowflake
    use: [schemachange]
  - if: a database DevOps review workflow, approval gates, or audit trail is needed across engines
    use: [bytebase]
  - if: the primary path is unavailable or the schema is only described in docs
    use: [reference/trace, search_query]
best_guess_output: A schema migration plan or implementation with compatibility and rollback considerations.
output_artifacts: knowledge/platform-engineer-schema-migration.md
done_when: The schema change is bounded, compatible where needed, and safe to deploy or revert with explicit verification.
---

# Schema Migration

## Purpose

Plan and execute schema changes with operational safety. This skill builds the migration model first, then chooses the narrowest safe execution path: engine-native DDL for straightforward edits, declarative diff/planning when drift control matters, versioned migrations when auditability or multi-step rollout is the priority, and online schema change tools when table size or write sensitivity rules out any locking DDL.

This skill covers schema shape, constraints, indexes, backfills, compatibility windows, rollback posture, and verification. It does not own product data modeling, application feature design, or unrelated infra change.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/platform-engineer-schema-migration.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Inputs and Assumptions

Required inputs:
- the exact schema change request and the tables, indexes, constraints, or views it touches
- the current schema source of truth, migration history, and deployment path
- the target database engine and version when known
- the expected data volume, lock sensitivity, and rollback constraints
- whether the change must remain backward compatible during rollout

Assumptions:
- If engine or version is missing, infer the nearest production engine from the repository and label the inference.
- If the change touches live data, assume compatibility and rollback must be proven before cutover.
- If multiple implementation paths exist, prefer the one with the smallest blast radius and fewest irreversible steps.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live or current repo evidence: schema files, migration files, tests, deployment scripts, and runtime logs.
2. Structured system access: schema review, migration tooling output, and deployment metadata when available.
3. Docs and artifacts: ADRs, runbooks, design notes, and prior migration plans.
4. Screenshots or static input: diagrams, copied SQL, or review material.
5. Inference: derive the likely shape from code patterns or adjacent migrations only as a last resort.

State which path was used and note its limits in the deliverable. Prefer paths 1 and 2 together when the schema affects durable data or live traffic.

## Environment and Reproducibility

Record the following when known:

- database engine and version
- environment reviewed: local, preview, staging, or production
- migration framework or workflow in use
- deployment window or release identifier
- data volume and table hotness
- lock tolerance, replica lag, and feature-flag assumptions
- backup, snapshot, or restore posture

If any item is unknown, state it explicitly. Do not present inferred lock or data-shape behavior as confirmed behavior.

## Model Building

Before evaluating implementation details, construct the schema model.

The model should answer:

1. What schema objects are in scope: tables, columns, indexes, constraints, sequences, triggers, views, or permissions?
2. What dependencies exist between objects and code paths?
3. Which parts of the change are additive, transitional, or destructive?
4. What data must be backfilled, rewritten, or normalized?
5. What compatibility window is required for old and new code to coexist?
6. What rollback path exists if the change fails or must be reverted?

No migration recommendation should be written before the model is built and named.

## Core Method Execution

Follow this sequence:

1. Confirm scope and source of truth.
- Identify the exact schema surface, the owning service or database, and the migration framework if one exists.
2. Inventory the schema model.
- List the affected objects, dependencies, data flows, and any hidden coupling in code or downstream consumers.
3. Classify the change.
- Separate additive, transitional, and destructive work so the rollout order stays explicit.
4. Review operational risk.
- Estimate lock behavior, write amplification, backfill cost, replication lag, and any irreversible step.
5. Choose the tool path.
- Prefer engine-native DDL for straightforward changes, declarative planning for drift-sensitive workflows, versioned migrations when history and repeatability matter, and online schema change tools when table size or lock sensitivity rules out locking DDL.
6. Sequence the rollout.
- Prefer expand, backfill, validate, cut over, then clean up when the schema change touches live data.
7. Define verification and rollback.
- State how success will be checked and what it would take to revert safely.
8. Surface unknowns.
- Mark any assumption or unverified dependency clearly and lower confidence on conclusions that depend on it.

## Required Deliverable Sections

Within `## Skill: schema-migration`, include:
- `### Migration framing`: Define the requested change, owning database, desired end state, and whether the change is additive, transitional, or destructive.
- `### Required inputs and assumptions`: State what was available, what was missing, and which assumptions were inferred.
- `### Input mode and evidence path`: State the strongest evidence path used and what it could not prove.
- `### Environment and reproducibility`: Record the engine, version, environment, migration workflow, data volume, and rollout assumptions.
- `### Schema model`: Inventory the schema objects, dependencies, and data movement involved. Build this before proposing actions.
- `### Migration plan`: Describe the step-by-step sequence, including preflight checks, backfill, validation, cutover, and cleanup if applicable.
- `### Compatibility window`: State how old and new schema shapes coexist and what code versions must remain compatible.
- `### Rollback and recovery`: Explain rollback triggers, the revert path, and when restore or backup is required instead of code rollback.
- `### Verification plan`: Describe how success will be checked, including lock impact, data checks, and post-deploy signals.
- `### Operational risks`: Capture lock contention, long validation scans, data rewrite cost, replication lag, and irreversible data loss risk.
- `### Tool selection rationale`: State why specific tools were chosen or skipped.
- `### Prioritization logic`: Explain how to order multiple schema changes by blast radius, irreversibility, and compatibility risk.
- `### Limits and unknowns`: State what could not be validated and what still needs runtime confirmation.
- `### Structured findings`: Document discrete findings using the finding schema below.
- `### Pattern detection`: Identify recurring anti-patterns across the migration history or current plan.
- `### Recommendations`: Link each recommendation to a finding. Keep recommendations directional, not overconfident.
- `### Coverage map`: State which areas were deeply analyzed, partially analyzed, or not analyzed.

## Structured Findings

Use this schema for each discrete finding. Populate as many fields as evidence supports; mark unknown fields explicitly.

#### Finding <id>
- Observation:
- Evidence:
- Repro steps or validation path:
- Cause:
- Impact:
- Confidence:

Findings should be numbered sequentially and referenced by ID in the Recommendations section. Do not collapse multiple distinct findings into one entry.

## Pattern Detection

Identify recurring migration anti-patterns in the codebase or plan under review. Common patterns to look for:

- Skipping compatibility windows: applying destructive removals before the old code version has been fully retired.
- Repeated lock events: multiple `ALTER TABLE` operations on the same hot table without online DDL tooling.
- Missing backfill validation: populating new columns without verifying completeness before cutover.
- Unbounded backfills: `UPDATE` statements without batching or throttling on large tables.
- Implicit schema drift: schema state diverging from migration files due to manual interventions.
- Missing rollback provisions: migrations with no revert path and no snapshot or backup trigger.
- Constraint additions without `NOT VALID`: adding foreign keys or check constraints that cause a full table scan under lock.
- Tight coupling of migration and deploy: schema changes and application code shipped in the same atomic deploy without a compatibility window.
- Snowflake-specific: applying destructive column changes without cloning or time-travel safeguards.

Note each pattern with a count if recurring, and reference the relevant Finding IDs.

## Recommendations

Each recommendation must:
- Reference the Finding ID it addresses.
- State the recommended action concisely.
- Describe the expected outcome.
- Note confidence and any prerequisite evidence still missing.

Recommendations should be directional, not prescriptive beyond what the evidence supports. Avoid recommending irreversible actions when the evidence path was inference only.

## Coverage Map

State coverage explicitly for each major area of the migration plan:

- **Deeply analyzed**: areas where live repo evidence and logs were both available and consistent.
- **Partially analyzed**: areas where only one evidence source was available, or where the source had gaps.
- **Not analyzed**: areas that were out of scope, inaccessible, or explicitly deferred.

The coverage map is required even when all areas are fully analyzed. It signals the limits of the deliverable to reviewers and operators.

## Limits and Unknowns

State explicitly what could not be validated during this skill execution:

- Missing engine or version information and what was inferred instead.
- Table sizes, row counts, or write rates that were not confirmed from live data.
- Lock behavior that was estimated rather than observed.
- Replica lag, backup posture, or feature-flag state that was assumed.
- Downstream consumers or foreign key relationships that were not traced.
- Whether the migration framework's history table reflects actual production state.

Lower confidence on any finding or recommendation that depends on an unresolved unknown. Do not present inferred behavior as confirmed.

## Tool Path

- Start with `repository`.
- If recent deploys, lock waits, failures, or rollback signals matter, add `logs`.
- If the change is a direct DDL edit and the engine supports a safe native path, prefer `engine-native-ddl` first.
- For PostgreSQL specifically, favor `CREATE INDEX CONCURRENTLY` for write-sensitive indexes and `NOT VALID` plus `VALIDATE CONSTRAINT` for large constraint additions when the lock profile matters.
- If the repo uses declarative schema diffing, linting, or pre-approval, use `atlas` for planning and drift checks.
- If the repo uses versioned migration files and audit history is the source of truth, use `flyway` or `liquibase` to stay aligned with that workflow.
- If the table is large and MySQL cannot tolerate write locks during DDL, use `gh-ost` (preferred, triggerless) or `pt-online-schema-change` (trigger-based, established).
- If the Postgres table is large and multi-version schema coexistence is needed during rollout, use `pgroll`.
- If the stack is Go-based and migration tooling should be lightweight and dependency-free, use `golang-migrate`.
- If the stack is Python with SQLAlchemy, use `alembic`.
- If the stack is Node.js with Prisma ORM, use `prisma-migrate`.
- If migrations must be language-agnostic with a minimal footprint, use `dbmate`.
- If the target system is Snowflake, use `schemachange`.
- If a database DevOps review workflow, DBA approval gates, or cross-engine audit trail is needed, use `bytebase`.
- If the primary path is unavailable or the schema is only described in docs, switch to `reference/trace, search_query`.
- If both paths fail, produce the best-guess output described as: A schema migration plan or implementation with compatibility and rollback considerations.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Tool Selection Rationale

Use this reference when selecting among tools. State the rationale explicitly in the deliverable.

**engine-native-ddl**
Use when the change is straightforward, the engine supports a safe non-locking path (e.g., `CREATE INDEX CONCURRENTLY`, instant `ADD COLUMN DEFAULT` in Postgres 11+), and no external framework is required. Lowest overhead; highest portability.

**atlas**
Use when the team wants declarative schema-as-code with Git-native planning, drift detection, and approval gates. Atlas computes the diff from a desired schema state, making it a strong fit for infrastructure-as-code workflows and teams familiar with Terraform-style operations. Best fit for multi-database or polyglot environments where a single CLI should own schema review.

**flyway**
Use when the repo already uses ordered versioned SQL migration files and an explicit schema history table is the audit source. Flyway's unified `flyway.toml` format (current default) simplifies configuration. Strong fit for Java ecosystems and teams that want minimal ceremony around sequential migrations.

**liquibase**
Use when changelog-driven execution with contexts, labels, and rollback policy control is the key requirement. Better fit than Flyway when teams need conditional migration logic, per-environment changelogs, or enterprise governance features. Supports XML, YAML, JSON, and SQL changelogs.

**gh-ost** (MySQL only)
Use when altering large MySQL tables that cannot tolerate write interruptions. gh-ost is triggerless: it uses MySQL binlog replication to capture changes and apply them to a ghost table, avoiding trigger overhead and the concurrency issues that affect pt-online-schema-change. Preferred over pt-osc for most production MySQL workloads. Does not support all DDL operations; verify before use.

**pt-online-schema-change** (MySQL only)
Use when gh-ost is unavailable or unsupported for the specific DDL operation. pt-osc is trigger-based and well-established, but triggers add write overhead and can cause issues under high concurrency. Appropriate when the team already operates Percona Toolkit and gh-ost has not been adopted.

**pgroll** (Postgres only)
Use when Postgres tables are large and the rollout requires multiple schema versions to coexist during deployment. pgroll creates virtual schemas using views so old and new application versions can read the same table simultaneously. Strong fit for expand-contract rollouts where blue-green or canary deployments must not force a coordinated cutover. Requires Postgres 14+.

**skeema** (MySQL/MariaDB only)
Use when MySQL schema is managed declaratively from SQL files and the team wants automated diff and deploy with optional gh-ost or pt-osc integration for large tables. Skeema enforces schema consistency as code without requiring a history table. Good fit for teams that prefer a Terraform-style workflow for MySQL specifically.

**bytebase**
Use when database changes require structured review workflows, DBA approval gates, or organization-wide audit trails across multiple engines and teams. Bytebase wraps gh-ost for MySQL online schema migrations and provides a GUI, policy engine, and CI integration. Best fit when schema governance, not just execution, is the gap.

**golang-migrate**
Use when the stack is primarily Go or when language-agnostic SQL migrations must run with minimal runtime dependencies. golang-migrate supports many database drivers and can run as a CLI or library. Well-suited for microservices where embedding a Java-based tool is undesirable.

**alembic**
Use when the stack is Python with SQLAlchemy. Alembic generates migration scripts from model diffs or manual authoring and integrates natively with the SQLAlchemy ORM. The standard choice for Python-centric teams; not appropriate outside the Python ecosystem.

**prisma-migrate**
Use when the stack is Node.js or TypeScript and the application uses Prisma ORM. Prisma Migrate generates and applies migrations from the Prisma schema file, keeping the ORM model and database schema in sync. Tightly coupled to the Prisma ecosystem; not suitable for teams that do not use Prisma.

**dbmate**
Use when migrations must be language-agnostic, the team wants plain SQL files, and a lightweight binary with no runtime framework is preferred. dbmate supports Postgres, MySQL, SQLite, and ClickHouse. Good fit for polyglot teams or projects where other tools introduce too much overhead.

**schemachange** (Snowflake only)
Use when the target system is Snowflake and versioned SQL-based schema migrations must integrate with a CI/CD pipeline. schemachange follows a Flyway-style versioned file convention applied to Snowflake's SQL dialect. Not applicable to transactional databases.

## Workflow Notes

- Treat compatibility and rollback as required design elements, not optional notes.
- Keep migration sequencing concrete enough that operators and reviewers can act safely.
- Prefer additive steps first, then backfill, then validation, then cutover, then cleanup.
- Make destructive steps explicit and isolate them from reversible steps.
- Preserve exact object names, constraint names, and migration identifiers where execution safety depends on them.
- Group low-risk changes only when they share the same lock profile and compatibility window.
- When the engine is PostgreSQL, remember that `CREATE INDEX CONCURRENTLY` avoids blocking writes but cannot run inside a transaction block, and that `ALTER TABLE` operations still need lock-aware planning.
- When the engine is MySQL and tables are large, default to gh-ost or pt-osc rather than native DDL unless INSTANT DDL is confirmed safe for the operation.
- Atlas is the better fit when the team wants declarative planning, previewed diffs, or approval gates around schema drift.
- Flyway is the better fit when ordered versioned migrations and an explicit schema history table are the key control surface.
- Liquibase is the better fit when changelog-driven execution needs contexts, labels, and rollback policy control.
- pgroll enables multi-version schema coexistence in Postgres, which is essential when coordinated cutover between app and database is not possible.
- gh-ost captures changes via binlog rather than triggers, which eliminates trigger overhead and makes it safer for high-write MySQL tables than pt-osc.
- Bytebase is appropriate when the organization needs DBA review gates, not just execution tooling.

## Prioritization Logic

Prioritize by blast radius and irreversibility:

1. Required compatibility steps that keep the app deployable.
2. Lock-reducing work that lowers operational risk before any destructive change.
3. Backfills and validation that prove the new shape is safe.
4. Cutover steps that switch read or write paths.
5. Cleanup and destructive removals after the compatibility window closes.

If several changes share the same risk profile, group them into one migration plan. If they do not share the same lock profile, keep them separate.

