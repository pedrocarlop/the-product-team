#!/usr/bin/env python3
import sys
import os
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS_DIR = ROOT / "logs/benchmarks"

def get_latest_run(scenario_name: str):
    runs = sorted(LOGS_DIR.glob(f"{scenario_name}_*"), reverse=True)
    return runs[0] if runs else None

def meta_optimize(scenario_name: str, role: str, skill: str):
    latest_run = get_latest_run(scenario_name)
    if not latest_run:
        return {"error": f"No baseline run found for scenario {scenario_name}"}

    # 1. Get current score
    output_artifact = latest_run / "design-concept.md"
    if not output_artifact.exists():
        return {"error": f"Output artifact {output_artifact} not found"}

    # Run the judge
    judge_cmd = [sys.executable, str(ROOT / "auto-improve/judge.py"), str(output_artifact)]
    result = subprocess.run(judge_cmd, capture_output=True, text=True)
    baseline_result = json.loads(result.stdout)
    baseline_score = baseline_result["score"]
    
    print(f"BASELINE SCORE: {baseline_score}")
    print(f"REASONS: {baseline_result['reasons']}")
    
    if baseline_score >= 1.0:
        print("Skill achieved a perfect score. No optimization needed.")
        return {"status": "complete", "score": baseline_score}

    # 2. Strategy: Diagnostics and Modifications
    # In a real AutoAgent, we'd call an LLM with the reasons and the skill content.
    # We would say: "Improve this skill to fix these failures: {reasons}"
    
    print("Meta-Optimizer: Proposing a class of improvements for '{}'".format(skill))
    # For now, we'll output the "Optimization Prompt" for the agent.
    
    optimization_prompt = f"""
    OPTIMIZATION TARGET: {role}/{skill}
    CURRENT SCORE: {baseline_score}/1.0
    FAILURES:
    {json.dumps(baseline_result['reasons'], indent=2)}
    
    TASK: Modify 'agents/{role}/skills/{skill}.md' to specifically address these failures.
    Ensure you follow the 'skill-authoring-guide.md' for formatting.
    """
    
    print("\n--- OPTIMIZATION PROMPT ---\n")
    print(optimization_prompt)
    print("\n--- END PROMPT ---\n")
    
    return {
        "status": "ready_for_iteration",
        "baseline_score": baseline_score,
        "failures": baseline_result['reasons']
    }

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: meta_optimizer.py <scenario_name> <role> <skill>")
        sys.exit(1)
        
    result = meta_optimize(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
