---
name: retrospect
description: "Analyze recurring mistakes or quality issues and propose targeted instruction updates to prevent them. Use when the user reports a repeated mistake, when the same issue appears across multiple timeline entries, when a specialist repeatedly returns mismatches, or when the user explicitly asks for process improvement."
---

# Retrospect

## Overview

The learning loop for the Product Team workflow. Retrospect identifies systemic patterns — not one-off errors — and proposes targeted fixes to instructions, routing rules, or skill files to prevent recurrence. Every retrospective produces a concrete, auditable change proposal, not a philosophical observation.

## When to Use

- When the user says "you keep doing X" or "this is the same mistake as last time."
- When you notice in `logs/TIMELINE.md` that the same issue appears in 2+ projects.
- When a specialist repeatedly returns a mismatch or escalation for the same reason.
- When the user explicitly asks for a retrospective or process improvement.
- When a review consistently catches the same class of defect.

## When Not to Use

- For one-off errors that are unlikely to recur. Just fix them directly.
- When the issue is a single misunderstanding, not a pattern. Clarify and move on.
- When the user is asking for a task, not reflection. Do the task first.

## Prerequisites

- At least 2 concrete instances of the pattern (project slugs, dates, or specific exchanges).
- Access to `logs/TIMELINE.md` and relevant `context.md` files for evidence.
- Knowledge of which files contain the instructions that govern the failing behavior.

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

### Step 2: Identify the Pattern

Answer these questions with specifics — not generalities:

| Question | Required Detail |
|----------|----------------|
| What went wrong? | The exact mistake — name the behavior, not the category |
| When did it happen? | Project slugs, dates, roles involved |
| What was expected? | The correct behavior |
| What actually happened? | The incorrect behavior |
| How many times? | Count of occurrences (minimum 2 to qualify as a pattern) |

**One pattern per retrospective.** Do not bundle unrelated issues. If you find multiple patterns, create separate retrospectives.

### Step 3: Classify the Root Cause

Use this taxonomy to identify what failed:

```
What type of failure is this?
├── INSTRUCTION GAP — needed guidance doesn't exist
│   └── Fix type: ADD instruction to the relevant file
├── INSTRUCTION UNCLEAR — guidance exists but is ambiguous
│   └── Fix type: REWRITE instruction for clarity
├── INSTRUCTION IGNORED — guidance exists, is clear, but wasn't followed
│   └── Fix type: RESTRUCTURE for emphasis (move to guardrails, add "IMPORTANT" prefix)
├── ROUTING ERROR — wrong role was assigned
│   └── Fix type: UPDATE routing rules in route.md or staff.md
├── CONTEXT LOSS — information was lost between conversations
│   └── Fix type: IMPROVE context.md template or logging rules
├── SKILL GAP — specialist skill file is missing guidance
│   └── Fix type: UPDATE the specific skill file
├── STAFFING ERROR — wrong number of roles, or wrong roles
│   └── Fix type: UPDATE staffing heuristics in staff.md
└── TOOL MISUSE — a tool was used incorrectly or skipped
    └── Fix type: ADD tool usage protocol to the relevant skill
```

### Step 4: Gather Evidence

Before proposing a fix, collect concrete evidence:

1. **Search the timeline**: Read `logs/TIMELINE.md` entries for the affected projects.
2. **Read context files**: Check `logs/active/<slug>/context.md` for each instance.
3. **Check specialist output**: Read relevant `deliverables/*.md` or `reviews/*.md` files.
4. **Identify the instruction source**: Find the exact file and section that should have governed the behavior.

Document the evidence trail — where you looked and what you found.

### Step 5: Propose a Targeted Fix

Write a concrete proposal with all five elements:

```markdown
### Proposed Fix

**What to change**: <exact file path and section>
**Current content**: <what the instruction says now, or "MISSING — no instruction exists">
**Proposed content**: <the new or modified instruction, written exactly as it should appear>
**Why this helps**: <one sentence connecting the fix to the root cause>
**Verification**: <how to confirm the fix works in the next relevant task>
```

**Rules for good fixes:**
- Fix the **system**, not the symptom. If the mistake keeps happening, the instructions are wrong — not the agent.
- Make fixes **testable**. "Be more careful" is not a fix. "Always check X before Y" is.
- Keep fixes **minimal**. Change only what's needed to prevent the pattern. Don't rewrite the whole file.
- Be **specific**. Reference exact file paths, line ranges, and section headers.

### Step 6: Apply or Escalate

Follow this decision tree:

