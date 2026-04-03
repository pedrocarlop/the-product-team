---
name: research-plan
description: Apply decision-first research planning — audit what decisions need to be made, formulate questions that reduce uncertainty, select methods by attitudinal/behavioral × qualitative/quantitative fit, design samples tied to questions not availability, and scope outputs before the study runs.
trigger: When the team needs a structured study plan rather than ad hoc interviews, or when research scope, method, or sample has not been formally decided.
required_inputs:
  - Product or design decision to be informed
  - Known constraints (timeline, budget, access to participants)
recommended_passes:
  - decision-audit
  - question-formulation
  - method-selection
  - sample-design
  - risk-assessment
  - output-scoping
tool_stack:
  runtime:
    primary: notion
    secondary: dovetail
  artifacts:
    primary: aurelius
  fallback:
    primary: search_query, reference/ground
tool_routing:
  - if: notion is available
    use: notion — write and maintain the living plan linked to the project brief
  - if: prior research may exist
    use: dovetail — search existing studies before committing to a new one
  - if: traceability from question to insight is required
    use: aurelius — link plan questions to eventual findings
  - if: team is on Atlassian stack
    use: confluence — link plan to Jira epics instead of Notion
  - if: collaborative question framing is needed
    use: miro or figjam — run a framing session before writing the plan
  - if: all primary tools are unavailable
    use: search_query, reference/ground — best-guess output; label as inferred
best_guess_output: A research plan with decision context, prioritized research questions, method selection rationale, sample design, risk register, and output scope.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher-research-plan.md
done_when: Every research question maps to a product decision, every method choice is justified against the question type, sample is specified with profile and size rationale, risks are documented, and the plan can be executed without inventing protocol details later.
---

## Purpose

This skill applies decision-first research planning. It uses the GQM (Goal-Question-Metric) framework to anchor questions to goals, the decision impact × uncertainty matrix to prioritize, and the attitudinal/behavioral × qualitative/quantitative method selection matrix to choose the right method per question.

It does NOT conduct the study. It does NOT synthesize findings. It does NOT generate participant screeners or discussion guides — those are downstream skills.

---

## Required Inputs and Assumptions

**Required inputs:**
- The product or design decision the research must inform (e.g., "whether to redesign onboarding" or "which of two navigation models to ship")
- Known constraints: timeline, recruiting access, budget, team availability

**Known vs. unknown at plan time:**
- Known: decision framing, rough timeline, team context
- Often unknown: exact participant availability, whether prior research covers the question

**Assumption rule:** If inputs are missing, infer them from available context and label each inference as an assumption. State assumptions explicitly in the plan. Do not proceed silently.

---

## Input Mode and Evidence Path

Evidence gathering hierarchy for research planning:

1. Live/real interaction — not applicable at plan stage
2. Structured system access — search Dovetail or Notion for prior research that may already answer the question
3. Design artifacts/documentation — review existing briefs, specs, or OKRs to extract the decision context
4. Screenshots/static input — review any shared mockups or flows that define what is being studied
5. Inference — if no prior evidence exists, the plan is built from the decision context and stated assumptions

**Path used at plan stage:** primarily (2) and (3), with (5) as fallback. Limitation: if Dovetail or Notion are unavailable, prior research overlap cannot be confirmed and must be flagged as a risk.

---

## Tool Stack

**Runtime primary — Notion:** Write and maintain the living research plan. Link to the project brief, OKRs, and downstream deliverables. Best for plans that evolve as scope changes.

**Runtime secondary — Dovetail:** Search the research repository before finalizing questions. Confirms whether existing evidence already answers a question, preventing redundant studies.

**Artifacts — Aurelius:** Link each research question in the plan to the insights it eventually generates. Required when the team needs provenance from question → evidence → decision.

**Fallback — Confluence:** Use in Atlassian-led organizations. Link the plan to Jira epics for traceability in engineering-led workflows.

**Collaborative framing — Miro / FigJam:** Use to run a team framing session when the decision context is unclear before writing the plan.

**Final fallback — search_query, reference/ground:** Produce a best-guess plan when all structured tools are unavailable. Label output as inferred.

---

## Tool Routing

| Condition | Tool |
|---|---|
| Notion available | Write plan in Notion; link to brief and deliverables |
| Prior research may exist | Check Dovetail before formulating questions |
| Traceability required | Register questions in Aurelius |
| Atlassian stack | Use Confluence; link to Jira epics |
| Question framing is ambiguous | Use Miro or FigJam for collaborative session |
| All tools unavailable | search_query + reference/ground; label output as inferred |

Prefer combining tools: Dovetail check → Notion plan → Aurelius registration is the standard chain for mature research orgs.

---

## Environment and Reproducibility

**Platform:** not applicable — plan is a document artifact, not a software execution
**Auth state:** Notion, Dovetail, and Aurelius require authenticated access; if access is missing, fall back to structured document output
**Version:** the plan should carry a version date and a status field (draft / approved / active / complete)
**Reproducibility:** all assumptions and tool paths used must be documented in the plan so another researcher can pick it up without context loss

---

## Model Building

Before selecting a method, the agent MUST construct a decision model:

**Step 1 — Decision audit:** What product or design decision does this study need to unlock? State it as a single actionable decision (e.g., "whether to proceed with concept A, B, or neither").

