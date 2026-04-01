---
name: standardize
description: Define and document repeatable design standards so quality, critique, and handoff stay consistent across the team.
---

# Standardize

## Purpose

Use this skill to turn recurring design judgment into shared standards that can be applied consistently across work and across people.

## When to Use

- When a design team needs a clearer definition of good work
- When critique, handoff, or review decisions vary too much between people
- When repeated issues should become a documented standard instead of repeated feedback

## When Not to Use

- When you only need to review a single design artifact
- When the main need is coaching a designer on a specific gap
- When the decision is about where design effort should go next

## Required Inputs

- The workflow, surface, or decision area that needs standardization
- Examples of inconsistent work or repeated failure modes
- The people or teams who will use the standard
- Existing rules, patterns, or constraints that should be preserved
- Any threshold for exceptions, escalation, or required review

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: design-systems
project: <slug>
deliverable: design-systems.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Inventory where judgment is currently inconsistent or expensive.
2. Define the standard in observable terms that others can apply.
3. Distinguish required rules from preferred patterns and stylistic preferences.
4. Write the standard in a reusable format such as checklist, rubric, or examples.
5. Socialize the standard with the people who will use it and explain why it exists.
6. Revisit the standard after real use to remove ambiguity and fix gaps.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Explicit over implicit
- Observable over interpretive
- Reusable over one-off
- Minimal and practical over exhaustive
- Stable enough to guide decisions, flexible enough for real product constraints
- Aligned with product goals and user outcomes

## Output Contract

- A documented standard, checklist, rubric, or pattern set
- Clear pass/fail or acceptable/unacceptable guidance where needed
- Examples that show the standard in practice
- Any exceptions, owners, or review points that need to be tracked

## Examples

### Example 1

Input:
- The team keeps shipping inconsistent empty states and unclear recovery actions

Expected output:
- A small standard covering messaging, actions, and state behavior
- Examples of good and bad patterns
- A note on when to escalate exceptions

## Guardrails

- Do not standardize away useful judgment too early
- Do not encode personal taste as policy
- Do not make the standard so large that nobody uses it
- Do not forget to explain the user or business reason behind the rule

## Optional Tools / Resources

- Design system documentation
- Review rubrics or critique notes
- Notion pages, team docs, or decision logs
- Shared examples from recent product work
