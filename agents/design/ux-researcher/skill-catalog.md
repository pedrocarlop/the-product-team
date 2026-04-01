# UX Researcher Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `competitor-research`

- Description: Benchmark adjacent products and patterns to inform UX decisions.
- Trigger: When the team needs external pattern or competitor evidence.
- Primary MCP/tool: refero
- Fallback: search_query, open
- Best guess: A benchmark report with patterns, screenshots, and implications.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Relevant competitor patterns are documented with evidence or clearly marked inference.

## `interview-guide-build`

- Description: Write the interview or discussion guide with sequencing, probes, and evidence goals.
- Trigger: When live research sessions need a structured guide.
- Primary MCP/tool: notion
- Fallback: search_query, ux-researcher/research-plan
- Best guess: An interview guide that supports comparable sessions.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: A moderator can run sessions without improvising the core script.

## `research-plan`

- Description: Define the research objective, method, sample, risks, and reporting path before the study runs.
- Trigger: When the team needs a real study plan instead of ad hoc interviews.
- Primary MCP/tool: notion
- Fallback: search_query, reference/ground
- Best guess: A research plan with question, method, sample, and outputs.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: A study can be executed without inventing the protocol later.

## `research-readout-deck`

- Description: Package research findings into a readout that aligns stakeholders quickly.
- Trigger: When research must be socialized to decision-makers.
- Primary MCP/tool: notion
- Fallback: ux-researcher/research-synthesis, open
- Best guess: A research readout deck or memo with findings and actions.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: A stakeholder can understand the key findings in one pass.

## `research-synthesis`

- Description: Turn notes, recordings, or artifacts into findings, themes, and recommendations.
- Trigger: After interviews, workshops, or other qualitative studies.
- Primary MCP/tool: notion, figma
- Fallback: ux-researcher/research-plan, search_query
- Best guess: A synthesis with themes, evidence, and design implications.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: The team can act on findings instead of raw notes.

## `screener-form-build`

- Description: Prepare the participant screener or intake form needed to recruit the right people.
- Trigger: When a study needs recruitment or intake filtering.
- Primary MCP/tool: google_forms
- Fallback: notion, ux-researcher/research-plan
- Best guess: A screener form or equivalent structured questionnaire.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Recruiting can start with clear inclusion and exclusion criteria.

## `study-ops-and-recruiting`

- Description: Define the operational plan for scheduling, recruiting, consent, and study logistics.
- Trigger: When research needs a concrete execution plan beyond the study design.
- Primary MCP/tool: notion, google_forms
- Fallback: ux-researcher/screener-form-build, open
- Best guess: A study ops plan with recruiting flow and logistics.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: The study can be scheduled and staffed cleanly.
