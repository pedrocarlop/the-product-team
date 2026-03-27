---
name: narrate
description: Turn validated analysis into a clear business story that leads with the finding, explains the implication, and supports the decision.
activation_hints:
  - "Use when the analysis is complete and the result needs to be communicated to stakeholders."
  - "Route here for memos, dashboards, updates, or executive summaries that need a business narrative."
  - "Do not use for framing, measurement, or data validation work."
---

# Narrate

## Purpose

Use this skill to communicate analytical results in a way that helps people decide what to do next. Lead with the finding, explain what it means, and keep the story grounded in the validated numbers.

## When to Use

- When a result needs to be shared with decision-makers
- When a memo, update, or dashboard needs a clear takeaway
- When the audience needs the business implication, not just the statistic

## When Not to Use

- When the analysis is still in progress
- When the metric definition or data quality has not yet been validated
- When the work is purely technical and not meant for stakeholders

## Required Inputs

- The validated analysis result
- The audience and their decision context
- The business question being answered
- Any uncertainty, caveats, or limitations
- The preferred delivery format

## Workflow

1. Start with the conclusion or most important finding.
2. Translate the number into its business consequence.
3. Add only the evidence needed to support the takeaway.
4. State uncertainty, caveats, and data limits plainly.
5. Match the format to the audience: memo, slide, dashboard, or short update.
6. Close with the decision or next step the finding should inform.

## Design Principles / Evaluation Criteria

- Findings before methodology
- Business implication before statistical detail
- Clarity over completeness
- Uncertainty should be explicit, not hidden in vague language
- Good narration makes the next action obvious

## Output Contract

- A concise finding-led summary
- The business implication
- Supporting evidence and key numbers
- Caveats or limitations
- The decision or action the audience should consider

## Examples

### Example 1

Input:
- Result: "D30 retention fell 8 points in March"
- Audience: Product leadership

Expected output:
- Narrative: "D30 retention fell 8 points in the March cohort, driven by paid social users who dropped out before onboarding completed. We should review the paid acquisition mix and the onboarding step where the drop began."

## Guardrails

- Do not lead with methodology when the audience needs the takeaway
- Do not overstate causality when the analysis only supports association
- Do not bury caveats that change how the result should be interpreted
- Do not turn a finding into marketing language

## Optional Tools / Resources

- Notion for memo-style summaries
- Sheets or dashboard exports for supporting tables
- Charts or screenshots that make the finding easier to absorb
- Prior analyses for comparison and context

- Shared MCP servers: Notion MCP, GitHub MCP, Linear MCP
- Reference websites: [Mode SQL Tutorial (mode.com)](https://mode.com/sql-tutorial/), [Google Analytics Help (support.google.com)](https://support.google.com/analytics/), [Looker Documentation (cloud.google.com)](https://cloud.google.com/looker/docs), [Tableau Learning (tableau.com)](https://www.tableau.com/learn), [Kaggle Learn (kaggle.com)](https://www.kaggle.com/learn)
