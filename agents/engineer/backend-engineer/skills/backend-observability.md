---
name: backend-observability
description: Add or refine backend telemetry by building a signal model first, then using logs, traces, metrics, and error data to expose actionable operational insight with explicit cost and privacy tradeoffs.
trigger: When debugging or operations depend on better backend visibility.
analysis_framework: backend observability gap analysis across signals, consumers, alertability, and operational cost
primary_mcp: repository
fallback_tools: search_query, reference/reuse
required_inputs:
  - the service, endpoint, job, or integration boundary being observed
  - the symptom, incident, or visibility gap that needs better signals
  - the environment, build, deploy, or release context when known
  - existing logging, metrics, tracing, and alerting conventions when known
  - privacy, retention, sampling, or cost constraints when relevant
recommended_passes:
  - signal model construction
  - current instrumentation inventory
  - gap and cardinality review
  - alertability and consumer mapping
  - verification and residual risk synthesis
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [sentry, honeycomb, datadog]
  observability:
    primary: [opentelemetry, grafana_loki, grafana_tempo, grafana_prometheus]
    secondary: [grafana_pyroscope]
  artifacts:
    primary: [reference/reuse, search_query]
  fallback:
    primary: [reference/reuse, search_query]
tool_routing:
  - if: live runtime evidence and logs are available
    use: [repository, logs]
  - if: instrumentation seams or propagation code need to be changed or confirmed
    use: [repository, opentelemetry]
  - if: distributed traces or high-cardinality service slicing are needed
    use: [honeycomb, grafana_tempo]
  - if: exception grouping, release regressions, or error fingerprints are the main question
    use: [sentry]
  - if: metrics, dashboards, or alert thresholds are the main question
    use: [grafana_prometheus]
  - if: logs are the primary source of truth
    use: [grafana_loki]
  - if: only static artifacts or docs are available
    use: [reference/reuse, search_query]
best_guess_output: An observability change or backend diagnostics plan with a signal model, instrumentation inventory, verification notes, and explicit residual risk.
output_artifacts: knowledge/backend-engineer-backend-observability.md
done_when: Important backend behavior can be inspected after deployment by the intended operators, with the signal path, consumers, and remaining blind spots documented.
---

# Backend Observability

## Purpose

Add or refine backend telemetry by first modeling what must be observable, then choosing the smallest set of logs, metrics, traces, and diagnostics that make failures, regressions, and operational drift actionable.

This skill is for improving inspectability, alertability, and debugging speed. It is not for generic dashboard sprawl, incident command ownership, or rewriting product behavior without evidence.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/backend-engineer-backend-observability.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: backend-observability`, include:
- `### Coverage goal`: Explain what backend behavior needs better visibility and why.
- `### Signals to add or refine`: Specify the logs, metrics, traces, or diagnostics to change.
- `### Where instrumentation lands`: Identify the services, code paths, or runtime boundaries involved.
- `### Alerting or debugging use`: State how the new signals should be used operationally.
- `### Risk or cost tradeoffs`: Note noise, cost, privacy, or performance tradeoffs.
- `### Verification notes`: Explain how to confirm the instrumentation is useful and working.

## Required Inputs and Assumptions

Required inputs:
- The backend surface in scope, such as a service, endpoint, background job, queue consumer, or external integration.
- The symptom or operational question that needs better visibility.
- The environment or release context when known, including build hash, deploy target, or incident window.
- Existing signal conventions when known, including log schema, metric names, trace propagation, and alert ownership.
- Constraints that affect telemetry design, especially PII, sampling, retention, cardinality, or storage cost.

Known vs unknown:
- Known: the code path or runtime boundary that should become easier to inspect.
- Often unknown: whether the current signals are already good enough, whether the same convention is used everywhere, and which operator will consume the signal.

Assumption rule:
- If key inputs are missing, infer a provisional scope and prefix each inferred item with `Assumed context:`.
- Lower confidence for any finding that depends on an inferred service, release, or consumer.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live runtime and operational evidence - running logs, traces, metrics, and error telemetry from the active system.
2. Structured system access - repository code, telemetry backends, dashboards, alert rules, and vendor consoles such as Sentry, Honeycomb, or Grafana.
3. Design artifacts or documentation - runbooks, architecture docs, incident notes, and observability conventions.
4. Screenshots or static snapshots - exported dashboards, log excerpts, or trace captures.
5. Inference - code patterns and naming conventions when nothing live is available.

