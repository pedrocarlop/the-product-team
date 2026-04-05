#!/usr/bin/env python3
"""Update an installed Product Team package to the latest available source."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path


PACKAGE_SLUG = "product-team"
CANDIDATE_BASE_DIRS = (".codex", ".claude", ".antigravity")

BASE_DIR_TO_PLATFORM = {
    ".codex": "codex",
    ".claude": "claude",
    ".antigravity": "antigravity",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update an installed Product Team workflow in the current project."
    )
    parser.add_argument(
        "--source",
        choices=("auto", "local", "remote"),
        default="auto",
        help="Where to pull the update from. Defaults to auto.",
    )
    parser.add_argument(
        "--ref",
        help="Override the tracked branch or tag when updating from a remote archive.",
    )
    return parser.parse_args()


def detect_base_dir(root: Path) -> str | None:
    for candidate in CANDIDATE_BASE_DIRS:
        if (root / candidate / PACKAGE_SLUG / "manifest.json").exists():
            return candidate
    return None


def project_root() -> Path:
    script_path = Path(__file__).resolve()
    for candidate in (script_path.parent,) + tuple(script_path.parents):
        if detect_base_dir(candidate):
            return candidate
    raise FileNotFoundError(
        "Could not find product-team manifest.json in any of "
        f"{', '.join(CANDIDATE_BASE_DIRS)}. "
        "Run this updater from an installed target repository."
    )


def load_manifest(root: Path, base_dir: str) -> dict:
    manifest_path = root / base_dir / PACKAGE_SLUG / "manifest.json"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def github_archive_url(repo_url: str | None, ref: str | None) -> str | None:
    if not repo_url or not ref:
        return None
    if not repo_url.startswith("https://github.com/"):
        return None
    return f"{repo_url}/archive/refs/heads/{ref}.tar.gz"


def local_install_script(local_source_root: str | None) -> Path | None:
    if not local_source_root:
        return None
    install_path = Path(local_source_root).expanduser().resolve() / "scripts" / "install.py"
    if install_path.exists():
        return install_path
    return None


def run_installer(install_script: Path, target_root: Path, extra_args: list[str] | None = None) -> int:
    cmd = [sys.executable, str(install_script), "--target", str(target_root)]
    if extra_args:
        cmd.extend(extra_args)
    completed = subprocess.run(cmd)
    return completed.returncode


def extract_archive(archive_url: str, destination: Path) -> Path:
    archive_path = destination / "product-team.tar.gz"
    urllib.request.urlretrieve(archive_url, archive_path)

    with tarfile.open(archive_path, "r:gz") as archive:
        archive.extractall(destination, filter="data")

    candidates = [path for path in destination.iterdir() if path.is_dir()]
    for candidate in candidates:
        if (candidate / "scripts" / "install.py").exists():
            return candidate

    raise FileNotFoundError(
        f"Could not find scripts/install.py in downloaded archive from {archive_url}"
    )


def update_from_remote(
    target_root: Path,
    platform: str,
    repo_url: str | None,
    ref: str | None,
    archive_url: str | None,
) -> int:
    effective_ref = ref or "main"
    effective_archive_url = archive_url or github_archive_url(repo_url, effective_ref)
    if not effective_archive_url:
        print(
            "No remote archive URL is recorded for this install. "
            "Reinstall once from the source repo to seed updater metadata.",
            file=sys.stderr,
        )
        return 1

    with tempfile.TemporaryDirectory(prefix="product-team-update-") as tmp_dir:
        extracted_root = extract_archive(effective_archive_url, Path(tmp_dir))
        extra_args = [
            "--platform",
            platform,
            "--source-ref",
            effective_ref,
            "--source-archive-url",
            effective_archive_url,
        ]
        if repo_url:
            extra_args.extend(["--source-repo-url", repo_url])
        return run_installer(
            extracted_root / "scripts" / "install.py",
            target_root,
            extra_args=extra_args,
        )


def main() -> int:
    args = parse_args()

    try:
        root = project_root()
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    base_dir = detect_base_dir(root)
    assert base_dir is not None
    manifest = load_manifest(root, base_dir)
    install_source = manifest.get("install_source", {})

    platform = manifest.get("platform") or BASE_DIR_TO_PLATFORM.get(base_dir, "codex")

    local_script = local_install_script(install_source.get("local_source_root"))
    repo_url = install_source.get("repo_url")
    ref = args.ref or install_source.get("ref")
    archive_url = install_source.get("archive_url")

    if args.source in {"auto", "local"} and local_script:
        return run_installer(local_script, root, extra_args=["--platform", platform])

    if args.source == "local":
        print(
            "The recorded local Product Team source checkout is unavailable. "
            "Use --source remote or reinstall from a live checkout.",
            file=sys.stderr,
        )
        return 1

    return update_from_remote(root, platform, repo_url, ref, archive_url)


if __name__ == "__main__":
    raise SystemExit(main())
