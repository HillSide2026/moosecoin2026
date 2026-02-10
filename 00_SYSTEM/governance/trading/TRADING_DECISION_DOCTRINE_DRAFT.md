---
id: GOV-2026-00X
title: Trading Decision Doctrine (Draft)
owner: ML1
status: draft
created_date: 2026-02-10
last_updated: 2026-02-10
effective_date: 2026-02-10
tags: [trading, governance, decision, doctrine]
provenance:
  decided_by: ML1
  decided_on: 2026-02-10
  context: Draft decision doctrine for trading strategy governance
---

# Trading Decision Doctrine (Draft)

## Purpose
Define how trading decisions are formed, approved, recorded, and traced to governing rules.

## Scope
**In Scope**
- Decision types (strategy, playbook, execution)
- Approval requirements and authority gates
- Traceability to rule IDs and source artifacts

**Out of Scope**
- Trading execution or order placement
- Platform implementation details

## Decision Types
- **Strategy Decisions (Layer 2)** — define when trading is allowed to exist
- **Playbook Decisions (Layer 2a)** — operational guidance without execution logic
- **Execution Decisions (Layer 3)** — implementation details (must be gated and approved)

## Decision Gates
- All decisions require ML1 approval before becoming binding
- Any decision that modifies or overrides a rule must include:
  - Rule ID(s)
  - Rationale
  - Downstream impact analysis

## Traceability Requirements
- Every decision MUST cite:
  - Rule ID(s)
  - Source artifact(s)
  - Approval record
- Decisions that lack traceability are invalid and must be paused

## Exceptions & Overrides
- Exceptions are allowed only with explicit ML1 approval
- Exceptions must be recorded as a decision with a sunset date or review trigger

## Open Questions (for ML1)
1. Should decision types map to distinct document locations?
2. What is the standard rule ID format for this system?
