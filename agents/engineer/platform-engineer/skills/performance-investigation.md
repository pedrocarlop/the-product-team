---
name: performance-investigation
description: Localize a performance bottleneck by building a USE/RED evidence model from telemetry, traces, metrics, profiles, and runtime output before recommending the next highest-leverage validation.
trigger: When latency, throughput, saturation, or cost is degraded and the bottleneck is unclear.
method_label: use-red-bottleneck-localization
analysis_framework: USE + RED performance investigation across utilization, saturation, errors, rate, and duration
primary_mcp: repository, logs
fallback_tools: search_query, reference/trace
required_inputs:
  - the exact symptom, surface, or workflow being investigated
  - the service, job, endpoint, cluster, or deploy in scope
  - the target or baseline when known, including latency, throughput, CPU, memory, or cost expectations
  - the environment and time window where the issue was observed
  - any trace IDs, dashboards, profiles, logs, or benchmark results already available
  - the workload shape, traffic pattern, and auth or data state when relevant
recommended_passes:
  - performance model construction
  - evidence inventory
  - USE/RED bottleneck scan
  - dependency and saturation check
  - profiling or trace drill-down
  - validation and residual risk synthesis
tool_stack:
  runtime:
    primary: [repository, logs]
    secondary: [sentry, datadog, newrelic]
  observability:
    primary: [opentelemetry, grafana_loki, grafana_tempo, grafana_prometheus]
    secondary: [grafana_pyroscope, honeycomb, signoz, uptrace]
  tracing:
    primary: [grafana_tempo, opentelemetry]
    secondary: [jaeger, zipkin]
  profiling:
    primary: [grafana_pyroscope]
    secondary: [parca, async_profiler, clinic_js, perf, pprof, bpftrace, flamescope]
  ebpf_observability:
    primary: [coroot]
    secondary: [pixie, parca]
  load_testing:
    primary: [k6]
    secondary: [vegeta, artillery, gatling, oha, bombardier, benchmark_harness]
  fallback:
    primary: [search_query, reference/trace]
tool_routing:
  - if: live telemetry or runtime logs are available
    use: [repository, logs, opentelemetry]
  - if: request latency, dependency timing, or error propagation is unclear
    use: [grafana_tempo, grafana_prometheus, grafana_loki]
  - if: open-source Datadog alternative is preferred for traces, metrics, and logs
    use: [signoz, uptrace]
  - if: CNCF-graduated tracing backend is preferred
    use: [jaeger]
  - if: CPU, memory, GC, lock contention, or hot code paths are suspected
    use: [grafana_pyroscope, perf, pprof]
  - if: eBPF-based continuous profiling is needed with low overhead
    use: [parca]
  - if: JVM hot-path or lock contention profiling is needed
    use: [async_profiler]
  - if: Node.js event loop, I/O blocking, or CPU profiling is needed
    use: [clinic_js]
  - if: Kubernetes-native auto-instrumented service map and bottleneck detection is needed
    use: [coroot, pixie]
  - if: the issue only appears under pressure or queue buildup
    use: [k6]
  - if: constant-rate HTTP load testing is needed
    use: [vegeta]
  - if: scenario-based or multi-protocol load testing is needed
    use: [artillery, gatling]
  - if: quick HTTP benchmarking or latency distribution check is needed
    use: [oha, bombardier]
  - if: managed observability is already instrumented
    use: [sentry, datadog, newrelic]
  - if: only static artifacts exist
    use: [search_query, reference/trace]
best_guess_output: A performance investigation with the leading bottleneck, evidence, and next highest-leverage validation.
output_artifacts: logs/active/<project-slug>/deliverables/platform-engineer-performance-investigation.md
done_when: The main performance constraint is localized credibly, with evidence, assumptions, and the next validation step explicit.
---

# Performance Investigation

## Purpose

Localize a performance bottleneck by building a USE/RED model first, then testing the candidate bottleneck against live telemetry, traces, metrics, profiles, load tests, and repository evidence.

