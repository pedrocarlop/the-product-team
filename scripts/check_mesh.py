#!/usr/bin/env python3
"""Check the integrity of the agent skill mesh using regex to avoid dependencies."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def get_role_from_path(path: Path) -> str:
    parts = path.parts
    try:
        agents_idx = parts.index('agents')
        # agents/<discipline>/<role>/skills/
        return parts[agents_idx + 2]
    except (ValueError, IndexError):
        return "unknown"

def extract_frontmatter(content: str) -> str:
    match = re.search(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
    if match:
        return match.group(1)
    
    # Fallback for files that might not have delimiters
    return content

def get_mesh_references(frontmatter: str, block_name: str) -> list[str]:
    """Extract list items from a mesh block (inputs or next)."""
    # Find the block start: e.g., "  inputs:"
    # Then find all lines starting with "    - " until the next unindented key
    block_pattern = rf"^\s+{block_name}:\s*\n((?:\s+-\s+.*\n?)*)"
    match = re.search(block_pattern, frontmatter, re.MULTILINE)
    if not match:
        return []
    
    items_block = match.group(1)
    items = []
    for line in items_block.splitlines():
        # Remove trailing comments
        line = line.split('#')[0].strip()
        if not line:
            continue
        # Remove leading list marker
        if line.startswith("-"):
            line = line[1:].strip()
        # Strip quotes and whitespace
        item = line.strip('"\' ')
        if item and item.lower() != 'none':
            items.append(item)
    return items

def get_field(frontmatter: str, field_name: str) -> str:
    match = re.search(rf"^{field_name}:\s*(.*)$", frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"\'')
    return ""

def main():
    skills_paths = list(ROOT.glob("agents/**/skills/*.md"))
    
    skill_registry = {} # { "role:skill_name": path }
    mesh_links = []     # [ (source, type, target) ]
    
    # First pass: Register all skills
    for path in skills_paths:
        if path.name == "skill-catalog.md":
            continue
            
        role = get_role_from_path(path)
        content = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)
        
        skill_name = get_field(fm, "name")
        if not skill_name:
            skill_name = path.stem
            
        full_key = f"{role}:{skill_name}"
        skill_registry[full_key] = path
        
        inputs = get_mesh_references(fm, "inputs")
        for inp in inputs:
            mesh_links.append((full_key, "INPUT", inp))
            
        next_skills = get_mesh_references(fm, "next")
        for nxt in next_skills:
            mesh_links.append((full_key, "NEXT", nxt))

    # Second pass: Check references
    broken_links = []
    
    # Add manual mapping for some known roles that might be listed as business:role:skill or similar
    # The current standard is role:skill
    
    for source, ltype, target in mesh_links:
        # Normalize target: some might have 'business:' prefix which we should ignore for now if it's there
        normalized_target = target
        if target.startswith("business:"):
            normalized_target = target.replace("business:", "", 1)
        if target.startswith("engineer:"):
            normalized_target = target.replace("engineer:", "", 1)
            
        if normalized_target not in skill_registry:
            broken_links.append(f"BROKEN {ltype}: {source} -> {target}")

    if broken_links:
        print(f"Found {len(broken_links)} broken links in the skill mesh:")
        for link in broken_links:
            print(f"  {link}")
        return 1
    else:
        print(f"Skill mesh integrity verified across {len(skill_registry)} skills. All links are valid.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
