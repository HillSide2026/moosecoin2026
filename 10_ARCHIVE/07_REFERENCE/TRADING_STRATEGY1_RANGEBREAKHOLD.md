---
id: 26-001-00001-STRATEGY-RANGE-BREAK-HOLD-V1
title: Range Break & Hold Strategy (Concrete v1.0)
owner: ML1
status: deprecated
created_date: 2026-02-08
last_updated: 2026-03-01
tags: [trading, strategy, execution, archived]
---

# Range Break & Hold Strategy (Concrete v1.0)

**One-Sentence Summary:** Trade the first sustained break from a clearly defined range, exit immediately if price returns to balance, and hold only while momentum persists.

## 1. Instruments & Timeframe

- Markets: EUR/USD, USD/JPY, GBP/USD
- Timeframe: 5-minute or 15-minute charts only
- Session: London + New York overlap only
- If outside session: no trading

## 2. Definition of a Clearly Defined Range (Non-Negotiable)

A range exists only if all conditions are met:

- Price trades between two horizontal levels (support & resistance)
- At least 6 consecutive candles remain fully inside those levels
- At least 2 failed attempts to break each side of the range
- Range height >= 2x spread and <= recent average swing size

If any condition fails: no range, no trade.

## 3. Behavior Inside the Range

- No trades allowed
- No anticipation
- No fading
- No partial positions
- Price inside the range = flat, always

## 4. Entry Rule (The Only Entry)

A valid entry occurs only when all are true:

- A candle closes fully outside the range
- The next candle does NOT re-enter the range
- Entry is taken at the open of the following candle
- Direction = direction of the break

If price wicks out but closes inside: ignore.
If price closes out but immediately re-enters: no trade.

## 5. Invalidation / Stop (Hard Rule)

- Stop = opposite side of the range
- If any candle closes back inside the range: exit immediately
- No discretion
- No “give it one more bar”
- This is a fail-fast trade by design

## 6. Position Sizing

- Risk fixed % per trade (e.g. 0.25%–0.5%)
- Position size calculated only from:
- Entry price
- Stop distance (range width)
- No scaling in
- No adding to winners

## 7. Profit Management (No Targets)

There are no profit targets.

Exit occurs when momentum decays, defined as any one of the following:

- Two consecutive candles fail to make progress in the breakout direction
- A full candle closes against the position
- Price begins forming a new compression (small overlapping candles)

If none occur: stay in the trade.

## 8. Trade Frequency Constraints

- Maximum 1 trade per range
- Maximum 2 trades per session
- If stopped out: do not re-enter the same range

## 9. When You Do Not Trade (Explicit)

You do not trade if:

- The range is messy or slanted
- The breakout candle is unusually large (exhaustion)
- Spread widens materially during the break
- You cannot define the stop before entry

If unsure: no trade.

## 10. Strategy Success Criteria

This strategy is judged on:

- Strict rule adherence
- Small average loss
- Occasional large directional wins
- Long periods of inactivity
- Low trade count is expected
- Missing moves is acceptable
- Survival is non-negotiable
