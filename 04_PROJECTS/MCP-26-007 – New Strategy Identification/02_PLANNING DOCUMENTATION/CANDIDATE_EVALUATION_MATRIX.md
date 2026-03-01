---
id: 26-001-00007-CANDIDATE-MATRIX
title: Candidate Evaluation Matrix - Strategy Identification
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, evaluation, matrix]
---

# Candidate Evaluation Matrix

## Purpose

Provide pass/fail governance criteria for candidate strategies. This matrix supports ML1 selection decisions and avoids preference-based ranking.

## Evaluation Framework

| Criterion | Requirement | Type | Strategy 2 Candidate |
|----------|-------------|------|----------------------|
| Regime clarity | Regimes explicitly defined and mutually exclusive | Mandatory | Pass (draft thresholds pending) |
| Deterministic entry | Single entry trigger with objective checks | Mandatory | Pass |
| Deterministic invalidation | Immediate, objective fail condition | Mandatory | Pass |
| Risk enforceability | Fixed-risk sizing and hard constraints | Mandatory | Pass |
| No-discretion architecture | No override path in normal flow | Mandatory | Pass |
| Auditability | Trade must be reconstructible from logs | Mandatory | Pass |
| Ambiguity handling | Unknown states default to no trade | Mandatory | Pass |
| Operational feasibility | Implementable with available data/feed constraints | Mandatory | Pending |
| Complexity tolerance | Rule count and dependencies operationally manageable | Advisory | Pass |

## Selection Rule

- Any mandatory `Fail` disqualifies candidate.
- Mandatory `Pending` items must be resolved before selection decision.
- Advisory items inform refinement priorities but do not block by themselves.

## ML1 Decision Points

- DM-001: Accept candidate as primary (yes/no)
- DM-002: Require threshold refinements before acceptance (yes/no)
- DM-003: Keep backup candidate path open (yes/no)
