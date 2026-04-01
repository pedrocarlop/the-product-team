---
name: profile
description: Measure real-user and lab performance to identify the bottleneck before optimizing.
---

# Profile

## Purpose

Use this skill to establish what is slow, where the slowness appears, and which metric best represents the user impact.

## When to Use

- When the request is vague, such as "this feels slow" or "performance regressed"
- When we need a baseline before changing code, assets, or infrastructure
- When we need to compare real-user data with lab data and understand the gap

## When Not to Use

- When the bottleneck has already been proven and the task is to remediate it
- When the work is purely budget-setting or CI gate wiring
- When the problem is clearly non-performance, such as a functional bug or content issue

## Required Inputs

- The surface being measured, such as a route, endpoint, interaction, or device class
- The symptom or metric that triggered the investigation
- Any available traces, RUM data, Lighthouse reports, or WebPageTest runs
- The success threshold or budget we are trying to meet

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: platform-engineer
project: <slug>
deliverable: platform-engineer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Clarify whether we are looking at field data, lab data, or both.
2. Pick the narrowest metric that matches the user pain, not just the easiest number to collect.
3. Record a baseline on representative hardware or traffic conditions.
4. Identify the primary metric pattern, such as LCP, INP, CLS, TTFB, bundle size, or p99 latency.
5. Capture enough context to compare before and after later.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Measure the user experience, not just the implementation
- Prefer representative devices and traffic over ideal local conditions
- Use one primary metric and a small set of supporting metrics
- Keep the baseline reproducible

## Output Contract

- The metric being tracked
- The measurement method and environment
- The baseline value and any notable context
- The next investigation step, if the bottleneck is still unclear

## Guardrails

- Do not optimize from intuition alone
- Do not report a lab score as if it were field reality
- Do not widen the scope before the baseline is captured

## Optional Tools / Resources

- MCP: Chrome DevTools MCP, GitHub MCP, Sentry MCP, Notion MCP
- Websites: [web.dev Performance](https://web.dev/explore/fast), [Chrome for Developers / Performance](https://developer.chrome.com/docs/performance), [Lighthouse Docs](https://developer.chrome.com/docs/lighthouse/overview), [Sentry Performance Docs](https://docs.sentry.io/product/performance/), [Node.js Diagnostics](https://nodejs.org/en/learn/diagnostics)
- Browser traces and profiling captures
- Benchmark baselines and lab or field data
- Release regressions or incident notes
