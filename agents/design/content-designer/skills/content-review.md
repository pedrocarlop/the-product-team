---
name: content-review
description: Applies heuristic evaluation, readability scoring, and voice/tone rubric analysis to audit an existing content surface — surfaces, components, and copy taxonomy — and produces traceable findings, severity-scored issues, and directional rewrite recommendations.
trigger: When product copy exists on a surface, flow, or component set and the team needs to know what to rewrite, in what order, and why. Run after shipping, before a content audit, ahead of a brand refresh, or when copy quality is flagged as a risk.
required_inputs:
  - The content surface to review: URL, Figma file, repository strings, screenshots, or a copied-in copy deck
  - The product's voice and tone guidelines (or enough context to infer them)
  - Audience definition: who uses this surface, their context, and their literacy level
  - Review scope: what is in and out of scope (full product, single flow, specific component type)
recommended_passes:
  - Pass 1 — Content model: inventory surfaces, components, and copy taxonomy before evaluating anything
  - Pass 2 — Heuristic evaluation: apply the content heuristics to every string in scope
  - Pass 3 — Readability and voice scoring: score for reading level and tone alignment
  - Pass 4 — Consistency audit: check terminology, label patterns, and structural drift
  - Pass 5 — Finding consolidation, prioritization, and recommendations
tool_stack:
  runtime:
    primary: repository, notion
    secondary: figma, writer
  artifacts:
    primary: notion, google_docs
  fallback:
    primary: search_query, reference/ground
tool_routing:
  - if: repository is connected and source strings are accessible
    use: repository to extract the full copy inventory directly from code; cross-reference with figma for rendered context
  - if: figma is connected and designs contain the live copy
    use: figma to walk every frame and component; extract strings into a content inventory before evaluating
  - if: writer.com is configured for the team
    use: writer for real-time voice/tone scoring against the team's brand guidelines; use its style guide checker to flag deviations
  - if: a url to a live product surface is provided
    use: search_query + web fetch to capture the rendered copy; build the content inventory from the live page
  - if: screenshots or a copy deck is the only input
    use: extract strings manually from the provided artifact; mark coverage as partial and declare evidence path as screenshots/artifacts
  - if: no tooling is available
    use: fallback — produce best-guess review from provided context; label all output as inferred
best_guess_output: A content review with a surface inventory, heuristic findings in structured schema, readability scores, voice/tone ratings, severity-prioritized issues, and directional rewrite recommendations — labeled as inferred where no direct source access exists.
output_artifacts:
  - knowledge/runs/<run-id>/content-designer-content-review.md
  - knowledge/runs/<run-id>/assets/ (for visual artifacts)
done_when: Every string in scope has been evaluated against the content heuristics, every finding has a location reference and severity score, and the team can prioritize rewrites without reading the raw copy themselves.
---

# Content Review

## Purpose

This skill audits an existing content surface by constructing a content model first, then applying structured heuristic evaluation, readability scoring, voice/tone rubric analysis, and consistency auditing to produce traceable findings and prioritized recommendations.

Reasoning type: evaluative — comparing observed copy against defined quality criteria, then translating defects into directional recommendations.

Methods anchored to: content heuristics (clarity, consistency, voice, tone, actionability, context-appropriateness), Flesch-Kincaid and Gunning Fog readability scoring, content inventory and audit methodology (Halvorson & Rach), voice and tone rubric scoring (MailChimp Voice and Tone model, Nielsen Norman Group UX writing guidelines), and comparative content analysis.

This skill does NOT write new copy, design flows, or make product decisions. It diagnoses content quality and tells the team what to rewrite and why.

---

## Required Inputs and Assumptions

**Required:**
- Content surface: a URL, Figma file link, repository path, screenshots, or pasted copy deck
- Voice and tone guidelines: brand doc, style guide, or enough product context to reconstruct them
- Audience definition: who uses this surface, their reading context, and their expected literacy level
- Review scope declaration: which surfaces, flows, or component types are in scope

**Known vs unknown at review time:**
- Known: what copy exists, where it lives, and the review scope
- Often unknown: whether the voice guidelines are current, whether the copy was written intentionally or accumulated through multiple authors, whether any strings are dynamically generated or localized
- Often unknown: what reading level the audience actually has (must be estimated from audience definition)

