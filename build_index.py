#!/usr/bin/env python3
"""Regenerate index.md (Home) = front matter + jump buttons + the workshop narrative VERBATIM.

The Home page must mirror the canonical narrative verbatim (see the update-workshop-site
skill). Run this whenever the narrative changes instead of hand-editing index.md:

    python3 build_index.py

By default it reads the narrative from the sibling collateral folder (this repo cloned
inside the OneDrive "o11y AI Workshop '27" project) and writes index.md next to this script.
Override the source with an argument or the NARRATIVE_MD env var if your layout differs:

    python3 build_index.py "/path/to/1 - narrative.md"
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_NARRATIVE = HERE.parent / "collateral" / "1 - narrative.md"

narrative_path = Path(
    sys.argv[1] if len(sys.argv) > 1 else os.environ.get("NARRATIVE_MD", DEFAULT_NARRATIVE)
)
OUT = HERE / "index.md"

FRONT = (
    "---\n"
    "layout: default\n"
    "title: Home\n"
    "nav_order: 1\n"
    "permalink: /\n"
    "---\n\n"
)

BUTTONS = (
    "\n"
    "[Start: Setup & Prerequisites](setup.html){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }\n"
    "[Jump to the labs](section-0-overview.html){: .btn .fs-5 .mb-4 .mb-md-0 }\n"
)

if not narrative_path.exists():
    sys.exit(f"narrative not found: {narrative_path}\n"
             f"Pass the path as an argument or set NARRATIVE_MD.")

text = narrative_path.read_text(encoding="utf-8")
lines = text.split("\n")

# Insert the jump buttons just after the first horizontal rule (the one below the title block).
insert_at = None
for i, ln in enumerate(lines):
    if ln.strip() == "---" and i > 0:
        insert_at = i + 1
        break

if insert_at is None:
    body = text
else:
    body = "\n".join(lines[:insert_at]) + "\n" + BUTTONS + "\n".join(lines[insert_at:])

# Workshop-specific presentation: wrap each "Executive outcome …" paragraph in a
# just-the-docs `outcome` callout so it stands out on the Home page (the text is
# unchanged — only blockquote/callout markup is added). Requires an `outcome`
# callout defined in _config.yml.
out_lines = []
n_outcomes = 0
for ln in (FRONT + body).split("\n"):
    if ln.startswith("**Executive outcome"):
        out_lines.append("{: .outcome }")
        out_lines.append("> " + ln)
        n_outcomes += 1
    else:
        out_lines.append(ln)

OUT.write_text("\n".join(out_lines), encoding="utf-8")
print(f"wrote {OUT} from {narrative_path} ({OUT.stat().st_size} bytes; "
      f"{n_outcomes} executive-outcome callouts)")
