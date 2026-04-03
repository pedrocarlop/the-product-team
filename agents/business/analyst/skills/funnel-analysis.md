---
name: funnel-analysis
description: Encode the expert process for analyzing multi-stage user journeys to identify friction, drop-offs, and behavioral patterns using modern analytics stacks.
trigger: When funnel conversion or progression performance is underperforming or requires optimization.
best_guess_output: A detailed breakdown of funnel bottlenecks with cohort analysis and prioritized optimization hypotheses.
output_artifacts: logs/active/<project-slug>/deliverables/analyst-funnel-analysis.md
done_when: The team has a prioritized list of funnel friction points supported by evidence and actionable next steps.
---

# Funnel Analysis

## 1. Purpose
Analyze user progression through defined stages to locate major drop-offs, diagnose causes using behavioral and qualitative data, and recommend high-leverage optimizations. This skill focuses on conversion optimization and friction reduction across the customer lifecycle (Awareness to Referral).

## 2. Required Inputs and Assumptions
- **Required Inputs:**
    - Funnel stage definitions (events/milestones).
    - Conversion data (volumes and rates).
    - User cohort definitions (e.g., source, device, user type).
- **Assumptions:**
    - Event tracking is reasonably accurate and consistent.
    - Data represents a statistically significant sample size unless otherwise noted.

## 3. Input Mode and Evidence Path
The agent gathers evidence using the following hierarchy:
1. **Live Analytics Access:** Direct queries to Amplitude, Mixpanel, or SQL databases for quantitative data.
2. **Session Replay Analysis:** Contentsquare or Hotjar for qualitative friction evidence.
3. **Internal Documentation:** Product specs or Notion pages defining the intended user flow.
4. **Static Reports:** Pre-existing dashboard screenshots or CSV exports.
5. **Inference:** Based on general UX best practices (labeled clearly as assumptions).

## 4. Tool Stack
```yaml
tool_stack:
  runtime:
    primary: [Amplitude, Mixpanel, SQL]
    secondary: [Contentsquare, Hotjar, Google Analytics 4]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, reference/trace]
```

## 5. Tool Routing
- If raw database access is available (Snowflake/BigQuery), use **SQL** for complex cohort slicing.
- If product analytics tools are active, use **Amplitude/Mixpanel** for behavioral funnel visualization.
- If high friction is identified at a specific UI step, use **Contentsquare/Hotjar** for session replay diagnosis.
- If no live tools are available, use **search_query** to find benchmarks and **reference/trace** for repository artifacts.

## 6. Environment and Reproducibility
Every analysis must capture:
- **Date Range:** The temporal window of the data analyzed.
- **Platform:** Web, iOS, Android, or Cross-platform.
- **State:** Authenticated vs. Anonymous users.
- **Version:** Build number or Experiment branch.

## 7. Model Building (The ROI Funnel)
Before analysis, the agent must construct a 6-stage funnel model:
1. **Awareness:** Initial touchpoint or landing page visit.
2. **Acquisition:** Successful sign-up or lead capture.
3. **Activation:** User experiences the "Aha!" moment (core value action).
4. **Retention:** User returns for a second or subsequent session.
5. **Revenue:** Completion of a primary monetization event (e.g., checkout).
6. **Referral:** User invites others or shares the product.

## 8. Core Method Execution
The agent follows this expert diagnostic workflow:
1. **Funnel Mapping:** Align product-specific events to the 6-stage ROI model.
2. **Baseline Measurement:** Calculate step-to-step and overall conversion rates.
3. **Drop-off Identification:** Flag any step with a >20% relative drop-off as a primary bottleneck.
4. **Cohort Comparison:** Slice the funnel by segments (e.g., Device Type, Traffic Source, User Persona) to identify variance.
5. **Friction Diagnosis:** Review session replays or error logs at the identified bottleneck.
6. **Hypothesis Generation:** Formulate "If-Then" statements for optimization (e.g., "If we simplify the field count in Acquisition, then conversion will increase by X%").

## 9. Structured Findings
Findings must be recorded in this format:
- **Finding:** [Short, descriptive title]
- **Observation:** [Quantified behavior or drop-off]
- **Evidence:** [Data point, screenshot reference, or query ID]
- **Repro steps:** [Navigation path in the tool to see this data]
- **Cause:** [Technical bug, UX friction, or value proposition gap]
- **Impact:** [Estimated lost users or revenue impact]
- **Confidence:** [High/Medium/Low]

## 10. Prioritization Logic
- **Critical:** Drop-offs closest to the **Revenue** stage or impacting >40% of users.
- **High:** Significant friction in **Activation** for new users.
- **Medium:** Minor UX polish or secondary funnel optimizations.
- **Group:** Combine minor UI inconsistencies into a single "UX Consistency" theme.

## 11. Pattern Detection
Identify systemic issues across cohorts:
- "Mobile-only checkout failure."
- "Activation lag for users from Organic Search."
- "Global decline in Acquisition since last deployment."

## 12. Recommendations
- Must link directly to a specific Finding.
- Must be directional (e.g., "Reduce friction in Step X") rather than prescriptive.
- Categorize by effort: Quick Win, Strategic Initiative, or Technical Fix.

## 13. Coverage Map
State explicitly:
- **Deeply Analyzed:** Stages with full event coverage and cohort slicing.
- **Partially Analyzed:** Stages with missing some context or low sample size.
- **Not Analyzed:** Stages where no data was available.

## 14. Limits and Unknowns
- Declare "Dark Funnel" steps (untracked user actions).
- Note attribution windows (e.g., "7-day view-through conversion").
- Disclose any data sampling applied by the tool.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/analyst-funnel-analysis.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

## 16. Workflow Rules
- **Model first:** Build the ROI funnel model before calculating any conversion rates.
- **No Hallucination:** If a data point is missing, label it as "Unknown" or "Requires Validation."
- **Fact vs. Inference:** Clearly distinguish between "Observed Drop-off" (Fact) and "Likely Cause" (Inference).

