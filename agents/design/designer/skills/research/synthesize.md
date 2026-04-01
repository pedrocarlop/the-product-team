---
name: synthesize
description: Turn research notes, transcripts, and observations into defensible themes, insights, and implications the design team can act on.
---

# Synthesize

## Purpose

Use this skill to convert raw research material into findings that explain what is happening, why it matters, and what the team should do with it.

## When to Use

- When interviews, tests, or field notes are complete
- When the team needs patterns, themes, and evidence-backed insights
- When raw notes need to become a decision-ready summary

## When Not to Use

- When the task is still to recruit, plan, or moderate sessions
- When the output should stay at the note-taking level
- When there is not yet enough evidence to compare observations

## Required Inputs

- Session notes, transcripts, artifacts, or data excerpts
- The original research question and decision context
- Any known segments, cohorts, or comparisons that matter
- The audience and format for the synthesis output

## Workflow

### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: designer
project: <slug>
deliverable: designer.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

1. Revisit the research question before looking at the notes.
2. Group observations by repeated behavior, pain point, or decision pattern.
3. Separate signal from isolated anecdotes.
4. Turn themes into insights that explain the underlying reason.
5. Tie each insight back to the decision it should influence.
6. Note uncertainty, contradictions, and gaps instead of smoothing them over.
7. Produce a concise artifact that another team member can challenge or extend.

### Step 2: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.

## Design Principles / Evaluation Criteria

- Themes are rooted in evidence, not vibes
- Insights explain why a pattern exists
- One-off comments do not outrank repeated behavior
- Uncertainty is explicit
- The final artifact supports design and product decisions, not just retrospective reading

## Output Contract

- Key themes grouped by evidence
- Insights written as cause-and-effect statements
- Supporting quotes or observations for each insight
- Open questions, contradictions, and follow-up opportunities
- Clear implications for the next decision or design step

## Examples

### Example 1

Input:
- Notes from 6 interviews about a billing settings flow

Expected output:
- Theme: users are uncertain which card is active
- Insight: the interface presents account-level status but users think in terms of the card they most recently used
- Implication: make the active payment method explicit in the primary view

## Guardrails

- Do not present raw observations as finished insights
- Do not overgeneralize from a single participant
- Do not remove contradictions just to keep the story clean
- Do not skip the link between evidence and implication

## Optional Tools / Resources

- Notion for coding, affinity mapping, and findings docs
- FigJam for collaborative synthesis
- Recorded transcripts or annotated notes
