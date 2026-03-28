---
name: animate
description: Add purposeful motion and micro-interactions that improve feedback, orientation, and perceived quality without harming performance or accessibility.
---

# Animate

Use this skill to define motion for a feature, flow, or component set that needs clearer feedback or a stronger sense of responsiveness.

## When to Use

- When state changes feel abrupt, unclear, or lifeless
- When a surface needs micro-interactions, transition behavior, or loading motion
- When motion can improve understanding, feedback, or delight for a key task

## Required Inputs

- The user action or system event that triggers each motion moment
- The exact elements and states involved before and after the change
- The communication goal for each motion moment
- Timing budget, interruption rules, and performance constraints
- Reduced-motion expectations and accessibility constraints

## How to Use

Start with the communication goal for each motion moment: confirming an action, guiding attention, preserving spatial continuity, or reducing perceived wait time. Limit motion to the moments that matter most, then define the trigger, duration, easing, delay, and interruption behavior for each one.

Check every proposed animation against performance and accessibility constraints. Reduced-motion fallbacks and compositor-friendly motion behavior are part of the spec, not optional extras.

For every motion moment, specify the concrete behavior instead of naming a vibe. Say what moves, what stays still, which properties change, when the motion starts, how it ends, what interrupts it, and what the user should understand because of it.

## Workflow

1. List the exact motion moments in the interaction.
2. For each one, name the trigger, affected elements, before state, and after state.
3. Specify the motion properties, duration, easing, delay, sequencing, and completion state.
4. Define interruption, cancellation, and reverse behavior where relevant.
5. Note implementation constraints such as compositor-safe properties, maximum duration, and no-blocking-input requirements.
6. Define the reduced-motion fallback and confirm the meaning still survives.

## What to Produce

- A motion spec for each prioritized transition or micro-interaction with trigger, affected elements, before and after states, changed properties, duration, easing, delay, sequencing, and interruption rules
- Reduced-motion behavior and any implementation constraints that must be respected
- Acceptance notes describing what users should perceive and what must not happen

## Notes for Motion Designer

Motion is successful when it clarifies the interface before users consciously notice it. Decorative animation that competes with the task is a design defect, not a flourish.

If engineering could read your motion spec and still ask "what exactly animates?", the spec is not detailed enough.

## Optional Tools / Resources

- Figma MCP, Chrome DevTools MCP, and Paper MCP for motion references and prototype review
- [Motion](https://motion.dev/)
- [LottieFiles](https://lottiefiles.com/)
- [Material Design motion guidance](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [After Effects](https://www.adobe.com/products/aftereffects.html)
