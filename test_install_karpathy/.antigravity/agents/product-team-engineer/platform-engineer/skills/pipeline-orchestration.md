---
name: pipeline-orchestration
description: Build a durable-flow model for platform pipelines by clarifying sequencing, scheduling, retries, ownership, observability, and rollout risk before choosing implementation changes.
trigger: When build, data, or platform pipelines need orchestration, recovery, or operational hardening.
mesh:
  inputs:
    - backend-engineer:integration-flow-build
  next:
    - platform-engineer:infra-release
  context: "Orchestrates the build and deployment pipelines for the feature."
primary_mcp: repository, logs
fallback_tools:
  - reference/ground
  - search_query
required_inputs:
  - the pipeline, workflow, scheduler, queue, or event path under review
  - the trigger, cadence, or upstream condition that starts work
  - the desired outputs, side effects, and ownership boundaries for each stage
  - retry, timeout, ordering, backfill, compensation, and idempotency expectations
  - the environment, deployment stage, and any known operational constraints
  - runtime evidence such as logs, traces, metrics, run history, or job status when available
recommended_passes:
  - pipeline scope and boundary inventory
  - sequence and dependency modeling
  - retry, failure, and recovery analysis
  - ownership, scheduling, and handoff review
  - observability and rollout risk review
  - pattern detection and anti-pattern sweep
  - synthesis and prioritization
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [traces, metrics]
  orchestration:
    primary: [temporal, aws_step_functions, argo_workflows]
    secondary: [airflow, prefect, dagster, kubernetes_cronjob]
    emerging: [restate, hatchet, inngest, windmill, conductor, mage_ai]
  stream_processing:
    primary: [apache_flink, kafka_connect]
    secondary: [bytewax, redpanda_connect, estuary_flow]
    cloud: [eventbridge, sqs, sns]
  serverless_compute:
    primary: [modal]
    secondary: [aws_lambda, cloud_run]
  data_pipeline:
    primary: [dagster, prefect]
    secondary: [mage_ai, hamilton, kestra]
  observability:
    primary: [opentelemetry, prometheus, grafana]
    secondary: [search_query]
  artifacts:
    primary: [docs, diagrams]
  fallback:
    primary: [reference/ground, search_query]
tool_routing:
  - if: the work is a durable, long-running, or human-in-the-loop workflow
    use: [temporal]
  - if: the work is durable execution but Temporal is too heavy or self-hosted setup is a constraint
    use: [restate, hatchet]
  - if: the work is event-driven and runs in a serverless or edge environment
    use: [inngest]
  - if: the work is aws-native and the control flow is best expressed as a state machine
    use: [aws_step_functions]
  - if: the work is kubernetes-native, container-first, or DAG-shaped
    use: [argo_workflows]
  - if: the work is scheduled batch orchestration with Python-first authoring
    use: [airflow, prefect, dagster]
  - if: the work is a data pipeline with asset-centric lineage and observability needs
    use: [dagster]
  - if: the work is a data pipeline targeting cloud-native sources with low-code authoring
    use: [mage_ai]
  - if: the work is a lightweight Python-first feature or data transformation DAG
    use: [hamilton]
  - if: the work is declarative and language-agnostic with YAML-first workflow definitions
    use: [kestra, windmill]
  - if: the work is Netflix/microservice-style long-running workflow with language-agnostic support
    use: [conductor]
  - if: the work is mostly time-based and runs as a simple periodic job
    use: [kubernetes_cronjob]
  - if: the work is stateful stream processing with exactly-once guarantees at scale
    use: [apache_flink]
  - if: the work is Python stream processing without JVM overhead
    use: [bytewax]
  - if: the work moves records between systems through connectors or CDC
    use: [kafka_connect, redpanda_connect]
  - if: the work is real-time CDC and streaming pipelines with unified batch support
    use: [estuary_flow]
  - if: the work is serverless compute for data-heavy or ML pipeline stages
    use: [modal]
  - if: the key risk is signal quality, correlation, or alertability
    use: [opentelemetry, prometheus, grafana]
  - if: runtime evidence is thin or the target system is not accessible
    use: [reference/ground, search_query]
best_guess_output: A pipeline orchestration design or implementation direction with explicit sequencing, retries, ownership, observability, and rollout notes.
output_artifacts: knowledge/platform-engineer-pipeline-orchestration.md
done_when: The pipeline model, failure behavior, ownership, and observability are explicit enough to implement, review, or operate without hidden assumptions.
---

# Pipeline Orchestration

## Purpose

