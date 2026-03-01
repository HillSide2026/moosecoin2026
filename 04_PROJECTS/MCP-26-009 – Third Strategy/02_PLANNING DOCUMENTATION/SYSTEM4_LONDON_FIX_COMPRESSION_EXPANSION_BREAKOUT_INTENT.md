---
id: MCP-26-009-SYSTEM4-INTENT
title: Strategy Intent - SYSTEM4 London Fix Compression to Expansion Breakout
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, strategy, intent, philosophy, system4]
---

# Strategy Intent Document

## Strategy ID

`SYSTEM4_LONDON_FIX_COMPRESSION_EXPANSION_BREAKOUT`

## Core Thesis

Trade only volatility expansion emerging from statistically abnormal compression
into the London Fix.

No compression means no trade. Exit immediately when expansion fails. Hold only
while expansion persists.

## Structural Inefficiency Exploited

- Intraday volatility can compress into fix liquidity before expanding sharply.
- Compression structures offer bounded invalidation with asymmetric expansion
  potential.
- Time-bounded transition windows improve structural timing versus all-session
  breakout participation.

## Explicit Non-Goals

- Not directional prediction
- Not discretionary breakout chasing
- Not noise trading outside defined session structure
- Not high-frequency activity model

## Market Microstructure Assumption

- London + NY overlap can produce compression pockets before fix-driven
  expansion.
- Valid transitions are structurally stronger when compression is statistically
  abnormal and macro contamination is absent.
- Expansion quality degrades when spread widens or macro flow dominates.

## Expected Behavioral Edge Source

- Regime-first gating reduces participation in dead or dislocated states.
- Compression-to-expansion transitions provide favorable asymmetry when
  invalidation is tight.
- Strict no-trade defaults reduce overtrading in ambiguous structure.

## Known Failure Regimes

- Dislocated pre-fix macro expansion
- Slanted or noisy compression that is not structurally valid
- Breakouts with immediate volatility collapse
- Spread/loss of liquidity during breakout trigger

## Drift Prevention Clauses

- Regime must be confirmed before compression validation.
- Compression validation must pass before breakout evaluation.
- Any ambiguity defaults to no-trade.
- Any risk-increasing change requires explicit ML1 decision.
