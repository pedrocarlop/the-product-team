---
name: positioning-brief
description: Expert positioning and messaging strategy using April Dunford's framework and JTBD, validated with buyer intelligence signals.
trigger: When a product or feature needs a market-facing position, or existing messaging fails to resonate with the target audience.
best_guess_output: A comprehensive positioning brief with audience segments, competitive alternatives, unique attributes, value propositions, and message testing evidence.
output_artifacts: knowledge/go-to-market-positioning-brief.md
done_when: Positioning is validated via internal alignment and external buyer signals (e.g., Wynter/Ignition validation).
mesh:
  inputs:
    - product-lead:write-prd
    - ux-researcher:competitor-research
    - product-lead:prioritize-roadmap
  next:
    - go-to-market:campaign-brief
    - go-to-market:launch-plan
    - content-designer:microcopy-flow-design
  context: "Positioning defines the strategic 'why' and 'who' before tactical launch planning and creative execution."
required_inputs:
  - Product capabilities (feature list or technical spec)
  - Target audience definition (ICP/Personas)
  - Competitive landscape (known competitors)
tool_stack:
  runtime:
    primary: [Ignition, Wynter]
    secondary: [Crayon, Klue, Notion]
  artifacts:
    primary: [Notion, Google Docs]
  fallback:
    primary: [Google Search, Internal Docs]
---

# Positioning Brief

## 2. Purpose
This skill defines how a product should be positioned against competitive alternatives to maximize perceived value for a specific target audience. It applies strategic reasoning to transform features into differentiated value pillars validated by real buyer intelligence.

## 3. Required Inputs and Assumptions
- **Required:** Product specs, current ICP, known competitors.
- **Known:** Current market category (if applicable).
- **Assumptions:** If missing, the agent will infer competitive alternatives based on the JTBD and label them as `[Assumed]`.

## 4. Input Mode and Evidence Path
1. **Live Interaction:** Extracting customer pain points from recent sales calls or interview transcripts (Gong/Chorus).
2. **Structured Access:** Querying **Crayon/Klue** for real-time competitor feature sets.
3. **Design Artifacts:** Reviewing product roadmaps in **Ignition**.
4. **Inference:** Mapping feature value based on industry benchmarks.

## 5. Tool Stack (Capabilities)
Defined in frontmatter. Key capabilities include high-fidelity message testing (Wynter) and GTM orchestration (Ignition).

## 6. Tool Routing (Decision System)
- **IF** competitive data is needed **USE** [Crayon/Klue].
- **IF** messaging needs validation with real buyers **USE** [Wynter].
- **IF** orchestrating the launch assets and feature-to-benefit mapping **USE** [Ignition].
- **IF** only static docs exist **USE** [Internal Search/Notion].

## 7. Environment and Reproducibility
Capture the current market conditions (e.g., "SaaS market saturation in Category X") and the version of the product being positioned (e.g., "v2.0 Beta").

## 8. Model Building (Before Analysis)
Before analysis, construct a **Positioning Model**:
- **Alternatives:** What would customers do if we didn't exist? (Include 'do nothing' or 'spreadsheets').
- **Attributes:** Unique features only we have.
- **Value:** The benefit those attributes provide (mapped to JTBD).
- **Customers:** Who cares most about that value?
- **Category:** The market context that makes the value obvious.

## 9. Core Method Execution
1. **Competitive Audit:** Identify alternatives using Crayon/Klue.
2. **Unique Attribute Mapping:** List capabilities that differentiate the product.
3. **Value Discovery (JTBD):** Translate attributes into functional and emotional outcomes.
4. **Segment Selection:** Match the highest value to the most underserved customer segment.
5. **Message Testing (Wynter):** Draft 3 messaging variants and simulate/run buyer preference tests.

## 10. Structured Findings
- **Finding:** [Observation]
- **Evidence:** [Link to Wynter test or Competitor Site]
- **Impact:** [High/Med/Low]
- **Confidence:** [Certainty score based on source]

## 11. Prioritization Logic
- **Primary Differentiators:** Features that are both unique and high-value.
- **Table Stakes:** Features that are high-value but not unique (group these).
- **Niche Wins:** Unique but low-volume value points.

## 12. Pattern Detection
Identify recurring buyer objections or "messaging friction" where the value proposition is misunderstood by the test panel.

## 13. Recommendations
- **Directional:** "Shift focus from 'Efficiency' to 'Risk Mitigation' based on Wynter feedback."
- **Actionable:** "Update the homepage hero section to reflect the JTBD: [New Copy]."

## 14. Coverage Map
- **Deeply Analyzed:** Competitive alternatives, Core value pillars.
- **Partially Analyzed:** Long-tail customer segments.
- **Not Analyzed:** Pricing strategy (unless specified).

## 15. Limits and Unknowns
- Requires real-world conversion data for final validation.
- Confidence is lower in emerging market categories where alternatives are not yet established.

## 16. Workflow Rules
- Build the Positioning Model (Step 8) before writing a single message.
- Distinguish between "Functional Benefit" and "Differentiated Value."
- No hallucinated competitor features; use evidence-based data only.

## 17. Output Contract
- **Target:** `knowledge/go-to-market-positioning-brief.md`
- **Constraint:** Do not modify the `## Strategy` section if it was already approved by a human agent.
- **Section Updated:** Append findings to the project-specific GTM log.