This skill is for diagnosis and localization. It does not make the final infra change unless the user explicitly asks for implementation.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/platform-engineer-performance-investigation.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: performance-investigation`, include:
- `### Symptom framing`: State the exact slowdown, saturation, or cost problem and the scope.
- `### Required inputs and assumptions`: List what was known, what was missing, and what had to be assumed.
- `### Input mode and evidence path`: Declare whether the analysis used live runtime evidence, structured system access, artifacts, screenshots, or inference.
- `### Environment and reproducibility`: Record the environment, build or deploy version, workload shape, auth or data state, and parity caveats.
- `### Performance model`: Build the resource and request-path model before conclusions.
- `### Evidence reviewed`: Summarize the logs, traces, metrics, profiles, load tests, or code paths that actually informed the diagnosis.
- `### Core method execution`: Record which step of the method was reached and what it produced.
- `### Structured findings`: Record findings with the required schema below.
- `### Pattern detection`: Call out any recurring anti-patterns identified.
- `### Prioritization logic`: Explain how bottlenecks were ordered and grouped.
- `### Tool path`: State the path used, why it was chosen, and what it could not validate.
- `### Recommendations`: Link each recommendation to a specific finding; be directional, not overconfident.
- `### Coverage map`: State what was deeply analyzed, partially analyzed, and not analyzed.
- `### Workflow notes`: Capture method discipline, inference limits, and any validation sequence used.
- `### Limits and unknowns`: State what could not be proven and what still needs real-world verification.

## Required Inputs and Assumptions

Required inputs:
- The exact symptom and what "slow" means in this case.
- The service, endpoint, job, cluster, or deploy in scope.
- The performance target or baseline when known.
- The environment and time window where the issue was observed.
- Any telemetry IDs, dashboards, traces, profiles, logs, or benchmark results already available.
- The workload shape, traffic pattern, and auth or data state when relevant.

Known vs unknown:
- Known at trigger time: the symptom, the affected surface, and often the rough environment.
- Often unknown: whether the issue is CPU-, memory-, I/O-, dependency-, or queue-bound, and whether the regression is local, regional, or release-specific.

Assumption rule:
- If a required input is missing, infer a provisional frame and prefix each inferred item with `Assumed context:`.
- Lower confidence on any finding that depends on an inferred environment, workload, or baseline.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. Live runtime / traffic evidence — direct system behavior under real or reproduced load.
2. Structured system access — logs, traces, metrics, profiles, vendor consoles, and benchmark outputs.
3. Documentation or design artifacts — runbooks, architecture notes, SLOs, or workload descriptions.
4. Screenshots or static snapshots — exported charts, trace captures, or console output.
5. Inference — code reading and symptom matching when no live evidence exists.

Declare the path used in `### Evidence reviewed` and note its limits. Prefer live evidence when it exists, then combine telemetry with repository review when the signal needs end-to-end confirmation.

## Environment and Reproducibility

Capture the following when known:

- Environment and deploy target.
- Build hash, version, release tag, or image digest.
- Region, cluster, or node pool when relevant.
- Authentication state, user role, and data state.
- Traffic shape, request mix, concurrency, and queue depth.
- Sampling, retention, or export settings that affect visibility.
- Browser, device, or client context when the slowdown is user-facing.

If any item is unknown, say so explicitly. Do not treat staging, sampled, or synthetic traffic as production parity unless that gap has been checked.

## Performance Model

Build the model before conclusions:

- Workload shape: steady state, burst, cron-driven, queue-driven, or interactive.
- Resource model: CPU, memory, disk, network, allocation, GC, connection pools, or locks.
- Request model: rate, errors, duration, retries, backpressure, and downstream spans.
- Dependency model: which service, queue, cache, datastore, or external API could be the ceiling.
- Baseline model: what changed, when it changed, and what "normal" looked like before the regression.

