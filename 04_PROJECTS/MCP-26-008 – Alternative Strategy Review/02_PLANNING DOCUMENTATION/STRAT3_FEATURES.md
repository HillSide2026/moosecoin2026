---
id: 26-001-00008-STRAT3-FEATURES
title: Feature Specification - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, features, quantitative, strat3]
---

# STRAT3 Feature Specification

This document defines feature construction required for deterministic STRAT3 execution logic.

## 1. Imbalance Spike Feature

### Definition

Spike feature measures event-window expansion relative to normalized volatility.

### Proposed Calculation

- Compute ATR on 5m bars (configured lookback).
- Compute absolute move over 15:55-16:00 window.
- Calculate `spike_atr_multiple = fix_window_move / atr_5m`.
- Mark valid spike when multiple is between configured min/max bounds.

### Output

- `spike_atr_multiple`: float
- `spike_valid`: `true` or `false`
- `spike_direction`: `up` or `down`

## 2. Regime Computation

### Inputs

- Session/time-window feature
- Volatility state feature
- Macro contamination feature
- Spike feature

### Logic

- If macro contamination true or persistent directional expansion pre-fix -> `dislocated`
- Else if no abnormal volatility and fix move < 1x ATR -> `dormant`
- Else if stable pre-fix state and sudden 15:55-16:00 expansion and no contamination -> `transitional`
- Else -> `dormant` (safety default)

### Output

- `regime_label`: `dormant`, `transitional`, or `dislocated`

## 3. Stall Confirmation Feature

### Definition

Stall confirmation validates spike completion before fade entry.

### Proposed Logic

- Confirm full candle close after 16:00 that does not extend spike extreme.
- Confirm next candle fails to make new extreme.
- Confirm compression or opposing close.

### Output

- `stall_confirmed`: `true` or `false`
- `stall_reason_codes`: list

## 4. Macro Contamination Tagging

### Definition

Macro contamination flags event-driven conditions that invalidate reversion assumptions.

### Proposed Logic

- Use macro event feed with severity classification.
- If relevant medium/high severity event occurred in prior 60 minutes, set contamination true.
- If feed unavailable, default to no-trade and log missing input.

### Output

- `macro_contaminated`: `true` or `false`
- `macro_event_refs`: event identifiers/timestamps

## 5. Spread State Feature

### Definition

Spread state determines whether execution quality is acceptable for participation.

### Proposed Calculation

- Compute current spread at setup and trigger points.
- Compute session median spread baseline.
- Calculate `spread_ratio = current_spread / session_median_spread`.
- Gate fails when ratio exceeds configured threshold.

### Output

- `spread_ratio`: float
- `spread_gate_pass`: `true` or `false`

## 6. Retracement and Exit Features

### Definition

Exit features measure unwind progress and decay after entry.

### Proposed Calculations

- Compute retracement ratio from spike extreme toward pre-spike reference.
- Track consecutive non-advancing candles.
- Track hard time-stop condition (>= 16:20 London time).

### Output

- `retracement_ratio`: float
- `non_advance_count`: integer
- `time_stop_hit`: `true` or `false`

## 7. Reproducibility and Logging Requirements

- All feature inputs/outputs and timestamps must be logged per decision cycle.
- Feature code version must be attached to each trade record.
- Missing required feature input forces no-trade with explicit gate-fail reason.
