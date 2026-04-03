---
name: competitor-research
description: Build a structured competitive landscape model by systematically collecting, comparing, and interpreting UI patterns, user flows, and market signals from adjacent products to inform specific UX decisions.
trigger: When the team needs external pattern or competitor evidence to inform a design decision, benchmark a feature, or identify gaps in the current experience.
required_inputs:
  - the decision or design question the research should inform
  - the product surface or interaction type being benchmarked
  - the target user segment or context when known
  - the competitive set or market frame when known
recommended_passes:
  - competitive landscape model construction
  - pattern inventory across comparison set
  - quantitative context gathering (traffic, engagement)
  - gap analysis against current product
  - implication derivation
tool_stack:
  runtime:
    primary: [refero]
    secondary: [mobbin, page_flows, ux_archive]
  artifacts:
    primary: [figma]
  quantitative:
    primary: [similarweb]
  fallback:
    primary: [search_query, open]
tool_routing:
  - if: benchmarking shipped SaaS product interfaces or flows
    use: [refero]
  - if: broad mobile or web UI pattern reference is needed
    use: [mobbin]
  - if: interaction timing, transitions, or flow sequences must be observed
    use: [page_flows]
  - if: category-specific interaction patterns (e.g., onboarding, empty states) are the focus
    use: [ux_archive]
  - if: quantitative signals such as traffic, engagement, or audience overlap are needed
    use: [similarweb]
  - if: organizing screenshots into a comparison grid
    use: [figma]
  - if: primary tools are unavailable, blocked, or out of credits
    use: [search_query, open]
best_guess_output: A competitive landscape report with a comparison set, pattern inventory, evidence citations, gap analysis, and design implications.
output_artifacts: logs/active/<project-slug>/deliverables/ux-researcher-competitor-research.md
done_when: The competitive landscape model is constructed, relevant patterns are documented with sourced evidence or explicitly labeled as inferred, and implications are linked to the originating design decision.
---

# Competitor Research

## Purpose

Build a competitive landscape model by collecting, comparing, and interpreting UI patterns, user flows, and market signals from adjacent products.

This skill applies structured benchmarking — landscape model construction, pattern inventory, gap analysis — to produce actionable evidence that informs a specific product or design decision.

This skill does not produce gallery dumps disconnected from a decision, restate obvious market observations without evidence, or make design recommendations without first building the landscape model.

## Required Inputs and Assumptions

Required inputs:
- The decision or design question the research should answer
- The product surface or interaction type being benchmarked
- The target user segment or use context when available
- The competitive set or market frame when available

If inputs are missing, infer provisional values and prefix each with `Assumed context:`. Lower the confidence of any finding that depends on an inferred input.

Known vs unknown: the competitive set is often known by name but not by which surfaces are most relevant. The decision frame may be stated vaguely. Both must be resolved before the landscape model is built.

## Input Mode and Evidence Path

Evidence gathering follows this hierarchy:

1. **Live/real interaction** — Direct use of the competitor product in a real session. Highest fidelity; requires access and time.
2. **Structured system access** — Refero, Mobbin, Page Flows, UX Archive. Curated, searchable, annotated. Best balance of coverage and speed.
3. **Design artifacts/documentation** — Figma community files, case studies, design system docs. Useful as supplement; may be outdated.
4. **Screenshots/static input** — Manual screenshots or images shared by stakeholders. Limited to visible states; no flow context.
5. **Inference** — Pattern inference when direct evidence is unavailable. Must be labeled explicitly.

Declare which path was used and state its limitations in the deliverable. Prefer path 2 as the default when primary tools are available. Combine paths when they address different evidence gaps.

## Tool Stack

**Runtime — primary:** Refero (AI-powered design reference library; 6,000+ real SaaS flows; best for benchmarking shipped product interfaces and using AI-powered visual search to find similar screens).

**Runtime — secondary:** Mobbin (300,000+ screenshots and flows from mobile and web; best for broad pattern coverage across categories); Page Flows (video recordings of real user journeys with annotations; best for flow transitions, empty states, and onboarding sequences in motion); UX Archive (curated mobile UX patterns by flow type; best for category-leader reference on specific interaction patterns).

**Quantitative context:** SimilarWeb (web traffic, engagement metrics, audience overlap; use to add quantitative grounding to qualitative pattern findings or to prioritize which competitors matter most).

