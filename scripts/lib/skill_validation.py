"""Shared skill validation helpers for Product Team scripts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


KNOWN_MCP_SERVERS = {
    "figma",
    "chrome_devtools",
    "notion",
    "linear",
    "slack",
    "github",
    "paper",
    "stitch",
    "refero",
    "google_forms",
}

BANNED_SKILL_NAMES = {
    "apply-patch",
    "search-query",
    "chrome-click",
    "chrome-lighthouse-audit",
    "chrome-list-console-messages",
    "chrome-list-network-requests",
    "chrome-navigate-page",
    "chrome-take-snapshot",
    "figma-get-design-context",
    "figma-get-screenshot",
    "image-query",
}

REQUIRED_SKILL_FIELDS = {
    "name",
    "description",
    "trigger",
    "primary_mcp",
    "fallback_tools",
    "best_guess_output",
    "output_artifacts",
    "done_when",
}

APPROVED_VIRTUAL_ALIASES = {
    "repository",
    "deliverables",
    "logs",
    "context",
    "timeline",
    "subagents",
    "role metadata",
    "conversation context",
    "named source systems",
    "repository review",
    "context review",
    "role-catalog review",
}


@dataclass(frozen=True)
class SkillValidationContext:
    discipline: str
    role_name: str
    mcp_servers: tuple[str, ...]
    web_tools: tuple[str, ...]
    skill_files: tuple[Path, ...]


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    body = text.split("---\n", 2)[1]
    fields: dict[str, str] = {}
    for line in body.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def split_tokens(value: str) -> list[str]:
    return [token.strip() for token in value.split(",") if token.strip()]


def expected_section_anchor(skill_name: str) -> str:
    return f"## Skill: {skill_name}"


def discover_skill_references(contexts: list[SkillValidationContext]) -> set[str]:
    references: set[str] = set()
    for context in contexts:
        for skill_path in context.skill_files:
            references.add(f"{context.role_name}/{skill_path.stem}")
    return references


def allowed_tool_tokens(context: SkillValidationContext, skill_references: set[str]) -> set[str]:
    return (
        set(context.mcp_servers)
        | set(context.web_tools)
        | APPROVED_VIRTUAL_ALIASES
        | skill_references
    )


def validate_tool_field(
    *,
    context: SkillValidationContext,
    skill_path: Path,
    field_name: str,
    field_value: str,
    skill_references: set[str],
    failures: list[str],
) -> None:
    tokens = split_tokens(field_value)
    if not tokens:
        failures.append(f"{context.role_name}: {skill_path.name} has an empty {field_name} field.")
        return

    allowed = allowed_tool_tokens(context, skill_references)
    for token in tokens:
        if token not in allowed:
            failures.append(
                f"{context.role_name}: {skill_path.name} uses unsupported {field_name} token '{token}'."
            )


def validate_design_contract(
    *,
    context: SkillValidationContext,
    skill_path: Path,
    fields: dict[str, str],
    text: str,
    failures: list[str],
) -> None:
    section_anchor = fields.get("section_anchor")
    expected_anchor = expected_section_anchor(skill_path.stem)
    if section_anchor != expected_anchor:
        failures.append(
            f"{context.role_name}: {skill_path.name} must declare section_anchor '{expected_anchor}'."
        )

    required_snippets = (
        "## Shared Deliverable Contract",
        "## Required Deliverable Sections",
        "## Reflection",
        "What worked",
        "What didn't",
        "Next steps",
    )
    for snippet in required_snippets:
        if snippet not in text:
            failures.append(
                f"{context.role_name}: {skill_path.name} is missing required design contract text '{snippet}'."
            )

    if context.role_name != "ui-designer":
        return

    if skill_path.stem == "ui-concept-direction":
        for snippet in (
            "### Direction 1",
            "### Direction 2",
            "### Direction 3",
            "Divergence axes",
            "Why this is materially different",
            "3 meaningfully different high-level directions",
            "at least 3 axes chosen from",
        ):
            if snippet not in text:
                failures.append(f"{context.role_name}: {skill_path.name} is missing '{snippet}'.")

    if skill_path.stem == "ui-variant-exploration":
        for snippet in (
            "### Variant comparison",
            "Core idea",
            "Divergence axes",
            "Strengths",
            "Weaknesses",
            "Risks",
            "Best use case",
            "Why not chosen",
            "### Winning direction",
            "### Similarity check",
            "one recommendation",
        ):
            if snippet not in text:
                failures.append(f"{context.role_name}: {skill_path.name} is missing '{snippet}'.")

    if skill_path.stem == "screen-production-design":
        for snippet in (
            "### Assignment type",
            "### Chosen direction",
            "### Inherited principles",
            "### Non-goals",
            "new design",
            "If no upstream direction exists",
        ):
            if snippet not in text:
                failures.append(f"{context.role_name}: {skill_path.name} is missing '{snippet}'.")


def validate_design_anchor_uniqueness(
    context: SkillValidationContext,
    skill_fields: dict[Path, dict[str, str]],
    failures: list[str],
) -> None:
    artifact_to_anchors: dict[str, dict[str, Path]] = {}
    for skill_path, fields in skill_fields.items():
        artifact = fields.get("output_artifacts", "")
        anchor = fields.get("section_anchor", "")
        if not artifact:
            continue
        artifact_anchors = artifact_to_anchors.setdefault(artifact, {})
        if anchor in artifact_anchors:
            failures.append(
                f"{context.role_name}: {skill_path.name} duplicates section_anchor '{anchor}' "
                f"for shared artifact '{artifact}'."
            )
            continue
        artifact_anchors[anchor] = skill_path


BUSINESS_SKILL_REQUIRED_SNIPPETS = {
    "product-lead": {
        "frame-problem": (
            "### Problem statement",
            "### Objective and success criteria",
            "### Constraints and non-goals",
            "### Decision frame",
            "### Open questions",
        ),
        "write-prd": (
            "### Objective",
            "### Scope",
            "### Non-goals",
            "### Key scenarios",
            "### Requirements and decisions",
            "### Acceptance criteria",
            "### Dependencies and risks",
            "### Open questions",
        ),
        "prioritize-roadmap": (
            "### Candidate bets",
            "### Prioritization criteria",
            "### Scoring or ranking table",
            "### Sequencing dependencies",
            "### Recommendation",
            "### Tradeoffs and deferrals",
        ),
        "experiment-brief": (
            "### Hypothesis",
            "### Audience and scope",
            "### Primary metric",
            "### Guardrails",
            "### Decision rules",
            "### Rollout or instrumentation notes",
            "### Risks",
        ),
        "stakeholder-memo": (
            "### Audience and purpose",
            "### Recommendation",
            "### Why now",
            "### Evidence",
            "### Risks and tradeoffs",
            "### Asks or decisions needed",
            "### Next steps",
        ),
    },
    "analyst": {
        "metric-definition": (
            "### Metric name and purpose",
            "### Formula",
            "### Segments and cuts",
            "### Source of truth",
            "### Caveats",
            "### Instrumentation gaps",
        ),
        "funnel-analysis": (
            "### Funnel stages",
            "### Stage performance",
            "### Largest drop-offs",
            "### Likely causes",
            "### Recommended actions",
            "### Data quality caveats",
        ),
        "forecast-model": (
            "### Forecast question",
            "### Assumptions",
            "### Driver model",
            "### Base/upside/downside scenarios",
            "### Sensitivity analysis",
            "### Decision implication",
        ),
        "experiment-readout": (
            "### Experiment setup",
            "### Observed results",
            "### Metric impact",
            "### Confidence and validity",
            "### Decision",
            "### Recommended follow-up",
        ),
        "dashboard-story": (
            "### Executive summary",
            "### Key metrics",
            "### Important changes",
            "### What matters",
            "### Recommended actions",
            "### Watch list",
        ),
    },
    "go-to-market": {
        "positioning-brief": (
            "### Target audience",
            "### Problem and alternatives",
            "### Differentiated promise",
            "### Message pillars",
            "### Proof points",
            "### Objections and caveats",
            "### Reuse guidance",
        ),
        "launch-plan": (
            "### Launch scope",
            "### Milestones and gates",
            "### Owners",
            "### Dependencies",
            "### Readiness checklist",
            "### Risks and blockers",
            "### Open decisions",
        ),
        "campaign-brief": (
            "### Objective",
            "### Audience",
            "### Core message",
            "### Channels",
            "### Creative direction",
            "### KPI and measurement",
            "### Dependencies",
        ),
        "sales-enablement": (
            "### Core pitch",
            "### Ideal use cases",
            "### Proof points",
            "### Objection-handling matrix",
            "### Qualification cues",
            "### Escalation notes",
        ),
        "partner-thesis": (
            "### Partnership goal",
            "### Target partner types",
            "### Why each matters",
            "### Value exchange",
            "### Operating model",
            "### Selection risks",
            "### Next steps",
        ),
        "customer-signal-synthesis": (
            "### Sources reviewed",
            "### Recurring themes",
            "### Signal strength",
            "### Customer impact",
            "### GTM implications",
            "### Recommended actions",
            "### Unknowns",
        ),
    },
    "business-ops": {
        "process-map": (
            "### Current-state flow",
            "### Target-state flow",
            "### Owners and handoffs",
            "### Bottlenecks",
            "### Gaps",
            "### Recommended changes",
        ),
        "operating-rhythm": (
            "### Cadence table",
            "### Purpose of each ceremony",
            "### Inputs and outputs",
            "### Decision rights",
            "### Escalation path",
            "### Risks",
        ),
        "workflow-design": (
            "### Trigger",
            "### Roles and responsibilities",
            "### Workflow steps",
            "### Artifacts and systems",
            "### Failure modes",
            "### Adoption notes",
        ),
        "tooling-audit": (
            "### Tool inventory",
            "### Current owner",
            "### Keep/change/remove recommendation",
            "### Gap analysis",
            "### Integration issues",
            "### Recommended roadmap",
        ),
        "execution-tracker": (
            "### Tracking model",
            "### Required fields",
            "### Status definitions",
            "### Owner and escalation rules",
            "### Update cadence",
            "### Reporting views",
        ),
    },
}


def validate_business_contract(
    *,
    context: SkillValidationContext,
    skill_path: Path,
    fields: dict[str, str],
    text: str,
    failures: list[str],
) -> None:
    section_anchor = fields.get("section_anchor")
    expected_anchor = expected_section_anchor(skill_path.stem)
    if section_anchor != expected_anchor:
        failures.append(
            f"{context.role_name}: {skill_path.name} must declare section_anchor '{expected_anchor}'."
        )

    required_snippets = (
        "## Shared Deliverable Contract",
        "## Required Deliverable Sections",
        "## Tool Path",
        "## Workflow Notes",
        "## Output Contract",
        "## Reflection",
        "Update only the section named by `section_anchor`.",
        "Update the role-level reflection footer by appending or refreshing",
        "Within `## Skill:",
        "Keep all work for this skill inside",
    )
    for snippet in required_snippets:
        if snippet not in text:
            failures.append(
                f"{context.role_name}: {skill_path.name} is missing required business contract text '{snippet}'."
            )

    role_snippets = BUSINESS_SKILL_REQUIRED_SNIPPETS.get(context.role_name, {})
    for snippet in role_snippets.get(skill_path.stem, ()):
        if snippet not in text:
            failures.append(f"{context.role_name}: {skill_path.name} is missing '{snippet}'.")


ENGINEER_SKILL_REQUIRED_SNIPPETS = {
    "frontend-engineer": {
        "implement-from-design": (
            "### Design target",
            "### Implementation scope",
            "### State coverage",
            "### Interaction notes",
            "### Code touchpoints",
            "### Open implementation risks",
        ),
        "stateful-ui-build": (
            "### Surface and state model",
            "### Loading state",
            "### Error and recovery state",
            "### Empty state",
            "### Interactive transitions",
            "### Verification notes",
        ),
        "responsive-refinement": (
            "### Target breakpoints",
            "### Current issues",
            "### Responsive adjustments",
            "### State-specific behavior",
            "### Risks and regressions",
            "### Verification plan",
        ),
        "component-implementation": (
            "### Component purpose",
            "### API or props",
            "### Variants and states",
            "### Composition and reuse constraints",
            "### Code touchpoints",
            "### Adoption notes",
        ),
        "browser-debug": (
            "### Observed issue",
            "### Reproduction steps",
            "### Browser evidence",
            "### Suspected source of truth",
            "### Fix direction",
            "### Open unknowns",
        ),
        "frontend-verify": (
            "### Verification scope",
            "### Behavior checks",
            "### Layout and responsive checks",
            "### Accessibility or quality checks",
            "### Findings",
            "### Residual risk",
        ),
    },
    "backend-engineer": {
        "api-implementation": (
            "### API surface",
            "### Inputs and outputs",
            "### Behavior and invariants",
            "### Error handling",
            "### Code touchpoints",
            "### Rollout or compatibility notes",
        ),
        "domain-model-build": (
            "### Domain entities or concepts",
            "### Core rules",
            "### State transitions",
            "### Data transformations",
            "### Code touchpoints",
            "### Open risks",
        ),
        "integration-flow-build": (
            "### Systems involved",
            "### Trigger and flow",
            "### Payload or contract boundaries",
            "### Failure handling",
            "### Observability needs",
            "### Rollout notes",
        ),
        "backend-observability": (
            "### Coverage goal",
            "### Signals to add or refine",
            "### Where instrumentation lands",
            "### Alerting or debugging use",
            "### Risk or cost tradeoffs",
            "### Verification notes",
        ),
        "backend-verify": (
            "### Verification scope",
            "### Contract checks",
            "### Failure-path checks",
            "### Operational checks",
            "### Findings",
            "### Residual risk",
        ),
    },
    "platform-engineer": {
        "schema-migration": (
            "### Schema change summary",
            "### Migration steps",
            "### Compatibility window",
            "### Rollback plan",
            "### Operational risks",
            "### Verification plan",
        ),
        "pipeline-orchestration": (
            "### Pipeline scope",
            "### Execution sequence",
            "### Retry and failure policy",
            "### Ownership and handoffs",
            "### Observability",
            "### Open risks",
        ),
        "infra-release": (
            "### Release scope",
            "### Preconditions",
            "### Execution plan",
            "### Rollback posture",
            "### Operational safeguards",
            "### Verification and follow-up",
        ),
        "performance-investigation": (
            "### Performance symptom",
            "### Measurement or evidence",
            "### Bottleneck hypothesis",
            "### Localization findings",
            "### Recommended next step",
            "### Confidence and unknowns",
        ),
        "security-hardening": (
            "### Threat or weakness",
            "### Affected surface",
            "### Hardening change",
            "### Residual risk",
            "### Operational impact",
            "### Verification notes",
        ),
        "ci-cd-governance": (
            "### Governance goal",
            "### Current gaps",
            "### Proposed gates or rules",
            "### Enforcement points",
            "### Exception path",
            "### Adoption risks",
        ),
    },
    "reference": {
        "ground": (
            "### Question being grounded",
            "### Sources checked",
            "### Confirmed facts",
            "### Unknowns",
            "### Implications for downstream roles",
        ),
        "reuse": (
            "### Target problem",
            "### Reusable candidates",
            "### Preferred pattern",
            "### Why chosen",
            "### Exact files or artifacts to follow",
            "### Caveats",
        ),
        "trace": (
            "### Entry point",
            "### Trace path",
            "### Source of truth",
            "### Ownership boundary",
            "### Downstream action",
        ),
        "verify": (
            "### Claim under review",
            "### Evidence checked",
            "### Pass/fail/unresolved result",
            "### Contradictions or gaps",
            "### Recommended follow-up",
        ),
    },
}


def validate_engineer_contract(
    *,
    context: SkillValidationContext,
    skill_path: Path,
    fields: dict[str, str],
    text: str,
    failures: list[str],
) -> None:
    section_anchor = fields.get("section_anchor")
    expected_anchor = expected_section_anchor(skill_path.stem)
    if section_anchor != expected_anchor:
        failures.append(
            f"{context.role_name}: {skill_path.name} must declare section_anchor '{expected_anchor}'."
        )

    required_snippets = (
        "## Shared Deliverable Contract",
        "## Required Deliverable Sections",
        "## Tool Path",
        "## Workflow Notes",
        "## Output Contract",
        "## Reflection",
        "Update only the section named by `section_anchor`.",
        "Update the role-level reflection footer by appending or refreshing",
        "Within `## Skill:",
        "Keep all work for this skill inside",
    )
    for snippet in required_snippets:
        if snippet not in text:
            failures.append(
                f"{context.role_name}: {skill_path.name} is missing required engineering contract text '{snippet}'."
            )

    role_snippets = ENGINEER_SKILL_REQUIRED_SNIPPETS.get(context.role_name, {})
    for snippet in role_snippets.get(skill_path.stem, ()):
        if snippet not in text:
            failures.append(f"{context.role_name}: {skill_path.name} is missing '{snippet}'.")


def validate_skill_contexts(
    contexts: list[SkillValidationContext],
    failures: list[str],
    *,
    enforce_banned_names: bool,
) -> None:
    skill_references = discover_skill_references(contexts)

    for context in contexts:
        skill_fields: dict[Path, dict[str, str]] = {}

        for skill_path in context.skill_files:
            fields = parse_front_matter(skill_path)
            text = skill_path.read_text(encoding="utf-8")
            missing = REQUIRED_SKILL_FIELDS - set(fields)
            if missing:
                failures.append(
                    f"{context.role_name}: {skill_path.name} missing fields: {', '.join(sorted(missing))}."
                )
            if enforce_banned_names and skill_path.stem in BANNED_SKILL_NAMES:
                failures.append(
                    f"{context.role_name}: banned thin-wrapper skill remains: {skill_path.name}."
                )

            skill_fields[skill_path] = fields

            primary_mcp = fields.get("primary_mcp")
            if primary_mcp:
                validate_tool_field(
                    context=context,
                    skill_path=skill_path,
                    field_name="primary_mcp",
                    field_value=primary_mcp,
                    skill_references=skill_references,
                    failures=failures,
                )

            fallback_tools = fields.get("fallback_tools")
            if fallback_tools:
                validate_tool_field(
                    context=context,
                    skill_path=skill_path,
                    field_name="fallback_tools",
                    field_value=fallback_tools,
                    skill_references=skill_references,
                    failures=failures,
                )

            if context.discipline == "design":
                validate_design_contract(
                    context=context,
                    skill_path=skill_path,
                    fields=fields,
                    text=text,
                    failures=failures,
                )
            elif context.discipline == "business":
                validate_business_contract(
                    context=context,
                    skill_path=skill_path,
                    fields=fields,
                    text=text,
                    failures=failures,
                )
            elif context.discipline == "engineer":
                validate_engineer_contract(
                    context=context,
                    skill_path=skill_path,
                    fields=fields,
                    text=text,
                    failures=failures,
                )

        if context.discipline == "design":
            validate_design_anchor_uniqueness(context, skill_fields, failures)
        elif context.discipline == "business":
            validate_design_anchor_uniqueness(context, skill_fields, failures)
        elif context.discipline == "engineer":
            validate_design_anchor_uniqueness(context, skill_fields, failures)
