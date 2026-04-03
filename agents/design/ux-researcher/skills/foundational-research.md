---
name: foundational-research
description: Conduct high-level problem-space research and category behavior analysis for generic or outcome-first requests. Focus on user needs, frustrations, and competitor UX benchmarks in a broad category.
trigger: When the request is category-first or lacks a bounded user problem. Usually staffed alongside `venture-discovery`.
best_guess_output: A Foundations Deck with detailed category user behaviors, frustration mapping, and qualitative competitor UX teardowns.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher-foundational-research.md
done_when: The category's "unmet needs" are identified, and the team has qualitative evidence for why current solutions are failing.
tool_stack:
  runtime:
    primary: [refero, mobbin, user_interviews]
    secondary: [dovetail, grain, tldv]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, open_browser]
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
- Perform qualitative teardowns of the top 3-5 competitors using `Refero` and `Mobbin`.
- **Benchmarking Focus:** How do they handle onboarding, the "aha moment," and the core value delivery?
- **Gap Analysis:** Where is the UX breaking down for competitors?

### Step 4: Persona Archetypes
- Define 2-3 high-level behavior-based archetypes (not demographics).
- Focus on: "What triggers them to seek a solution?" and "What prevents them from switching?"

## 4. Structured Findings
The deliverable must contain:
- `### The User Problem`: One-line problem statement grounded in qualitative evidence.
- `### Behavioral Clusters`: Narratives of how users currently interact with the category.
- `### Competitor UX Teardown`: Multi-screen/flow benchmark with gap identification.
- `### Unmet Needs`: The specific opportunities for differentiation.

## 5. Output Contract
- **Target Path:** `logs/active/<project-slug>/deliverables/ux-researcher-foundational-research.md`
- **Format:** High-fidelity Markdown (Pitch/Notion ready).
- **Mandatory Ask:** End with "### Insights for Design" listing specific design-direction recommendations.

## 6. Lossless Deliverable Contract
Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
