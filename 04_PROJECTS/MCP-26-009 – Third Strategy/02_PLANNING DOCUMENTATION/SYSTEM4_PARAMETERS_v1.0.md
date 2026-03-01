---
id: MCP-26-009-SYSTEM4-PARAMETERS
title: Parameter Definition Sheet - SYSTEM4 v1.0
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, parameters, quantitative, system4]
---

# SYSTEM4 Parameters v1.0

Each parameter includes rationale, sensitivity expectation, and risk impact
class.

## Parameter Table

| Parameter | Proposed Value | Rationale | Sensitivity Expectation | Risk Impact Classification |
|----------|----------------|-----------|--------------------------|----------------------------|
| ATR lookback | 14 bars (5m) | Stable short-horizon volatility baseline | Medium sensitivity | High |
| Dormant volatility cutoff | 20-day 30th percentile | Filters dead overlap sessions | High sensitivity near boundary | High |
| Compression volatility cutoff | 20-day intraday 25th percentile (15:15-15:45) | Ensures statistically abnormal compression | High sensitivity | High |
| Sequential contraction length | Last 4 candles contracting | Enforces directional compression quality | Medium sensitivity | Medium |
| Min contained candles | 6 candles | Requires coherent micro-range | Medium sensitivity | Medium |
| Compression range minimum | >= 2x spread | Excludes micro-noise structures | High sensitivity | Medium |
| Compression range maximum | <= 60% avg 5m swing size | Excludes already-expanded structures | Medium sensitivity | Medium |
| Breakout window | 15:55-16:10 London | Anchors transition to fix structure | Low sensitivity | High |
| Macro contamination lookback | 60 minutes | Excludes dislocated macro conditions | Medium sensitivity | High |
| Macro event forward filter | Scheduled event within 30 minutes -> no-trade | Avoids event collision risk | Low sensitivity | High |
| Break exhaustion filter | Break candle <= 2.5x compression height | Avoids exhaustion break chase | Medium sensitivity | High |
| Spread degradation threshold | <= 2x session median spread at trigger | Preserves execution quality | Medium sensitivity | High |
| Fixed risk per trade | 0.25% to 0.50% equity | Bounded downside per setup | High sensitivity; direct P/L impact | Critical |
| Max trades per structure | 1 | Prevents churn on same setup | Low sensitivity | High |
| Max trades per session | 2 | Caps session concentration risk | Low sensitivity | High |
| Hard time stop | 16:25 London | Prevents late-session decay exposure | Low sensitivity | High |

## Parameter Governance Notes

- Parameters are not justified by backtest-only arguments.
- Parameter changes require change control and ML1 approval.
- Any parameter change that weakens risk constraints is high severity by
  default.
