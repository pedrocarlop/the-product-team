# UX Researcher Skill Catalog

Read this file first when you are staffed for orchestrated work.
Use this catalog to choose or confirm the exact role-local workflow to run.
Open only the matching `skills/*.md` files, follow their MCP/fallback sequence, and end your handoff with `Read <skill-paths> skills for this task.`

## `research-plan`

- Description: Structure a study using GQM question formulation, decision impact × uncertainty prioritization, and the attitudinal/behavioral × qualitative/quantitative method selection matrix.
- Trigger: When the team needs a real study plan instead of ad hoc interviews.
- Primary MCP/tool: notion, dovetail
- Fallback: search_query, reference/ground
- Best guess: A research plan with question, method, sample, and outputs.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Every research question maps to a decision, a method, and a sample — and the team can run the study without inventing the protocol later.

## `screener-form-build`

- Description: Design participant screeners using profile modeling, quota sampling logic, and behavioral disqualifier best practices.
- Trigger: When a study needs recruitment or intake filtering.
- Primary MCP/tool: typeform, google_forms
- Fallback: tally, notion, ux-researcher/research-plan
- Best guess: A screener form or equivalent structured questionnaire.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Every question has explicit include/exclude logic, quota targets are defined, and recruiting can start without guessing intent.

## `interview-guide-build`

- Description: Write semi-structured interview guides using topic mapping, probe laddering, JTBD framing, and per-section evidence goals.
- Trigger: When live research sessions need a structured guide.
- Primary MCP/tool: notion
- Fallback: dovetail, looppanel, search_query, ux-researcher/research-plan
- Best guess: An interview guide that supports comparable sessions.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Every section has an evidence goal, mandatory questions are separated from optional probes, and a moderator can run the session without improvising the core script.

## `competitor-research`

- Description: Benchmark adjacent products using landscape modeling, pattern sourcing across Refero/Mobbin/Page Flows, gap analysis, and implication mapping.
- Trigger: When the team needs external pattern or competitor evidence.
- Primary MCP/tool: refero, mobbin
- Secondary MCP/tool: page_flows, ux_archive, similarweb
- Fallback: search_query, open
- Best guess: A benchmark report with patterns, screenshots, and implications.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Competitive set is defined, patterns are inventoried with evidence, gaps are documented, and implications are tied to the current product decision.

## `study-ops-and-recruiting`

- Description: Build the full operational dependency model (recruiting → screening → scheduling → consent → session → incentive → closeout) grounded in UXPA ResearchOps framework.
- Trigger: When research needs a concrete execution plan beyond the study design.
- Primary MCP/tool: rally_uxr, notion
- Secondary MCP/tool: ethnio, calendly, tremendous
- Fallback: ux-researcher/screener-form-build, open
- Best guess: A study ops plan with recruiting flow and logistics.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Every operational phase has an owner, tool, and contingency — and the study can be scheduled and staffed without unresolved dependencies.

## `research-synthesis`

- Description: Transform source material into findings using thematic analysis (Braun & Clarke), affinity diagramming, and the atomic research model (facts → insights → opportunities → recommendations).
- Trigger: After interviews, workshops, or other qualitative studies.
- Primary MCP/tool: dovetail, notion
- Secondary MCP/tool: looppanel, condens, aurelius, figjam, miro
- Fallback: ux-researcher/research-plan, search_query
- Best guess: A synthesis with themes, evidence, and design implications.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Every theme is supported by traceable evidence, every finding has a confidence rating, and the team can act on findings instead of raw notes.

## `research-readout-deck`

- Description: Package research into stakeholder-aligned readouts using the Pyramid Principle and situation → complication → resolution → recommendation narrative arc.
- Trigger: When research must be socialized to decision-makers.
- Primary MCP/tool: notion, pitch
- Secondary MCP/tool: loom, google_slides, canva, confluence
- Fallback: ux-researcher/research-synthesis, open
- Best guess: A research readout deck or memo with findings and actions.
- Output: logs/active/<project-slug>/deliverables/ux-researcher.md
- Done when: Audience-decision model is built, findings lead with insight (not methodology), every recommendation links to evidence, and the stakeholder ask is explicit.
