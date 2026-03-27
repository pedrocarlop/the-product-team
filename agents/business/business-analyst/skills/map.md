---
name: map
description: Translate a clarified business need into an AS-IS and TO-BE process map with stakeholders, decisions, handoffs, and system touchpoints.
activation_hints:
  - "Use when the business problem is understood and the next step is documenting process flow."
  - "Route here for AS-IS / TO-BE mapping, swimlanes, handoffs, and exception paths."
  - "Do not use for requirement elicitation, formal specification, or test validation."
---

# Map

## Purpose

Use this skill to document how a business process works today and how it should work after the change, with enough structure that teams can see roles, decisions, and operational impact.

## When to Use

- When you need an AS-IS or TO-BE process map
- When handoffs between teams or systems need to be made visible
- When decision points, exceptions, or rework paths need to be documented

## When Not to Use

- When the main task is discovering the underlying business need
- When you only need a requirements list or acceptance criteria
- When the process has not yet been clarified enough to map meaningfully

## Required Inputs

- The clarified business problem and target outcome
- The stakeholders, roles, and systems involved
- Known current-state steps or artifacts
- Known exceptions, variants, and escalation points
- Any timing, volume, or operational constraints

## Workflow

1. Document the current state in observable, step-by-step terms.
2. Identify every role, decision, handoff, and system touchpoint.
3. Capture the happy path first, then add alternate and exception paths.
4. Mark where delays, rework, or duplicate effort appear.
5. Draft the future state with the smallest necessary process change that solves the problem.
6. Check that the map explains operational impact clearly enough for downstream specification.

## Design Principles / Evaluation Criteria

- Clarity over diagram complexity
- Every decision should have an owner or rule behind it
- Exceptions matter as much as the happy path
- Handoffs should be explicit and easy to follow
- The future state should be understandable without extra narration

## Output Contract

- An AS-IS process map
- A TO-BE process map
- A list of key decisions, handoffs, and touchpoints
- A summary of gaps, waste, or bottlenecks observed

## Examples

### Example 1

Input:
- Current process note: "Approvals happen by email and sometimes in Slack."

Expected output:
- Map note: "Approval step is split across channels, creating an unclear handoff and inconsistent audit trail."
- TO-BE note: "All approvals route through a single tracked step with named approver and timestamp."

## Guardrails

- Do not map only the happy path
- Do not skip system touchpoints because they seem minor
- Do not convert the map into a solution design exercise too early
- Do not leave ownership ambiguous on decisions or handoffs

## Optional Tools / Resources

- Existing SOPs or process docs
- Whiteboards, flowcharts, or workshop outputs
- Timing or volume data
- Stakeholder interviews and operational examples

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
