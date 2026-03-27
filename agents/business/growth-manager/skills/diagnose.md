---
name: diagnose
description: Find the binding growth constraint by reading funnel data, cohort behavior, and segment-level patterns before recommending any move.
activation_hints:
  - "Use when growth is stalling and the team needs to identify the real bottleneck."
  - "Route here for funnel diagnosis, cohort analysis, retention drops, CAC shifts, or unexplained conversion changes."
  - "Do not use for experiment design, event tracking implementation, or rollout planning."
---

# Diagnose

## Purpose

Use this skill to identify the current growth bottleneck, explain why it is binding, and separate signal from noise before the team invests in a fix.

## When to Use

- When a funnel stage is underperforming and the team needs to know where to look first
- When conversion, retention, or revenue moved and the cause is unclear
- When the team needs a quantified problem statement before experiments or scaling work

## When Not to Use

- When the bottleneck is already known and the work is to test a solution
- When the task is primarily setting up events, dashboards, or tracking specs
- When the problem is operational rollout rather than root-cause analysis

## Required Inputs

- The metric or funnel stage that is failing
- The time window where the change appeared
- Available data sources such as Amplitude, Mixpanel, SQL, HubSpot, or ad platform data
- Relevant segments such as channel, plan, cohort, device, geography, or lifecycle stage
- Any prior hypotheses, recent launches, or market events that could affect interpretation

## Workflow

1. Define the exact metric, stage, and time window under investigation.
2. Pull the relevant funnel or cohort data and compare against the prior baseline.
3. Segment the data until the likely driver becomes visible, rather than relying on aggregate averages.
4. Check whether the issue is acquisition quality, activation drop-off, retention decay, or monetization friction.
5. State the binding constraint in plain language with the supporting evidence.
6. Separate likely causes from correlations, and note where more data is needed before acting.

## Design Principles / Evaluation Criteria

- Quantify the bottleneck instead of naming a generic symptom
- Prefer segment-level evidence over averages
- Use the smallest explanation that accounts for the observed change
- Distinguish root cause from downstream consequence
- Keep the output actionable for experiment or instrumentation follow-up

## Output Contract

- The identified bottleneck and why it is binding
- The supporting metric evidence and time window
- The most relevant segments or cohorts
- A short list of plausible causes ranked by confidence
- Any data gaps that block a stronger conclusion

## Examples

### Example 1

Input:
- Metric: Trial-to-paid conversion
- Context: Conversion dropped after a new onboarding launch
- Data: Amplitude funnel by cohort and device

Expected output:
- Bottleneck: Mobile trial users are dropping at the pricing step at a much higher rate than desktop users
- Evidence: Desktop conversion is flat, mobile conversion fell 18% week over week, and the launch changed the price-screen layout on mobile only
- Next step: Test whether the new layout is causing confusion before changing pricing or targeting

## Guardrails

- Do not recommend a solution before identifying the bottleneck
- Do not rely on aggregate numbers if a segment break could change the conclusion
- Do not invent data that is not present in the source systems
- Do not confuse correlation with causation

## Optional Tools / Resources

- Amplitude or Mixpanel funnel and cohort reports
- SQL queries over event and revenue tables
- HubSpot or CRM source data
- Notion notes on prior experiments or launches

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Mixpanel Blog (mixpanel.com)](https://mixpanel.com/blog/), [Andrew Chen Essays (andrewchen.com)](https://andrewchen.com/)
