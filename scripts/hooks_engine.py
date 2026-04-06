#!/usr/bin/env python3

import os
import sys
import json
import subprocess
import argparse
from datetime import datetime

"""
Product Team Hooks Engine
Inspired by ECC's hook execution wrapper.

This script executes arbitrary skills/tasks while wrapping them in Pre/Post execution hooks.
Usage:
  ./scripts/hooks_engine.py --role <role> --skill <skill_name> --action "<command to run>"
"""

def log_hook(event_type, msg):
    timestamp = datetime.now().isoformat()
    log_dir = "logs/hooks"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{event_type}_log.txt")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"[Hook Engine: {event_type}] {msg}")

def run_pre_flight(role, skill):
    log_hook("PreFlight", f"Validating transition to '{role}' for skill '{skill}'")
    # Here you could load `agents/{role}/skill-catalog.md` or similar 
    # to enforce valid assignment schemas, check inputs_used, etc.
    if not os.path.exists(f"agents/{role.split('/')[0]}/{role.split('/')[-1]}"):
        pass # Handle dynamic path or skip
    return True

def run_post_flight(role, skill, exit_code, stdout, stderr):
    log_hook("PostFlight", f"Execution complete. Code: {exit_code}")
    # Write a receipt or summary
    manifest_dir = f"knowledge/runs/run-current"
    os.makedirs(manifest_dir, exist_ok=True)
    manifest_path = os.path.join(manifest_dir, "manifest.json")
    
    data = []
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                pass
                
    data.append({
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "skill": skill,
        "success": exit_code == 0
    })
    
    with open(manifest_path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

def main():
    parser = argparse.ArgumentParser(description="Hook Engine execution wrapper")
    parser.add_argument("--role", required=True, help="Agent role executing, e.g. engineer/frontend-engineer")
    parser.add_argument("--skill", required=True, help="Skill name being executed")
    parser.add_argument("--action", required=False, help="Action to execute under hook umbrella")
    
    args = parser.parse_args()
    
    if not run_pre_flight(args.role, args.skill):
        print(f"[Error] PreFlight hook failed for {args.role}")
        sys.exit(1)
        
    exit_code = 0
    stdout, stderr = "", ""
    if args.action:
        log_hook("Execute", f"Running command: {args.action}")
        result = subprocess.run(args.action, shell=True, text=True, capture_output=True)
        exit_code = result.returncode
        stdout = result.stdout
        stderr = result.stderr
        if stdout:
            print(stdout)
        if stderr and exit_code != 0:
            print(f"[Stderr]: {stderr}", file=sys.stderr)
            
    run_post_flight(args.role, args.skill, exit_code, stdout, stderr)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
