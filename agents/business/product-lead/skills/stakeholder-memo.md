---
name: stakeholder-memo
description: Synthesize diverse signals into a high-stakes decision memo using the Pyramid Principle and Amazon 6-Page narrative styles.
trigger: When a product decision needs alignment, funding, or executive approval.
best_guess_output: A stakeholder memo with recommendation, risks, and asks.
output_artifacts: knowledge/product-lead-stakeholder-memo.md
section_anchor: stakeholder-memo
done_when: All primary stakeholders have received a clear, evidence-based recommendation with explicit asks and identified risks.
mesh:
  inputs:
    - product-lead:prioritize-roadmap
    - analyst:experiment-readout
    - product-lead:venture-discovery
  next:
    - go-to-market:launch-plan
    - business-ops:process-map
  context: "Memos consolidate delivery outcomes and strategic decisions for stakeholder alignment and external communication."
tool_stack:
  runtime:
    primary: [notion, loom, grain]
    secondary: [repository, slack]
  artifacts:
    primary: [notion]
  fallback:
    primary: [search_query, reference/verify]
tool_routing:
  - if: meeting/interview evidence is needed use: [grain]
  - if: asynchronous visual context is required use: [loom]
  - if: collaborative document creation use: [notion]
---

# Stakeholder Memo

## 2. Purpose
Prepare a concise decision memo or update for stakeholders. This skill applies narrative synthesis and risk-adjusted reasoning to drive organizational alignment. It explicitly does NOT perform deep technical architecture or financial auditing, but synthesizes their outputs into a directional brief.

## 3. Required Inputs and Assumptions
- **Required Inputs**: PRD, user research findings, interview transcripts (via Grain), current roadmap, and previous stakeholder feedback.
- **Known vs Unknown**: Identify which stakeholders have already been consulted.
- **Assumptions**: If stakeholder incentives are unclear, the agent must infer them via role analysis (e.g., Finance focus on ROI, Eng focus on debt) and label as assumptions.

## 4. Input Mode and Evidence Path
Follow this hierarchy:
1. **Live Interaction**: Real-time signals from meeting logs or interviews (Grain).
2. **Structured System Access**: Data from Notion/Repository (GitHub/Linear).
3. **Design Artifacts**: Screenshots or Figma links.
4. **Asynchronous Context**: Loom recordings for walkthroughs.
5. **Inference**: Sentiment mapping based on communication patterns (Slack/Email).

## 5. Tool Stack (Capabilities)
- **Primary Runtime**: Notion (collaboration), Loom (video context), Grain (meeting evidence).
- **Secondary Runtime**: Repository (source of truth), Slack (sentiment).
- **Artifacts**: Notion (target deliverable).
- **Fallback**: Search/Verify.

## 6. Tool Routing (Decision System)
- **If** meeting evidence is the primary source **use** [grain] to extract specific quotes and sentiment.
- **If** the memo requires a visual walkthrough of a prototype or plan **use** [loom] to embed context.
- **If** gathering distributed feedback from the team **use** [notion] for collaborative drafting.

## 7. Environment and Reproducibility
- **Platform**: Notion-based documentation workspace.
- **State**: Capture the "As-Of" date for all status updates and the specific version of the roadmap referenced.

## 8. Model Building (Before Analysis)
Before drafting the memo, the agent must construct:
- **Stakeholder Influence Map**: A matrix mapping power vs. interest to identify key "blockers" and "champions."
- **Decision Tree**: A visualization of the primary recommendation versus the "Do Nothing" or "Alternative" paths, including branching consequences.

## 9. Core Method Execution
The workflow must follow these expert frameworks:
1. **Narrative Synthesis (Amazon 6-Page Style)**: Focus on the "Future Press Release" and "FAQs" logic—writing for clarity and reading-first meetings.
2. **Pyramid Principle**: Lead with the answer (Recommendation), followed by supporting arguments, then data.
3. **Risk-Adjusted Recommendation**: Each proposal must include a "Type 1 vs Type 2" decision classification (Irreversible vs. Reversible).

## 10. Structured Findings
Every signal cited in the memo must follow this schema:
- **Finding**: [Clear Header]
- **Observation**: [The raw signal from Grain/Slack]
- **Evidence**: [Specific quote or link]
- **Impact**: [High/Med/Low impact on the decision]
- **Confidence**: [Level of certainty in the signal]

## 11. Prioritization Logic
- **Executive Summary First**: The recommendation must be visible without scrolling.
- **Type 1 Decisions**: Prioritize irreversible decisions for deep analysis.
- **Pattern Grouping**: Group minor stakeholder concerns into "Systemic Patterns" (e.g., "General lack of clarity on GTM").

## 12. Pattern Detection
Identify and call out:
- **Decision Fatigue**: When leadership is being asked to make too many small choices.
- **Misaligned Incentives**: When the recommendation creates value for the product but friction for a specific department (e.g., Sales vs. Product).

## 13. Recommendations
- Must be directional (e.g., "Proceed with Beta" not "The team thinks...").
- Links directly to the "Evidence" section.
- Includes a "Risk Mitigation" step for every primary recommendation.

## 14. Coverage Map
- **Deeply Analyzed**: [e.g., Product-Market Fit signals, Technical Feasibility]
- **Partially Analyzed**: [e.g., Long-term cost maintenance]
- **Not Analyzed**: [e.g., Legal compliance, Tax implications]

## 15. Limits and Unknowns
- State what could not be validated (e.g., "Customer reaction to the new pricing model is speculative").
- Define what requires real-world testing (e.g., "A/B test needed to confirm conversion lift").

## 16. Workflow Rules
- **Build the Stakeholder Map first**.
- **Distinguish fact vs. inference** using tags.
- **No Hallucinations**: Every quote must be traceable to Grain or repository logs.

## 17. Output Contract
### Lossless Deliverable Contract
- Produce a standalone deliverable at the path specified in `output_artifacts`.
- **Formatting**: `knowledge/product-lead-stakeholder-memo.md`.
- **Do not merge** into primary role docs.
- **Include reflection**: `## Reflection` with `What worked`, `What didn't`, and `Next steps`.

### Required Deliverable Sections:
- `### Recommendation`: The core ask.
- `### Context & The "Why Now"`: The forcing function.
- `### Analysis of Alternatives`: Why the other paths were rejected.
- `### Stakeholder Alignment Status`: Who is "In" and who has "Concerns."
- `### Risks & Mitigation`: The "Pre-Mortem" results.
- `### Immediate Asks`: Clear list of decisions needed today.
- `## Reflection`: What worked/didn't, next steps.
