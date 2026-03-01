---
id: 26-001-00007-STRAT2-EXEC-PLAYBOOK
title: Operational Playbook - STRAT2
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, operations, playbook, strat2]
---

# STRAT2_EXECUTION_PLAYBOOK

## 1. Pre-Session Checklist

- Confirm session window (13:00-16:30 London time)
- Confirm instrument universe enabled (EUR/USD, USD/JPY, GBP/USD)
- Confirm data feed health and timestamp integrity
- Confirm risk-engine configuration/version
- Confirm assumption register status (no unresolved critical failures)

## 2. Regime Classification Checklist

- Compute regime inputs (volatility percentile, expansion, macro contamination)
- Assign regime label
- If regime != transitional -> no-trade
- Log regime state before setup evaluation

## 3. Spread Check Procedure

- Measure live spread vs overlap baseline
- If spread exceeds threshold -> no-trade
- Record spread measurement and gate outcome

## 4. Trade Logging Procedure

- Create/append trade record using `TRADE_LOG_SCHEMA.md`
- Log strategy ID and version before entry
- Log setup metrics and gate outcomes
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
