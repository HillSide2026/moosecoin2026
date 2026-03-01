---
id: 26-001-00007-RISK-LITE
title: Initial Risk Register (Lite) - New Strategy Identification
owner: ML1
status: draft
created_date: 2026-03-01
last_updated: 2026-03-01
tags: [trading, strategy, risks, initiation]
---

# Initial Risk Register (Lite)

| Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
|--------|-------------|------------|--------|------------|-------|--------|
| R1 | Candidate strategy cannot be implemented deterministically | Medium | High | Require rule precision and enforceability checks during screening | ML1 | Open |
| R2 | Strategy drift toward discretionary behavior | Medium | High | Enforce explicit gates and no-override design principle | ML1 | Open |
| R3 | Candidate complexity exceeds operational capacity | Medium | High | Prefer simpler, auditable structures over high-complexity approaches | ML1 | Open |
| R4 | Overfitting narrative without robust regime logic | Medium | High | Require regime definitions and failure conditions up front | ML1 | Open |
| R5 | Selection bias toward recent market behavior | Medium | Medium | Compare candidates across multiple market states conceptually before modeling | ML1 | Open |

## Assumptions to Validate

- A viable replacement strategy can be specified within current doctrine constraints
- Candidate strategy can be represented in `02_MODELS/` with required model components
- Low trade frequency remains acceptable when required by regime logic
