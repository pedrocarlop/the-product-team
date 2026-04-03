# Platform Engineer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `ci-cd-governance`

- Description: Define or improve delivery controls by modeling the pipeline first, then turning policy into enforceable checks, approvals, provenance requirements, and exception handling.
- Trigger: When releases need stronger automation, control, or governance across CI/CD.
- Primary MCP/tool: repository, logs
- Fallback: reference/reuse, search_query
- Best guess: A CI/CD governance proposal or implementation with controls, exceptions, and rollout guidance.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-ci-cd-governance.md
- Done when: Delivery rules are concrete enough to enforce repeatedly, with owners, exception paths, and enforcement points identified.

## `infra-release`

- Description: Execute a rollback-first infrastructure release by building a release model, selecting the narrowest safe tool path, and verifying rollout, rollback, and operational readiness from present-state evidence.
- Trigger: When infra, platform, IaC, or deployment changes must be released safely.
- Primary MCP/tool: repository
- Fallback: search_query, reference/verify
- Best guess: A release runbook or implementation summary with scope, prereqs, execution, rollback, verification, and residual risk.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-infra-release.md
- Done when: The release path, rollback posture, verification evidence, and remaining unknowns are explicit enough for safe execution or audit.

## `performance-investigation`

- Description: Localize a performance bottleneck by building a USE/RED evidence model from telemetry, traces, metrics, profiles, and runtime output before recommending the next highest-leverage validation.
- Trigger: When latency, throughput, saturation, or cost is degraded and the bottleneck is unclear.
- Primary MCP/tool: repository, logs
- Fallback: search_query, reference/trace
- Best guess: A performance investigation with the leading bottleneck, evidence, and next highest-leverage validation.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-performance-investigation.md
- Done when: The main performance constraint is localized credibly, with evidence, assumptions, and the next validation step explicit.

## `pipeline-orchestration`

- Description: Build a durable-flow model for platform pipelines by clarifying sequencing, scheduling, retries, ownership, observability, and rollout risk before choosing implementation changes.
- Trigger: When build, data, or platform pipelines need orchestration, recovery, or operational hardening.
- Primary MCP/tool: repository, logs
- Fallback: reference/ground, search_query
- Best guess: A pipeline orchestration design or implementation direction with explicit sequencing, retries, ownership, observability, and rollout notes.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-pipeline-orchestration.md
- Done when: The pipeline model, failure behavior, ownership, and observability are explicit enough to implement, review, or operate without hidden assumptions.

## `schema-migration`

- Description: Plan and execute schema changes through engine-native DDL, versioned migration tooling, and rollback-aware rollout sequencing before touching persistent data.
- Trigger: When persistent data models must change safely.
- Primary MCP/tool: repository, logs
- Fallback: reference/trace, search_query
- Best guess: A schema migration plan or implementation with compatibility and rollback considerations.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-schema-migration.md
- Done when: The schema change is bounded, compatible where needed, and safe to deploy or revert with explicit verification.

## `security-hardening`

- Description: Analyze a concrete security weakness, choose the least-invasive effective control, and verify that the remediation measurably reduces risk.
- Trigger: When the system needs a specific security fix, guardrail, or hardening step.
- Primary MCP/tool: repository, logs
- Fallback: reference/verify, search_query
- Best guess: A security hardening change or remediation plan with evidence, residual risk, and verification steps.
- Output: logs/active/<project-slug>/deliverables/platform-engineer-security-hardening.md
- Done when: The weakness, remediation, evidence path, and residual risk are explicit enough to implement and review.
