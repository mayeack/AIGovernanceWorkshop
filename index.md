---
layout: default
title: Home
nav_order: 1
permalink: /
---

# One Cisco: Governing Agentic AI End to End

### The Agentic AI Governance Workshop — FY'27

**Secure. Observable. Governed. Measurable. One Cisco, end to end.**

*A field workshop for the executives accountable for AI — and the engineers who run it. Observability is one of four governed pillars covered here, not the whole story.*

---

[Start: Setup & Prerequisites](setup.html){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Jump to the labs](section-0-overview.html){: .btn .fs-5 .mb-4 .mb-md-0 }

## The Problem: AI Is Moving Faster Than Governance

Enterprises are shipping agentic AI into production faster than they can govern it. Autonomous and semi-autonomous agents now make decisions, call tools, and generate language that reaches customers, patients, and regulators — at machine speed, around the clock, at a volume no human review queue can keep pace with.

The risk is not theoretical. A single AI interaction can leak PII or PHI, absorb a prompt injection that overrides its instructions, fabricate a medical treatment that never existed, or quietly drift away from the behavior it was certified with. Each of these is, simultaneously, a **security** event, an **operations** event, a **quality** event, and a **compliance** event.

Yet most organizations are trying to govern this with disconnected point solutions. The security team sees a blocked prompt in one console. The SRE sees a latency spike in another. The data-science team sees a quality score in a third. The compliance officer, during an audit, is handed screenshots from all three and asked to reconstruct what actually happened on a given turn. **Four tools, four truths, no single thread connecting them.** By the time the story is stitched together by hand, the agent has served thousands more turns.

That gap — between the speed of agentic AI and the speed of governing it — is the problem this workshop closes.

---

## The One Cisco Thesis

One Cisco closes the governance gap end to end with **one integrated architecture across four pillars** — and the differentiator versus point tools is structural, not cosmetic:

> **Every AI interaction is captured once and correlated on a shared, OTel-compliant identifier, so security, operations, quality, and audit become one investigation, not four disconnected tools.**

The four pillars:

| Pillar | Capability | Platform |
| --- | --- | --- |
| **Measure / Evaluate** | Define **good**, then prove it — baseline vs. poisoned behavior, token & cost, signals that surface unknown unknowns, continuous metrics on a deployed agent | Cisco Agent Observability |
| **Secure** | Runtime policy + guardrails on every prompt and response | Cisco AI Defense |
| **Observe** | End-to-end tracing, latency, and cost | Splunk Observability Cloud |
| **Govern** | Immutable audit trail + forensics + security incident response | Splunk Core / Enterprise Security |

### The Single Pane of Glass

The architectural anchor is the **AI Governance Overview** dashboard in Splunk Core. It answers, in one view, the question every leader is actually asking — *"Is our AI safe, reliable, accurate, and accountable right now?"* — through KPI tiles (Total AI Requests, Cost, Token Usage, Unique Sessions), safety tiles (Safety Violations, PII Detected, Policy Blocked, Guardrails Triggered), GenAI Detection summaries, cost / latency / volume trends, and a Recent AI Requests log you pivot from to any turn's correlated record. Pillar deep-dives — Prompt Injection Detection, PII Detection, and Tokenomics are one click away.

---

## Start with Evaluation: Define "Good" Before You Can Guard It

Before any guardrail can fire, someone has to define what the guardrail is *for*. That definition is an **evaluation** — and in this architecture it comes first, because **a guardrail is just an evaluation finding with an action attached.** You cannot block what you have not measured, and you cannot certify what you cannot define.

**Cisco Agent Observability** (formerly Galileo) is where agentic behavior gets defined and measured. It evaluates the *whole agent trace* — workflow, agents, tool calls, and the LLM response — and scores each turn against research-backed metrics (hallucination, context adherence, PII/PHI leakage, tool-selection quality) plus **custom metrics you define for your own domain**. Those metrics are run by **Luna**, Cisco's family of small, purpose-built evaluation models, so you get LLM-as-judge quality *without* paying frontier-model prices to score every turn — and that cost profile is exactly what makes evaluation affordable to run **continuously**, not just once. You run it two ways: as an **offline experiment** over a dataset before you ship — and as **continuous scoring** on live traffic once deployed, where its **signals surface the unknown unknowns** no one anticipated.

## The Journey: One Turn, Four Pillars, One Thread

