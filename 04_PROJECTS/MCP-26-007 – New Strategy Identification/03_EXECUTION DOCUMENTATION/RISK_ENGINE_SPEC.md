---
id: 26-001-00007-RISK-ENGINE-SPEC
title: Risk Model Specification - STRAT2
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, risk, governance, strat2]
---

# RISK_ENGINE_SPEC

## Purpose

Define enforceable risk-engine rules for STRAT2 implementation.

## Position Sizing Formula

`position_size = (account_equity * risk_pct) / stop_distance`

Where:

- `risk_pct` in [0.25%, 0.50%] per approved profile
- `stop_distance` = entry price to opposite side of range

## Session Risk Constraints

- Maximum exposure per session: configurable cap (default ML1-controlled)
- Maximum trades per session: 2
- Maximum trades per range: 1
- Maximum correlated exposure: one directional risk unit across strongly correlated instruments

## Kill-Switch Rules

### Spread Degradation Kill-Switch

- If live spread at trigger exceeds configured threshold relative to overlap median, no-trade.
- If spread degrades materially while in position, suspension/stand-aside rule may apply (per ML1 tolerance settings).

### Liquidity Degradation Rule

- If liquidity quality is below required execution standard, no-trade.
- Repeated liquidity failures in session -> suspend further entries for session.

## Enforcement Requirements

- No manual override path
- Gate checks must run before every entry
- Gate-fail reason must be logged
