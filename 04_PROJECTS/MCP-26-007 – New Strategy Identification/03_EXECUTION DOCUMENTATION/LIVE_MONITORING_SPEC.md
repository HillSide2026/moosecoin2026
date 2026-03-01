---
id: 26-001-00007-LIVE-MONITORING-SPEC
title: Live Monitoring Specification - STRAT2
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, monitoring, performance, strat2]
---

# LIVE_MONITORING_SPEC

## Purpose

Define live monitoring expectations and intervention thresholds for STRAT2.

## Expected Behavior Bands

- Expected win rate range: ML1-defined target band
- Expected average R multiple: ML1-defined target band
- Expected trade frequency: low frequency, bounded by session constraints

## Risk and Suspension Thresholds

- Max drawdown threshold: ML1-defined hard limit
- Suspension threshold: any breach of defined tolerance band requiring review

## Trigger Conditions for Review

- Win rate persistently outside expected band
- Average R multiple persistently below tolerance
- Trade frequency drift inconsistent with regime design
- Drawdown exceeds threshold
- Repeated gate anomalies (spread/liquidity/assumption failures)

## Required Monitoring Outputs

- Daily summary snapshot
- Weekly variance report against expected bands
- Threshold breach events with timestamped evidence
- Decision required memo for ML1 when suspension trigger occurs
