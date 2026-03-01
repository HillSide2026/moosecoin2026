---
id: 26-001-00001-SCOPE
title: Scope Boundaries - Formalize Trading Strategy
owner: ML1
status: draft
created_date: 2026-02-03
last_updated: 2026-02-03
tags: [trading, strategy, scope, initiation]
---

# Scope Boundaries

This document defines what Project 26-001-00001 explicitly includes and excludes.

---

## Purpose

Clear scope boundaries prevent:
- Scope creep into downstream projects
- Premature platform or tooling decisions
- Confusion about project deliverables
- Circular dependencies between projects

---

## In Scope

### 1. Trading Strategy Doctrine

**Included:**
- Market selection criteria (which markets to trade)
- Asset class definitions and boundaries
- Risk tolerance frameworks and limits
- Position sizing principles
- Time horizon classifications
- Portfolio allocation guidelines

**Format:** Binding doctrine (`01_DOCTRINE/` canonical doctrine subdirectories)

### 2. Trading Approach Model

**Included:**
- Decision trees for market analysis
- Entry/exit decision frameworks
- Review and rebalancing cadences
- Escalation procedures for edge cases
- Integration between strategy and tactics

**Format:** Procedural model (`02_MODELS/`)

### 3. Trading Tactics Checklists

**Included:**
- Pre-trade checklists
- Execution procedures
- Post-trade review processes
- Record-keeping requirements
- Error handling procedures

**Format:** Protocol checklists (`03_PROTOCOLS/checklists/`)

### 4. Terminology and Definitions

**Included:**
- Strategy vs Approach vs Tactics definitions
- Trading-specific glossary terms
- Decision hierarchy documentation

---

## Explicit Exclusions

### 1. Platform Selection (Deferred to 26-001-00002)

**NOT included in this project:**
- Trading platform evaluation
- Broker selection criteria
- API or tooling requirements
- Fee structure analysis
- Platform-specific workflows

**Reason:** Platform decisions depend on strategy outputs from this project.

### 2. Website Development (Deferred to 26-001-00003)

**NOT included in this project:**
- Public-facing content strategy
- Website feature requirements
- Brand or messaging decisions
- User interface design

**Reason:** Website content depends on formalized strategy.

### 3. Tax or Legal Considerations

**NOT included in this project:**
- Tax optimization strategies
- Regulatory compliance frameworks
- Legal entity structuring
- Reporting requirements

**Reason:** Out of domain; requires separate expertise.

### 4. Specific Trade Decisions

**NOT included in this project:**
- Individual trade recommendations
- Specific entry/exit calls
- Real-time market analysis
- Performance attribution

**Reason:** This project formalizes the framework, not individual decisions.

### 5. Automation Implementation

**NOT included in this project:**
- Trading bot development
- Automated execution systems
- Algorithm coding
- Backtesting infrastructure

**Reason:** Implementation follows formalization; premature to specify.

---

## Boundary Decisions (Requires ML1 Input)

The following items are at the scope boundary and require ML1 decision:

| Item | Include? | Rationale |
|------|----------|-----------|
| Cryptocurrency markets | TBD (Decision Backlog DB-001) | Depends on asset class scope |
| Options/derivatives | TBD (Decision Backlog DB-002) | Depends on complexity appetite |
| Leverage policy | TBD (Decision Backlog DB-003) | Risk vs return considerations |
| Multi-account coordination | TBD (Decision Backlog DB-004) | Operational complexity |

---

## Dependency Implications

```
26-001-00001 (This Project)
    |
    +---> 26-001-00002 (Platform Selection)
    |         Blocked until: Strategy outputs complete
    |         Needs: Market scope, execution requirements
    |
    +---> 26-001-00003 (Website Development)
              Blocked until: Strategy outputs complete
              Needs: Messaging framework, public positioning
```

---

## Scope Change Process

Any proposed scope change must:

1. Be documented in `06_ACTIONS.md`
2. Include impact analysis on timeline and dependencies
3. Receive explicit ML1 approval before proceeding
4. Update this document if approved

---

## Approvals

| Role | Decision | Date | Notes |
|------|----------|------|-------|
| ML1 | Pending | | Review scope boundaries |

---

*Document Status: DRAFT - Awaiting ML1 Review and Approval*
