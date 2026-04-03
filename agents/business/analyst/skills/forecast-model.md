---
name: forecast-model
description: Generate evidence-based forecasts using time-series decomposition (Prophet), scenario planning (Monte Carlo), and driver-based modeling to support strategic decision-making.
trigger: When the user needs to project future volumes, revenue, adoption, or any time-bound metric based on historical patterns and explicit assumptions.
best_guess_output: A decision-ready forecast report containing centered projections, scenario ranges (P10/P50/P90), and sensitivity analysis of key drivers.
output_artifacts: logs/active/<project-slug>/deliverables/analyst-forecast-model.md
done_when: The forecast is reproducible, grounded in historical data, accounts for external signals, and provides actionable scenario-based insights.
tool_stack:
  runtime:
    primary: [BigQuery ML, Hex, Jupyter]
    secondary: [Prophet, statsmodels, scipy.stats]
  artifacts:
    primary: [notion]
  fallback:
    primary: [search_query]
tool_routing:
  - if: historical data is in BigQuery
    use: [BigQuery ML, Prophet]
  - if: complex scenario simulation or custom logic is required
    use: [Jupyter, scipy.stats]
  - if: quick visualization and documentation are needed
    use: [Hex]
---

## 1. Purpose
The `forecast-model` skill applies statistical forecasting and scenario simulation to translate historical data and business assumptions into future-facing projections. It encodes an expert workflow that prioritizes decomposition of trends from seasonality and noise, uses probabilistic modeling to handle uncertainty, and anchors findings to actionable business drivers. It explicitly avoids "single-point" guessing and does not provide financial legal advice.

## 2. Required Inputs and Assumptions
- **Historical Time-Series Data**: Minimum 2 full cycles of data to capture seasonality (e.g., 24 months for annual cycles).
- **Metric Definitions**: Explicitly defined North Star or secondary metrics (refer to `metric-definition` skill).
- **Driver Hypotheses**: Initial set of variables believed to influence the metric (e.g., CAC, LTV, Retention).
- **Explicit Assumptions**: Baseline growth rates, planned product launches, and known external constraints.
- **Rule**: If specific drivers are unknown, infer them from industry benchmarks and label clearly as "Inferred Assumptions".

## 3. Input Mode and Evidence Path
The agent follows this evidence hierarchy:
1. **Live System Data**: Direct SQL queries to BigQuery or Snowflake for raw metrics.
2. **Analytical Artifacts**: Reviewing existing Hex notebooks, Tableau dashboards, or Jupyter experiments.
3. **Strategy Documentation**: Extracting planned interventions from PRDs or Strategy docs.
4. **Market Research**: Using `search_query` for external benchmarks (e.g., "average retention for SaaS in 2026").
5. **Inference**: Mathematical extrapolation from sparse data points.

## 4. Tool Stack (Capabilities)
- **Time Series Decomposition**: `Prophet` for automated seasonality and holiday handling; `statsmodels` for ARIMA/SARIMAX.
- **Probabilistic Simulation**: `scipy.stats` and `numpy` for Monte Carlo simulations (P10/P50/P90).
- **Large-Scale Modeling**: `BigQuery ML` for rapid baseline forecasting on massive datasets.
- **Collaborative Analysis**: `Hex` or `Jupyter` for reproducible code and interactive visualization.

## 5. Tool Routing (Decision System)
- **if** data is structured in a warehouse **use** [BigQuery ML] for initial baseline.
- **if** the metric has strong seasonal/holiday components **use** [Prophet] via Hex/Jupyter.
- **if** modeling "what-if" scenarios with high variance **use** [Monte Carlo simulations].
- **if** documentation is the primary requirement **use** [Notion/Markdown].

## 6. Environment and Reproducibility
The output must document:
- **Dataset Version**: Snapshot timestamp or UTC range.
- **Model Params**: Hyperparameters (e.g., seasonality_prior_scale, changepoint_range).
- **Software State**: Library versions (e.g., Prophet v1.1.5, BigQuery ML API v2).
- **Random Seed**: Fixed seeds for any stochastic simulations to ensure identical results upon re-run.

## 7. Model Building (Before Analysis)
Before executing a forecast, the agent must construct a **Driver Model**:
1. **Mathematical Decomposition**: Map $Metric = f(Driver_1, Driver_2, ... Driver_n)$. (Example: $Revenue = Users * Conversion * AOV$).
2. **Structural Assumptions**: Define lag effects (e.g., "Marketing spend today affects users in T+14 days").
3. **Scenario Boundaries**: Set the bounds for 'Baseline' (status quo), 'Accelerated' (optimized), and 'Constrained' (pessimistic) inputs.

## 8. Core Method Execution
1. **Data Sanitization**: Detect and treat outliers (e.g., 0-value days, bot spikes) using IQR or Z-score methods.
2. **Baseline Forecast (P50)**: Run a time-series model (Prophet/ARIMA) on the sanitized historical data to project the most likely future path.
3. **Scenario Perturbation**:
   - **Monte Carlo Loop**: Randomly sample from driver distributions (e.g., Normal/Beta) 10,000+ times.
   - **Range Calculation**: Aggregate results into P10 (Downside), P50 (Expected), and P90 (Upside).
4. **Sensitivity Analysis**: Execute a "One-Factor-at-a-Time" (OFAT) test to rank drivers by their impact on the final outcome.
5. **Validation**: Backtest the model against the last 3 months of known data to calculate MAPE/RMSE.

## 9. Structured Findings
### Forecast Output
- **Projected Value**: [Value] at [Date].
- **Confidence Interval**: [P10 Value] to [P90 Value].
- **Growth Rate (YoY/MoM)**: [Percentage].

### Model Insights
- **Primary Driver**: [Driver Name] (Impact Score: [X.X]).
- **Seasonality Detect**: [e.g., "Strong weekly seasonality; peaks on Tuesdays"].
- **Changepoint Detect**: [e.g., "Significant trend shift identified on 2026-01-15"].

## 10. Prioritization Logic
- **High Severity**: Flag scenarios where the downside (P10) breaches critical thresholds (e.g., runway exhaustion, SLA violations).
- **Impact Ranking**: Focus recommendations on drivers with high sensitivity AND high controllability.

## 11. Pattern Detection
- **Diminishing Returns**: Detect if incremental driver increases (e.g., more spend) lead to plateauing outcomes.
- **Regime Shifts**: Identify if the underlying data generation process has changed (e.g., post-rebrand behavior vs. pre-rebrand).

## 12. Recommendations
- **Strategic Direction**: e.g., "Shift focus to Retention over Acquisition, as Retention has 3x higher sensitivity for 2027 Revenue."
- **Monitoring Triggers**: "If Weekly Active Users fall below [X], the current forecast is invalidated; trigger re-modeling."

## 13. Coverage Map
- **Deep Analysis**: [Metrics/Segments analyzed with full decomposition].
- **Partial Analysis**: [Metrics with sparse data/only linear extrapolation].
- **Exclusions**: [External factors not modeled (e.g., specific competitor pricing)].

## 14. Limits and Unknowns
- **Black Swan Risks**: Limitations in modeling unexpected external shocks.
- **Sparse Data**: Low confidence in segments with < 6 months of history.
- **Integration Gaps**: Specific tools or data silos not accessible during analysis.

## 15. Workflow Rules
- **Model Before Analysis**: Never run a forecast without a defined driver model.
- **Probabilistic over Deterministic**: Always provide ranges (P10-P90), never just one number.
- **Grounding**: Every assumption must be linked to a specific piece of evidence or labeled as "Working Hypothesis".

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/analyst-forecast-model.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.

