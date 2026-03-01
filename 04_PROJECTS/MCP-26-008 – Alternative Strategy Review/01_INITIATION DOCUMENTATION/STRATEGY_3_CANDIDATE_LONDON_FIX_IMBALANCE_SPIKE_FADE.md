---
id: 26-001-00008-STRATEGY-3-CANDIDATE
title: Strategy 3 Candidate - London Fix Imbalance Spike Fade
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, candidate, regime, london-fix, mean-reversion]
---

# Strategy 3 Candidate - London Fix Imbalance Spike Fade

## Classification

- Type: Controlled reversion architecture
- Role: Conditional mean reversion after flow completion
- Not this:
  - Anticipation
  - Counter-trend discretionary trading

## Core Thesis

Trade only statistically extreme imbalance spikes that occur during the London 4PM Fix window.

Enter only after the imbalance event completes. Exit immediately if imbalance persists.
Hold only while reversion structure develops.

Priority stack:

1. Controlled exposure
2. Short holding time
3. Structural exhaustion
4. Strict invalidation

## Market Universe and Session Constraints

### Instruments

- EUR/USD
- USD/JPY
- GBP/USD

### Timeframes

- 5m primary
- 1m execution precision allowed (decision remains 5m-based)

### Session

- London Fix window only
- 15:55-16:10 London time
- Outside this window: no trade

This is strictly a fix-event strategy.

## Regime Logic (Gate Before Signal)

Regime must be confirmed before spike evaluation.

Rule precedence:

1. Regime
2. Spike magnitude
3. Signal

### Dormant Regime

- No abnormal volatility into fix
- Fix move < 1x 5m ATR
- Action: no trade

### Dislocated Regime

- Macro catalyst within prior 60 minutes
- Persistent directional expansion pre-fix
- Action: no trade

### Transitional Regime (Only Valid Regime)

- Stable overlap session
- Sudden volatility expansion during 15:55-16:00
- No macro contamination
- Action: risk allowed

## Setup Definition - Valid Imbalance Spike

All conditions must pass:

- Fix window move (15:55-16:00) >= 1.8x to 2.5x 5m ATR
- Move occurs within 1 to 2 candles maximum
- Spread does not widen beyond 2x session median
- No macro event in prior 60 minutes
- Move extends beyond prior overlap range boundary

If any condition fails: setup invalid.

## During-Spike Behavior

- No anticipation
- No fading during active imbalance
- No partial entries
- No guessing top or bottom
- Remain flat until stall confirmation

## Entry Logic (Single Pattern Only)

Only one entry pattern is allowed.

Step 1 - Spike completion:

- Wait for a full candle close after 16:00
- That candle fails to extend the spike further

Step 2 - Re-entry test:

- Next candle fails to make a new extreme, and
- Shows compression or an opposing close

Entry trigger:

- Enter opposite direction of spike at open of next candle
- Wick-only reversal is invalid
- If spike resumes immediately: setup invalid

## Invalidation and Stop Logic

Stop placement:

- Short fade: above spike extreme
- Long fade: below spike extreme

Hard exit triggers:

- Any candle close beyond spike extreme
- Spread widening beyond threshold
- Volatility re-expands in spike direction

No discretion. No delay. Fail fast.

## Sizing Logic

- Fixed fractional risk per trade: 0.25% to 0.50% of equity
- Single allocation only

Position size:

`position_size = (equity * risk_pct) / abs(spike_extreme - entry_price)`

No scaling, no partial exits.

## Profit Management

No fixed target.

Exit when any applies:

- 50% to 70% retracement of spike
- Momentum stalls (two non-advancing candles)
- Compression forms
- 16:20 London time reached

Holding beyond 16:20 is not permitted.

## Participation Constraints

- Max 1 trade per fix event
- Max 1 fix trade per day
- No re-entry after stop-out
- Missing spike is acceptable
- Low participation is expected

## Explicit No-Trade Filters

No trade if any apply:

- Spike is multi-stage (gradual expansion)
- Spike occurs before 15:55
- Spread degradation > 2x median
- Range boundary was not clearly violated
- Regime classification is uncertain

Ambiguity defaults to no trade.

## Non-Negotiable Risk Constraints

- No averaging down
- No discretionary override
- No scaling
- Single active strategy instance
- Liquidity deterioration forces stand-aside
- Macro shock overrides everything
- Assumption failure requires strategy suspension

## Operational Decision Engine Structure

1. Regime Filter
   - Session check
   - Macro contamination
   - Volatility classification
2. Risk Gate
   - Spread check
   - Liquidity check
   - Slippage risk check
3. Spike Engine
   - ATR multiple test
   - Time window validation
   - Range violation check
4. Stall Confirmation Engine
   - Failure to extend
   - Compression signal
5. Sizing Engine
   - Fixed fractional computation
6. Exit Engine
   - Spike extreme breach
   - Retracement threshold
   - Time stop
7. Monitoring and Audit Layer
   - Log spike magnitude
   - Log ATR multiple
   - Log spread state
   - Log exit cause
   - Log regime state
   - Log version identifier

## Auditability Requirement

All trades must be reconstructible.

## Status

Candidate draft for ML1 review under Project 26-001-00008. Not approved doctrine and not authorized for live deployment.
