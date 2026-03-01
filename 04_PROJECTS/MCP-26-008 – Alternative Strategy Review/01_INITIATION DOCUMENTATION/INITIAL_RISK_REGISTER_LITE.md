---
id: 26-001-00008-RISK-LITE
title: Initial Risk Register (Lite) - Alternative Strategy Review
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, risks, initiation]
---

# Initial Risk Register (Lite)

| Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
|--------|-------------|------------|--------|------------|-------|--------|
| R1 | Alternative candidate is not materially distinct from existing strategy concepts | Medium | Medium | Require explicit differentiation criteria in review template | ML1 | Open |
| R2 | Candidate contains hidden discretionary logic | Medium | High | Enforce deterministic rule wording and reject ambiguous triggers | ML1 | Open |
| R3 | Candidate conflicts with doctrine risk constraints | Medium | High | Run doctrine compatibility screening before any advancement | ML1 | Open |
| R4 | Review effort expands without decision closure | Medium | Medium | Use time-boxed review cycles and ML1 decision checkpoints | ML1 | Open |
| R5 | Candidate depends on unavailable or unreliable data inputs | Medium | High | Require data dependency declaration and availability check in initiation | ML1 | Open |

## Assumptions to Validate

- At least one viable alternative strategy can be documented within current doctrine constraints
- Candidate logic can be represented cleanly in `02_MODELS/` as a decision engine
- Governance-first screening can eliminate weak candidates before planning-stage investment
