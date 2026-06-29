---
layout: default
title: Lab 2 — Secure
nav_order: 5
---

# Lab 2 — SECURE (Cisco AI Defense)
{: .no_toc }

**Pillar:** Secure<br>
**Tool:** Cisco AI Defense<br>
**Timing:** 20 minutes<br>
**Outcome:** Trusted AI
{: .fs-5 .fw-300 }

<!-- persona:start -->

{: .persona }
> **Who this is for.** The **CISO** and **AI Security / AppSec** teams. Primary
> question: _Is our AI safe to put in front of customers, and can I prove
> threats are stopped in real time?_ AI / ML Platform leaders join as the owners
> who author and tune the guardrails alongside security.

<!-- persona:end -->

1. TOC
{:toc}

---

## Objective

{: .objective }
> Turn the Lab 1 finding into enforcement: a medical-advice response is **non-compliant**; you update the governing policy and re-run to ensure a **governed** response.

## Background

Cisco AI Defense is a live integration: it inspects the prompt (pre-LLM) and the response (post-LLM) against **multiple guardrails** and blocks non-compliant content. The **Prescriptive Overreach** finding measured in [Lab 1](lab-1-measure.html) is authored here as a **custom response-direction guardrail**.

>>>TBD: Reference Cisco AI Defense lab for deep dive in setup and configuration

## Step by step

### 1. Access DemoBot

Lorem ipsum

### 2. Prompt Prescriptive Overreach

This is the DemoBot control panel — the behind-the-scenes settings that lets you deliberately inject unsafe AI behavior and switch defenses on and off.

Cisco AI Defense Policy Review — Routes every prompt through AI Defense before it reaches the assistant, blocking unsafe inputs up front.

Behavior injection toggles (Synthetic PII/PHI, Toxic Content, Hallucinated Content, Prescriptive Overreach) — The "poison" switches: deliberately force the AI to leak data, turn toxic, fabricate facts, or overstep its scope.

![alt text](image-20.png)

Feel free to explore how the various toggles generate non-compliant behavior, and how that behavior is blocked when Cisco AI Defense is toggled on.

### 3. Access Cisco AI Defense

Lorem ipsum

### 4. Review Dashboard

The Cisco AI Defense dashboard is the security command center for the AI estate — it discovers every AI asset in use, enforces protection around it, and shows in one number how many threats have been stopped, turning AI security from a blind spot into an actively defended perimeter.

Total events detected — The headline: how many risky AI interactions were caught, and how many were stopped versus merely watched. This is the proof of active defense — the AI isn't just observed, threats are intercepted in real time.

Applications & Protection status — Inventories the AI applications in use and shows how many are actually protected versus exposed. The value is closing the gap between "AI we know about" and "AI we're defending" — you can't secure what you can't see.

AI Assets — A complete map of the AI attack surface: the agents, models, data, and third-party apps employees touch. This is asset discovery for AI — the foundation of any security program, surfacing shadow AI before it becomes a breach.

![alt text](image-9.png)

### 5. Review Associated Policies

Click on Secure -> Runtime Policies.

![alt text](image-18.png)

Click on **Yeack Protect**.

This is where AI protection gets enforced — the Yeack Protect policy in Cisco AI Defense shows the live guardrails wrapped around our agentic system, turning security intent into specific rules that actively block threats in real time.

Guardrail profiles — Organizes protection into the three dimensions that matter — keeping attackers out, keeping data private, and keeping responses appropriate. The value is comprehensive coverage in one policy, not a single narrow filter.

Direction (Prompt / Response / both) — Each rule inspects the right side of the conversation — what the user sends in, what the AI sends back, or both. The value is precision: threats are caught at the exact point they enter or leave.

Action & Status (Block / Enabled) — Shows whether each guardrail is on and set to stop violations or just monitor them. This is enforcement, not observation — the difference between a policy on paper and a control that actually intervenes.

Filter strength (Medium) — A tunable dial on how aggressively each rule fires. The value is balance — protection calibrated to the business's risk tolerance, tightenable where the stakes are higher.

![alt text](image-19.png)

### 6. Create Custom Prescriptive Overreach Guardrail

Lorem ipsum - pending availability of Policy Studio

### 7. Validate Applied Guardrail

Lorem ipsum

## Outcome

A risky medical response went from **non-compliant to governed**. The unsafe output never reached the user; the policy was authored and tuned on the spot; the fix was re-validated against the live app immediately.

- **Threats are stopped, not just seen.** Cisco AI Defense inspects every prompt and every response, and blocks what crosses the line in real time.
- **Governance is a runtime control.** Policy is written and tuned the moment a gap appears — not filed as a quarterly change request.
- **Measure and enforce are one loop.** The Lab 1 finding became the guardrail.

<!-- exec-outcome:start -->

{: .outcome }
> **Executive outcome — Trusted AI.** Non-compliant output never reaches the user, and policy is authored and tuned in real time, then re-validated immediately against the live app — governance you can watch happen, not a quarter-long change request.

<!-- exec-outcome:end -->

---

[← Lab 1](lab-1-measure.html){: .btn } [Next: Lab 3 — Observe →](lab-3-observe.html){: .btn .btn-primary }
