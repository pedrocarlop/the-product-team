---
name: test
description: Design and run usability tests that measure whether users can complete key tasks, where they struggle, and what the interface needs to change.
---

# Test

## Purpose

Use this skill to validate whether users can complete a task, understand the interface, and recover when things go wrong.

## When to Use

- When the team needs to check usability before design decisions harden
- When you need task-based evidence for comprehension, findability, or flow issues
- When success or failure can be defined clearly in advance

## When Not to Use

- When the question is exploratory and better suited to interviews
- When the study plan is not yet defined
- When the task is already complete and the work is only synthesis

## Required Inputs

- The task or flow to test
- Success and failure criteria
- The participant profile and how closely they need to match the target user
- The environment or prototype fidelity available
- The specific behaviors or states that must be observed

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: designer
project: <slug>
deliverable: designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Define what successful completion means before the session starts.
2. Break the task into realistic prompts that reflect user intent.
3. Include paths for errors, hesitation, recovery, and abandonment.
4. Run the test with consistent moderation and note-taking.
5. Record completion, confusion points, workarounds, and time to recover.
6. Compare results across participants rather than relying on one strong opinion.
7. Summarize what failed, why it failed, and what to change next.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Task success is defined before testing begins
- Prompts reflect real user goals, not interface instructions
- Errors and recovery are treated as first-class evidence
- Results are compared across participants and segments
- The output points to concrete design changes

## Output Contract

- Test goal and task list
- Success and failure criteria
- Observed completion rates and notable breakdowns
- Evidence-based recommendations or follow-up questions

## Examples

### Example 1

Input:
- Task: update a payment method in settings
- Goal: find out whether users can locate and complete the action without help

Expected output:
- A test plan with the exact prompt, success definition, and failure triggers
- Results noting where users hesitated, what labels confused them, and whether they recovered

## Guardrails

- Do not evaluate usability without a defined success criterion
- Do not treat a prototype session as real-world proof of behavior
- Do not let moderation drift vary between participants
- Do not turn test notes into synthesis unless the study is complete

## Optional Tools / Resources

- Maze or similar testing tools
- Playwright or session replay when appropriate
- Notion for test plans and results
