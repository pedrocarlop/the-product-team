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
mesh:
  inputs:
    - ux-researcher:foundational-research # Uses the behavior/category research to ground the venture thesis
  next:
    - product-lead:frame-problem
    - analyst:forecast-model
  context: "Venture discovery translates category research into a business model and market thesis, which then needs a bounded product problem to solve."
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

### Step 2: Competitor Mapping (Landscape and Visuals)
- **Extensive List:** Map a comprehensive landscape of **10+ competitors**, ranging from direct incumbents and disruptive startups to indirect or niche players.
- **Visual Branding & Product Evidence:** For each major player, capture high-fidelity images of their **branding (logos, aesthetic)** and **products sold (screenshots of current offerings)**. **Mandatory:** Include the live website URL and direct product links for each competitor to allow direct validation.
- **Gap analysis (White Space):** Identify where the current landscape fails to address specific user needs or market segments. **Critical Questioning:** For every white space or opportunity identified, explicitly answer: *Why would a customer buy/use this specifically over existing solutions?* Back this with data signals (market reports, search trends, or traffic growth in adjacent niches).
*Note: Collaborate with `ux-researcher` for detailed UX benchmarking and full flow captures.*

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
- `### Opportunity Statement`: The "Why Now" and the core thesis. **Must include the "Why Buy" rationale** (customer motivation) and supporting data signals.
- `### Competitor Landscape & Brand Imagery`: An extensive list of competitors paired with screenshots of their brand architecture and products sold. Include **live links** to their websites and core product pages. Reference screenshots with relative paths: `![Competitor Brand](assets/competitor-name.png)`.
- `### Market Dynamics`: TAM/SAM/SOM numbers with sources.
- `### Business Model Canvas`: Structured table or list.
- `### Monetization Strategy`: Specific pricing models and revenue levers.
- `### Strategic Recommendations`: 3-5 high-leverage directions. Each recommendation must pass the "Why Buy" test and be linked to at least one data signal.

## 5. Output Contract
- **Target Path:** `knowledge/product-lead-venture-discovery.md`
- **Format:** High-fidelity Markdown (Pitch/Notion ready).
- **Mandatory Ask:** End with "### Decisions for the User" listing the specific go/no-go calls needed.

## 6. Lossless Deliverable Contract
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/runs/<run-id>/assets/`. 
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/runs/<run-id>/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths.
  - For `take_screenshot`, you MUST supply the `filePath` parameter pointing directly to the destination in the project workspace.
  - For `generate_image`, or tools that save to your `.gemini`/`.antigravity` brain directory or `/tmp`, you MUST use bash to manually move the image file into the project directory.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths or paths outside the workspace.

