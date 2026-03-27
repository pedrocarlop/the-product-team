---
name: critique
description: Evaluate a design through structured heuristic analysis, scoring usability across cognitive load, discoverability, affordance, error prevention, and task completion to produce actionable findings.
---

# Critique

## Purpose

Use this skill to deliver a structured, heuristic-grounded usability critique that identifies the specific barriers most likely to prevent users from understanding, navigating, and completing their tasks.

## When to Use

- When a design needs a systematic usability review before refinement or approval
- When the team wants findings grounded in established heuristics, not just opinion
- When it is important to identify the few issues most likely to hurt task success, ranked by severity
- When a design needs evaluation against specific user modes: first-time use, expert efficiency, error recovery, or high-anxiety moments

## When Not to Use

- When the review needs strategic alignment judgment or portfolio-level quality assessment (route to design director)
- When the main need is visual polish, brand consistency, or art direction feedback
- When the task is to redesign rather than evaluate

## Required Inputs

- The design artifact: screens, prototype, or live implementation to review
- The primary user task and success criteria for the surface being evaluated
- The relevant user modes or personas: first-time user, power user, stressed user, returning user
- Any task flows, wireframes, or specs that define the intended interaction model
- Known constraints: platform conventions, accessibility requirements, or design system rules

## Workflow

1. Identify the primary user task and the critical path the user must complete.
2. Check for generic or low-intent design signals that suggest the surface is derivative rather than thoughtfully composed.
3. Score the interface against Nielsen's 10 heuristics, noting the specific element and the specific violation for each finding.
4. Evaluate cognitive load: is the user asked to remember, interpret, or decide more than necessary at any step?
5. Assess discoverability and affordance: can the user find the primary action and understand what interactive elements do?
6. Check error prevention and recovery: does the UI prevent mistakes and provide clear recovery when they occur?
7. Rank findings by severity (how badly it hurts task success) and frequency (how many users will encounter it).

## Design Principles / Evaluation Criteria

- Findings must cite a specific heuristic or usability principle, not just personal preference
- Severity should reflect actual task impact: can the user complete the task, or are they blocked?
- Frequency matters: an issue that affects every user is more severe than one that affects edge cases
- The critique should distinguish between design intent failures and implementation bugs
- Positive patterns should be named specifically so the designer knows what to preserve

## Output Contract

- A usability health score grounded in the heuristic review
- The 3-5 highest-severity findings, each with: the specific element, the heuristic violated, the user impact, and a concrete fix direction
- Relevant persona or user-mode red flags: first-time confusion, expert inefficiency, high-anxiety failure points
- The strongest positive patterns worth preserving
- A clear recommendation: ready, needs revision with specific items, or needs significant rework

## Examples

### Example 1

Input:
- A settings page with 15 toggles, no grouping, and no confirmation on destructive changes

Expected output:
- Finding 1 (Severity: High): Lack of grouping violates "Recognition over recall" -- users must read every toggle to find the one they need. Fix: Group by category with section headers.
- Finding 2 (Severity: High): No confirmation on destructive toggles violates "Error prevention" -- users can accidentally disable critical features. Fix: Add confirmation dialog for destructive changes.
- Finding 3 (Severity: Medium): All toggles use identical visual weight, violating "Visibility of system status" -- the user cannot distinguish high-impact from low-impact settings. Fix: Use visual hierarchy to differentiate.
- Positive: Toggle labels are clear and use consistent verb structure.

## Guardrails

- Do not soften findings into generic encouragement; specificity serves the designer
- Do not confuse a usability critique with a full redesign brief
- Do not evaluate visual aesthetics unless the aesthetic choice causes a measurable usability problem
- Do not skip error states, edge cases, or recovery paths in the evaluation
- Do not rank findings by personal annoyance; rank by user task impact and frequency

## Optional Tools / Resources

- [Nielsen Norman Group Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Maze](https://maze.co/) for remote usability testing
- [Dovetail](https://dovetail.com/) for research synthesis
- Figma MCP and Chrome DevTools MCP for inspecting the live or prototyped interface
- Task flow documentation for the surface being reviewed