Build or improve platform pipeline orchestration by modeling the flow first, then choosing the least risky orchestration path for the platform. This skill focuses on durable execution, scheduling, retries, handoffs, and operator visibility. It does not own domain modeling, API contract design, or generic backend implementation guidance unless those affect the pipeline directly.

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/platform-engineer-pipeline-orchestration.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Inputs and Assumptions

Required inputs:
- The pipeline, workflow, scheduler, queue, or event path under review
- The trigger, cadence, or upstream condition that starts work
- The desired outputs, side effects, and ownership boundaries for each stage
- Retry, timeout, ordering, backfill, compensation, and idempotency expectations
- The environment, deployment stage, and any known operational constraints
- Runtime evidence such as logs, traces, metrics, run history, or job status when available

If inputs are missing, infer a provisional frame and prefix each inferred item with `Assumed pipeline context:`. Lower confidence for any conclusion that depends on inferred context.

Known vs unknown:
- The orchestration surface may be explicit in code or only implied by schedulers, queues, or cron definitions.
- Delivery semantics, ownership, and rollback posture are often under-specified and must be surfaced before conclusions are written.
- Time-based behavior can differ across environments, so schedule, timezone, and data windows must be recorded when known.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live or current runtime evidence from logs, traces, metrics, workflow history, queue state, or job runs.
2. Structured repository evidence from code, configs, tests, manifests, and deployment definitions.
3. Design artifacts or documentation such as ADRs, runbooks, diagrams, or platform notes.
4. Screenshots, static payload samples, or incident attachments.
5. Inference from naming, conventions, or adjacent code.

State which path was used and note its limits. Prefer live evidence when the goal is to validate present behavior; prefer repository evidence when the goal is to understand intended orchestration.

## Environment and Reproducibility

Record the following when known:
- service, repository, cluster, namespace, or workflow name
- deployment stage, build hash, image tag, or release version
- scheduler, queue, topic, cron, or workflow identifiers
- timezone, cadence, retention window, and replay window when relevant
- auth state, tenancy, and any feature flags or rollout gates
- sample run IDs, correlation IDs, trace IDs, or failing job IDs
- the exact tooling or environment used to observe the pipeline

If anything is unknown, state it explicitly. Do not present test or staging behavior as equivalent to production unless that was actually verified.

## Model Building

Before analysis, build a pipeline model with these elements:
- stages, triggers, and downstream side effects
- synchronous versus asynchronous segments
- dependencies, ordering, and fan-out or fan-in points
- retry, timeout, backoff, duplicate delivery, and compensation behavior
- backfill, replay, pause, resume, and drain behavior
- ownership boundaries and operator intervention points
- logs, metrics, traces, alerts, and debug hooks
- blast radius, rollout gates, and rollback paths

No conclusion should be written before this model exists.

## Required Deliverable Sections

Within `## Skill: pipeline-orchestration`, include:
- `### Pipeline scope`: Define the exact pipeline, workflow, or flow being reviewed.
- `### Required inputs and assumptions`: State what was known, what was missing, and which assumptions were made.
- `### Input mode and evidence path`: Identify the evidence path used and its limits.
- `### Environment and reproducibility`: Record the stage, identifiers, timing, and context needed to replay or compare behavior.
- `### Pipeline model`: Capture stages, dependencies, ownership, and operator boundaries before any recommendation.
- `### Orchestration choice`: Explain why the chosen engine, scheduler, or event pipeline fits the workload.
- `### Failure and recovery`: Describe retries, backoff, dead-lettering, compensation, backfill, replay, and manual recovery.
- `### Observability and operations`: State the signals needed to run, debug, and alert on the flow.
- `### Pattern detection`: Identify recurring anti-patterns observed across the pipeline.
- `### Structured findings`: Document each issue using the structured findings schema.
- `### Prioritization logic`: Rank the highest-risk issues by user impact, data loss risk, stalled work, or operational load.
- `### Recommendations`: Give the smallest safe next steps tied directly to findings and risks.
- `### Coverage map`: State what was deeply analyzed, partially analyzed, and not analyzed.
- `### Open risks`: Call out ambiguities, missing evidence, or rollout concerns that remain.
- `### Limits and unknowns`: Explain what could not be validated and what still needs real-world confirmation.

## Tool Path

