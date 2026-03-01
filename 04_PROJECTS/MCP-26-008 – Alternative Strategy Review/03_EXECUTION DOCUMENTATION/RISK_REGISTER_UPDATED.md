---
id: 26-001-00008-RISK-REGISTER-UPDATED
title: Risk Register (Updated) - Alternative Strategy Review
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, risks, execution, strat3]
---

# Risk Register (Updated)

## Purpose

Track execution-stage risk changes as implementation detail increases.

## Updated Risks

| Risk ID | Description | Impacted Layer | Likelihood | Impact | Mitigation | Owner | Status |
|---------|-------------|----------------|------------|--------|------------|-------|--------|
| R-001 | Macro contamination gating unavailable at decision time | Regime / Risk | Medium | Critical | Default to no-trade and escalate | ML1 | Open |
| R-002 | Stall-confirmation false positives increase fade losses | Signal / Exit | Medium | High | Tighten confirmation logic and audit gate outcomes | ML1 | Open |
| R-003 | Spread degradation not captured quickly enough | Risk / Execution | Medium | High | Enforce pre-entry and in-trade spread checks | ML1 | Open |
| R-004 | Event-window timing drift causes invalid participation | Regime / Operations | Low | High | Enforce hard session gates and timestamp validation | ML1 | Open |

## Risk Handling Notes

- Risks with no mapped mitigation remain blocked until ML1 disposition.
- Risk state changes must be synchronized with decision and change-request logs.
