---
name: experiment-brief
description: Define a product experiment using Hypothesis-Driven Development and Pre-Registration of Decision Rules.
trigger: When the team wants to validate an idea before full commitment.
best_guess_output: An experiment brief with metrics, decision rules, and model-based rationale.
output_artifacts: knowledge/product-lead-experiment-brief.md
done_when: The experiment can be run and judged without inventing criteria later.
---

# Experiment Brief

## 1. Purpose
Define a product experiment with hypothesis, metrics, scope, and decision rules. This skill applies **Hypothesis-Driven Development** (HDD) to ensure experiments are grounded in clear product logic and **Pre-Registration of Decision Rules** to avoid post-hoc rationalization. It does NOT perform the actual data analysis (see `analyst/experiment-readout`).

## 2. Required Inputs and Assumptions
- **Required inputs**: Problem statement, proposed solution, goal metric.
- **Known vs unknown**: Current baseline performance, implementation constraints.
- **Assumptions**: If missing, infer the "Experiment Logic Model" (e.g., "If we change X, users will do Y because Z") and label clearly as an assumption.

## 3. Input Mode and Evidence Path
1. **Live / real interaction**: Reviewing current product behavior and funnel performance.
2. **Design artifacts**: Reviewing PRDs or Loom videos of the proposed change.
3. **Structured system access**: Amplitude dashboards or Statsig feature configurations.
4. **Inference**: Based on general product management best practices for similar features.

## 4. Tool Stack (Capabilities)
tool_stack:
  runtime:
    primary: [notion, linear]
    secondary: [amplitude, statsig, braintrust]
  artifacts:
    primary: [github]
  fallback:
    primary: [analyst/experiment-readout, search_query]

## 5. Tool Routing (Decision System)
tool_routing:
  - if: behavioral signals or historical funnel data are needed
    use: [amplitude]
  - if: feature gating or automated rollout rules are being defined
    use: [statsig]
  - if: AI model performance or evaluation is part of the treatment
    use: [braintrust]
  - if: tracking experiment status or tasks
    use: [linear, notion]

## 6. Environment and Reproducibility
- **Platform**: Specify Web, iOS, Android, or Cross-platform.
- **Environment**: Staging, Production (Canary), or Production (A/B).
- **Tool Version**: Note the specific project or build version if applicable.

## 7. Model Building (Before Analysis)
The agent must construct an **Experiment Logic Model** before defining success criteria:
- **Product Funnel Baseline**: Map the current user flow and identify where the "friction" or "opportunity" exists.
- **Treatment Logic**: Diagram how the proposed change modifies that flow.
- **Primary vs. Proxy Metrics**: Identify the ultimate goal (e.g., LTV) and the measurable proxy (e.g., Week 1 Retention).

## 8. Core Method Execution
1. **Pre-Registration of Decision Rules**: Define "Gamble's pre-registration standard" by stating:
   - "If Metric X > Y, then Scale (Winner)."
   - "If Metric X < Z, then Rollback (Loser)."
   - "If confidence interval overlaps 0, then Iterate or Kill."
2. **Hypothesis Construction**: Use the format "We believe [Business Change] for [User Segment] will result in [Outcome] as measured by [Primary Metric]."
3. **Sample Size Planning**: Use AI-assisted calculators (or Statsig's built-in power analysis) to estimate duration and required traffic.
4. **Instrumentation Audit**: Identify missing events in Amplitude/Statsig that must be implemented for a valid readout.

## 9. Structured Findings (Deliverable Sections)
The deliverable at `knowledge/product-lead-experiment-brief.md` must include:
- `### Hypothesis`: HDD-format statement.
- `### Experiment Logic Model`: Description of the funnel impact.
- `### Audience and Scope`: Segment definitions and surfacing rules.
- `### Primary Metric`: Name, definition, and target lift.
- `### Guardrails (Counter-metrics)`: Metrics that must not degrade (e.g., Latency, Cancellation Rate).
- `### Pre-Registered Decision Rules`: The stop/go criteria.
- `### Instrumentation Requirements`: Required events and properties for Amplitude/Statsig.
- `### Pattern Detection`: Note any potential "interference effects" or "cannibalization" risks.

## 10. Prioritization Logic
- **Primary Metric** is the single source of truth for the Go/No-Go decision.
- **Guardrail Violations** override a "Winning" primary metric (Automatic Kill).
- **Secondary Metrics** provide context but do not drive the scale decision.

## 11. Pattern Detection
- **Interference Effects**: When the treatment of one user affects the control of another (e.g., social features).
- **Cannibalization**: When the new feature merely shifts usage from an existing high-value feature.
- **Novelty Effect**: Detecting if initial spikes are due to change itself rather than long-term value.

## 12. Recommendations
- Link to specific findings in the Logic Model or Risk assessment.
- Directional advice on whether to proceed with low-conf results or pivot entirely.

## 13. Coverage Map
- **Deeply Analyzed**: Primary hypothesis, decision rules, primary metric definition.
- **Partially Analyzed**: Sample size estimates (depends on real-time traffic), secondary metrics.
- **Not Analyzed**: Statistical significance calculations (deferred to readout phase).

## 14. Limits and Unknowns (Mandatory)
- Implementation costs (requires Engineering input).
- External factors (market seasonality, competitor launches) that may affect the signal.
- Limits of the tracking plan (e.g., "Cannot track offline conversions").

## 15. Workflow Rules
- **Lossless Deliverable Contract**: Standard sections must be preserved.
- **Pre-commit**: Decision rules must be written before implementation starts.
- **No Hallucination**: Use actual historical p50/p90 values if Amplitude is accessible; otherwise, label as "Inferred Baseline."

## 16. Output Contract
- **Target File**: `knowledge/product-lead-experiment-brief.md`.
- **Do NOT modify**: Role-level READMEs or global skill lists.
- **Append**: Link to the Execution Manifest (`orchestrator.md`).
- **Include Reflection**: `## Reflection` section with `What worked`, `What didn't`, and `Next steps`.

## 17. Lossless Deliverable Contract
- Produce a standalone deliverable at the path specified in `output_artifacts`.
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest once complete.
