---
name: route
description: Decide lead, account, opportunity, and handoff routing so revenue work lands with the right owner at the right time.
---

# Route

## Purpose

Use this skill to define and maintain routing logic for revenue work so leads, accounts, opportunities, and handoffs move to the correct owner without ambiguity.

## When to Use

- When lead assignment rules need to be created or changed
- When ownership should move between marketing, SDR, AE, CS, or ops
- When routing depends on geography, segment, product, capacity, or account state
- When escalation paths or exception handling need to be made explicit

## When Not to Use

- When the main problem is dirty data or broken field standards
- When the task is to build a forecast or capacity model
- When the work is about explaining performance instead of assigning ownership

## Required Inputs

- The object being routed and the decision point
- Ownership rules, segment definitions, and any fallback logic
- Capacity limits, service-level expectations, and timing requirements
- The systems that will enforce the routing decision
- Any exceptions that must bypass the standard flow

## Workflow

1. Identify the record type and the exact moment routing should occur.
2. Define the ownership rule in plain language before writing system logic.
3. Specify the primary path, fallback path, and exception path.
4. Check capacity and timing so the rule is operable in the real workflow.
5. Document the handoff criteria and the signal that triggers the next owner.
6. Verify the rule can be monitored and audited after it goes live.

## Design Principles / Evaluation Criteria

- Clear ownership at every step
- Routing should be based on explicit rules, not tribal knowledge
- Exceptions should be visible and limited
- The logic should reflect actual operating capacity
- Handoffs should be measurable and auditable

## Output Contract

- The routing rule or decision tree
- Ownership, fallback, and exception paths
- The systems or workflows that enforce the rule
- Notes on operational limits or risks

## Examples

### Example 1

Input:
- Request: "Route enterprise inbound leads to the right AE within five minutes."
- Context: Segments are defined by employee count and ARR potential

Expected output:
- Rule: Route by segment and territory, then fallback to the assigned queue
- Enforcement: CRM workflow with capacity-aware assignment
- Output: A documented routing policy and exception path

## Guardrails

- Do not route work without a clear ownership rule
- Do not hide manual overrides without logging them
- Do not create routing logic that ignores capacity or response-time limits
- Do not confuse routing with lead scoring or forecast logic

## Optional Tools / Resources

- Salesforce or HubSpot workflows
- Slack for handoff notifications
- Notion for routing policy documentation
- Capacity or territory planning sheets

- Shared MCP servers: Notion MCP, Slack MCP, Linear MCP
- Reference websites: [HubSpot Revenue Operations resources (hubspot.com)](https://www.hubspot.com/revenue-operations), [Salesforce Revenue Intelligence resources (salesforce.com)](https://www.salesforce.com/resources/), [Gartner Sales Operations insights (gartner.com)](https://www.gartner.com/en/sales), [McKinsey Growth, Marketing & Sales Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights), [Winning by Design Resources (winningbydesign.com)](https://winningbydesign.com/resources/)
