---
name: research-readout-deck
description: Structure and deliver research findings as a stakeholder-ready readout using the Pyramid Principle and narrative arc — leading with conclusions, anchoring every recommendation to evidence, and making the ask explicit.
trigger: When research findings must be socialized to decision-makers, sponsors, or cross-functional partners — especially when alignment, prioritization, or a go/no-go decision is on the line.
required_inputs:
  - Synthesized research findings or a completed research-synthesis output
  - Audience list with roles and stake in the decision
  - Decision or question the research was commissioned to answer
recommended_passes:
  - research-synthesis (prerequisite — findings must be synthesized before the readout is structured)
best_guess_output: A structured research readout with audience model, insight hierarchy, narrative arc, evidence highlights, recommendations, and stakeholder asks.
output_artifacts:
  - knowledge/runs/<run-id>/ux-researcher-research-readout-deck.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: The readout contains a complete audience-decision model, findings ordered by decision relevance, at least one recommendation linked to evidence with a stated confidence level, and an explicit stakeholder ask — and a stakeholder unfamiliar with the research could act on it in one pass.
tool_stack:
  runtime:
    primary: notion
    secondary: pitch, loom
  artifacts:
    primary: knowledge/ux-researcher.md
  fallback:
    primary: research-synthesis skill output, open/browser
tool_routing:
  - if: living research repository is needed and findings must remain discoverable post-presentation
    use: notion
  - if: executive audience requires a polished visual deck with co-editing and version history
    use: pitch
  - if: stakeholders are async or cross-timezone and need a narrated walkthrough
    use: loom
  - if: org is Atlassian-native and findings need to link to Jira tickets
    use: confluence
  - if: cross-functional team already working in Google Workspace
    use: google-slides
  - if: researcher needs branded one-pager without design skill dependency
    use: canva
  - if: no tool access
    use: best-guess output labeled as inferred
---

## Purpose

This skill structures synthesized research findings into a stakeholder-ready readout. It applies the Pyramid Principle (lead with the conclusion), narrative arc framing (situation → complication → resolution → recommendation), and executive communication best practices to ensure findings drive decisions — not just awareness.

It does NOT conduct research, recruit participants, analyze raw data, or produce a synthesis from scratch. It assumes findings are already synthesized. If they are not, run `research-synthesis` first.

---

## Required Inputs and Assumptions

**Required:**
- Synthesized research findings (themes, patterns, evidence)
- Audience: who will attend or consume the readout, their roles, and their stake in the outcome
- The decision or question the research was commissioned to answer

**Known vs Unknown:**
- If the audience list is unknown → infer from project context and label as assumption
- If the decision framing is unstated → infer from the research brief or synthesis and label as assumption
- If findings have not been synthesized → block and prompt to run `research-synthesis` first

**Rule:** Never skip the audience-decision model. If inputs are missing, infer them explicitly and state the assumption — do not silently proceed.

---

## Input Mode and Evidence Path

Evidence hierarchy used by this skill:

1. Live/real interaction — preferred when the researcher is presenting live and can respond to questions
2. Structured system access — Notion pages, Confluence docs, or Pitch decks with linked evidence
3. Design artifacts/documentation — synthesized research docs, affinity maps, research reports
4. Screenshots/static input — slide exports, static PDFs of findings
5. Inference — when no inputs are available; all inferred content must be labeled

**Path used for this skill:** Primarily (3) design artifacts/documentation, sourced from the `research-synthesis` output. If the synthesis is unavailable, the agent falls back to (5) inference and labels all content accordingly.

**Limitation:** This skill cannot verify whether stakeholders acted on the readout post-delivery. It cannot guarantee findings were not misinterpreted after the session.

---

## Tool Stack

**Runtime primary — Notion:** Living research repository. Use to store and share the readout as a structured doc that remains discoverable after the presentation. Supports inline comments, linked evidence, and versioning.

**Runtime secondary — Pitch:** Collaborative, design-forward slide deck tool with real-time co-editing and version history. Use when the readout is for an executive audience where visual quality and polish matter. Pitch decks should mirror the narrative arc and section structure defined below.

