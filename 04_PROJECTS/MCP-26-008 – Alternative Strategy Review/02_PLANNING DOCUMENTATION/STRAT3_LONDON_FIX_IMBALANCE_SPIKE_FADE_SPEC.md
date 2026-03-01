---
id: 26-001-00008-STRAT3-SPEC
title: Strategy Specification - STRAT3 London Fix Imbalance Spike Fade
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, specification, procedural, strat3]
---

# STRAT3 London Fix Imbalance Spike Fade Specification

This document is the procedural contract for Strategy 3.

## 1. Market Universe

- EUR/USD
- USD/JPY
- GBP/USD

## 2. Session Constraints

- Session window: London fix event only
- Time window: 15:55-16:10 London time
- Outside session: no-trade
- Primary timeframe: 5m
- Execution precision: 1m allowed for order timing only

## 3. Regime Classification Definitions

### Dormant

- No abnormal volatility into fix
- Fix move < 1x 5m ATR
- Action: no-trade

### Dislocated

- Macro catalyst in prior 60 minutes, or
- Persistent directional expansion pre-fix
- Action: no-trade

### Transitional (Only Tradable Regime)

- Stable overlap session before event
- Sudden volatility expansion in 15:55-16:00 window
- No macro contamination
- Action: risk allowed (subject to remaining gates)

Default when regime is unclear: dormant -> no-trade.

## 4. Setup Requirements (Valid Imbalance Spike)

All conditions must pass:

- 15:55-16:00 move magnitude >= 1.8x and <= 2.5x 5m ATR
- Move forms within 1 to 2 candles maximum
- Spread <= 2x session median spread
- No macro event contamination in prior 60 minutes
- Move extends beyond prior overlap range boundary

Any failure invalidates setup.

## 5. Entry Logic (Single Pattern)

Entry requires both steps:

1. Spike completion:
   - A full candle closes after 16:00
   - The close fails to extend the spike extreme
2. Re-entry test:
   - Next candle fails to make a new extreme
   - Compression or an opposing close is present

Trigger:

- Enter opposite the spike direction at open of following candle
- Wick-only reversal is invalid
- Immediate spike resumption invalidates setup

No secondary trigger is allowed.

## 6. Invalidation Rules

- Stop for short fade: above spike extreme
- Stop for long fade: below spike extreme
- Immediate hard exit when any applies:
  - Candle closes beyond spike extreme
  - Spread widens beyond threshold
  - Volatility re-expands in spike direction

No discretion, no delay, no override.

## 7. Profit Management

- No fixed target
- Exit when any applies:
  - 50% to 70% retracement of spike achieved
  - Two non-advancing candles
  - Compression forms
  - 16:20 London time reached (hard time stop)

## 8. Participation Constraints

- Maximum 1 trade per fix event
- Maximum 1 fix trade per day
- No re-entry after stop-out on same event
- Missing trades are acceptable

## 9. No-Trade Filters

No-trade if any apply:

- Spike is multi-stage gradual expansion
- Spike event occurs before 15:55
- Spread degradation > 2x median
- Prior range boundary was not clearly violated
- Regime classification is uncertain

## 10. Non-Negotiable Risk Constraints

- No averaging down
- No scaling/add-ons
- No discretionary overrides
- Single active strategy instance per account
- Liquidity deterioration forces stand-aside
- Macro shock override enforces no-trade
- Assumption failure triggers suspension pending ML1 review

## 11. Audit Requirement

Every decision path must be reconstructible:

- Regime state and classification inputs
- Spike magnitude and ATR multiple
- Spread state and risk-gate outcomes
- Entry/exit timestamps and exit reason
- Strategy/model version linkage
