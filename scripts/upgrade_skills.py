#!/usr/bin/env python3
"""Upgrade all skills with GIANT standards: structured headers and reflection."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Regex patterns
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
WORKFLOW_RE = re.compile(r"(## (?:Required )?Workflow\n\n)(?:\*\*Follow these steps in order\. Do not skip steps\.\*\*\n\n)?", re.IGNORECASE)
STEP_RE = re.compile(r"### Step (\d+):")

def get_role_from_path(path: Path) -> str:
    # agents/domain/role/skills/...
    parts = path.parts
    try:
        # Expected: (..., 'agents', 'business', 'product-lead', 'skills', ...)
        agents_idx = parts.index('agents')
        return parts[agents_idx + 2]
    except (ValueError, IndexError):
        return "unknown"

def get_discipline_from_path(path: Path) -> str:
    parts = path.parts
    try:
        agents_idx = parts.index('agents')
        return parts[agents_idx + 1]
    except (ValueError, IndexError):
        return "unknown"


def parse_front_matter_fields(content: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(content)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def ensure_section_anchor(content: str, skill_name: str) -> str:
    if "section_anchor:" in content:
        return content

    anchor_line = f'section_anchor: "## Skill: {skill_name}"\n'
    if "done_when:" in content:
        return content.replace("done_when:", anchor_line + "done_when:", 1)

    match = FRONT_MATTER_RE.match(content)
    if not match:
        return content

    insert_at = match.end() - 4
    return content[:insert_at] + anchor_line + content[insert_at:]


def upgrade_business_content(content: str, role: str, skill_name: str) -> str:
    content = ensure_section_anchor(content, skill_name)
    if "## Shared Deliverable Contract" in content:
        return content

    wf_match = WORKFLOW_RE.search(content)
    if not wf_match:
        return content

    fields = parse_front_matter_fields(content)
    primary_mcp = fields.get("primary_mcp", "<primary MCP/tool>")
    fallback_tools = fields.get("fallback_tools", "<fallback tools>")
    best_guess_output = fields.get("best_guess_output", "<best guess output>")
    output_artifact = fields.get("output_artifacts", f"logs/active/<project-slug>/deliverables/{role}.md")
    done_when = fields.get("done_when", "<done when>")

    business_scaffold = f"""## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: {skill_name}`, include:
- `### Objective`
- `### Evidence and inputs`
- `### Analysis`
- `### Recommendation`
- `### Risks and open questions`

## Tool Path

- Start with `{primary_mcp}`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `{fallback_tools}`.
- If both paths fail, produce the best-guess output described as: {best_guess_output}
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Replace the generic section list above with business-skill-specific sections before shipping.
- Preserve concrete details that downstream roles must carry forward.

## Output Contract

- Write or update `{output_artifact}`.
- Keep all work for this skill inside `## Skill: {skill_name}`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: {done_when}
"""

    return content[:wf_match.start()] + business_scaffold


def upgrade_engineer_content(content: str, role: str, skill_name: str) -> str:
    content = ensure_section_anchor(content, skill_name)
    if "## Shared Deliverable Contract" in content:
        return content

    wf_match = WORKFLOW_RE.search(content)
    if not wf_match:
        return content

    fields = parse_front_matter_fields(content)
    primary_mcp = fields.get("primary_mcp", "<primary MCP/tool>")
    fallback_tools = fields.get("fallback_tools", "<fallback tools>")
    best_guess_output = fields.get("best_guess_output", "<best guess output>")
    output_artifact = fields.get("output_artifacts", f"logs/active/<project-slug>/deliverables/{role}.md")
    done_when = fields.get("done_when", "<done when>")

    engineer_scaffold = f"""## Shared Deliverable Contract

- Update only the section named by `section_anchor`.
- If the role deliverable does not exist yet, create it with one YAML header, this skill section, and one trailing `## Reflection` block.
- Preserve all other skill sections in the shared role deliverable.
- Update the role-level reflection footer by appending or refreshing `### <skill-name>` with `What worked`, `What didn't`, and `Next steps`.

## Required Deliverable Sections

Within `## Skill: {skill_name}`, include:
- `### Scope`
- `### Source of truth`
- `### Implementation or analysis plan`
- `### Code touchpoints`
- `### Risks and follow-up`

## Tool Path

