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

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: orchestrator
project: <slug>
deliverable: orchestrator.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

### Step 2: Identify Required Capabilities (Role Discovery)

Instead of hardcoded mapping, the Orchestrator must "scan" the specialized **Capability Cards** located at `agents/<domain>/<role>/capabilities.md`.

Match the project objective against these cards:

| Domain | Role | Card Path |
|--------|------|-----------|
| Business | `product-lead`, `analyst`, `go-to-market`, `business-ops` | `agents/business/<role>/capabilities.md` |
| Design | `designer`, `design-systems` | `agents/design/<role>/capabilities.md` |
| Engineering | `engineer`, `platform-engineer` | `agents/engineer/<role>/capabilities.md` |
| Review | `reviewer` | `agents/review/<role>/capabilities.md` |

**Verification**: Only staff a role if its **Purpose** and **Managed Skills** in the `capabilities.md` card directly align with the task.

### Step 3: Apply the Minimum Viable Team Test

For each candidate role, ask:

```
Would removing this role materially degrade the outcome?
├── YES → Staff it.
└── NO → Don't staff it.
```

**Key heuristics:**

- **One role = one subagent.** Never double-staff the same capability.
- **Skip reviewer** unless the task has high risk (production deployment, user-facing copy, cross-team impact).
- **Skip product-lead** if requirements are already specified by the user.

### Step 4: Set Skill Hints

For each staffed role, include a `skill_hint` linking to a specific skill group from their `capabilities.md` (e.g., `designer (skill_hint: ux/flow)`).

### Step 5: Calibrate Reasoning Effort (OpenAI Tiering)

Align reasoning effort with task complexity. **The Orchestrator always uses `high` reasoning for planning.**

| Task Characteristics | Reasoning Level | When |
|---------------------|----------------|------|
| Well-scoped, low ambiguity | `medium` | Fix a bug, add a field, write copy |
| Multi-step, cross-cutting | `high` | Feature implementation, architecture, complex design |
| High autonomy, novel | `high` | System redesign, multi-phase migration |

Default to `medium` for simple execution tasks. Reserve `high` for planning and high-stakes reasoning.

### Step 6: Define Ownership and Sequencing

For each staffed role, specify:
- **Owns**: what artifacts and decisions this role is accountable for.
- **Reads from**: what upstream deliverables this role consumes.
- **Blocked by**: what must complete before this role starts (if sequential).
- **Repo write authority**: whether this role may edit repo-tracked code for the current stage. Default is `none`. Assign a single explicit repo-write owner per stage unless you deliberately split disjoint scopes.

```
Example:
  designer:
    owns: deliverables/designer.md
    reads from: context.md
    blocked by: nothing (can start immediately)
    repo writes: none
  
  engineer:
    owns: deliverables/engineer.md, working code
    reads from: context.md, deliverables/designer.md
    blocked by: designer (needs design specs first)
    repo writes: explicit owner for app code in `app/settings/**`
```

### Step 7: Update Context

Write the staffing decision to `logs/active/<project-slug>/context.md`:

```markdown
### Step 8: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Staffing
| Role | Skill Hint | Reasoning | Owns | Repo Writes |
|------|-----------|-----------|------|-------------|
| <role> | <hint or —> | <medium/high> | <deliverable> | <none / explicit owner + scope> |

## Sequencing
<sequential / parallel / mixed>
<brief description of execution order>
```

## Worked Examples

### Example 1: Simple Feature Implementation
**Task:** "Add a dark mode toggle to the settings page"

**Staffing:**
- `engineer` (skill_hint: frontend/translate, frontend/stateful) — reasoning: medium
- `engineer` is the only repo-write owner for this stage.
- No designer needed — toggle is a standard pattern.
- No reviewer needed — low risk, one-page change.

**Team size:** 1 role.

### Example 2: New Feature with Design
**Task:** "Build a team workspaces feature with invite flow"

**Staffing:**
- `designer` (skill_hint: ux/flow, ux/wire, ui/stateful) — reasoning: high
- `engineer` (skill_hint: fullstack/model, fullstack/wire) — reasoning: high
- `platform-engineer` (skill_hint: api/shape, database/schema) — reasoning: high

**Repo writes:**
- `engineer` owns feature code in the app surface.
- `platform-engineer` may own repo writes only if the orchestrator assigns a disjoint backend or infrastructure scope.

**Sequencing:** designer → engineer + platform-engineer (parallel) → orchestrator review.
**Team size:** 3 roles.

### Example 3: Analytics Dashboard
**Task:** "Create a metrics dashboard showing MRR, churn, and cohort retention"

**Staffing:**
- `analyst` (skill_hint: data/frame, data/measure) — reasoning: medium
- `engineer` (skill_hint: frontend/translate) — reasoning: medium

**Repo writes:**
- `analyst`: none
- `engineer`: explicit owner for dashboard implementation scope

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
- Do not assign more than one repo-write owner in the same stage unless the scopes are explicitly disjoint.

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
