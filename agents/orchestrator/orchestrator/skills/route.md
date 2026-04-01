---
name: route
description: "Decide whether a request should be handled via direct execution or routed into the multi-agent workflow. Use at the start of every new request. Determines the execution mode, creates the project context, and appends to the timeline."
---

# Route

## Overview

The first checkpoint on every request. Route decides whether the orchestrator should execute the work directly (single-domain, low ambiguity) or spin up a multi-agent workflow (cross-functional, ambiguous, review-gated). A poor routing decision cascades waste — over-routing burns tokens and latency, under-routing produces shallow work.

## When to Use

- At the start of every new request — no exceptions.
- When a mid-cycle change materially shifts the domain or scope.
- When a specialist returns a mismatch that implies a different routing decision was needed.

## When Not to Use

- Mid-execution within an already-routed workflow (use `coordinate` instead).
- When the user is asking a clarifying question, not requesting work.

## Prerequisites

- The user's request is clear enough to classify (if not, ask first).
- `logs/TIMELINE.md` is accessible for past-project lookup.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Understand the Request

Read the user's request and extract:
- **Objective**: what the user wants to exist when this is done.
- **Constraints**: timeline, tech stack, quality bar, scope boundaries.
- **Ambiguity level**: are the requirements specific enough to act on, or do they need discovery?
- **Likely deliverables**: code, design specs, analysis, documentation, plans.

### Step 2: Check Project History

Read `logs/TIMELINE.md`. Look for:
- Active projects this request might continue or extend.
- Past projects with similar domain that reveal useful context.
- If this is clearly a continuation, reuse the existing project slug and `context.md`.

### Step 3: Classify the Domain

Classify likely domain(s) first. Determine the primary domain(s) without reading the full role catalog:

| Signal | Likely Domain |
|--------|--------------|
| Mentions code, implementation, bugs, tests | `engineer` or `platform-engineer` |
| Mentions UI, layout, flow, wireframe, usability | `designer` |
| Mentions tokens, components, design system | `design-systems` |
| Mentions strategy, roadmap, PRD, prioritization | `product-lead` |
| Mentions metrics, forecasting, revenue, data | `analyst` |
| Mentions growth, positioning, launch, partnerships | `go-to-market` |
| Mentions process, operations, coordination | `business-ops` |
| Mentions review, quality, validation, audit | `reviewer` |

If the task maps cleanly to **one domain** → likely direct execution.
If the task spans **two or more domains** → likely orchestration.

### Step 4: Apply the Routing Decision Tree

```
Is the task single-domain?
├── YES → Is it clearly scoped (requirements are specific)?
│   ├── YES → Is specialist staffing needed to materially improve outcome?
│   │   ├── YES → ORCHESTRATE (single specialist)
│   │   └── NO → DIRECT EXECUTION
│   └── NO → Does it need discovery or planning before execution?
│       ├── YES → ORCHESTRATE (with discovery phase)
│       └── NO → DIRECT EXECUTION (with reasonable assumptions)
└── NO → Does it need cross-functional coordination?
    ├── YES → ORCHESTRATE (multi-role)
    └── NO → Can it be decomposed into independent single-domain tasks?
        ├── YES → DIRECT EXECUTION (sequential single-domain)
        └── NO → ORCHESTRATE (multi-role)
```

### Step 5: Estimate Coordination Cost

Before committing to orchestration, estimate the cost:
- **Direct execution**: ~1 agent turn, fast, low overhead.
- **Single specialist**: ~2 turns (assign + execute), moderate overhead.
- **Multi-role orchestration**: ~4-8 turns (plan + approve + execute + review), significant overhead.

Only orchestrate when the coordination benefit **clearly exceeds** the token and latency cost. Simple tasks with orchestration overhead feel slow and wasteful.

### Step 6: Create the Project Context

Create `logs/active/<project-slug>/context.md` with:

```markdown
# <Project Title>

## Objective
<What the user wants to exist when this is done>

## Constraints
<Timeline, tech stack, quality bar, scope boundaries>

## Routing Decision
<Direct execution | Single specialist | Multi-role orchestration>
<1-sentence justification>

## Done When
<Concrete, verifiable completion criteria>
- <criterion 1>
- <criterion 2>
- ...

## Status
Routed — <execution mode>
```

Append a row to `logs/TIMELINE.md`:
```
| <date> | <project-slug> | <1-line description> | active |
```

## Worked Examples

### Example 1: Trivial Direct Execution
**Request:** "Fix the typo in the login button — it says 'Sing In' instead of 'Sign In'"

**Routing:**
- Single domain: `engineer` (frontend).
- Clearly scoped: fix one string.
- Specialist staffing would not improve outcome.
- → **Direct execution.** Fix the typo directly.

### Example 2: Single Specialist
**Request:** "Write a PRD for adding team workspaces to the app"

**Routing:**
- Single domain: `product-lead`.
- Ambiguous: needs discovery and structuring.
- Specialist staffing would materially improve outcome (PRD quality).
- → **Orchestrate with `product-lead`.**

### Example 3: Multi-Role Orchestration
**Request:** "Design and implement a new onboarding flow with analytics tracking"

**Routing:**
- Multiple domains: `designer` (UX + UI), `engineer` (implementation), `analyst` (analytics).
- Cross-functional coordination needed.
- → **Orchestrate with multi-role team.** Seek approval before execution.

## Guardrails

- Do not load the full `references/role-catalog.md` for obvious single-domain tasks — classify from context first.
- Do not default to orchestration out of caution — direct execution is the default.
- Do not skip creating `context.md` even for direct execution — it enables continuity.
- Do not begin substantial multi-role execution before explicit user approval.
- Do not route to "reference" — it is a helper archetype, not staffable.
- Do not re-route mid-cycle without explicitly pausing and resetting.

## Troubleshooting

### Issue: Task seems to span multiple domains but is actually simple
**Cause:** Keywords from multiple domains are present but the actual work is single-domain.
**Solution:** Focus on the deliverable, not the keywords. "Build a landing page with analytics" is primarily `engineer` work — instrumentation is a detail, not a separate domain.

### Issue: Routing changes after execution starts
**Cause:** New information during execution reveals the initial routing was wrong.
**Solution:** Pause execution, update `context.md` with the new understanding, re-route explicitly. Do not silently add or remove specialists.

### Issue: User request is too vague to route
**Cause:** Missing objective, scope, or constraints.
**Solution:** Ask one focused clarifying question before routing. Do not guess the scope — a wrong guess wastes more time than a quick question.
