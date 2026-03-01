---
id: 26-001-00008-ASSUMPTION-REGISTER
title: Assumption Register - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, assumptions, strat3]
---

# ASSUMPTION_REGISTER

If any critical assumption fails, strategy suspension is required pending ML1 review.

## Assumptions

| Assumption ID | Assumed Condition | Monitoring Signal | Failure Trigger | Action on Failure | Status |
|---------------|-------------------|-------------------|-----------------|-------------------|--------|
| A-001 | Fix-window spikes include exhaustion candidates after flow completion | Spike continuation rate after stall signal | Persistent continuation after approved entries | Suspend strategy and review | Open |
| A-002 | Liquidity profile in fix window supports deterministic execution | Fill quality, slippage, and spread metrics | Repeated poor fills or slippage spikes | Suspend entries for session, escalate | Open |
| A-003 | Spread stability remains inside threshold at decision/entry times | Spread ratio tracking vs session median | Frequent >2x threshold breaches | Suspend strategy and review | Open |
| A-004 | Regime classification reliably separates dislocated from transitional states | Regime consistency and macro-tag outcomes | Recurring misclassification pattern | Suspend and recalibrate definitions | Open |

## Governance Note

Assumption failure is not an optimization signal. It is a suspension signal.