Declare which path was used in the deliverable and state its limitations. Prefer live runtime evidence when it exists, and combine repository review with telemetry backend inspection when the signal design needs to be validated end to end.

## Tool Selection Rationale

- `repository` confirms the exact code paths, middleware, handlers, and instrumentation seams.
- `logs` confirms what the service actually emitted under runtime conditions.
- `opentelemetry` is the vendor-neutral path for spans, context propagation, and standard semantic conventions.
- `grafana_loki`, `grafana_tempo`, and `grafana_prometheus` cover the common Grafana LGTM split across logs, traces, and metrics.
- `honeycomb` is strong when high-cardinality trace slicing or fast exploratory debugging is needed.
- `sentry` is strong when exception grouping, release regression detection, and error fingerprints matter.
- `search_query` and `reference/reuse` are useful for current vendor docs, naming conventions, or patterns when live telemetry is missing.

## Tool Stack

**Runtime - primary:**

- `repository`: inspect code, instrumentation calls, and ownership boundaries.
- `logs`: inspect runtime output, error bursts, request IDs, and deployment-era behavior.

**Runtime - secondary:**

- `sentry`: group exceptions, inspect release regressions, and follow error fingerprints.
- `honeycomb`: explore high-cardinality traces and service interactions.
- `datadog`: inspect managed logs, metrics, traces, and alert state when the project uses it.

**Observability - primary:**

- `opentelemetry`: standardize spans, metrics, baggage, propagation, and semantic conventions.
- `grafana_loki`: inspect and query logs.
- `grafana_tempo`: inspect distributed traces.
- `grafana_prometheus`: inspect metrics, thresholds, and alert expressions.

**Observability - secondary:**

- `grafana_pyroscope`: inspect profiling signals when the bottleneck is CPU, memory, or latency amplification.

**Artifacts - primary:**

- `reference/reuse`: reuse existing observability patterns, runbooks, and conventions.
- `search_query`: confirm current vendor behavior or official guidance when needed.

**Fallback - primary:**

- `reference/reuse`
- `search_query`

## Tool Routing

- If the runtime is live and operational telemetry exists, start with `repository` and `logs`.
- If context propagation, span naming, or metric design must be changed, use `opentelemetry` alongside repository review.
- If the question depends on distributed trace exploration or high-cardinality filtering, use `honeycomb` or `grafana_tempo`.
- If the question is about exception clustering or release regression monitoring, use `sentry`.
- If the question is about thresholds, counters, ratios, or alert noise, use `grafana_prometheus`.
- If the question is about structured log content, correlation IDs, or event ordering, use `grafana_loki`.
- If only static artifacts exist, fall back to `reference/reuse` and `search_query`.
- Avoid a single-signal answer when the issue crosses logs, metrics, and traces. Combine tools when the runtime story is incomplete.

## Tool Path

- Start with `repository, logs`.
- If instrumentation seams or semantic conventions need changes, use `opentelemetry`.
- If traces are the main debugging surface, use `honeycomb` or `grafana_tempo`.
- If metrics and alert thresholds are the main question, use `grafana_prometheus`.
- If logs are the dominant evidence path, use `grafana_loki`.
- If the project relies on vendor backends such as `sentry` or `datadog`, use them to confirm operator usefulness and runtime behavior.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `reference/reuse, search_query`.
- If both paths fail, produce the best-guess output described as: An observability change or backend diagnostics plan with a signal model, instrumentation inventory, verification notes, and explicit residual risk.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Environment and Reproducibility

Record the following when known:

- Service or boundary under review.
- Environment, deployment target, or incident window.
- Build hash, version, release tag, or container image digest.
- Runtime, collector, or agent version when instrumentation behavior depends on it.
- Sampling rate, retention window, and log or trace export settings.
- Auth state, data state, and feature flags that affect emitted telemetry.
- Correlation IDs, trace IDs, or request IDs used to reproduce the signal.
- Region or cluster when the same path behaves differently across environments.

If any of the above is unknown, state it explicitly. Do not treat staging telemetry as production parity without noting the gap.

## Model Building

Build the observability model before analysis. No conclusions about signal quality should be written before the model exists.

Model the following:

