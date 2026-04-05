---
name: frame-problem
description: Turn a raw, vague, or outcome-first request into a clear product problem, constraints, success criteria, and decision frame using 2026 AI-first discovery methods.
trigger: When the request is vague, outcome-first, or lacks a bounded problem definition.
mesh:
  inputs:
    - business-ops:tooling-audit
    - analyst:funnel-analysis
  next:
    - product-lead:write-prd
    - ux-researcher:research-plan
  context: "Frames the problem and success criteria before writing the PRD."
best_guess_output: A structured framing brief with a JTBD model, root-cause analysis (5 Whys), and crisp success criteria.
output_artifacts: knowledge/product-lead-frame-problem.md
done_when: The problem is crisply bounded, success measures are defined, and the decision frame is clear to the team.
tool_stack:
  runtime:
    primary: [lane, zeda_io]
    secondary: [chat_prd, notion]
  artifacts:
    primary: [repository, notion]
  fallback:
    primary: [search_query, reference_ground]
tool_routing:
  - if: "ecosystem feedback or massive unstructured signal exists"
    use: [zeda_io]
  - if: "alignment between discovery evidence and roadmap is needed"
    use: [lane]
  - if: "iterative logic-checking or edge-case discovery is required"
    use: [chat_prd]
mesh:
  inputs:
    - product-lead:venture-discovery # The business thesis provides the context for the product problem
    - ux-researcher:foundational-research # User behaviors ground the JTBD model
  next:
    - product-designer:problem-framing
    - product-lead:write-prd
  context: "Problem framing is the bridge between a broad business opportunity and a specific product specification or design challenge."
---

# Frame Problem

## 1. Purpose
Turn a raw request into a clear product problem, constraints, success criteria, and decision frame. This skill applies **critical framing** and **system thinking** to ensure the team solves the right problem before committing resources. It explicitly does NOT perform solutioning or detailed UI design.

## 2. Required Inputs and Assumptions
- **Required Inputs:** Raw request (vague/outcome-first), context on stakeholders, project slug.
- **Assumptions:** If context is missing, infer the most likely business intent based on the repository history and label it as `Assumption`.

## 3. Input Mode and Evidence Path
1. **Live Interaction / Logs:** Extract intent from recent chat/thread logs in the environment.
2. **Structured System Access:** Query `Lane` for discovery logs or `Zeda.io` for customer feedback signals.
3. **Design Artifacts:** Read existing PRDs or Roadmaps in `Notion` or the `Repository`.
4. **Inference:** Used as a last resort if primary evidence is missing.

## 4. Tool Stack (Capabilities)
- **Lane:** AI-driven discovery insights and alignment between signal and strategy.
- **Zeda.io:** Voice of the customer (VoC) aggregation and product signal extraction.
- **ChatPRD:** Rapid framing, clarifying questions, and logic-checking co-pilot.
- **Notion/Repository:** System of record for existing context and artifact persistence.

## 5. Tool Routing (Decision System)
- Use **Zeda.io** first if the request stems from "customer complaints" or "market feedback".
- Use **Lane** if the request is tied to a specific "strategic initiative" or "roadmap item".
- Use **ChatPRD** to generate the initial "5 Whys" and "JTBD" models through iterative prompting.
- Fallback to **Repository** search if tool-specific integrations are unavailable.

## 6. Environment and Reproducibility
- **State:** Projects must have an active `logs/active/<slug>` directory.
- **Reproducibility:** Capture the build/version of the prototype or documentation being analyzed to ensure findings are grounded in a specific state.

## 7. Model Building (Before Analysis)
Before evaluating the request, the agent must construct:
- **JTBD Model:** Define the "Job" (Situation, Motivation, Expected Outcome).
- **User Journey Map:** A high-level map of where this problem intersects the existing user flow.
- **Stakeholder Map:** Identify requester, impacted users, and final decision-makers.

## 8. Core Method Execution
1. **5 Whys Analysis:** Drill into the raw request to find the root problem (anchor to the "5 Whys" framework).
2. **Problem-Solution Fit Check:** Evaluate if the implied solution in the request actually addresses the root problem.
3. **Constraint Mapping:** Identify technical, legal, or business blockers.
4. **Success Metric Definition:** Define lagging (Impact) and leading (Behavioral) indicators.

## 9. Structured Findings
- **Observation:** What was heard/read?
- **Evidence:** Links to Zeda.io feedback or Lane discovery logs.
- **Cause:** Why is this a problem now?
- **Impact:** What happens if we DON'T solve this?
- **Confidence:** Score (1-5) based on evidence quality.

## 10. Prioritization Logic
- **Criticality:** Does this block the main user loop?
- **Alignment:** How well does this align with the project's strategic North Star?
- **Urgency:** Is there a competitive or compliance deadline?

## 11. Pattern Detection
- Identify if this request is a symptom of a larger **system-level gap** (e.g., recurring onboarding friction across multiple modules).
- Detect **broken mental models** where stakeholders confuse "features" with "outcomes".

## 12. Recommendations
- **Directional:** "Investigate [X]" or "Proceed with [Y] given [Z] constraints".
- **Risk Mitigation:** If confidence is low (<3), recommend a "Spike" or "Validation" phase.

## 13. Coverage Map
- **Deeply Analyzed:** Core problem, JTBD, success criteria.
- **Partially Analyzed:** Technical feasibility (requires Eng Lead verification).
- **Not Analyzed:** Competitive landscape, detailed UI/UX.

## 14. Limits and Unknowns
- State where the framing relies on unvalidated stakeholder opinions.
- List "Open Questions" that require synchronous meetings or further research.

## 15. Workflow Rules
- **Model Before Analysis:** Never draft the final problem statement without first mapping the JTBD.
- **Evidence-Based:** Every claim in the framing must be backed by a tool-sourced finding or explicit log snippet.
- **No Hallucinations:** If a metric or constraint is unknown, label it clearly as `UNKNOWN_REQUIRES_VALIDATION`.

## 16. Output Contract
- **Target Path:** `knowledge/product-lead-frame-problem.md`
- **Format:** Markdown with structured headers.
- **Preserve:** Do not overwrite the `## Reflection` section if it already exists; append any new reflection.

## 17. Lossless Deliverable Contract
Produce a standalone deliverable at the path specified in `output_artifacts` containing:
- `### Problem statement`: One crisp, bounded sentence.
- `### Objective and success criteria`: Outcomes and measures.
- `### Constraints and non-goals`: Captured dependencies and out-of-scope items.
- `### Decision frame`: Tradeoffs that matter for the next step.
- `### Open questions`: Unresolved issues.
- `## Reflection`: `What worked`, `What didn't`, and `Next steps`.

Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
