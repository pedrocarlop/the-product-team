---
name: harden
description: Strengthen an interface against edge cases, failure states, localization pressure, and real-world data conditions so it remains reliable outside ideal demos.
---

# Harden

Use this skill to make a UI spec or implementation resilient under messy, production-grade conditions.

## When to Use

- When a surface needs full state coverage beyond the happy path
- When text overflow, localization, permissions, loading, or error handling are known risks
- When a design works in ideal conditions but is fragile with real content or real failures

## How to Use

Stress the interface with long and short text, empty and oversized data, slow or failed requests, validation errors, restricted permissions, destructive actions, and locale expansion. Check how the surface behaves when assumptions break, not just when everything is populated and successful.

Translate weaknesses into explicit requirements: fallback states, wrapping behavior, resilient layout rules, recovery paths, and implementation constraints. If a state is important enough to ship, it is important enough to specify.

## What to Produce

- A hardening checklist covering edge cases, failure paths, and content extremes
- Specific resilience requirements for layout, copy, state coverage, and implementation behavior
- A punch list of fragile points that must be resolved before release

## Notes for Design Technologist

Hardening is not adding exceptions after the fact. It is making the core interface durable enough to survive normal product reality.
