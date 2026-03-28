#!/usr/bin/env python3
"""Install the Product Team Codex workflow into a target project."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.toml_utils import discover_toml_paths, load_toml


PACKAGE_VERSION = "1.1.1"
PACKAGE_SLUG = "product-team"
PACKAGE_DIRNAME = ".codex/product-team"
MARKER_START = "<!-- PRODUCT_TEAM_FOR_CODEX:START -->"
MARKER_END = "<!-- PRODUCT_TEAM_FOR_CODEX:END -->"
COMMON_PLACEHOLDER_TARGETS = {
    "/path/to/project",
    "/path/to/repo",
    "<path/to/project>",
    "<project-path>",
}
NAME_PATTERN = re.compile(r'^name = "([^"]+)"$', re.MULTILINE)
DISPLAY_NAME_PATTERN = re.compile(r'^display_name = "([^"]+)"$', re.MULTILINE)
LOCAL_SKILLS_PATTERN = re.compile(r"^local_skills = \[(.*)\]$", re.MULTILINE)


@dataclass(frozen=True)
class RoleSpec:
    discipline: str
    source_name: str
    installed_name: str
    source_toml: Path
    source_skills_dir: Path

    @property
    def installed_namespace(self) -> str:
        return f"{PACKAGE_SLUG}-{self.discipline}"

    @property
    def installed_role_dir(self) -> Path:
        return Path(".codex") / "agents" / self.installed_namespace / self.source_name

    @property
    def installed_toml_path(self) -> Path:
        return self.installed_role_dir / self.source_toml.name

    @property
    def installed_skills_dir(self) -> Path:
        return self.installed_role_dir / "skills"

    @property
    def legacy_flat_toml_path(self) -> Path:
        return Path(".codex") / "agents" / f"{self.installed_name}.toml"

    @property
    def legacy_flat_role_dir(self) -> Path:
        return Path(".codex") / "agents" / self.installed_name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the Product Team workflow for Codex into a project folder."
    )
    parser.add_argument(
        "--target",
        default=".",
        help="Project directory to install into. Defaults to the current directory.",
    )
    parser.add_argument(
        "--source-root",
        help="Absolute or relative path to the source Product Team checkout used for this install.",
    )
    parser.add_argument(
        "--source-repo-url",
        help="Canonical repository URL for the Product Team source.",
    )
    parser.add_argument(
        "--source-ref",
        help="Branch or tag to track when updating from a remote archive.",
    )
    parser.add_argument(
        "--source-archive-url",
        help="Archive URL that can be used to fetch the latest Product Team package.",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def placeholder_target_error(raw_target: str, resolved_target: Path) -> str | None:
    raw_target = raw_target.strip()
    normalized_target = raw_target.replace("\\", "/").rstrip("/")

    if "<" in raw_target or ">" in raw_target:
        return (
            f"Refusing to install into placeholder target {raw_target!r}. "
            'Pass the real project folder instead, for example --target "$PWD".'
        )

    if normalized_target in COMMON_PLACEHOLDER_TARGETS:
        return (
            f"Refusing to install into placeholder target {raw_target!r}. "
            'Pass the real project folder instead, for example --target "$PWD".'
        )

    if resolved_target.parts[:4] == (resolved_target.anchor, "path", "to", "project"):
        return (
            f"Refusing to install into placeholder target {str(resolved_target)!r}. "
            'Pass the real project folder instead, for example --target "$PWD".'
        )

    return None


def run_git(root: Path, *args: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip() or None


def normalize_repo_url(url: str | None) -> str | None:
    if not url:
        return None

    normalized = url.strip()
    if normalized.startswith("git@github.com:"):
        normalized = f"https://github.com/{normalized.removeprefix('git@github.com:')}"
    elif normalized.startswith("ssh://git@github.com/"):
        normalized = f"https://github.com/{normalized.removeprefix('ssh://git@github.com/')}"

    if normalized.endswith(".git"):
        normalized = normalized[:-4]

    return normalized


def github_archive_url(repo_url: str | None, ref: str | None) -> str | None:
    if not repo_url or not ref:
        return None
    if not repo_url.startswith("https://github.com/"):
        return None
    return f"{repo_url}/archive/refs/heads/{ref}.tar.gz"


def detect_install_source(root: Path, args: argparse.Namespace) -> dict[str, str | None]:
    local_source_root: str | None = None
    if args.source_root:
        local_source_root = str(Path(args.source_root).expanduser().resolve())
    elif not args.source_repo_url and not args.source_archive_url:
        local_source_root = str(root)

    repo_url = normalize_repo_url(args.source_repo_url) or normalize_repo_url(
        run_git(root, "remote", "get-url", "origin")
    )
    ref = args.source_ref or run_git(root, "rev-parse", "--abbrev-ref", "HEAD")
    if ref == "HEAD":
        ref = None
    if not ref:
        ref = "main"

    archive_url = args.source_archive_url or github_archive_url(repo_url, ref)

    return {
        "install_mode": "local_checkout" if local_source_root else "archive",
        "local_source_root": local_source_root,
        "repo_url": repo_url,
        "ref": ref,
        "archive_url": archive_url,
    }


def managed_agents_block(fragment: str) -> str:
    fragment = fragment.strip()
    return f"{MARKER_START}\n{fragment}\n{MARKER_END}\n"


def update_agents_md(fragment_path: Path, target_root: Path) -> None:
    agents_path = target_root / "AGENTS.md"
    managed_block = managed_agents_block(fragment_path.read_text(encoding="utf-8"))

    if not agents_path.exists():
        agents_path.write_text(managed_block, encoding="utf-8")
        return

    current = agents_path.read_text(encoding="utf-8")
    has_start = MARKER_START in current
    has_end = MARKER_END in current

    if has_start != has_end:
        raise RuntimeError("AGENTS.md contains only one Product Team marker; resolve it manually.")

    if has_start and has_end:
        start_index = current.index(MARKER_START)
        end_index = current.index(MARKER_END) + len(MARKER_END)
        replacement = managed_block.rstrip("\n")
        updated = f"{current[:start_index]}{replacement}{current[end_index:]}"
    else:
        prefix = current.rstrip()
        spacer = "\n\n" if prefix else ""
        updated = f"{prefix}{spacer}{managed_block}"

    agents_path.write_text(updated.rstrip() + "\n", encoding="utf-8")


def rewrite_local_skills(match: re.Match[str]) -> str:
    skills = match.group(1).replace('"reference"', f'"{PACKAGE_SLUG}-reference"')
    return f"local_skills = [{skills}]"


def transform_toml(text: str, role: RoleSpec) -> str:
    text = NAME_PATTERN.sub(f'name = "{role.installed_name}"', text, count=1)
    text = DISPLAY_NAME_PATTERN.sub(
        lambda match: f'display_name = "Product Team {match.group(1)}"',
        text,
        count=1,
    )
    text = text.replace(
        'handoff_to = ["orchestrator"]',
        f'handoff_to = ["{PACKAGE_SLUG}-orchestrator"]',
    )
    text = LOCAL_SKILLS_PATTERN.sub(rewrite_local_skills, text)
    return text


def discover_roles(root: Path) -> list[RoleSpec]:
    roles: list[RoleSpec] = []
    for source_toml in discover_toml_paths(root):
        discipline = source_toml.parent.parent.name
        source_name = load_toml(source_toml)["name"]
        installed_name = f"{PACKAGE_SLUG}-{source_name}"
        roles.append(
            RoleSpec(
                discipline=discipline,
                source_name=source_name,
                installed_name=installed_name,
                source_toml=source_toml,
                source_skills_dir=source_toml.parent / "skills",
            )
        )
    return roles


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def remove_managed_path(path: Path) -> None:
    if path.is_file() or path.is_symlink():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def prune_empty_parents(path: Path, stop: Path) -> None:
    current = path
    while current != stop and current.exists():
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def remove_previous_managed_roles(target_root: Path, current_roles: list[RoleSpec]) -> None:
    manifest_path = target_root / PACKAGE_DIRNAME / "manifest.json"
    managed_paths: set[Path] = set()

    if manifest_path.exists():
        try:
            previous_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous_manifest = {}

        for role in previous_manifest.get("roles", []):
            installed_name = role.get("installed_name")
            if installed_name:
                managed_paths.add(target_root / ".codex" / "agents" / f"{installed_name}.toml")
                managed_paths.add(target_root / ".codex" / "agents" / installed_name)

            relative_toml_path = role.get("relative_toml_path")
            relative_role_dir = role.get("relative_role_dir")
            if relative_toml_path:
                managed_paths.add(target_root / Path(relative_toml_path))
            if relative_role_dir:
                managed_paths.add(target_root / Path(relative_role_dir))

    for role in current_roles:
        managed_paths.add(target_root / role.legacy_flat_toml_path)
        managed_paths.add(target_root / role.legacy_flat_role_dir)
        managed_paths.add(target_root / role.installed_role_dir)

    for path in sorted(managed_paths, key=lambda candidate: len(candidate.parts), reverse=True):
        remove_managed_path(path)

    for namespace_dir in {target_root / ".codex" / "agents" / role.installed_namespace for role in current_roles}:
        prune_empty_parents(namespace_dir, target_root / ".codex" / "agents")


def copy_role(role: RoleSpec, target_root: Path) -> None:
    role_root = target_root / role.installed_role_dir
    ensure_directory(role_root)

    transformed_toml = transform_toml(
        role.source_toml.read_text(encoding="utf-8"),
        role,
    )
    (target_root / role.installed_toml_path).write_text(
        transformed_toml,
        encoding="utf-8",
    )

    target_skills_root = target_root / role.installed_skills_dir

    if role.source_skills_dir.is_dir():
        if target_skills_root.exists():
            shutil.rmtree(target_skills_root)
        shutil.copytree(
            role.source_skills_dir,
            target_skills_root,
            ignore=shutil.ignore_patterns(".DS_Store"),
        )
    else:
        ensure_directory(target_skills_root)


def install_package_docs(root: Path, target_root: Path) -> None:
    package_root = target_root / ".codex" / PACKAGE_SLUG
    refs_root = package_root / "references"
    scripts_root = package_root / "scripts"
    ensure_directory(refs_root)
    ensure_directory(scripts_root)

    (package_root / "README.md").write_text(
        (root / "assets" / "package-README.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (refs_root / "logs-workflow-contract.md").write_text(
        (root / "logs" / "README.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (refs_root / "role-catalog.md").write_text(
        (root / "references" / "role-catalog.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    validate_script_source = root / "scripts" / "validate-install.py"
    validate_script_target = scripts_root / "validate-install.py"
    shutil.copy2(validate_script_source, validate_script_target)
    validate_script_target.chmod(0o755)
    update_script_source = root / "scripts" / "update-install.py"
    update_script_target = scripts_root / "update-install.py"
    shutil.copy2(update_script_source, update_script_target)
    update_script_target.chmod(0o755)


def install_logs(root: Path, target_root: Path) -> bool:
    logs_root = target_root / "logs"
    active_dir = logs_root / "active"
    archive_dir = logs_root / "archive"
    ensure_directory(active_dir)
    ensure_directory(archive_dir)

    for keep_path in (active_dir / ".gitkeep", archive_dir / ".gitkeep"):
        if not keep_path.exists():
            keep_path.write_text("", encoding="utf-8")

    readme_path = logs_root / "README.md"
    if readme_path.exists():
        return False

    readme_path.write_text(
        (root / "logs" / "README.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    return True


def write_manifest(
    target_root: Path,
    roles: list[RoleSpec],
    install_source: dict[str, str | None],
) -> None:
    package_root = target_root / ".codex" / PACKAGE_SLUG
    ensure_directory(package_root)
    manifest = {
        "schema_version": 3,
        "package_name": PACKAGE_SLUG,
        "version": PACKAGE_VERSION,
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "install_source": install_source,
        "managed_agents_markers": {
            "start": MARKER_START,
            "end": MARKER_END,
        },
        "roles": [
            {
                "discipline": role.discipline,
                "source_name": role.source_name,
                "installed_name": role.installed_name,
                "installed_namespace": role.installed_namespace,
                "relative_role_dir": role.installed_role_dir.as_posix(),
                "relative_toml_path": role.installed_toml_path.as_posix(),
                "relative_skills_dir": role.installed_skills_dir.as_posix(),
            }
            for role in roles
        ],
    }
    (package_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    root = repo_root()
    target_root = Path(args.target).expanduser().resolve()
    target_error = placeholder_target_error(args.target, target_root)
    roles = discover_roles(root)
    install_source = detect_install_source(root, args)

    required_paths = [
        root / "assets" / "AGENTS.fragment.md",
        root / "assets" / "package-README.md",
        root / "logs" / "README.md",
        root / "references" / "role-catalog.md",
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
    update_agents_md(root / "assets" / "AGENTS.fragment.md", target_root)
    write_manifest(target_root, roles, install_source)

    print(f"Installed Product Team v{PACKAGE_VERSION} for Codex into {target_root}")
    print(f"Installed {len(roles)} namespaced role definitions.")
    if created_logs_readme:
        print("Created logs/README.md from the workflow contract.")
    else:
        print("Kept the target project's existing logs/README.md.")
    print("Next step: python3 .codex/product-team/scripts/validate-install.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
