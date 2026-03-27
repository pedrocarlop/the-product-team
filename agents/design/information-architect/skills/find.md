---
name: find
description: Design the search and findability experience so users can locate content through search, browse, filters, and recovery paths with minimal friction.
activation_hints:
  - "Use when users need to locate known items or recover from not finding something."
  - "Route here for search behavior, zero results, filters, sorting, and browse-to-search handoff."
  - "Do not use for unrelated content strategy or for purely visual layout decisions."
---

# Find

## Purpose

Use this skill to design how users discover and retrieve content, including search, filters, browsing aids, and recovery when results are missing or incomplete.

## When to Use

- When users need to find an item, page, record, or topic quickly
- When browse paths and search paths need to work together
- When filters, sorting, or result grouping are part of the experience
- When the product needs a zero-results or partial-results recovery pattern

## When Not to Use

- When the issue is only the wording of one label or section name
- When the main work is defining categories rather than retrieval behavior
- When the task is purely about visual polish on a search component

## Required Inputs

- The content users need to find
- The primary and secondary retrieval methods available
- Known search terms, synonyms, and misspellings
- Filters, facets, and sort options the content model can support
- Zero-result, no-access, or low-confidence recovery requirements

## Workflow

1. Define the target objects users are trying to find and the likely terms they will use.
2. Map the retrieval paths: direct search, browse, filters, shortcuts, and related content.
3. Identify the fields, facets, and sort options that support meaningful narrowing.
4. Design what happens when users get no results, too many results, or weak matches.
5. Check that browse and search reinforce each other instead of competing.
6. Verify the experience supports recovery, not just successful queries.

## Design Principles / Evaluation Criteria

- Search should return useful results before it returns perfect results
- Recovery paths matter as much as the happy path
- Filters must reflect real content metadata, not desired metadata
- Browsing and searching should feel like parts of one system
- Zero-result states should guide the user forward, not just apologize

## Output Contract

- A retrieval model covering search, browse, and filter behavior
- A zero-result and recovery pattern
- A list of supported search fields, facets, and sort choices
- Notes on synonym handling or result ranking assumptions

## Examples

### Example 1

Input:
- User task: Find a policy they only remember by topic, not exact name

Expected output:
- Find note: "Support topic-based search, synonym matching, and browse entry points so the user can recover even without the exact title."
- Recovery note: "If no direct match exists, surface related topics and the nearest browse path instead of stopping at an empty page."

## Guardrails

- Do not design search without matching it to the content model
- Do not promise filters that the data cannot support
- Do not make zero results a dead end
- Do not separate search behavior from the rest of the IA

## Optional Tools / Resources

- Search analytics and query logs
- Card sorts, tree tests, and first-click tests
- Metadata schemas and content models
- Product walkthroughs or screenshot audits

