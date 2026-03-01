---
id: 26-001-00007-TEMPLATE-COMPLIANCE
title: Template Compliance Checklist
owner: ML1
status: active
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [compliance, templates]
---

# Template Compliance Checklist

## Initiation (Mandatory)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Project Charter | Yes | Yes | `01_INITIATION DOCUMENTATION/PROJECT_CHARTER.md` | |
| Business Case / Rationale | Yes | Yes | `01_INITIATION DOCUMENTATION/BUSINESS_CASE.md` | |
| High-Level Requirements Summary | Yes | Yes | `01_INITIATION DOCUMENTATION/HIGH_LEVEL_REQUIREMENTS_SUMMARY.md` | |
| Initial Risk Register (Lite) | Yes | Yes | `01_INITIATION DOCUMENTATION/INITIAL_RISK_REGISTER_LITE.md` | |

## Planning (Mandatory)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Scope Statement | Yes | Yes | `02_PLANNING DOCUMENTATION/SCOPE_STATEMENT.md` | |
| Risk Register (Full) | Yes | Yes | `02_PLANNING DOCUMENTATION/RISK_REGISTER_FULL.md` | |
| Change Control Process | Yes | Yes | `02_PLANNING DOCUMENTATION/CHANGE_CONTROL_PROCESS.md` | |

## Planning (Project-Specific)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Strategy Formalization Plan | Yes | Yes | `02_PLANNING DOCUMENTATION/STRATEGY_FORMALIZATION_PLAN.md` | Strategy-formalization specific |
| Regime Definition Specification | Yes | Yes | `02_PLANNING DOCUMENTATION/REGIME_DEFINITION_SPEC.md` | Strategy-formalization specific |
| Candidate Evaluation Matrix | Yes | Yes | `02_PLANNING DOCUMENTATION/CANDIDATE_EVALUATION_MATRIX.md` | Strategy-formalization specific |
| Validation Plan | Yes | Yes | `02_PLANNING DOCUMENTATION/VALIDATION_PLAN.md` | Strategy-formalization specific |

## Planning (Layered Strategy Formalization)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Strategy Intent Document | Yes | Yes | `02_PLANNING DOCUMENTATION/STRAT2_LONDON_FIX_BREAKOUT_HOLD_INTENT.md` | Intent and philosophy layer |
| Design Principles Reference | Yes | Yes | `02_PLANNING DOCUMENTATION/TRADING_PRINCIPLES.md` | Shared principles |
| Strategy Specification Document | Yes | Yes | `02_PLANNING DOCUMENTATION/STRAT2_LONDON_FIX_BREAKOUT_HOLD_SPEC.md` | Structural specification layer |
| Decision Tree Diagram | Yes | Yes | `02_PLANNING DOCUMENTATION/STRAT2_DECISION_FLOW_v1.0.drawio` | Regime -> Risk -> Setup -> Entry -> Exit -> Audit |
| Parameter Definition Sheet | Yes | Yes | `02_PLANNING DOCUMENTATION/STRAT2_PARAMETERS_v1.0.md` | Quantitative definition layer |
| Feature Specification Document | Yes | Yes | `02_PLANNING DOCUMENTATION/STRAT2_FEATURES.md` | Quantitative definition layer |

## Execution (Mandatory)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Decision Log | Yes | Yes | `03_EXECUTION DOCUMENTATION/DECISION_LOG.md` | Pre-created for implementation stage |
| Issue Log | Yes | Yes | `03_EXECUTION DOCUMENTATION/ISSUE_LOG.md` | Pre-created for implementation stage |
| Change Requests Log | Yes | Yes | `03_EXECUTION DOCUMENTATION/CHANGE_REQUESTS_LOG.md` | Pre-created for implementation stage |
| Risk Register (Updated) | Yes | Yes | `03_EXECUTION DOCUMENTATION/RISK_REGISTER_UPDATED.md` | Pre-created for implementation stage |
| Status Report | Yes | Yes | `03_EXECUTION DOCUMENTATION/STATUS_REPORT.md` | Pre-created for implementation stage |

## Execution (Risk and Governance Layer)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Risk Model Specification | Yes | Yes | `03_EXECUTION DOCUMENTATION/RISK_ENGINE_SPEC.md` | Required for implementation stage |
| Change Control Log | Yes | Yes | `03_EXECUTION DOCUMENTATION/CHANGE_LOG.md` | No silent modifications |
| Assumption Register | Yes | Yes | `03_EXECUTION DOCUMENTATION/ASSUMPTION_REGISTER.md` | Assumption failure -> suspension |

## Execution (Operations Layer)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Operational Playbook | Yes | Yes | `03_EXECUTION DOCUMENTATION/STRAT2_EXECUTION_PLAYBOOK.md` | Required for implementation stage |
| Trade Log Schema | Yes | Yes | `03_EXECUTION DOCUMENTATION/TRADE_LOG_SCHEMA.md` | Auditability requirement |

## Execution (Validation and Monitoring Layer)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Backtest Protocol Document | Yes | Yes | `03_EXECUTION DOCUMENTATION/BACKTEST_PROTOCOL_v1.md` | No backtest without protocol |
| Performance Monitoring Framework | Yes | Yes | `03_EXECUTION DOCUMENTATION/LIVE_MONITORING_SPEC.md` | Live deviation triggers review |

## Closure (Mandatory)

| Document | Required | Present | Location | Notes |
|----------|----------|---------|----------|-------|
| Final Deliverables Acceptance Record | Yes | No | | Not started |
| Project Closure Report | Yes | No | | Not started |
| Lessons Learned / Retrospective | Yes | No | | Not started |
| Archive Index | Yes | No | | Not started |