- Start with `repository, logs`.
- Use `temporal` when the flow needs durable execution, long waits, retries, signals, or human-in-the-loop steps.
- Use `restate` or `hatchet` when durable execution is needed but Temporal's operational overhead or SDK coupling is a constraint; both are lighter-weight alternatives with strong durability guarantees.
- Use `inngest` when the workflow is event-triggered, serverless-friendly, or needs fan-out without managing queues explicitly.
- Use `windmill` when the team needs a self-hosted, open-source workflow engine with a built-in UI for script-to-workflow conversion.
- Use `conductor` when the platform is microservice-oriented and needs language-agnostic, long-running workflow definitions at scale (originally Netflix OSS, now open-source under Orkes).
- Use `aws_step_functions` when the orchestration is best expressed as a managed state machine with explicit task transitions.
- Use `argo_workflows` when the platform is Kubernetes-native, container-first, or DAG-shaped.
- Use `airflow`, `prefect`, or `dagster` when the pipeline is scheduled, batch-oriented, or easiest to express as code-first DAGs or assets.
- Use `dagster` specifically when asset lineage, data quality checks, and developer-facing observability are first-class concerns.
- Use `mage_ai` when the team wants low-code or cloud-native data pipeline authoring with built-in support for batch and streaming.
- Use `hamilton` when the pipeline is a lightweight Python DAG for feature engineering, data transforms, or ML pipelines that should not carry orchestrator overhead.
- Use `kestra` when the team wants declarative, language-agnostic YAML-first workflow definitions.
- Use `kubernetes_cronjob` when the flow is a simple periodic job with limited branching.
- Use `apache_flink` when the pipeline requires stateful stream processing, exactly-once semantics, or complex event processing at scale.
- Use `bytewax` when the stream processing must be Python-native and the team wants to avoid JVM-based tooling.
- Use `kafka_connect` or `redpanda_connect` when the work is connector-driven or centered on streaming, CDC, or source/sink movement; prefer `redpanda_connect` (formerly Benthos) for its 300+ connector ecosystem and lightweight deployment.
- Use `estuary_flow` when the pipeline needs unified real-time CDC, streaming, and batch movement across sources and destinations.
- Use `modal` when individual pipeline stages need serverless, GPU-backed, or burst compute without managing container infrastructure.
- Use `opentelemetry`, `prometheus`, and `grafana` when observability, correlation, or alertability is the main uncertainty.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A pipeline orchestration design or implementation direction with explicit sequencing, retries, ownership, observability, and rollout notes.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Tool Selection Rationale

- Use `repository` to confirm intended code, config, and deployment state; it cannot prove runtime health.
- Use `logs`, `traces`, and `metrics` to confirm present behavior; they cannot prove future stability.
- Use `temporal` for long-running, stateful, or human-gated flows where exactly-once activity execution matters; its SDK coupling and operational footprint are the tradeoff.
- Use `restate` when you need durable execution with a lighter footprint than Temporal; it embeds into services and avoids a separate orchestration cluster.
- Use `hatchet` for cloud-native task queues that need durable execution, fair queuing, and concurrency control without full Temporal complexity.
- Use `inngest` for event-triggered workflows in serverless environments where you want zero-queue-management and built-in retries.
- Use `conductor` when your platform is polyglot and you need language-agnostic workflow definitions with a strong separation between orchestration logic and worker implementation.
- Use `windmill` when you want an open-source, self-hosted alternative that turns scripts into workflows and UIs without additional glue code.
- Use `airflow`, `prefect`, `dagster` only when the workload shape matches their native strengths: scheduled batch jobs, DAG-first authoring, or asset-centric data pipelines respectively.
- Use `mage_ai` for teams that want a modern, interactive Airflow alternative with lower authoring friction and cloud-native integrations.
- Use `hamilton` for lightweight Python function-DAGs where importing a full orchestrator would be overkill; it has no scheduler and must be called by another runner.
- Use `apache_flink` for stateful, high-throughput stream processing where exactly-once guarantees and complex windowing are required; its JVM footprint and operational complexity are the tradeoff.
- Use `bytewax` when Python-native stream processing is preferred and JVM tooling is a constraint; it is less mature than Flink for large-scale stateful workloads.
- Use `redpanda_connect` (formerly Benthos) for message routing, transformation, and fan-out between sources and sinks; its 300+ connector library is its main strength.
- Use `estuary_flow` when CDC and real-time streaming pipelines need to be defined declaratively with both batch and streaming targets.
- Use `modal` for burst or GPU-dependent pipeline stages where serverless container management would otherwise add operational overhead.
- Use `opentelemetry`, `prometheus`, and `grafana` to validate signal quality, correlation, and alertability rather than correctness alone.
- Use `reference/ground` and `search_query` only when the primary evidence path is thin or unavailable.

## Workflow Notes

