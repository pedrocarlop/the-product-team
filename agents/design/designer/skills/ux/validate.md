---
name: validate
description: Validate a UX direction with heuristics, scenarios, and usability checks before the design is handed off or implemented.
---

# Validate

## Purpose

Use this skill to test whether the proposed UX actually works for the user, not just whether it looks complete on paper.

## When to Use

- When a flow, wireframe, or interaction model needs usability review
- When the team needs to check for friction, confusion, or hidden edge cases
- When you want to prioritize design fixes before handoff or implementation

## When Not to Use

- When the structure has not yet been mapped
- When the work is primarily about layout, hierarchy, or visual refinement
- When no meaningful test question or user task is defined

## Required Inputs

- The current UX direction, wireframe, prototype, or flow description
- The target users and the scenario to evaluate
- The success criteria or business outcome that matters most
- Known risks, assumptions, and edge cases to inspect
- Any constraints on test method, time, or available participants

## Workflow

1. State the question the validation should answer.
2. Define the user tasks or scenarios that will expose the risk.
3. Choose the lightest useful method, such as heuristic review, scenario walk-through, or moderated test.
4. Check the experience against clarity, recoverability, discoverability, and error handling.
5. Separate confirmed issues from assumptions and open questions.
6. Prioritize findings by severity and impact on the target task.
7. Recommend the smallest set of changes that would materially improve the experience.

## Design Principles / Evaluation Criteria

- The user should understand what is happening and what to do next
- Important paths should be discoverable without coaching
- Errors and edge cases should be recoverable
- The design should support the intended user outcome with minimal friction
- Findings should be specific enough to drive action

## Output Contract

- A validation summary with the test question and method used
- A prioritized list of issues, risks, or failed assumptions
- Recommendations for fixes or follow-up tests
- Any confidence limits on the findings

## Guardrails

- Do not present a heuristic review as if it were a full user study
- Do not claim validation that was not actually performed
- Do not blur design preference with usability failure
- Do not ignore high-severity friction just because the flow is otherwise functional

## Optional Tools / Resources

- Prototype or screenshot evidence
- Research notes, support tickets, or analytics
- Existing usability heuristics or internal design review criteria
- Task scripts or discussion guides for a follow-up test
