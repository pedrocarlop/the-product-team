# Content Designer Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `content-review`

- Description: Review an existing content surface for clarity, consistency, and voice.
- Trigger: When the product copy exists but quality is in doubt.
- Primary MCP/tool: repository, notion
- Fallback: search_query, reference/ground
- Best guess: A content review with issues, recommendations, and priorities.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: The team knows what to rewrite and why.

## `conversation-and-guidance-design`

- Description: Write guided help, assistant, or in-product guidance content that supports task completion.
- Trigger: When the product needs embedded guidance or conversational support.
- Primary MCP/tool: notion
- Fallback: search_query, reference/ground
- Best guess: A guidance or conversation design pack.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: The guidance supports the task clearly and fits the product voice.

## `error-empty-success-states`

- Description: Design the messaging for non-happy-path states so users can recover or proceed confidently.
- Trigger: When a feature needs state-specific messaging beyond the default path.
- Primary MCP/tool: notion, figma
- Fallback: reference/trace, search_query
- Best guess: A state-message set for error, empty, loading, and success moments.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: Critical states have explicit user-facing messaging.

## `localization-prep`

- Description: Prepare content for translation, expansion, and locale-sensitive adaptation.
- Trigger: When user-facing text must survive localization cleanly.
- Primary MCP/tool: notion, figma
- Fallback: reference/verify, search_query
- Best guess: A localization-ready content pack with notes on constraints.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: Strings and content patterns are ready for localization work.

## `microcopy-flow-design`

- Description: Write the core product copy across a flow so users know what is happening and what to do next.
- Trigger: When a feature or flow needs coherent UX writing.
- Primary MCP/tool: notion, figma
- Fallback: search_query, reference/ground
- Best guess: A flow-level microcopy set with key user-facing text.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: The flow can be followed without copy ambiguity.

## `naming-and-taxonomy`

- Description: Define names and labels so concepts, navigation, and settings stay coherent.
- Trigger: When terminology or IA wording needs deliberate design.
- Primary MCP/tool: notion
- Fallback: search_query, reference/reuse
- Best guess: A naming and taxonomy proposal with rationale.
- Output: logs/active/<project-slug>/deliverables/content-designer.md
- Done when: Labels are distinct, durable, and understandable.