**Assumption rule:** If voice and tone guidelines are not provided, infer them from the most consistent copy on the surface (modal headers, primary CTAs, empty states). Document inferred guidelines at the top of the content model and label them as `assumed`. Flag for verification before recommendations are acted on.

---

## Input Mode and Evidence Path

Declare the path used before beginning the content model. Options:

1. **Live product** — review happens directly on a rendered product surface (browser, device). Highest fidelity; captures actual rendered strings, truncation, dynamic states.
2. **Repository access** — strings extracted from source code or localization files. Complete coverage; may miss rendered-state context (truncation, wrapping, empty states).
3. **Figma / design files** — copy reviewed from design frames and components. Good structural coverage; may not reflect shipped copy if designs diverge from code.
4. **Screenshots or copy deck** — static images or a pasted document. Partial coverage; cannot verify complete string sets or dynamic states.
5. **Inference** — no direct surface access; review is from memory, stakeholder description, or second-hand documentation. Label all output as `inferred`. Flag for verification before acting.

**Declare the path in the `### Content model` section of the deliverable.**

---

## Tool Stack

**Runtime primary — Repository**
Direct access to source strings, localization files (i18n keys), and component copy. Enables complete inventory with location references. Use for any audit where accuracy and traceability to code are required. Preferred over design files when the two diverge.

**Runtime primary — Notion**
Content audit templates, finding databases, rewrite tracking. Use for structured deliverable writing, issue logging, and rewrite status tracking across multiple review cycles.

**Runtime secondary — Figma**
Renders copy in design context — shows truncation, layout pressure, component hierarchy. Use to audit copy against its visual and structural environment. Invaluable for evaluating label length, button copy, and empty state composition.

**Runtime secondary — Writer.com**
AI-powered brand writing assistant with style guide enforcement, terminology management, and real-time tone scoring. Flags passive voice, banned terms, brand deviations, and reading-level issues. Use when the team has a configured Writer workspace with brand guidelines loaded. Paid tool (team plan ~$18/user/month as of 2025).

**Readability scoring — Hemingway Editor**
Highlights sentence complexity, adverbs, passive voice, and assigns a grade-level score. Web-based, free. Use for quick readability diagnostics on body copy, onboarding text, and instructional content. Not suitable for very short UI strings.

**Readability scoring — Readable.com**
Aggregates multiple readability formulas (Flesch-Kincaid, Gunning Fog, SMOG, Coleman-Liau). Batch analysis for URLs and documents. Use when auditing marketing pages, help content, or long-form product copy at scale. Free tier available; paid plans from ~$4/month.

**Voice/tone consistency — Acrolinx**
Enterprise-grade content governance platform. Scores copy against custom style guides, flags terminology drift, and tracks quality over time across large content systems. Use for enterprise products with significant content volume and multiple authors. High-cost enterprise tool.

**UX writing reference — UX Writing Hub**
Repository of UX writing patterns, guidelines, and annotated examples. Use as a reference standard when evaluating copy against established UX writing conventions (button labels, error messages, empty states, confirmation dialogs).

**Content testing — Maze**
Unmoderated usability testing platform with content-specific tests (preference tests, five-second tests). Use when a finding requires validation — e.g., testing whether a rewritten CTA performs better than the original. Paid tool (~$99/month for teams as of 2025).

**Fallback — search_query, reference/ground**
Use search for accessing public UX writing guidelines, readability benchmarks, or competitor copy examples when no tooling is available. Use reference/ground for aligning on methodology or heuristic definitions.

---

## Tool Routing

- Repository connected + strings accessible → extract full copy inventory from source; cross-reference Figma for rendered context; use Writer for voice scoring if configured.
- Figma connected, no repo access → extract strings frame-by-frame; flag coverage gaps where dynamic states are not visible in static frames.
- Writer.com configured with brand guidelines → use Writer as primary voice/tone scoring tool; supplement with heuristic evaluation for structural and clarity issues.
- Live URL available → use web fetch to capture rendered copy; supplement with Hemingway or Readable for readability scoring.
- Screenshots or copy deck only → build partial inventory from provided artifacts; mark coverage as limited; label output as `artifacts`.
- No tooling available → produce best-guess review from context provided. Label each finding as `sourced`, `fallback`, or `inferred` to match actual evidence path.

---

## Environment and Reproducibility

