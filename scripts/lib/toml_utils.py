"""Shared TOML loading and role discovery utilities for Product Team scripts."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


DISCIPLINE_ORDER = ("business", "design", "engineer", "review")
DISCIPLINE_LABELS = {
    "business": "Business Roles",
    "design": "Design Roles",
    "engineer": "Engineering Roles",
    "review": "Review Roles",
}
EXCLUDED_ROLES = {"orchestrator", "reference"}
MANAGED_ROLE_TOMLS = (
    Path("agents/orchestrator/orchestrator/orchestrator.toml"),
    Path("agents/business/product-lead/product-lead.toml"),
    Path("agents/business/analyst/analyst.toml"),
    Path("agents/business/go-to-market/go-to-market.toml"),
    Path("agents/business/business-ops/business-ops.toml"),
    Path("agents/design/ux-researcher/ux-researcher.toml"),
    Path("agents/design/product-designer/product-designer.toml"),
    Path("agents/design/ui-designer/ui-designer.toml"),
    Path("agents/design/content-designer/content-designer.toml"),
    Path("agents/design/design-systems-designer/design-systems-designer.toml"),
    Path("agents/engineer/frontend-engineer/frontend-engineer.toml"),
    Path("agents/engineer/backend-engineer/backend-engineer.toml"),
    Path("agents/engineer/platform-engineer/platform-engineer.toml"),
    Path("agents/review/design-reviewer/design-reviewer.toml"),
    Path("agents/review/qa-reviewer/qa-reviewer.toml"),
    Path("agents/engineer/reference/reference.toml"),
)


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
    repo_write_policy: str


def discover_toml_paths(root: Path) -> list[Path]:
    """Discover the Product Team managed role TOML files under agents/."""
    return [root / relative_path for relative_path in MANAGED_ROLE_TOMLS]


def load_roles(root: Path) -> list[RoleEntry]:
    """Load all specialist roles (excluding orchestrator and reference) as RoleEntry objects."""
    roles: list[RoleEntry] = []
    managed_by_discipline = {discipline: [] for discipline in DISCIPLINE_ORDER}

    for path in discover_toml_paths(root):
        discipline = path.parent.parent.name
        if discipline not in managed_by_discipline:
            continue
        managed_by_discipline[discipline].append(path)

    for discipline in DISCIPLINE_ORDER:
        for path in managed_by_discipline[discipline]:
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
                    repo_write_policy=data["execution_policy"].get("repo_write_policy", "never"),
                )
            )

    return roles
