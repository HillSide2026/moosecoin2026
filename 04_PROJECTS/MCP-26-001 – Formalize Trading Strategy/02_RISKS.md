---
id: 26-001-00001-RISKS
title: Risks - Formalize Trading Strategy
owner: ML1
status: draft
created_date: 2026-02-06
last_updated: 2026-02-06
tags: [trading, strategy, risks]
---

# Risks

Risk and assumptions register with mitigations.

---

## Active Risks

| # | Category | Subcategory | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|---|----------|-------------|------|------------|--------|------------|-------|--------|
| R-001 | Strategic |  | Logic Overfitting | Medium | High | Simplicity bias, walk-forward tests | Designer | Open |
| R-002 | Operational | Scope | Risk Rule Bypass | Low | Critical | Hard-coded veto logic | Engineer | Open |
| R-003 | Strategic |  | Regime Shift | Medium | Medium | Conservative sizing, kill-switch | Risk | Open |
| R-004 | Operational | Schedule | Data Errors | Medium | High | Multi-source validation | Engineer | Open |
| R-005 | Operational | Schedule | Execution Drift | Medium | Medium | Conservative slippage assumptions | Engineer | Open |
| R-006 | Operational | Scope | Scope Creep | High | High | Strict change control | Sponsor | Open |
| R-007 | Operational | Budget | Early Success Bias | Medium | High | Scale-up caps | Risk | Open |

## Assumptions Requiring Validation

| # | Assumption | Validation Method | Status |
|---|------------|-------------------|--------|
| A-001 | Reliable historical price data is available | Source evaluation during execution | Pending |
| A-002 | Execution venue supports required order types | Platform selection (26-001-00002) | Pending |
| A-003 | Capital owner accepts low trade frequency | ML1 confirmation | Pending |
| A-004 | Standing aside is an acceptable outcome | ML1 confirmation | Pending |

## Constraints (Non-Negotiable)

| # | Constraint | Source |
|---|------------|--------|
| C-001 | Hard risk limits (per-trade, daily, weekly) | Scope Statement |
| C-002 | No averaging down or position scaling | Scope Statement |
| C-003 | Crypto exposure flat by session end | Scope Statement |
| C-004 | Single active strategy instance per account | Scope Statement |

## Retired Risks

| # | Risk | Resolution | Date |
|---|------|------------|------|
| | | | |

---

*Note: Risks are project-specific assessments. They do not constitute doctrine or systemic guidance.*
