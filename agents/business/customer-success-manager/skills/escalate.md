---
name: escalate
description: Handle high-risk customer situations with clear criteria, fast internal routing, and a structured recovery plan.
activation_hints:
  - "Use when a customer is threatening churn, a critical issue is blocking value, or account risk needs immediate coordination."
  - "Route here for executive escalation, daily communication cadences, root-cause tracking, and recovery planning."
  - "Do not use for routine onboarding, low-risk health checks, or standard renewal prep."
---

# Escalate

## Purpose

Use this skill to move a customer issue from concern to coordinated action, with explicit ownership, urgency, and recovery steps.

## When to Use

- When the customer threatens to cancel or reduce spend
- When a critical issue blocks production use or business value
- When the health score crosses into urgent risk and needs immediate intervention

## When Not to Use

- When the issue can be handled through normal onboarding or health work
- When the situation is important but not urgent
- When no clear customer impact or risk is present

## Required Inputs

- Customer name and account context
- Description of the issue or risk signal
- Business impact, urgency, and scope
- Existing owner, supporting teams, and current customer communication
- Any deadline, contract pressure, or executive involvement

## Workflow

1. Confirm the issue meets escalation criteria.
2. Clarify the customer impact and the deadline pressure.
3. Identify the internal owner, decision maker, and needed supporting teams.
4. Set the immediate communication cadence with the customer.
5. Define the recovery plan, success condition, and follow-up checkpoints.
6. Capture the root cause and prevention angle once the situation is contained.

## Design Principles / Evaluation Criteria

- Escalation should reduce uncertainty quickly
- The customer should know who owns the next step
- Internal routing should happen fast and once
- Recovery should include prevention, not just resolution
- Communication cadence matters as much as the fix

## Output Contract

- Escalation summary with severity and customer impact
- Named owner and supporting responders
- Immediate next actions and customer communication cadence
- Root-cause note or follow-up requirement

## Examples

### Example 1

Input:
- Customer: Enterprise account
- Issue: Production workflow blocked by a bug
- Impact: Users cannot complete a critical task

Expected output:
- An escalation summary with severity, owner, and immediate update cadence
- A recovery plan that includes follow-up until the issue is resolved

## Guardrails

- Do not escalate every complaint
- Do not leave ownership ambiguous
- Do not treat escalation as a one-way notification
- Do not close the issue without a prevention note

## Optional Tools / Resources

- Escalation playbook
- Account health history
- Internal routing contacts
- Incident or issue tracking system

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Customer Service Blog (hubspot.com)](https://blog.hubspot.com/service), [Gainsight Resources (gainsight.com)](https://www.gainsight.com/resources/), [Intercom Blog (intercom.com)](https://www.intercom.com/blog), [Zendesk Blog (zendesk.com)](https://www.zendesk.com/blog/), [Nielsen Norman Group (nngroup.com)](https://www.nngroup.com/)
