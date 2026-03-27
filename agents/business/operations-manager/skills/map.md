---
name: map
description: Translate an operational problem into current-state and future-state process maps with swim lanes, SLA boundaries, failure modes, and capacity constraints.
---

# Map

## Purpose

Use this skill to document how an operational process works today and how it should work after a change, with enough structure to expose ownership gaps, SLA violations, capacity bottlenecks, and rework loops that degrade throughput.

## When to Use

- When a process is handled inconsistently across teams, shifts, or geographies and needs to be standardized
- When throughput, cycle time, or error rate indicates a structural process problem
- When handoffs between teams or systems are causing delays, rework, or dropped items
- When a new tool, automation, or headcount change requires the process to be redesigned

## When Not to Use

- When the process is already mapped and the task is scoping a product or technology change around it
- When the main problem is strategic prioritization rather than execution mechanics
- When the task is writing requirements or acceptance criteria for a downstream team

## Required Inputs

- The operational problem or trigger: what broke, what is slow, or what is inconsistent
- The teams, roles, shifts, and systems involved in the current process
- Volume, frequency, and timing data (daily ticket count, average cycle time, peak load)
- Known pain points: delays, rework loops, manual workarounds, and escalation triggers
- SLA or compliance constraints that bound acceptable performance
- Any existing SOPs, runbooks, or process documentation

## Workflow

1. Restate the process in plain operational terms: what goes in, what comes out, and who is responsible at each step.
2. Document the current state with swim lanes for each responsible party (person, team, or system).
3. Mark every handoff, queue, approval gate, and exception path.
4. Measure or estimate cycle time, wait time, and rework frequency at each step.
5. Identify the constraint: where does the process stall, loop, or fail most often?
6. Draft the future state by removing the constraint with the smallest viable process change.
7. Add SLA checkpoints and escalation triggers to the future state so the improved process can be monitored.

## Design Principles / Evaluation Criteria

- Swim lanes make ownership unambiguous at every step
- Cycle time and wait time should be visible, not hidden inside a step
- Exceptions and rework loops matter as much as the happy path
- The future state should reduce the identified constraint, not add process for its own sake
- SLA and escalation rules should be explicit enough to automate or alert on

## Output Contract

- An AS-IS process map with swim lanes, handoffs, and timing estimates
- A TO-BE process map with the constraint removed and SLA checkpoints added
- A constraint summary: what causes the most delay, rework, or failure
- A list of handoffs, queues, and escalation triggers with ownership assignments
- Capacity or volume notes that affect feasibility of the future state

## Examples

### Example 1

Input:
- Current process note: "Vendor approvals happen through email, Slack, and a shared doc. Average cycle time is 4 days but the SLA is 2 days."

Expected output:
- AS-IS note: "Approval ownership is split across three channels. No single queue tracks status, so follow-ups are manual and approvals stall when the approver is out."
- Constraint: "The bottleneck is the lack of a single queue with visibility into aging items."
- TO-BE note: "All approvals route through one tracked queue with a named approver, a 24-hour SLA reminder, and an auto-escalation to backup at 48 hours."

## Guardrails

- Do not map only the happy path; rework loops and exception paths drive most operational cost
- Do not skip timing estimates even when exact data is unavailable -- use informed ranges
- Do not design a future state that solves problems the current state does not actually have
- Do not leave ownership ambiguous on any decision, queue, or handoff
- Do not turn the map into a technology requirements document; stay at the process layer

## Optional Tools / Resources

- Existing SOPs, runbooks, or process docs
- Workshop notes, flowcharts, or whiteboards
- Timing, volume, or error-rate data from ticketing or monitoring systems
- Stakeholder interviews and operational walk-throughs

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [McKinsey Operations Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/operations/our-insights), [Asana Work Innovation Lab (asana.com)](https://asana.com/resources), [Harvard Business Review Operations (hbr.org)](https://hbr.org/topic/operations), [Lean Enterprise Institute (lean.org)](https://www.lean.org/explore-lean/)
