---
name: blueprint
description: Create or revise end-to-end service blueprints that map customer actions, frontstage interactions, backstage processes, and support systems across the full journey.
---

# Blueprint

## Purpose

Use this skill to define the full service experience so the team can see how a user request moves through channels, people, systems, and backstage work from start to finish.

## When to Use

- When the experience spans digital, human, and operational touchpoints
- When a flow depends on support teams, fulfillment, notifications, callbacks, or manual review
- When the goal is to document the service as a system rather than just a user interface

## When Not to Use

- When the task is only about one screen, one component, or one copy string
- When the main need is UI layout rather than service orchestration
- When the artifact is a pure implementation spec without backstage concern

## Required Inputs

- The service goal and the user moment being designed
- Known touchpoints, channels, and supporting teams or systems
- Current-state evidence or assumptions about backstage behavior
- Constraints such as latency, ownership, policy, or compliance
- Any screenshots, notes, or source materials that show the current journey

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

1. Define the service boundary: where the experience starts, where it ends, and what counts as resolution.
2. Map user actions in order, including the moments when the user leaves the product.
3. Add frontstage interactions for each step, covering digital, human, and physical touchpoints.
4. Identify backstage processes, systems, and ownership transitions that make each step possible.
5. Mark failure modes, waits, escalation paths, and recovery points explicitly.
6. Verify that the blueprint can be handed to operations, product, and design without extra interpretation.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Full journey over isolated steps
- Backstage visibility over implied process
- Clear ownership over vague collaboration
- Failure states alongside happy paths
- Operational realism over idealized flow

## Output Contract

- A service blueprint or journey map that shows customer actions, frontstage interactions, backstage work, and support systems
- Notes on the most important handoffs, delays, and failure modes
- Any assumptions that should be validated with operations or stakeholders

## Guardrails

- Do not collapse backstage work into a generic "internal process" box
- Do not omit handoffs between teams, channels, or systems
- Do not present a digital-only journey as a complete service blueprint

## Optional Tools / Resources

- Notion MCP, Figma MCP, and Chrome DevTools MCP for journey evidence and service mapping
- [Service Design Network](https://www.service-design-network.org/)
- [Miro Service Blueprint templates](https://miro.com/templates/service-blueprint/)
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Dovetail](https://dovetail.com/)
- [IDEO design resources](https://www.ideo.com/journal)
