---
id: 26-001-00007-STRAT2-SPEC
title: Strategy Specification - STRAT2 London Fix Breakout-and-Hold
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, specification, procedural, strat2]
---

# STRAT2 London Fix Breakout-and-Hold Specification

This document is the procedural contract for Strategy 2.

## 1. Market Universe

- EUR/USD
- USD/JPY
- GBP/USD

## 2. Session Constraints

- Session window: London + New York overlap
- Time window: 13:00-16:30 London time
- Outside session: no-trade
- Primary timeframe: 5m
- Secondary timeframe: 15m confirmation only

## 3. Regime Classification Definitions

### Dormant

- Overlap volatility below 20-day 30th percentile
- No directional expansion
- Action: no-trade

### Dislocated

- Macro impulse contamination in prior 60 minutes OR
- One-directional expansion >= 1.5x ATR
- Action: no-trade

### Transitional (Only Tradable Regime)

- Compression present
- Expansion pressure building
- No macro contamination
- Action: risk allowed (subject to remaining gates)

Default when regime is unclear: dormant -> no-trade.

## 4. Setup Requirements

All conditions must pass:

- Horizontal support/resistance boundaries
- At least 6 consecutive contained candles
- At least 2 failed break attempts on each side
- Range height >= 2x spread
- Range height <= recent average swing size (10-swing baseline)

Any failure invalidates setup.

## 5. Entry Logic (Single Pattern)

- Break candle must close fully outside range
- Wick-only breakouts are invalid
- Next candle must not re-enter range
- Entry at open of following candle
- Direction equals breakout direction

No secondary trigger is allowed.

## 6. Invalidation Rules

- Stop location: opposite side of range
- Any close back inside range triggers immediate exit
- No discretion, no delay, no override

## 7. Profit Management

- No fixed target
- Hold while momentum persists
- Exit on any momentum-decay trigger:
  - Two candles fail to progress
  - One full candle closes against position
  - Visible compression returns

## 8. Participation Constraints

- Maximum 1 trade per range
- Maximum 2 trades per session
- No re-entry after stop-out on same range
- Low activity is expected behavior

## 9. No-Trade Filters

No-trade if any apply:

- Slanted range
- Oversized breakout candle (exhaustion proxy)
- Spread degradation at break
- Stop cannot be defined pre-entry
- Any ambiguity in state

## 10. Non-Negotiable Risk Constraints

- No averaging down
- No scaling/add-ons
- No discretionary override path
- Single active strategy instance per account
- Liquidity degradation -> stand aside
- Assumption failure -> strategy suspension pending ML1 review

## 11. Audit Requirement

Every decision path must be reconstructible:

- Regime state
- Risk-gate outcomes
- Setup/entry validation state
- Exit reason
- Strategy/model version linkage
