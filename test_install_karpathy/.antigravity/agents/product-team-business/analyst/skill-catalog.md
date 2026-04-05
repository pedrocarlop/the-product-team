# Analyst Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `dashboard-story`

- Description: Transform raw metrics and dashboard visualizations into a cohesive, narrative-driven business story using the Pyramid Principle and Goal-Signal-Metric frameworks.
- Trigger: When a dashboard exists (Tableau, Power BI, Looker, etc.) but the team requires a synthesis of what the numbers mean, why they changed, and what actions to take.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A structured narrative readout leading with an executive takeaway, supported by trend analysis and recommended actions.
- Output: knowledge/analyst-dashboard-story.md
- Done when: The reader can understand the core performance story, the primary driver of change, and the specific next steps without needing to open the source dashboard.

## `experiment-readout`

- Description: Interpret an experiment and translate the result into a decision using statistical rigor and business context.
- Trigger: When an experiment has completed or reached sufficient sample size and requires a structured decision-ready summary.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A statistical readout including primary metric lift, guardrail impact, confidence assessment, and a clear "go/no-go" recommendation.
- Output: knowledge/analyst-experiment-readout.md
- Done when: The readout provides a clear recommendation based on pre-committed success criteria, with all validity checks passed.

## `forecast-model`

- Description: Generate evidence-based forecasts using time-series decomposition (Prophet), scenario planning (Monte Carlo), and driver-based modeling to support strategic decision-making.
- Trigger: When the user needs to project future volumes, revenue, adoption, or any time-bound metric based on historical patterns and explicit assumptions.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A decision-ready forecast report containing centered projections, scenario ranges (P10/P50/P90), and sensitivity analysis of key drivers.
- Output: knowledge/analyst-forecast-model.md
- Done when: The forecast is reproducible, grounded in historical data, accounts for external signals, and provides actionable scenario-based insights.

## `funnel-analysis`

- Description: Encode the expert process for analyzing multi-stage user journeys to identify friction, drop-offs, and behavioral patterns using modern analytics stacks.
- Trigger: When funnel conversion or progression performance is underperforming or requires optimization.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A detailed breakdown of funnel bottlenecks with cohort analysis and prioritized optimization hypotheses.
- Output: knowledge/analyst-funnel-analysis.md
- Done when: The team has a prioritized list of funnel friction points supported by evidence and actionable next steps.

## `metric-definition`

- Description: Define and model business/product metrics using hierarchical (NSM) and categorical (HEART/AARRR) frameworks for 2026 modern data stacks.
- Trigger: When the team is debating success criteria, defining feature goals, or auditing performance measurement.
- Primary MCP/tool: Missing primary_mcp.
- Fallback: Missing fallback_tools.
- Best guess: A structured metric model including NSM/Input hierarchies, SQL/DBT logic, and instrumentation mapping (Amplitude/Mixpanel).
- Output: knowledge/analyst-metric-definition.md
- Done when: The metric model is mathematically sound, mapped to business value, and instrumentable in modern analytics tools.
