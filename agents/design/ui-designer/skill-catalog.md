# UI Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `component-design`

- Description: Create or extend reusable UI components with explicit anatomy, state coverage, reuse rules, and handoff signals.
- Trigger: When the feature needs reusable UI patterns, not just one-off screens.
- Primary MCP/tool: figma
- Fallback: paper (production), stitch (inspiration only)
- Best guess: A reusable component proposal with explicit states, reuse rules, and handoff notes.
- Output: logs/active/<project-slug>/deliverables/ui-designer-component-design.md
- Done when: Component purpose, states, and intended reuse are explicit.

## `responsive-and-state-spec`

- Description: Build a matrix-based contract for how a UI behaves across breakpoints, device classes, and meaningful interface states.
- Trigger: When a design must survive real devices, async states, and content stress without losing hierarchy or usability.
- Primary MCP/tool: figma
- Fallback: paper (production), chrome_devtools, search_query, open, stitch (inspiration)
- Best guess: A responsive and state specification with breakpoint matrix, state matrix, exceptions, stress cases, and implementation signals.
- Output: logs/active/<project-slug>/deliverables/ui-designer-responsive-and-state-spec.md
- Done when: Desktop, mobile, and critical states are explicitly covered, unsupported combinations are named, and implementation signals are clear enough for engineering to preserve.

## `screen-production-design`

- Description: Converge an approved UI direction into implementation-ready screens by locking hierarchy, layout, tokens, states, and any required `project-ds-spec.md` deltas.
- Trigger: When a concept must become a production-ready design.
- Primary MCP/tool: figma
- Fallback: paper (production/edit), stitch (inspiration only)
- Best guess: A production-ready screen spec or screen set with handoff notes and required `project-ds-spec.md` updates.
- Output: logs/active/<project-slug>/deliverables/ui-designer-screen-production-design.md
- Done when: Layout, hierarchy, tokens, and core states are specified clearly.

## `ui-concept-direction`

- Description: Compare and shape multiple visually distinct concept directions, grounded in reference systems and implementation constraints, so the team can choose a direction and seed the shared design spec.
- Trigger: When a new UI direction or concept needs exploration.
- Primary MCP/tool: paper
- Fallback: stitch (inspiration), search_query
- Best guess: A concept direction with clear visual thesis and promising directions.
- Output: logs/active/<project-slug>/deliverables/ui-designer-ui-concept-direction.md
- Done when: A team can choose or refine one of 3 materially different directions, understand the recommended path, and see the shared design spec seeded.

## `ui-variant-exploration`

- Description: Build a comparison model, explore materially different UI directions, and recommend the strongest variant from evidence.
- Trigger: When the team needs options before committing to a single UI direction.
- Primary MCP/tool: paper
- Fallback: stitch (inspiration), figma
- Best guess: A variant comparison with recommendation and rationale.
- Output: logs/active/<project-slug>/deliverables/ui-designer-ui-variant-exploration.md
- Done when: The chosen direction clearly beats the alternatives on the intended goal.

## `visual-polish-and-consistency`

- Description: Run an evidence-based final polish pass that checks hierarchy, spacing, typography, and cross-surface consistency before handoff.
- Trigger: When a design is structurally sound but still needs a final consistency and regression pass.
- Primary MCP/tool: figma
- Fallback: paper (production/edit), chrome_devtools, stitch (inspiration)
- Best guess: A polished design with a concrete issue-fix list, consistency notes, and readiness limits.
- Output: logs/active/<project-slug>/deliverables/ui-designer-visual-polish-and-consistency.md
- Done when: The design reads as deliberate and consistent, with concrete fixes, coverage notes, and readiness gaps called out.
