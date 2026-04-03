---
name: partner-thesis
description: Define a data-driven ecosystem-led growth (ELG) strategy and partner prioritization model using 2026 PRM/ELG tools.
trigger: When partnership exploration, ecosystem-led growth (ELG) strategy, or partner prioritization is needed.
best_guess_output: A comprehensive partner thesis with ROI-driven rationale and Nearbound execution paths.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market-partner-thesis.md
section_anchor: partner-thesis
done_when: The partnership strategy is specific enough to initiate automated account mapping (Crossbeam/Reveal) or PRM onboarding (PartnerStack/Impartner).
required_inputs:
  - Product positioning brief
  - CRM account data (for mapping)
  - Ideal Customer Profile (ICP)
tool_stack:
  runtime:
    primary: [Crossbeam, Reveal, PartnerStack]
    secondary: [Impartner, Impact.com]
  artifacts:
    primary: [go-to-market/positioning-brief, crm-export]
---

# Partner Thesis (Ecosystem-Led Growth & Nearbound)

## 2. Purpose
This skill applies **Ecosystem-Led Growth (ELG)** reasoning to identify, prioritize, and model high-impact partnerships. It moves beyond generic lists to define **Nearbound** execution paths—leveraging partner signals to influence sales cycles and increase close rates. It does NOT manage daily partner operations; it defines the strategic thesis for the ecosystem.

## 3. Required Inputs and Assumptions
- **Required Inputs:** Target ICP, core product value proposition, and (if accessible) CRM account lists for overlap analysis.
- **Known vs. Unknown:** Knowns include current product limits; unknowns often include specific partner churn rates or internal partner program health.
- **Assumptions:** In the absence of live Crossbeam/Reveal data, the agent will assume overlap based on market adjacency and segment density, labeling these as "Inferred Overlaps."

## 4. Input Mode and Evidence Path
1. **Live Interaction:** Real-time account mapping via Crossbeam or Reveal API (Highest Fidelity).
2. **Structured System Access:** PRM portal exports (PartnerStack/Impartner) or CRM partner tags.
3. **Design Artifacts:** Existing partner tiers or ecosystem maps.
4. **Inference:** Competitive analysis and market adjacency mapping (Last Resort).

## 5. Tool Stack (Capabilities)
- **Primary (Mapping & ELG):** **Crossbeam** and **Reveal** for identifying account overlaps and "Nearbound" influence opportunities.
- **Secondary (Management & Payouts):** **PartnerStack** for B2B SaaS channel automation and **Impartner** for enterprise-grade PRM and AI-driven churn prediction.
- **Performance (Creators/Affiliates):** **Impact.com** for performance-driven creator and affiliate programs with advanced CAC/ROI attribution.

## 6. Tool Routing (Decision System)
- **if:** Live account mapping is possible → **use:** [Crossbeam, Reveal] for data-driven overlap analysis.
- **if:** Scaling a B2B SaaS referral/reseller program → **use:** [PartnerStack] for payout automation.
- **if:** Enterprise-scale complexity with AI prediction needed → **use:** [Impartner] for "Multiplier" AI agent support.
- **if:** Influencer/Creator-led growth is the focus → **use:** [Impact.com] for ROI tracking.

## 7. Environment and Reproducibility
- **State:** Must capture the date of overlap analysis (account mapping data becomes stale quickly).
- **Version:** Note the specific version of the product positioning being used as the thesis anchor.

## 8. Model Building (Before Analysis)
Before evaluating individual partners, the agent must construct:
- **Ecosystem Map:** A visual/conceptual model of "Who owns the trust" for the target ICP.
- **Nearbound Influence Model:** Identifying which partners have the most overlap with the CURRENT sales pipeline vs. the total addressable market (TAM).

## 9. Core Method Execution
1. **Category Identification:** Segment partners into Tech, Channel, Service, and Marketplace (AWS/Azure/GCP).
2. **Account Overlap Analysis:** Use Crossbeam/Reveal (or inference) to find "Strongholds" where partners have high customer density in our target accounts.
3. **Value Exchange Modeling:** Define the "Give/Get" for each tier (e.g., Tech partners give integrations/stickiness, get co-marketing).
4. **Marketplace-First Filter:** Evaluate the thesis against Cloud Marketplaces to ensure transactional ease.
5. **Nearbound Playbook Drafting:** Define how AEs will use partner signals to "warm up" cold outreach.

## 10. Structured Findings
- **Partner Profile Name:**
- **Category:** [Tech/Service/Channel/Creator]
- **Evidence/Overlap Ratio:** [e.g., 40% Overlap in Tier 1 Accounts]
- **Value Prop to Partner:**
- **Expected ROI Impact:** [High/Med/Low]
- **Confidence:** [Based on data source]

## 11. Prioritization Logic
- **Priority 1 (Strategic Overlap):** High overlap in current "Open Opportunities" (Nearbound play).
- **Priority 2 (Ecosystem Gap):** Partners who fill a critical product gap identified in the positioning-brief.
- **Priority 3 (Marketplace Leverage):** Partners that accelerate Cloud Marketplace transactions.

## 12. Pattern Detection
Identify:
- **Coalition Clusters:** Groups of partners that frequently co-exist in successful deals.
- **Integration Chokepoints:** Technical blockers preventing high-overlap partners from being viable.
- **Signal Multipliers:** Specific partners whose "intro" has a historically higher conversion rate.

## 13. Recommendations
- **Strategic Next Steps:** Link directly to findings (e.g., "Initiate Crossbeam mapping with Partner X due to 60% segment overlap").
- **Directional Advice:** "Shift to Marketplace-First billing for the EMEA region to reduce friction."

## 14. Coverage Map
- **Deeply Analyzed:** Tier 1 Tech and Channel partners.
- **Partially Analyzed:** Long-tail service partners.
- **Not Analyzed:** Geographical-specific partners in non-target regions.

## 15. Limits and Unknowns
- Cannot validate the "willingness to co-sell" of specific partner AEs without live interaction.
- ROI predictions are subject to partner program "noisy" data (e.g., poorly tracked attribution in legacy CRMs).

## 16. Workflow Rules
- **Model Before Analysis:** Never list partners without first mapping the ecosystem.
- **Fact vs. Inference:** Clearly label inferred overlaps if live mapping is unavailable.
- **Nearbound-First:** Prioritize "who can help us win now" over "who looks good on paper."

## 17. Output Contract
- **Target File:** `logs/active/<project-slug>/deliverables/go-to-market-partner-thesis.md`
- **Link Result:** Must be linked in `orchestrator.md`.
- **Reflection Mandatory:** Every thesis must conclude with a `## Reflection` on the data quality used.
