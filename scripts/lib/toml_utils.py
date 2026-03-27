"""Shared TOML loading and role discovery utilities for Product Team scripts."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


DISCIPLINE_ORDER = ("business", "design", "engineer")
DISCIPLINE_LABELS = {
    "business": "Business Roles",
    "design": "Design Roles",
    "engineer": "Engineering Roles",
}
EXCLUDED_ROLES = {"orchestrator", "reference"}


def load_toml(path: Path) -> dict:
    """Load and parse a TOML file."""
    return tomllib.loads(path.read_text(encoding="utf-8"))


@dataclass(frozen=True)
class RoleEntry:
    discipline: str
    name: str
    display_name: str
    description: str
    owns: tuple[str, ...]
    role_kind: str


def load_roles(root: Path) -> list[RoleEntry]:
    """Load all specialist roles (excluding orchestrator and reference) as RoleEntry objects."""
    roles: list[RoleEntry] = []

    for discipline in DISCIPLINE_ORDER:
        for path in sorted((root / "agents" / discipline).glob("*/*.toml")):
            data = load_toml(path)
            role_name = data["name"]
            if role_name in EXCLUDED_ROLES:
                continue

            roles.append(
                RoleEntry(
                    discipline=discipline,
                    name=role_name,
                    display_name=data["display_name"],
                    description=data["description"].strip().rstrip("."),
                    owns=tuple(data["role_boundary"]["owns"]),
                    role_kind=data["execution_policy"]["role_kind"],
                )
            )

    return roles


def discover_toml_paths(root: Path) -> list[Path]:
    """Discover all role TOML files under agents/."""
    return sorted((root / "agents").glob("*/*/*.toml"))
