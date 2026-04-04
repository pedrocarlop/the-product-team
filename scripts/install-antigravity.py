#!/usr/bin/env python3
"""Install the Product Team workflow for Antigravity into a target project."""

from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from install import (
    PACKAGE_SLUG,
    PACKAGE_VERSION,
    copy_role,
    detect_install_source,
    discover_roles,
    install_logs,
    install_package_docs,
    parse_args,
    placeholder_target_error,
    remove_previous_managed_roles,
    repo_root,
    write_manifest,
)

MARKER_START = "<!-- PRODUCT_TEAM_FOR_ANTIGRAVITY:START -->"
MARKER_END = "<!-- PRODUCT_TEAM_FOR_ANTIGRAVITY:END -->"
FRAGMENT_NAME = "ANTIGRAVITY.fragment.md"
TARGET_FILE = "ANTIGRAVITY.md"


def managed_antigravity_block(fragment: str) -> str:
    fragment = fragment.strip()
    return f"{MARKER_START}\n{fragment}\n{MARKER_END}\n"


def update_antigravity_md(fragment_path: Path, target_root: Path) -> None:
    ag_path = target_root / TARGET_FILE
    managed_block = managed_antigravity_block(fragment_path.read_text(encoding="utf-8"))

    if not ag_path.exists():
        ag_path.write_text(managed_block, encoding="utf-8")
        return

    current = ag_path.read_text(encoding="utf-8")
    has_start = MARKER_START in current
    has_end = MARKER_END in current

    if has_start != has_end:
        raise RuntimeError(
            f"{TARGET_FILE} contains only one Product Team marker; resolve it manually."
        )

    if has_start and has_end:
        start_index = current.index(MARKER_START)
        end_index = current.index(MARKER_END) + len(MARKER_END)
        replacement = managed_block.rstrip("\n")
        updated = f"{current[:start_index]}{replacement}{current[end_index:]}"
    else:
        prefix = current.rstrip()
        spacer = "\n\n" if prefix else ""
        updated = f"{prefix}{spacer}{managed_block}"

    ag_path.write_text(updated.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    root = repo_root()
    target_root = Path(args.target).expanduser().resolve()
    target_error = placeholder_target_error(args.target, target_root)
    roles = discover_roles(root)
    install_source = detect_install_source(root, args)

    required_paths = [
        root / "assets" / FRAGMENT_NAME,
        root / "assets" / "package-README.md",
        root / "logs" / "README.md",
        root / "references" / "role-catalog.md",
        root / "scripts" / "render_skill_catalogs.py",
        root / "scripts" / "validate-install.py",
        root / "scripts" / "update-install.py",
    ]
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing required source file: {path}", file=sys.stderr)
        return 1

    if target_error:
        print(target_error, file=sys.stderr)
        return 2

    if not roles:
        print("No roles found under agents/.", file=sys.stderr)
        return 1

    target_root.mkdir(parents=True, exist_ok=True)

    remove_previous_managed_roles(target_root, roles)
    with ThreadPoolExecutor(max_workers=8) as pool:
        pool.map(lambda role: copy_role(role, target_root), roles)

    install_package_docs(root, target_root)
    created_logs_readme = install_logs(root, target_root)
    update_antigravity_md(root / "assets" / FRAGMENT_NAME, target_root)
    write_manifest(target_root, roles, install_source)

    print(f"Installed Product Team v{PACKAGE_VERSION} for Antigravity into {target_root}")
    print(f"Installed {len(roles)} namespaced role definitions.")
    if created_logs_readme:
        print("Created logs/README.md from the workflow contract.")
    else:
        print("Kept the target project's existing logs/README.md.")
    print("Next step: python3 .codex/product-team/scripts/validate-install.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
