---
name: implement-from-design
description: Implement a design faithfully in production code with the required states and interactions.
trigger: When approved design work is ready for implementation.
primary_mcp: repository, figma
fallback_tools: chrome_devtools, reference/trace
best_guess_output: Working UI implementation aligned to the design spec.
output_artifacts: logs/active/<project-slug>/deliverables/frontend-engineer.md
section_anchor: "## Skill: implement-from-design"
done_when: The implemented surface matches the intended structure and behavior.
---

# Implement From Design

## Purpose

Implement a design faithfully in production code with the required states and interactions.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: implement-from-design`, include:
- `### Design target`: Identify the design source, surface, or approved direction being implemented.
- `### System foundation`: State whether the pass reuses an existing UI foundation or initializes one from `project-ds-spec.md`.
- `### Implementation scope`: Define what parts of the design are in scope for this pass.
- `### State coverage`: List required states, flows, and conditional behavior that must be represented in code.
- `### Interaction notes`: Capture important interactions, transitions, or behavioral nuances.
- `### Code touchpoints`: Identify the files, components, or routes involved.
- `### Open implementation risks`: Call out remaining uncertainty, gaps, or blockers.

## Tool Path

- Start with `repository, figma`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `chrome_devtools, reference/trace`.
- If both paths fail, produce the best-guess output described as: Working UI implementation aligned to the design spec.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Read `logs/active/<project-slug>/deliverables/project-ds-spec.md` first when it exists.
- If `project-ds-spec.md` recommends shadcn/ui, the assignment owns repo writes, and the frontend is blank or near-empty, initialize the latest official shadcn/ui foundation before feature-specific implementation. Prefer a reviewed `shadcn/create` output when the spec includes one; otherwise use the official CLI path such as `pnpm dlx shadcn@latest init -t <framework>` and `--monorepo` when the repo shape requires it.
- Translate the spec into the generated foundation instead of accepting defaults blindly. Align the resulting `components.json`, theme variables, primitive base, icon library, registries, and starter components to the decisions recorded in `project-ds-spec.md`.
- Do not re-run shadcn initialization over an established system just because it would be convenient. If the project is no longer blank enough, keep the existing foundation and note the mismatch or incremental-adoption plan instead.
- Preserve fidelity-critical design details without turning the artifact into line-by-line implementation prose.
- Call out where design intent is clear versus where engineering judgment had to fill gaps.
- Keep code touchpoints exact so downstream review can verify the right surface.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/frontend-engineer.md`.
- Keep all work for this skill inside `## Skill: implement-from-design`.
- Record which tool path was used and why.
- If this pass initialized shadcn/ui, record the exact setup path and the foundation files it created or updated.
- Ensure the section meets this done-when bar: The implemented surface matches the intended structure and behavior.