The workshop is delivered against a real, running application: MedAdvice — a multi-agent medical-advice chatbot. The same engine re-skins to six verticals (medical, tax, benefits, legal, finance, telecom), which is the proof that the governance pattern generalizes far beyond healthcare.

MedAdvice applies safety gates before and after every LLM call. **Cisco AI Defense** (Part 2) is a live integration: it inspects the prompt pre-LLM and the response post-LLM against multiple guardrails — PII, PHI, PCI, Harassment, Hate, Profanity, Prompt Injection, etc. — and blocks non-compliant content. Every turn is logged with full governance and audit metadata in Cisco Data Fabric.

That same per-turn telemetry feeds **Splunk Observability Cloud** (Part 3), the operational lens on the running agent. Where **Cisco AI Defense** governs what MedAdvice is allowed to say, **Observability Cloud** watches how it runs — emitting OpenTelemetry traces, spans, latency, and token/cost telemetry for every LLM call and tool hop across the multi-agent graph. Because each trace carries the same shared identifier as that turn's security verdict and quality score, a slow or expensive turn is one click from the exact span that caused it.

Splunk Core (Part 4) is where all of it comes to rest — the immutable audit trail and single pane over every governed turn, so any interaction can be pulled back by that same shared identifier and, when it's evidence-backed, escalated into Splunk Enterprise Security as a notable event.

None of these downstream pillars stand on their own, though — the foundation was laid in by **Cisco Agent Observability** (Part 1). The baseline-vs-poisoned evaluation is what defined "good" in the first place: the metrics, the thresholds, and the failure modes worth governing. AI Defense enforces that definition, Observability Cloud confirms the agent honors it under load, and Splunk Core proves it held — every pillar that follows is measuring against the baseline the evaluation set.

### Section 0 — AI Governance Overview: The Single Pane of Glass

**Scenario.** The exec opens the AI Governance Overview dashboard. Governed turns, policy blocks, injections, hallucinations, PII hits, and token cost are all on one screen.

**What One Cisco does.** Presents the entire governed AI estate in a single view, every KPI live, every governed turn traceable to its correlated record.

**Executive outcome.** The leader sees the posture of the AI program at a glance — and knows that any number on the screen is one click from the evidence behind it.

### Part 1 — Measure / Evaluate (Cisco Agent Observability): Define Good, Catch the Unknown Unknowns

**Scenario.** Before anything is secured or operated, the agent is *measured*. A **baseline** model and a **poisoned** model are run against the same patient prompts, and every turn is scored — quality, token usage, and cost — side by side.

**What One Cisco does.** Cisco Agent Observability evaluates the *whole agent trace* and scores each turn **baseline vs. poisoned**, using **Luna** — Cisco's small, purpose-built evaluator models — so continuous LLM-as-judge scoring is affordable instead of a frontier-model bill. It **surfaces token usage and cost** per arm, runs the custom metrics you defined, and flags the **unknown unknowns**: anomalous clusters, drift, and novel failure modes no rubric anticipated. The poisoned model's prescription overreach is caught here, quantified against the baseline, and handed to Part 2 to be enforced as a guardrail. Once the agent is live, those same signals and metrics keep running, turning quality into **consistent, continuous intelligence on the deployed agent** — not a one-time pre-ship check.

**Executive outcome — Improved Outcomes.** Quality, cost, and risk become measured, governed metrics with a baseline and an SLA — not a vibe. Poisoned behavior is caught before it ships, the cost of every behavior is visible, signals surface failures no one thought to test for, and continuous metrics keep the deployed agent honest over time.

### Part 2 — Secure (Cisco AI Defense): From Blocked to Compliant

**Scenario.** The evaluation in Part 1 measured the poisoned model's prescription overreach on otherwise benign prompts. Now that finding becomes enforcement.

**What One Cisco does.** This is where the evaluation becomes enforcement. Cisco AI Defense applies runtime guardrails on the prompt and the response — *per direction*, since the model's output is its own risk surface — and the prescription-overreach finding from the Cisco Agent Observability evaluation in Part 1 is authored here as a **custom response-direction guardrail**, so the exact behavior the eval measured is what now gets blocked. In the workshop, the participants author and tune the governing policy *in real time*, then re-run — taking it from **not blocked → compliant** live.

