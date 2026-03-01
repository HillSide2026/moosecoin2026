---
id: 26-001-00001-MODEL-V2
title: Trading Model v2
owner: ML1
status: in_progress
created_date: 2026-02-08
last_updated: 2026-03-01
tags: [trading, model, decision-engine, execution]
---

# Trading Model v2

## 1. Purpose & Scope

This model operationalizes a single concrete strategy: **Range Break & Hold (v1.0)**.
It defines a procedural decision engine and execution requirements.
Doctrine remains binding authority.

## 2. Decision Engine Components

- Regime filter: session/timeframe/market eligibility and stand-aside conditions
- Risk model: hard constraints, invalidation, and suspension logic
- Entry logic: explicit breakout-and-confirmation entry criteria
- Exit logic: invalidation and momentum-decay exit criteria
- Signal generation: directional trigger from valid range break and hold
- Sizing engine: fixed-risk sizing from entry and stop distance

## 3. Strategy Summary

**One-Sentence Summary:** Trade the first sustained break from a clearly defined range, exit immediately if price returns to balance, and hold only while momentum persists.

## 4. Instruments, Timeframe, and Session

- Markets: EUR/USD, USD/JPY, GBP/USD
- Timeframe: 5-minute or 15-minute charts only
- Session: London + New York overlap only
- If outside session: no trading

## 5. Range Definition (Non-Negotiable)

A range exists only if all conditions are met:

- Price trades between two horizontal levels (support & resistance)
- At least 6 consecutive candles remain fully inside those levels
- At least 2 failed attempts to break each side of the range
- Range height >= 2x spread and <= recent average swing size

If any condition fails: no range, no trade.

## 6. Behavior Inside the Range

- No trades allowed
- No anticipation
- No fading
- No partial positions
- Price inside the range = flat, always

## 7. Entry Rule (The Only Entry)

A valid entry occurs only when all are true:

- A candle closes fully outside the range
- The next candle does NOT re-enter the range
- Entry is taken at the open of the following candle
- Direction = direction of the break

If price wicks out but closes inside: ignore.
If price closes out but immediately re-enters: no trade.

## 8. Invalidation / Stop (Hard Rule)

- Stop = opposite side of the range
- If any candle closes back inside the range: exit immediately
- No discretion
- No “give it one more bar”
- This is a fail-fast trade by design

## 9. Position Sizing

- Risk fixed % per trade (e.g. 0.25%–0.5%)
- Position size calculated only from:
  - Entry price
  - Stop distance (range width)
- No scaling in
- No adding to winners

## 10. Profit Management (No Targets)

There are no profit targets.

Exit occurs when momentum decays, defined as any one of the following:

- Two consecutive candles fail to make progress in the breakout direction
- A full candle closes against the position
- Price begins forming a new compression (small overlapping candles)

If none occur: stay in the trade.

## 11. Trade Frequency Constraints

- Maximum 1 trade per range
- Maximum 2 trades per session
- If stopped out: do not re-enter the same range

## 12. When You Do Not Trade (Explicit)

You do not trade if:

- The range is messy or slanted
- The breakout candle is unusually large (exhaustion)
- Spread widens materially during the break
- You cannot define the stop before entry

If unsure: no trade.

## 13. Hard Constraints (Always Enforced)

- No averaging down
- No position scaling
- No discretionary overrides
- No exceptions
- Crypto exposure flat by session end
- Single active strategy instance per account

## 14. Monitoring & Suspension Rules

- If liquidity or spreads degrade materially: stand aside
- If any candle closes back inside the range: exit immediately
- If assumptions fail: suspend strategy and require review/approval to reactivate

## 15. Change Control

Any change requires:
- Rationale
- Impact analysis
- Approval

Risk-increasing changes require capital-owner consent.

## 16. Auditability

Every trade must be explainable, reconstructible, and version-bound. If it can’t be audited, it doesn’t belong.
