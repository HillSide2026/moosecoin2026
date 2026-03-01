---
project:
  id: 26-001-00002
  title: MooseCoin - Selecting and Implementing Trading Platform
  stage: execution
  status: in_progress
owner:
  ml1: ML1
created_date: 2026-02-03
last_updated: 2026-02-08
dependencies:
  depends_on: [26-001-00001]
  blocks: [26-001-00003]
tags: [trading, platform, implementation]
---

# Project Overview

## Governance

| Property | Value |
|----------|-------|
| Lifecycle Model | Standard 4-stage project lifecycle (minimum) |
| Authority | ML1 approves transitions between stages |
| Role of ML2 | System-of-record, structure, consistency, audit trail |

## Project Charter (Initiation)

**Project ID:** 26-001-00002  
**Project Name:** Trading Platform Selection & Implementation  
**Owner:** ML1  

### Purpose

Select and implement a trading platform that can mechanically and verifiably enforce the approved MooseCoin trading strategy, as defined in:

- Layer 1 — Governance & Risk Doctrine
- Layer 2 — Strategy Principles and Platform Gating Checklist

This project exists to ensure strategy fidelity, not convenience or speed.

### Scope (Explicit)

**In Scope**

- Evaluation of candidate trading platforms against the platform gating checklist
- Disqualification of platforms that fail any mandatory requirement
- Selection of a compliant platform
- Configuration planning consistent with strategy constraints
- Validation of enforcement, logging, and auditability

**Out of Scope**

- Defining or modifying trading strategy
- Designing or optimizing setups
- Live trading or capital deployment
- Broker or venue selection beyond platform compatibility
- Public or external communications

### Authority & Decision Rights

- Final authority: ML1
- No platform may be selected or configured without explicit ML1 approval
- No exceptions, overrides, or workaround approvals permitted

### Success Criteria (Initiation-Level)

The project is considered viable if:

- At least one candidate platform can, in principle, satisfy 100% of the gating checklist
- Platform selection decisions are binary (pass/fail), not comparative “best fit”
- No strategy compromises are required to fit tooling

### Current Status

Open — Initiation Stage (Active)

## Business Case / Rationale

### Why This Project Exists

The trading strategy is explicitly rule-bound, regime-aware, and risk-first. A trading platform that cannot enforce these constraints would:

- Introduce hidden discretion
- Distort strategy behavior
- Create un-auditable risk

Therefore, platform selection is a strategic risk-control decision, not an IT choice.

### Why Now

- Layer 2 strategy content is sufficiently defined to derive non-negotiable platform requirements
- Proceeding now prevents downstream rework and tool-driven strategy drift

### Expected Value

- Elimination of incompatible platforms early
- Reduction of operational and execution risk
- Faster transition to testing once a platform is approved
- Clear separation between strategy intent and tool capability

## Constraints

- Must not force strategy drift
- Must support required instruments, execution speed, and controls

## Key Dates

| Date | Event |
|------|-------|
| 2026-02-03 | Project opened |
| | Initiation complete |
| | Planning complete |
| | Execution complete |
| | Project closed |

## Current Stage

**Stage 2: Planning** — Complete (2026-02-08)

**Stage 3: Execution** — In Progress

## Dependencies

| Dependency | Status | Impact |
|------------|--------|--------|
| 26-001-00001 (Trading Strategy) | In Progress | Must complete before this project can proceed to Closing |

## Downstream Projects

- 26-001-00003 (Website Development) — blocked until Closing

## Status Summary

Initiation and Planning complete. Execution in progress.

## High-Level Requirements Summary (Initiation)

A platform may proceed beyond Initiation only if it satisfies **all** requirements below. The authoritative source for detailed requirements is:

- `04_PROJECTS/MCP-26-001 – Formalize Trading Strategy/03_EXECUTION DOCUMENTATION/PLATFORM_REQUIREMENTS_GATING_CHECKLIST.md`

**Testable Requirements (Pass/Fail):**

- Enforce session boundaries and timeframes mechanically (London + New York overlap; 5m/15m only)
- Support deterministic range identification and rule evaluation
- Enforce hard risk limits, trade frequency caps, and kill-switches
- Prevent discretionary overrides, scaling, or averaging down
- Provide complete audit logs with version binding (strategy and rule versions)
- Support backtesting and paper trading under identical rules

**Failure on any single requirement = platform rejected.**

## Stakeholder Register (Elective)

| Stakeholder | Role | Decision Rights |
|-------------|------|----------------|
| ML1 | Capital owner / sponsor | Final approval |
| ML2 (Second Brain) | System of record | Documentation only |
| MooseCoin | Execution entity | No decision authority |

## Key Assumptions (Initiation)

- Strategy rules take precedence over platform convenience
- Fewer viable platforms is an acceptable outcome
- Manual workarounds are not acceptable substitutes for enforcement
- “Almost compliant” platforms are treated as non-compliant

## Constraints (Initiation)

- No platform customization that alters strategy behavior
- No live trading during this project
- No exceptions to the gating checklist
- No dependency on undocumented platform features

## Initiation Stage Conclusion

The project is justified and necessary. Strategy content is sufficiently defined to gate platforms. Execution and configuration remain out of scope.

**Decision:**
- ✔ Project proceeds beyond Initiation
- ✔ Planning may begin
- ✖ No platform selection yet

## Exit Criteria for Initiation Stage

Initiation is complete when:

- The platform gating checklist is adopted as binding
- Evaluation criteria are frozen
- Planning artifacts for candidate evaluation are approved by ML1
