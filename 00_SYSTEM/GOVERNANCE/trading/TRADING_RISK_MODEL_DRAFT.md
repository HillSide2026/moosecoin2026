---
id: GOV-2026-00Y
title: Trading Risk Model (Draft)
owner: ML1
status: draft
created_date: 2026-02-10
last_updated: 2026-02-10
effective_date: 2026-02-10
tags: [trading, governance, risk, model]
provenance:
  decided_by: ML1
  decided_on: 2026-02-10
  context: Draft risk model for trading strategy governance
---

# Trading Risk Model (Draft)

## Purpose
Define the risk framework that governs trading strategy participation and exposure.

## Scope
**In Scope**
- Risk classes and limits
- Position sizing constraints
- Drawdown and exposure limits
- Correlation and concentration controls

**Out of Scope**
- Execution logic or platform implementation
- Instrument selection (strategy-level)

## Risk Classes (Draft)
- **Low Risk** — conservative exposure; narrow participation
- **Medium Risk** — standard exposure within limits
- **High Risk** — requires explicit ML1 approval per decision

## Core Constraints (Draft)
- Maximum loss per trade
- Maximum daily loss
- Maximum weekly loss
- Max concurrent positions
- Max correlated exposure

## Position Sizing (Draft)
- Risk per trade as fixed % of capital
- No averaging down
- No scaling without explicit approval

## Risk Triggers
- Breach of any limit triggers immediate halt and review
- Repeated near‑breaches require ML1 review

## Traceability Requirements
- Risk limits must be expressed as rule IDs
- All exceptions require ML1 approval and documented rationale

## Open Questions (for ML1)
1. What are the initial numeric limits for each risk class?
2. Should risk classes be strategy‑specific or global?