**Runtime secondary — Loom:** Async screen + webcam recording with chapters and time-stamped comments. Use when stakeholders are distributed or when the researcher cannot present live. Record a narrated walkthrough of the Notion doc or Pitch deck.

**Alternatives:**
- Confluence: when the org is Atlassian-native and findings need to be linked to Jira tickets
- Google Slides: when the cross-functional team is already in Google Workspace and zero-friction sharing is the priority
- Canva: when a branded one-pager or research infographic is needed and the researcher has no design support

**Fallback:** research-synthesis skill output as source material, open/browser for reference. Label output as `fallback` or `inferred`.

---

## Tool Routing

- Notion is the default doc layer. Always write the structured readout to Notion first.
- Add a Pitch deck layer when the audience is executive or the readout requires visual narrative support.
- Add a Loom layer when the team is async or when a narrated walkthrough increases comprehension.
- Switch to Confluence only when the org context makes Notion unsuitable (Atlassian-first).
- Use Google Slides as a drop-in for Pitch when collaboration friction is the primary constraint.
- Use Canva only for standalone one-pager artifacts, not as a replacement for the primary readout.
- Never route to a single tool when combining tools increases stakeholder reach (e.g., Notion doc + Loom walkthrough).

---

## Environment and Reproducibility

- Platform: web-based tools (Notion, Pitch, Loom, Confluence, Google Slides, Canva)
- Auth state: assumed to be authenticated per org setup; if not authenticated, fall back to best-guess output in the deliverable file
- Data state: findings must be finalized before the readout is structured; in-progress synthesis produces unstable readouts
- Version: readout sections should be versioned by date if the deck is updated post-delivery
- If environment is unknown → state explicitly and label all outputs as `inferred`

---

## Model Building

Before structuring the readout, the agent MUST construct an audience-decision model. No slides, no narrative arc, no findings ordering — until the model is complete.

**Audience-Decision Model:**

| Dimension | Questions to answer |
|---|---|
| Who are the stakeholders? | Roles, org level, relationship to the product/problem |
| What decision do they need to make? | Go/no-go, prioritization, investment, pivot, continue |
| What do they already believe? | Prior assumptions, existing mental models, anchored positions |
| What would change their mind? | Evidence type (qualitative, quantitative), threshold of confidence, messenger credibility |
| What is at stake for them? | Career, budget, roadmap, team direction |

The model is written explicitly in the readout under `### Audience and decision`. It is not internal scaffolding — it is a deliverable section because misaligned audience models are the most common reason readouts fail to drive decisions.

---

## Core Method Execution

The readout is constructed in five sequential steps. Do not skip steps or reorder them.

**Step 1 — Build the audience-decision model**
Identify stakeholders, their decision, their priors, and what evidence would move them. Write into `### Audience and decision`.

**Step 2 — Construct the insight hierarchy (Pyramid Principle)**
Order findings by decision relevance, not research completeness. Apply the Pyramid Principle:
- Top: the governing conclusion (the single most important thing the stakeholders need to know)
- Second level: 3–5 supporting findings that prove or qualify the governing conclusion
- Third level: evidence, quotes, data points that support each finding
Do not lead with methodology. Do not lead with participant demographics. Lead with the conclusion.

**Step 3 — Frame the narrative arc**
Map findings onto the situation → complication → resolution → recommendation arc:
- Situation: what was true before the research (shared context, no new information)
- Complication: what the research revealed that changes or challenges the situation
- Resolution: what the findings mean for the decision at hand
- Recommendation: the specific action or direction the team should take
Write into `### Narrative arc` (internal framing — used to structure the deck, not always a visible section to stakeholders).

**Step 4 — Curate evidence**
Select the minimum evidence needed to make each finding credible. Avoid exhaustive note-dumping. Prioritize:
- Direct participant quotes that are specific and emotionally legible
- Behavioral data (what users did, not just what they said)
- Contradiction or surprise findings (findings that challenge priors carry more persuasive weight)
Write into `### Evidence highlights`.

