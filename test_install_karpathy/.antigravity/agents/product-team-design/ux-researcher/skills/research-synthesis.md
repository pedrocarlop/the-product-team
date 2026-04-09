---
name: research-synthesis
description: Applies thematic analysis, affinity diagramming, and the atomic research model to convert raw qualitative data into traceable findings, themes, and design-ready recommendations.
trigger: After interviews, workshops, usability sessions, diary studies, or any qualitative data collection. Run when raw notes, transcripts, or recordings exist and the team needs actionable insight.
mesh:
  inputs:
    - ux-researcher:research-plan
  next:
    - product-designer:journey-and-flow-design
    - product-lead:write-prd
  context: "Translates research findings into actionable insights for design and product specs."
required_inputs:
  - Raw notes, transcripts, recordings, or observation artifacts from at least one research session
  - Research questions or study goals (to anchor coding and theme formation)
  - Participant IDs or session identifiers (for traceability)
recommended_passes:
  - Pass 1 — Evidence model: inventory sources, assign participant IDs, confirm session coverage
  - Pass 2 — Observation coding: open codes on raw data
  - Pass 3 — Theme clustering: axial and selective coding, affinity grouping
  - Pass 4 — Implication drawing and confidence assessment
tool_stack:
  runtime:
    primary: dovetail
    secondary: notion, looppanel
  artifacts:
    primary: figjam, miro
  fallback:
    primary: research-plan skill, search_query
tool_routing:
  - if: dovetail is connected and transcripts are available
    use: dovetail for auto-transcription, AI tagging, highlight clustering, and pattern surfacing
  - if: team is working collaboratively in real time
    use: figjam or miro for live affinity diagramming; import clusters into notion afterward
  - if: dovetail is unavailable and transcripts exist
    use: looppanel for auto-coding against research questions, then notion for synthesis structure
  - if: traceability to source quotes is required
    use: aurelius to link every insight to its originating session and participant
  - if: budget or tooling limits dovetail
    use: condens as direct alternative (AI-assisted tagging, highlight reels, participant panels)
  - if: all synthesis tools are unavailable
    use: fallback — produce best-guess synthesis from available notes; label as inferred
best_guess_output: A structured synthesis with source inventory, coded observations, themes with evidence, and directional design implications — labeled as inferred where no primary tool access exists.
output_artifacts:
  - knowledge/ux-researcher-research-synthesis.md
  - knowledge/assets/ (for visual artifacts)
done_when: Every research question is addressed by at least one theme with traceable evidence, every finding has a source ID, and the team can make a product or design decision without reading raw notes.
---

# Research Synthesis

## Purpose

This skill applies structured qualitative analysis to raw research data — notes, transcripts, recordings, artifacts — and produces traceable findings, themes, and recommendations the team can act on.

Reasoning type: inductive — moving from specific observations to broader patterns to design implications.

Methods anchored to: Braun & Clarke 6-step thematic analysis, affinity diagramming, grounded theory coding (open → axial → selective), and the atomic research model (facts → insights → opportunities → recommendations).

This skill does NOT conduct sessions, design studies, or make product decisions. It transforms existing evidence into structured meaning.

---

## Required Inputs and Assumptions

**Required:**
- Raw source material: notes, transcripts, recordings, or observation artifacts
- Research questions or goals the study was designed to answer
- Participant or session identifiers (used for traceability)

**Known vs unknown at synthesis time:**
- Known: what data was collected, how many sessions ran
- Often unknown: full participant demographics, whether the study was fully powered, whether all recordings are complete

**Assumption rule:** If research questions are not explicitly documented, infer them from session guide headings or observable study structure. Label inferred questions as `assumed` and note them at the top of the source inventory.

---

## Input Mode and Evidence Path

Declare the path used before starting synthesis. Options:

1. **Live / real interaction** — synthesis happens during a live session (e.g., collaborative affinity workshop with the team). Highest fidelity; captures non-verbal cues if notes are strong.
2. **Structured system access** — transcripts and session data are available in Dovetail, Condens, Looppanel, or Aurelius. AI-assisted tagging accelerates open coding.
3. **Design artifacts / documentation** — synthesis from journey maps, sketches, affinity boards already created. Treat these as pre-coded artifacts; verify original source traceability.
4. **Screenshots / static input** — session screenshots, survey exports, or static notes. Limitations: no audio context, no participant tone, potential transcription gaps.
5. **Inference** — no direct access to source material; synthesis is from memory, summaries, or second-hand notes. Label all output as `inferred`. Flag for verification.

**Declare the path in the `### Source material` section of the deliverable.**

---

## Tool Stack

**Runtime primary — Dovetail**
Auto-transcribes interviews and usability sessions. AI surface-clusters tags across studies, identifies recurring language, and highlights quotes. Best for teams running continuous research. Use for open coding acceleration and cross-study pattern detection.

**Runtime secondary — Notion**
Synthesis templates, tagged observation databases, linked finding cards. Use for structured deliverable writing and insight documentation when Dovetail output needs narrative organization.

