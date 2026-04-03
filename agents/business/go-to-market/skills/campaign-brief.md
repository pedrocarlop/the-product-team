---
name: campaign-brief
description: Orchestrates and executes integrated marketing campaigns using cross-channel signals and AI-driven automation.
trigger: When a new product feature, seasonal event, or market opportunity requires a coordinated marketing execution.
best_guess_output: A comprehensive campaign brief including asset mapping, channel strategy, and automation routing.
output_artifacts: logs/active/<project-slug>/deliverables/go-to-market-campaign-brief.md
section_anchor: Campaign Execution
done_when: All 17 sections are complete and the campaign-audience-asset model is fully mapped with evidence-based tool routing.
required_inputs:
  - product_update_specs
  - target_audience_segments
  - campaign_goals_kpis
  - available_budget_ranges
tool_stack:
  runtime:
    primary: [HubSpot, Salesforce]
    secondary: [Guideflow, Mutiny]
  artifacts:
    primary: [Jasper, Copy.ai]
tool_routing:
  - if: "PLG or high-conversion demo flow is required"
    use: [Guideflow]
  - if: "Hyper-personalization at the web edge is needed"
    use: [Mutiny]
  - if: "Enterprise ABM and CRM-tight orchestration is needed"
    use: [Salesforce Agentforce]
  - if: "Inbound-focused multi-channel execution is needed"
    use: [HubSpot Breeze]
---

# Campaign Brief

## 2. Purpose
The `campaign-brief` skill translates high-level marketing goals into an executable, evidence-based plan. It applies **Channel-Audience-Asset (CAA)** reasoning to ensure every campaign touchpoint is grounded in data and optimized for 2026 autonomous execution environments. It does NOT perform creative design or manual copy testing; it defines the architecture for AI agents to execute those tasks.

## 3. Required Inputs and Assumptions
*   **Target Segments:** Defined personas or ICP (Ideal Customer Profile) data.
*   **Core Message:** The primary value proposition (assumed from `positioning-brief` if not provided).
*   **KPIs:** Success metrics (e.g., pipeline generated, demo conversion rate).
*   **Assumptions:** If budget is not specified, assume a "performance-optimized" tier. If channels are not specified, assume a multi-channel mix (Social, Email, Web, Search).

## 4. Input Mode and Evidence Path
1.  **Live Interaction:** Real-time customer signals from CRM (HubSpot/Salesforce).
2.  **Structured System Access:** Historical campaign performance logs.
3.  **Design Artifacts:** Existing brand guidelines and positioning briefs.
4.  **Inference:** Using 2026 market benchmarks to fill gaps in audience behavior.

## 5. Tool Stack (Capabilities)
*   **Orchestration (Primary):** HubSpot Breeze AI (Inbound) / Salesforce Agentforce (Enterprise).
*   **Conversion (Secondary):** Guideflow (Interactive Demos), Mutiny (Web Personalization).
*   **Content Generation (Artifacts):** Jasper Brand AI (Full-funnel consistency), Copy.ai (Workflow automation).

## 6. Tool Routing (Decision System)
*   **High-Volume B2B:** Route to HubSpot for self-optimizing "Breeze" workflows.
*   **Enterprise ABM:** Route to Salesforce Agentforce for proactive account-level triggers.
*   **Frictionless Conversion:** Deploy Guideflow demos for complex SaaS features.
*   **Dynamic Landing Pages:** Route conversion optimization to Mutiny AI edge rules.

## 7. Environment and Reproducibility
*   **Platform:** 2026 Marketing Technology Stack.
*   **State:** Requires authenticated access to CRM and Content Orchestrators.
*   **Version:** All briefs must reference the current "Brand AI" version for Jasper/Copy.ai consistency.

## 8. Model Building (Before Analysis)
The agent must construct a **Channel-Audience-Asset (CAA) Model**:
1.  **Map Personas:** Cross-reference audience segments with specific pain points.
2.  **Inventory Assets:** Identify required videos, demos (Guideflow), and personalized web components (Mutiny).
3.  **Define Flows:** Map the user journey from initial signal to final conversion.

## 9. Core Method Execution
1.  **Signal Analysis:** Analyze CRM data via Breeze/Agentforce to identify high-intent audience clusters.
2.  **Asset Mapping:** Generate a manifesto of assets required for each channel using Jasper.
3.  **Personalization Logic:** Define Mutiny rules for dynamic content based on landing page triggers.
4.  **Demo Integration:** Sequence Guideflow interactive demos into the high-intent stages of the funnel.
5.  **Workflow Configuration:** Define the triggers for autonomous AI agents to launch and optimize the campaign.

## 10. Structured Findings
*   **Finding:** Gaps in asset coverage for specific funnel stages.
*   **Evidence:** CAA Model vs. existing asset inventory.
*   **Impact:** Potential drop-off in the "Evaluation" phase of the buyer journey.
*   **Confidence:** High (based on asset inventory audit).

## 11. Prioritization Logic
1.  **Critical:** Revenue-generating conversion paths (Guideflow demo flows).
2.  **High:** High-reach channel assets (Social/Email).
3.  **Medium:** Secondary nurturing sequences.
4.  **Patterns:** Group low-impact asset requests into singular "Brand Package" updates.

## 12. Pattern Detection
*   **Segment Drift:** Detecting when audience signals no longer align with the core message.
*   **Automation Fatigue:** Identifying overlapping triggers in HubSpot/Salesforce that may lead to over-communication.
*   **Conversion Friction:** Systemic drops in demo engagement across multiple channels.

## 13. Recommendations
*   **Direct:** "Deploy Guideflow interactive demos on the 'Pricing' page to reduce friction."
*   **Pattern-Based:** "Re-train Jasper Brand AI on the new 'Value Proposition' to ensure cross-channel consistency."
*   **Workflow:** "Enable self-optimizing Breeze agents for the 'Mid-Market' segment."

## 14. Coverage Map
*   **Deep Analysis:** High-intent conversion paths and demo sequencing.
*   **Partial Analysis:** Top-of-funnel social awareness (requires creative-specific inputs).
*   **Not Analyzed:** Offline events or external PR agency coordination.

## 15. Limits and Unknowns
*   **Attribution:** 2026 privacy-first tracking may limit exact ROI per social post.
*   **Latency:** AI agent execution time in Salesforce might vary based on API load.
*   **Validation:** Final creative tone requires human brand-lead review.

## 16. Workflow Rules
*   **Model First:** Never write the brief before the CAA Model is complete.
*   **Evidence-Based:** Every asset request must be linked to a target segment pain point.
*   **Tool-Agnostic Method:** The strategy must hold even if tools change, though routing depends on tool capabilities.

## 17. Output Contract
*   **Target:** `logs/active/<project-slug>/deliverables/go-to-market-campaign-brief.md`
*   **Modified:** Updates the specific campaign brief file.
*   **Protected:** Must NOT modify global brand-voice files in `assets/`.
