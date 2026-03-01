---
id: 26-001-00007-TRADE-LOG-SCHEMA
title: Trade Log Schema - STRAT2
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, schema, audit, strat2]
---

# TRADE_LOG_SCHEMA

Each trade record must capture the following fields for auditability.

## Required Fields

- `strategy_id`
- `strategy_version`
- `regime_classification`
- `setup_metrics`
- `entry_timestamp`
- `stop_distance`
- `spread_at_entry`
- `exit_trigger_type`
- `slippage`
- `screenshot_reference` (optional)

## Example Record Shape

```yaml
trade_id: TRD-YYYYMMDD-###
strategy_id: STRAT2_LONDON_FIX_BREAKOUT_HOLD
strategy_version: v1.0
regime_classification: transitional
setup_metrics:
  range_height_pips: 12.5
  contained_candles: 7
  failed_break_attempts_per_side: 2
entry_timestamp: YYYY-MM-DDTHH:MM:SSZ
stop_distance_pips: 8.2
spread_at_entry_pips: 0.7
exit_trigger_type: fail_fast_reentry | momentum_decay | session_cutoff | risk_killswitch
slippage_pips: 0.3
screenshot_reference: null
```

## Logging Rules

- Missing required fields invalidate audit completeness.
- Trade record must be version-locked to strategy/model logic in effect at entry.