**Step 2 — Uncertainty mapping:** What is currently unknown that blocks that decision? List each unknown explicitly.

**Step 3 — Evidence check:** Does existing research (Dovetail, Notion) already reduce any of these unknowns? Flag covered unknowns as "may already be answered."

**Step 4 — Question formulation (GQM):** For each remaining unknown, write a research question using GQM:
- Goal: what you want to understand
- Question: what you need to ask to achieve that goal
- Metric: how you will know the answer

No method is selected until this model is complete. No conclusions before model construction.

---

## Core Method Execution

Follow this sequence exactly:

**1. Decision audit**
State the decision in one sentence. Identify who makes it and when. Confirm the decision is real and blockers are unknown.

**2. Prior research check**
Query Dovetail (or available repository) for studies addressing similar questions. Document findings: covered / partially covered / not covered.

**3. Question formulation using GQM**
For each remaining unknown, write one research question. Apply GQM: Goal → Question → Metric. Each question must map to exactly one decision.

**4. Method selection**
Use the attitudinal/behavioral × qualitative/quantitative matrix:
- Attitudinal + qualitative: interviews, diary studies — use for understanding mental models and motivations
- Attitudinal + quantitative: surveys — use for measuring attitudes at scale
- Behavioral + qualitative: usability testing, contextual inquiry — use for observing task performance and friction
- Behavioral + quantitative: analytics, A/B testing — use for measuring behavior at scale

Select the method that best reduces uncertainty for the question type. Do not default to interviews for all questions.

**5. Sample design**
Tie the sample profile to the question, not to availability. Specify: segment, inclusion criteria, exclusion criteria, size rationale, and recruitment approach.

**6. Risk assessment**
Identify threats to validity: recruitment failure, selection bias, demand characteristics, method-question mismatch, scope creep.

**7. Output scoping**
Define what the study will produce: artifact types, readout format, audience, timing, and the decision it feeds.

---

## Structured Findings

Each research question in the plan must be written in this schema:

```
Research Question: [single clear question]
Decision it unlocks: [the product or design decision]
Method: [chosen method and why it fits]
Sample size and profile: [segment, size, rationale]
Recruitment approach: [channel, screener criteria, timeline]
Risk / bias: [top 1–2 threats and mitigations]
Confidence level needed: [directional / moderate / high — and why]
```

One schema block per research question. Do not combine multiple questions into one block.

---

## Prioritization Logic

Prioritize research questions using: **impact of decision × uncertainty of answer**

| Impact | Uncertainty | Priority |
|---|---|---|
| High | High | Must answer — top priority |
| High | Low | Answer quickly — may already be covered |
| Low | High | Group with other low-stakes questions or deprioritize |
| Low | Low | Cut — not worth a study slot |

**Must-answer questions** are flagged with a `[MUST ANSWER]` marker in the plan.

**Low-stakes grouping:** combine low-impact questions into a single generative study if they share a method and sample profile.

---

## Pattern Detection

Before finalizing the plan, the agent must check for:

- **Overlapping questions:** two questions that would be answered by the same data — merge or drop one
- **Method-question mismatches:** e.g., using a survey to understand a complex mental model — flag and correct
- **Scope creep signals:** more than five distinct research questions in one study — split or deprioritize
- **Under-specified samples:** sample defined only as "users" or "customers" without segment, behavior, or lifecycle criteria — reject and specify

Flag detected issues in the plan before proceeding to output.

---

## Recommendations

Every recommendation must link to a decision:

- State which decision the recommendation serves
- Assess method fit: is the proposed method the right type (attitudinal/behavioral × qualitative/quantitative) for the question?
- Assess sample tradeoffs: convenience sample vs. representative sample — flag when convenience sample introduces interpretive limits
- Flag when a question is better answered by existing data (analytics, prior studies) than a new study

Do not recommend a method without justifying it against the question type.

---

## Coverage Map

The plan must include a coverage map with three columns:

| Decision | Coverage | Notes |
|---|---|---|
| [Decision A] | Fully covered | Covered by Q1 via [method] |
| [Decision B] | Partially covered | Q2 covers attitudes; behavior unmeasured |
| [Decision C] | Out of scope | Requires data not available in this study |

"Out of scope" items must be explicitly named — not omitted.

---

## Limits and Unknowns

The plan cannot guarantee:

- **Recruitment success:** participant availability and screener pass rates are uncertain until recruiting begins
- **Participant quality:** self-reported behavior and attitudes may diverge from actual behavior
- **Method execution fidelity:** usability tests and interviews depend on facilitator skill and participant engagement
- **Generalizability:** qualitative samples produce directional evidence, not statistically representative findings
- **Prior research completeness:** the Dovetail check is only as good as what has been logged; undocumented research is invisible

These limits must be stated in the plan. Do not imply higher confidence than the method and sample support.

---

## Workflow Rules

1. Build the decision model before selecting any method.
2. Check for prior research before formulating new questions.
3. Tie the sample to the question, not to what is easiest to recruit.
4. Do not invent sample profiles — if the segment is unknown, state that and flag it as a plan risk.
5. Document what the study will NOT answer in the coverage map.
6. Flag all assumptions made due to missing inputs.
7. Do not run pattern detection after writing the plan — run it during question formulation.
8. Label the plan section as `sourced`, `fallback`, or `inferred` based on the tool path used.

---


### Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/ux-researcher-research-plan.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.
