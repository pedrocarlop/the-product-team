# UI Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `component-design`

- Description: Create or extend reusable UI components needed by the surface.
- Trigger: When the feature needs reusable UI patterns, not just one-off screens.
- Primary MCP/tool: figma
- Fallback: paper, stitch
- Best guess: A component proposal or production component design.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: Component purpose, states, and intended reuse are explicit.

## `responsive-and-state-spec`

- Description: Define how the UI behaves across breakpoints and meaningful interface states.
- Trigger: When a design must survive real devices and async/system states.
- Primary MCP/tool: figma
- Fallback: paper, reference/trace
- Best guess: A responsive and state specification for the screen or flow.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: Desktop, mobile, and critical states are explicitly covered.

## `screen-production-design`

- Description: Produce or refine the definitive screen design for implementation.
- Trigger: When a concept must become a production-ready design.
- Primary MCP/tool: figma
- Fallback: paper, stitch
- Best guess: A production-ready screen spec or screen set.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: Layout, hierarchy, tokens, and core states are specified clearly.

## `ui-concept-direction`

- Description: Explore and establish the visual direction for a new surface before production detailing.
- Trigger: When a new UI direction or concept needs exploration.
- Primary MCP/tool: stitch
- Fallback: paper, search_query
- Best guess: A concept direction with clear visual thesis and promising directions.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: A team can choose or refine a direction instead of staring at a blank page.

## `ui-variant-exploration`

- Description: Generate and compare multiple visual variants against the same product goal.
- Trigger: When the team needs options before committing to a single UI direction.
- Primary MCP/tool: stitch
- Fallback: paper, figma
- Best guess: A variant comparison with recommendation and rationale.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: The chosen direction clearly beats the alternatives on the intended goal.

## `visual-polish-and-consistency`

- Description: Run the final pass on alignment, hierarchy, typography, spacing, and consistency.
- Trigger: When a design works structurally but needs a ship-ready polish pass.
- Primary MCP/tool: figma
- Fallback: paper, chrome_devtools
- Best guess: A polished design with corrected visual inconsistencies.
- Output: logs/active/<project-slug>/deliverables/ui-designer.md
- Done when: The design reads as deliberate and consistent, not provisional.
