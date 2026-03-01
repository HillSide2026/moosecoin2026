---
id: 26-001-00001-DEPENDENCIES
title: Dependencies - Formalize Trading Strategy
owner: ML1
status: draft
created_date: 2026-02-06
last_updated: 2026-02-06
tags: [trading, strategy, dependencies]
---

# Dependencies

Dependency map, work breakdown, schedule, resource plan, and budget baseline.

---

## Upstream Dependencies

| # | Dependency | Type | Status | Impact if Delayed |
|---|------------|------|--------|-------------------|
| | None — this is the first project in the chain | | | |

## Downstream Impacts

| # | Project | Dependency Type | Notes |
|---|---------|-----------------|-------|
| 1 | 26-001-00002 (Trading Platform Selection) | Blocks | Cannot begin until this project reaches Closing |
| 2 | 26-001-00003 (Website Development) | Blocks | Cannot begin until this project reaches Closing |

## External Constraints

| # | Constraint | Source | Impact |
|---|------------|--------|--------|
| 1 | Historical price data availability | Market data vendors | Blocks backtesting phase |
| 2 | Execution venue order type support | Broker/exchange | Blocks live pilot |

---

## Work Breakdown Structure (WBS)

### 1. Strategy Formalization

- 1.1 Decompose discretionary logic into rules
- 1.2 Define valid market conditions
- 1.3 Define invalidation-based stops
- 1.4 Define target logic and R-multiples

### 2. Risk Engine

- 2.1 Encode risk limits
- 2.2 Exposure aggregation logic
- 2.3 Kill-switch and auto-stand-down
- 2.4 Risk audit tests

### 3. System Architecture

- 3.1 Signal module
- 3.2 Risk gate module
- 3.3 Execution module
- 3.4 Logging & audit module

### 4. Testing & Validation

- 4.1 Historical backtesting
- 4.2 Walk-forward testing
- 4.3 Paper trading
- 4.4 Failure-mode simulations

### 5. Deployment

- 5.1 Pilot configuration
- 5.2 Capital caps enforcement
- 5.3 Monitoring dashboards
- 5.4 Go/No-Go review

---

## Schedule / Roadmap

| Phase | Duration | Dependencies | Milestone |
|-------|----------|-------------|-----------|
| Strategy Formalization | 3 weeks | Initiation complete | Rule spec approved |
| Risk Engine Build | 2 weeks | Strategy rules | Risk engine locked |
| System Integration | 3 weeks | Risk engine | End-to-end system |
| Backtesting | 2 weeks | Integrated system | Backtest sign-off |
| Paper Trading | 4 weeks | Backtest approval | Forward-test sign-off |
| Live Pilot | 4 weeks | Paper success | Pilot review |

**Critical Path:** Strategy Formalization -> Risk Engine -> Integration -> Testing

---

## Resource Plan

| Role | Responsibility | Allocation | Constraints |
|------|---------------|------------|-------------|
| System Designer | Strategy logic | Part-time | Must avoid overfitting |
| Quant/Engineer | Implementation | Full-time | Code simplicity required |
| Risk Reviewer | Independent review | Part-time | Veto authority |
| Operator | Monitoring | Minimal | No trade control |

---

## Budget / Cost Baseline

### Cost Categories

- Engineering development
- Data acquisition
- Infrastructure (servers, execution)
- Testing & validation

### Baseline Estimate (Relative)

| Category | Allocation |
|----------|-----------|
| Development | 40% |
| Testing & Validation | 30% |
| Infrastructure | 20% |
| Contingency | 10% |

**Burn Rate Control:** Phase-gated release of budget tied to milestone approval.

---

*Note: Dependencies are expressed as project IDs, not folder paths. See PROJECT_SCHEMA.md section 10.*