- **Platform:** review is conducted against the surface as it exists at review time. If copy is dynamic or personalized, state which variant or state was reviewed.
- **Auth state:** repository access requires read permissions on the relevant codebase or i18n files; Figma requires view access to the file; Writer requires team workspace access.
- **Data state:** content reviews are point-in-time snapshots. Copy changes after the review date are not reflected. Record review date and surface version (build number, commit hash, or design file version) to support future comparison.
- **Version:** if the surface has been localized, specify which locale was reviewed. If only one locale was reviewed, state this as a coverage gap.

---

## Model Building

The agent must construct a content model before evaluating any copy. No heuristic evaluation, readability scoring, or findings until the content model is complete.

### Content model components

**1. Surface inventory**
List every distinct surface, screen, or component group in scope:
```
| ID   | Surface / Component     | Type              | Location Reference           | Status       |
|------|-------------------------|-------------------|------------------------------|--------------|
| S01  | Onboarding flow         | Multi-step form   | /src/onboarding/ or Frame 4  | In scope     |
| S02  | Empty states            | Component set     | EmptyState.tsx or Frame 12   | In scope     |
| S03  | Settings page           | Form + labels     | /settings                    | Out of scope |
```

**2. Copy taxonomy**
Classify the copy types present on the surface:
- **Navigation labels** — menu items, tabs, breadcrumbs
- **Headings and subheadings** — page titles, section headers, modal titles
- **Body copy** — instructional text, descriptions, help text
- **CTAs and button labels** — primary, secondary, destructive actions
- **Form labels and placeholders** — field labels, placeholder text, hint text
- **Error, warning, and success messages** — validation, system feedback
- **Empty states** — zero-data and first-use states
- **Microcopy** — tooltips, badges, timestamps, status labels
- **Legal and compliance copy** — terms, consent, disclaimers

**3. Terminology register**
Extract the key nouns, verbs, and product-specific terms used across the surface. Note where the same concept is named differently in different places — this is a consistency defect to capture before heuristic evaluation begins.

No findings, no evaluations, no implications until the surface inventory and copy taxonomy are built.

---

## Core Method Execution

Follows a five-heuristic content evaluation adapted from Nielsen Norman Group UX writing guidelines, Halvorson & Rach content strategy methodology, and the MailChimp voice and tone model.

**Step 1 — Heuristic evaluation**
Evaluate every string in scope against the five content heuristics. Apply one heuristic pass at a time across the full surface rather than evaluating one string against all heuristics before moving to the next.

Heuristic 1: **Clarity** — Does the copy tell the user exactly what is happening, what they need to do, or what outcome to expect? Flag: jargon, ambiguous pronouns, passive constructions that obscure the actor, and multi-clause sentences where one will do.

Heuristic 2: **Consistency** — Is the same concept named the same way everywhere on this surface and across the product? Flag: synonym drift (two labels for the same thing), structural inconsistency (some headers are questions, others are noun phrases), and formatting inconsistency (sentence case vs. title case mixed without rule).

Heuristic 3: **Voice** — Does the copy sound like it was written by the same author with a coherent brand personality? Flag: register shifts (formal in one section, casual in another), copy that sounds like internal jargon or engineering language, and strings that feel templated or machine-generated without human review.

Heuristic 4: **Tone** — Is the emotional register of the copy appropriate to the user's context and task? Flag: copy that is too playful for a high-stakes action (e.g., destructive operations, error recovery), copy that is too formal for a casual onboarding moment, and error messages that blame the user.

Heuristic 5: **Actionability** — Does copy that asks the user to do something give them enough information to act confidently? Flag: vague CTAs ("Click here", "Submit"), button labels that do not match the action's outcome, missing context on irreversible actions, and help text that restates the label without adding information.

**Step 2 — Readability assessment**
For body copy, instructional text, onboarding content, and error messages (not for short labels or CTAs): score using Flesch-Kincaid Reading Ease and Gunning Fog Index.

Target benchmarks:
- Consumer product (general audience): Flesch-Kincaid grade 6–8, Flesch Reading Ease 60–70
- B2B / professional tool: grade 8–10 acceptable; above grade 12 requires justification
- Medical, legal, or financial content: follow domain-specific plain language standards

Flag any body copy scoring above the target grade level. Note that readability tools should not be applied blindly to short UI strings — apply judgment.

