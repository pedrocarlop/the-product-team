---
name: specify
description: Convert mapped business processes and stakeholder needs into traceable requirements, business rules, and acceptance criteria tied to process steps.
---

# Specify

## Purpose

Use this skill to turn a documented business process into precise, implementable requirements that trace from process steps to system behavior and can be validated by stakeholders.

## When to Use

- When a process map or current-state analysis has been completed and needs to become actionable requirements
- When business rules embedded in workflows, policies, or manual procedures must be formalized
- When acceptance criteria need to reflect process-level outcomes, not just feature behavior
- When traceability between process steps, requirements, and validation evidence is required

## When Not to Use

- When the business process has not been mapped or is still contested
- When the task is product-level feature definition rather than process-driven requirements
- When you are validating the solution rather than defining what it must do

## Required Inputs

- The process map, workflow summary, or current-state documentation
- Business rules from policy documents, compliance mandates, or SME interviews
- The stakeholders who own each process step and will sign off on requirements
- Data inputs, outputs, and handoff points between process steps
- Existing numbering, traceability, or documentation conventions

## Workflow

1. Walk the process map step by step and extract the decision points, rules, and system interactions.
2. Write each requirement against the process step it derives from, not as a standalone feature request.
3. Separate functional requirements, business rules, data constraints, and assumptions.
4. Add acceptance criteria that reflect the process outcome, including handoff conditions and exception paths.
5. Assign identifiers and link each requirement to its source process step or policy.
6. Review with the process owner to confirm the requirements match actual practice, not idealized flow.

## Design Principles / Evaluation Criteria

- Requirements should trace to process steps, not float as orphaned features
- Business rules should come from documented sources, not assumptions
- Acceptance criteria should cover the handoff between process steps, not just within them
- Exception paths matter as much as the happy path
- Language should be business-facing and verifiable by non-technical stakeholders

## Output Contract

- A numbered requirements set with process-step traceability
- Business rules extracted from policy, compliance, or SME sources
- Acceptance criteria covering happy path, exceptions, and handoff conditions
- A traceability matrix linking requirements to process steps, owners, and validation method

## Examples

### Example 1

Input:
- Process: Expense approval workflow with manager review, finance check, and payment release
- Source: Process map from current-state analysis

Expected output:
- REQ-001: "The system must route expense submissions to the submitter's direct manager before finance review." (traces to process step 2)
- Acceptance criteria: "Given an expense is submitted, when the manager has not yet acted, then finance review actions are unavailable."
- Business rule: "Expenses above $5,000 require VP-level approval in addition to direct manager." (source: Finance Policy v3.1)

## Guardrails

- Do not write requirements that cannot be traced to a process step or business rule
- Do not assume process behavior without confirming with the process owner
- Do not skip exception paths and handoff conditions
- Do not use implementation language when business language is sufficient

## Optional Tools / Resources

- Process maps and current-state documentation
- Policy documents and compliance references
- BRD/FRD templates and traceability matrices
- Stakeholder interview notes

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
