---
name: staff
description: "Select the minimum viable role set for an orchestrated task, assign ownership, and set reasoning calibration. Use after routing decides orchestration is needed, or when a staffed role may be redundant, missing, or incorrectly assigned."
---

# Staff

## Overview

Staff work deliberately with the minimum viable team. Every added role costs tokens, latency, and coordination overhead. This skill provides a structured approach to deciding which roles are needed, what they own, and how much reasoning effort each should apply.

## When to Use

- After `route` decides orchestration is needed.
- When adjusting the team mid-cycle (specialist mismatch, new scope).
- When unsure whether a reviewer or additional specialist adds value.

## When Not to Use

- For direct execution — no staffing needed.
- When re-running a previously approved staffing decision without scope change.

## Prerequisites

- Routing decision is made (direct vs orchestrated).
- `context.md` exists with objective, constraints, and done-when criteria.
- The domain classification from `route` is available.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Identify Required Capabilities

From the `context.md` objective and done-when criteria, list the **capabilities** needed:

| Capability Needed | Maps to Role |
|-------------------|-------------|
| UI/UX flows, wireframes, visual design, content | `designer` |
| Token architecture, component library, design governance | `design-systems` |
| Frontend, backend, fullstack, mobile, ML implementation | `engineer` |
| API design, database, infrastructure, security, architecture | `platform-engineer` |
| Product strategy, discovery, PRD, prioritization | `product-lead` |
| Metrics, financial modeling, forecasting | `analyst` |
| Growth, marketing, positioning, partnerships, customer success | `go-to-market` |
| Process mapping, operational systems, coordination | `business-ops` |
| Cross-discipline validation, quality gates | `reviewer` |

### Step 2: Apply the Minimum Viable Team Test

For each candidate role, ask:

```
Would removing this role materially degrade the outcome?
├── YES → Staff it.
└── NO → Don't staff it.
```

**Key heuristics:**

- **One role = one subagent.** Never double-staff the same capability.
- **Skip reviewer** unless the task has high risk (production deployment, user-facing copy, cross-team impact) and a review pass would catch something the executor would miss.
- **Skip product-lead** if requirements are already specified by the user — don't add discovery overhead to execution-ready tasks.
- **Skip designer** if the UI is fully specified (Figma ready, design system established) — `engineer` can translate directly.
- **Skip analyst** unless the task requires _building_ metrics or models, not just using existing data.

### Step 3: Set Skill Hints

For each staffed role, optionally include a `skill_hint` listing which discipline groups are most relevant. This helps the specialist start focused:

```
engineer (skill_hint: frontend/translate, frontend/stateful)
designer (skill_hint: ux/flow, ui/stateful)
```

Only include hints when the discipline is non-obvious. If the task clearly maps to one discipline, the specialist will find it themselves.

### Step 4: Calibrate Reasoning Effort

Not every task needs maximum reasoning. Set `model_reasoning_effort` per role:

| Task Characteristics | Reasoning Level | When |
|---------------------|----------------|------|
| Well-scoped, single-domain, low ambiguity | `medium` | Fix a bug, add a field, write copy, extend a component |
| Multi-step, some ambiguity, cross-cutting | `high` | Feature implementation, architecture decisions, complex design |
| Genuinely hard, long-horizon, high autonomy | `high` | System redesign, novel algorithms, multi-phase migration |

Default to `medium` for straightforward tasks. Reserve `high` for tasks where overthinking actually helps.

### Step 5: Define Ownership and Sequencing

For each staffed role, specify:
- **Owns**: what artifacts and decisions this role is accountable for.
- **Reads from**: what upstream deliverables this role consumes.
- **Blocked by**: what must complete before this role starts (if sequential).

```
Example:
  designer:
    owns: deliverables/designer.md
    reads from: context.md
    blocked by: nothing (can start immediately)
  
  engineer:
    owns: deliverables/engineer.md, working code
    reads from: context.md, deliverables/designer.md
    blocked by: designer (needs design specs first)
```