```
Is the fix to an installed Product Team file (.codex/product-team/ or .codex/agents/)?
├── YES → Propose the change to the user for approval before editing.
└── NO → Is the fix to a target-project file (AGENTS.md, project config)?
    ├── YES → Apply directly if the user has given standing permission.
    │         Otherwise, propose for approval.
    └── NO → Is the fix to a source Product Team package file?
        └── YES → Note it as a suggestion for the package maintainer.
                   Do not modify source files directly.
```

### Step 7: Write the Retrospective Record

Write to `logs/active/<project-slug>/retrospective.md`:

```markdown
# Retrospective: <pattern name>

### Step 8: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Pattern
<1-2 sentence description of what keeps going wrong>

## Instances
| Date | Project | Role | What Happened |
|------|---------|------|---------------|
| <date> | <slug> | <role> | <1-line description> |
| <date> | <slug> | <role> | <1-line description> |

## Root Cause
**Category**: <from taxonomy: INSTRUCTION GAP | UNCLEAR | IGNORED | ROUTING ERROR | CONTEXT LOSS | SKILL GAP | STAFFING ERROR | TOOL MISUSE>
**Analysis**: <2-3 sentences on why this keeps happening>

## Proposed Fix
**File**: <path>
**Current**: <content or MISSING>
**Proposed**: <new content>
**Why**: <1 sentence>

## Verification
<How to confirm the fix works>

## Status
<applied | proposed | deferred>
```

## Worked Examples

### Example 1: Instruction Gap
**Pattern:** The orchestrator keeps staffing `reviewer` for simple, low-risk tasks, wasting tokens.

**Evidence:**
- `20260315-add-footer-link`: reviewer staffed for a 1-line HTML change.
- `20260318-fix-typo-login`: reviewer staffed for a string fix.

**Root cause:** INSTRUCTION GAP — `staff.md` lists "Include reviewers only when they materially reduce risk" but doesn't define what constitutes "low risk" where review is obviously unnecessary.

**Proposed fix:**
- **File:** `agents/orchestrator/orchestrator/skills/staff.md`
- **Current:** "Include reviewers only when they materially reduce risk."
- **Proposed:** "Include reviewers only when they materially reduce risk. Skip reviewer for: single-file changes, copy fixes, dependency updates, configuration changes, and any task with no user-facing behavior change."
- **Why:** Enumerating the common low-risk cases prevents the orchestrator from defaulting to "include reviewer just in case."

### Example 2: Routing Error
**Pattern:** Tasks that mention "analytics" are routed to `analyst` even when the actual work is frontend dashboard implementation.

**Evidence:**
- `20260320-analytics-dashboard`: routed to analyst, but the task was building a chart component.
- `20260322-metrics-page`: routed to analyst + engineer, but analyst had nothing to do.

**Root cause:** ROUTING ERROR — `route.md` maps "mentions metrics" to `analyst`, but many analytics tasks are pure frontend implementation.

**Proposed fix:**
- **File:** `agents/orchestrator/orchestrator/skills/route.md`
- **Section:** Domain classification table
- **Current:** "Mentions metrics, forecasting, revenue, data → `analyst`"
- **Proposed:** "Mentions metrics, forecasting, revenue, data → `analyst` if the task is _defining_ metrics or _building_ models. If the task is _displaying_ existing metrics in a UI → `engineer`."
- **Why:** Distinguishes between metric definition (analyst work) and metric display (engineer work).

## Guardrails

- One pattern per retrospective. Do not bundle unrelated issues — each gets its own record.
- Minimum 2 instances to qualify as a pattern. One-off errors don't need a systemic fix.
- Do not write essay-length retrospectives. Keep them short and actionable.
- Do not fix symptoms ("remind the agent to check X") — fix the system ("add X to the checklist in the skill file").
- After applying a fix, verify it in the next relevant task — do not assume it worked.
- Do not modify source Product Team package files directly — note them as suggestions only.

## Troubleshooting

### Issue: Can't find enough instances to qualify as a pattern
**Cause:** The issue might genuinely be a one-off.
**Solution:** Note it for future reference but don't create a full retrospective. If it happens again, you'll have the prior instance to pair with.

### Issue: Root cause is ambiguous — could be instruction gap or routing error
**Cause:** Multiple system failures may contribute to the same surface behavior.
**Solution:** Pick the most upstream cause. If routing put the task on the wrong role, fix routing first — the downstream instruction gap might resolve itself.

### Issue: Proposed fix would be a large change to a core file
**Cause:** The pattern reveals a fundamental gap in the workflow design.
**Solution:** Propose the minimal viable fix for the immediate pattern. Note the larger systemic issue separately for the package maintainer. Don't try to redesign the workflow in a retrospective.
