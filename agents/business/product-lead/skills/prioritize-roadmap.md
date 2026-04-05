---
name: prioritize-roadmap
description: Rank work against impact, effort, sequencing, and strategic fit using RICE 2.0 and Outcome-Based Roadmapping.
trigger: When multiple candidate bets compete for attention or quarterly planning is initiated.
best_guess_output: A ranked roadmap or priority decision with rationale grounded in strategic fit and resource constraints.
output_artifacts: knowledge/product-lead-prioritize-roadmap.md
done_when: The ordering is explicit, tradeoffs are documented, and North Star alignment is verified.
---

# Prioritize Roadmap

## 1. Purpose
Rank candidate product bets against impact, effort, sequencing, and strategic fit to ensure the team focus is on the highest-leverage work. It applies **Outcome-Based Roadmapping** and **RICE 2.0** reasoning.

## 2. Required Inputs and Assumptions
- **Candidate Bets**: A list of features, experiments, or infrastructure tasks.
- **Product Strategy**: Current North Star metrics and quarterly objectives.
- **Capacity Data**: Engineering and compute resources available.
- **Assumptions**: If specific reach or impact data is missing, the agent will infer based on historical patterns and label as "Analyst Inference".

## 3. Input Mode and Evidence Path
1. **Live Interaction**: Direct access to Jira Product Discovery or Airtable ProductCentral.
2. **Artifact Review**: Reading PRDs, experiment briefs, and stakeholder memos.
3. **Inference**: Using market benchmarks and previous performance when direct data is unavailable.

## 4. Tool Stack (Capabilities)
- **Primary (Strategic & Signal)**: `Jira Product Discovery` (signal-to-priority), `Airtable ProductCentral` (portfolio ops), `Craft.io` (strategic alignment).
- **Secondary (Execution)**: `Notion`, `Linear`.
- **Analytic Fallback**: `analyst/metric-definition`, `search_query`.

## 5. Tool Routing (Decision System)
- **If capturing market/user signals**: Use `Jira Product Discovery`.
- **If managing portfolio-level operations**: Use `Airtable ProductCentral`.
- **If aligning with top-down corporate strategy**: Use `Craft.io`.
- **If execution-level tracking is needed**: Use `Linear`.

## 6. Environment and Reproducibility
- State the planning horizon (e.g., Q3 2026).
- Document any tool-specific filters or views used (e.g., "Active Signal View" in Jira).
- Record the snapshot date of the backlog to ensure reproducibility.

## 7. Model Building (Before Analysis)
Before scoring, the agent must build:
- **Strategic Opportunity Map**: Visualizing how each bet maps to the North Star metric and secondary outcomes.
- **Resource Capacity Model**: Cross-referencing bets against Engineering bandwidth and "Compute/Latency" constraints (essential for AI-heavy roadmaps).

## 8. Core Method Execution
1. **Outcome Mapping**: Align each candidate bet with a specific desired outcome (not just a feature).
2. **Weighted Scorecard (RICE 2.0)**:
   - **Reach**: Number of users affected.
   - **Impact**: Contribution to the specific outcome.
   - **Confidence**: Data-backed certainty vs. intuition.
   - **Effort**: Engineering days.
   - **Compute/Latency Weighting**: Penalty for features that significantly increase inference costs or response times.
3. **Sensitivity Testing**: Vary the "Confidence" score to see if it changes the top-3 ranking, identifying "high-risk/high-reward" vs "safe bets".

## 9. Structured Findings
For every prioritized item:
- **Bet Name**: Name of the initiative.
- **RICE 2.0 Score**: Detailed breakdown of the score components.
- **Strategic Alignment**: How it fits the North Star.
- **Evidence**: Links to customer signals or research artifacts.

## 10. Prioritization Logic
- **Primary Driver**: Weighted RICE 2.0 score.
- **Tie-breaker**: Strategic alignment with the current quarterly "Bridge" objective.
- **Constraints**: Items exceeding 40% of compute budget are flagged for secondary review.

## 11. Pattern Detection
Identify:
- **Bottleneck Features**: A small feature that unblocks multiple high-impact bets.
- **High-Leverage Infrastructure**: Backend changes that improve RICE scores across an entire theme.
- **Thematic Bloat**: Too many small bets in one area with diminishing returns.

## 12. Recommendations
- **The "Final List"**: The recommended sequence of execution.
- **The "Cut Line"**: Items that are deferred and the rationale (e.g., "High impact but lacks confidence/compute budget").

## 13. Coverage Map
- **Areas Analyzed**: Core workflow, user onboarding, AI inference speed.
- **Areas Excluded**: Long-term R&D, maintenance-only requests.

## 14. Limits and Unknowns
- State where "Effort" estimates are placeholders.
- Identify "Confidence" gaps where further research is needed before committing resources.

## 15. Workflow Rules
- Build the **Strategic Opportunity Map** before scoring.
- Separate "Leadership Preference" from "Evidence-Based Score".
- Do not hallucinate capacity; if engineering bandwidth is unknown, state it as a limit.

## 16. Output Contract (Lossless Deliverable)
- Produce a standalone deliverable at `knowledge/product-lead-prioritize-roadmap.md`.
- Ensure rationale for every ranking change is preserved.
- Link this deliverable in `orchestrator.md`.
- Include a `## Reflection` section with `What worked`, `What didn't`, and `Next steps`.

## 17. Structured Sections in Deliverable
- `### Candidate bets`: Detailed view of options.
- `### Scoring or ranking table`: The RICE 2.0 output.
- `### Sequencing dependencies`: Prerequisites and coupling.
- `### Recommendation`: Final proposed order.
- `### Tradeoffs and deferrals`: What was left behind.
