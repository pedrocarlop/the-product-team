---
name: surface
description: Specify service touchpoints across digital, human, and physical surfaces so each interaction is owned, legible, and consistent within the broader service experience.
activation_hints:
  - "Use when documenting or redesigning touchpoints, status updates, notifications, or service surfaces across channels."
  - "Route here for channel-specific interaction specs that need to fit into a larger service blueprint."
  - "Do not use for abstract service strategy without a concrete user-facing surface."
---

# Surface

## Purpose

Use this skill to define what each touchpoint should communicate, how it behaves, who owns it, and how it fits into the surrounding service journey.

## When to Use

- When the service depends on emails, SMS, calls, dashboards, confirmations, or support interactions
- When a touchpoint needs channel-specific interaction rules
- When multiple surfaces must speak with one consistent service voice
- When a screen, notification, or human interaction is part of a longer service process

## When Not to Use

- When the task is only to redesign one isolated screen
- When the main problem is backstage logic with no user-facing surface
- When there is no concrete touchpoint to specify

## Required Inputs

- The touchpoints in scope and the channel for each one
- The user goal and emotional state at each surface
- Ownership, timing, and operational dependency for each touchpoint
- Failure and waiting states that the surface must communicate
- Any content or interaction constraints specific to the channel

## Workflow

1. List the touchpoints in the order users encounter them.
2. Describe the purpose of each surface and the state it communicates.
3. Define who owns the surface and what triggers it.
4. Specify the behavior for loading, success, error, delay, and escalation states.
5. Check for channel drift, duplicated messages, or missing context between surfaces.
6. Confirm the touchpoint still makes sense inside the broader service blueprint.

## Design Principles / Evaluation Criteria

- Channel fit over one-size-fits-all messaging
- Clear state communication over ambiguous status
- Ownership and timing over generic availability
- Consistency across surfaces over local optimization
- Recovery guidance over dead-end notification

## Output Contract

- A touchpoint specification for each surface with channel, purpose, owner, state behavior, and timing
- Notes on content, interaction, or operational constraints
- Any dependencies that should be reviewed with support or operations

## Guardrails

- Do not design touchpoints in isolation from the service flow
- Do not omit non-digital surfaces when they matter to the experience
- Do not treat notifications as decorative add-ons rather than service infrastructure
