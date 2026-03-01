---
id: 26-001-00008-TRADE-LOG-SCHEMA
title: Trade Log Schema - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, schema, audit, strat3]
---

# TRADE_LOG_SCHEMA

Each trade record must capture the following fields for auditability.

## Required Fields

- `strategy_id`
- `strategy_version`
- `regime_classification`
- `spike_metrics`
- `stall_confirmation_state`
- `entry_timestamp`
- `stop_distance`
- `spread_at_entry`
- `exit_trigger_type`
- `slippage`
- `screenshot_reference` (optional)

## Example Record Shape

```yaml
trade_id: TRD-YYYYMMDD-###
strategy_id: STRAT3_LONDON_FIX_IMBALANCE_SPIKE_FADE
strategy_version: v1.0
regime_classification: transitional
spike_metrics:
  atr_multiple: 2.1
  event_window: 15:55-16:00
  range_violation: true
stall_confirmation_state:
  post_1600_non_extension: true
  no_new_extreme_next_candle: true
  compression_or_opposing_close: true
entry_timestamp: YYYY-MM-DDTHH:MM:SSZ
stop_distance_pips: 7.4
spread_at_entry_pips: 0.8
exit_trigger_type: spike_breach | retracement_band | momentum_stall | time_stop | risk_killswitch
slippage_pips: 0.2
screenshot_reference: null
```

## Logging Rules

- Missing required fields invalidate audit completeness.
- Trade record must be version-locked to strategy/model logic in effect at entry.
