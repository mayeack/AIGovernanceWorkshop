---
layout: default
title: Lab 2 — Secure
nav_order: 5
---

# Lab 2 — SECURE (Cisco AI Defense)
{: .no_toc }

**Pillar:** Secure<br>
**Tool:** Cisco AI Defense + MedAdvice chat<br>
**Timing:** 12–15 min<br>
**Outcome:** Trusted AI
{: .fs-5 .fw-300 }

1. TOC
{:toc}

---

## Objective

Turn the Lab 1 finding into enforcement: a medical-advice response is **blocked** as non-compliant; you update the governing policy and re-run to a **compliant** response. Take a prompt from blocked → compliant, live.

## Background

MedAdvice applies safety gates **before and after** the LLM call. Cisco AI Defense is a live integration: it inspects the prompt (pre-LLM) and the response (post-LLM) against **multiple guardrails** (PII, PHI, PCI, Harassment, Hate, Profanity, Sexual, Violence, Social Division, Prompt Injection, Code) and blocks non-compliant content. The **prescription-overreach** finding measured in [Lab 1](lab-1-measure.html) is authored here as a **custom response-direction guardrail**. Internal policy rules additionally block self-harm pre-LLM, and deterministic escalation rules route emergencies (e.g. chest pain) to a human-review queue.

## Step by step

1. In the **Cisco AI Defense console**, show the policy currently governing MedAdvice — including the **custom guardrail promoted from the Lab 1 measurement**. Point to the guardrails and thresholds — this is the live control plane, authored and tuned in real time.

2. In the **MedAdvice chat** (`/app`), trigger a deterministic, correlated blocked moment from a terminal. Scenario 3 sends a PHI/PII-heavy turn that AI Defense flags/blocks:

   ```bash
   venv/bin/python scripts/demo/seed_governance_scenarios.py --only 3
   ```

   {: .note }
   > Other deterministic block/flag moments: scenario **7** (policy-violating / toxic response → `policy_action=flag`) and scenario **8** (self-harm → hard policy block). Use whichever maps best to the policy you're demonstrating.

3. Show the **blocked** outcome in the chat UI / response — the non-compliant content does not reach the user. In the AI Defense console, show the verdict and which guardrail tripped.

4. **Tune the policy** in the AI Defense console (adjust the governing rule so a compliant response is permitted), and **re-run** the prompt.

5. Show the now-**compliant** response delivered to the user.

6. Pivot to Splunk: open the AI Governance Overview Dashboard's **Secure** section ("Policy blocks & guardrail trips over time") and show the block you just created appear, correlated by `event_id`.

## What this shows

- The block came from the eval. The overreach was measured in Lab 1 and authored as a guardrail here — eval defines it; the guardrail enforces it.
- Governance is a runtime control you author and tune in real time, not a quarterly review.
- Pre-LLM **and** post-LLM — the prompt going in and the response coming out are both inspected against multiple guardrails.
- The same turn is already in Splunk with the AI Defense verdict attached, correlated with the quality score that produced the guardrail.

## Expected result

First run: response **blocked**, verdict visible in AI Defense, block visible in Splunk. After tuning: same prompt returns a **compliant** response. The **Policy Blocks** KPI in the AI Governance Overview Dashboard increments.

{: .warning }
> If Lab 2 no longer shows a block, the policy was probably left in its tuned (permissive) state from a prior run. In AI Defense, revert the governing policy to its blocking state, then re-run the scenario.

<!-- exec-outcome:start -->
{: .outcome }
> **Executive outcome — Trusted AI.** Non-compliant output never reaches the user, and policy is authored and tuned in real time, then re-validated immediately against the live app — governance you can watch happen, not a quarter-long change request.
<!-- exec-outcome:end -->

---

[← Lab 1](lab-1-measure.html){: .btn } [Next: Lab 3 — Observe →](lab-3-observe.html){: .btn .btn-primary }
