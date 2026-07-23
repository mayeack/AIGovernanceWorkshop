#!/usr/bin/env python3
"""Regenerate content/_index.md (Home) = hero front matter + the workshop narrative VERBATIM,
and sync each lab/overview page's full Executive outcome from that same narrative.

The Home page must mirror the canonical narrative verbatim (see the update-workshop-site
skill). With the Hugo splunk-workshop theme, the narrative's title block (title, tagline,
pillars line) moves into the hero front matter and the old jump buttons become hero CTAs —
that is the only "workshop UI" transformation. Everything after the title block is emitted
verbatim, except that each `**Executive outcome …**` paragraph is wrapped in a
`{{% notice info "Executive outcome" %}}` callout (text unchanged, markup only) and image
paths are rewritten to /images/ (screenshots live in static/images/).

The same run syncs the five Executive-outcome paragraphs onto the overview/lab pages
(between `<!-- exec-outcome:start -->` / `<!-- exec-outcome:end -->` markers), so they never
drift from Home. Run this whenever the narrative changes instead of hand-editing:

    python3 build_index.py

By default it reads the narrative from the sibling collateral folder (this repo cloned
inside the OneDrive "o11y AI Workshop '27" project). Override with an argument or the
NARRATIVE_MD env var:

    python3 build_index.py "/path/to/1 - narrative.md"
"""
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_NARRATIVE = HERE.parent / "collateral" / "1 - narrative.md"

narrative_path = Path(
    sys.argv[1] if len(sys.argv) > 1 else os.environ.get("NARRATIVE_MD", DEFAULT_NARRATIVE)
)
OUT = HERE / "content" / "_index.md"
WORKSHOP_DIR = HERE / "content" / "workshops" / "ai-governance"

if not narrative_path.exists():
    sys.exit(f"narrative not found: {narrative_path}\n"
             f"Pass the path as an argument or set NARRATIVE_MD.")

text = narrative_path.read_text(encoding="utf-8")
lines = text.split("\n")

# --- Split the title block (everything before the first hr) from the body ------------------
try:
    hr = next(i for i, ln in enumerate(lines) if ln.strip() == "---" and i > 0)
except StopIteration:
    sys.exit("narrative has no '---' after the title block — layout changed?")

title_block = [ln for ln in lines[:hr]]
body_lines = lines[hr + 1:]

h1 = tagline = pillars = ""
extra_title_lines = []  # e.g. the italic "A field workshop…" descriptor — kept in the body
for ln in title_block:
    s = ln.strip()
    if not s:
        continue
    if s.startswith("# ") and not h1:
        h1 = s[2:].strip()
    elif s.startswith("### ") and not tagline:
        tagline = s[4:].strip()
    elif s.startswith("**") and s.endswith("**") and not pillars:
        pillars = s.strip("*").strip()
    else:
        extra_title_lines.append(ln)

if not h1:
    sys.exit("narrative title block has no '# ' heading — layout changed?")


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


# The hero renders the H1 with a gradient accent on emphasized text.
hero_title = h1.replace("End to End", "*End to End*") if "End to End" in h1 else h1

FRONT = f'''+++
title         = "{esc(h1)}"
hero_title    = "{esc(hero_title)}"
eyebrow       = "{esc(tagline)}"
description   = "{esc(pillars)}"
home_sections = ["workshops"]

[[cta]]
label = "Start: Setup & Prerequisites"
href  = "/workshops/ai-governance/01-setup/"
style = "primary"

[[cta]]
label = "Jump to the labs"
href  = "/workshops/ai-governance/02-overview/"
style = "ghost"
+++
'''

# --- Body: verbatim narrative + outcome callouts + image path rewrite ----------------------
out_lines = []
n_outcomes = 0
for ln in extra_title_lines + [""] + body_lines:
    if ln.startswith("**Executive outcome"):
        out_lines.append('{{% notice style="info" title="Executive outcome" icon="star" %}}')
        out_lines.append(ln)
        out_lines.append("{{% /notice %}}")
        n_outcomes += 1
    else:
        out_lines.append(ln.replace("](image", "](/images/image"))

body = re.sub(r"\n{3,}", "\n\n", "\n".join(out_lines)).strip("\n")
OUT.write_text(FRONT + "\n" + body + "\n", encoding="utf-8")
print(f"wrote {OUT} from {narrative_path} ({OUT.stat().st_size} bytes; "
      f"{n_outcomes} executive-outcome callouts)")

# --- Sync each lab/overview page's full Executive outcome from the narrative ---------------
# The narrative has exactly five "**Executive outcome …**" paragraphs, in this order:
# Overview, Part 1, Part 2, Part 3, Part 4 — mapped positionally to the pages below. Each
# page carries its outcome as a notice callout between sentinel markers, so the text stays
# verbatim-identical to Home.
OUTCOME_PAGES = [
    "02-overview.md",        # Overview / single pane of glass
    "03-lab-1-measure.md",   # Part 1 — Measure
    "04-lab-2-secure.md",    # Part 2 — Secure
    "05-lab-3-observe.md",   # Part 3 — Observe
    "06-lab-4-govern.md",    # Part 4 — Govern
]
MARK_START = "<!-- exec-outcome:start -->"
MARK_END = "<!-- exec-outcome:end -->"

outcomes = [ln for ln in lines if ln.startswith("**Executive outcome")]
if len(outcomes) != len(OUTCOME_PAGES):
    sys.exit(f"expected {len(OUTCOME_PAGES)} '**Executive outcome' paragraphs in the "
             f"narrative, found {len(outcomes)} — cannot sync lab pages safely.")

synced = 0
for page_name, outcome in zip(OUTCOME_PAGES, outcomes):
    page = WORKSHOP_DIR / page_name
    if not page.exists():
        print(f"  skip {page_name}: not found")
        continue
    page_lines = page.read_text(encoding="utf-8").split("\n")
    try:
        s = page_lines.index(MARK_START)
        e = page_lines.index(MARK_END)
    except ValueError:
        print(f"  skip {page_name}: missing exec-outcome markers")
        continue
    block = [MARK_START, "",
             '{{% notice style="info" title="Executive outcome" icon="star" %}}',
             outcome,
             "{{% /notice %}}",
             "", MARK_END]
    page_lines[s:e + 1] = block
    page.write_text("\n".join(page_lines), encoding="utf-8")
    synced += 1

print(f"synced {synced}/{len(OUTCOME_PAGES)} lab/overview executive outcomes from {narrative_path}")
