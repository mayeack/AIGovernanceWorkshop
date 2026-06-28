---
layout: default
title: Lab 3 — Observe
nav_order: 6
---

# Lab 3 — OBSERVE (Splunk Observability Cloud)
{: .no_toc }

**Pillar:** Observe<br>
**Tool:** Splunk Observability Cloud<br>
**Timing:** 12–15 min<br>
**Outcome:** Operational Excellence
{: .fs-5 .fw-300 }

1. TOC
{:toc}

---

## Objective

{: .objective }
> The response is compliant, but latency has spiked beyond SLO. Use the Troubleshooting & Remediation Agent to trace the request end-to-end, isolate the bottleneck, and restore performance.

## Background

## Step by step

### 1. Access Splunk Observability Cloud

Lorem ipsum

### 2. Lorem Ipsum

1. Show the **healthy baseline** first: in the AI Governance Overview Dashboard's Observe section ("Response latency avg / p90"), point out the steady-state — **avg latency ~8s**.

2. **Inject the incident** live (disruptive; auto-expires). The endpoint drives sustained authenticated load and forces latency/errors against `service=demobot-v3`:

   ```bash
   curl -u x:$ACCESS_KEY -X POST http://localhost:8001/api/incident/start \
     -H 'Content-Type: application/json' \
     -d '{"latency_ms":15000,"error_rate":0.4,"duration_s":90,"drive_traffic":true}'
   ```

   This forces ~15s latency with ~40% errors for 90 seconds, with a load driver keeping the APM MetricSets dense above their detector thresholds.

   {: .warning }
   > **Always pass explicit values.** A bare `POST /api/incident/start` uses larger API defaults (`latency_ms=20000`, `error_rate=0.6`, `duration_s=600`) — ~20s / ~60% / ~600s — which is too long for the room. Pass `duration_s` (and friends) every time to keep the incident short and predictable.

3. In **Splunk Observability Cloud → APM**, select `service=demobot-v3`. Watch the latency and error-rate **detectors breach** their thresholds.

4. Use the **Troubleshooting & Remediation Agent** / APM trace view to drill into a slow trace, walk the span waterfall, and **isolate the bottleneck**. The agent finds the cause; you apply the fix.

5. **Restore performance** — let the incident auto-expire, or stop it early:

   ```bash
   curl -u x:$ACCESS_KEY -X POST http://localhost:8001/api/incident/stop
   ```

   Check status any time with `GET /api/incident/status`.

6. Confirm latency returns to baseline in the APM service view and in the AI Governance Overview Dashboard's Observe latency chart.

## Outcome

- Same platform, same correlation key. The slow turn in APM is the **same** `trace_id` you'd pull up in the audit log — operations, quality, and forensics share one identity.
- A Troubleshooting & Remediation Agent traces end-to-end and points at the bottleneck instead of you grepping logs.
- Cost and latency aren't separate dashboards — Observe shows token usage and latency on the same governed turns Cisco Agent Observability already scored for quality.

APM detectors breach during the ~90s incident; the trace view isolates the slow span; latency returns to ~8s baseline after stop/expiry. The AI Governance Overview Dashboard's Observe latency line shows the spike and recovery.

{: .note }
> The incident is a controlled fault injection against the demo service — safe, time-boxed, and reversible. It does not affect any real workload.

<!-- exec-outcome:start -->

{: .outcome }
> **Executive outcome — Operational Excellence.** Reliable, cost-efficient AI — performance problems are found by tracing, not guessing.

<!-- exec-outcome:end -->

---

[← Lab 2](lab-2-secure.html){: .btn } [Next: Lab 4 — Govern →](lab-4-govern.html){: .btn .btn-primary }