**Artifacts:** Figma or FigJam (organize screenshots into comparison grids; annotate patterns; prepare deliverable exhibits).

**Fallback:** web search + open (manual browsing when primary tools are unavailable or a product is not indexed).

## Tool Routing

- Benchmarking shipped SaaS product interfaces or flows → start with Refero.
- Broad UI pattern reference across many products or platforms → use Mobbin.
- Flow transitions, empty states, onboarding sequences, or interaction timing → use Page Flows.
- Category-specific interaction patterns against category leaders → use UX Archive.
- Traffic, engagement, or audience overlap data needed to contextualize findings → use SimilarWeb.
- Organizing and comparing screenshots → use Figma.
- Primary tools unavailable → use search_query + open; label output as `fallback`.
- Avoid relying on a single tool. Combining Refero (pattern sourcing) with SimilarWeb (quantitative context) and Page Flows (flow sequences) produces stronger evidence than any one tool alone.

## Environment and Reproducibility

Record the following in the deliverable when known:
- Date of research session (competitor UIs change frequently; evidence ages quickly)
- Platform and device used for live sessions (desktop web, mobile web, native iOS/Android)
- Authentication state (signed in vs. signed out surfaces often differ significantly)
- Product version or release when observable
- Tool versions: Refero 4.0+ for AI visual search capability; Mobbin session date
- Any regional or pricing-tier gating that may affect the surfaces observed

If any of the above is unknown, state it explicitly. Do not present gated or version-specific UI as universally representative.

## Model Building

Before evaluating competitors, the agent MUST construct a competitive landscape model:

1. **Define the competitive set**: Which products compete on the same surface, flow, or user job? Distinguish direct competitors (same segment, same job) from adjacent references (different segment but relevant pattern).
2. **Define the comparison dimensions**: What interaction types, flows, or UI patterns are being benchmarked? Examples: onboarding flow, empty state handling, navigation model, pricing page pattern, error recovery.
3. **Map the evidence available per competitor**: For each product in the set, note which surfaces can be sourced (via tools), which require fallback, and which must be inferred.
4. **Identify known gaps before analysis begins**: Where is the evidence set thin? Which competitors are missing? Which surfaces cannot be accessed?

No pattern inventory or findings may be written before the landscape model is complete.

## Core Method Execution

Follow this sequence:

**Step 1 — Clarify the decision frame.** Identify the specific design question this research must answer. If the frame is vague, write a provisional question, label it `Assumed context:`, and proceed.

**Step 2 — Build the landscape model.** Construct the competitive set (direct + adjacent), define comparison dimensions, and map evidence availability per competitor. Document this in `### Landscape model` before proceeding.

**Step 3 — Source pattern evidence.** For each competitor in the comparison set, use the tool routing logic to collect UI patterns, flows, and screens relevant to the comparison dimensions. Start with Refero; supplement with Mobbin, Page Flows, and UX Archive for breadth and motion context. Label each piece of evidence as `sourced`, `fallback`, or `inferred`.

**Step 4 — Add quantitative context.** Use SimilarWeb to check traffic volume, engagement benchmarks, and audience overlap for the top competitors. This grounds pattern findings in market relevance — a pattern from a low-traffic product carries different weight than one from a category leader.

**Step 5 — Inventory patterns.** For each comparison dimension, describe how each competitor handles it. Group similar approaches. Note outliers.

**Step 6 — Run gap analysis.** Compare the pattern inventory against the current product. Identify: (a) patterns the current product is missing, (b) patterns the current product does differently without evidence of user preference, (c) table-stakes patterns that are consistent across the field.

**Step 7 — Derive implications.** For each significant gap or pattern, state what it means for the current design decision. Implications must be directional and linked to evidence — not free-floating opinions.

**Step 8 — Structure and prioritize findings.** Apply the finding schema below. Prioritize by decision impact. Group minor patterns.

## Structured Findings

Every finding must use this exact schema. No free-form output. Separate observation from interpretation. Every finding must be traceable to a source.

```
#### Finding <id>
Observation: [What was seen, without interpretation]
Evidence: [Tool or source + screenshot reference or citation]
Source: [Competitor name, surface, date]
Cause: [Why this pattern likely exists — labeled as inferred if not confirmed]
Impact: [What this means for the current product or design decision]
Confidence: [High / Medium / Low + rationale]
```