**Step 3 — Voice and tone rubric scoring**
Score the surface's overall voice and tone against the brand guidelines (or inferred guidelines) using a four-point rubric:

```
Dimension         | 1 — Off-brand         | 2 — Inconsistent      | 3 — Mostly on-brand   | 4 — On-brand
Warmth            | Cold / clinical        | Varies by section     | Mostly warm           | Consistently warm
Clarity           | Frequently unclear     | Uneven                | Mostly clear          | Consistently clear
Confidence        | Hesitant / apologetic  | Varies                | Mostly confident      | Consistently confident
Human-ness        | Robotic / templated    | Varies                | Mostly human          | Consistently human
```

Record the score per dimension and use it to anchor voice/tone findings.

**Step 4 — Consistency audit**
Cross-reference the terminology register built in the content model with every instance of each term in scope. Produce a terminology table:

```
| Concept         | Instances found          | Verdict          |
|-----------------|--------------------------|------------------|
| Save action     | "Save", "Save draft", "Keep changes" | Inconsistent — 3 labels for 1 action |
| Error recovery  | "Try again", "Retry", "Go back" | Inconsistent     |
| Account         | "Account", "Profile"     | Inconsistent     |
```

Flag every case where the same concept has more than one label.

**Step 5 — Produce structured findings**
Translate each defect identified in steps 1–4 into the structured finding schema below.

---

## Structured Findings

Every finding must conform to this schema. No free-form narrative in the findings section.

```
Finding [ID]
Observation:   [What the copy says — factual, no interpretation; quote verbatim where possible]
Evidence:      [Location reference: component name, screen ID, file path, or frame number]
Heuristic:     [Which of the five heuristics is violated: Clarity / Consistency / Voice / Tone / Actionability]
Cause:         [Why this is a defect: jargon, passive voice, synonym drift, register mismatch, etc.]
Impact:        [Effect on the user: confusion, hesitation, mistrust, task failure, etc.]
Severity:      [Critical / High / Medium / Low — see severity criteria below]
Confidence:    [High / Medium / Low — see confidence criteria below]
```

**Severity criteria:**
- Critical: copy defect that directly causes task failure, misrepresents a system action, or violates legal/compliance requirements
- High: copy that causes user confusion, friction, or hesitation in a primary flow; synonym drift on a core product concept
- Medium: voice or tone inconsistency that degrades trust or brand coherence; readability significantly above target grade level
- Low: stylistic preference, minor formatting inconsistency, or optional improvement with no material user impact

**Confidence criteria:**
- High: defect is observable in the rendered surface and violates an explicit guideline or established convention
- Medium: defect is observable but the guideline may be implicit or the impact is inferred rather than tested
- Low: defect is inferred from partial evidence (screenshots, copy deck) or requires user testing to confirm impact

**Separation rule:** Observation and Impact must be written by different reasoning steps. Never collapse what the copy says with what it does to the user in the same sentence.

---

## Prioritization Logic

After all findings are recorded:

1. **Score each finding:** severity (Critical = 4, High = 3, Medium = 2, Low = 1) × frequency (number of instances of this defect type on the surface, capped at 3). Maximum score = 12.
2. **Group by defect type:** findings sharing the same cause (e.g., "synonym drift on core objects", "passive voice in error messages") are grouped as a pattern rather than listed as individual issues. Pattern findings carry higher weight.
3. **Flag critical outliers:** any Critical finding — regardless of frequency — is elevated to the top of the report with a flag. Single-instance critical defects (e.g., a misleading confirmation message on a destructive action) must be addressed before any other finding.
4. **Separate functional from stylistic:** functional defects (Clarity, Actionability, Consistency on core objects) are always prioritized over stylistic preferences (Voice, Tone on peripheral copy). Do not let tone polish displace functional rewrites in the priority stack.

---

## Pattern Detection

The agent must explicitly identify and document:

- **Systematic synonym drift:** the same concept named differently in 3+ locations — strongest consistency signal; report as a pattern with a complete list of instances, not as individual findings
- **Voice register breaks:** sections of the surface that sound authored by a different voice (often indicating legacy copy, engineering-authored strings, or legal edits that were not style-reviewed); isolate and name the break point
- **Structural inconsistency patterns:** headings that mix grammatical forms (questions + noun phrases + imperatives) without a rule; this is a content model defect, not a copy defect, and requires a structural fix alongside rewrites
- **Tone mismatches at high-stakes moments:** error messages, destructive action confirmations, and empty states that use the wrong emotional register for the context — often the most impactful finding category
- **Readability drift by section:** surfaces where onboarding copy is accessible but settings or help text spikes to grade 12+ — often caused by different authors or copy imported from documentation

