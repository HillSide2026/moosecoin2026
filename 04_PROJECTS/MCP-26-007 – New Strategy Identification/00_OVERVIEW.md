---
project:
  id: 26-001-00007
  title: New Strategy Identification
  stage: planning
  status: in_progress
owner:
  ml1: ML1
created_date: 2026-03-01
last_updated: 2026-03-01
dependencies:
  depends_on: []
  blocks: []
tags: [trading, strategy, discovery, planning]
---

# Project Overview

## Governance

| Property | Value |
|----------|-------|
| Lifecycle Model | Standard 4-stage project lifecycle (minimum) |
| Authority | ML1 approves transitions between stages |
| Role of ML2 | System-of-record, structure, consistency, audit trail |

## Objective

Identify and define a new strategy candidate that can replace archived Strategy 1 and satisfy ML2 governance requirements.

## Scope

### In Scope

- Define strategy search space and exclusions
- Generate strategy candidates with explicit hypotheses
- Define evaluation criteria for regime fit, risk profile, and auditability
- Select one primary candidate for deeper modeling in `02_MODELS/`

### Explicit Exclusions

- Live trading or capital deployment
- Platform optimization and execution engineering
- Doctrine approval or canon promotion

## Dependencies

| Dependency | Status | Impact |
|------------|--------|--------|
| None | n/a | Project can proceed immediately |

## Key Dates

| Date | Event |
|------|-------|
| 2026-03-01 | Project opened |
| 2026-03-01 | Initiation complete |
| | Planning complete |
| | Execution complete |
| | Project closed |

## Current Stage

**Stage 2: Planning** — In Progress

## Status Summary

Project advanced to Planning with initial candidate defined and planning baseline artifacts created.

Current candidate artifact:

- `01_INITIATION DOCUMENTATION/STRATEGY_2_CANDIDATE_LONDON_FIX_BREAKOUT_AND_HOLD.md`

Planning artifacts:

- `02_PLANNING DOCUMENTATION/SCOPE_STATEMENT.md`
- `02_PLANNING DOCUMENTATION/RISK_REGISTER_FULL.md`
- `02_PLANNING DOCUMENTATION/CHANGE_CONTROL_PROCESS.md`
- `02_PLANNING DOCUMENTATION/STRATEGY_FORMALIZATION_PLAN.md`
- `02_PLANNING DOCUMENTATION/REGIME_DEFINITION_SPEC.md`
- `02_PLANNING DOCUMENTATION/CANDIDATE_EVALUATION_MATRIX.md`
- `02_PLANNING DOCUMENTATION/VALIDATION_PLAN.md`
- `02_PLANNING DOCUMENTATION/STRAT2_LONDON_FIX_BREAKOUT_HOLD_INTENT.md`
- `02_PLANNING DOCUMENTATION/TRADING_PRINCIPLES.md`
- `02_PLANNING DOCUMENTATION/STRAT2_LONDON_FIX_BREAKOUT_HOLD_SPEC.md`
- `02_PLANNING DOCUMENTATION/STRAT2_DECISION_FLOW_v1.0.drawio`
- `02_PLANNING DOCUMENTATION/STRAT2_PARAMETERS_v1.0.md`
- `02_PLANNING DOCUMENTATION/STRAT2_FEATURES.md`

Execution-stage artifacts (pre-created for implementation readiness):

- `03_EXECUTION DOCUMENTATION/DECISION_LOG.md`
- `03_EXECUTION DOCUMENTATION/ISSUE_LOG.md`
- `03_EXECUTION DOCUMENTATION/CHANGE_REQUESTS_LOG.md`
- `03_EXECUTION DOCUMENTATION/RISK_REGISTER_UPDATED.md`
- `03_EXECUTION DOCUMENTATION/STATUS_REPORT.md`
- `03_EXECUTION DOCUMENTATION/RISK_ENGINE_SPEC.md`
- `03_EXECUTION DOCUMENTATION/CHANGE_LOG.md`
- `03_EXECUTION DOCUMENTATION/ASSUMPTION_REGISTER.md`
- `03_EXECUTION DOCUMENTATION/STRAT2_EXECUTION_PLAYBOOK.md`
- `03_EXECUTION DOCUMENTATION/TRADE_LOG_SCHEMA.md`
- `03_EXECUTION DOCUMENTATION/BACKTEST_PROTOCOL_v1.md`
- `03_EXECUTION DOCUMENTATION/LIVE_MONITORING_SPEC.md`