Anchor the analysis to USE for resource bottlenecks and RED for request paths. When a service is dependency-bound, include queueing, downstream latency, retries, and backpressure in the model. No conclusion before the model exists.

## Evidence Reviewed

State what was actually checked:

- Request path and code paths in the repository.
- Runtime logs and error bursts.
- Traces and span timing.
- Metrics, dashboards, and saturation trends.
- Profiles or flame graphs.
- Load tests or benchmark runs.

For each signal, note what it can confirm and what it cannot. A missing metric is not evidence of safety.

## Core Method Execution

Execute these steps in sequence. Record which step was reached and what it produced.

1. **Frame the symptom.** State the observable degradation in concrete terms: which surface, which metric, how far from baseline, and when it started. Do not proceed with vague inputs.

2. **Build the performance model.** Map the workload shape, resource model, request model, dependency model, and baseline before looking at any data. This model is the hypothesis scaffold.

3. **Inventory available evidence.** List every signal that exists: traces, metrics, logs, profiles, load test results, alerts. Note what is missing and what the gap implies.

4. **Run the USE/RED scan.** For each resource (CPU, memory, disk, network, connection pools, GC, locks): check Utilization, Saturation, and Errors. For each request path: check Rate, Errors, and Duration. Identify which dimension is breaching first.

5. **Drill into profiling and traces.** If the USE/RED scan points to a specific resource or span, open the matching profiler or trace backend. Look for hot code paths, long-tail spans, retried calls, or lock contention windows. Use flame graphs to confirm the CPU or allocation story.

6. **Reproduce under load if needed.** If the bottleneck only manifests under pressure, use a load tool to recreate the workload shape. Validate that saturation, queue depth, or latency degradation appears at the expected concurrency.

7. **Validate the hypothesis.** Check whether the candidate bottleneck explains the observed symptom end-to-end. If it does not fully explain the symptom, note the residual gap and list what would close it.

8. **Synthesize findings and next steps.** Produce structured findings, a prioritization rationale, and a recommendation for the single next highest-leverage validation or remediation.

## Pattern Detection

Identify recurring anti-patterns during the USE/RED scan and profiling drill. Check for:

- **N+1 queries**: repeated fine-grained database calls inside a loop; visible as many near-identical short spans in a trace.
- **Connection pool exhaustion**: threads blocked waiting for a DB or HTTP connection; visible as queue depth growth and timeout bursts.
- **GC pressure**: allocation rate exceeding collection throughput; visible in heap profilers, GC pause logs, and allocation flame graphs.
- **Retry amplification**: upstream retry storms magnifying a transient downstream error into sustained overload.
- **Missing caching layer**: identical expensive reads repeated across requests; visible in trace fan-out and high DB read rates.
- **Hot lock contention**: threads serializing on a single mutex or synchronized block; visible in thread profilers and lock wait metrics.
- **Thread or goroutine starvation**: insufficient concurrency budget for the actual workload; visible in queue depth and p99 divergence from p50.
- **Unbounded fan-out**: scatter/gather calls where the number of downstream calls grows with request size; visible in span count spikes.
- **Cold-start spikes**: latency bursts tied to JIT compilation, connection establishment, or cache warmup after a deploy.
- **Clock skew or timeout misconfiguration**: client timeouts shorter than server processing time, causing premature failures that mask real latency.

Record each detected pattern with the evidence that supports it. Do not assert a pattern without an evidence reference.

## Structured Findings

Use this exact schema:

#### Finding <id>
- Observation:
- Evidence:
- Repro or validation path:
- Bottleneck hypothesis:
- Impact:
- Priority:
- Confidence:

Rules:
- Separate observation from interpretation.
- Merge duplicates that share the same bottleneck.
- Label any inference that depends on missing runtime evidence.
- Sort findings by the bottleneck that most constrains user experience or system stability.

## Prioritization Logic

