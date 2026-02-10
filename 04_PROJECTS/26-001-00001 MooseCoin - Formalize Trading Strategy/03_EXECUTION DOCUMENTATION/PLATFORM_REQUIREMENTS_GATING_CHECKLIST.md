---
id: 26-001-00001-PLATFORM-GATING-CHECKLIST
title: Trading Platform Gating Checklist (Minimum Implementation Requirements)
owner: ML1
status: in_progress
created_date: 2026-02-08
last_updated: 2026-02-08
tags: [trading, platform, requirements, execution]
---

# Trading Platform Gating Checklist (Minimum Implementation Requirements)

**Rule:** If a platform cannot satisfy every mandatory item below without workaround logic, it is disqualified.

## 1. Instrument & Session Specifications (MANDATORY)

The platform must support:

- Exact symbol mapping for: EUR/USD, USD/JPY, GBP/USD
- Explicit venue/exchange identifiers per symbol
- Timezone handling sufficient to define London + New York overlap
- Precise session start/end timestamps
- Holiday and early-close calendars with ability to disable trading on affected sessions
- Chart timeframe restriction: 5-minute and 15-minute only
- No execution on other timeframes

**Fail condition:** Cannot hard-restrict execution to approved sessions and timeframes.

## 2. Market Data Requirements (MANDATORY)

The platform must support:

- Explicit price data source selection
- Candle construction rules:
  - Bid / ask / mid selection
  - Timezone-aligned candles
  - Session-aware candle boundaries
- Spread measurement using live bid/ask
- Quantifiable spread expansion logic:
  - Ability to compute median / baseline spread
- Definition of “recent average swing size” with:
  - Configurable lookback window
  - Explicit metric (range, ATR, or equivalent)

**Fail condition:** Spread, candle, or swing metrics are opaque or fixed by vendor.

## 3. Range Identification Rules (MANDATORY)

The platform must allow fully quantified range logic, including:

- Horizontal level definition with pip-based tolerance
- “6 consecutive candles fully inside range”:
  - Explicit wick inclusion/exclusion control
- “2 failed break attempts”:
  - Explicit definition of failure vs continuation
- Range height constraints:
  - Min / max height (absolute or relative)
- Slanted or noisy ranges:
  - Quantifiable rejection criteria

**Fail condition:** Ranges cannot be defined deterministically.

## 4. Entry Rules (MANDATORY)

The platform must support:

- Exact definition of “candle closes fully outside range”
- Wick handling rules
- “Next candle does NOT re-enter”:
  - Wick vs body logic configurable
- Entry timing control:
  - Open of following candle
  - Market vs limit selection
- Explicit slippage tolerance assumptions

**Fail condition:** Entry logic relies on discretionary confirmation.

## 5. Stop & Invalidation Logic (MANDATORY)

The platform must support:

- Stop placement at opposite side of range
- Optional pip buffer
- Invalidation rule: any candle close back inside range
- Immediate exit execution:
  - Market or limit
  - Max slippage constraint

**Fail condition:** Stops or invalidation cannot be enforced mechanically.

## 6. Position Sizing (MANDATORY)

The platform must support:

- Fixed risk % per trade (exact value)
- Equity-based sizing (not balance-only)
- Position size rounding rules
- Minimum lot enforcement
- Max exposure limits:
  - Per instrument
  - Per session

**Fail condition:** Risk sizing is approximate or broker-imposed only.

## 7. Profit Management (MANDATORY)

The platform must support quantified exit logic for:

- Momentum decay:
  - Two consecutive candles fail to extend
  - Full candle close against position
- New compression:
  - Candle overlap / range contraction metrics
- Exit execution type and timing control

**Fail condition:** Exits depend on manual judgment.

## 8. Trade Frequency Constraints (MANDATORY)

The platform must enforce:

- Unique Range ID tracking
- Max 1 trade per range
- Max 2 trades per session
- Session counter reset logic
- Explicit definition of “stopped out”

**Fail condition:** Trade frequency limits cannot be enforced programmatically.

## 9. No-Trade Filters (MANDATORY)

The platform must support pre-trade rejection if:

- Breakout candle size exceeds threshold relative to ATR or recent swing
- Spread widens beyond defined multiple
- Stop cannot be defined before entry

**Fail condition:** Platform cannot reject trades pre-execution.

## 10. Risk & Governance Constraints (MANDATORY)

The platform must enforce:

- No position scaling
- No averaging down
- No discretionary overrides
- Global kill-switch on:
  - Risk breach
  - Rule violation
- Explicit change control:
  - Rule versioning
  - Approval before activation

**Fail condition:** Rules can be overridden live.

## 11. Execution & Monitoring (MANDATORY)

The platform must support:

- Market, limit, and stop orders
- Slippage caps with reject/replace logic
- Mandatory logging of:
  - Trade rationale
  - Range ID
  - Strategy version
  - Rule version
- Centralized audit trail storage

**Fail condition:** Trades cannot be reconstructed post-hoc.

## 12. Testing & Validation (MANDATORY)

The platform must provide:

- Historical data sufficient for backtesting:
  - Session-aligned
  - Spread-aware
- Paper trading environment with identical execution rules
- Acceptance criteria:
  - 100% rule compliance
  - No manual intervention

**Fail condition:** Live behavior cannot be validated pre-deployment.

## Final Gating Rule (Non-Negotiable)

If any single item above is unsupported, the platform is rejected — not worked around.
