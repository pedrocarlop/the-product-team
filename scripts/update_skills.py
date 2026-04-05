import re
from pathlib import Path
import sys

def update_toml(file_path):
    print(f"Updating TOML: {file_path}")
    content = file_path.read_text(encoding="utf-8")
    
    # 1. owned_outputs -> target_deliverables
    content = content.replace("owned_outputs", "target_deliverables")
    
    # 2. artifact_paths/may_write_paths update
    content = re.sub(r'(artifact_paths|may_write_paths) = \["(?:logs/active/<project-slug>/deliverables/|knowledge/)[^"]*"\]',
                     r'\1 = ["knowledge/"]', content)
    
    # 3. System prompt update for single deliverable
    # Check if bold header is missing if some other text was introduced
    content = re.sub(r'- Keep your owned output current at `(?:logs/active/<project-slug>/deliverables/|knowledge/)[^`]+`\.',
                     r'- **Lossless Handoff**: Produce one standalone deliverable per assigned skill as named in `owned_outputs`.', content)
    
    # 4. Direct Consumption instruction
    if "- **Direct Consumption**:" not in content:
        # Insert after Role charter or in Execution section
        content = re.sub(r'(Execution:)', r'\1\n- **Direct Consumption**: Read all relevant original skill deliverables from the Execution Manifest (`orchestrator.md`) before acting.', content)

    file_path.write_text(content, encoding="utf-8")

def update_skill_md(file_path):
    print(f"Updating Skill MD: {file_path}")
    content = file_path.read_text(encoding="utf-8")
    
    parts = file_path.parts
    if 'agents' not in parts: return
    idx = parts.index('agents')
    role = parts[idx + 2]
    skill = file_path.stem
    
    # 1. Update YAML output_artifacts
    content = re.sub(r'output_artifacts: (?:logs/active/<project-slug>/deliverables/|knowledge/)[^\n]+',
                     f'output_artifacts: knowledge/{role}-{skill}.md', content)
    
    # 2. Remove section_anchor (with or without numbers, flexible spacing)
    content = re.sub(r'(?:## \d+\. )?section_anchor: [^\n]+\n', '', content, flags=re.IGNORECASE)
    content = re.sub(r'section_anchor: [^\n]+\n', '', content, flags=re.IGNORECASE)
    
    # 3. Prepare new contract
    new_contract = f"""## Lossless Deliverable Contract

- Produce a standalone deliverable at the path specified in the YAML `output_artifacts` (formatted as `knowledge/{role}-{skill}.md`).
- Do not merge this output into a shared role-level document.
- Ensure the deliverable preserves all nuance, edge cases, and rationale for direct consumption by implementation owners.
- Link this deliverable in the Execution Manifest (`orchestrator.md`) once complete.
- Include a `## Reflection` section at the end of the deliverable with `What worked`, `What didn't`, and `Next steps`."""

    # 4. Replace Shared Deliverable Contract (allowing for numbers and flexible spacing)
    # Flexible pattern: allow for 1 or 2 newlines after header, and zero or more bullet points
    pattern_shared = r'## (?:\d+\. )?Shared Deliverable Contract\s*\n+(?:- [^\n]+\n)*'
    if re.search(pattern_shared, content, flags=re.IGNORECASE):
        content = re.sub(pattern_shared, new_contract + "\n", content, flags=re.IGNORECASE)
    
    # 5. Handle "Output Contract" section which may be redundant or conflicting
    pattern_output = r'## (?:\d+\. )?Output Contract\s*\n+(?:- [^\n]+\n)*'
    if re.search(pattern_output, content, flags=re.IGNORECASE):
        content = re.sub(pattern_output, '', content, flags=re.IGNORECASE)

    file_path.write_text(content, encoding="utf-8")

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            target = Path(arg)
            if target.suffix == ".toml": update_toml(target)
            elif target.suffix == ".md": update_skill_md(target)
            else: print(f"Unknown extension: {target}")
        return

    base_dir = Path("agents")
    for toml_file in base_dir.rglob("*.toml"):
        if toml_file.stem != "orchestrator":
            update_toml(toml_file)
            
    for skill_file in base_dir.rglob("skills/*.md"):
        if skill_file.parts[-2] == "orchestrator": continue
        update_skill_md(skill_file)

if __name__ == "__main__":
    main()
