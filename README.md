# Agentic AI Governance Workshop

Customer-facing site for the **One Cisco — Agentic AI Governance Workshop**, published with
GitHub Pages (just-the-docs theme) at:

**https://mayeack.github.io/AIGovernanceWorkshop/**

A hands-on workshop for governing agentic AI across four correlated pillars — **Measure,
Secure, Observe, Govern** — on a live multi-agent demo application.

## Editing

This is a Jekyll site served from the `main` branch root. Edit the Markdown pages
(`index.md`, `setup.md`, `lab-*.md`, `wrap-up.md`, `reference.md`); commit to `main` and
GitHub Pages rebuilds automatically (~1 min).

Local preview (optional):

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000/AIGovernanceWorkshop/
```

## Conventions

- **Customer-facing.** No internal sales positioning or facilitator-only delivery notes.
- **`index.md` (Home)** mirrors the canonical workshop narrative verbatim, plus
  workshop-specific UI (jump-to-labs buttons).
- The lab commands reference the demo application repo
  ([DemoBot](https://github.com/mayeack/DemoBot)) — `scripts/demo/seed_governance_scenarios.py`,
  `scripts/demo/galileo_eval_prescription.py`, and the `/api/incident/*` endpoints.
- **Outcomes** use the standard **`outcome` callout** — a blue, thick-bordered box (color in
  `_config.yml`, border weight in `_sass/custom/custom.scss`). On Home it is applied
  automatically by `build_index.py`; elsewhere precede the outcome with `{: .outcome }`.
