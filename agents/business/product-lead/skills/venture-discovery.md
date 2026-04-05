---
name: venture-discovery
description: Perform foundational business and product diligence for generic or outcome-first requests. Includes TAM analysis, Business Model Canvas, Value Proposition Design, and Monetization strategy.
trigger: When a request is generic, category-first, or asks for a "company", "startup", or "business" from scratch without a bounded problem.
best_guess_output: A comprehensive Venture Thesis with market sizing (TAM/SAM/SOM), a completed Business Model Canvas, Value Prop Map, and Trends/Risks analysis.
output_artifacts: knowledge/product-lead-venture-discovery.md
done_when: The business fundamentals are modeled, market potential is quantified, and the strategic direction is clear enough for a user go/no-go decision.
tool_stack:
  runtime:
    primary: [lane, search_query]
    secondary: [notion, similarweb]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, reference_ground]
---

# Venture Discovery

## 1. Purpose
Turn a generic venture-level request into a structured business thesis. This skill ensures the team understands the market, the competition, and the economic viability of the proposed product before committing to design or engineering. It explicitly favors **slides and documentation** over UI mocks.

## 2. Required Inputs and Assumptions
- **Required Inputs:** High-level category or category-first request (e.g., "High-end kitchenware company").
- **Assumptions:** Market trends and size should be grounded in 2024-2026 data. If specific geographic data is missing, assume a "Global/US-First" context unless otherwise specified.

## 3. Core Method Execution

### Step 1: Market Sizing (TAM/SAM/SOM)
- **TAM (Total Addressable Market):** Total market demand for the category.
- **SAM (Serviceable Addressable Market):** The portion of the TAM targeted by your specific product type.
- **SOM (Serviceable Obtainable Market):** The portion of SAM you can realistically capture.
Use `search_query` and `SimilarWeb` (if available) to pull recent market reports and competitor traffic.

### Step 2: Competitor Mapping (Swot)
- Map the current landscape: Incumbents, Disruptors, and Niche players.
- Identify the "Gap in the Market" (White Space).
*Note: Collaborate with `ux-researcher` for detailed UX benchmarking.*

### Step 3: Business Model Canvas
Complete the 9 building blocks:
1. **Value Propositions:** What unique value do we deliver?
2. **Customer Segments:** Who are we creating value for?
3. **Channels:** How do we reach them?
4. **Customer Relationships:** How do we interact?
5. **Revenue Streams:** How do we make money? (Monetization)
6. **Key Resources:** What do we need to build it?
7. **Key Activities:** What must we do to deliver?
8. **Key Partners:** Who can help us?
9. **Cost Structure:** What are the major costs?

### Step 4: Value Proposition Design (Customer Profile vs Value Map)
- **Pains & Gains:** What are the actual problems users face in this category?
- **Pain Relievers & Gain Creators:** How does our solution address them?

### Step 5: Trends and Risks (PESTEL)
- Analyze Political, Economic, Social, Technological, Environmental, and Legal trends.
- Use `Lane` to synthesize strategic risks.

## 4. Structured Findings
The deliverable must contain:
- `### Opportunity Statement`: The "Why Now" and the core thesis.
- `### Market Dynamics`: TAM/SAM/SOM numbers with sources.
- `### Business Model Canvas`: Structured table or list.
- `### Monetization Strategy`: Specific pricing models and revenue levers.
- `### Strategic Recommendations`: 3-5 high-leverage directions.

## 5. Output Contract
- **Target Path:** `knowledge/product-lead-venture-discovery.md`
- **Format:** High-fidelity Markdown (Pitch/Notion ready).
- **Mandatory Ask:** End with "### Decisions for the User" listing the specific go/no-go calls needed.

## 6. Lossless Deliverable Contract
Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
