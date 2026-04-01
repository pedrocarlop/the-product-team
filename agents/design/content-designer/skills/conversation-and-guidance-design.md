---
name: conversation-and-guidance-design
description: Write guided help, assistant, or in-product guidance content that supports task completion.
trigger: When the product needs embedded guidance or conversational support.
primary_mcp: notion
fallback_tools: search_query, reference/ground
best_guess_output: A guidance or conversation design pack.
output_artifacts: logs/active/<project-slug>/deliverables/content-designer.md
section_anchor: "## Skill: conversation-and-guidance-design"
done_when: The guidance supports the task clearly and fits the product voice.
---

# Conversation And Guidance Design

## Purpose

Write guided help, assistant, or in-product guidance content that supports task completion.

## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: conversation-and-guidance-design`, include:
- `### User intent map`: Explain the user jobs, confusion points, and moments when guidance appears.
- `### Entry points`: Define where guidance starts and what contextual trigger activates it.
- `### Guidance model`: Describe the narrative arc, step logic, or assistant posture.
- `### Key messages`: List the core messages, prompts, and reassurance moments.
- `### Escalation and fallback copy`: Define how the guidance exits, hands off, or recovers from failure.

## Tool Path

- Start with `notion`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `search_query, reference/ground`.
- If both paths fail, produce the best-guess output described as: A guidance or conversation design pack.
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Keep the copy tied to a specific user task instead of writing a generic help article.
- Document the assistant or guidance tone explicitly when the surface is conversational.
- Make the boundaries between guidance, automation, and user action obvious.

## Output Contract

- Write or update `logs/active/<project-slug>/deliverables/content-designer.md`.
- Keep all work for this skill inside `## Skill: conversation-and-guidance-design`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: The guidance supports the task clearly and fits the product voice.
