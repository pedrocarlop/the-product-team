---
name: specify
description: Convert business needs and process understanding into precise requirements, business rules, and acceptance criteria that can be implemented and traced.
activation_hints:
  - "Use when the business need and process are known and you need testable requirements."
  - "Route here for BRDs, FRDs, user stories, business rules, and traceability."
  - "Do not use for discovery or process mapping."
---

# Specify

## Purpose

Use this skill to turn a mapped business need into clear, implementable requirements that tell teams what must be true and how success will be judged.

## When to Use

- When the problem statement and process impact are already understood
- When you need functional requirements, business rules, or user stories
- When acceptance criteria and traceability need to be written clearly

## When Not to Use

- When the requirements are still fuzzy or contested
- When you still need to understand the current state process
- When you are validating the final solution rather than defining it

## Required Inputs

- The agreed business problem and target outcome
- The relevant process map or workflow summary
- Known business rules, constraints, and dependencies
- Stakeholders who will review or sign off
- Any wording, numbering, or traceability conventions already in use

## Workflow

1. Break the business need into discrete requirements that can be tested independently.
2. State each requirement in precise, unambiguous language.
3. Separate functional behavior, business rules, constraints, and assumptions.
4. Add acceptance criteria that cover the happy path and meaningful edge cases.
5. Assign identifiers and trace requirements to the business problem or process step.
6. Review the wording for internal consistency and testability.

## Design Principles / Evaluation Criteria

- One requirement, one meaning
- Testability over narrative style
- Business language over technical jargon
- Traceability from problem to requirement to validation
- Completeness without unnecessary duplication

## Output Contract

- A numbered requirements set with unique identifiers
- Supporting business rules and assumptions
- Acceptance criteria for each requirement
- A traceability summary linking requirements to the problem or process step

## Examples

### Example 1

Input:
- Process note: "Managers need to approve requests before finance processes them."

Expected output:
- Requirement: "REQ-001: The system must prevent finance processing until an approved manager decision is recorded."
- Acceptance criteria: "Given a request is pending, when finance opens it, then processing actions remain unavailable until approval exists."

## Guardrails

- Do not bundle multiple requirements into one paragraph
- Do not write acceptance criteria that cannot be tested
- Do not hide assumptions inside requirement text
- Do not introduce solution details unless they are business constraints

## Optional Tools / Resources

- BRD or FRD templates
- Traceability matrix
- Policy documents or compliance rules
- Review notes from stakeholders or engineering

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [Harvard Business Review (hbr.org)](https://hbr.org/), [BA Times (batimes.com)](https://www.batimes.com/), [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [ProductPlan Glossary and Guides (productplan.com)](https://www.productplan.com/glossary/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/)
