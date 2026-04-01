---
name: instrument
description: Specify, audit, and verify growth tracking so funnel metrics are measurable, trustworthy, and ready for experiments.
---

# Instrument

## Purpose

Use this skill to make sure the product’s growth events, properties, and dashboards are accurate enough to support decisions.

## When to Use

- When a funnel step is missing or ambiguous in analytics
- When a launch needs new events or event properties before shipping
- When the team needs to audit whether a metric is complete and trustworthy

## When Not to Use

- When the data already exists and the task is to decide what to test
- When the work is primarily root-cause diagnosis or rollout planning
- When the issue is a business decision, not a measurement gap

## Required Inputs

- The metric or user action that must be measured
- The product surface or journey stage where the event should fire
- Existing analytics taxonomy or tracking conventions
- Required properties, dimensions, and identity requirements
- Any known reporting gaps or duplicate events

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

1. Define the user action and the decision it must support.
2. Specify the event name, trigger condition, and required properties.
3. Check whether the event fits the existing taxonomy and identity model.
4. Audit coverage for missing steps, incomplete properties, or duplicate signals.
5. Verify the event in analytics after implementation or in a staging environment if possible.
6. Document the gap, the fix, and the validation status so downstream work can trust the data.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Measure the exact user action the team cares about
- Keep event names and properties consistent across surfaces
- Prefer verification over assumption
- Make every critical growth metric traceable to a defined event
- Prevent dashboards from becoming misleading because of partial coverage

## Output Contract

- Event or tracking specification
- Required properties and identity rules
- Coverage gaps or ambiguities found during audit
- Verification status and remaining risks
- Follow-up work needed before analytics can be trusted

## Examples

### Example 1

Input:
- Need: Track onboarding completion
- Surface: New web onboarding flow
- Existing issue: Completion cannot be segmented by plan type

Expected output:
- Event spec: `Onboarding Completed`
- Required properties: plan_type, onboarding_variant, device_type
- Validation: Confirm event fires once per user and appears in the funnel report with all properties populated

## Guardrails

- Do not define events that cannot be verified
- Do not leave required properties unspecified
- Do not measure the same action with multiple competing events
- Do not ship analytics changes without a validation step

## Optional Tools / Resources

- Amplitude, Mixpanel, or other analytics tooling
- SQL event tables and warehouse schemas
- Product tracking specs or implementation docs
- Launch or QA checklists

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Reforge Essays (reforge.com)](https://www.reforge.com/blog), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Mixpanel Blog (mixpanel.com)](https://mixpanel.com/blog/), [Andrew Chen Essays (andrewchen.com)](https://andrewchen.com/)
