---
id: 26-001-00007-STRAT2-FEATURES
title: Feature Specification - STRAT2
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, features, quantitative, strat2]
---

# STRAT2 Feature Specification

This document defines feature construction required for deterministic STRAT2 execution logic.

## 1. Compression Feature

### Definition

Compression quantifies reduced directional and range activity prior to a potential transition.

### Proposed Calculation

- Compute rolling true-range percentile over overlap session bars.
- Compute rolling body-size percentile over same window.
- Mark compression state when both are below configured thresholds.

### Output

- `compression_state`: `true` or `false`
- `compression_score`: normalized [0,1]

## 2. Regime Computation

### Inputs

- Volatility percentile feature
- ATR expansion feature
- Compression feature
- Macro contamination feature

### Logic

- If macro contamination true OR expansion >= dislocation threshold -> `dislocated`
- Else if volatility percentile below dormant threshold AND no expansion -> `dormant`
- Else if compression true AND expansion pressure present AND no contamination -> `transitional`
- Else -> `dormant` (safety default)

### Output

- `regime_label`: `dormant`, `transitional`, or `dislocated`
- `regime_confidence`: optional score for diagnostics (not discretionary override)

## 3. Macro Contamination Tagging

### Definition

Macro contamination flags recent event-driven conditions that invalidate structural setups.

### Proposed Logic

- Use macro event feed with severity tags.
- If medium/high event occurred within prior 60 minutes for relevant currency pair, set contamination true.
- If feed unavailable, contamination state defaults to true for safety OR strategy defaults to no-trade (final decision pending).

### Output

- `macro_contaminated`: `true` or `false`
- `macro_event_ref`: event identifier/timestamp list

## 4. Volatility Percentile Computation

### Definition

Volatility percentile measures current overlap volatility relative to a rolling historical baseline.

### Proposed Calculation

- Calculate session-normalized volatility metric (for example: rolling ATR or realized range) on 5m bars.
- Evaluate current value against 20-day historical distribution for same session context.
- Emit percentile rank.

### Output

- `vol_percentile_20d`: [0,100]

## 5. Reproducibility and Logging Requirements

- Feature inputs, outputs, and timestamps must be logged for each decision cycle.
- Feature code version must be attached to each run/trade record.
- Any missing feature input forces no-trade behavior and logs a gate-fail reason.
