---
name: ground
description: Ground decisions in the actual target repository and any named source-system or design-system repositories before proposing new behavior.
---

# Ground

## Purpose

Use this skill to establish a factual baseline from the real repository context. The goal is to identify existing conventions, constraints, and vocabulary so later decisions are based on evidence instead of memory or assumption.

## When to Use

- When a request mentions an unfamiliar feature area, component, or module
- When the target repository may already have an approved pattern we should follow
- When a named source-system or design-system repository has been provided and must be checked directly
- When the right next step is discovery, not writing

## When Not to Use

- When the task is to implement a known change
- When the task is to review a finished artifact for correctness
- When the request is purely about drafting copy, policy, or strategy without repo context

## Required Inputs

- The target repository or workspace to inspect
- Any named external repository, design system, or source system to compare against
- The feature, area, or decision that needs grounding
- Any explicit constraints, version pins, or known non-negotiables

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

1. Identify the exact area that needs grounding and name the decision being made.
2. Inspect the target repository for established patterns, terminology, and nearby examples.
3. Inspect any named external repository or design system directly, if one was provided.
4. Record the relevant facts, including any gaps, contradictions, or missing context.
5. Distinguish observed evidence from inference so later work can reuse the facts safely.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Grounding should come from the closest authoritative source available
- Existing patterns outrank invented abstractions
- Conflicts should be surfaced, not smoothed over
- Evidence should be specific enough that another person can trace it back

## Output Contract

- A concise inventory of the patterns, constraints, and vocabulary that were found
- The source location for each important observation
- A clear list of unknowns, conflicts, or assumptions that remain

## Examples

### Example 1

Input:
- Task: Add a new settings screen
- Context: The repo already has multiple account settings pages

Expected output:
- Grounding summary: The app uses a shared settings shell, a common section header style, and route-level feature flags
- Evidence: `src/settings/Shell.tsx`, `src/settings/sections/*`
- Unknowns: No existing pattern for destructive account actions

## Guardrails

- Do not assume a pattern exists without checking the codebase
- Do not merge target-repo behavior with external-repo behavior unless both are verified
- Do not hide uncertainty behind generic language
- Do not turn grounding work into implementation work

## Optional Tools / Resources

- MCP: Notion MCP, GitHub MCP
- Websites: [MDN Web Docs](https://developer.mozilla.org/), [DevDocs](https://devdocs.io/), [GitHub Docs](https://docs.github.com/), [RFC Editor](https://www.rfc-editor.org/), [IETF Datatracker](https://datatracker.ietf.org/)
- Repository search and file-tree inspection
- Design-system docs or component libraries
- Source-system repositories named in the request
- Architecture notes, README files, and feature docs
