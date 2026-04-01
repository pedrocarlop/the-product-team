---
name: renew
description: Plan and run renewal work with clear timing, risk management, forecast discipline, and expansion awareness.
---

# Renew

## Purpose

Use this skill to make renewal a managed process instead of a last-minute event, with clear timing, risk handling, and stakeholder coverage.

## When to Use

- When the renewal date is within the planning window
- When the account needs a renewal forecast or renewal call plan
- When expansion opportunities should be paired with the renewal conversation

## When Not to Use

- When the customer is still onboarding
- When the main problem is a technical or customer-health escalation
- When no contract or renewal date is in scope

## Required Inputs

- Contract end date and renewal window
- ARR, segment, and commercial structure
- Current health status and major risks
- Stakeholder map, especially champion and economic buyer
- Expansion signals or unresolved blockers

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

1. Anchor the work on the renewal date and the required lead time.
2. Review current health, usage, and stakeholder coverage for risk.
3. Identify renewal blockers, unresolved commitments, and expansion signals.
4. Build the renewal plan with milestones for internal alignment and customer communication.
5. Determine whether the motion is renewal-only or renewal plus expansion.
6. Update forecast status with the most accurate risk picture available.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Renewal should begin early enough to resolve risk, not just register it
- The plan should separate facts from assumptions
- Expansion should be discussed when it is earned by value and adoption
- Forecasting should reflect real customer status, not optimism
- Stakeholder breadth matters as much as product usage

## Output Contract

- Renewal timeline with key milestones
- Risk summary and mitigation plan
- Customer-facing conversation structure when needed
- Forecast status or recommended next commercial step

## Examples

### Example 1

Input:
- Account: Mid-market
- Renewal date: 90 days out
- Signals: Strong usage, one champion, expansion signal present

Expected output:
- A renewal plan that starts the conversation now
- A note to multi-thread the account and include expansion discovery in the discussion

## Guardrails

- Do not wait until the last month to start renewal work
- Do not treat renewal as a pure sales handoff
- Do not ignore risk signals because the customer is still active
- Do not pursue expansion before the customer has shown value

## Optional Tools / Resources

- Renewal calendar
- CRM forecast fields
- Account health history
- Stakeholder notes and commercial terms

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Customer Service Blog (hubspot.com)](https://blog.hubspot.com/service), [Gainsight Resources (gainsight.com)](https://www.gainsight.com/resources/), [Intercom Blog (intercom.com)](https://www.intercom.com/blog), [Zendesk Blog (zendesk.com)](https://www.zendesk.com/blog/), [Nielsen Norman Group (nngroup.com)](https://www.nngroup.com/)
