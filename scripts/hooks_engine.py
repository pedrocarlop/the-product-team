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
  ./scripts/hooks_engine.py --role <role> --skill <skill_name> [--run-id <id>] [--project-slug <slug>] --action "<command to run>"

Execution records are written to logs/active/<project-slug>/runs/<run-id>-<timestamp>/.
Knowledge deliverables are NOT written here — agents write those directly to knowledge/.
"""


def log_hook(event_type, msg):
    timestamp = datetime.now().isoformat()
    log_dir = "logs/hooks"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{event_type}_log.txt")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"[Hook Engine: {event_type}] {msg}")


def run_pre_flight(role, skill, run_id=None, project_slug=None):
    log_hook("PreFlight", f"Validating transition to '{role}' for skill '{skill}'")

    run_dir = None
    if run_id and project_slug:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        run_dir = f"logs/active/{project_slug}/runs/{run_id}-{timestamp}"
        os.makedirs(run_dir, exist_ok=True)
        log_hook("PreFlight", f"Created run directory: {run_dir}")

    return run_dir


def run_post_flight(role, skill, exit_code, stdout, stderr, run_dir=None):
    log_hook("PostFlight", f"Execution complete. Code: {exit_code}")

    # Write manifest to the run directory if available, otherwise to logs/hooks/
    manifest_parent = run_dir if run_dir else "logs/hooks"
    os.makedirs(manifest_parent, exist_ok=True)
    manifest_path = os.path.join(manifest_parent, "manifest.json")

    data = []
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            try:
                data = json.load(f)
            except Exception:
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
    parser.add_argument("--run-id", required=False, default=None, help="Unique run identifier, e.g. RUN-001")
    parser.add_argument("--project-slug", required=False, default=None, help="Project slug, e.g. 20260315-analytics-mvp")
    parser.add_argument("--action", required=False, help="Action to execute under hook umbrella")

    args = parser.parse_args()

    run_dir = run_pre_flight(args.role, args.skill, args.run_id, args.project_slug)

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

    run_post_flight(args.role, args.skill, exit_code, stdout, stderr, run_dir)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
