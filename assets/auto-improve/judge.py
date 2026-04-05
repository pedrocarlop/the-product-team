#!/usr/bin/env python3
import sys
import re
import json
import argparse
from pathlib import Path


# ---------------------------------------------------------------------------
# Common checks (applied to all artifact types)
# ---------------------------------------------------------------------------

def check_common(content: str) -> list:
    """Checks applied regardless of scenario type. Returns list of (name, passed, weight) tuples."""
    checks = []

    # YAML frontmatter
    has_yaml = content.strip().startswith("---") and "\n---" in content[4:]
    checks.append(("yaml_frontmatter", has_yaml, 0.05))

    # ## Reflection section
    has_reflection = bool(re.search(r"^##\s+Reflection", content, re.MULTILINE | re.IGNORECASE))
    checks.append(("reflection_section", has_reflection, 0.05))

    # Evidence labeling (sourced / fallback / inferred markers)
    evidence_labels = re.findall(
        r"\b(sourced|fallback|inferred)\b", content, re.IGNORECASE
    )
    has_evidence_labels = len(evidence_labels) >= 1
    checks.append(("evidence_labeling", has_evidence_labels, 0.05))

    # Coverage map (any markdown table or explicit "coverage" heading)
    has_coverage = bool(
        re.search(r"^##\s+Coverage", content, re.MULTILINE | re.IGNORECASE)
        or re.search(r"\|.*\|.*\|", content)
    )
    checks.append(("coverage_map", has_coverage, 0.05))

    return checks


# ---------------------------------------------------------------------------
# Rubric-based scoring
# ---------------------------------------------------------------------------

def judge_rubric(artifact_path: Path, rubric_path: Path) -> dict:
    """Score an artifact against a rubric.json file.

    rubric.json schema:
    {
      "checks": [
        {"name": "...", "pattern": "regex", "weight": 0.2, "description": "..."},
        {"name": "...", "section": "## Section Name", "weight": 0.15},
        {"name": "...", "min_words": 200, "weight": 0.1}
      ],
      "pass_threshold": 0.7
    }
    """
    if not artifact_path.exists():
        return {"score": 0.0, "reason": "Artifact not found", "passed": False, "mode": "rubric"}

    content = artifact_path.read_text()

    with open(rubric_path) as f:
        rubric = json.load(f)

    checks = rubric.get("checks", [])
    pass_threshold = rubric.get("pass_threshold", 0.7)

    total_weight = sum(c.get("weight", 0.1) for c in checks)
    earned = 0.0
    reasons = []

    for check in checks:
        name = check.get("name", "unnamed")
        weight = check.get("weight", 0.1)
        passed = False

        if "pattern" in check:
            passed = bool(re.search(check["pattern"], content, re.IGNORECASE | re.MULTILINE))
        elif "section" in check:
            section_heading = check["section"]
            passed = section_heading.lower() in content.lower()
        elif "min_words" in check:
            passed = len(content.split()) >= check["min_words"]
        elif "contains" in check:
            passed = check["contains"].lower() in content.lower()

        if passed:
            earned += weight
            reasons.append(f"PASS: {name} ({check.get('description', '')})")
        else:
            reasons.append(f"FAIL: {name} ({check.get('description', '')})")

    # Add common checks
    common = check_common(content)
    common_weight = sum(w for _, _, w in common)
    total_weight += common_weight
    for name, passed, weight in common:
        if passed:
            earned += weight
            reasons.append(f"PASS: [common] {name}")
        else:
            reasons.append(f"FAIL: [common] {name}")

    score = round(earned / total_weight, 2) if total_weight > 0 else 0.0

    return {
        "score": score,
        "total": 1.0,
        "reasons": reasons,
        "passed": score >= pass_threshold,
        "mode": "rubric",
    }


# ---------------------------------------------------------------------------
# Improved deterministic scoring (fallback when no rubric exists)
# ---------------------------------------------------------------------------

