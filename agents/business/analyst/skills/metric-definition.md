---
name: metric-definition
description: Define and model business/product metrics using hierarchical (NSM) and categorical (HEART/AARRR) frameworks for 2026 modern data stacks.
trigger: When the team is debating success criteria, defining feature goals, or auditing performance measurement.
best_guess_output: A structured metric model including NSM/Input hierarchies, SQL/DBT logic, and instrumentation mapping (Amplitude/Mixpanel).
output_artifacts: logs/active/<project-slug>/deliverables/analyst-metric-definition.md
done_when: The metric model is mathematically sound, mapped to business value, and instrumentable in modern analytics tools.
---

## 1. Purpose
Define the business or product metric model so downstream analysis measures the right thing. This skill applies hierarchical reasoning (North Star -> Input Metrics) and expert frameworks (HEART, AARRR) to ensure that measurement is both holistic and actionable.

## 2. Required Inputs and Assumptions
### Required Inputs:
- Desired business outcome (e.g., "increase retention", "higher LTV").
- User flow, funnel description, or product feature specs.
- Current instrumentation status (if known).
### Assumptions:
- If the stack is unknown, assume a 2026 Modern Data Stack (Snowflake/BigQuery, DBT, Amplitude/Mixpanel, Statsig).
- If the business model is not specified, assume a SaaS/Product-Led Growth (PLG) context.

## 3. Input Mode and Evidence Path
- **Live / System Interaction:** Browsing `Amplitude`, `Mixpanel`, or `Posthog` dashboards (if accessible).
- **Design/Documentation:** Reading PRDs, Notion specs, or Figmas for intended user value.
- **Repository Metadata:** Analyzing `DBT` models, SQL schemas, or telemetry configuration files.
- **Inference:** Using industry-specific benchmarks for SaaS, E-commerce, or Fintech.

## 4. Tool Stack (Capabilities)
- **Runtime:**
  - `repository`: For analyzing data models and schema files.
  - `notion`: For aligning on business goals and requirements.
- **Modern Analytics (2026):**
  - `Amplitude` / `Mixpanel`: For event-based behavioral analysis.
  - `DBT` / `SQL`: For core metric logic modeling and warehouse-side transformations.
  - `Statsig`: For mapping metrics to A/B testing and experimentation.

## 5. Tool Routing (Decision System)
- **If repository is available:** Prioritize `models/` and `schema.yml` to understand existing data logic.
- **If product specs are available:** Prioritize `notion` or PR documents to derive the North Star Metric.
- **If telemetry is needed:** Navigate to search for event-tracking documentation or `analytics.js` configs.

## 6. Environment and Reproducibility
- **Stack Type:** 2026 Modern Data Stack.
- **State:** Explicitly state if the definition is based on existing implementation or is a proposed ideal.
- **Portability:** Use ANSI SQL for metric logic to ensure reproducibility across warehouses.

## 7. Model Building (Before Analysis)
Before defining a single metric, the agent must construct a **Metric Hierarchy Model**:
1. **North Star Metric (NSM):** Identify the single leading indicator of sustainable growth and long-term customer value.
2. **Input Metrics:** Identify the four core levers that drive the NSM:
   - **Breadth:** How many users are performing the action?
   - **Depth:** What is the level of engagement per user?
   - **Frequency:** How often does the user engage?
   - **Efficiency:** How friction-free is the conversion?
3. **Framework Mapping:** Align specific metrics to HEART (Happiness, Engagement, Adoption, Retention, Task Success) or AARRR (Acquisition, Activation, Retention, Referral, Revenue).

## 8. Core Method Execution
### Step 1: Framework Rooting
- For long-term growth -> **North Star**
- For user experience value -> **HEART**
- For funnel optimization -> **AARRR**

### Step 2: Formula Logic Definition
Specify the mathematical rigor:
- **Numerator/Denominator:** Explicitly state what counts (and what is excluded).
- **Time Windowing:** Standardize on Daily (DAU), Weekly (WAU), or Monthly (MAU).
- **Aggregation Logic:** Sum, Average, Median (P50), or Percentile (P90).

### Step 3: Instrumentation Mapping
Define where the data comes from:
- **Event-Driven:** Named events (e.g., `button_clicked`) for 2026 behavioral tools.
- **Batch-Driven:** Table joins for warehouse-side reporting (SQL/DBT).

## 9. Structured Findings
### Metric Definition Block Template:
- **Metric Name:** [e.g., L7 Retention Rate]
- **Framework:** [e.g., Retention - HEART]
- **Definition:** [One sentence purpose]
- **Logic:** `COUNT(DISTINCT user_id) WHERE last_event_at >= NOW() - 7 DAYS / Total Users`
- **Recommended Cuts:** [e.g., Platform, User Segment, Acquisition Channel]
- **Confidence Level:** [Low/Med/High based on existing instrumentation]

## 10. Prioritization Logic
- **Primary:** North Star and top-level Input metrics.
- **Guardrail Metrics:** Metrics that ensure optimization in one area (e.g., clicks) doesn't hurt another (e.g., churn).
- **Exploratory Metrics:** Diagnostic metrics for deep-dive analysis only.

## 11. Pattern Detection
Identify systemic measurement issues:
- **Metric Dilution:** Detecting the 'dashboard sprawl' where too many signals confuse the team.
- **Vanity Over-Indexing:** Flagging metrics like 'Total Registered Users' that don't reflect health.
- **Lagging Indicator Bias:** Warning when the team relies solely on revenue or churn (which are too late to act on).

## 12. Recommendations
- Propose specific instrumentation additions (e.g., "Add `page_visible` event for true session duration").
- Suggest dashboard configurations for Amplitude/Mixpanel.
- Recommend DBT schema changes to simplify reporting.

## 13. Coverage Map
- [ ] Core Growth / NSM
- [ ] Retention / Engagement
- [ ] Monetization / Efficiency

## 14. Limits and Unknowns
- Data quality risks (e.g., bot traffic, tracking blockers).
- Attribution window constraints.
- Privacy-related data gaps (e.g., lack of cross-device stitching).

## 15. Workflow Rules
- **Model first, formula second:** Never define a formula without its place in the NSM/Input hierarchy.
- **Fact vs. Inference:** Clearly label source-backed data vs. benchmark-based assumptions.
- **Traceability:** Maintain exact naming for source tables/events where they exist in the repo.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/analyst-metric-definition.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