**Runtime secondary — Looppanel**
AI-powered interview analysis. Auto-codes transcripts against research questions, generates summary insights per session. Strong 2025 alternative for reducing synthesis time when Dovetail is not available.

**Artifacts — FigJam / Miro**
Collaborative affinity diagramming: digital sticky notes, cluster grouping, journey map annotation. FigJam preferred when team lives in Figma. Miro preferred for mixed remote/in-person synthesis workshops.

**Traceability — Aurelius**
Links every published insight to originating sessions and participant quotes. Use when stakeholders require evidence chains or when research will be referenced across multiple projects.

**Alternative to Dovetail — Condens**
AI-assisted tagging, auto-transcription, highlight reels, participant panel management. Mid-market pricing. Use as direct Dovetail substitute for teams without enterprise budget.

**Fallback — research-plan skill, search_query**
Use for question alignment if study goals are undocumented. Use search for method reference if synthesis approach is in dispute.

---

## Tool Routing

- Dovetail connected + transcripts available → use Dovetail for transcription, AI tagging, and clustering. Export highlights to Notion for structured synthesis.
- Collaborative real-time synthesis → use FigJam or Miro for affinity diagramming; consolidate clusters into Notion afterward.
- Dovetail unavailable → use Looppanel for auto-coding, then Notion for deliverable structure.
- Traceability to source quotes required → use Aurelius. Link every finding card to originating sessions.
- Dovetail cost-constrained → use Condens as drop-in alternative.
- All tools unavailable → produce best-guess synthesis from available notes. Label each finding as `sourced`, `fallback`, or `inferred` to match actual evidence path.

---

## Environment and Reproducibility

- **Platform:** browser-based tools (Dovetail, Notion, Looppanel, FigJam, Miro, Condens, Aurelius) — no local install required
- **Auth state:** Dovetail and Looppanel require project workspace access; FigJam requires team Figma seat; Aurelius requires workspace invite
- **Data state:** synthesis is reproducible only if source material is preserved in the repository. If transcripts or recordings are deleted, synthesis cannot be verified.
- **Version:** session identifiers and synthesis date must be logged to support future re-analysis. If source material version is unknown, state explicitly in the coverage map.

---

## Model Building

The agent must construct an evidence model before drawing any conclusions.

### Evidence model components

**1. Source material inventory**
List every artifact that will be analyzed:
```
| ID     | Type        | Participant | Session Date | Status         |
|--------|-------------|-------------|--------------|----------------|
| S01    | Transcript  | P01         | YYYY-MM-DD   | Complete       |
| S02    | Notes       | P02         | YYYY-MM-DD   | Partial        |
| S03    | Recording   | P03         | YYYY-MM-DD   | Not analyzed   |
```
Flag partial or missing sources before coding begins.

**2. Participant profiles**
Record attributes relevant to the study (role, tenure, segment, context) without personally identifiable information. These inform whether patterns are segment-specific or universal.

**3. Observation corpus**
Extract discrete observations from source material — one observation per sticky note or row. Each observation must reference its source ID. This is the raw input to open coding.

No themes, no conclusions, no implications until the observation corpus is built.

---

## Core Method Execution

Follows Braun & Clarke 6-step thematic analysis plus grounded theory coding and affinity diagramming.

**Step 1 — Familiarize with the data**
Read or re-read all source material. Do not code yet. Note initial reactions separately. Identify any sessions that are incomplete or ambiguous.

**Step 2 — Open coding (generate initial codes)**
Assign short descriptive codes to every meaningful observation in the corpus. One code per observation unit. Aim for specific codes, not categories. Example: `confusion-with-date-picker` not `navigation issues`. In Dovetail or Looppanel, auto-generated tags are starting points — review and adjust every tag manually for accuracy.

**Step 3 — Axial coding (search for themes)**
Group open codes into candidate themes by affinity. Use FigJam or Miro for physical clustering if working collaboratively. Each theme cluster must contain at least two observations from at least two participants to qualify as a pattern (single-source themes are labeled as outliers and noted separately).

**Step 4 — Selective coding (review and refine themes)**
Test each theme against the full observation corpus. Ask: does this theme accurately represent the observations in it? Are there observations that don't fit any theme? Merge, split, or rename themes as needed. Eliminate themes that are too broad or internally inconsistent.

**Step 5 — Define and name themes**
Write a one-sentence definition for each theme. The name must describe the user experience, not the research method. Example: `Trust erodes when pricing information is hidden` not `Pricing transparency findings`.

**Step 6 — Produce structured findings**
Translate each coded observation into the structured finding schema below. Aggregate findings under their parent theme.

**Atomic research model mapping:**
- Open codes → facts (discrete, verifiable observations)
- Theme clusters → insights (patterns that explain behavior)
- Theme implications → opportunities (where the product can improve)
- Recommendations → recommendations (specific, actionable directions)

---

