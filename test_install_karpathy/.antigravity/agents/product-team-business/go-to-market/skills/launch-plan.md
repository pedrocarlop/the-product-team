---
name: launch-plan
description: Orchestrates the end-to-end launch workflow using 2026 GTM standards, centering on predictive readiness and multi-tool orchestration.
trigger: When a product feature or initiative is scheduled for market release or enters a dedicated GTM phase.
best_guess_output: A predictive launch plan with integrated readiness gates, workstream owners, and risk-adjusted milestones.
output_artifacts: knowledge/go-to-market-launch-plan.md
section_anchor: launch-plan
done_when: The launch plan is signed off with all critical path dependencies mapped and readiness gates defined.
mesh:
  inputs:
    - platform-engineer:infra-release
    - go-to-market:positioning-brief
    - go-to-market:campaign-brief
  next:
    - go-to-market:sales-enablement
  context: "Orchestrates the transition from product development to market execution."
required_inputs:
  - Positioning Brief (positioning-brief.md)
  - Campaign Brief (campaign-brief.md)
  - Product Roadmap (Productboard/Linear)
tool_stack:
  runtime:
    primary: [Ignition, Linear, Productboard]
    secondary: [Asana, Monday.com]
  artifacts:
    primary: [Gong, Intercom, Slack]
---

# Launch Plan

## 2. Purpose
This skill orchestrates the transition from product development to market execution. It applies **predictive launch reasoning** to align product readiness with marketing momentum. It does NOT perform technical QA or direct media buying; it manages the **orchestration of readiness**.

## 3. Required Inputs and Assumptions
### Required Inputs
| Input | Source | Purpose |
| :--- | :--- | :--- |
| Positioning Brief | `positioning-brief` | Defines the "Who" and "Why" |
| Campaign Brief | `campaign-brief` | Defines the "How" and creative direction |
| Roadmap Sync | Productboard | Defines the "What" and target dates |
| Readiness Sync | Linear | Defines the technical "Can we" |

### Assumptions
- A target launch window has been identified.
- Core positioning is stable enough for workstream initiation.
- If specific tool access is missing, the agent will infer based on the most recent project documentation.

## 4. Input Mode and Evidence Path
The skill follows this evidence hierarchy:
1. **Direct Integration**: Live data from Ignition (Launch OS), Productboard (Roadmap), and Linear (Technical debt/readiness).
2. **Design/Release Artifacts**: PRDs, Figma specs, Engineering RFCs.
3. **Static Interaction Logs**: Slack threads, Gong snippets for sales feedback.
4. **Agent Inference**: Based on historical project patterns.

*Limitation: Static documentation may lag behind live tool state. Always timestamp the "Last Sync" in the output.*

## 5. Tool Stack (Capabilities)
- **Runtime**:
    - Primary: [Ignition GTM OS] # For launch orchestration and predictive gating
    - Secondary: [Productboard, Linear] # For source-of-truth syncing
- **Artifacts**:
    - Primary: [Markdown Deliverable]
    - Fallback: [Notion/Docs]

## 6. Tool Routing (Decision System)
- **IF** Ignition is available: Use as the central GTM OS for milestone tracking and asset orchestration.
- **IF** Productboard is accessible: Extract feature scope and milestone dates directly.
- **IF** Linear status is "In Progress" or "Blocked": Automatically flag the corresponding Launch Gate as "At Risk".
- **IF** Zero tool access exists: Rely on `positioning-brief` and `campaign-brief` to construct a best-guess plan.

## 7. Environment and Reproducibility
- **Current Era**: 2026 Product Marketing Environment.
- **Tool Context**: Standard SaaS GTM Stack (Ignition-centric).
- **State**: Requires knowledge of current "Launch Tiers" (P1, P2, P3) and corresponding resource allocation.

## 8. Model Building (Before Analysis)
Before drafting the plan, the agent must build the **Launch Readiness Model (LRM)**:
- **Workstream Mapping**: Product, Marketing, Sales, Support, Operations.
- **Dependency Graph**: Map "Product Readiness" (Linear) -> "Sales Enablement" (Ignition) -> "Public Launch".
- **Gate Definitions**: Define Go/No-Go criteria for each phase (Internal Alpha, Beta, GA).

## 9. Core Method Execution
The workflow follows the **2026 Orchestration Framework**:
1. **Sync Scope**: Import features from Productboard.
2. **Map Workstreams**: Create owners for messaging, enablement, demand gen, and technical readiness in Ignition.
3. **Establish Gates**: 
   - Gate 1: Messaging Lock (Based on Positioning Brief)
   - Gate 2: Enablement Ready (Assets generated in Ignition)
   - Gate 3: Technical Confidence (Linear milestone completion > 90%)
4. **Predictive Risk Assessment**: Analyze historical velocity to predict if the GA date is realistic.
5. **Asset Alignment**: Map specific assets (from Campaign Brief) to launch phases.

## 10. Structured Findings
For any risk or blocker identified:
- **Finding**: [Risk Name]
- **Observation**: [What was seen in Linear/Productboard]
- **Evidence**: [Link or Quote]
- **Impact**: [How it affects the GA date]
- **Confidence**: [High/Med/Low]

## 11. Prioritization Logic
- **Critical Path First**: Any item that directly impacts the GA date.
- **P1 Workstreams**: Messaging and Sales Enablement are prioritized over secondary social proof.
- **Risk Weighting**: High-impact dependencies in Linear are surfaced over minor UX polish.

## 12. Pattern Detection
Identify systemic GTM failures:
- **Messaging Lag**: Is the technical work moving faster than the positioning lock?
- **Enablement Gap**: Are sales teams being trained too close to the GA date?
- **Dependency Clusters**: Are too many workstreams reliant on a single individual or team?

## 13. Recommendations
Recommendations must be directional:
- "Shift GA date by +1 week to align with sales readiness."
- "Parallelize 'Sales Training' with 'Final Testing' to regain schedule."
- "De-scope [Feature X] to ensure P1 stability for launch."

## 14. Coverage Map
- **Deeply Analyzed**: Product scope, technical readiness, core GTM workstreams.
- **Partially Analyzed**: Channel-specific creative assets (if not in brief).
- **Not Analyzed**: Media budget optimization, Paid social delivery.

## 15. Limits and Unknowns
- Cannot validate real-time internal team sentiment without Slack/Intercom access.
- Predictive dates are based on current data and do not account for future "Black Swan" technical blocks.
- Requires project-specific "Launch Tiering" to be defined in inputs.

## 16. Workflow Rules
- **Model first**: Never suggest a date without mapping dependencies.
- **Evidence-based**: If a date comes from Productboard, say so.
- **Fact vs. Inference**: Clearly label predicted dates as "Projected".
- **No Hallucinations**: Do not invent feature specifications not present in the roadmap.

## 17. Output Contract
- **Target**: `knowledge/go-to-market-launch-plan.md`
- **Update Rule**: Overwrite with the latest version; preserve the "Changelog" section at the footer.
- **Prohibited**: Do not modify the core `positioning-brief` or `campaign-brief` files.
