---
name: trace
description: Trace features, patterns, and decisions through the codebase so the real implementation path is understood end to end.
---

# Trace

## Purpose

Use this skill to follow a concept through the repository until the implementation path is clear. Tracing helps reveal where a behavior starts, how it moves, what depends on it, and where a change would actually land.

## When to Use

- When a feature spans multiple files, layers, or packages
- When you need to locate the source of truth for a value, prop, setting, or state transition
- When you need to understand why an implementation behaves a certain way
- When a decision depends on where a pattern originates and how it propagates

## When Not to Use

- When the task is only to gather existing conventions at a high level
- When the answer is already obvious from a single file
- When the task is implementation or validation after the path is understood

## Required Inputs

- The feature, symbol, or behavior to trace
- Any known entry point, identifier, or file if one exists
- The scope boundaries for the trace, such as package, app surface, or platform
- Any symptoms, anomalies, or decision points that motivated the trace

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: reference
project: <slug>
deliverable: reference.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Start from the strongest known anchor point, such as a route, component, helper, or config key.
2. Follow imports, calls, props, events, and data transformations outward until the path is clear.
3. Separate source-of-truth locations from derived or mirrored values.
4. Note any branching behavior, conditional handling, or environment-specific paths.
5. Summarize the trace as a chain of evidence, not as a guess about intent.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- A trace should explain how the behavior works, not just where it appears
- The shortest correct path is better than a broad but vague inventory
- Source-of-truth locations matter more than every intermediate hop
- Traces should make future reuse or change safer

## Output Contract

- The starting point and the full traced path
- Source-of-truth locations versus derived locations
- Any branching conditions, variants, or edge cases found along the way

## Examples

### Example 1

Input:
- Behavior: Loading state shown on checkout
- Anchor: Checkout route

Expected output:
- Trace summary: Route -> page container -> data hook -> request client -> loading state renderer
- Source of truth: `useCheckoutState`
- Notes: Mobile uses the same hook but a different skeleton component

## Guardrails

- Do not stop at the first matching reference if the real source of truth lives elsewhere
- Do not collapse multiple branches into one path when the code distinguishes them
- Do not infer behavior from naming alone
- Do not widen the trace beyond the needed scope unless a dependency forces it

## Optional Tools / Resources

- MCP: Notion MCP, GitHub MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [DevDocs](https://devdocs.io/), [GitHub Docs](https://docs.github.com/), [RFC Editor](https://www.rfc-editor.org/), [IETF Datatracker](https://datatracker.ietf.org/)
- Repository search and symbol lookup
- Call graphs, import graphs, and route maps
- Debug logs, tests, and storybook examples
- Architecture notes and change history
