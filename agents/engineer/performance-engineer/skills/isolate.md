---
name: isolate
description: Narrow a performance issue to the browser, network, backend, or dependency causing it.
activation_hints:
  - "Use when a baseline exists and we need the root cause."
  - "Use when traces, flame graphs, or waterfalls are available."
  - "Do not use for setting targets or verifying a finished fix."
---

# Isolate

## Purpose

Use this skill to identify the specific layer, component, or request that is responsible for the slowdown.

## When to Use

- When profiling has shown that a performance issue exists
- When the fix path depends on whether the problem is in the browser, network, or backend
- When several plausible causes exist and we need to rule them in or out

## When Not to Use

- When no baseline has been taken yet
- When the task is just to codify a budget or acceptance threshold
- When the root cause has already been proven and the work is remediation

## Required Inputs

- The relevant trace, flame graph, waterfall, heap snapshot, or APM data
- The metric that is degraded
- Any recent code, dependency, or infrastructure changes
- The most likely candidate layers or components

## Workflow

1. Break the issue into browser, network, backend, caching, and asset-delivery hypotheses.
2. Inspect the highest-signal trace or graph first.
3. Eliminate false leads by comparing timings, spans, or request order.
4. Trace the cost to the smallest responsible unit, such as a function, query, image, or third-party script.
5. Note any secondary effects that could matter during the fix.

## Design Principles / Evaluation Criteria

- Isolate the cause, not just the symptom
- Use evidence that matches the layer being investigated
- Prefer the smallest accountable unit
- Keep the diagnosis reproducible enough that another person could confirm it

## Output Contract

- The most likely root cause
- The evidence that supports it
- The layer or component boundary where the issue lives
- Any remaining uncertainty or alternate explanations

## Guardrails

- Do not guess based on code reading alone when traces are available
- Do not jump to a fix before ruling out adjacent layers
- Do not collapse multiple possible causes into one unsupported conclusion