- Prioritize customer-visible latency, throughput collapse, error amplification, and cost blowups first.
- Then prioritize sustained saturation, queue growth, GC pressure, lock contention, or hot loops that explain the symptom.
- Group related low-level symptoms under one root cause when they share a dependency or resource ceiling.
- Do not split one bottleneck into multiple findings unless the evidence shows independent causes.

## Recommendations

Each recommendation must:
- Reference a specific finding by ID.
- State the expected outcome if the recommendation is applied.
- Be directional, not overconfident — frame as "most likely to reduce X" not "will fix X".
- Include the next validation step needed to confirm the recommendation was effective.
- Flag when the recommendation requires load testing, profiling, or runtime measurement to verify rather than a code change alone.

Do not issue recommendations for findings with low confidence without explicitly labeling them as speculative.

## Tool Selection Rationale

- `repository` confirms the exact code paths, config, deployment wiring, and benchmark harnesses.
- `logs` confirms what the system actually emitted under runtime conditions.
- `opentelemetry` gives vendor-neutral correlation across traces, metrics, and logs; preferred for OTEL-instrumented stacks.
- `grafana_loki`, `grafana_tempo`, and `grafana_prometheus` separate log, trace, and metric analysis within the Grafana stack.
- `grafana_pyroscope` is the first choice for CPU, memory, allocation, and hot-path profiling; integrates natively with Grafana dashboards and supports Go, Python, Ruby, Java, .NET, PHP, Rust, and eBPF agents.
- `parca` is an eBPF-based continuous profiling platform backed by Polar Signals; well-suited for compiled languages (Go, C, C++, Rust) with sub-1% overhead and native pprof compatibility; fully open-source with strong Prometheus integration.
- `async_profiler` is the preferred low-overhead JVM profiler for Java and Kotlin; captures CPU, wall-clock, allocation, and lock contention without the bias of safepoint-based profilers; ideal for production JVM services.
- `clinic_js` (clinic doctor, clinic flame, clinic bubbleprof) diagnoses Node.js-specific issues: event loop blocking, async I/O bottlenecks, and CPU hot paths; runs as a standalone wrapper with minimal setup.
- `bpftrace` and `perf` are Linux system-level tools for tracing kernel calls, I/O, and scheduling; use when user-space profilers miss the bottleneck.
- `flamescope` provides time-series heat-map visualization of stack traces (developed at Netflix); useful for identifying intermittent or periodic CPU spikes that aggregate profilers would hide.
- `coroot` is an eBPF-based open-source observability and APM platform that auto-builds service maps, runs predefined performance inspections, and integrates continuous profiling; useful when manual instrumentation is sparse and a Kubernetes service map is needed quickly.
- `pixie` provides Kubernetes-native eBPF auto-instrumentation with zero code changes, covering metrics, traces, and logs at the pod level; part of the CNCF ecosystem.
- `signoz` is an open-source, OTEL-native alternative to Datadog and New Relic; unified logs, metrics, and traces with dashboards and alerting on a self-hosted stack built on ClickHouse.
- `uptrace` is an open-source APM built natively on OpenTelemetry and ClickHouse; strong for high-volume trace and metric ingestion with predictable self-hosted costs.
- `jaeger` is a CNCF-graduated distributed tracing backend originally from Uber; mature OTEL integration and a proven choice for teams already on the CNCF stack.
- `zipkin` is a simpler distributed tracing alternative to Jaeger; lower operational complexity for lightweight deployments.
- `k6` recreates the workload shape and validates whether the bottleneck appears under sustained or peak load; scriptable in JavaScript with native Kubernetes operator support.
- `vegeta` is a Go-based constant-rate HTTP load tester; preferred when you need to hold a precise request rate and measure latency distribution without rate auto-scaling.
- `artillery` supports HTTP, WebSocket, gRPC, and GraphQL; scenario-based and suited for multi-step user flows with YAML-first configuration.
- `gatling` is Scala/Java-based with high throughput simulation and detailed HTML reporting; preferred for enterprise load testing or when Java/JVM ecosystem integration is required.
- `oha` is a modern HTTP benchmarking tool with a real-time TUI; fast to invoke for quick latency baseline checks without scripting overhead.
- `bombardier` is a Go-based HTTP benchmarking tool; simpler than k6 for quick concurrency sweeps and connection saturation checks.
- `sentry`, `datadog`, and `newrelic` are useful when managed runtime debugging or release-aware telemetry is already present.
- `search_query` and `reference/trace` are fallback-only when live evidence is missing.

