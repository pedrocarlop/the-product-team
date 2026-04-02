# Design Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `accessibility-review`

- Description: Run a barrier-focused accessibility review by building an accessibility model, traversing task paths, and grounding barrier findings in the strongest available evidence path.
- Trigger: When accessibility risk needs a structured expert review before release, sign-off, or remediation planning.
- Primary MCP/tool: chrome_devtools
- Fallback: figma, reference/ground, search_query
- Best guess: An accessibility review with evidence-tagged barriers, grouped patterns, and directional remediation guidance.
- Output: logs/active/<project-slug>/reviews/design-reviewer.md
- Done when: The reviewed surface has evidence-backed accessibility barriers, grouped patterns, coverage limits, and prioritized fix directions that distinguish observed issues from assumptions.

## `copy-review`

- Description: Review product copy as a content system by modeling user commitments, terminology, states, and guidance across the strongest available evidence path instead of critiquing isolated strings.
- Trigger: When content quality, clarity, or trust needs an independent review before ship, rewrite, or localization planning.
- Primary MCP/tool: repository, figma, chrome_devtools
- Fallback: notion, reference/ground, search_query
- Best guess: A copy review with evidence-tagged language issues, grouped patterns, and directional rewrite guidance.
- Output: logs/active/<project-slug>/reviews/design-reviewer.md
- Done when: The team knows which language problems are local, which are systemic, how strong the evidence is, and what should change first.

## `design-fidelity-review`

- Description: Compare the implemented surface against the design source of truth by building source and implementation models, then classifying meaningful drift by component, state, breakpoint, and layout behavior.
- Trigger: When a design or implemented surface needs fidelity review before sign-off, bug filing, or remediation planning.
- Primary MCP/tool: figma, chrome_devtools
- Fallback: reference/verify, open
- Best guess: A fidelity review with evidence-tagged drift findings, grouped patterns, and directional remediation guidance.
- Output: logs/active/<project-slug>/reviews/design-reviewer.md
- Done when: Meaningful design drift is identified with evidence, taxonomy, priority, and clear separation between implementation error and source ambiguity.

## `design-system-compliance-review`

- Description: Audit alignment with the design system by modeling the system contract and tracing tokens, components, patterns, and exceptions across the reviewed surface.
- Trigger: When consistency or system conformance is in doubt before release, QA sign-off, or normalization work.
- Primary MCP/tool: figma, repository
- Fallback: reference/reuse, chrome_devtools
- Best guess: A design-system compliance review with evidence-tagged conformance issues, grouped variance patterns, and justified exceptions called out.
- Output: logs/active/<project-slug>/reviews/design-reviewer.md
- Done when: Design-system conformance issues, justified exceptions, and system gaps are concrete, traceable, and actionable.

## `usability-review`

- Description: Run an expert usability inspection of a flow or surface by building a UI model, walking key tasks, and grounding findings in Nielsen's heuristics across the strongest available evidence path.
- Trigger: When UX quality needs a focused expert inspection pass before sign-off, bug filing, or remediation planning.
- Primary MCP/tool: chrome_devtools
- Fallback: figma, reference/ground
- Best guess: A usability review with concrete friction points, grouped patterns, and clearly marked evidence limits.
- Output: logs/active/<project-slug>/reviews/design-reviewer.md
- Done when: The biggest usability risks are explicit, reproducible, severity-rated, grouped into actionable patterns, and labeled by evidence confidence.
