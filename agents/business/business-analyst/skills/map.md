---
name: map
description: Translate a clarified business need into an AS-IS and TO-BE process map that exposes decision logic, data dependencies, and system integration points for downstream specification.
---

# Map

## Purpose

Use this skill to document a business process in enough detail that product, design, and engineering teams can build from it: who decides what, where data moves between systems, and which rules govern exceptions. The map is an analytical artifact, not an operational runbook.

## When to Use

- When a business process needs to be understood before writing requirements or user stories
- When decision logic, business rules, or exception handling is buried in tribal knowledge
- When system integration points, data flows, or approval hierarchies need to be made explicit for a downstream team
- When stakeholders describe the same process differently and a single source of truth is needed

## When Not to Use

- When the main task is discovering the underlying business need (use the frame skill first)
- When the process is already documented and the task is to optimize throughput or SLA performance
- When the work is writing requirements or acceptance criteria rather than understanding the process they describe

## Required Inputs

- The clarified business problem and target outcome
- The stakeholders, roles, and systems involved
- Known current-state steps, artifacts, and data objects that move between steps
- Known decision rules, business policies, and exception criteria
- System names and integration points where data enters or leaves the process
- Any regulatory, compliance, or audit requirements that constrain the process

## Workflow

1. Document the current state in observable, step-by-step terms with the data objects that flow between steps.
2. Identify every decision point and capture the business rule or policy that governs it.
3. Map system touchpoints: where data is created, read, updated, or handed off to another system.
4. Capture the happy path first, then add alternate paths, exception rules, and escalation criteria.
5. Mark where information is lost, duplicated, or manually re-entered between systems.
6. Draft the future state focused on closing data gaps and clarifying decision rules, not on operational speed.
7. Verify that the map is detailed enough for a requirements author or product manager to write specifications from it.

## Design Principles / Evaluation Criteria

- Decision rules should be explicit enough to automate or at least to write acceptance criteria from
- Data objects and system handoffs should be named, not implied
- Exceptions matter as much as the happy path because they often drive the most complex requirements
- The map should serve downstream specification work, not replace it
- The future state should be understandable by someone who was not in the room when it was created

## Output Contract

- An AS-IS process map with decision rules, data objects, and system touchpoints
- A TO-BE process map with decision rules clarified and data gaps closed
- A list of key decisions with the business rule or policy behind each one
- A list of system integration points and the data that crosses each boundary
- A summary of gaps, ambiguities, or undocumented rules that need stakeholder confirmation

## Examples

### Example 1

Input:
- Current process note: "Refund approvals happen by email and sometimes in Slack. The threshold depends on the customer tier."

Expected output:
- AS-IS note: "Refund requests above $500 require manager approval, but the tier lookup is manual and the threshold is not enforced by any system. Approvals happen in email with no audit trail."
- Decision rule: "Approval threshold = $500 for standard tier, $2000 for enterprise tier (source: finance policy doc, last updated Q2)."
- TO-BE note: "Tier lookup is automated from the CRM record. Approvals below threshold are auto-approved with a log entry. Approvals above threshold route to the finance queue with a 24-hour SLA."

## Guardrails

- Do not map only the happy path; exception paths drive the most complex downstream requirements
- Do not skip system integration points because the data flow seems obvious
- Do not convert the map into a solution design or UI specification
- Do not leave decision rules as "manager decides" without capturing the criteria the manager uses
- Do not assume a process is correct just because it is current; note where the stated rule and observed behavior diverge

## Optional Tools / Resources

- Existing SOPs, policy documents, or process docs
- Whiteboards, flowcharts, or workshop outputs
- System architecture diagrams or integration inventories
- Stakeholder interviews and operational walk-throughs

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
