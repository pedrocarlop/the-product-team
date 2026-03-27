---
name: frame
description: Turn an ambiguous product request into a clear problem statement, scope boundary, success criteria, and design direction for the rest of the work.
activation_hints:
  - "Use when the request is unclear, broad, or not yet ready for flows or UI decisions."
  - "Route here when you need to define the problem, users, constraints, and what success means."
  - "Do not use for detailed interaction design, visual layout, or component selection."
---

# Frame

## Purpose

Use this skill to define the design problem precisely enough that the rest of the UX and UI work can proceed with confidence.

## When to Use

- When the request is fuzzy, overly broad, or full of assumptions
- When the team needs a shared problem statement before flow or UI work starts
- When success criteria, constraints, or scope boundaries are not yet explicit

## When Not to Use

- When the problem statement is already agreed and the task is to design the solution
- When the work is primarily about state coverage, component choice, or visual treatment
- When the request is for a local screen fix rather than an upfront framing pass

## Required Inputs

- The request, goal, or opportunity being considered
- The users affected and the task they are trying to complete
- Known constraints, dependencies, risks, and business stakes
- Any evidence, research, or stakeholder context that changes the framing
- The decision that the framing needs to support

## Workflow

1. Restate the problem in one sentence that a non-designer could confirm or correct.
2. Identify who is affected, what they do today, and what pain or friction matters.
3. Separate facts, assumptions, and open questions so the team can see the uncertainty.
4. Define the smallest useful scope that could test the core assumption.
5. Name the success criteria and what would count as a meaningful improvement.
6. Capture the constraints or tradeoffs that should shape the rest of the design work.

## Design Principles / Evaluation Criteria

- Clear problem definition before solution work
- User outcome over feature description
- Explicit assumptions instead of hidden guesses
- Scope that is small enough to test but large enough to matter
- Success criteria that are measurable or observable

## Output Contract

- A concise problem statement
- The affected users, constraints, and business stakes
- Key assumptions and open questions
- A scoped design direction or testable hypothesis

## Examples

### Example 1

Input:
- Request: "Improve checkout"
- Context: Abandonment increased, but the drop-off point is unclear

Expected output:
- Problem statement: "Users are leaving checkout before payment because the flow asks for too much effort too late."
- Scope: "Focus on the payment step and its prerequisites, not the entire shopping journey."
- Success criteria: "Reduce payment-step abandonment and support successful completion on first attempt."

## Guardrails

- Do not turn framing into full solution design
- Do not invent facts or business goals that are not supported
- Do not skip the user task in favor of a purely internal project description
- Do not let the framing become so broad that it cannot guide design work

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for source context and framing evidence
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Maze](https://maze.co/)
- [Dovetail](https://dovetail.com/)
- [Material Design](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
