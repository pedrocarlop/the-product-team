---
name: apply-patch
tool: apply_patch
description: Write the service design package — blueprints, journey maps, cross-channel touchpoint specs, and backstage process documentation.
---

# Apply Patch

Use this skill to write the four service design artifacts. Service design output must map the full end-to-end experience — not just the digital surface, but the backstage processes and cross-channel touchpoints that support it.

## When to Use

- After completing service research and journey mapping
- When writing the service blueprint in `task-flows.md` (swim-lane format covering customer actions, frontstage, backstage, and support processes)
- When documenting cross-channel touchpoints and handoff moments in `ui-spec.md`
- When revising artifacts in response to reviewer feedback

## How to Use

Invoke `apply_patch` targeting the correct output file path:

- **research-and-rationale.md**: Current-state service analysis, pain points at handoff moments, and the design rationale for the proposed service changes
- **task-flows.md**: Full service blueprint — customer journey, frontstage (digital and human), backstage (systems and processes), and support touchpoints
- **ui-spec.md**: Specification of each touchpoint — channel, interaction type, responsible party, latency expectations, and failure modes
- **component-mapping.md**: Digital touchpoint components mapped to `CMP-*` entries; non-digital touchpoints documented as service components

## What to Produce

Every service blueprint must cover:
- Customer-facing journey steps from first touchpoint to resolution
- Backstage triggers — what system or human action each frontstage step depends on
- Failure modes — what happens when a backstage process fails
- Handoff moments — explicit ownership transitions between channels or teams

## Notes for Service Designer

A service blueprint that only maps the digital journey is incomplete. Every handoff moment between digital, human, and automated backstage processes must be explicitly documented.
