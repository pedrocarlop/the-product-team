#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path


PACKAGE_SLUG = "product-team"
MARKER_START = "<!-- PRODUCT_TEAM_FOR_CODEX:START -->"
MARKER_END = "<!-- PRODUCT_TEAM_FOR_CODEX:END -->"


def project_root() -> Path:
    script_path = Path(__file__).resolve()
    for candidate in (script_path.parent,) + tuple(script_path.parents):
        manifest_path = candidate / ".codex" / PACKAGE_SLUG / "manifest.json"
        if manifest_path.exists():
            return candidate
    raise FileNotFoundError(
        "Could not find .codex/product-team/manifest.json. "
        "Run this validator from an installed target repository."
    )


def expect(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def load_manifest(root: Path) -> dict:
    manifest_path = root / ".codex" / PACKAGE_SLUG / "manifest.json"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def installed_role_paths(root: Path, role: dict) -> tuple[Path, Path]:
    installed_name = role["installed_name"]
    relative_toml_path = role.get("relative_toml_path")
    relative_skills_dir = role.get("relative_skills_dir")

    if relative_toml_path and relative_skills_dir:
        return root / Path(relative_toml_path), root / Path(relative_skills_dir)

    return (
        root / ".codex" / "agents" / f"{installed_name}.toml",
        root / ".codex" / "agents" / installed_name / "skills",
    )


def main() -> int:
    failures: list[str] = []

    try:
        root = project_root()
    except FileNotFoundError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    manifest_path = root / ".codex" / PACKAGE_SLUG / "manifest.json"
    expect(manifest_path.exists(), f"Missing manifest: {manifest_path}", failures)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    manifest = load_manifest(root)
    expected_roles = manifest.get("roles", [])
    roles_by_name = {role["installed_name"]: role for role in expected_roles}
    installed_names = {role["installed_name"] for role in expected_roles}

    expect(manifest.get("package_name") == PACKAGE_SLUG, "Manifest package_name is incorrect.", failures)
    expect(f"{PACKAGE_SLUG}-orchestrator" in installed_names, "Manifest is missing the orchestrator role.", failures)
    expect(f"{PACKAGE_SLUG}-reference" in installed_names, "Manifest is missing the reference role.", failures)

    agents_md = root / "AGENTS.md"
    expect(agents_md.exists(), "Missing AGENTS.md in target project.", failures)
    if agents_md.exists():
        agents_text = agents_md.read_text(encoding="utf-8")
        expect(MARKER_START in agents_text and MARKER_END in agents_text, "AGENTS.md is missing Product Team markers.", failures)

    expect((root / "logs" / "active").is_dir(), "Missing logs/active directory.", failures)
    expect((root / "logs" / "archive").is_dir(), "Missing logs/archive directory.", failures)

    refs_root = root / ".codex" / PACKAGE_SLUG / "references"
    expect((refs_root / "logs-workflow-contract.md").exists(), "Missing installed logs contract reference doc.", failures)
    expect((refs_root / "role-catalog.md").exists(), "Missing installed role catalog reference doc.", failures)

    orchestrator_name = f"{PACKAGE_SLUG}-orchestrator"
    reference_name = f"{PACKAGE_SLUG}-reference"

    for role in expected_roles:
        source_name = role["source_name"]
        installed_name = role["installed_name"]
        toml_path, skills_dir = installed_role_paths(root, role)

        expect(toml_path.exists(), f"Missing agent definition: {toml_path}", failures)
        expect(skills_dir.is_dir(), f"Missing skills directory: {skills_dir}", failures)
        if skills_dir.is_dir():
            expect(any(path.suffix == ".md" for path in skills_dir.rglob("*.md")), f"No markdown skills found in {skills_dir}", failures)

        if not toml_path.exists():
            continue

        data = load_toml(toml_path)
        expect(data.get("name") == installed_name, f"{toml_path}: name must be {installed_name!r}.", failures)

        role_boundary = data.get("role_boundary", {})
        capabilities = data.get("capabilities", {})
        local_skills = capabilities.get("local_skills", [])

        if source_name == "orchestrator":
            execution_policy = data.get("execution_policy", {})
            expect(execution_policy.get("role_kind") == "orchestrator", f"{toml_path}: orchestrator role_kind must be orchestrator.", failures)
        else:
            handoff_to = role_boundary.get("handoff_to", [])
            expect(orchestrator_name in handoff_to, f"{toml_path}: handoff_to must include {orchestrator_name!r}.", failures)

        expect("reference" not in local_skills, f"{toml_path}: local_skills must not contain bare 'reference'.", failures)

        if source_name != "reference" and reference_name in local_skills:
            reference_role = roles_by_name.get(reference_name, {"installed_name": reference_name})
            reference_path, _ = installed_role_paths(root, reference_role)
            expect(reference_path.exists(), f"{toml_path}: references shared skill {reference_name!r}, but the shared role is missing.", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Installed Product Team workflow validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
