---
id: 26-001-00007-SCOPE-STATEMENT
title: Scope Statement - New Strategy Identification
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, scope, strategy]
---

# Scope Statement

## In Scope

- Define the evaluation framework for Strategy 2 candidate validation
- Formalize regime definitions, no-trade filters, and fail-fast rules
- Build candidate comparison criteria for alternative strategy options
- Produce a planning-level decision package for ML1 strategy selection
- Define handoff requirements for downstream model formalization in `02_MODELS/`

## Out of Scope

- Live trading or capital deployment
- Broker/platform integration
- Production automation implementation
- Doctrine publication or binding approval

## Assumptions

- Strategy 1 remains archived while Strategy 2 is under evaluation
- Candidate strategy must preserve governance-first risk posture
- Low trade frequency and stand-aside behavior remain acceptable by design

## Constraints

- No discretionary override pathways in candidate logic
- No weakening of non-negotiable risk constraints
- All candidate rules must be objectively testable
- Ambiguity defaults to no trade
- All outputs must remain advisory until ML1 approval