**Step 5 — Frame the stakeholder ask**
Make the ask explicit. State what you need from the stakeholders after the readout: a decision, a prioritization call, a follow-up meeting, a resource commitment, or an acknowledgment. Vague asks produce vague outcomes. Write into `### Stakeholder asks`.

---

## Structured Findings

Each finding in the readout must follow this schema:

```
### Finding: <short headline — conclusion first>

Audience:
  <who this finding is most relevant to>

Finding:
  <the insight, stated as a conclusion — not "we observed that..." but "users cannot X because Y">

Evidence:
  <curated quotes, behavioral observations, or data points — minimum viable set>

Confidence:
  High | Medium | Low
  <brief rationale: sample size, consistency across sources, method reliability>

Recommendation:
  <directional guidance linked to this finding — framed as "we recommend" not "you must">

Stakeholder ask:
  <the specific action or decision needed from this audience in response to this finding>
```

---

## Prioritization Logic

Findings are ordered by **decision relevance**, not by research completeness or discovery sequence.

Rules:
1. Lead with the finding most directly tied to the decision the stakeholders need to make.
2. Group supporting evidence under each finding — do not present evidence as standalone findings.
3. Limit the readout to 3–5 primary findings. Additional findings go to the appendix or coverage map.
4. Contradictory findings are not buried — they are surfaced explicitly with a confidence label.
5. Gaps and unknowns are stated, not omitted. A gap the team doesn't know about is a risk.

---

## Pattern Detection

Before finalizing the readout, the agent must explicitly check for:

- **Finding clusters:** Multiple findings that point to the same underlying problem or opportunity — consolidate into one governing finding with supporting evidence
- **Contradictions:** Findings that conflict with each other or with stakeholder priors — surface these, state the tension, and provide a confidence-weighted interpretation
- **Gaps:** Areas the research did not cover that are relevant to the decision — list in `### Coverage map` under "deferred"
- **Unacknowledged risks:** Patterns the team has not surfaced publicly but that the research reveals — flag explicitly, do not soften

---

## Recommendations

Each recommendation must:
- Link directly to a named finding (no orphan recommendations)
- Be framed as directional guidance: "we recommend" or "the evidence points toward" — not mandates
- Include a confidence level (High / Medium / Low) with rationale
- Be scoped to what the research can support — do not overclaim

Recommendations are written into the finding schema above and summarized in `### Recommendations` as a consolidated list for stakeholder review.

---

## Coverage Map

Written into `### Coverage map`. Three explicit buckets:

**In the readout:**
List of findings included, with the rationale for prioritization.

**Deprioritized:**
Findings that were researched but excluded from the primary readout because they are not decision-relevant at this stage. Available in the full synthesis.

**Deferred:**
Research questions that were not answered in this study — either out of scope, insufficient data, or not yet conducted. Each deferred item is a stated gap, not a silent omission.

---

## Limits and Unknowns

This skill cannot guarantee:
- Stakeholder follow-through on recommendations after the readout
- That the decision made is the correct one — the readout informs, it does not decide
- That findings remain valid if the product context or user base changes materially after the research is conducted
- Scope creep prevention post-readout — additional questions raised in the session are out of scope unless a follow-up research plan is commissioned
- That the readout was interpreted as intended — live presentation and async consumption produce different comprehension outcomes

---

## Workflow Rules

1. Build the audience-decision model before structuring any section of the deck.
2. Apply the Pyramid Principle: conclusion first, evidence second, methodology last (or never).
3. Lead with insight, not process. Stakeholders do not need to know how you ran the sessions.
4. No raw data dumps. Every quote, clip, or data point must be curated to support a named finding.
5. Evidence must be the minimum viable set — enough to be credible, not everything you collected.
6. Make the stakeholder ask explicit and specific. "Any questions?" is not a stakeholder ask.
7. State all assumptions and gaps. Omitting them reduces credibility when they surface later.
8. Label all outputs by path: `sourced`, `fallback`, or `inferred`.

---

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/ux-researcher-research-readout-deck.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/runs/<run-id>/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.
