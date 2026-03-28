---
name: health
description: Assess customer health using leading indicators, segment-aware thresholds, and clear actions for proactive outreach or escalation.
---

# Health

## Purpose

Use this skill to determine whether an account is on track, at risk, or in active churn danger, and to translate that reading into the right next action.

## When to Use

- When a health score needs to be defined, updated, or interpreted
- When usage or engagement data suggests risk
- When the team needs a consistent green/yellow/red framework

## When Not to Use

- When the primary task is onboarding design
- When the task is a renewal conversation or commercial negotiation
- When the focus is a specific escalation incident rather than portfolio health

## Required Inputs

- Account name, segment, and current status
- Usage signals, adoption depth, and engagement pattern
- Stakeholder coverage and recent customer communication
- Renewal timing and known business changes
- Existing thresholds, if any

## Workflow

1. Review the account's leading indicators: login frequency, adoption depth, and stakeholder engagement.
2. Compare those signals against the segment baseline and the customer's recent history.
3. Classify the account into green, yellow, or red using the current threshold model.
4. Identify the specific behaviors that support the classification.
5. Name the intervention or monitoring action that follows from the score.
6. Check whether the score is stale, inconsistent, or missing a critical signal.

## Design Principles / Evaluation Criteria

- Leading indicators matter more than lagging ones
- Segment context should affect interpretation
- Every score should explain the "why," not just the label
- Health should be operational, meaning it leads to a concrete action
- Thresholds should be easy to audit and update

## Output Contract

- Current health classification
- Short explanation of the signals behind it
- Recommended next action, owner, and urgency

## Examples

### Example 1

Input:
- Account: Enterprise customer
- Signals: Usage down 30%, champion inactive, renewal in 75 days

Expected output:
- Red health status with a note that the score is driven by declining usage and disengaged stakeholder coverage
- A recommendation to trigger proactive outreach and escalation review

## Guardrails

- Do not rely on a single metric in isolation
- Do not treat a stale score as current truth
- Do not ignore stakeholder risk when usage still looks healthy
- Do not invent precision that the underlying data does not support

## Optional Tools / Resources

- Product usage analytics
- CRM account history
- Customer communication logs
- Segment-level benchmark data

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Customer Service Blog (hubspot.com)](https://blog.hubspot.com/service), [Gainsight Resources (gainsight.com)](https://www.gainsight.com/resources/), [Intercom Blog (intercom.com)](https://www.intercom.com/blog), [Zendesk Blog (zendesk.com)](https://www.zendesk.com/blog/), [Nielsen Norman Group (nngroup.com)](https://www.nngroup.com/)