def judge_deterministic(artifact_path: Path, scenario_type: str) -> dict:
    if not artifact_path.exists():
        return {"score": 0.0, "reason": "Artifact not found", "passed": False, "mode": "deterministic"}

    content = artifact_path.read_text()
    score = 0.0
    reasons = []

    if scenario_type == "design":
        # YAML header
        if content.strip().startswith("---"):
            score += 0.1
            reasons.append("PASS: YAML frontmatter present.")
        else:
            reasons.append("FAIL: No YAML frontmatter.")

        # ## sections structure (at least 3 heading-2 sections)
        h2_sections = re.findall(r"^##\s+.+", content, re.MULTILINE)
        if len(h2_sections) >= 3:
            score += 0.15
            reasons.append(f"PASS: Found {len(h2_sections)} ## sections.")
        else:
            reasons.append(f"FAIL: Only {len(h2_sections)} ## sections (need >= 3).")

        # Color token definitions (HSL, RGB, hex with semantic names, or token patterns)
        color_tokens = re.findall(
            r"(hsl\(|rgb\(|#[0-9a-fA-F]{3,8}\b|--[\w-]+-color|color[-_][\w-]+)",
            content, re.IGNORECASE
        )
        if color_tokens:
            score += 0.2
            reasons.append(f"PASS: Found {len(color_tokens)} color token references.")
        else:
            reasons.append("FAIL: No color token definitions found.")

        # Component breakdown (## Component or component-related subsections)
        if re.search(r"##\s+Component", content, re.IGNORECASE):
            score += 0.2
            reasons.append("PASS: Component breakdown found.")
        else:
            reasons.append("FAIL: No component breakdown section.")

        # Reflection section
        if re.search(r"^##\s+Reflection", content, re.MULTILINE | re.IGNORECASE):
            score += 0.1
            reasons.append("PASS: Reflection section present.")
        else:
            reasons.append("FAIL: No reflection section.")

        # Typography specification (any font family mention or typography heading)
        if re.search(r"(font[-_]?family|typeface|typography|Inter|Roboto|Outfit|sans-serif)", content, re.IGNORECASE):
            score += 0.15
            reasons.append("PASS: Typography specified.")
        else:
            reasons.append("FAIL: No typography specification.")

        # Sufficient depth (word count)
        if len(content.split()) >= 200:
            score += 0.1
            reasons.append("PASS: Sufficient content depth.")
        else:
            reasons.append("FAIL: Content too shallow (< 200 words).")

    elif scenario_type == "engineering":
        # Proper code structure (function/class/component definition)
        if re.search(r"(export\s+(default\s+)?|function\s+|const\s+\w+\s*=|class\s+\w+)", content):
            score += 0.15
            reasons.append("PASS: Code structure with exports/definitions.")
        else:
            reasons.append("FAIL: No proper code structure found.")

        # Imports
        if re.search(r"(import\s+.+from|require\()", content):
            score += 0.15
            reasons.append("PASS: Import statements present.")
        else:
            reasons.append("FAIL: No import statements.")

        # Component patterns (JSX return, render method, or template)
        if re.search(r"(return\s*\(|render\s*\(|<template>)", content):
            score += 0.2
            reasons.append("PASS: Component rendering pattern found.")
        else:
            reasons.append("FAIL: No component rendering pattern.")

        # Type annotations or PropTypes
        if re.search(r"(:\s*(string|number|boolean|React\.|Props|interface\s|type\s)|PropTypes)", content):
            score += 0.1
            reasons.append("PASS: Type annotations found.")
        else:
            reasons.append("FAIL: No type annotations.")

        # Styling approach (Tailwind classes, CSS modules, styled-components)
        if re.search(r"(className=|backdrop-blur|bg-|styled\.|css\`|\.module\.)", content):
            score += 0.15
            reasons.append("PASS: Styling approach present.")
        else:
            reasons.append("FAIL: No styling approach detected.")

        # Error handling or edge cases
        if re.search(r"(catch\s*\(|\.catch|try\s*\{|fallback|error|loading|empty)", content, re.IGNORECASE):
            score += 0.1
            reasons.append("PASS: Error/edge case handling.")
        else:
            reasons.append("FAIL: No error handling detected.")

        # Sufficient implementation depth
        if len(content.split("\n")) >= 30:
            score += 0.15
            reasons.append("PASS: Sufficient implementation depth.")
        else:
            reasons.append("FAIL: Implementation too shallow (< 30 lines).")

    elif scenario_type == "business":
        # Required sections check
        required_sections = [
            "Problem Statement", "Success Metrics", "User Stories",
            "Requirements", "Constraints"
        ]
        found_sections = [s for s in required_sections if s.lower() in content.lower()]
        section_ratio = len(found_sections) / len(required_sections)
        score += section_ratio * 0.25
        reasons.append(f"{'PASS' if section_ratio >= 0.6 else 'FAIL'}: Found {len(found_sections)}/{len(required_sections)} required sections.")

        # Evidence citations (references, data points, or sourced claims)
        citations = re.findall(
            r"(\[\d+\]|\(source:|\bcited?\b|according to|research shows|data indicates|sourced|evidence)",
            content, re.IGNORECASE
        )
        if citations:
            score += 0.15
            reasons.append(f"PASS: {len(citations)} evidence citations found.")
        else:
            reasons.append("FAIL: No evidence citations.")

        # Measurable metrics (numbers, percentages, KPIs)
        metrics = re.findall(r"(\d+%|\bKPI\b|\bOKR\b|\bmetric\b|measurable|baseline|target)", content, re.IGNORECASE)
        if len(metrics) >= 2:
            score += 0.2
            reasons.append(f"PASS: {len(metrics)} measurable metric references.")
        else:
            reasons.append(f"FAIL: Only {len(metrics)} metric references (need >= 2).")

        # Structured format (uses headings, lists, tables)
        has_structure = (
            len(re.findall(r"^##\s+", content, re.MULTILINE)) >= 3
            and (re.search(r"^[-*]\s+", content, re.MULTILINE) or re.search(r"^\d+\.\s+", content, re.MULTILINE))
        )
        if has_structure:
            score += 0.15
            reasons.append("PASS: Well-structured format (headings + lists).")
        else:
            reasons.append("FAIL: Insufficient document structure.")

        # Content depth
        word_count = len(content.split())
        if word_count >= 300:
            score += 0.15
            reasons.append(f"PASS: Good content depth ({word_count} words).")
        else:
            reasons.append(f"FAIL: Content too shallow ({word_count} words, need >= 300).")

        # Actionability (acceptance criteria, action items, next steps)
        if re.search(r"(acceptance criteria|action item|next step|deliverable|timeline|milestone)", content, re.IGNORECASE):
            score += 0.1
            reasons.append("PASS: Actionable elements present.")
        else:
            reasons.append("FAIL: No actionable elements (acceptance criteria, action items, etc.).")

    score = min(round(score, 2), 1.0)

    return {
        "score": score,
        "total": 1.0,
        "reasons": reasons,
        "passed": score >= 0.7,
        "mode": "deterministic",
    }


