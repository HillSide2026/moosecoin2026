---
id: 26-001-00001-DEFINITIONS
title: Definitions - Strategy, Approach, and Tactics
owner: ML1
status: draft
created_date: 2026-02-03
last_updated: 2026-02-03
tags: [trading, strategy, definitions, initiation]
---

# Definitions: Strategy vs Approach vs Tactics

This document establishes the terminology hierarchy for trading formalization.

---

## Purpose

Clear definitions prevent:
- Confusion between levels of abstraction
- Mixing strategic and tactical concerns
- Inappropriate delegation of decisions
- Drift in document authority

---

## The Three-Level Hierarchy

```
STRATEGY (Why + What)
    |
    v
APPROACH (How, generally)
    |
    v
TACTICS (How, specifically)
```

---

## Level 1: Strategy

### Definition

**Strategy** is the set of enduring principles that define *what* we are trying to achieve and *why*. Strategy answers fundamental questions about identity, purpose, and constraints.

### Characteristics

| Property | Description |
|----------|-------------|
| Time Horizon | Long-term (years) |
| Change Frequency | Rarely; requires significant justification |
| Decision Maker | ML1 only |
| Authority Level | Binding (`authority.level: binding`) |
| Location | `01_DOCTRINE/binding/` |

### Strategy Answers

- What markets do we participate in?
- What is our risk tolerance?
- What are our return objectives?
- What constraints are non-negotiable?
- What is our competitive advantage?

### Strategy Does NOT Answer

- Which specific trades to make
- When to enter or exit positions
- What platform to use
- Day-to-day operational decisions

### Example Strategic Statements

- "We trade only liquid markets with daily volume > $X"
- "Maximum portfolio drawdown tolerance is Y%"
- "We do not use leverage exceeding Z:1"
- "Decisions requiring discretion are escalated to ML1"

---

## Level 2: Approach

### Definition

**Approach** is the general methodology for *how* we implement strategy. Approach translates strategic principles into repeatable frameworks and decision processes.

### Characteristics

| Property | Description |
|----------|-------------|
| Time Horizon | Medium-term (months to years) |
| Change Frequency | Periodic review; adjustable with experience |
| Decision Maker | ML1 (with ML2 drafting) |
| Authority Level | Procedural (`authority.level: procedural`) |
| Location | `02_PLAYBOOKS/` |

### Approach Answers

- How do we analyze market conditions?
- What decision frameworks guide position sizing?
- How do we balance competing objectives?
- What review cadence maintains alignment?
- How do we handle edge cases?

### Approach Does NOT Answer

- Specific entry/exit prices
- Individual position decisions
- Real-time market calls
- Tool or platform selection

### Example Approach Statements

- "Market analysis follows the [Framework Name] decision tree"
- "Position sizing scales with conviction level per the sizing matrix"
- "Weekly review assesses portfolio alignment with strategy"
- "Edge cases are logged and escalated within 24 hours"

---

## Level 3: Tactics

### Definition

**Tactics** are the specific, executable procedures for *how* we act in the moment. Tactics are the implementation layer that connects approach to action.

### Characteristics

| Property | Description |
|----------|-------------|
| Time Horizon | Short-term (hours to weeks) |
| Change Frequency | Frequently; optimized with experience |
| Decision Maker | ML2 (within bounds set by Strategy/Approach) |
| Authority Level | Procedural (`authority.level: procedural`) |
| Location | `03_TEMPLATES/checklists/` |

### Tactics Answers

- What are the steps before placing a trade?
- What records must be created?
- How do we execute an entry/exit?
- What error handling procedures apply?
- What post-trade review is required?

### Tactics Does NOT Answer

- Whether to trade a given market (Strategy)
- How to size the position (Approach)
- What risk tolerance applies (Strategy)
- Framework-level decisions (Approach)

### Example Tactical Statements

- "Before any trade: complete pre-trade checklist"
- "Record trade rationale in execution log within 1 hour"
- "Use limit orders unless market conditions require market orders"
- "Review all trades weekly using the post-trade template"

---

## Hierarchy Rules

### 1. Lower Levels Cannot Override Higher Levels

Tactics cannot contradict Approach. Approach cannot contradict Strategy.

```
INVALID: Tactical checklist permits leverage > Strategy limit
INVALID: Approach playbook trades markets excluded by Strategy
```

### 2. Decisions Flow Down, Not Up

Strategic decisions inform Approach. Approach decisions inform Tactics.

```
VALID: Strategy defines risk tolerance -> Approach creates sizing framework -> Tactics implement execution
INVALID: Tactical convenience drives Approach change without Strategy review
```

### 3. Authority Increases with Abstraction

Higher-level documents require more approval and change less frequently.

| Level | Approval | Review Frequency |
|-------|----------|------------------|
| Strategy | ML1 only | Annually minimum |
| Approach | ML1 (draft by ML2) | Quarterly |
| Tactics | ML1 review | Monthly |

### 4. Ambiguity Resolves Upward

When tactics are unclear, consult approach. When approach is unclear, consult strategy. When strategy is unclear, escalate to ML1.

---

## Document Mapping

| Level | Document Type | Repository Location | Authority |
|-------|---------------|---------------------|-----------|
| Strategy | Doctrine | `01_DOCTRINE/binding/` | Binding, Source-of-Truth |
| Approach | Playbook | `02_PLAYBOOKS/` | Procedural, Not Source-of-Truth |
| Tactics | Checklist | `03_TEMPLATES/checklists/` | Procedural, Not Source-of-Truth |

---

## Application to This Project

Project 26-001-00001 will produce:

1. **Trading Strategy Doctrine** (Level 1)
   - Defines markets, risk, constraints
   - Binding authority
   - ML1 authored and approved

2. **Trading Approach Playbook** (Level 2)
   - Decision frameworks and procedures
   - Procedural authority
   - ML2 drafted, ML1 approved

3. **Trading Tactics Checklists** (Level 3)
   - Execution procedures
   - Procedural authority
   - ML2 drafted, ML1 reviewed

---

## Approvals

| Role | Decision | Date | Notes |
|------|----------|------|-------|
| ML1 | Pending | | Review definitions for accuracy |

---

*Document Status: DRAFT - Awaiting ML1 Review and Approval*
