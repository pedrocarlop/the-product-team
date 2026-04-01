# Design Reviewer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `accessibility-review`

- Description: Review the surface against accessibility expectations, user impact, and implementation evidence.
- Trigger: When accessibility risk must be assessed before shipping.
- Primary MCP/tool: chrome_devtools
- Fallback: search_query, reference/verify
- Best guess: An accessibility review with findings and likely fix directions.
- Output: logs/active/<project-slug>/deliverables/design-reviewer.md
- Done when: The team knows which barriers matter most and why.

## `copy-review`

- Description: Review labels, states, and guidance for clarity, consistency, and suitability.
- Trigger: When content quality needs independent review.
- Primary MCP/tool: repository, figma
- Fallback: reference/ground, search_query
- Best guess: A copy review with prioritized recommendations.
- Output: logs/active/<project-slug>/deliverables/design-reviewer.md
- Done when: The team knows what content needs rewriting and why.

## `design-fidelity-review`

- Description: Compare the implementation or artifact against the intended design and call out meaningful drift.
- Trigger: When a design or implemented surface needs fidelity review.
- Primary MCP/tool: figma, chrome_devtools
- Fallback: reference/verify, open
- Best guess: A fidelity review with prioritized findings.
- Output: logs/active/<project-slug>/deliverables/design-reviewer.md
- Done when: Meaningful design drift is identified with evidence.

## `design-system-compliance-review`

- Description: Check whether the work aligns with the design system and justified exceptions.
- Trigger: When consistency or system conformance is in doubt.
- Primary MCP/tool: figma, repository
- Fallback: reference/reuse, chrome_devtools
- Best guess: A design-system compliance review with exceptions called out.
- Output: logs/active/<project-slug>/deliverables/design-reviewer.md
- Done when: System conformance issues are concrete and actionable.

## `usability-review`

- Description: Evaluate whether the flow or surface is understandable and operable for the intended task.
- Trigger: When UX quality needs a focused review pass.
- Primary MCP/tool: chrome_devtools
- Fallback: figma, reference/ground
- Best guess: A usability review with concrete friction points and risk.
- Output: logs/active/<project-slug>/deliverables/design-reviewer.md
- Done when: The biggest usability risks are explicit and reproducible.