## Tool Path

- Start with `repository, logs`.
- If request latency or dependency timing is unclear, add `opentelemetry`, `grafana_tempo`, and `grafana_prometheus`; use `signoz` or `uptrace` if the stack is self-hosted and OTEL-native; use `jaeger` if the team is already on the CNCF tracing stack.
- If the problem looks CPU-, memory-, or allocation-bound, use `grafana_pyroscope` before speculating from code; use `parca` for eBPF-based continuous profiling of compiled languages with minimal overhead.
- If the service runs on the JVM, prefer `async_profiler` over safepoint-biased profilers for CPU, allocation, and lock contention.
- If the service is Node.js and event loop blocking or async I/O is suspect, use `clinic_js`.
- If system-level I/O, scheduling, or kernel calls are involved, use `bpftrace` or `perf`.
- If flame graph time-series patterns matter (intermittent spikes, periodic pauses), use `flamescope`.
- If the stack runs on Kubernetes and instrumentation is sparse, use `coroot` or `pixie` for eBPF auto-discovery and service mapping.
- If the issue only appears under pressure, use `k6` or the existing benchmark harness to reproduce the traffic shape; use `vegeta` for constant-rate validation; use `artillery` or `gatling` for scenario-based or multi-protocol flows; use `oha` or `bombardier` for quick latency sweeps.
- If production monitoring is already instrumented in a vendor tool, use `sentry`, `datadog`, or `newrelic` to confirm the runtime story.
- If only static artifacts exist, use `search_query` and `reference/trace`.
- If all primary paths fail, produce the best-guess output described as: A performance investigation with the leading bottleneck, evidence, and next highest-leverage validation.
- Label the section as `sourced`, `fallback`, or `inferred` to match the path used.

## Coverage Map

Record coverage explicitly for each deliverable:

- **Deeply analyzed**: surfaces where multiple signals were cross-referenced (e.g., traces confirmed by metrics and profiler output).
- **Partially analyzed**: surfaces examined with one signal only, or where data gaps required inference.
- **Not analyzed**: surfaces in scope that had no available evidence (telemetry missing, not instrumented, environment unreachable).

A finding that depends entirely on a not-analyzed surface must be labeled as speculative. Coverage gaps must be named, not silenced.

## Workflow Notes

- Build the model first, then test the weakest assumption first.
- Prefer direct evidence over extrapolation; keep facts and inference separate.
- Use load tests to recreate saturation, not to invent a bottleneck.
- Treat profiles, traces, and metrics as complementary signals; combine them when a single source is ambiguous.
- Preserve exact values for rates, durations, queue depth, CPU, memory, and error counts.
- If the bottleneck cannot be proven, state the best-supported hypothesis and the next validation step.


## Limits and Unknowns

- Repository-only analysis can suggest likely hotspots, but it cannot prove runtime behavior.
- Telemetry gaps, missing tags, or unsampled paths lower confidence and should be called out.
- Synthetic or lab load is only comparable to production when the workload shape matches closely.
- Cross-region, cross-cluster, and auth-state differences must be labeled if they are assumed.
- eBPF-based tools (Parca, Coroot, Pixie) require kernel version compatibility and appropriate Linux capabilities; validate before assuming availability in a given environment.
- Continuous profiling adds minimal overhead (<1% for eBPF-based tools) but must be validated against production security and compliance policies before deployment.
- Any unresolved uncertainty should stay visible rather than being folded into a false pass.
