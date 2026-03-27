#!/usr/bin/env python3
"""Remove activation_hints from skill YAML frontmatter where the body has a 'When to Use' section."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"

# Match the activation_hints block in YAML frontmatter (multi-line list)
ACTIVATION_HINTS_RE = re.compile(
    r"activation_hints:\n(?:  - [^\n]+\n)+",
)


def process_skill(path: Path) -> bool:
    """Strip activation_hints if the body has a 'When to Use' section. Returns True if changed."""
    text = path.read_text(encoding="utf-8")

    # Must have YAML frontmatter
    if not text.startswith("---"):
        return False

    # Find frontmatter boundaries
    second_fence = text.index("---", 3)
    frontmatter = text[: second_fence + 3]
    body = text[second_fence + 3 :]

    # Only strip if body has "When to Use" section
    if "## When to Use" not in body:
        return False

    # Only strip if frontmatter has activation_hints
    if "activation_hints:" not in frontmatter:
        return False

    new_frontmatter = ACTIVATION_HINTS_RE.sub("", frontmatter)
    if new_frontmatter == frontmatter:
        return False

    path.write_text(new_frontmatter + body, encoding="utf-8")
    return True


def main() -> int:
    skills = sorted(AGENTS_DIR.rglob("skills/*.md"))
    changed = 0

    for path in skills:
        if process_skill(path):
            changed += 1
            print(f"  {path.relative_to(ROOT)}")

    print(f"\nStripped activation_hints from {changed} of {len(skills)} skill files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
