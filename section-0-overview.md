---
layout: default
title: AI Governance Overview Dashboard
nav_order: 3
---

# AI Governance Overview Dashboard: The Single Pane of Glass
{: .no_toc }

**Pillar:** Overview<br>
**Tool:** Splunk — AI Governance Overview dashboard<br>
**Timing:** 8–10 min<br>
**Outcome:** Unified Visibility & Control
{: .fs-5 .fw-300 }

1. TOC
{:toc}

---

## Objective

Establish the thesis: every governed turn and its quality/security scores live in one view, and you drill from there into any pillar.

## Step by step

1. Open the **AI Governance Overview** dashboard in Splunk; set the time range to **Last 7 days**.
2. Walk the **KPI and safety tiles** left to right:
   - **Total AI Requests** — every turn the platform governed.
   - **Safety Violations / Policy Blocked / Guardrails Triggered** — non-compliant content stopped or flagged at runtime (Cisco AI Defense + internal policy).
   - **PII Detected** — sensitive-data detections (the `ai_cim:pii:ml_scoring` pipeline correlates by `event_id`).
   - **Total Token Usage / Total Cost** — spend as a first-class governance signal.
   - **Unique Sessions** — breadth of activity.
3. Walk the **GenAI / ML Detection summaries** and the cost / latency / volume trends. The Overview previews all four governance dimensions (Measure, Secure, Observe, Govern) in one surface; the dedicated pillar dashboards in the same TA are the deep-dives, one click away.
4. Land on the **Recent AI Requests (Detailed Log)** table at the bottom. Pick a flagged turn, copy its `event_id`, and run the pivot below to resolve it to the **full correlated record** (Cisco Agent Observability score + AI Defense verdict + PII/injection/hallucination scores). This is the teaser for [Lab 4](lab-4-govern.html).

   ```spl
   index=gen_ai_log "<event_id>"
   ```

## What this shows

- Every number on the screen comes from the **same governed turns**. Quality, security, operations, and audit aren't four tools — they're four views of one record, joined on `gen_ai.event.id` / `trace_id`.
- Point tools each see a slice. One Cisco captures the interaction **once** and correlates the rest together — one investigation, not four.

## Expected result

The KPI tiles are populated and the Govern table has rows. Over a rolling ~7–30 day window you should see roughly:

| Signal | Range |
|---|---|
| Governed turns | ~170–190 across ~165 sessions, ~50 end-users |
| Policy blocks | ~11–14 |
| Prompt-injection attempts (ML-detected) | ~12 |
| Hallucinations flagged | ~90 |
| PII/PHI hits | ~17 |
| Toxic hits | ~56 |
| Tokens | ~120K |
| Avg latency | ~8s |

<!-- exec-outcome:start -->
{: .outcome }
> **Executive outcome.** The leader sees the posture of the AI program at a glance — and knows that any number on the screen is one click from the evidence behind it.
<!-- exec-outcome:end -->

---

[Next: Lab 1 — Measure →](lab-1-measure.html){: .btn .btn-primary }
