---
name: wire
description: Translate task flows and information architecture into low-fidelity wireframes that define screen purpose, content hierarchy, and interaction scaffolding for user-centered evaluation.
---

# Wire

## Purpose

Use this skill to turn a mapped user flow into wireframes that make screen purpose, content priority, and interaction logic visible enough for early usability evaluation and stakeholder alignment.

## When to Use

- When a task map or IA exists and the next step is defining what appears on each screen and why
- When layout decisions need to be grounded in user mental models and task priority
- When responsive behavior, empty states, or conditional paths need structural definition before visual design begins
- When the team needs a reviewable artifact to validate assumptions about user behavior

## When Not to Use

- When the problem is still about what the experience should do, not how screens should be arranged
- When the request is for high-fidelity UI, brand styling, or visual polish
- When the work is primarily about measuring usability of an existing implementation

## Required Inputs

- The mapped flow, task model, or information architecture
- User research insights, personas, or mental model evidence that should inform hierarchy
- Any screenshots or existing screens the wireframe must align with
- Component constraints, platform patterns, and breakpoints
- State requirements: loading, empty, error, success, disabled, and conditional paths
- Known accessibility, content length, or localization constraints

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

1. Restate the user's primary goal for each screen and use it to drive hierarchy decisions.
2. Arrange content from most task-relevant to least, using research evidence to resolve priority conflicts.
3. Place controls and feedback where they reduce decision cost and support progressive disclosure.
4. Define interaction behavior for primary, secondary, and conditional actions, noting branching logic.
5. Draft responsive variants that preserve task priority across viewport sizes.
6. Annotate unresolved assumptions, open user research questions, and decisions that need validation.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Hierarchy should reflect user task priority, not internal data structure
- Every screen should have a single clear primary action
- States and edge cases must be visible in the scaffold, not deferred
- The wireframe should invite critique and iteration, not premature commitment
- Content strategy and interaction logic matter more than pixel precision
- Annotations should make the rationale legible to non-designers

## Output Contract

- Low-fidelity wireframes or screen skeletons organized by flow
- Interaction notes explaining primary paths, branches, and conditional logic
- Responsive or layout variants when viewport changes affect hierarchy
- A list of open assumptions or questions that need user validation
- Callouts for areas where research evidence is thin

## Guardrails

- Do not add visual styling that distracts from structural decisions
- Do not leave critical interactions implied when they need to be explicit
- Do not over-specify pixels when the question is still about flow or hierarchy
- Do not ignore states that materially change the user's path or confidence
- Do not treat wireframes as final; they exist to be tested and revised

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, Notion MCP, and Paper MCP for flow grounding and wireframe context
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Maze](https://maze.co/)
- [Dovetail](https://dovetail.com/)
- [Material Design](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
