#!/usr/bin/env python3
"""
Migrate deliverable paths from logs/ to knowledge/.

Replaces:
  logs/active/<project-slug>/deliverables/  →  knowledge/
  logs/active/<slug>/deliverables/          →  knowledge/
  logs/active/<project-slug>/runs/<run-id>/deliverables/  →  knowledge/runs/<run-id>/
  logs/active/<slug>/runs/<run-id>/deliverables/          →  knowledge/runs/<run-id>/
  logs/active/<project-slug>/reviews/       →  knowledge/reviews/

Does NOT touch:
  logs/active/<project-slug>/context.md
  logs/active/<project-slug>/plans/
  logs/active/<project-slug>/decisions/
  logs/active/<project-slug>/runs/<run-id>/ (without /deliverables/)
  logs/TIMELINE.md
  logs/archive/
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files to process (skip .git, archive, benchmarks, __pycache__)
SKIP_DIRS = {'.git', '__pycache__', 'logs/archive', 'logs/benchmarks'}

# Ordered replacements (most specific first)
REPLACEMENTS = [
    # runs/<run-id>/deliverables/ patterns
    (
        r'logs/active/<project-slug>/runs/<run-id>/deliverables/',
        'knowledge/runs/<run-id>/'
    ),
    (
        r'logs/active/<slug>/runs/<run-id>/deliverables/',
        'knowledge/runs/<run-id>/'
    ),
    # reviews/ patterns
    (
        r'logs/active/<project-slug>/reviews/',
        'knowledge/reviews/'
    ),
    (
        r'logs/active/<slug>/reviews/',
        'knowledge/reviews/'
    ),
    # deliverables/ patterns (after runs/ to avoid double-replacing)
    (
        r'logs/active/<project-slug>/deliverables/',
        'knowledge/'
    ),
    (
        r'logs/active/<slug>/deliverables/',
        'knowledge/'
    ),
]


def should_process(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    if any(rel.startswith(skip) for skip in SKIP_DIRS):
        return False
    if path.suffix not in ('.md', '.toml', '.sh'):
        return False
    # Don't process the migration script itself or the new READMEs
    if path.name == 'migrate-to-knowledge.py':
        return False
    # Skip files already migrated (knowledge/README.md, app/README.md)
    rel_str = str(path.relative_to(ROOT))
    if rel_str.startswith('knowledge/') or rel_str.startswith('app/'):
        return False
    return True


def migrate_file(path: Path, dry_run: bool = False) -> list[str]:
    changes = []
    content = path.read_text()
    new_content = content

    for old, new in REPLACEMENTS:
        if old in new_content:
            count = new_content.count(old)
            new_content = new_content.replace(old, new)
            changes.append(f"  {old} → {new} ({count}x)")

    if changes and not dry_run:
        path.write_text(new_content)

    return changes


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN (no files will be modified) ===\n")

    total_files = 0
    total_replacements = 0

    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        if not should_process(path):
            continue

        changes = migrate_file(path, dry_run=dry_run)
        if changes:
            rel = path.relative_to(ROOT)
            print(f"{rel}:")
            for c in changes:
                print(c)
            print()
            total_files += 1
            total_replacements += len(changes)

    print(f"{'Would modify' if dry_run else 'Modified'} {total_files} files with {total_replacements} replacement patterns.")

    if dry_run:
        print("\nRe-run without --dry-run to apply changes.")


if __name__ == '__main__':
    main()
