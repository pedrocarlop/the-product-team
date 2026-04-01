---
name: calibrate
description: Align expectations for performance, growth, promotion, and team health so people decisions are consistent and evidence-based.
---

# Calibrate

## Purpose

Use this skill to align people decisions and expectations so the team applies a consistent standard to performance, growth, and readiness.

## When to Use

- When managers or peers need to compare readiness across people or roles
- When promotion, growth, or performance expectations need to be made concrete
- When feedback needs to be aligned before it is delivered
- When the team needs a shared standard for what good looks like

## When Not to Use

- When the issue is a staffing or headcount question
- When the main need is to plan a project or remove a blocker
- When the decision is about technical direction rather than people judgment
- When there is not enough evidence yet to compare against the bar

## Required Inputs

- The role, level, or expectation being calibrated
- The evidence available, including examples and outcomes
- The standard or rubric being used
- The audience for the calibration decision
- Any known risks, conflicts, or prior feedback that affect judgment

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Define the standard being used before comparing people against it.
2. Gather specific evidence, not general impressions.
3. Compare the evidence to the bar and identify gaps or strengths.
4. Check for inconsistency across raters or managers.
5. Reconcile disagreements by returning to the rubric and the examples.
6. Write down the decision, rationale, and any follow-up actions.
7. Make sure the calibrated view is simple enough to communicate consistently.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Calibration should reduce bias, not just produce consensus
- Evidence should be specific and recent enough to trust
- The standard should stay stable across people being compared
- Feedback should be actionable and tied to observable behavior
- Decisions should be explainable without relying on status or tenure

## Output Contract

- Calibrated decision or recommendation
- Evidence summary tied to the standard
- Any disagreements and how they were resolved
- Follow-up feedback or development actions

## Examples

### Example 1

Input:
- Request: "Calibrate promotion readiness for two engineers"
- Evidence: project outcomes, peer feedback, and role expectations

Expected output:
- Decision: who is ready, who needs more evidence, and why
- Rationale: examples mapped to the stated bar
- Follow-up: the development work that would close remaining gaps

## Guardrails

- Do not calibrate without a shared bar or rubric
- Do not rely on vague praise or frustration
- Do not collapse distinct levels or roles into one standard
- Do not let the loudest voice in the room determine the answer

## Optional Tools / Resources

- Role expectations, promotion rubrics, and growth frameworks
- Performance notes, examples, and feedback history
- Calibration packets or decision memos
- Meeting notes from manager or peer reviews