- Treat retries, ownership, and observability as design constraints, not afterthoughts.
- Separate happy-path sequencing from failure handling, replay, and recovery.
- Preserve exact queue, topic, job, schedule, and workflow identifiers when they matter.
- Keep the orchestration engine, the trigger, and the data plane responsibilities distinct.
- Prefer concrete state transitions and timing over generic prose.
- Do not recommend a heavyweight orchestration engine when a simpler scheduler or function DAG would do the same job.
- When choosing between streaming tools, verify whether exactly-once delivery is actually required or if at-least-once with idempotent consumers is sufficient.

## Pattern Detection

Before writing findings, sweep the pipeline model for these recurring anti-patterns. If a pattern is present, flag it in findings:

- **Retry storm**: No backoff or jitter on retries; downstream gets hammered during failure cascades. Look for fixed-interval retry configs or missing exponential backoff settings.
- **Missing idempotency keys**: Workers process the same message or job twice without deduplication logic. Look for missing correlation IDs, absent unique constraint checks, or repeated side effects in logs.
- **Ownership gap**: A pipeline stage has no clear on-call owner or runbook pointer. Look for stages with no team label, no alert routing, or no SLA definition.
- **Observability blindspot**: A stage emits no metrics, no traces, or no structured logs. Look for stages where the only signal is job exit code or absence of errors.
- **Fan-out without back-pressure**: A trigger spawns unbounded parallel work with no concurrency limit or queue depth guard. Look for fan-out points without rate limits or worker pool caps.
- **Implicit ordering assumption**: A stage assumes upstream order without a guarantee. Look for stages that consume from queues or topics without partition key or sequencing enforcement.
- **Scheduler drift**: A cron or time-based job accumulates lag because it is not catching up after missed windows. Look for jobs that skip rather than backfill missed runs.
- **Silent discard**: Messages or events are dropped without a dead-letter queue, alert, or log entry. Look for consumer error handlers that only log and continue.
- **Config-environment mismatch**: A pipeline uses different retry, timeout, or concurrency settings between staging and production. Look for environment-specific overrides that diverge silently.
- **Monolithic DAG**: A single DAG or workflow encodes too many unrelated responsibilities, making partial failure and partial replay impossible. Look for DAGs with 30+ tasks or mixed ownership domains.

## Structured Findings

Use this exact schema for review or diagnosis output. No free-form findings:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps or validation path:
- Cause:
- Impact:
- Confidence:

## Prioritization Logic

- Critical: data loss, duplicate side effects, unrecoverable backlog, or broken recovery.
- High: stalled pipelines, retry storms, missed schedules, or ownership gaps that block operations.
- Medium: observability gaps, unclear handoffs, or rollout complexity.
- Low: naming, layout, or documentation drift that does not change behavior.
- Group repeated low-risk issues into patterns instead of splitting them across many findings.

## Recommendations

Recommendations must follow these rules:
- Every recommendation must reference at least one finding ID or named risk.
- Prefer the smallest safe change that reduces the highest-priority risk.
- Do not recommend a full re-platform when a config change or guardrail would address the finding.
- Express confidence level: high (evidence-backed), medium (inferred from pattern), or low (speculative).
- Separate immediate operational actions from longer-term architectural improvements.
- Do not over-specify implementation details; leave room for the team to own the solution.

Recommendation schema:

#### Recommendation <id>
- Links to: [Finding <id> or Risk name]
- Action:
- Rationale:
- Confidence:
- Priority: [Critical / High / Medium / Low]
- Effort estimate: [hours / days / sprint]

## Coverage Map

State the analysis depth for each area of the pipeline:

**Deeply analyzed** — areas where live evidence, code, or config was reviewed and conclusions are grounded:
- List each area with the evidence source used.

**Partially analyzed** — areas where some evidence exists but gaps remain:
- List each area and name what is missing.

**Not analyzed** — areas outside the scope of this pass or where evidence was unavailable:
- List each area and note whether it should be addressed in a follow-up pass.

The coverage map must be written before the Recommendations section is considered complete. Do not recommend actions on areas listed as not analyzed without explicitly flagging the confidence as low and speculative.


## Limits and Unknowns

- Do not claim delivery guarantees that the evidence does not support.
- Do not treat a healthy local run as proof of production safety.
- Do not assume exactly-once behavior unless the system explicitly proves it.
- Do not overfit to one scheduler or workflow engine when the same control flow can be modeled multiple ways.
- Do not recommend emerging tools (Restate, Hatchet, Inngest, Bytewax, Modal) for high-criticality production pipelines without first confirming production maturity, community support, and team familiarity.
- State any unresolved timing, tenancy, rollout, or replay uncertainty plainly.
- If stream processing tool choice is uncertain, flag the JVM vs. Python tradeoff and exactly-once requirement explicitly before recommending Flink or Bytewax.
