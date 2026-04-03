#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_DIR = ROOT / "auto-improve/scenarios"
LOGS_DIR = ROOT / "logs/benchmarks"

def run_benchmark(scenario_name: str, role: str, skill: str):
    scenario_path = SCENARIOS_DIR / scenario_name
    instruction = (scenario_path / "instruction.md").read_text()
    
    # Path to the specific skill being tested
    skill_path = ROOT / f"agents/{role}/skills/{skill}.md"
    if not skill_path.exists():
        return {"error": f"Skill {skill} not found at {skill_path}"}
    
    skill_content = skill_path.read_text()
    
    # Prepare the "Execution Context"
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = LOGS_DIR / f"{scenario_name}_{run_id}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    (run_dir / "context.md").write_text(f"### SKILL UNDER TEST: {skill}\n\n{skill_content}\n\n### TASK:\n{instruction}")
    
    print(f"Benchmark '{scenario_name}' prepared for {role}/{skill}.")
    print(f"Context saved to: {run_dir}/context.md")
    
    # In a real AutoAgent, we'd call an LLM here.
    # For this simulation, we'll wait for the human/agent to provide the output.
    print(f"EXPECTATION: Produce 'design-concept.md' in {run_dir}")
    
    return {
        "run_id": run_id,
        "run_dir": str(run_dir),
        "scenario": scenario_name,
        "role": role,
        "skill": skill
    }

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: benchmark.py <scenario_name> <role> <skill>")
        sys.exit(1)
        
    result = run_benchmark(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
