#!/usr/bin/env python3
import sys
import re
import json
import argparse
from pathlib import Path

def judge_deterministic(artifact_path: Path, scenario_type: str):
    if not artifact_path.exists():
        return {"score": 0.0, "reason": "Artifact not found", "passed": False}

    content = artifact_path.read_text()
    score = 0.0
    reasons = []

    if scenario_type == "design":
        # HSL Check
        # Matches both legacy comma syntax and modern space syntax: hsl(220, 100%, 50%) or hsl(220 100% 50%)
        hsl_matches = re.findall(r"hsl\(\s*\d+(?:\s*,\s*|\s+)\d+%(?:\s*,\s*|\s+)\d+%\s*(?:/\s*[\d.]+%?)?\s*\)", content, re.IGNORECASE)
        if hsl_matches:
            score += 0.3
            reasons.append("Found HSL color definitions.")
        # Typography
        if any(f in content for f in ["Inter", "Roboto", "Outfit"]):
            score += 0.2
            reasons.append("Modern typography specified.")
        # Aesthetics
        if "glass" in content.lower() or "gradient" in content.lower():
            score += 0.2
            reasons.append("Premium aesthetics (glass/gradient) included.")
        # Components
        if "## Component" in content:
            score += 0.3
            reasons.append("Component breakdown found.")

    elif scenario_type == "engineering":
        # Code Syntax (React/TSX)
        if "export default" in content or "const" in content:
            score += 0.2
            reasons.append("Valid React component structure.")
        # Lucide Icons
        if "lucide-react" in content:
            score += 0.2
            reasons.append("Using lucide-react icons.")
        # Tailwind / Glassmorphism
        if "backdrop-blur" in content or "bg-" in content:
            score += 0.3
            reasons.append("Tailwind CSS with glassmorphic classes.")
        # Functional implementation
        if "return (" in content:
            score += 0.3
            reasons.append("Functional component with JSX return.")

    elif scenario_type == "business":
        # PRD Structure
        required_sections = ["Problem Statement", "Success Metrics", "User Stories"]
        found_sections = [s for s in required_sections if s.lower() in content.lower()]
        score += (len(found_sections) / len(required_sections)) * 0.5
        reasons.append(f"Found {len(found_sections)}/{len(required_sections)} required sections.")
        # Complexity/Ambiguity
        if len(content.split()) > 300:
            score += 0.3
            reasons.append("High requirement density (word count > 300).")
        # KPI checks
        if "KPI" in content or "measurable" in content.lower():
            score += 0.2
            reasons.append("Measurable success metrics included.")

    return {
        "score": round(score, 2),
        "total": 1.0,
        "reasons": reasons,
        "passed": score >= 0.7,
        "mode": "deterministic"
    }

def judge_llm(artifact_path: Path, scenario_type: str, instruction: str):
    content = artifact_path.read_text()
    
    # Generate the prompt for the LLM-as-Judge
    prompt = f"""
### LLM JUDGE REQUEST ###
Scenario Category: {scenario_type}
Original Task: {instruction}

Deliverable Content:
---
{content}
---

Evaluation Rubric:
1. **Fidelity**: Does the output matches the aesthetic and technical bar (premium, high-quality)?
2. **Clarity**: Is the output readable and actionable for the next agent/person in the chain?
3. **Completeness**: Are all requirements from the instruction met?

Output Format:
JSON with keys: "score" (0.0-1.0), "reasoning" (detailed), and "verdict" (pass/fail).
##########################
"""
    print(prompt)
    
    # In this script, we'll just output the prompt and return a "pending" status.
    # The agent/user should provide the JSON response.
    return {
        "status": "pending_llm_score",
        "prompt": prompt,
        "mode": "llm"
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_path", type=str)
    parser.add_argument("--mode", choices=["deterministic", "llm"], default="deterministic")
    parser.add_argument("--type", choices=["design", "engineering", "business"], default="design")
    parser.add_argument("--instruction", type=str, help="Instruction for the scenario")
    args = parser.parse_args()

    path = Path(args.artifact_path)
    if args.mode == "llm":
        result = judge_llm(path, args.type, args.instruction)
    else:
        result = judge_deterministic(path, args.type)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
