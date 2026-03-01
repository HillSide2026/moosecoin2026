---
id: 26-001-00007-REGIME-SPEC
title: Regime Definition Specification - Strategy 2 Candidate
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, regime, specification]
---

# Regime Definition Specification

## Purpose

Translate regime labels into measurable conditions for deterministic use by the decision engine.

## Regime Precedence

1. Session eligibility
2. Macro contamination filter
3. Volatility state
4. Expansion/compression state

If any required input is unavailable, default to `dormant` and no trade.

## Regime States

### Dormant

Required conditions:

- Overlap volatility < 20-day 30th percentile
- No directional expansion signal

Action:

- No trade

### Dislocated

Required conditions (any):

- Large macro impulse within prior 60 minutes
- One-directional expansion >= 1.5x ATR

Action:

- No trade

### Transitional

Required conditions:

- Compression present
- Expansion pressure building
- No macro shock contamination
- Not dormant and not dislocated

Action:

- Trade risk allowed (subject to all downstream gates)

## Data and Calculation Inputs

- 5m/15m OHLCV bars for in-scope instruments
- Rolling 20-day volatility baseline
- ATR baseline for expansion tests
- Macro event calendar/flags for contamination gate
- Spread and liquidity context for go/no-go checks

## Open Specification Decisions

- SD-001: Final numeric definition of "large macro impulse"
- SD-002: Exact compression metric
- SD-003: Expansion pressure threshold definition
- SD-004: Fallback rule if macro feed is delayed
