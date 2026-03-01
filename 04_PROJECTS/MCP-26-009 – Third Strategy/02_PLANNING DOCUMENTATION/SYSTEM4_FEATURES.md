---
id: MCP-26-009-SYSTEM4-FEATURES
title: Feature Specification - SYSTEM4
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, features, quantitative, system4]
---

# SYSTEM4 Feature Specification

This document defines feature construction required for deterministic SYSTEM4
execution logic.

## 1. Compression Volatility Feature

### Definition

Measures whether pre-fix volatility is statistically compressed.

### Proposed Calculation

- Compute realized volatility for 15:15-15:45 window on 5m bars.
- Compare against 20-day intraday distribution for the same window.
- Emit percentile rank and compression-pass state.

### Output

- `compression_vol_percentile`: [0,100]
- `compression_vol_pass`: `true` or `false`

## 2. Sequential Contraction Feature

### Definition

Validates progressive contraction in recent candle ranges.

### Proposed Calculation

- Compute true range for last 4 bars.
- Validate strict or threshold-based monotonic contraction.

### Output

- `sequential_contraction_pass`: `true` or `false`
- `contraction_ratio`: float

## 3. Compression Range Integrity Feature

### Definition

Validates structural quality of micro-range.

### Proposed Calculation

- Compute compression high-low range.
- Validate minimum/maximum bounds:
  - `range_height >= 2 * spread`
  - `range_height <= 0.6 * avg_5m_swing_size`
- Count contained candles.

### Output

- `range_height`: float
- `contained_candle_count`: integer
- `range_integrity_pass`: `true` or `false`

## 4. Regime Computation

### Inputs

- Overlap volatility percentile feature
- Macro contamination feature
- Pre-fix directional expansion feature
- Compression features

### Logic

- If macro contamination true or pre-fix expansion >= 1.5x ATR -> `dislocated`
- Else if overlap volatility < dormant cutoff and no catalysts -> `dormant`
- Else if normal overlap volatility and compression criteria pass and no macro distortion -> `transitional`
- Else -> `dormant` (safety default)

### Output

- `regime_label`: `dormant`, `transitional`, or `dislocated`

## 5. Breakout Confirmation Feature

### Definition

Validates valid full-close break and non-reentry confirmation.

### Proposed Logic

- Check 5m full-candle close outside compression range within 15:55-16:10.
- Reject wick-only break.
- Confirm next candle does not fully re-enter compression range.

### Output

- `break_confirmed`: `true` or `false`
- `break_window_pass`: `true` or `false`
- `reentry_fail`: `true` or `false`

## 6. Spread and Liquidity Gate Feature

### Definition

Ensures execution quality is acceptable at trigger.

### Proposed Calculation

- Measure current spread and session median spread.
- Compute spread ratio.
- Gate-fail if ratio exceeds threshold.
- Include liquidity quality flag where available.

### Output

- `spread_ratio`: float
- `spread_gate_pass`: `true` or `false`
- `liquidity_gate_pass`: `true` or `false`

## 7. Momentum Decay Exit Feature

### Definition

Detects expansion failure and exit timing conditions.

### Proposed Logic

- Track extension candles in breakout direction.
- Mark decay if two consecutive candles fail to extend range.
- Mark decay if opposing close occurs.
- Mark decay if new micro-compression forms.
- Force exit at hard time stop (>= 16:25 London).

### Output

- `extension_fail_count`: integer
- `opposing_close_flag`: `true` or `false`
- `new_micro_compression_flag`: `true` or `false`
- `time_stop_hit`: `true` or `false`

## 8. Reproducibility and Logging Requirements

- All feature inputs/outputs and timestamps must be logged per decision cycle.
- Feature code version must be attached to each trade record.
- Missing required feature inputs force no-trade with explicit gate-fail reason.
