#!/usr/bin/env python3
"""Install the Product Team workflow for Antigravity into a target project.

Thin wrapper around install.py --platform antigravity. Kept for backward compatibility.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from install import main as _main

sys.argv = [arg for arg in sys.argv if arg != "--platform"] + ["--platform", "antigravity"]
raise SystemExit(_main())
