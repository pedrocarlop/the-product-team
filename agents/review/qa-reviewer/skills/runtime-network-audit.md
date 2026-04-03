---
name: runtime-network-audit
description: Audit runtime behavior by building a flow-and-dependency model first, then tracing requests, failures, degraded states, and observability gaps across the strongest available runtime evidence path.
trigger: When release confidence, incident triage, or QA sign-off depends on real runtime and network evidence rather than static reasoning.
analysis_framework: runtime flow audit across traversal, request dependency chains, anomaly confirmation, and observability quality
primary_mcp: chrome_devtools
fallback_tools:
  - repository
  - reference/trace
required_inputs:
  - target environment, URL, or flow under audit
  - auth, data, and feature-flag assumptions
  - expected happy path or success criteria
  - known incident symptoms or hypotheses when available
  - build, version, or release context when known
recommended_passes:
  - environment and state setup
  - flow traversal
  - request and dependency mapping
  - failure and anomaly confirmation
  - observability gap analysis
tool_stack:
  runtime:
    primary: [chrome_devtools]
    secondary: [logs, playwright]
  artifacts:
    primary: [repository, reference/trace]
  fallback:
    primary: [repository, reference/trace]
tool_routing:
  - if: live runtime is available and inspectable
    use: [chrome_devtools]
  - if: multi-step traversal, retries, or asynchronous state transitions must be reproduced
    use: [chrome_devtools, playwright]
  - if: request intent or dependency ownership needs code or configuration context
    use: [repository]
  - if: runtime is unavailable and only traces, linked evidence, or review artifacts exist
    use: [reference/trace]
best_guess_output: A runtime and network audit with evidence-tagged failures, dependency context, and observability gaps.
output_artifacts: logs/active/<project-slug>/reviews/qa-reviewer.md
done_when: The main runtime issues are identified with reproducible evidence, request context, dependency mapping, and explicit limits on what could not be observed directly.
---

# Runtime Network Audit

## Purpose

Audit runtime behavior by modeling the flow, request graph, and dependency chain before drawing conclusions about failures or release risk.

This skill applies runtime QA reasoning across observable behavior, network sequencing, system dependencies, and observability quality.

This skill does not replace deep backend root-cause analysis, long-horizon performance profiling, or production monitoring ownership.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/qa-reviewer-runtime-network-audit.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: runtime-network-audit`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.
- `### Review framing`: Define the environment, target flow, audit goal, and runtime conditions being inspected.
- `### Required inputs and assumptions`: State the known auth, data, feature-flag, and expected-behavior assumptions, plus any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live runtime interaction, structured traces and runtime inspection, repository and artifact inspection, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record browser, operating system, viewport, network conditions, auth state, data setup, build version, and any parity gaps when known.
- `### Runtime scope and environment`: Record device assumptions, auth state, data state, feature flags, network conditions, and setup required for reproduction.
- `### Runtime flow and dependency model`: Build the model first by documenting the user or system flow, key transitions, request sequence, downstream dependencies, and expected success conditions before evaluating anomalies.
- `### Runtime flow map`: Summarize the main user or system flows executed during the audit and the key transition points inspected.
- `### Audit passes`: List the passes used such as environment and state setup, flow traversal, request and dependency mapping, failure and anomaly confirmation, and observability gap analysis.
- `### Runtime findings`: Record findings using the required finding schema below.
- `### Request and dependency graph`: Capture important requests, downstream services, retries, sequencing, and coupling relationships.
- `### Failures and anomalies`: Separate confirmed breakage, degraded behavior, suspicious traces, and unresolved runtime signals.
- `### Confirmed failures and anomalies`: Separate confirmed breakage from suspicious but unresolved signals.
- `### Reproduction evidence`: Provide the exact steps, request context, and artifacts needed to reproduce each confirmed runtime issue.
- `### Observability gaps`: Note missing logs, opaque errors, hidden retries, weak correlation IDs, or unclear ownership boundaries that blocked confident diagnosis.
- `### Priority risks`: Highlight the runtime issues with the highest user, operational, or release impact.
- `### Systemic runtime patterns`: Group repeated failure modes such as cache incoherence, timeout chains, auth drift, or brittle retry logic.
- `### Coverage map`: State what was deeply audited, partially audited, and not audited.
- `### Recommendations`: Link next actions to findings without pretending the full root cause is already proven.
- `### Limits and unknowns`: Explain what could not be observed directly or reproduced reliably.

For each finding inside `### Runtime findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps:
- Request or dependency context:
- Failure type:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the strongest runtime evidence path available: live runtime interaction -> structured traces and runtime inspection -> repository and artifact inspection -> inference.
- Start with `chrome_devtools` when a live browser-visible runtime exists.
- Use `chrome_devtools` for network sequencing, request inspection, console evidence, state transitions, timing, storage state, and browser-visible runtime failures.
- Use `playwright` when the audit depends on reliable multi-step traversal, repeated runs, or reproducible asynchronous behavior.
- Use `repository` to map requests to code owners, feature flags, configuration, and expected dependency behavior.
- Use `reference/trace` when the strongest remaining evidence is a stored trace, prior audit artifact, or linked runtime record.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `repository, reference/trace`.
- If both paths fail, produce the best-guess output described as: A runtime and network audit with evidence-tagged failures, dependency context, and observability gaps.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-path audit.

## Workflow Notes

- Audit by flow first and by request second so the network evidence stays tied to user-visible behavior.
- Treat `required_inputs` as real prerequisites. If the expected happy path, auth state, or feature-flag assumptions are missing, infer a provisional set, prefix each inferred item with `Assumed runtime context:`, and lower confidence for findings that depend on it.
- Build the runtime flow and dependency model before analysis. Do not jump from a failing request straight to a release-level conclusion.
- Capture dependency chains, not just isolated failing requests. Many runtime issues are emergent behaviors across retries, sequencing, or shared state.
- Separate confirmed failures from anomalies. Suspicious traces that cannot be reproduced or correlated should remain explicitly unresolved.
- Treat missing observability as a real QA finding when it blocks reliable diagnosis or release confidence.
- Run the passes in sequence so the audit stays grounded: setup first, traversal second, request mapping third, anomaly confirmation fourth, and observability analysis last.
- After all passes, consolidate overlapping failures into systemic patterns before prioritization.
- Distinguish clearly between observed evidence, inferred cause area, and recommendation direction.

