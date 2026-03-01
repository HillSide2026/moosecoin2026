---
id: 26-001-00008-RISKS-FULL
title: Risk Register (Full) - Alternative Strategy Review
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [planning, risks, strategy, strat3]
---

# Risk Register (Full)

| Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
|--------|-------------|------------|--------|------------|-------|--------|
| R1 | Spike threshold band is miscalibrated, causing over-trading or under-trading | Medium | High | Keep thresholds explicit and flag for controlled validation protocol | ML1 | Open |
| R2 | Macro contamination tagging is incomplete or unavailable at decision time | Medium | Critical | Default to no-trade when contamination feed is missing or ambiguous | ML1 | Open |
| R3 | Stall confirmation rules remain ambiguous in edge cases | Medium | High | Enforce deterministic signal definitions with explicit fail conditions | ML1 | Open |
| R4 | Spread/liquidity degradation invalidates expected execution quality | Medium | High | Maintain hard risk gate and stand-aside triggers | ML1 | Open |
| R5 | Strategy behaves as discretionary counter-trend fade in practice | Low | Critical | Preserve single-pattern entry and strict no-anticipation rule | ML1 | Open |
| R6 | Time-window constraints are violated operationally | Low | High | Enforce session gates and hard time-stop in decision engine | ML1 | Open |
| R7 | Documentation drift between STRAT3 intent/spec/parameters/features | Medium | Medium | Keep cross-references synchronized and require version-linked updates | ML1 | Open |
| R8 | Premature implementation before planning-stage decision closure | Medium | High | Gate model handoff on explicit ML1 go/no-go decision | ML1 | Open |
