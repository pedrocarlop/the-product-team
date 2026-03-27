---
name: taxonomy
description: Define the controlled vocabulary and classification scheme that keeps product content organized, searchable, and consistent across surfaces.
---

# Taxonomy

## Purpose

Use this skill to define how content is classified so users, search, and navigation can all rely on the same vocabulary and grouping rules.

## When to Use

- When the product needs categories, tags, facets, or shared metadata
- When the same concept is being named differently in different places
- When grouping rules must be explicit for search, filtering, or browsing
- When the content model is expanding and needs durable classification rules

## When Not to Use

- When the issue is only the wording of a single visible label
- When the structure is already correct and only needs a local rename
- When the work is primarily about visual hierarchy or screen layout

## Required Inputs

- The content types or entities that need classification
- The user tasks the taxonomy must support
- Existing labels, categories, tags, or metadata fields
- Known synonyms, overlap areas, and ambiguous terms
- Constraints from search, filters, localization, or governance

## Workflow

1. Identify the content types that need to be classified and the decisions users need to make.
2. Distinguish user vocabulary from internal vocabulary and choose the more legible option where possible.
3. Define each category, what it includes, and what it excludes.
4. Check for overlap, synonym drift, and categories that exist only because of implementation convenience.
5. Confirm the taxonomy can support both browsing and retrieval without creating duplicate concepts.
6. Document the governance rule for keeping the taxonomy consistent over time.

## Design Principles / Evaluation Criteria

- Categories should be distinct enough to avoid overlap
- Labels should be predictable from a user's point of view
- Classification should support both search and navigation
- The taxonomy should scale without exploding into ad hoc buckets
- The same concept should keep the same name across the product

## Output Contract

- A taxonomy list with definitions
- Inclusion and exclusion rules for each category
- A synonym or alias list where needed
- A governance note for ownership and future changes

## Examples

### Example 1

Input:
- Current labels: "Assets", "Files", and "Documents" are used interchangeably.

Expected output:
- Taxonomy note: "Use one controlled term for user-facing content and map the other terms as aliases so search and navigation stay consistent."
- Definition note: "Documents include authored records and reference materials; files are the stored containers, not the user-facing category."

## Guardrails

- Do not create categories that users cannot distinguish
- Do not use internal team names as taxonomy labels unless users use them too
- Do not let search, filters, and navigation use different terms for the same concept
- Do not leave category boundaries undefined

## Optional Tools / Resources

- Existing content models or metadata schemas
- Search logs and zero-result reports
- Support tickets or user research on terminology confusion
- Card-sort findings and label tests