---

## Recommendations

Each recommendation must:
- Reference the finding or pattern it addresses (by ID)
- Be directional — point toward what the rewrite should achieve, not a full rewrite prescription (that is the job of the microcopy-flow-design or error-empty-success-states skills)
- Distinguish between: rewrite now (clear defect, guideline violation), validate before rewriting (finding is Medium or Low confidence, needs user testing), and structural fix required (the copy cannot be fixed without changing the component structure or content model)

Format:
```
Recommendation [ID]
Finding(s):     [Finding IDs addressed]
Direction:      [What the rewrite should achieve — not the rewrite itself]
Type:           [Rewrite now / Validate before rewriting / Structural fix required]
Severity:       [Inherited from highest-severity finding addressed]
Priority:       [High / Medium / Low — derived from prioritization score]
```

Do not write draft copy in the findings or recommendations section. If the team requests draft copy after reviewing this report, that work belongs in the microcopy-flow-design or error-empty-success-states skills.

---

## Coverage Map

Document in the deliverable:

| Surface ID | Surface / Component     | Coverage Status     | Evidence Path    | Notes                             |
|------------|-------------------------|---------------------|------------------|-----------------------------------|
| S01        | Onboarding flow         | Fully reviewed      | Repository       |                                   |
| S02        | Empty states            | Partially reviewed  | Figma frames     | Dynamic states not visible        |
| S03        | Localized strings (fr)  | Not reviewed        | Out of scope     | Locale review requires separate pass |

State overall coverage confidence: what proportion of the declared scope was fully reviewed. If fewer than 70% of in-scope surfaces were fully reviewed, flag the review as preliminary.

---

## Limits and Unknowns

Document honestly:

- Where the review is thin: surfaces reviewed only from screenshots or a copy deck without rendered context
- What requires user testing to confirm: Medium and Low confidence findings where impact is inferred rather than observed
- Dynamic and personalized copy: strings that vary by user state, role, or data could not be fully audited — list which states were not reviewed
- Localization gaps: if only one locale was reviewed, all findings are locale-specific and may not apply to translated versions
- Voice guideline uncertainty: if guidelines were inferred rather than sourced, all voice and tone findings carry higher uncertainty — flag for stakeholder confirmation before acting

---

## Workflow Rules

1. Build the content model (surface inventory + copy taxonomy + terminology register) before applying any heuristic.
2. Complete all five heuristic passes before scoring severity or writing findings.
3. Complete the readability assessment and voice/tone rubric scoring before consolidating findings.
4. Run the consistency audit last — it depends on the full terminology register being built first.
5. No recommendations before findings are finalized. Do not jump to "fix this" before the defect is clearly characterized.
6. Separate functional findings from stylistic preferences throughout. Never let tone polish displace functional rewrite priorities.
7. Label every output section as `sourced`, `fallback`, or `inferred` to match the evidence path actually used.
8. If a surface cannot be fully accessed mid-review, update the coverage map and note the gap before continuing. Do not fill coverage gaps with assumptions.
9. Do not write draft copy in this skill. Findings and recommendations are diagnostic outputs. Actual rewrites belong in microcopy-flow-design, error-empty-success-states, or another content production skill.

---


### Required sections within `## Skill: content-review`

- `### Content model` — surface inventory, copy taxonomy, terminology register, evidence path declared
- `### Heuristic findings` — all findings in structured schema, grouped by heuristic
- `### Readability scores` — per-surface readability scores with benchmark comparison
- `### Voice and tone rating` — rubric scores with dimension-level notes
- `### Consistency audit` — terminology table with verdict per concept
- `### Prioritized issues` — findings ranked by severity × frequency score; critical outliers elevated
- `### Recommendations` — all recommendations in structured schema, linked to findings
- `### Coverage map` — what was fully, partially, and not reviewed
- `### Confidence and gaps` — where review is strong, where evidence is thin, what requires user testing to confirm
