---
name: align
description: Align service design decisions with operational reality, stakeholder needs, and service metrics so the proposed experience can actually be delivered and measured.
---

# Align

## Purpose

Use this skill to check that the designed service can be delivered, supported, measured, and adopted by the organization that runs it.

## When to Use

- When service design needs to be validated against staffing, systems, policy, or cost constraints
- When the team needs to reconcile user needs with operational realities
- When success metrics and ownership need to be made explicit
- When stakeholders need a shared view of tradeoffs before work proceeds

## When Not to Use

- When the task is only to map journeys or touchpoints
- When alignment is already settled and the open question is purely execution detail
- When no organizational constraint or tradeoff is being evaluated

## Required Inputs

- The proposed service change and the business or user outcome it should support
- Relevant operational constraints, policies, or capability gaps
- Stakeholders who need to agree on the direction
- Service metrics or signals that define success
- Any known implementation risks or dependencies

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

1. Restate the service goal in terms the organization can evaluate.
2. Identify the constraints, assumptions, and tradeoffs that shape the design.
3. Map which teams or roles must support the design for it to work.
4. Tie the proposal to service metrics or business outcomes.
5. Call out open decisions, dependencies, and risks that need confirmation.
6. Verify the design remains realistic and accountable after the alignment check.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Feasibility over aspiration
- Shared understanding over hidden assumptions
- Measurable outcomes over vague success language
- Clear accountability over diffuse ownership
- Constraint-aware decisions over idealized designs

## Output Contract

- A concise alignment note covering goals, constraints, tradeoffs, stakeholders, and success measures
- A list of open issues or approvals needed before implementation
- Any recommendations for revising the service blueprint or touchpoints to fit reality

## Guardrails

- Do not optimize for agreement by hiding hard tradeoffs
- Do not treat operational constraints as after-the-fact implementation detail
- Do not mark a service as ready if ownership or metrics are still unclear
