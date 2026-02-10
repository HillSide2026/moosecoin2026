---
id: 26-001-00001-CHARTER
title: Project Charter - Formalize Trading Strategy
owner: ML1
status: draft
created_date: 2026-02-03
last_updated: 2026-02-03
tags: [trading, strategy, charter, initiation]
---

# Project Charter

## Project Identification

| Field | Value |
|-------|-------|
| Project ID | 26-001-00001 |
| Project Name | Formalize Trading Strategy, Approach, and Tactics |
| Client | MooseCoin |
| Project Manager | ML1 |
| Start Date | 2026-02-03 |
| Target Completion | TBD (tracked in Decision Backlog DB-005) |

---

## Purpose Statement

This project exists to convert implicit trading judgment into explicit, inspectable doctrine. The goal is to create a formal, documented framework that captures the decision-making logic currently held as tacit knowledge, making it auditable, teachable, and systematically applicable.

---

## Objectives

### Primary Objectives

1. **Formalize Trading Strategy Doctrine**
   - Define enduring principles that govern trading decisions
   - Establish market scope and asset class boundaries
   - Document risk tolerance frameworks

2. **Develop Trading Approach Playbook**
   - Create procedural guidance for applying strategy
   - Define decision trees for common scenarios
   - Establish review and adjustment cadences

3. **Create Trading Tactics Checklists**
   - Document execution-level procedures
   - Define entry/exit criteria
   - Create position sizing guidelines

### Success Criteria

- All implicit trading logic is documented in explicit form
- Clear hierarchy established: Strategy > Approach > Tactics
- Downstream projects (Platform Selection, Website Development) can proceed with clarity
- ML1 approves final doctrine set as authoritative

---

## Stakeholders

| Role | Name | Responsibility |
|------|------|----------------|
| Decision Authority | ML1 | Approves all outputs, makes discretionary calls |
| System Operator | ML2 | Documents, structures, maintains consistency |

---

## Scope Summary

### In Scope

- Trading Strategy Doctrine (binding, source-of-truth eligible)
- Trading Approach Playbook (procedural guidance)
- Trading Tactics Checklists (execution procedures)
- Definitions and terminology standardization
- Decision hierarchy and approval gates

### Out of Scope

See `SCOPE_BOUNDARIES.md` for explicit exclusions.

---

## Constraints

| Constraint | Description |
|------------|-------------|
| Authority | No project artifact can become canon without ML1 explicit approval |
| Extraction | Patterns may only be extracted per GOV-2026-004 |
| Downstream | Platform and Website projects are blocked until this completes |

---

## Assumptions

1. ML1 has sufficient domain knowledge to make required trading decisions
2. Trading activity will continue during formalization (parallel operation)
3. The formalized doctrine will replace, not supplement, implicit decision-making

---

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Scope creep into platform decisions | High | Medium | Explicit scope boundaries enforced |
| Implicit logic remains unformalized | High | Medium | Structured review checkpoints |
| Premature systematization | Medium | Low | ML1 retains discretionary authority |

---

## Deliverables

| Deliverable | Stage | Format | Approval Required |
|-------------|-------|--------|-------------------|
| Project Charter | Initiation | Markdown | ML1 |
| Scope Boundaries | Initiation | Markdown | ML1 |
| Definitions Document | Initiation | Markdown | ML1 |
| Document Schema | Planning | Markdown | ML1 |
| Draft Doctrine | Execution | Markdown | ML1 |
| Final Doctrine Set v1.0 | Closing | Markdown | ML1 |

---

## Governance

This project follows the Standard 4-Stage Lifecycle:

1. **Initiation** (current) - Define scope, objectives, constraints
2. **Planning** - Design structure, standards, execution plan
3. **Execution & Monitoring** - Draft artifacts, detect drift
4. **Closing** - Validate and finalize deliverables

**Gate Control:** ML1 approval required for each stage transition.

---

## Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project Sponsor | ML1 | Pending | |

---

*Document Status: DRAFT - Awaiting ML1 Review and Approval*
