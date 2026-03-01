---
id: DOCTRINE-2026-005
title: Trading System Minimum Components
owner: ML1
status: approved
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [doctrine, trading, risk, execution]
effective_date: 2026-03-01
supersedes: null
provenance:
  decided_by: ML1
  decided_on: 2026-03-01
  context: Establishes the minimum required doctrinal components for the Trading System.
---

# Trading System Minimum Components

## Purpose

This doctrine defines the minimum component set that must be explicitly
defined and approved in `01_DOCTRINE` for the Trading System.

Trading System = ML2 + Execution Environment (third-party app(s)).

If any required component is missing, ambiguous, or unapproved, trading must
stand aside.

## Required Components

### 1. Strategy Invariants

The doctrine must define non-negotiable strategy truths, including:
- market and timeframe scope
- regime and eligibility boundaries
- invalidation conditions
- prohibited deviations from intent

### 2. Risk Constraints

The doctrine must define hard risk boundaries, including:
- maximum loss limits (per-trade, per-session/day, and aggregate where applicable)
- mandatory stop/invalidation behavior
- suspension or shutdown triggers
- explicitly prohibited risk behaviors

### 3. Position Sizing Logic

The doctrine must define deterministic sizing logic, including:
- sizing inputs (for example: risk budget, stop distance, instrument constraints)
- calculation method
- rounding and minimum/maximum size rules
- conditions where no valid size exists (and therefore no trade)

### 4. Capital Allocation Rules

The doctrine must define how capital is allocated and bounded, including:
- allocation buckets by strategy/account/instrument (as applicable)
- concentration and correlation limits
- concurrent exposure limits
- reallocation/rebalance rules and authority

### 5. Trading Procedures

The doctrine must define executable procedures, including:
- pre-trade checks and eligibility gates
- entry, management, and exit procedures
- exception and fail-safe handling
- post-trade recording and review obligations

## Precedence and Enforcement

- Doctrine is binding.
- Models and protocols may operationalize doctrine but may not weaken it.
- Execution Environment behavior must conform to doctrine.
- If doctrine and implementation conflict, doctrine prevails and execution must
  stop until resolved.

## Change Control

Changes to any required component are doctrinal changes and require explicit
ML1 approval.