# ---------------------------------------------------------------------------
# LLM judge path
# ---------------------------------------------------------------------------

def judge_llm(artifact_path: Path, scenario_type: str, instruction: str,
              llm_response_path: Path = None) -> dict:
    """LLM-as-judge scoring.

    If --llm-response is provided, parse the JSON file and return structured result.
    Otherwise, print the prompt for the LLM and return pending status.
    """
    if not artifact_path.exists():
        return {"score": 0.0, "reason": "Artifact not found", "passed": False, "mode": "llm"}

    # If an LLM response file is provided, parse it and return the result
    if llm_response_path is not None:
        if not llm_response_path.exists():
            return {"error": f"LLM response file not found: {llm_response_path}", "mode": "llm"}

        try:
            with open(llm_response_path) as f:
                llm_data = json.load(f)

            llm_score = float(llm_data.get("score", 0.0))
            llm_reasoning = llm_data.get("reasoning", "No reasoning provided.")
            llm_verdict = llm_data.get("verdict", "fail")

            return {
                "score": round(llm_score, 2),
                "total": 1.0,
                "reasons": [llm_reasoning],
                "passed": llm_verdict.lower() == "pass",
                "mode": "llm",
                "llm_verdict": llm_verdict,
            }
        except (json.JSONDecodeError, ValueError) as e:
            return {"error": f"Failed to parse LLM response: {e}", "mode": "llm"}

    # No response file -- generate the prompt for human/LLM evaluation
    content = artifact_path.read_text()

    prompt = f"""
### LLM JUDGE REQUEST ###
Scenario Category: {scenario_type}
Original Task: {instruction}

Deliverable Content:
---
{content}
---

Evaluation Rubric:
1. **Fidelity**: Does the output match the aesthetic and technical bar (premium, high-quality)?
2. **Clarity**: Is the output readable and actionable for the next agent/person in the chain?
3. **Completeness**: Are all requirements from the instruction met?

Output Format:
JSON with keys: "score" (0.0-1.0), "reasoning" (detailed), and "verdict" (pass/fail).
##########################
"""
    print(prompt)

    return {
        "status": "pending_llm_score",
        "prompt": prompt,
        "mode": "llm",
    }


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Judge an artifact produced by a benchmark run."
    )
    parser.add_argument("artifact_path", type=str, help="Path to the artifact file to judge")
    parser.add_argument(
        "--mode",
        choices=["deterministic", "llm", "rubric"],
        default="deterministic",
        help="Scoring mode (default: deterministic)",
    )
    parser.add_argument(
        "--type",
        choices=["design", "engineering", "business"],
        default="design",
        help="Scenario type for deterministic scoring",
    )
    parser.add_argument(
        "--instruction",
        type=str,
        help="Instruction text for LLM judge mode",
    )
    parser.add_argument(
        "--rubric",
        type=str,
        default=None,
        help="Path to a rubric.json file for rubric-based scoring",
    )
    parser.add_argument(
        "--llm-response",
        type=str,
        default=None,
        help="Path to a JSON file containing the LLM judge's score/reasoning",
    )
    args = parser.parse_args()

    path = Path(args.artifact_path)

    if args.mode == "rubric":
        rubric_path = Path(args.rubric) if args.rubric else None
        if rubric_path is None:
            # Try to find rubric.json next to the artifact
            candidate = path.parent / "rubric.json"
            if candidate.exists():
                rubric_path = candidate
        if rubric_path is None or not rubric_path.exists():
            print("ERROR: Rubric mode requires a rubric.json file. "
                  "Use --rubric <path> or place rubric.json next to the artifact.",
                  file=sys.stderr)
            sys.exit(1)
        result = judge_rubric(path, rubric_path)
    elif args.mode == "llm":
        llm_resp = Path(args.llm_response) if args.llm_response else None
        result = judge_llm(path, args.type, args.instruction or "", llm_resp)
    else:
        # Deterministic mode: check for rubric.json in scenario dir as optional upgrade
        result = judge_deterministic(path, args.type)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