Confidence guide:
- **High** — sourced directly from the product, multiple tools corroborate, or a consistent pattern across 3+ competitors.
- **Medium** — sourced from one tool, one competitor, or one surface; not yet cross-validated.
- **Low** — inferred from indirect evidence, outdated screenshots, or a single fallback source.

## Prioritization Logic

Prioritize findings by decision impact:

1. **Critical** — Patterns that directly affect the design decision at hand; table-stakes gaps that, if unaddressed, signal a major UX deficit.
2. **Significant** — Patterns that reveal meaningful differentiation opportunities or risks worth designing for.
3. **Minor** — Patterns that are interesting but not immediately actionable. Group these into a single `### Minor patterns` block rather than listing as standalone findings.

Do not include more than eight standalone findings. Surface-level observations that do not connect to the decision frame belong in the coverage map or gaps section, not in findings.

## Pattern Detection

After the pattern inventory is complete, the agent must identify:

- **Recurring patterns**: Interaction conventions or UI approaches used by 3+ competitors — these signal a settled category norm.
- **System-level problems**: Where multiple competitors struggle with the same flow or state (e.g., all handle empty state poorly), indicating an opportunity rather than a benchmark to follow.
- **Broken mental models**: Where competitors have converged on a pattern that user research suggests conflicts with user expectations — flag these explicitly.
- **Differentiators**: Where one competitor departs from the norm in a way that is meaningfully better or worse.

Distinguish category convergence (what the market has settled on) from category best practice (what actually works well for users). They are not always the same.

## Recommendations

Recommendations must:
- Link to a specific finding by ID
- Be directional, not prescriptive — state what to consider, not what to build
- Acknowledge evidence limits where confidence is Medium or Low
- Avoid recommending copying a competitor pattern without stating why it is appropriate for this product and user context

Format: `Rec <id> [links to Finding <id>]: <directional recommendation>.`

## Coverage Map

State explicitly:

- **Deeply analyzed**: Competitors, surfaces, and flows that were sourced from primary tools with high evidence coverage.
- **Partially analyzed**: Competitors or surfaces where evidence was incomplete, gated, or fallback-sourced.
- **Not analyzed**: Competitors excluded from this pass, surfaces not accessed, flows that could not be observed.

The coverage map sets expectations for what downstream design work can rely on vs. what needs further validation.

## Limits and Unknowns

Mandatory section. State:

- What competitor surfaces could not be accessed (gated by auth, pricing tier, geography)
- Where screenshots are outdated or may not reflect current product state
- What quantitative signals are missing or proxied
- Where inferred causes have not been validated by user research
- Where pattern prevalence is based on a small sample (fewer than 3 competitors)
- What real-world validation would increase confidence in the highest-impact findings

Do not omit this section or collapse it to a single line. Low-confidence areas must be named.

## Workflow Rules

- Build the landscape model before writing any pattern inventory or findings.
- Distinguish fact (directly sourced) from inference (reasoned from indirect evidence). Label every inference.
- Merge duplicate observations before writing findings. One finding per distinct pattern — not one per screenshot.
- Avoid redundancy between the pattern inventory and findings. The inventory is raw material; findings are interpreted conclusions.
- Do not hallucinate competitor UI details. If a surface cannot be sourced, mark it as `Not accessed` and lower confidence accordingly.
- Record the tool path used for each competitor or surface so the evidence is reproducible.

## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `logs/active/<slug>/deliverables/ux-researcher-competitor-research.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`.
- **Embed generated images**: If tools like `stitch`, `v0`, or `generate_image` were used to produce UI designs or concepts, embed the resulting images/screenshots directly into the markdown deliverable using standard markdown image syntax.

## Required Deliverable Sections

Within `## Skill: competitor-research`, include:
- `### Visual artifacts`: (Mandatory if visual tools were used) Embed all generated screens, concepts, or images.

- `### Landscape model`: Competitive set (direct + adjacent), comparison dimensions, evidence availability per competitor.
- `### Pattern inventory`: How each competitor handles each comparison dimension. Grouped by dimension, not by competitor.
- `### Quantitative context`: SimilarWeb signals or equivalent for the top competitors. If unavailable, state so.
- `### Gap analysis`: What the current product is missing, doing differently, or aligning with table stakes.
- `### Findings`: Structured findings using the required schema.
- `### Recommendations`: Directional recommendations linked to findings.
- `### Coverage map`: What was deeply, partially, and not analyzed.
- `### Gaps in evidence`: What could not be sourced, verified, or confirmed.

