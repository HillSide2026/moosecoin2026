---
id: 26-001-00007-VALIDATION-PLAN
title: Validation Plan - Strategy 2 Candidate
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, validation, strategy]
---

# Validation Plan

## Purpose

Define how Strategy 2 candidate behavior will be validated before execution-stage promotion work.

## Validation Principles

- Validate rule behavior before profitability claims
- Prefer deterministic pass/fail checks over narrative interpretation
- Treat missing data or ambiguity as no trade

## Validation Layers

1. Structural validation
2. Regime classification validation
3. Entry/exit rule validation
4. Risk and sizing validation
5. Auditability validation

## Required Test Scenarios

### Structural

- Valid clean range passes all setup checks
- Slanted/unclean range fails as no trade

### Regime

- Dormant -> no trade
- Dislocated -> no trade
- Transitional -> trade allowed (if other gates pass)
- Unknown regime input -> no trade

### Entry/Invalidation

- Wick-only breakout rejected
- Full close + non-reentry accepted
- Any close back inside range triggers immediate exit

### Risk/Sizing

- Position size equals fixed-risk formula output
- No scaling or add-on orders permitted
- Stop must be computable pre-entry or trade rejected

### Audit

- Regime label and supporting metrics logged
- Range boundaries logged
- Entry reason and exit reason logged
- Strategy/model version linked to trade record

## Minimum Evidence Package

- Scenario test logs
- Rule outcome table (expected vs actual)
- Exception list with unresolved issues
- ML1 decision memo: proceed/hold/rework
