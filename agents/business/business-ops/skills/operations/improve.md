---
name: improve
description: Diagnose recurring operational pain, identify root causes, and drive measurable process, quality, or efficiency improvements.
---

# Improve

## Purpose

Use this skill to make an operational system better by finding the root cause of recurring problems and changing the process, tooling, or control that produces them.

## When to Use

- When the same operational issue keeps happening
- When time, cost, quality, or throughput needs to improve
- When metrics show a process is underperforming or drifting

## When Not to Use

- When the process is not yet mapped or understood
- When the main need is to document the standard way of working
- When the issue is mostly about coordination between teams rather than the process itself

## Required Inputs

- The problem symptom, metric, or incident that triggered the work
- Any available data on frequency, impact, and trend
- The current process, owners, and tools involved
- Prior fixes, workarounds, or failed attempts
- Any constraints that limit the options for change

## Workflow

1. Define the problem in measurable terms and separate symptoms from causes.
2. Gather evidence from incidents, metrics, or user and team feedback.
3. Run a root-cause analysis and identify the smallest systemic fix.
4. Compare improvement options by impact, effort, and operational risk.
5. Implement the change with a way to measure whether it worked.
6. Recheck the result and document the learning so the same issue does not recur.

## Design Principles / Evaluation Criteria

- Fix the system, not just the symptom
- Use evidence before choosing a solution
- Improvements should have a measurable before and after
- Prefer the smallest change that removes the recurring failure
- Learning should be captured so the issue does not reappear

## Output Contract

- A problem statement with supporting evidence
- A root-cause analysis
- A prioritized improvement plan
- Success metrics and a follow-up check

## Examples

### Example 1

Input:
- Issue: "Monthly reports are always late."

Expected output:
- RCA note: "The delay comes from two manual handoffs and an unclear approval owner, not from report creation time."
- Improvement note: "Remove one approval step, assign a single owner, and measure report completion time for the next three cycles."

## Guardrails

- Do not treat the loudest symptom as the root cause
- Do not recommend changes without evidence
- Do not improve a process in a way that makes coordination harder
- Do not ship a fix without a way to verify the outcome

## Optional Tools / Resources

- Incident logs and retrospective notes
- Operational dashboards and KPI trends
- Process maps and SOPs
- Team feedback and customer-impact data

- Shared MCP servers: Notion MCP, Linear MCP, Slack MCP
- Reference websites: [Atlassian Team Playbook (atlassian.com)](https://www.atlassian.com/team-playbook), [McKinsey Operations Insights (mckinsey.com)](https://www.mckinsey.com/capabilities/operations/our-insights), [Asana Work Innovation Lab (asana.com)](https://asana.com/resources), [Harvard Business Review Operations (hbr.org)](https://hbr.org/topic/operations), [Lean Enterprise Institute (lean.org)](https://www.lean.org/explore-lean/)
