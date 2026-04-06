#!/usr/bin/env python3

import os
import json
import argparse
from datetime import datetime

"""
Product Team Instincts Memory CLI
Inspired by ECC Continuous Learning.

Manages reusable execution patterns (Instincts) across projects.
Instincts are stored as structured JSON.
"""

INSTINCTS_DIR = "knowledge/instincts"
INDEX_FILE = os.path.join(INSTINCTS_DIR, "index.json")

def ensure_setup():
    os.makedirs(INSTINCTS_DIR, exist_ok=True)
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'w') as f:
            json.dump({}, f)

def load_index():
    ensure_setup()
    with open(INDEX_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_index(data):
    ensure_setup()
    with open(INDEX_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def save_instinct(name, description, pattern, confidence="medium"):
    idx = load_index()
    
    instinct_data = {
        "name": name,
        "description": description,
        "pattern": pattern,
        "confidence": confidence,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "usage_count": 0
    }
    
    if name in idx:
        instinct_data["created_at"] = idx[name].get("created_at", instinct_data["created_at"])
        instinct_data["usage_count"] = idx[name].get("usage_count", 0)
    
    idx[name] = instinct_data
    save_index(idx)
    
    file_path = os.path.join(INSTINCTS_DIR, f"{name}.json")
    with open(file_path, 'w') as f:
        json.dump(instinct_data, f, indent=2)
        
    print(f"Instinct '{name}' saved successfully to {file_path}")

def query_instinct(keyword):
    idx = load_index()
    results = []
    for name, data in idx.items():
        if keyword.lower() in name.lower() or keyword.lower() in data.get("description", "").lower():
            results.append(data)
            
    if not results:
        print(f"No instincts found matching '{keyword}'")
        return
        
    for r in results:
        print(f"--- {r['name']} (Confidence: {r['confidence']}) ---")
        print(f"Description: {r['description']}")
        print(f"Pattern: \n{r['pattern']}")
        print("-" * 40)
        
        # update usage count
        idx[r['name']]["usage_count"] += 1
    save_index(idx)

def main():
    parser = argparse.ArgumentParser(description="Instincts Memory CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # Save
    parser_save = subparsers.add_parser("save")
    parser_save.add_argument("--name", required=True)
    parser_save.add_argument("--description", required=True)
    parser_save.add_argument("--pattern", required=True)
    parser_save.add_argument("--confidence", default="medium", choices=["low", "medium", "high", "guaranteed"])
    
    # Query
    parser_query = subparsers.add_parser("query")
    parser_query.add_argument("--keyword", required=True)
    
    # List
    parser_list = subparsers.add_parser("list")
    
    args = parser.parse_args()
    
    if args.command == "save":
        save_instinct(args.name, args.description, args.pattern, args.confidence)
    elif args.command == "query":
        query_instinct(args.keyword)
    elif args.command == "list":
        idx = load_index()
        for name, data in idx.items():
            print(f"- {name}: {data['description']} (Used: {data.get('usage_count', 0)})")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
