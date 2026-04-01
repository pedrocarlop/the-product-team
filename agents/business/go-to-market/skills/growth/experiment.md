---
name: experiment
description: Design, size, and evaluate growth experiments with clear hypotheses, guardrails, and a decision rule before launch.
---

# Experiment

## Purpose

Use this skill to turn a growth idea into a testable experiment with a pre-registered hypothesis, a clear metric target, and a trustworthy readout.

## When to Use

- When the team wants to validate a change against a specific funnel metric
- When the work needs sample size, power, or significance planning
- When a result must be read and explained without post-hoc metric fishing

## When Not to Use

- When the main question is what is broken in the funnel
- When the task is primarily instrumentation, dashboarding, or tracking validation
- When the change is already proven and the work is rollout or operationalization

## Required Inputs

- The hypothesis and expected mechanism of change
- The primary metric and any guardrail metrics
- Baseline conversion or rate data
- Available traffic, audience size, or sample frame
- Constraints on timing, eligibility, or rollout

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: go-to-market
project: <slug>
deliverable: go-to-market.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. State the hypothesis in a testable format with one expected outcome.
2. Choose one primary metric and a small number of guardrails.
3. Estimate sample size and duration using baseline rate, minimum detectable effect, and desired confidence.
4. Define assignment, eligibility, and exposure rules before launch.
5. Write the decision rule for win, lose, or inconclusive outcomes.
6. After the test ends, interpret results against the pre-set criteria and segment where needed.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Pre-register the hypothesis and success criteria
- Optimize for learning quality, not just statistical significance
- Keep the metric set small and tied to the hypothesis
- Avoid hidden bias in assignment or exposure
- Treat null and negative results as useful outcomes

## Output Contract

- The hypothesis statement
- Primary and guardrail metrics
- Sample size and expected runtime
- Launch criteria and decision rule
- Result interpretation or recommended next step

## Examples

### Example 1

Input:
- Idea: Add social proof to the pricing page
- Baseline: 4.2% trial start rate
- Audience: 25,000 weekly visitors

Expected output:
- Hypothesis: We believe adding social proof will increase trial starts by 10% because it reduces pricing anxiety
- Metrics: Primary = trial start rate, guardrails = page load time and checkout abandonment
- Decision rule: Ship only if the primary metric lifts at the pre-set confidence threshold without guardrail harm

## Guardrails

- Do not launch without a pre-defined primary metric
- Do not change the evaluation criteria after results are visible
- Do not run underpowered tests and call them winners
- Do not optimize a proxy metric that is unrelated to the intended growth lever

## Optional Tools / Resources

- Statsig or equivalent experiment platform
- Amplitude, Mixpanel, or SQL baseline data
- Google Sheets for sample-size and scenario planning
- Notion for hypothesis and readout documentation

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Mixpanel Blog (mixpanel.com)](https://mixpanel.com/blog/), [Andrew Chen Essays (andrewchen.com)](https://andrewchen.com/)