**Executive outcome — Trusted AI.** Non-compliant output never reaches the user, and policy is authored and tuned in real time, then re-validated immediately against the live app — governance you can watch happen, not a quarter-long change request.

### Part 3 — Observe (Splunk Observability Cloud): Trace the Bottleneck, Restore the SLO

**Scenario.** The response is now compliant — but latency has spiked beyond SLO. The agent is correct and slow, which in production is its own kind of failure.

**What One Cisco does.** Cisco Agent Observability already told us whether the agent *answered* well (Part 1); Splunk Observability Cloud tells us whether it *ran* well. The participant will first observe key metrics, tracing data, and tokenomics using the AI Agent Monitoring dashboards in Observability Cloud. Then, using the **Troubleshooting & Remediation Agent** in Splunk Observability Cloud, the participants trace the request end to end across the service and isolates the root-cause bottleneck. The participant applies the fix; the agent's role is to find the cause.

**Executive outcome — Operational Excellence.** Reliable, cost-efficient AI — performance problems are found by tracing, not guessing.

### Part 4 — Govern (Splunk Core / Enterprise Security): Audit, Surface, Escalate

**Scenario.** An audit is underway. The reviewer needs to demonstrate not just that controls exist, but that they fired — and to act on what they find.

**What One Cisco does.** The reviewer works the **immutable AI interaction logs**, reviews interactions blocked by policies in Cisco AI Defense, surfaces a prompt-injection attempt directly in the dashboard, and creates a correlation search to automatically escalate evidence-backed findings to Enterprise Security. Every governed turn is in the audit table.

**Executive outcome — Accountability & Evidence.** End-to-end auditability and defensible evidence — the audit is a query, not a fire drill, and findings flow straight into the security workflow.

---

## One Turn, End to End: Following a Single Event

The differentiator is easiest to see on a single worked turn. Take one governed interaction. Because every pillar is integrated, the four stories above are not four separate investigations; they are four facets of *one event*:

1. **Measure.** Cisco Agent Observability turns answer quality, token cost, and risk from a subjective "vibe" into continuously measured, SLA-governed metrics — scored cheaply by Luna, optimizing agent behavior, with signals that surface the unknown unknowns before they ever reach a customer.
2. **Secure.** Cisco AI Defense inspects the prompt and response against the policies and guardrails; the verdict and any policy block are attached — including the custom guardrail promoted directly from the measurement above.
3. **Observe.** In Splunk Observability Cloud, that trace shows where the latency went across the service — the *operational* face of the event.
4. **Govern.** Every governed AI interaction lands in an immutable, fully correlated audit trail — so proving compliance becomes a single query instead of a fire drill, and evidence-backed threats like prompt injection flow straight into the existing security response workflow.

One turn. Four pillars. One thread. The data scientist, the security analyst, the SRE, and the auditor are all looking at the same event — which is exactly what "one investigation, not four" means in practice.

---

## Five Executive Outcomes

| Outcome | What it means | Grounded in |
| --- | --- | --- |
| **Unified Visibility & Control** | The whole AI program on one screen; every KPI live, every number one click from its evidence | single pane of glass (Section 0) |
| **Improved Outcomes** | Measurable quality, cost, and risk; optimized agent behavior, unknown unknowns surfaced | evaluation, signals & continuous metrics (Part 1) |
| **Trusted AI** | Safe, compliant responses; non-compliant output blocked at runtime | exposed→compliant live (Part 2) |
| **Operational Excellence** | Reliable, cost-efficient AI; trace, don't guess | APM trace-to-root-cause (Part 3) |
| **Accountability & Evidence** | End-to-end auditability; defensible, correlated evidence | immutable audit trail for every event (Part 4) |

---

## The Call to Action

Agentic AI is already in production. The question for every CISO, CIO, CTO, and Chief Risk and Compliance officer is no longer *whether* to govern it, but *whether you can prove you are.*

One Cisco makes that proof a single screen and a single thread. **Capture every AI interaction once. Correlate it across security, operations, quality, and audit. Investigate once, not four times.**

This workshop puts that correlated architecture in your hands against a live, running multi-agent application — and shows you the exact moment an evaluation catches a poisoned model and becomes a live guardrail, a non-compliant response is blocked, a latency breach is traced, and a prompt injection is escalated, all on the same turn, all on the same thread.

**Secure. Observable. Governed. Measurable. One Cisco, end to end.**

Let's govern AI at machine speed.

---