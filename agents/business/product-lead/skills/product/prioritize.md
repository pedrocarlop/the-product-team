---
name: prioritize
description: "Rank product opportunities using explicit criteria, tradeoffs, and evidence so the team can decide what to do next. Use when a roadmap is full, engineering is constrained, or the team disagrees on the highest ROI effort."
---

# Prioritize

## Overview

"Prioritize" determines the exact order in which work is executed based on a defensible scoring framework. When everything is a "Priority 1," nothing ships on time. A strong prioritization process forces stakeholders to confront trade-offs (e.g., Scope vs. Time vs. Resources) using objective criteria rather than relying on seniority or "who yells loudest."

## When to Use

- When the product backlog is unmanageable or overlapping in scope.
- When new, urgent requests threaten the delivery of planned roadmap items.
- When deciding what makes the cut for an MVP (Minimum Viable Product).
- When a deadline is looming and scope must be aggressively cut.

## When Not to Use

- When a single problem requires framing and definition (use `frame` instead).
- When the task is to write requirements for an already-chosen initiative (use `specify`).
- When the decision is purely technical architecture (e.g., selecting a database).

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 1: Align on the Decision Horizon

Determine the timeframe and the pool of candidates:
- Are we ranking items for the next Sprint (2 weeks), Quarter (3 months), or Half (6 months)?
- What is the hard constraint? (e.g., "We only have 1 Frontend Engineer for the quarter.")

### Step 2: Establish the Scoring Criteria

Select an objective framework (e.g., RICE, MoSCoW, Cost of Delay) and define the criteria:
- **Reach**: How many users are affected?
- **Impact**: How much does this move the target metric (High=3, Med=2, Low=1)?
- **Confidence**: How sure are we about these estimates (100% vs. 50%)?
- **Effort**: How many engineering weeks/months will this take?

### Step 3: Grade the Candidates (The Matrix)

Assess each initiative against the selected framework objectively.
- Do not let intuition override the math, but use judgment to flag anomalous scores.
- Example: *Initiative A (R=1000, I=3, C=80%, E=2 weeks) = Score 1.2*

### Step 4: Identify Dependencies and Sequencing

Adjust the raw math-based ranking based on reality:
- "Feature B scored lower than Feature A, but Feature A requires Feature B's data pipeline to exist first."
- Adjust the final queue to reflect logical sequencing.

### Step 5: Document the Trade-Offs (The Cuts)

Explicitly list what is *not* getting built and why:
- "We are prioritizing the Analytics redesign [A], which means the Notification system upgrade [Z] is postponed until Q3."

## Decision Tree: Is the Ranking Defensible?

```
Are the criteria (Impact vs Effort) universally applied to all candidates?
├── YES → Do the top items fit within the known engineering capacity constraint?
│   ├── YES → Are the "Cut" items explicitly documented and communicated?
│   │   ├── YES → The ranking is defensible.
│   │   └── NO → Document the trade-offs (Step 5) to prevent scope creep later.
│   └── NO → Cut scope. You cannot rank 3 items as Priority 1 if capacity only fits 1.
└── NO → Rerun the matrix (Step 3) objectively. Do not inflate "Confidence" artificially.
```

## Worked Examples

### Example 1: Scoring Competing Epics

**Input:** Two proposed epics: 1) "Dark Mode" vs. 2) "SAML SSO Auth." Capacity is 1 month.
**Workflow Application:**
- **Framework**: RICE.
- **Dark Mode**: Reach (10k DAU), Impact (Low/1), Confidence (100%), Effort (1 month). Score: 10k.
- **SAML SSO**: Reach (5 Enterprise Clients), Impact (High/3. unlocks $500k ARR), Confidence (80%), Effort (2 weeks). Score: 20k adjusted for value.
- **Decision**: Prioritize SAML SSO.
- **Trade-Off Note**: Dark Mode postponed to Q4.

### Example 2: Scoping Down an MVP

**Input:** A new feature has 10 listed requirements, but the launch is in 2 weeks.
**Workflow Application:**
- **Framework**: MoSCoW (Must, Should, Could, Won't have).
- **Must Have**: Core data ingestion, basic list view, error handling.
- **Should Have**: Search/Filtering (Wait until post-launch).
- **Could Have**: PDF Export (Wait).
- **Decision**: Launch with List View only. Search and Export removed from MVP.

## Guardrails

- **Never accept "Everything is a priority."** Rank order is mandatory (1, 2, 3...). There are no ties at the top.
- **Always anchor Impact to a specific metric or business goal.** "It's cool" is not Impact. "It increases retention by X%" is Impact.
- **Never score Effort without Consulting Engineering.** Product Leads do not size engineering effort.

## Troubleshooting

### Issue: Stakeholders constantly argue about the ranking
**Cause**: The scoring criteria (Step 2) were never agreed upon.
**Solution**: Pause the prioritization of *features* and force alignment on the *criteria*. E.g., "Are we optimizing for New User Growth or Enterprise Retention this quarter?"

### Issue: The top priority item takes 6 months and blocks everything
**Cause**: The item is an Epic, not a sliceable initiative.
**Solution**: Break the top priority into smaller milestones (1 month max) and re-rank the milestones against the rest of the backlog.

### Issue: "Pet projects" bypass the scoring system
**Cause**: Seniority override, or "Confidence" is artificially inflated.
**Solution**: Demand tangible evidence (user interviews, data logs) to justify a high Confidence score. If evidence is lacking, Confidence should be 20-50%, dropping the final score.
