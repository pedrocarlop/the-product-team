---
name: specify
description: Convert an agreed product direction into precise requirements, business rules, and acceptance criteria that can be built and tested.
activation_hints:
  - "Use when the product direction is chosen and you need implementable requirements."
  - "Route here for PRDs, user stories, acceptance criteria, and traceability."
  - "Do not use for discovery, framing, or choosing between competing options."
---

# Specify

## Purpose

Use this skill to turn a chosen product direction into clear requirements that tell the team what must be true, what is in scope, and how success will be judged.

## When to Use

- When the problem statement and intended outcome are already agreed
- When you need requirements, user stories, or acceptance criteria that can be implemented
- When the team needs traceability from the product decision to the work that will ship

## When Not to Use

- When the requirements are still disputed or fuzzy
- When the task is still about choosing the right solution
- When the work is only about communication or alignment

## Required Inputs

- The agreed product problem and target outcome
- The chosen direction or solution approach
- Known rules, constraints, dependencies, and risks
- Stakeholders who need to review or approve the requirements
- Any existing conventions for numbering, traceability, or documentation format

## Workflow

1. Break the product direction into discrete requirements that can be tested independently.
2. State each requirement in precise, unambiguous language.
3. Separate functional behavior, business rules, constraints, and assumptions.
4. Add acceptance criteria that cover the happy path and meaningful edge cases.
5. Link each requirement back to the problem statement or initiative it supports.
6. Review the wording for completeness, consistency, and testability.

## Design Principles / Evaluation Criteria

- One requirement, one meaning
- Testability over narrative style
- Traceability from problem to requirement to validation
- Completeness without unnecessary duplication
- Business language over implementation detail unless the implementation is itself a constraint

## Output Contract

- A numbered requirements set with clear identifiers
- Supporting business rules and assumptions
- Acceptance criteria for each requirement
- A traceability summary linking requirements to the product decision

## Examples

### Example 1

Input:
- Product direction: "Reduce activation drop-off for new users"

Expected output:
- Requirement: "REQ-001: The onboarding flow must show the next recommended step after account creation."
- Acceptance criteria: "Given a new user completes sign-up, when they reach the home screen, then the next step is visible without extra navigation."

## Guardrails

- Do not bundle multiple requirements into one paragraph
- Do not write acceptance criteria that cannot be tested
- Do not hide assumptions inside requirement text
- Do not introduce solution details unless they are a real constraint

## Optional Tools / Resources

- PRD templates
- Traceability matrix
- Product research notes
- Review notes from design, engineering, or stakeholders

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP, GitHub MCP
- Reference websites: [SVPG Articles (svpg.com)](https://www.svpg.com/articles/), [Lenny's Newsletter (lennysnewsletter.com)](https://www.lennysnewsletter.com/), [Mind the Product (mindtheproduct.com)](https://www.mindtheproduct.com/), [Amplitude Blog (amplitude.com)](https://amplitude.com/blog), [Product School Resources (productschool.com)](https://productschool.com/resources)
