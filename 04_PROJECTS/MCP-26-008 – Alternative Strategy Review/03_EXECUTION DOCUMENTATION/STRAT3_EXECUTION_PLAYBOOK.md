---
id: 26-001-00008-STRAT3-EXEC-PLAYBOOK
title: Operational Playbook - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, operations, playbook, strat3]
---

# STRAT3_EXECUTION_PLAYBOOK

## 1. Pre-Session Checklist

- Confirm London fix window controls (15:55-16:10 London)
- Confirm instrument universe enabled (EUR/USD, USD/JPY, GBP/USD)
- Confirm data feed health, timestamps, and session clock alignment
- Confirm risk-engine configuration/version
- Confirm assumption register status (no unresolved critical failures)

## 2. Regime Classification Checklist

- Compute regime inputs (macro contamination, volatility state, event-window expansion)
- Assign regime label
- If regime != transitional, no-trade
- Log regime state before spike evaluation

## 3. Spread Check Procedure

- Measure current spread ratio vs session median
- If ratio > 2x threshold, no-trade
- Record spread measurement and gate outcome

## 4. Trade Logging Procedure

- Create/append trade record using `TRADE_LOG_SCHEMA.md`
- Log strategy ID and version before entry
- Log spike metrics, stall confirmation, and gate outcomes
- Log exit trigger and slippage after close

## 5. Suspension Conditions

- Assumption failure event
- Repeated spread/liquidity degradation
- Risk-gate anomalies or missing critical inputs
- Any unresolved ambiguity in decision path

Action: suspend strategy execution and escalate to ML1.

## 6. Post-Session Review Checklist

- Review gate-fail reasons and counts
- Review trade outcomes vs expected behavior band
- Review execution quality (spread/slippage)
- Review assumption stability indicators
- Record required actions in status and issue logs
