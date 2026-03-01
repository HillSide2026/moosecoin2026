---
id: 26-001-00008-RISK-ENGINE-SPEC
title: Risk Model Specification - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, risk, governance, strat3]
---

# RISK_ENGINE_SPEC

## Purpose

Define enforceable risk-engine rules for STRAT3 implementation.

## Position Sizing Formula

`position_size = (account_equity * risk_pct) / abs(spike_extreme - entry_price)`

Where:

- `risk_pct` in [0.25%, 0.50%] per approved profile
- `spike_extreme` is the invalidation level
- `entry_price` is the confirmed post-stall entry

## Session Risk Constraints

- Maximum exposure per session: configurable cap (default ML1-controlled)
- Maximum trades per fix event: 1
- Maximum fix trades per day: 1
- Maximum correlated exposure: one directional risk unit across correlated pairs

## Kill-Switch Rules

### Spread Degradation Kill-Switch

- If spread ratio exceeds 2x session median at trigger, no-trade.
- If spread degrades materially while in position, force exit and suspend new entries for the session.

### Liquidity Degradation Rule

- If liquidity quality falls below required execution standard, no-trade.
- Repeated liquidity failures in session force stand-aside.

### Macro Shock Override

- Any macro contamination breach during active window forces no-trade or immediate risk-off action.

## Enforcement Requirements

- No manual override path
- Gate checks must run before every entry
- Gate-fail reason must be logged
