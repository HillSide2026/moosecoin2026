---
id: 26-001-00007-STRATEGY-2-CANDIDATE
title: Strategy 2 Candidate - London Fix Breakout-and-Hold Model
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, candidate, regime, breakout, fail-fast]
---

# Strategy 2 Candidate - London Fix Breakout-and-Hold Model

## Classification

- Type: Procedural, fail-fast architecture
- Role: Conditional participation engine
- Not this:
  - Volatility strategy
  - Fade strategy
  - Prediction strategy

## Core Thesis

Trade only the first sustained breakout from a valid pre-fix balance range formed during London + NY overlap.

Exit immediately if price returns to balance.
Hold only while post-break momentum persists.

Priority stack:

1. Structural validity
2. Survival
3. Process fidelity
4. Low activity
5. Strict rule compliance

## Market Universe and Session Constraints

### Instruments

- EUR/USD
- USD/JPY
- GBP/USD

### Timeframes

- 5m primary
- 15m secondary (confirmation only)

### Session

- London + New York overlap only
- 13:00-16:30 London time
- Outside this window: no trade

Rationale: fix flow builds during overlap liquidity. Outside overlap increases structural distortion risk.

## Regime Logic (Gate Before Signal)

Regime classification is mandatory and precedes setup evaluation.

### Dormant Regime

- Overlap volatility < 20-day 30th percentile
- No directional expansion
- Action: no trade

### Dislocated Regime

- Large macro impulse within prior 60 minutes
- One-directional 1.5x ATR expansion
- Action: no trade

### Transitional Regime (Only Valid Regime)

- Compression present
- Expansion pressure building
- No macro shock contamination
- Action: risk allowed

Default when unclear: Dormant -> no trade.

Rule precedence:

1. Regime
2. Setup
3. Signal

## Setup Definition - Valid Balance Range

All conditions must pass.

Structural requirements:

- Horizontal support and resistance boundaries
- Minimum 6 consecutive candles fully contained
- Minimum 2 failed break attempts on each side
- Range height:
  - >= 2x spread
  - <= recent average swing size (last 10 swings)

If any test fails: setup invalid.

## Inside-Range Behavior

Inside range means flat.

Explicit prohibitions:

- No anticipation
- No fading edges
- No partial entries
- No early positioning

## Entry Logic (Single Pattern Only)

This system allows one entry pattern.

Conditions:

- Full candle close outside range
- Break candle closes fully outside
- Wick-only breaks ignored
- Next candle must not re-enter range

Entry trigger:

- Entry at open of the candle following confirmation
- Direction equals breakout direction
- Immediate re-entry invalidates setup -> no trade

No secondary trigger.

## Invalidation and Stop Logic

Stop location:

- Opposite side of the range

Immediate exit conditions:

- Any close back inside range
- No discretion
- No delay

Architecture: fail-fast by design.

## Sizing Logic

Fixed fractional risk per trade.

Example:

- 0.25%-0.50% of account equity

Position size:

`position_size = (account_equity * risk_pct) / stop_distance`

Where stop distance = entry price - opposite side of range.

No:

- Scaling in
- Adding to winners
- Partial fills

Single allocation only.

## Profit Management

No profit target.

Hold while momentum persists.

Momentum-decay exit triggers:

- Two candles fail to advance in breakout direction
- One full candle closes against position
- Visible compression begins

If none occur, hold persists.

Intent: small losses, open-ended gains.

## Participation Constraints

- Max 1 trade per range
- Max 2 trades per session
- No re-entry on same range after stop-out
- Missing trades is acceptable
- Low activity is expected

## Explicit No-Trade Filters

Trade is invalid if:

- Range is slanted
- Breakout candle is oversized (exhaustion)
- Spread degrades at break
- Stop cannot be defined pre-entry
- Any ambiguity exists

Ambiguity defaults to no trade.

## Non-Negotiable Risk Constraints

- No averaging down
- No scaling
- No discretionary overrides
- Single active strategy instance per account
- Liquidity degradation -> stand aside
- Assumption failure -> suspend strategy pending review

This is governance-controlled capital behavior.

## Operational Decision Engine Structure

1. Regime Filter
   - Session -> Instrument -> Volatility state -> Macro contamination
2. Risk Model
   - Spread check
   - Liquidity check
   - Stop definability check
3. Setup Engine
   - Balance structure validation
   - Range metrics
   - Failed-break confirmation
4. Signal Engine
   - Breakout-candle validation
   - Re-entry validation
5. Sizing Engine
   - Fixed fractional computation
6. Exit Engine
   - Fail-fast re-entry detection
   - Momentum-decay monitoring
7. Monitoring and Audit Layer
   - Log regime state
   - Log range boundaries
   - Log entry validation
   - Log exit cause
   - Version-lock every trade

## Auditability Requirement

Every trade must be reconstructible from logs.

## Status

Candidate draft for ML1 review under Project 26-001-00007. Not approved doctrine and not authorized for live deployment.
