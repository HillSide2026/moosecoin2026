---
id: MCP-26-009-SYSTEM-4-CANDIDATE
title: System 4 Candidate - London Fix Compression to Expansion Breakout
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, candidate, system-4, london-fix, volatility-transition]
---

# System 4 Candidate - London Fix Compression to Expansion Breakout

## 1. Classification

- Type: Controlled volatility state transition model
- Role: Volatility-state exploitation (not directional prediction)
- Not this:
  - Directional forecasting model
  - Noise breakout model

## 2. Core Thesis

Trade only volatility expansion that emerges from statistically abnormal
compression into the London Fix.

No compression -> no trade.
Exit immediately if expansion fails.
Hold only while expansion persists.

Priority stack:

1. Regime alignment
2. Volatility asymmetry
3. Structural timing
4. Fail-fast invalidation

## 3. Market Universe and Session Constraints

### Instruments

- EUR/USD
- USD/JPY
- GBP/USD

### Timeframes

- 5m primary
- 15m secondary confirmation allowed

### Session Structure

- London + New York overlap only
- Compression must form between 13:00-15:45 London
- Breakout must occur between 15:55-16:10 London
- Outside this structure: no trade

## 4. Regime Logic (Gate Before Signal)

Regime classification precedes compression evaluation.

Rule precedence:

1. Regime
2. Compression
3. Break trigger

### Dormant Regime

- Entire overlap volatility < 20-day 30th percentile
- No expansion catalysts
- Action: no trade

Interpretation: dormant + no pressure = dead market.

### Dislocated Regime

- Macro impulse within prior 60 minutes
- 1.5x ATR directional move pre-fix
- Action: no trade

Interpretation: expansion already happened.

### Transitional Regime (Only Valid Regime)

- Normal overlap volatility
- Progressive intraday compression
- No macro distortion
- Action: risk allowed

Regime must allow volatility expansion potential.

## 5. Setup Definition - Valid Compression Structure

All criteria must pass.

### Volatility Conditions

- 15:15-15:45 realized volatility <= 20-day intraday 25th percentile
- True range of last 4 candles contracting sequentially
- Compression high-low range:
  - >= 2x spread
  - <= 60% of average 5m swing size
- Price remains inside clearly defined micro-range
  - Minimum 6 contained candles

If any condition fails: no setup.

## 6. Inside-Compression Behavior

- Flat by rule
- No anticipation
- No bracket orders before confirmation
- No directional bias

Compression without break = no trade.

## 7. Entry Logic (Single Pattern Only)

Only one entry pattern is allowed.

Step 1 - Compression validated:

- All structural tests passed

Step 2 - Break condition:

- Full 5m candle closes outside compression range during 15:55-16:10 London
- Wick-only break is invalid

Step 3 - Confirmation:

- Next candle must not fully re-enter compression range

Entry:

- Enter at open of following candle
- Direction = breakout direction
- Immediate re-entry invalidates setup

## 8. Invalidation and Stop Logic

Stop placement:

- Opposite side of compression range

Hard exit triggers:

- Any full candle close back inside range
- Volatility collapse immediately after break
- Spread degradation beyond threshold

No discretion. No override. Fail fast.

## 9. Sizing Logic

- Fixed fractional risk: 0.25%-0.50% of equity
- Single allocation only

Position size:

`position_size = (equity * risk_pct) / compression_range_height`

No scaling, no pyramiding, no partial exits.

## 10. Profit Management

No fixed target.

Exit only when expansion decays. Momentum decay is:

- Two consecutive candles fail to extend range
- One full candle closes opposite breakout direction
- New micro-compression forms
- 16:25 London time reached (hard time stop)

If expansion persists, hold persists.

## 11. Participation Constraints

- Max 1 trade per compression structure
- Max 2 trades per session
- No re-entry on same structure
- Missing breakout is acceptable
- Low activity is expected

## 12. Explicit No-Trade Filters

No trade if any apply:

- Compression is slanted
- Spread widens during break
- Break candle > 2.5x compression height (exhaustion risk)
- Stop cannot be defined precisely
- Macro event scheduled within 30 minutes
- Uncertainty in state/logic

Ambiguity defaults to no trade.

## 13. Non-Negotiable Risk Constraints

- No averaging down
- No scaling
- No discretionary overrides
- Single strategy instance active
- Liquidity degradation -> stand aside
- Structural assumption failure -> suspend model

Governed capital discipline applies.

## 14. Operational Decision Engine Structure

1. Regime Filter
   - Session validation
   - Volatility percentile check
   - Macro contamination filter
2. Risk Gate
   - Spread check
   - Liquidity check
   - Stop definability check
3. Compression Engine
   - Sequential contraction detection
   - Range integrity test
   - Volatility percentile validation
4. Breakout Engine
   - Time-window validation
   - Full-close confirmation
   - Re-entry check
5. Sizing Engine
   - Fixed fractional calculation
6. Exit Engine
   - Momentum decay detection
   - Time stop
   - Invalidation trigger
7. Monitoring and Audit Layer
   - Log compression metrics
   - Log volatility percentile
   - Log break time
   - Log exit cause
   - Log regime state
   - Log version ID

## 15. Auditability Requirement

Every trade must be reconstructible.

## 16. Engineering Characteristics

This model:

- Trades volatility transition, not direction
- Performs best on quiet overlap days
- Avoids spike-fade conflict with prior strategy streams
- Has lower win rate but higher asymmetry potential
- Is sensitive to spread widening at breakout

Expected behavior:

- Low frequency
- Occasional strong expansion capture
- Many no-trade days (correct behavior)

## Status

Candidate draft for ML1 review under Project MCP-26-009. Not approved doctrine
and not authorized for live deployment.
