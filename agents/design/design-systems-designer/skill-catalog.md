# Design Systems Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `atomic-library-build`

- Description: Build or reorganize the component library using atomic design as the structuring model.
- Trigger: When reusable components need a clear system structure.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: An atomic component library plan or build description.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Atoms, molecules, organisms, and higher-level patterns are clearly organized.

## `component-governance`

- Description: Define the rules for component ownership, variants, contribution, and deprecation.
- Trigger: When system growth needs operating rules, not just files.
- Primary MCP/tool: notion, figma
- Fallback: repository, reference/reuse
- Best guess: A governance model for component lifecycle and usage.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Teams know how components enter, change, and leave the system.

## `design-code-mapping`

- Description: Map design system components and tokens to their implementation counterparts.
- Trigger: When design and code need a reliable bridge.
- Primary MCP/tool: figma, repository
- Fallback: reference/trace, reference/verify
- Best guess: A design-code mapping with reusable implementation guidance.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md
- Done when: Design and engineering can identify the same system primitives reliably.

## `spacing-and-layout-scale`

- Description: Define the spacing, sizing, and layout scale that underpins UI consistency.
- Trigger: When system consistency depends on clearer spatial rules.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: A spacing and layout scale with usage guidance.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Designers can compose surfaces without inventing spacing ad hoc.

## `system-audit`

- Description: Assess the current design system for gaps, drift, duplication, and adoption risks.
- Trigger: When the system needs a baseline before extension or cleanup.
- Primary MCP/tool: figma, repository
- Fallback: paper, reference/ground
- Best guess: A system audit with prioritized gaps and recommendations.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: The team knows the real system health and next moves.

## `system-qa-and-adoption`

- Description: Validate the live system for consistency and define how teams should adopt it.
- Trigger: When the system exists but adoption or QA is weak.
- Primary MCP/tool: repository, figma
- Fallback: chrome_devtools, reference/verify
- Best guess: A system QA and adoption plan with key issues and rollout guidance.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: System issues and adoption blockers are concrete and prioritized.

## `token-architecture`

- Description: Define or refine the token model for color, typography, spacing, and semantic usage.
- Trigger: When the system needs a durable token foundation.
- Primary MCP/tool: figma
- Fallback: paper, repository
- Best guess: A token architecture proposal tied to system usage.
- Output: logs/active/<project-slug>/deliverables/design-systems-designer.md, logs/active/<project-slug>/deliverables/project-ds-spec.md
- Done when: Tokens are structured well enough to scale consistently.
