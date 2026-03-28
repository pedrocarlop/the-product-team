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


def installed_role_paths(root: Path, role: dict) -> tuple[Path, Path, Path]:
    installed_name = role["installed_name"]
    relative_toml_path = role.get("relative_toml_path")
    relative_skills_dir = role.get("relative_skills_dir")
    relative_catalog_path = role.get("relative_catalog_path")

    if relative_toml_path and relative_skills_dir and relative_catalog_path:
        return (
            root / Path(relative_toml_path),
            root / Path(relative_skills_dir),
            root / Path(relative_catalog_path),
        )

    return (
        root / ".codex" / "agents" / f"{installed_name}.toml",
        root / ".codex" / "agents" / installed_name / "skills",
        root / ".codex" / "agents" / installed_name / "skill-catalog.md",
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
    install_source = manifest.get("install_source", {})

    expect(manifest.get("package_name") == PACKAGE_SLUG, "Manifest package_name is incorrect.", failures)
    expect(f"{PACKAGE_SLUG}-orchestrator" in installed_names, "Manifest is missing the orchestrator role.", failures)
    expect(f"{PACKAGE_SLUG}-reference" in installed_names, "Manifest is missing the reference role.", failures)
    expect(
        any(install_source.get(key) for key in ("local_source_root", "repo_url", "archive_url")),
        "Manifest is missing install_source metadata for future updates.",
        failures,
    )

    agents_md = root / "AGENTS.md"
    expect(agents_md.exists(), "Missing AGENTS.md in target project.", failures)
    if agents_md.exists():
        agents_text = agents_md.read_text(encoding="utf-8")
        expect(MARKER_START in agents_text and MARKER_END in agents_text, "AGENTS.md is missing Product Team markers.", failures)

    expect((root / "logs" / "active").is_dir(), "Missing logs/active directory.", failures)
    expect((root / "logs" / "archive").is_dir(), "Missing logs/archive directory.", failures)

    refs_root = root / ".codex" / PACKAGE_SLUG / "references"
    scripts_root = root / ".codex" / PACKAGE_SLUG / "scripts"
    expect((refs_root / "logs-workflow-contract.md").exists(), "Missing installed logs contract reference doc.", failures)
    expect((refs_root / "role-catalog.md").exists(), "Missing installed role catalog reference doc.", failures)
    expect((scripts_root / "validate-install.py").exists(), "Missing installed validate-install.py script.", failures)
    expect((scripts_root / "update-install.py").exists(), "Missing installed update-install.py script.", failures)
    if (refs_root / "logs-workflow-contract.md").exists():
        logs_contract = (refs_root / "logs-workflow-contract.md").read_text(encoding="utf-8")
        expect("This is the plan" in logs_contract, "Installed logs contract is missing the approval handoff opener.", failures)
        expect("Do you want to proceed?" in logs_contract, "Installed logs contract is missing the approval handoff question.", failures)
        expect("Execution-grade specialist plan" in logs_contract, "Installed logs contract is missing the detailed role-plan contract.", failures)
        expect("Role-local skills consulted" in logs_contract, "Installed logs contract is missing the skills-consulted plan contract.", failures)
        expect("the orchestrator must quickly scan its own role-local `skill-catalog.md`" in logs_contract, "Installed logs contract is missing the orchestrator self-scan rule.", failures)
        expect("Critical detail register" in logs_contract, "Installed logs contract is missing the unified-plan detail register contract.", failures)
        expect("Overlap resolutions and conflict decisions" in logs_contract, "Installed logs contract is missing the overlap-resolution contract.", failures)

    orchestrator_name = f"{PACKAGE_SLUG}-orchestrator"
    reference_name = f"{PACKAGE_SLUG}-reference"

    for role in expected_roles:
        source_name = role["source_name"]
        installed_name = role["installed_name"]
        toml_path, skills_dir, catalog_path = installed_role_paths(root, role)

        expect(toml_path.exists(), f"Missing agent definition: {toml_path}", failures)
        expect(skills_dir.is_dir(), f"Missing skills directory: {skills_dir}", failures)
        expect(catalog_path.exists(), f"Missing skill catalog: {catalog_path}", failures)
        if skills_dir.is_dir():
            expect(any(path.suffix == ".md" for path in skills_dir.rglob("*.md")), f"No markdown skills found in {skills_dir}", failures)
        if catalog_path.exists():
            catalog_text = catalog_path.read_text(encoding="utf-8")
            expect("Read this file first" in catalog_text, f"{catalog_path}: skill catalog missing quick-scan guidance.", failures)
            expect("Read <skill-paths> skills for this task." in catalog_text, f"{catalog_path}: skill catalog missing handoff note contract.", failures)

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
            prompt = data.get("system_prompt", "")
            expect("your own `skill-catalog.md`" in prompt, f"{toml_path}: orchestrator prompt missing own-skill scan rule.", failures)
            expect("This is the plan" in prompt, f"{toml_path}: orchestrator prompt missing approval handoff opener.", failures)
            expect("Do you want to proceed?" in prompt, f"{toml_path}: orchestrator prompt missing approval handoff question.", failures)
            expect("read each staffed role's `skill-catalog.md`" in prompt, f"{toml_path}: orchestrator prompt missing staffed-role skill-reading rule.", failures)
            expect("best-practice source material" in prompt, f"{toml_path}: orchestrator prompt missing skill-derived best-practice rule.", failures)
            expect("Preserve all material implementation detail" in prompt, f"{toml_path}: orchestrator prompt missing detail-preservation rule.", failures)
            expect("Critical details that must survive merge" in prompt, f"{toml_path}: orchestrator prompt missing must-carry detail contract.", failures)
            expect("Do not delete detail from specialist plans during merge" in prompt, f"{toml_path}: orchestrator prompt missing no-detail-deletion rule.", failures)
            if catalog_path.exists():
                catalog_text = catalog_path.read_text(encoding="utf-8")
                expect("Read this file first on every request before meaningful work." in catalog_text, f"{catalog_path}: orchestrator skill catalog missing every-request scan rule.", failures)
        else:
            handoff_to = role_boundary.get("handoff_to", [])
            expect(orchestrator_name in handoff_to, f"{toml_path}: handoff_to must include {orchestrator_name!r}.", failures)
            if source_name != "reference":
                prompt = data.get("system_prompt", "")
                expect("execution-grade plan" in prompt, f"{toml_path}: specialist prompt missing detailed planning rule.", failures)
                expect("Role-local skills consulted" in prompt, f"{toml_path}: specialist prompt missing skills-consulted planning section.", failures)
                expect("Critical details that must survive merge" in prompt, f"{toml_path}: specialist prompt missing must-carry detail section contract.", failures)
                expect("Do not silently drop planned concrete details" in prompt, f"{toml_path}: specialist prompt missing execution detail preservation rule.", failures)

        expect("reference" not in local_skills, f"{toml_path}: local_skills must not contain bare 'reference'.", failures)

        if source_name != "reference" and reference_name in local_skills:
            reference_role = roles_by_name.get(reference_name, {"installed_name": reference_name})
            reference_path, _, _ = installed_role_paths(root, reference_role)
            expect(reference_path.exists(), f"{toml_path}: references shared skill {reference_name!r}, but the shared role is missing.", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Installed Product Team workflow validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
