---
name: copy-review
description: Review product copy as a content system by modeling user commitments, terminology, states, and guidance across the strongest available evidence path instead of critiquing isolated strings.
trigger: When content quality, clarity, or trust needs an independent review before ship, rewrite, or localization planning.
content_framework: clarity, decision support, terminology consistency, trust signals, and state coverage
primary_mcp: repository, figma, chrome_devtools
fallback_tools:
  - notion
  - reference/ground
  - search_query
required_inputs:
  - target flow or surface
  - primary audience or user goal
  - brand, legal, or compliance constraints when known
  - locale, platform, and release context assumptions
recommended_passes:
  - clarity and comprehension
  - decision support and next-step guidance
  - terminology and consistency
  - tone and trust
  - states, errors, and recovery language
tool_stack:
  runtime:
    primary: [chrome_devtools]
    secondary: [repository]
  artifacts:
    primary: [repository, figma]
    secondary: [notion]
  fallback:
    primary: [reference/ground, search_query]
tool_routing:
  - if: live product access exists and wording depends on runtime states or dynamic copy
    use: [chrome_devtools, repository]
  - if: repository strings or content source files exist
    use: [repository]
  - if: copy source of truth lives in design or docs
    use: [figma, notion]
  - if: only screenshots, docs, or static exports exist
    use: [open, search_query]
best_guess_output: A copy review with evidence-tagged language issues, grouped patterns, and directional rewrite guidance.
output_artifacts: logs/active/<project-slug>/reviews/design-reviewer.md
section_anchor: "## Skill: copy-review"
done_when: The team knows which language problems are local, which are systemic, how strong the evidence is, and what should change first.
---

# Copy Review

## Purpose

Review product copy as a system across labels, guidance, states, and trust signals instead of isolated strings.

This skill evaluates whether the language helps the intended user understand what is happening, decide what to do next, and recover when things go wrong.

This skill does not invent brand strategy, replace legal review, or claim that copy effectiveness has been validated with real users unless such evidence is explicitly provided.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: copy-review`, include:
- `### Review framing`: Define the product context, user goal, audience assumptions, content surfaces reviewed, and why this is a copy review rather than messaging strategy work.
- `### Required inputs and assumptions`: State the target flow or surface, audience, brand or legal constraints, locale assumptions, and any missing inputs inferred by the reviewer.
- `### Input mode and evidence path`: Choose the strongest available evidence path in this order: live product behavior, repository content sources, design artifacts or docs, screenshots or static exports, then inference.
- `### Tool selection rationale`: State which tools were used, why they were chosen, what they validated well, and where they were weak.
- `### Environment and reproducibility`: Record product state, locale, browser or platform, auth state, experiment flags, and content version or branch when known.
- `### Content system model`: Build the language model first by documenting the key surfaces, user commitments, domain terms, CTA families, state messages, and trust-sensitive moments.
- `### Evaluator passes`: List the passes used such as clarity and comprehension, decision support, terminology and consistency, tone and trust, and states, errors, and recovery language.
- `### Language findings`: Record findings using the required finding schema below.
- `### Prioritized findings`: Include all critical and major language problems as standalone findings, group minor issues into patterns, and prefer no more than 15 standalone findings by default unless additional findings are materially distinct or high severity.
- `### Systemic language patterns`: Group repeated issues such as vague CTA language, naming drift, weak empty states, false reassurance, or inconsistent domain vocabulary.
- `### Coverage map`: State what was deeply reviewed, partially reviewed, and not reviewed.
- `### Severity, confidence, and coverage confidence`: Separate copy impact severity from evidence confidence and state whether coverage came from live runtime, repository sources, artifact review, or screenshot-only inference.
- `### Directional rewrite guidance`: Link rewrite directions to findings without pretending every final string is already approved.
- `### Limits and unknowns`: Explain where business context, legal review, localization, analytics, or user research would still be needed.

For each finding inside `### Language findings`, use this exact mini-template:

#### Finding <id>
- Observation:
- Evidence:
- Repro steps or location:
- Primary issue type:
- Likely cause:
- Impact:
- Severity:
- Confidence:
- Recommendation direction:

## Tool Path

- Prefer the highest-fidelity evidence path available: live product behavior -> repository content sources -> design artifacts or docs -> screenshots or static exports -> inference.
- Start with `repository, figma, chrome_devtools` when the product surface, source strings, and runtime states are all available.
- Use `chrome_devtools` when copy depends on live states, validation messages, loading behavior, async confirmations, or runtime sequencing.
- Use `repository` when the review depends on source strings, shared content helpers, localization keys, conditional messaging, or variant coverage.
- Use `figma` when the review is pre-implementation or when design artifacts are the main source of truth for labels and state copy.
- Use `notion` when style guides, naming rules, policy notes, or approved terminology live in internal docs.
- Use `open` or `search_query` only for supporting context or static evidence when direct runtime or artifact access is unavailable.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `notion, reference/ground, search_query`.
- If both paths fail, produce the best-guess output described as: A copy review with evidence-tagged language issues, grouped patterns, and directional rewrite guidance.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.
- Combine tools when useful rather than forcing a single-source review.

## Workflow Notes

- Treat this as a content-system review, not as brand strategy, legal approval, or localization QA.
- Treat `required_inputs` as real prerequisites. If audience, constraints, or locale are missing, infer a provisional set, prefix each inferred item with `Assumed context:`, and lower confidence for findings that depend on it.
- Build the content system model before analysis. Do not jump from isolated string reactions to issue lists.
- Review the full conversation between screens and states, not just individual microcopy lines in isolation.
- Run evaluator passes in sequence so findings stay grounded: clarity first, decision support second, terminology and consistency third, then tone, trust, and recovery language.
- Distinguish clearly between observed wording problems, inferred content causes, and recommendation direction.
- Separate copy defects from product-policy gaps. A missing rule or unresolved business decision is not the same as a bad sentence.
- Prefer directional rewrite guidance when the right answer depends on product positioning, legal rules, localization constraints, or experimentation strategy.
- Surface systemic terminology debt explicitly so downstream teams can fix the content model, not just patch strings one by one.
- After all passes, merge duplicates and consolidate overlapping findings before prioritization.
- Do not claim comprehension, trust uplift, or conversion impact has been validated unless real research or analytics evidence exists.

## Output Contract

- Write or update `logs/active/<project-slug>/reviews/design-reviewer.md`.
- Keep all work for this skill inside `## Skill: copy-review`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The team knows which language problems are local, which are systemic, how strong the evidence is, and what should change first.
