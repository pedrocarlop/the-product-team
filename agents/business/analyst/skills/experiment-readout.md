---
name: experiment-readout
description: Interpret an experiment and translate the result into a decision using statistical rigor and business context.
trigger: When an experiment has completed or reached sufficient sample size and requires a structured decision-ready summary.
best_guess_output: A statistical readout including primary metric lift, guardrail impact, confidence assessment, and a clear "go/no-go" recommendation.
output_artifacts: knowledge/analyst-experiment-readout.md
done_when: The readout provides a clear recommendation based on pre-committed success criteria, with all validity checks passed.
tool_stack:
  runtime:
    primary: [Statsig, Eppo, GrowthBook, Amplitude Experiment]
    secondary: [Mixpanel, Looker, Jupyter]
  artifacts:
    primary: [repository, notion]
---

# Experiment Readout

## 1. Purpose
This skill encodes the process of interpreting experimental data to make stable product decisions. It applies statistical reasoning (NHST, Bayesian inference) to distinguish signal from noise and maps technical outcomes to business value.
- **Reasoning**: Statistical evaluation, causal inference, and decision modeling.
- **Does NOT do**: Designing the experiment (see `experiment-design`), calculating raw SQL metrics (unless part of an exploratory deep-dive).

## 2. Required Inputs and Assumptions
- **Experiment Specs**: Hypothesis, primary metric, target population, and pre-committed target lift.
- **Data Source**: Access to experiment results (via Statsig, Eppo, or raw warehouse).
- **Assumptions**: The experiment was configured correctly (randomization works) unless SRM is detected. If inputs are missing, they must be inferred from the artifact history and labeled as `[ASSUMPTION]`.

## 3. Input Mode and Evidence Path
- **Path 1 (Primary)**: Extract results directly from the experimentation platform (Statsig, Eppo, GrowthBook).
- **Path 2 (Secondary)**: Query data warehouse (Snowflake, BigQuery) for custom metrics or segmentation.
- **Path 3 (Fallback)**: Refer to static design artifacts or previous readout drafts.
- **Declared limitations**: Reliance on platform-calculated metrics may hide logging issues if SRM isn't checked manually.

## 4. Tool Stack (Capabilities)
- **runtime**:
    - **primary**: [Statsig, Eppo, GrowthBook, Amplitude Experiment]
    - **secondary**: [Mixpanel, Looker, Jupyter]
- **artifacts**:
    - **primary**: [repository, notion]

## 5. Tool Routing (Decision System)
- **if**: Experimentation platform (Statsig/Eppo) is accessible -> **use**: [primary runtime tools] for automated readout and SRM detection.
- **if**: Custom segmentation or deep-dive is required -> **use**: [secondary runtime tools] (Jupyter/Looker).
- **if**: Only static logs or design docs exist -> **use**: [artifact tools] to infer results based on documented success criteria.

## 6. Environment and Reproducibility
- **State**: Capture the Experiment ID, Date Range, and Sample Size.
- **Version**: Note the platform version (e.g., Statsig API v2) and the build/dataset version.
- **Reproducibility**: Any other analyst should be able to reach the same conclusion using the same filter set (e.g., "Exclude internal employees").

## 7. Model Building (Before Analysis)
Construct a **Test Integrity Model**:
- **Variant Mapping**: Identify Control vs Treatment groups and their specific configurations.
- **Metric Hierarchy**:
    - **North Star**: Long-term goal (e.g., LTV).
    - **Primary Metric**: Short-term proxy for the hypothesis.
    - **Secondary/Guardrail Metrics**: Metrics that must not degrade (e.g., Latency, Cancellation Rate).
- **Population Segments**: Identify key cohorts (New vs Existing, Mobile vs Web).

## 8. Core Method Execution
1.  **Validity Check (SRM)**: Calculate Sample Ratio Mismatch. If the observed split deviates from expected with p < 0.001, halt analysis and investigate logging.
2.  **Primary Metric Evaluation**:
    - Determine **Point Estimate** (Lift %) and **95% Confidence Interval**.
    - Check if the lower bound of the CI is above the **Minimum Detectable Effect (MDE)**.
    - Distinguish between **Statistical Significance** (is there signal?) and **Practical Significance** (is the lift big enough to care?).
3.  **Guardrail Monitoring**: Verify all guardrail metrics are within "safe zones" (no significant degradation).
4.  **Heterogeneous Treatment Effects**: Analyze segments. Did the feature fail for a specific region or device type?
5.  **Learning Library Check**: Compare results against historical experiments in the central library to identify recurring patterns.

## 9. Structured Findings
- **Metric Observation**:
  - `Metric`: [Name]
  - `Evidence`: [Lift %], [95% CI], [Target Lift]
  - `Interpretation`: [Success / Neutral / Failure]
- **Validity Status**:
  - `SRM Result`: [Pass/Fail]
  - `Confidence`: [High / Medium / Low]
  - `Confounders`: [e.g., Holiday period, overlapping marketing campaign]

## 10. Prioritization Logic
- **Critical**: Primary metric failure OR guardrail degradation.
- **High**: Statistically and practically significant lift on primary metric.
- **Medium**: Statistically significant but practically insignificant lift.
- **Low**: Shifts in non-critical secondary metrics.

## 11. Pattern Detection
- **Novelty Effect**: Check day-by-day lift; if it decays sharply after Day 3, it may be a novelty effect.
- **Selection Bias**: If the experiment is only tracking "Logged-in users," detect potential bias against new users.

## 12. Recommendations
- **Decision**: [ROLL OUT / KILL / ITERATE]
- **DirectionAL Advice**: Link clearly to the hypothesis. "The hypothesis was [Validated/Refuted] because [Evidence]."
- **Post-Rollout Plan**: Define monitoring plan for 100% rollout phase.

## 13. Coverage Map
- **Deeply Analyzed**: Primary metric, Performance Guardrails, Core Segments (Region, Platform).
- **Partially Analyzed**: Long-term retention (insufficient sample time).
- **Not Analyzed**: Data prior to the experiment start date.

## 14. Limits and Unknowns
- **Sample Bias**: Results may not generalize if skewed by a specific event (e.g., Black Friday).
- **Long-term Impact**: Cannibalization effects may take 30+ days to manifest.

## 15. Workflow Rules
- **Evidence over Opinion**: Do not "explain away" a negative result without data-backed proof of a bug.
- **Model Before Analysis**: Always build the Metric Hierarchy before looking at the dashboard.
- **Merge Duplicates**: Consolidate similar findings across multiple segments.


## 17. Done When
The readout enables a clear "Go/No-Go" decision, passes all statistical validity checks, and maps the experiment surface back to the original hypothesis.