## Structured Findings

Every finding must conform to this schema. No free-form narrative in the findings section.

```
Finding [ID]
Observation:   [What the participant said or did — factual, no interpretation]
Evidence:      [Direct quote or artifact reference — verbatim where possible]
Source:        [Session ID + Participant ID, e.g., S01/P02]
Theme:         [Parent theme name]
Implication:   [What this means for the product or experience]
Confidence:    [High / Medium / Low — see confidence criteria below]
```

**Confidence criteria:**
- High: observation present in 3+ sessions, consistent across participant segments
- Medium: observation in 2 sessions, or 1 session with strong corroborating artifact evidence
- Low: single observation, no corroboration, or source is partial/incomplete

**Separation rule:** Observation and Implication must be written by different reasoning steps. Never collapse observation into interpretation in the same sentence.

---

## Prioritization Logic

After all findings are coded and themed:

1. **Score each theme:** frequency (number of participants who surfaced it) × impact (severity of the user problem, rated 1–3). High-frequency + high-impact themes are primary findings.
2. **Group low-frequency observations:** observations from fewer than 2 participants that share a common code go into an `Edge cases and outliers` section rather than a primary theme.
3. **Flag high-impact outliers:** a single observation that, if true, would significantly change the product direction must be flagged explicitly even at Low confidence. Label: `[OUTLIER — high-impact, single source — verify before acting]`.
4. **Distinguish signal from noise:** observations caused by study conditions (facilitator error, unusual participant context, technical failure) are noted in the coverage map, not elevated as findings.

---

## Pattern Detection

The agent must explicitly identify and document:

- **Recurring observations:** the same behavior or statement appearing across 3+ participants — strongest signal; elevate to primary finding
- **Contradictions:** two participants experiencing the same feature in opposite ways — do not resolve prematurely; document as tension and note what conditions might explain the difference
- **Outliers worth noting:** rare but high-severity observations (e.g., a safety or trust issue surfaced once) — isolate, flag, recommend follow-up research
- **Mental model breakdowns:** moments where participant expectations mismatched system behavior — these often indicate the most actionable design opportunities

---

## Recommendations

Each recommendation must:
- Reference the theme it addresses (by name)
- Reference at least one supporting finding (by ID)
- Be directional for product or design — not a restatement of the observation
- Distinguish between: design change (can act now), further research needed (verify before acting), and strategic implication (requires cross-functional alignment)

Format:
```
Recommendation [ID]
Theme:          [Parent theme]
Supporting findings: [Finding IDs]
Direction:      [What the product or design should do]
Type:           [Design change / Further research needed / Strategic implication]
Priority:       [High / Medium / Low — derived from theme prioritization score]
```

Explicitly flag where more research is needed before a recommendation can be acted on.

---

## Coverage Map

Document in the deliverable:

| Source ID | Type       | Coverage Status | Notes                        |
|-----------|------------|-----------------|------------------------------|
| S01       | Transcript | Fully analyzed  |                              |
| S02       | Notes      | Partially analyzed | Missing last 20 minutes   |
| S03       | Recording  | Not analyzed    | Pending transcription        |

State the overall coverage confidence: what proportion of sessions contributed to the synthesis. If fewer than 70% of sessions are fully analyzed, flag the synthesis as preliminary.

---

## Limits and Unknowns

Document honestly:

- Where synthesis is thin: themes supported by only 1–2 sources
- What requires more sessions: open questions the current data cannot answer
- Where confidence is low: findings marked Low that are driving recommendations
- Participant representation gaps: segments not covered by current sessions
- Source quality issues: incomplete recordings, notes from memory, second-hand summaries

---

## Workflow Rules

1. Build the evidence model (source inventory + observation corpus) before writing a single code.
2. Complete open coding before grouping into themes.
3. Complete theme review and definition before drawing implications.
4. No premature conclusions: do not write recommendations before themes are finalized and reviewed against the full corpus.
5. Distinguish fact from inference throughout: observations are facts; implications are inferences. Label them separately at every stage.
6. Label every output section as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
7. If source material is missing mid-synthesis, halt, update the coverage map, and note the gap before continuing.

---


### Required sections within `## Skill: research-synthesis`

- `### Source material` — evidence model: source inventory, participant profiles, observation corpus status, evidence path declared
- `### Themes` — named themes with one-sentence definitions, frequency and impact scores
- `### Findings` — all findings in structured schema, grouped by theme
- `### Recommendations` — all recommendations in structured schema, linked to themes and findings
- `### Coverage map` — what was fully, partially, and not analyzed
- `### Confidence and gaps` — where synthesis is strong, where evidence is thin, what needs more sessions

## Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/ux-researcher-research-synthesis.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed and Store Visual Artifacts**: If tools like `stitch`, `v0`, or `generate_image` were used, you MUST copy the resulting images/screenshots to the project's run-specific assets directory: `knowledge/assets/`. Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/image-name.png)`. NEVER use absolute paths to your local brain directory.
