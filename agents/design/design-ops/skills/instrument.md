---
name: instrument
description: Define, audit, and verify the metrics and signals that let design operations measure process health and service quality.
activation_hints:
  - "Use when design ops needs visibility into throughput, latency, adoption, or quality."
  - "Route here for metrics definitions, dashboards, service levels, or reporting gaps."
  - "Do not use for process design unless measurement is the blocker."
---

# Instrument

## Purpose

Use this skill to make design operations measurable enough that the team can spot bottlenecks, prove impact, and see whether a process is actually working.

## When to Use

- When a workflow needs a metric before it can be improved
- When a dashboard is missing key signals or is tracking the wrong ones
- When the team needs to audit whether a service level, queue, or process is trustworthy

## When Not to Use

- When the main problem is unclear ownership or broken process steps
- When the data exists but the issue is mostly scheduling or coordination
- When the metric cannot be acted on by the people who receive it

## Required Inputs

- The decision or operational question the metric must support
- The process, queue, or service being measured
- Existing data sources, definitions, and reporting conventions
- The cadence for review and the audience for the metric
- Any known gaps, duplicates, or ambiguous signals

## Workflow

1. Define the operational question the metric must answer.
2. Identify the exact signal, event, or source of truth that represents the work.
3. Check whether the definition is consistent with existing reporting and terminology.
4. Audit the measurement path for missing data, duplicates, or misleading proxies.
5. Set a review cadence and a threshold for what counts as healthy or unhealthy.
6. Verify the signal in the dashboard or source system and document the definition.

## Design Principles / Evaluation Criteria

- Measure the real process, not a convenient proxy
- Keep definitions stable so trend lines remain trustworthy
- Prefer a small set of useful metrics over a noisy dashboard
- Make every metric actionable by a clear owner
- Verify before relying on the result

## Output Contract

- Metric or measurement specification
- Source of truth and definition notes
- Coverage gaps, ambiguities, or duplicates found during audit
- Healthy and unhealthy thresholds, if applicable
- Verification status and follow-up work

## Examples

### Example 1

Input:
- Need: Measure design request turnaround time
- Surface: Intake to final handoff
- Issue: Teams disagree on where the timer should start

Expected output:
- Metric spec: Start timer at approved intake, stop at final handoff
- Required dimensions: request type, owner, priority, queue
- Validation: Confirm the metric matches the source system and is not double-counted

## Guardrails

- Do not define a metric that the team cannot verify
- Do not rely on ambiguous proxies when a direct signal exists
- Do not publish dashboards without a named owner
- Do not treat raw data as a decision-ready metric without validation

## Optional Tools / Resources

- Analytics dashboards or service reporting tools
- Spreadsheets for operational tracking
- Intake systems, queue tools, or ticketing records
- Retro notes or process reviews that expose recurring issues
