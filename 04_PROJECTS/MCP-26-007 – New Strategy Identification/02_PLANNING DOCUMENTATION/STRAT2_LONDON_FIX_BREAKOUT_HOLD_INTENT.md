---
id: 26-001-00007-STRAT2-INTENT
title: Strategy Intent - STRAT2 London Fix Breakout-and-Hold
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, intent, philosophy, strat2]
---

# Strategy Intent Document

## Strategy ID

`STRAT2_LONDON_FIX_BREAKOUT_HOLD`

## Core Thesis

Trade only the first sustained breakout from a valid pre-fix balance range formed during London + New York overlap.

Exit immediately on structural failure (return to balance), and hold only while post-break momentum persists.

## Structural Inefficiency Exploited

- Transitional flow from balance to imbalance during overlap liquidity
- Early directional expansion after failed range-containment attempts
- Asymmetry between tightly-defined invalidation and open-ended continuation

## Explicit Non-Goals

- Not a volatility-harvesting strategy
- Not a fade/reversion strategy
- Not a predictive macro strategy
- Not a high-frequency activity strategy
- Not an optimization-first strategy

## Market Microstructure Assumption

- London + New York overlap concentrates executable liquidity and directional participation.
- Pre-fix balance zones can produce clean structural boundaries.
- Breakout validity degrades materially outside overlap session quality.

## Expected Behavioral Edge Source

- Conditional participation only in transitional regimes
- Strict no-trade behavior in dormant/dislocated conditions
- Deterministic setup and invalidation reduces behavioral drift
- Small accepted losses and selective continuation exposure

## Known Failure Regimes

- Dislocated macro impulse regimes with unstable execution quality
- False expansion events with rapid reversion into balance
- Slanted/noisy ranges where structural boundaries are not objective
- Spread and liquidity degradation at trigger point

## Drift Prevention Clauses

- Any ambiguity defaults to no-trade
- Any untestable rule is considered invalid for implementation
- Any change that increases discretion requires explicit ML1 decision