- Start with `{primary_mcp}`.
- If the primary path is unavailable, blocked, out of credits, or missing setup, switch to `{fallback_tools}`.
- If both paths fail, produce the best-guess output described as: {best_guess_output}
- Label the section clearly as `sourced`, `fallback`, or `inferred` to match the path actually used.

## Workflow Notes

- Replace the generic section list above with engineer-skill-specific sections before shipping.
- Preserve exact repo paths, contracts, and operational details that downstream roles must carry forward.

## Output Contract

- Write or update `{output_artifact}`.
- Keep all work for this skill inside `## Skill: {skill_name}`.
- Record which tool path was used and why.
- Ensure the section meets this done-when bar: {done_when}
"""

    return content[:wf_match.start()] + engineer_scaffold


def upgrade_content(content: str, discipline: str, role: str, skill_name: str) -> str:
    if discipline == "business":
        return upgrade_business_content(content, role, skill_name)
    if discipline == "engineer":
        return upgrade_engineer_content(content, role, skill_name)

    # 1. Check if already upgraded
    if "Step 1: Initialize the Deliverable Header" in content:
        return content

    # 2. Find Workflow section
    wf_match = WORKFLOW_RE.search(content)
    if not wf_match:
        return content

    header_step = f"""### Step 1: Initialize the Deliverable Header
Every deliverable for this skill must start with the standard YAML header:
```yaml
---
role: {role}
project: <slug>
deliverable: {role}.md
confidence: <0.0-1.0>
inputs_used: [context.md, <others>]
---
```

"""
    
    # Insert Header Step
    insertion_point = wf_match.end()
    new_content = content[:insertion_point] + header_step + content[insertion_point:]

    # 3. Renumber existing steps
    def renumber(match):
        num = int(match.group(1))
        return f"### Step {num + 1}:"
    
    # We only want to renumber steps AFTER our new Step 1
    # Find all steps starting from our new insertion point
    parts = re.split(r"(### Step \d+:)", new_content)
    # the first Step 1 is ours, don't renumber it.
    # Actually, let's just renumber everything from the 2nd match onwards.
    step_count = 0
    final_parts = []
    for part in parts:
        if part.startswith("### Step"):
            step_count += 1
            if step_count > 1:
                final_parts.append(f"### Step {step_count}:")
            else:
                final_parts.append(part)
        else:
            final_parts.append(part)
    
    new_content = "".join(final_parts)

    # 4. Add Reflection Step
    # Find the next header (##) after the workflow steps, or end of file
    # We find the last Step N and append after its block
    last_step_match = list(re.finditer(r"### Step (\d+):", new_content))[-1]
    last_step_num = int(last_step_match.group(1))
    
    reflection_step = f"""
### Step {last_step_num + 1}: Mandatory Reflection (Interleaved Thinking)
End the deliverable with a `## Reflection` section. Self-critique the work:
- **What worked**: successful implementation or analysis details.
- **What didn't**: trade-offs, shortcuts, or known limitations.
- **Next steps**: specific guidance for downstream roles or the reviewer.
"""

    # We need to find where the last step ends. 
    # Usually it ends at the next ## header or end of file.
    search_start = last_step_match.end()
    next_header = re.search(r"\n## ", new_content[search_start:])
    if next_header:
        reflection_point = search_start + next_header.start()
        new_content = new_content[:reflection_point] + reflection_step + new_content[reflection_point:]
    else:
        new_content = new_content.rstrip() + "\n" + reflection_step

    return new_content

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    skills_paths = list(ROOT.glob("agents/**/skills/**/*.md"))
    updated = 0
    stale = 0

    for path in skills_paths:
        if path.name == "skill-catalog.md":
            continue
        
        discipline = get_discipline_from_path(path)
        role = get_role_from_path(path)
        skill_name = path.stem
        content = path.read_text(encoding="utf-8")
        new_content = upgrade_content(content, discipline, role, skill_name)

        if content != new_content:
            if args.check:
                print(f"STALE: {path}")
                stale += 1
            elif args.write:
                path.write_text(new_content, encoding="utf-8")
                updated += 1
            else:
                print(f"WOULD UPDATE: {path}")
                updated += 1

    if args.check:
        return 1 if stale > 0 else 0
    
    if args.write:
        print(f"Updated {updated} skill files.")
    else:
        print(f"Found {updated} skill files to update. Run with --write to apply.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
