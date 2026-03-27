---
name: structure
description: Organize headings, labels, helper text, and content hierarchy so complex screens become easier to scan, understand, and act on.
activation_hints:
  - "Use when a screen is text-heavy, hard to scan, or forces users to read too much before acting."
  - "Route here for content hierarchy, grouping logic, headings, and helper-text placement."
  - "Do not use for simple string rewrites, naming strategy, or onboarding-specific teaching flows."
---

# Structure

## Purpose

Use this skill to improve the information design of dense product surfaces so users can scan, orient, and act without carrying unnecessary cognitive load.

## When to Use

- When a screen, form, settings page, or dashboard feels text-heavy or hard to scan
- When users must read too much before they can find the important action or detail
- When copy quality is acceptable at the sentence level but weak at the hierarchy level

## When Not to Use

- When the problem is primarily a local clarity issue in one string
- When the task is naming a concept or standardizing vocabulary across a flow
- When the surface needs full UX flow redesign beyond content organization

## Required Inputs

- The full surface content, including headings, labels, helper text, and section groupings
- The primary user task and the decisions users must make on the page
- Platform, screen-size, and responsiveness constraints
- Existing component patterns and any design-system guidance for forms or settings pages
- Business rules, validations, or legal content that must remain visible

## Workflow

1. Identify the page's primary task and the minimum information users need first.
2. Group related content by decision or job to be done, not by internal implementation.
3. Establish a clear hierarchy of headings, labels, helper text, and secondary explanation.
4. Move nonessential explanation into progressive disclosure or supporting copy where appropriate.
5. Rewrite section labels and helper text so users can scan confidently and understand what belongs where.
6. Review the page for selective reading, making sure users can act without reading everything.

## Design Principles / Evaluation Criteria

- Clear hierarchy and scanability
- Grouping by user task or decision
- Progressive disclosure for secondary detail
- Strong labels and headings that reduce rereading
- Preservation of essential legal, validation, and accessibility content
- Responsiveness and readability across common screen sizes

## Output Contract

- A clearer content hierarchy for the surface, including headings and grouping logic
- Revised labels, helper text, and supporting copy for high-friction sections
- Notes on what was surfaced, condensed, or deferred to improve scanning

## Examples

### Example 1

Input:
- Settings page with 18 controls in one long list
- Users struggle to find billing and notification options
- Existing copy is accurate but flat and hard to scan

Expected output:
- Proposed section groupings and headings
- Revised labels and helper text for ambiguous controls
- Notes on which secondary details move behind progressive disclosure

## Guardrails

- Do not hide essential warnings, validations, or legal disclosures just to make the page feel cleaner
- Do not reorganize content in ways that conflict with the actual product model or navigation
- Do not solve hierarchy problems with longer explanatory paragraphs
- Do not ignore mobile and constrained-width scanning behavior

## Optional Tools / Resources

- Screen mocks or screenshots
- Existing form, settings, or dashboard patterns
- Research notes showing scan or comprehension problems
- Accessibility guidance for headings, helper text, and reading order
