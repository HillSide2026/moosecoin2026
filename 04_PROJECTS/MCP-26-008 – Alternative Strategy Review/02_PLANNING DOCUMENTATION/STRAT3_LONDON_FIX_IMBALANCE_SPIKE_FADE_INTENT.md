---
id: 26-001-00008-STRAT3-INTENT
title: Strategy Intent - STRAT3 London Fix Imbalance Spike Fade
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, intent, philosophy, strat3]
---

# Strategy Intent Document

## Strategy ID

`STRAT3_LONDON_FIX_IMBALANCE_SPIKE_FADE`

## Core Thesis

Trade only statistically extreme imbalance spikes during the London 4PM Fix window, and only after the spike has completed.

Exit immediately if imbalance persists, and hold only while controlled reversion structure develops.

## Structural Inefficiency Exploited

- Fix-window flow can produce short-lived, non-equilibrium price extensions.
- The first post-spike stall can expose exhaustion rather than continuation.
- Bounded invalidation against spike extremes allows controlled reversion participation.

## Explicit Non-Goals

- Not anticipation of turning points before stall confirmation
- Not discretionary counter-trend trading
- Not all-session mean reversion
- Not frequency-seeking activity
- Not macro prediction

## Market Microstructure Assumption

- London fix flow can create rapid one-sided order imbalance near 16:00 London time.
- A subset of these moves is flow-driven and partially reversible once imbalance pressure exhausts.
- Structural validity degrades outside the event window or under macro contamination.

## Expected Behavioral Edge Source

- Conditional participation only after event completion and stall confirmation
- Strict no-trade behavior unless spike and regime conditions are both valid
- Fail-fast invalidation limits adverse persistence risk
- Time-bound holding period reduces exposure to post-event noise

## Known Failure Regimes

- Macro-driven directional expansion mistaken for fix imbalance
- Multi-stage trend expansion that does not represent exhaustion
- Spread/liquidity degradation that invalidates execution quality
- Regime ambiguity or missing data required for gate checks

## Drift Prevention Clauses

- Regime must be confirmed before signal evaluation
- Ambiguity defaults to no-trade
- No discretionary override path
- Any risk-increasing rule change requires explicit ML1 decision
