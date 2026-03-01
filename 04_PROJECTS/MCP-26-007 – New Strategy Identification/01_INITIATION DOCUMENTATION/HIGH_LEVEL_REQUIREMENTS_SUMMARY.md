---
id: 26-001-00007-REQUIREMENTS-SUMMARY
title: High-Level Requirements Summary - New Strategy Identification
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, requirements, initiation]
---

# High-Level Requirements Summary

## Mandatory Requirements

- Candidate strategy must have an explicit regime framework
- Candidate must define objective stand-aside conditions
- Candidate must support deterministic entry and invalidation logic
- Candidate must support fixed-risk sizing and hard risk ceilings
- Candidate must be auditable and reproducible from logs
- Candidate must be implementable without discretionary override paths

## Governance Requirements

- No candidate can override doctrine constraints
- Candidate assumptions must be explicit and testable
- Any risk-increasing design choice requires ML1 decision record

## Evaluation Outputs Required

- Candidate profile cards (thesis, regime, risk, failure modes)
- Comparison matrix against requirements
- Selection memo with ML1 decision points

## Exclusions

- No commitment to live deployment
- No performance promises
- No optimization loops during initiation