### Step 6: Update Context

Write the staffing decision to `logs/active/<project-slug>/context.md`:

```markdown
## Staffing
| Role | Skill Hint | Reasoning | Owns |
|------|-----------|-----------|------|
| <role> | <hint or —> | <medium/high> | <deliverable> |

## Sequencing
<sequential / parallel / mixed>
<brief description of execution order>
```

## Worked Examples

### Example 1: Simple Feature Implementation
**Task:** "Add a dark mode toggle to the settings page"

**Staffing:**
- `engineer` (skill_hint: frontend/translate, frontend/stateful) — reasoning: medium
- No designer needed — toggle is a standard pattern.
- No reviewer needed — low risk, one-page change.

**Team size:** 1 role.

### Example 2: New Feature with Design
**Task:** "Build a team workspaces feature with invite flow"

**Staffing:**
- `designer` (skill_hint: ux/flow, ux/wire, ui/stateful) — reasoning: high
- `engineer` (skill_hint: fullstack/model, fullstack/wire) — reasoning: high
- `platform-engineer` (skill_hint: api/shape, database/schema) — reasoning: high

**Sequencing:** designer → engineer + platform-engineer (parallel) → orchestrator review.
**Team size:** 3 roles.

### Example 3: Analytics Dashboard
**Task:** "Create a metrics dashboard showing MRR, churn, and cohort retention"

**Staffing:**
- `analyst` (skill_hint: data/frame, data/measure) — reasoning: medium
- `engineer` (skill_hint: frontend/translate) — reasoning: medium

**Sequencing:** analyst defines metrics → engineer implements the dashboard.
**Team size:** 2 roles.

### Example 4: Launch Readiness
**Task:** "Prepare for public launch: landing page, docs, monitoring, go-to-market plan"

**Staffing:**
- `designer` (skill_hint: ui/frontend-design) — reasoning: high
- `engineer` (skill_hint: frontend/translate) — reasoning: high
- `platform-engineer` (skill_hint: devops/observe, devops/release) — reasoning: high
- `go-to-market` (skill_hint: product-marketing/launch, marketing/position) — reasoning: medium
- `reviewer` — reasoning: high (high-risk, user-facing)

**Sequencing:** designer + go-to-market (parallel) → engineer + platform-engineer (parallel) → reviewer.
**Team size:** 5 roles. Seek user approval — this is substantial.

## Guardrails

- Do not staff more than 3 roles without explicit user approval — the cost is significant.
- Do not staff `reviewer` by default — only when review materially reduces risk.
- Do not staff roles based on task keywords alone — match to actual capability needs.
- Do not staff `reference` — it is a helper archetype, not an autonomous agent.
- Do not require specialist advisory plans by habit — only when ambiguity genuinely demands them.
- Do not duplicate capabilities across roles — if `engineer` can handle API work for a feature, don't also staff `platform-engineer`.

## Troubleshooting

### Issue: Specialist returns a mismatch
**Cause:** The task was assigned to the wrong role or the skill hint was off.
**Solution:** Re-evaluate the capability mapping. Adjust the staffed role or reassign. Update `context.md`.

### Issue: Work feels over-staffed
**Cause:** Roles were added for completeness rather than need.
**Solution:** Apply the minimum viable team test again. Remove any role where the answer to "would removal degrade the outcome?" is no.

### Issue: Sequencing creates unnecessary delays
**Cause:** Roles that could work in parallel are chained sequentially.
**Solution:** Parallelize when outputs don't depend on each other. Designer and analyst can often run in parallel. Engineer and platform-engineer can often run in parallel after shared planning.

### Issue: Reasoning effort doesn't match task
**Cause:** All roles defaulted to `high` reasoning.
**Solution:** Apply the calibration table. Simple, well-scoped tasks perform better with `medium` — less overthinking, faster turnaround.
