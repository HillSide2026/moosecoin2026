---
project:
  id: 26-001-00008
  title: Alternative Strategy Review
  stage: initiation
  status: in_progress
owner:
  ml1: ML1
created_date: 2026-03-01
last_updated: 2026-03-01
dependencies:
  depends_on: [26-001-00007]
  blocks: []
tags: [trading, strategy, review, alternative]
---

# Project Overview

## Governance

| Property | Value |
|----------|-------|
| Lifecycle Model | Standard 4-stage project lifecycle (minimum) |
| Authority | ML1 approves transitions between stages |
| Role of ML2 | System-of-record, structure, consistency, audit trail |

## Objective

Review and assess alternative strategy candidates against doctrine, risk, and implementation constraints before any formal promotion to modeling.

## Scope

### In Scope

- Define review criteria for alternative strategy candidates
- Evaluate candidate logic for regime clarity, risk coherence, and operational enforceability
- Produce ML1-ready recommendation on whether to advance a candidate to Planning

### Explicit Exclusions

- Live or paper trading
- Performance claims or profitability guarantees
- Doctrine edits and approvals
- Execution platform configuration

## Dependencies

| Dependency | Status | Impact |
|------------|--------|--------|
| 26-001-00007 (New Strategy Identification) | Active | Provides baseline context and prior candidate artifacts |

## Key Dates

| Date | Event |
|------|-------|
| 2026-03-01 | Project opened |
| 2026-03-01 | Strategy 3 candidate captured |
| | Initiation complete |
| | Planning complete |
| | Execution complete |
| | Project closed |

## Current Stage

**Stage 1: Initiation** — In Progress

## Status Summary

Initiation artifacts for alternative strategy review have been created and Strategy 3 has been captured as the active candidate for review.

Current candidate artifact:

- `01_INITIATION DOCUMENTATION/STRATEGY_3_CANDIDATE_LONDON_FIX_IMBALANCE_SPIKE_FADE.md`

Planning artifacts drafted for STRAT3:

- `02_PLANNING DOCUMENTATION/SCOPE_STATEMENT.md`
- `02_PLANNING DOCUMENTATION/RISK_REGISTER_FULL.md`
- `02_PLANNING DOCUMENTATION/CHANGE_CONTROL_PROCESS.md`
- `02_PLANNING DOCUMENTATION/STRAT3_LONDON_FIX_IMBALANCE_SPIKE_FADE_INTENT.md`
- `02_PLANNING DOCUMENTATION/STRAT3_LONDON_FIX_IMBALANCE_SPIKE_FADE_SPEC.md`
- `02_PLANNING DOCUMENTATION/STRAT3_PARAMETERS_v1.0.md`
- `02_PLANNING DOCUMENTATION/STRAT3_FEATURES.md`
- `02_PLANNING DOCUMENTATION/STRAT3_DECISION_FLOW_v1.0.drawio`

Execution artifacts pre-created for implementation readiness:

- `03_EXECUTION DOCUMENTATION/DECISION_LOG.md`
- `03_EXECUTION DOCUMENTATION/ISSUE_LOG.md`
- `03_EXECUTION DOCUMENTATION/CHANGE_REQUESTS_LOG.md`
- `03_EXECUTION DOCUMENTATION/RISK_REGISTER_UPDATED.md`
- `03_EXECUTION DOCUMENTATION/STATUS_REPORT.md`
- `03_EXECUTION DOCUMENTATION/RISK_ENGINE_SPEC.md`
- `03_EXECUTION DOCUMENTATION/CHANGE_LOG.md`
- `03_EXECUTION DOCUMENTATION/ASSUMPTION_REGISTER.md`
- `03_EXECUTION DOCUMENTATION/STRAT3_EXECUTION_PLAYBOOK.md`
- `03_EXECUTION DOCUMENTATION/TRADE_LOG_SCHEMA.md`
- `03_EXECUTION DOCUMENTATION/BACKTEST_PROTOCOL_v1.md`
- `03_EXECUTION DOCUMENTATION/LIVE_MONITORING_SPEC.md`

Planning stage remains open pending ML1 gate decision.
