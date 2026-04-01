---
name: compose
description: Compose mobile screens, components, and interaction states from approved app patterns, tokens, and platform conventions.
---

# Compose

## Purpose

Use this skill to assemble mobile UI from approved building blocks so the result is clear, reusable, and aligned with platform conventions.

## When to Use

- When a new mobile screen, component, or pattern needs to be defined
- When variants, states, or responsive behaviors need to be organized coherently
- When existing mobile pieces need to be recomposed into a cleaner structure
- When navigation, layout, or interaction anatomy needs to be clarified before implementation

## When Not to Use

- When the main task is translating a design into code
- When the problem is platform adaptation for accessibility or device constraints
- When the work is about release safety, testing, or rollout planning

## Required Inputs

- The user task and mobile product goal
- Available design tokens, primitives, and shared components
- Required states, variants, and interaction behaviors
- Device, platform, and viewport constraints
- Nearby mobile patterns that should be reused or referenced

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: engineer
project: <slug>
deliverable: engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Confirm whether the request is for a screen, component, composite pattern, or extension of an existing mobile asset.
2. Map the anatomy and separate fixed, optional, and variant-driven parts.
3. Compose the UI from approved tokens and reusable primitives only.
4. Define states, behavior, and composition rules so the pattern can be reused consistently.
5. Check for overlap with existing mobile patterns and remove unnecessary duplication.
6. Verify that the result can be implemented, documented, and tested without ambiguity.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Composition should express intent, not just visual arrangement
- Reuse should come before novelty when a shared pattern already exists
- Variants should stay bounded and understandable
- Anatomy should be explicit enough for design and code alignment
- The pattern should strengthen the mobile system vocabulary, not widen it casually

## Output Contract

- A mobile screen or component definition with anatomy, states, and variants
- Notes on token dependencies and composition rules
- Reuse or deprecation notes for related mobile assets
- Any open implementation or accessibility questions that still need follow-up

## Guardrails

- Do not create one-off structure when an existing pattern already covers the need
- Do not hide missing behavior inside undocumented local exceptions
- Do not make variants so broad that they become separate components in disguise
- Do not compose against raw values when approved tokens exist
- Do not skip accessibility or interaction states because the surface is mostly static

## Optional Tools / Resources

- MCP: GitHub MCP, Notion MCP, Sentry MCP, Figma MCP
- Websites: [Apple Developer Documentation](https://developer.apple.com/documentation/), [Android Developers](https://developer.android.com/), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines), [Material Design](https://m3.material.io/), [Flutter Docs](https://docs.flutter.dev/)
- Figma MCP for component authoring and structure review
- Existing mobile design system components or pattern libraries
- Storybook, component previews, or simulator screenshots
- Accessibility references and interaction specs
