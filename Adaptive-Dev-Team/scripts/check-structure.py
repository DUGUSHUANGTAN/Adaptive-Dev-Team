#!/usr/bin/env python3
"""Basic Skill structure validation."""
import os, sys

def check():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    required_dirs = [
        "roles", "builders", "specialists", "workflows",
        "protocols", "policies", "templates", "examples", "references"
    ]
    missing = [d for d in required_dirs if not os.path.isdir(os.path.join(base, d))]
    if missing:
        print("MISSING DIRS:", missing)
        return 1
    files = ["SKILL.md", "roles/leader.md", "protocols/delegation.md"]
    for f in files:
        if not os.path.exists(os.path.join(base, f)):
            print("MISSING FILE:", f)
            return 1
    print("Structure OK")
    return 0

if __name__ == "__main__":
    sys.exit(check())
