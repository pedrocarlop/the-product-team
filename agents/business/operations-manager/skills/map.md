---
name: map
description: Translate an operational problem into current-state and future-state process maps with roles, handoffs, decision points, and failure modes.
activation_hints:
  - "Use when the work needs an AS-IS / TO-BE view before anyone changes the process."
  - "Route here for swimlanes, handoffs, bottlenecks, escalation paths, and system touchpoints."
  - "Do not use for writing SOPs, coordinating execution, or driving continuous improvement."
---

# Map

## Purpose

Use this skill to document how an operational process works today and how it should work after a change, with enough structure that teams can see ownership, dependencies, and where work stalls.

## When to Use

- When a process is unclear, inconsistent, or handled differently by different teams
- When you need to make handoffs, approvals, or dependencies visible
- When the current flow needs to be understood before standardizing or improving it

## When Not to Use

- When the process is already understood and only needs to be documented as a repeatable standard
- When the main problem is coordination across teams rather than process structure
- When the task is primarily about fixing recurring issues after the process has already been mapped

## Required Inputs

- The operational problem or trigger that started the request
- The teams, owners, systems, and artifacts involved
- Any known current-state steps, variants, or exceptions
- Known pain points, delays, rework, or failure points
- Any timing, volume, or compliance constraints

## Workflow

1. Restate the process in plain operational terms and identify the outcome it must produce.
2. Document the current state step by step, including owners, tools, and decision points.
3. Mark every handoff, approval, dependency, and exception path.
4. Identify where work slows down, gets duplicated, or fails because information is missing.
5. Draft the smallest workable future state that removes the main friction.
6. Confirm the map is clear enough to support standardization or execution planning.

## Design Principles / Evaluation Criteria

- Clarity over diagram complexity
- Owners and decision points should always be explicit
- Exceptions matter as much as the happy path
- Handoffs should be visible, not implied
- The future state should solve the observed problem without adding unnecessary process

## Output Contract

- An AS-IS process map
- A TO-BE process map
- A list of key decisions, handoffs, and system touchpoints
- A summary of bottlenecks, waste, or failure modes

## Examples

### Example 1

Input:
- Current process note: "Vendor approvals happen through email, Slack, and a shared doc."

Expected output:
- Map note: "Approval ownership is split across channels, so there is no single source of truth for status or decision history."
- TO-BE note: "All approvals route through one tracked step with a named approver, timestamp, and stored decision record."

## Guardrails

- Do not map only the happy path
- Do not skip minor system touchpoints that create operational risk
- Do not turn the map into a solution spec too early
- Do not leave ownership ambiguous on any decision or handoff

## Optional Tools / Resources

- Existing SOPs or process docs
- Workshop notes, flowcharts, or whiteboards
- Timing, volume, or error-rate data
- Stakeholder interviews and operational examples

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [McKinsey Operations Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/operations/our-insights), [Asana Work Innovation Lab (asana.com)](https://asana.com/resources), [Harvard Business Review Operations (hbr.org)](https://hbr.org/topic/operations), [Lean Enterprise Institute (lean.org)](https://www.lean.org/explore-lean/)
