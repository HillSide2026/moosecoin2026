---
id: 26-001-00008-BACKTEST-PROTOCOL-V1
title: Backtest Protocol v1 - STRAT3
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [execution, validation, backtest, protocol, strat3]
---

# BACKTEST_PROTOCOL_v1

No backtest is valid without this protocol.

## 1. Data Windows

- In-sample period: define before test run
- Out-of-sample period: define before test run
- No overlap between in-sample and out-of-sample windows
- Session slicing must preserve fix-event window behavior

## 2. Transaction Cost Modeling

- Include spread costs by instrument and fix-window context
- Include commission assumptions where applicable
- Include slippage assumptions in all scenario runs

## 3. Slippage Assumption

- Baseline slippage parameter must be explicit
- Stress scenario uses adverse slippage multiplier
- Include event-window stress scenario for fix spikes

## 4. Walk-Forward Method

- Use fixed walk-forward segmentation
- Recompute parameters only at designated rebalance points
- Evaluate each segment independently before aggregation

## 5. Monte Carlo Requirement

- Monte Carlo perturbation of trade order and slippage
- Report distribution of drawdown and expectancy outcomes

## 6. Minimum Trade Count Threshold

- Define minimum count threshold before accepting statistical interpretation
- If threshold not met, result is informational only, not confirmatory

## 7. Reporting Output

- Protocol version
- Data windows used
- Cost/slippage assumptions
- Walk-forward results
- Monte Carlo summary
- Threshold compliance status
