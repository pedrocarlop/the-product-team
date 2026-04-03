---
name: dashboard-story
description: Transform raw metrics and dashboard visualizations into a cohesive, narrative-driven business story using the Pyramid Principle and Goal-Signal-Metric frameworks.
trigger: When a dashboard exists (Tableau, Power BI, Looker, etc.) but the team requires a synthesis of what the numbers mean, why they changed, and what actions to take.
best_guess_output: A structured narrative readout leading with an executive takeaway, supported by trend analysis and recommended actions.
output_artifacts: logs/active/<project-slug>/deliverables/analyst-dashboard-story.md
done_when: The reader can understand the core performance story, the primary driver of change, and the specific next steps without needing to open the source dashboard.
tool_stack:
  runtime:
    primary: [tableau, powerbi, looker, thoughtspot]
    secondary: [metabase, superset, domo]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, screenshot_analysis]
tool_routing:
  - if: interactive BI tool is accessible
    use: [tableau, powerbi, looker, thoughtspot]
  - if: only static exports or screenshots exist
    use: [screenshot_analysis, vision_llm]
  - if: data is in open-source/internal tools
    use: [metabase, superset, domo]
---

# Dashboard Story

## 1. Purpose
This skill synthesizes complex dashboard data into a narrative that explains business performance. It applies deductive reasoning to move from "what happened" to "why it happened" and "what to do next." It explicitly does NOT perform deep-dive exploratory data analysis (EDA) or raw data cleaning.

## 2. Required Inputs and Assumptions
- **Required Inputs:**
  - Link to or screenshot of the primary dashboard (Tableau, Power BI, Looker, etc.).
  - Time range for comparison (e.g., WoW, MoM, YoY).
  - Business context or specific "North Star" metric goal.
- **Assumptions:**
  - The metrics on the dashboard are accurate and finalized.
  - If inputs are missing, the agent will infer them from the repository context and label them as assumptions.

## 3. Input Mode and Evidence Path
1. **Live Interaction:** Connect via browser to live BI tools to inspect interactive elements and tooltips.
2. **Structured System Access:** Querying underlying metadata or LookML models if available.
3. **Static Input:** Analyze image exports or screenshots of dashboard views using Vision LLM capabilities.
4. **Inference:** Extracting metric definitions and previous performance from `repository` documentation.

## 4. Tool Stack (Capabilities)
- **Primary Runtime:** ThoughtSpot (NLQ), Tableau (Smart Narratives), Power BI.
- **Secondary Runtime:** Looker (Semantic Layer), Domo (Real-time Dashboards).
- **Open Source/Internal:** Metabase, Apache Superset.
- **Artifacts:** Notion for document housing, Repository for metric definitions.

## 5. Tool Routing (Decision System)
- `if`: Cloud-hosted BI (Tableau/Looker) is available → `use`: Browser-based DOM/Element inspection.
- `if`: Only static images exist → `use`: vision-based screenshot analysis.
- `if`: Natural language querying is possible → `use`: ThoughtSpot integration.
- `if`: Business logic is defined in code → `use`: Looker/LookML repository access.

## 6. Environment and Reproducibility
- **State Capture:** Document all active filter configurations (e.g., "Segments: Enterprise", "Region: EMEA").
- **Timestamp:** Record the "last refreshed" data timestamp from the dashboard.
- **Build/Version:** Note the version of the dashboard or the specific dataset being viewed.

## 7. Model Building (Before Analysis)
Before evaluating, the agent must construct a **Narrative Hierarchy Model**:
- **Goal Layer:** What is the primary business outcome?
- **Signal Layer:** Which dashboard components (charts, tiles) serve as signals for that goal?
- **Relationship Map:** How does Metric A (e.g., Traffic) influence Metric B (e.g., Conversion)?
- **Baseline:** Establish the expected "normal" range for the metrics.

## 8. Core Method Execution
The workflow follows the **Pyramid Principle** and **SCR (Situation-Complication-Resolution)** framework:
1. **Scan and Filter:** Configure the dashboard to the requested view.
2. **Goal-Signal-Metric (GSM) Alignment:** Map dashboard tiles to business goals.
3. **Identify Complications:** Detect trend breaks, anomalies, or performance gaps.
4. **Synthesize the "Answer":** Lead with the core conclusion as the "Pyramid Peak."
5. **Support with Evidence:** Group supporting metrics into logical clusters (e.g., "Top of Funnel," "Efficiency," "Retention").

## 9. Structured Findings
Every observation must follow this schema:
- **Observation:** [Clear statement of the metric change]
- **Evidence:** [Reference specific dashboard tile or value]
- **Repro steps:** [Filters and steps to see this exact view]
- **Cause:** [Inferred or stated reason for the change]
- **Impact:** [Business consequence of this finding]
- **Confidence:** [1-5 scale based on data clarity]

## 10. Prioritization Logic
- **Level 1 (Critical):** Any deviation in North Star metrics >10% or trend reversals.
- **Level 2 (Major):** Statistically significant changes in secondary KPIs or segment-specific anomalies.
- **Level 3 (Minor):** General variance, "business as usual" fluctuations, or noise.

## 11. Pattern Detection
- **Metric Drag:** Identifying when one failing metric is weighing down the entire system.
- **Lagging Indicator Confirmation:** Confirming if current signals match predicted outcomes.
- **Systemic vs. Point Issue:** Determining if the story is about a single feature or a platform-wide shift.

## 12. Recommendations
- Must link directly to a Finding in the SCR framework.
- Recommendations should be directional: "Investigate [X]," "Double down on [Y]," or "Revert [Z]."
- Distinguish between "Immediate Mitigation" and "Long-term Strategy."

## 13. Coverage Map
- **Fully Analyzed:** List specific dashboard tabs or metrics reviewed in depth.
- **Partially Analyzed:** List areas where only a surface-level summary was possible.
- **Out of Scope:** Explicitly list metrics or dates ignored to maintain focus.

## 14. Limits and Unknowns
- **Missing Data:** Identify specific tiles that were broken or empty.
- **Attribution Gap:** State where correlation does not equal causation.
- **Latency:** Acknowledge data freshness limitations.

## 15. Workflow Rules
- **Pyramid First:** Always lead with the answer.
- **Context over Content:** Explain *why* a 5% drop matters, don't just state it.
- **Merge Noise:** Group multiple small, related variances into a single thematic finding.
- **Fact vs. Inference:** Clearly label interpretations that aren't explicitly visible in the data.


## 17. Required Deliverable Sections
Within the deliverable, include:
- `### 1. Executive Summary`: The one sentence the CEO needs to read.
- `### 2. Performance Story (GSM)`: How signals align to business goals.
- `### 3. Key Observations`: Using the Structured Findings schema.
- `### 4. Recommended Actions`: Concrete next steps tied to findings.
- `### 5. Watch List`: High-risk metrics for the next cycle.
