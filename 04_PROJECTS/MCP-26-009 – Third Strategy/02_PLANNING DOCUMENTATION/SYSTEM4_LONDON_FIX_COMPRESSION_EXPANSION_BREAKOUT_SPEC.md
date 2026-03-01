---
id: MCP-26-009-SYSTEM4-SPEC
title: Strategy Specification - SYSTEM4 London Fix Compression to Expansion Breakout
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, specification, procedural, system4]
---

# SYSTEM4 London Fix Compression to Expansion Breakout Specification

This document is the procedural contract for System 4.

## 1. Market Universe

- EUR/USD
- USD/JPY
- GBP/USD

## 2. Session Constraints

- Session: London + New York overlap only
- Compression formation window: 13:00-15:45 London time
- Breakout window: 15:55-16:10 London time
- Outside defined structure: no-trade
- Primary timeframe: 5m
- Secondary confirmation: 15m allowed

## 3. Regime Classification Definitions

### Dormant

- Entire overlap volatility below 20-day 30th percentile
- No expansion catalysts
- Action: no-trade

### Dislocated

- Macro impulse in prior 60 minutes, or
- 1.5x ATR directional move pre-fix
- Action: no-trade

### Transitional (Only Tradable Regime)

- Normal overlap volatility
- Progressive intraday compression
- No macro distortion
- Action: risk allowed (subject to remaining gates)

Default when regime is unclear: dormant -> no-trade.

## 4. Setup Requirements (Valid Compression Structure)

All conditions must pass:

- 15:15-15:45 realized volatility <= 20-day intraday 25th percentile
- True range of last 4 candles contracts sequentially
- Compression range height:
  - >= 2x spread
  - <= 60% of average 5m swing size
- Price contained inside a micro-range with at least 6 contained candles

Any failure invalidates setup.

## 5. Entry Logic (Single Pattern)

Entry requires all steps:

1. Compression validated:
   - All setup tests pass
2. Break condition:
   - A full 5m candle closes outside compression range
   - Break occurs within 15:55-16:10 London window
   - Wick-only break is invalid
3. Confirmation:
   - Next candle does not fully re-enter compression range

Trigger:

- Enter at open of following candle
- Direction equals breakout direction
- Immediate re-entry invalidates setup

No secondary trigger is allowed.

## 6. Invalidation Rules

- Stop location: opposite side of compression range
- Immediate hard exit when any applies:
  - Full candle closes back inside compression range
  - Volatility collapses immediately after break
  - Spread degrades beyond threshold

No discretion, no delay, no override.

## 7. Profit Management

- No fixed target
- Exit when momentum decay appears:
  - Two consecutive candles fail to extend range
  - One full candle closes opposite breakout direction
  - New micro-compression forms
  - 16:25 London time reached (hard time stop)

## 8. Participation Constraints

- Maximum 1 trade per compression structure
- Maximum 2 trades per session
- No re-entry on same structure after invalidation
- Missing breakouts are acceptable

## 9. No-Trade Filters

No-trade if any apply:

- Compression is slanted
- Spread widens during break trigger
- Break candle > 2.5x compression height (exhaustion risk)
- Stop cannot be defined precisely
- Macro event scheduled within 30 minutes
- Regime/compression/break state uncertainty

## 10. Non-Negotiable Risk Constraints

- No averaging down
- No scaling or pyramiding
- No discretionary overrides
- Single strategy instance active per account
- Liquidity degradation forces stand-aside
- Structural assumption failure triggers suspension pending ML1 review

## 11. Audit Requirement

Every decision path must be reconstructible:

- Regime state and regime inputs
- Compression metrics and validation outcomes
- Breakout timestamp and confirmation outcomes
- Exit reason and timing
- Strategy/model version linkage
