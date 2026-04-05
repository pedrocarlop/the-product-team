#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.skill_validation import SkillValidationContext, validate_skill_contexts


PACKAGE_SLUG = "product-team"
MARKER_START = "<!-- PRODUCT_TEAM_FOR_CODEX:START -->"
MARKER_END = "<!-- PRODUCT_TEAM_FOR_CODEX:END -->"
EXPECTED_REPO_WRITE_POLICIES = {
    "orchestrator": "direct_only",
    "frontend-engineer": "explicit_owner_only",
    "backend-engineer": "explicit_owner_only",
    "platform-engineer": "explicit_owner_only",
    "reference": "never",
}


def expected_repo_write_policy(role: str) -> str:
    return EXPECTED_REPO_WRITE_POLICIES.get(role, "never")


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
    return json.loads((root / ".codex" / PACKAGE_SLUG / "manifest.json").read_text(encoding="utf-8"))


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def installed_role_paths(root: Path, role: dict) -> tuple[Path, Path, Path]:
    return (
        root / Path(role["relative_toml_path"]),
        root / Path(role["relative_skills_dir"]),
        root / Path(role["relative_catalog_path"]),
    )


def main() -> int:
    failures: list[str] = []
    skill_contexts: list[SkillValidationContext] = []

    try:
        root = project_root()
    except FileNotFoundError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    manifest = load_manifest(root)
    expected_roles = manifest.get("roles", [])
    installed_names = {role["installed_name"] for role in expected_roles}

    expect(manifest.get("package_name") == PACKAGE_SLUG, "Manifest package_name is incorrect.", failures)
    expect(f"{PACKAGE_SLUG}-orchestrator" in installed_names, "Manifest is missing the orchestrator role.", failures)
    expect(f"{PACKAGE_SLUG}-reference" in installed_names, "Manifest is missing the reference role.", failures)

    agents_md = root / "AGENTS.md"
    expect(agents_md.exists(), "Missing AGENTS.md in target project.", failures)
    if agents_md.exists():
        agents_text = agents_md.read_text(encoding="utf-8")
        expect(MARKER_START in agents_text and MARKER_END in agents_text, "AGENTS.md is missing Product Team markers.", failures)
        expect("skill_paths" in agents_text, "AGENTS.md is missing the skill_paths assignment rule.", failures)
        expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in agents_text, "AGENTS.md is missing the fallback rule.", failures)

    package_readme_path = root / ".codex" / PACKAGE_SLUG / "README.md"
    expect(package_readme_path.exists(), "Missing installed package README.", failures)
    if package_readme_path.exists():
        package_readme = package_readme_path.read_text(encoding="utf-8")
        expect("ui-designer" in package_readme and "ux-researcher" in package_readme, "Installed package README missing new role topology.", failures)
        expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in package_readme, "Installed package README missing fallback rule.", failures)
        expect("shadcn/ui" in package_readme, "Installed package README missing shadcn/ui foundation guidance.", failures)

    logs_contract = root / ".codex" / PACKAGE_SLUG / "references" / "logs-workflow-contract.md"
    expect(logs_contract.exists(), "Missing installed logs contract reference doc.", failures)
    if logs_contract.exists():
        logs_text = logs_contract.read_text(encoding="utf-8")
        expect("evidence_mode" in logs_text, "Installed logs contract missing evidence_mode.", failures)
        expect("skill_paths" in logs_text, "Installed logs contract missing skill_paths.", failures)

    project_ds_spec_template = root / ".codex" / PACKAGE_SLUG / "references" / "project-ds-spec-template.md"
    expect(project_ds_spec_template.exists(), "Missing installed project ds-spec template.", failures)
    if project_ds_spec_template.exists():
        template_text = project_ds_spec_template.read_text(encoding="utf-8")
        expect("project-ds-spec.md" in template_text, "Installed project ds-spec template missing artifact path guidance.", failures)
        expect("## Implementation Foundation" in template_text, "Installed project ds-spec template missing implementation foundation section.", failures)

    reference_library_readme = root / ".codex" / PACKAGE_SLUG / "references" / "reference-design-systems" / "README.md"
    expect(reference_library_readme.exists(), "Missing installed reference design systems library index.", failures)
    if reference_library_readme.exists():
        library_text = reference_library_readme.read_text(encoding="utf-8")
        expect("inspiration-only" in library_text or "inspiration only" in library_text, "Installed reference design systems library index missing reference-only guidance.", failures)

    for role in expected_roles:
        source_name = role["source_name"]
        toml_path, skills_dir, catalog_path = installed_role_paths(root, role)
        expect(toml_path.exists(), f"Missing agent definition: {toml_path}", failures)
        expect(skills_dir.is_dir(), f"Missing skills directory: {skills_dir}", failures)
        expect(catalog_path.exists(), f"Missing skill catalog: {catalog_path}", failures)

        if not toml_path.exists():
            continue

        data = load_toml(toml_path)
        prompt = data.get("system_prompt", "")

        expect(data.get("name") == role["installed_name"], f"{toml_path}: installed name mismatch.", failures)
        expect(data.get("execution_policy", {}).get("repo_write_policy") == expected_repo_write_policy(source_name), f"{toml_path}: unexpected repo_write_policy.", failures)
        expect("model_reasoning_effort" in toml_path.read_text(encoding="utf-8"), f"{toml_path}: must use model_reasoning_effort.", failures)
        expect(re.search(r"^reasoning_effort\s*=", toml_path.read_text(encoding="utf-8"), re.MULTILINE) is None, f"{toml_path}: uses legacy reasoning_effort.", failures)

        skill_files = tuple(sorted(skills_dir.rglob("*.md")))
        skill_contexts.append(
            SkillValidationContext(
                discipline=role["discipline"],
                role_name=source_name,
                mcp_servers=tuple(sorted(data.get("capabilities", {}).get("mcp_servers", []))),
                web_tools=tuple(sorted(data.get("capabilities", {}).get("web_tools", []))),
                skill_files=skill_files,
            )
        )

        if source_name == "orchestrator":
            expect("skill_paths" in prompt and "primary_tools" in prompt and "fallback_policy" in prompt and "evidence_mode" in prompt, f"{toml_path}: orchestrator prompt missing new assignment fields.", failures)
            continue

        if source_name == "reference":
            expect(data.get("outputs", {}).get("artifact_paths", []) == [], f"{toml_path}: reference must not own artifacts.", failures)
            expect(data.get("permissions", {}).get("may_write_paths", []) == [], f"{toml_path}: reference must not write artifacts.", failures)
            continue

        expect("skill-catalog.md" in prompt, f"{toml_path}: specialist prompt missing skill catalog rule.", failures)
        expect("skill_paths" in prompt, f"{toml_path}: specialist prompt missing skill_paths rule.", failures)
        expect("primary MCP -> alternative tool/MCP -> best guess inferred output" in prompt, f"{toml_path}: specialist prompt missing fallback sequence.", failures)
        expect("sourced" in prompt and "fallback" in prompt and "inferred" in prompt, f"{toml_path}: specialist prompt missing evidence labels.", failures)

        catalog_text = catalog_path.read_text(encoding="utf-8")
        expect("Primary MCP/tool:" in catalog_text, f"{catalog_path}: skill catalog missing primary tool summary.", failures)
        expect("Fallback:" in catalog_text, f"{catalog_path}: skill catalog missing fallback summary.", failures)
        expect("Done when:" in catalog_text, f"{catalog_path}: skill catalog missing done-when summary.", failures)

        if source_name == "ui-designer":
            concept_skill = skills_dir / "ui-concept-direction.md"
            screen_skill = skills_dir / "screen-production-design.md"
            if concept_skill.exists():
                concept_text = concept_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in concept_text, f"{concept_skill}: missing project ds-spec guidance.", failures)
                expect("reference-design-systems" in concept_text, f"{concept_skill}: missing reference design systems guidance.", failures)
                expect("shadcn/ui" in concept_text, f"{concept_skill}: missing shadcn/ui foundation guidance.", failures)
            if screen_skill.exists():
                screen_text = screen_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in screen_text, f"{screen_skill}: missing project ds-spec alignment guidance.", failures)

        if source_name == "design-systems-designer":
            token_skill = skills_dir / "token-architecture.md"
            audit_skill = skills_dir / "system-audit.md"
            if token_skill.exists():
                token_text = token_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in token_text, f"{token_skill}: missing project ds-spec translation guidance.", failures)
            if audit_skill.exists():
                audit_text = audit_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in audit_text, f"{audit_skill}: missing project ds-spec audit guidance.", failures)

        if source_name == "frontend-engineer":
            implement_skill = skills_dir / "implement-from-design.md"
            component_skill = skills_dir / "component-implementation.md"
            if implement_skill.exists():
                implement_text = implement_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in implement_text, f"{implement_skill}: missing project ds-spec guidance.", failures)
                expect("shadcn@latest" in implement_text, f"{implement_skill}: missing latest shadcn init guidance.", failures)
            if component_skill.exists():
                component_text = component_skill.read_text(encoding="utf-8")
                expect("project-ds-spec.md" in component_text, f"{component_skill}: missing project ds-spec guidance.", failures)
                expect("shadcn/ui" in component_text, f"{component_skill}: missing shadcn/ui foundation guidance.", failures)

    validate_skill_contexts(skill_contexts, failures, enforce_banned_names=False)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Installed Product Team workflow validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
