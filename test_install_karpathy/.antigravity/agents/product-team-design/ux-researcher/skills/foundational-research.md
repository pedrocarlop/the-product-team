---
name: foundational-research
description: Conduct high-level problem-space research and category behavior analysis for generic or outcome-first requests. Focus on user needs, frustrations, and competitor UX benchmarks in a broad category.
trigger: When the request is category-first or lacks a bounded user problem. Usually staffed alongside `venture-discovery`.
best_guess_output: A Foundations Deck with detailed category user behaviors, frustration mapping, and qualitative competitor UX teardowns.
output_artifacts:
  - knowledge/ux-researcher-foundational-research.md
  - knowledge/assets/ (for visual artifacts)
done_when: The category's "unmet needs" are identified, and the team has qualitative evidence for why current solutions are failing.
tool_stack:
  runtime:
    primary: [refero, mobbin, user_interviews]
    secondary: [dovetail, grain, tldv]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, chrome_devtools_navigate_page, chrome_devtools_take_screenshot, chrome_devtools_click, browser_subagent]
mesh:
  inputs:
    - none # Often the start of the discovery phase
  next:
    - product-lead:venture-discovery
    - product-designer:problem-framing
  context: "Foundational research identifies unmet needs, which must then be framed into a business case or a specific user-problem statement."
---

# Foundational Research

## 1. Purpose
This skill uncovers the qualitative "Why" behind a category before a single screen is designed. It focuses on identifying **deep user needs**, **behavioral patterns**, and **competitor UX gaps** to provide the evidence layer for the `venture-discovery` thesis.

## 2. Required Inputs and Assumptions
- **Required Inputs:** Broad category name or high-level problem space (e.g., "High-end kitchenware").
- **Assumptions:** "Foundational" research assumes zero existing product code and a blank-slate approach to the user problem.

## 3. Core Method Execution

### Step 1: Category Behavior Mapping
- Map the "Jobs to be Done" (JTBD) for users in the category.
- Identify the current ecosystem: How do users solve this problem today? (Workarounds, analogs).
- Use `search_query` and `User Interviews` (if available) to pull existing research or recruit for "Problem Discovery" sessions.

### Step 2: Frustration & Desire Analysis
- **Frustration Mapping:** What are the recurring "Pains" users experience?
- **Desire Mapping:** What are the unarticulated "Gains" users are seeking?
- **Pattern Detection:** Find clusters of dissatisfaction across reviews, social signals, or forum discussions.

### Step 3: Competitor UX Benchmarking
- Perform qualitative teardowns of an **extensive list of competitors (aim for 10+)** using `Refero` and `Mobbin`. This broad selection ensures a truly representative survey of the category and avoids over-reliance on a few dominant players.
- **Visual Evidence:** Every competitor in the set must be documented with:
    - **Brand Imagery:** Logos, color palettes, and typography that define their brand identity.
    - **Products Sold:** Clear screenshots or gallery captures showing the core products or services offered.
    - **Key Interfaces:** Landing pages, onboarding flows, and primary functional areas.
    - **Live Links:** Direct clickable URLs to their website, products, and documented flows.
- **Benchmarking Focus:** How do they handle onboarding, the "aha moment," and the core value delivery?
- **Gap Analysis:** Where is the UX breaking down for competitors?

### Step 4: Persona Archetypes
- Define 2-3 high-level behavior-based archetypes (not demographics).
- Focus on: "What triggers them to seek a solution?" and "What prevents them from switching?"

## 4. Structured Findings
The deliverable must contain:
- `### The User Problem`: One-line problem statement grounded in qualitative evidence.
- `### Behavioral Clusters`: Narratives of how users currently interact with the category.
- `### Competitor UX Teardown`: Detailed teardowns for each competitor including brand/product imagery, **live website links**, and specific flow benchmarks.
- `### Category Screenshots`: A curated gallery of the competition, showing brand aesthetics and products sold. Reference them with relative paths (e.g., `![Competitor Brand](assets/competitor-brand.png)`). Include URLs below each exhibit.
- `### Unmet Needs & White Space Opportunities`: Detailed analysis of the specific gaps where differentiation is possible. **Mandatory Questioning:** For each opportunity, explicitly answer: *Why would a customer buy/use this specifically?* Back every claim with a data signal (market trend, search volume, or user frustration pattern).
- `### Recommendations`: Directional recommendations for the next phase. Must be data-backed and address customer motivation.

## 5. Output Contract
- **Target Path:** `knowledge/ux-researcher-foundational-research.md`
- **Format:** High-fidelity Markdown (Pitch/Notion ready).
- **Mandatory Ask:** End with "### Insights for Design" listing specific design-direction recommendations. These must pass the "Why Buy" test and be linked to evidence.
- **Hypothesis Validation:** Frame any "White Space Opportunity" as a testable hypothesis with a clear "Why" (customer motivation) and supporting data.

## 6. Lossless Deliverable Contract
- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/ux-researcher-foundational-research.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.
