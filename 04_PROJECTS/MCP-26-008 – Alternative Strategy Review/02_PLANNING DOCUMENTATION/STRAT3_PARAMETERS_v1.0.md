---
id: 26-001-00008-STRAT3-PARAMETERS
title: Parameter Definition Sheet - STRAT3 v1.0
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, parameters, quantitative, strat3]
---

# STRAT3 Parameters v1.0

Each parameter includes rationale, sensitivity expectation, and risk impact class.

## Parameter Table

| Parameter | Proposed Value | Rationale | Sensitivity Expectation | Risk Impact Classification |
|----------|----------------|-----------|--------------------------|----------------------------|
| ATR lookback | 14 bars (5m) | Stable event-relative volatility baseline for spike normalization | Medium sensitivity; shorter windows increase noise | High |
| Spike magnitude minimum | >= 1.8x ATR | Excludes ordinary fix noise and requires statistical extremity | High sensitivity near threshold | High |
| Spike magnitude maximum | <= 2.5x ATR | Excludes runaway events likely to reflect dislocation | High sensitivity; too low over-filters | High |
| Spike formation duration | 1 to 2 candles | Forces sharp imbalance profile rather than gradual drift | Medium sensitivity | Medium |
| Regime event window | 15:55-16:00 London | Localizes regime trigger to fix expansion period | Low sensitivity | High |
| Tradable session window | 15:55-16:10 London | Keeps strategy bound to fix-event structure | Low sensitivity | High |
| Hard time stop | 16:20 London | Prevents prolonged exposure after event decay | Low sensitivity | High |
| Macro contamination lookback | 60 minutes | Avoids event overlap with macro shock flow | Medium sensitivity | High |
| Spread degradation threshold | > 2x session median spread | Blocks degraded execution conditions | Medium sensitivity | High |
| Max risk per trade | 0.25% to 0.50% equity | Bounded downside under fail-fast architecture | High sensitivity; direct P/L risk control | Critical |
| Max trades per event | 1 | Prevents churn and repeated fade attempts | Low sensitivity | High |
| Max fix trades per day | 1 | Caps concentration in single event regime | Low sensitivity | High |
| Retracement exit band | 50% to 70% of spike | Captures structural unwind without target overfitting | Medium sensitivity | Medium |
| Stall exit condition | 2 non-advancing candles | Exits when unwind momentum decays | Medium sensitivity | Medium |

## Parameter Governance Notes

- Parameters are not justified by backtest-only arguments.
- Parameter changes require change control and ML1 approval.
- Any parameter change that weakens risk constraints is high severity by default.
