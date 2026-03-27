---
name: map
description: Translate an information architecture problem into current-state and future-state structures with hierarchy, entry points, wayfinding, and findability constraints.
---

# Map

## Purpose

Use this skill to document how information is organized today and how it should be organized after the change, with enough structure that teams can see hierarchy, entry points, decision points, and findability risks.

## When to Use

- When a navigation or content structure needs to be made explicit
- When you need an AS-IS and TO-BE view of a site map or product tree
- When entry points, wayfinding paths, or structural dead ends need to be visible
- When the product has grown and the current grouping no longer scales cleanly

## When Not to Use

- When the main problem is only wording or tone on a label
- When the structure is already settled and only needs local copy cleanup
- When the task is primarily about visual hierarchy rather than information hierarchy

## Required Inputs

- The product area or surface being reorganized
- The current structure, if any, including known entry points and navigation paths
- The user tasks the structure must support
- Known content types, page types, or sections that must be grouped
- Constraints around scale, permissions, localization, or discoverability

## Workflow

1. Restate the structural problem in plain user terms and identify the target outcome.
2. Document the current structure in observable terms: pages, sections, paths, and handoffs.
3. Identify where users enter, branch, backtrack, or get stranded.
4. Draft the future structure with the smallest change that improves findability and scale.
5. Verify that the structure supports both browsing and known-item search behavior.
6. Check that the map can be turned into labels, navigation, and content groupings without gaps.

## Design Principles / Evaluation Criteria

- Structure should reflect user mental models, not internal org charts
- The main path should be obvious, but alternate paths must also be represented
- Dead ends and orphaned content are structural failures
- Groupings should remain legible as content volume grows
- The future state should be understandable without extra narration

## Output Contract

- An AS-IS structure map
- A TO-BE structure map
- A list of key entry points, branches, and dead ends
- A summary of scale, discoverability, or hierarchy risks

## Examples

### Example 1

Input:
- Current note: "Users find reports in three different places."

Expected output:
- Map note: "The structure splits reports across overlapping sections, which creates duplicate entry points and weakens discoverability."
- TO-BE note: "Reports are consolidated into one primary section with secondary entry points preserved only where the task demands it."

## Guardrails

- Do not map only the happy path
- Do not hide duplicate entry points if users can actually reach them
- Do not turn the map into a label exercise too early
- Do not leave hierarchy depth or ownership ambiguous

## Optional Tools / Resources

- Notion MCP and Figma MCP for structure notes, diagrams, and walkthroughs
- Existing sitemaps or navigation audits
- Card sort or tree-test results
- Search analytics and zero-result queries
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Baymard Institute](https://baymard.com/)
- [Optimal Workshop](https://www.optimalworkshop.com/)