- The observable surface: request, job, queue, integration, cache path, or scheduled task.
- The signal chain: entry point, downstream calls, retries, state transitions, and emitted telemetry.
- The consumers: developer, oncall, SRE, support, or release reviewer.
- The decision question: detect, diagnose, alert, or explain.
- The constraints: privacy, cost, cardinality, retention, and performance overhead.
- The success condition: what signal would let a person act with confidence.

## Core Method Execution

Follow this sequence:

1. Clarify the visibility goal. Name the exact backend behavior that must be seen, and who needs to see it.
2. Inventory current signals. List the logs, metrics, traces, dashboards, and alerts that already exist for the surface.
3. Map the runtime path. Identify entry points, downstream dependencies, retries, and error boundaries that should produce telemetry.
4. Check signal quality. Look for missing correlation IDs, noisy fields, unhelpful messages, sparse metrics, hidden retries, or broken trace propagation.
5. Check alertability. Decide whether the signal can page, warn, or only inform, and whether the threshold is actionable.
6. Design the smallest useful change. Prefer a targeted field, span, or metric over broad instrumentation spread.
7. Verify the change. Confirm that the new signal is visible, low-noise, and tied to a concrete debugging or operational use.
8. Synthesize the deliverable. Record the path used, what improved, what remains blind, and the residual risk.

Use OpenTelemetry semantic conventions when they fit the project, and preserve existing naming or tagging conventions when those are already established.

## Workflow Notes

- Optimize for actionable signals rather than telemetry volume.
- Preserve existing observability conventions unless they are themselves the problem.
- Keep operator consumers explicit so the added telemetry has a clear user.
- Make privacy, sampling, retention, and cardinality tradeoffs visible instead of implied.
- Separate signal design from broader product or infrastructure redesign.

## Structured Findings

Every finding must use this exact schema. Keep observation separate from interpretation. Every finding must be traceable to a signal, code path, or dashboard.

```text
#### Finding <id>
Observation: [What was seen, without interpretation]
Evidence: [Tool or source used + signal, route, dashboard, or trace reference]
Cause: [Why this likely exists; prefix with inferred if not confirmed from code or runtime]
Impact: [Effect on debugging speed, alertability, safety, privacy, or operational cost]
Confidence: [High / Medium / Low + rationale]
```

## Prioritization Logic

Prioritize findings by operational impact and the amount of blind spot they create:

1. Critical - missing or misleading signals on a critical path, invisible failures, broken correlation, unsafe PII exposure, or an alert gap that blocks response.
2. Significant - noisy logs, weak metrics, incomplete traces, poor thresholding, or missing signal consumers that reduce usefulness without fully blocking diagnosis.
3. Minor - naming cleanup, dashboard polish, or convenience fields. Group these into patterns rather than standalone findings unless they materially affect use.

## Pattern Detection

Look for recurring system-level problems, especially:

- Missing correlation IDs or trace context across service boundaries.
- Log spam, duplicate events, or unbounded cardinality.
- Alerts that fire without an actionable owner or runbook.
- Metrics that exist but cannot explain the failure mode.
- Retries, fallbacks, or compensations that are invisible in telemetry.
- PII, secrets, or user identifiers leaking into logs or traces.
- Signal duplication where logs, metrics, and traces disagree about the same incident.

## Recommendations

Recommendations must:

- Link to a specific finding by ID.
- Be directional, not fully prescriptive.
- Name the consumer or operational decision the signal should support.
- Note evidence limits when confidence is Medium or Low.

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly in the deliverable:

- Fully implemented - signals or dashboards that were inspected and confirmed useful.
- Partially implemented - paths or signals that exist but are incomplete, sampled, or non-production only.
- Not implemented - blind spots or telemetry gaps that still need work.
- Not analyzed - signal surfaces that were out of scope, inaccessible, or not needed for the current question.

## Limits and Unknowns

Mandatory section. State:

- What could not be validated from the available runtime or repository evidence.
- Where sampling, retention, or access limits may distort the conclusion.
- Which signals need real production traffic to prove usefulness.
- Where cost, privacy, or cardinality risk could not be fully measured.
- Any vendor-specific behavior that remains unconfirmed.

## Workflow Rules

The agent must:

- Build the signal model before analysis.
- Distinguish observed evidence from inference.
- Merge duplicate findings across logs, traces, and metrics.
- Avoid adding telemetry that cannot support a decision.
- Prefer existing conventions over new ones when both solve the same problem.
- Keep privacy, cost, and cardinality explicit.
- Document what remains blind instead of overstating confidence.

