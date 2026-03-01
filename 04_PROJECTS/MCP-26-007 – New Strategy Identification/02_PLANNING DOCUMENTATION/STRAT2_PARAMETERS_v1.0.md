---
id: 26-001-00007-STRAT2-PARAMETERS
title: Parameter Definition Sheet - STRAT2 v1.0
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, parameters, quantitative, strat2]
---

# STRAT2 Parameters v1.0

Each parameter includes rationale, sensitivity expectation, and risk impact class.

## Parameter Table

| Parameter | Proposed Value | Rationale | Sensitivity Expectation | Risk Impact Classification |
|----------|----------------|-----------|--------------------------|----------------------------|
| ATR lookback | 14 bars (5m) | Stable short-horizon volatility baseline for breakout context | Medium sensitivity; shorter lookback reacts faster but increases noise | High |
| Volatility percentile window | 20 trading days | Sufficient sample for session-relative state classification | Medium sensitivity; too short distorts dormant/dislocated boundaries | High |
| Dormant cutoff percentile | 30th percentile | Separates low-energy overlap states from tradable transitions | High sensitivity around boundary conditions | High |
| Dislocated expansion threshold | >= 1.5x ATR | Flags directional shock states likely to degrade execution quality | High sensitivity; lower values over-filter, higher values under-filter | High |
| Macro contamination lookback | 60 minutes | Captures recent event-shock spillover into setup window | Medium sensitivity | High |
| Spread degradation threshold | > 1.5x median overlap spread | Blocks structurally expensive/unstable trigger conditions | Medium sensitivity | High |
| Range minimum height | >= 2x spread | Prevents micro-noise structures from qualifying as valid balance | High sensitivity in low-volatility sessions | Medium |
| Range max height reference | <= average of last 10 swings | Prevents oversized "ranges" that are already unstable expansions | Medium sensitivity | Medium |
| Minimum contained candles | 6 candles | Requires meaningful balance before breakout validation | Low-medium sensitivity | Medium |
| Failed break attempts per side | 2 attempts | Confirms boundary testing before expansion | Medium sensitivity | Medium |
| Max trades per range | 1 | Enforces non-churn behavior and prevents repeated structural overexposure | Low sensitivity | High |
| Max trades per session | 2 | Caps activity and drawdown clustering in single session | Low sensitivity | High |
| Fixed risk per trade | 0.25%-0.50% equity | Ensures bounded downside during fail-fast behavior | High sensitivity; direct impact on loss profile | Critical |

## Parameter Governance Notes

- Parameters are not justified by backtest-only arguments.
- Parameter changes require explicit change control and ML1 approval.
- Any parameter that weakens risk constraints is treated as a high-severity change.
