---
id: 26-001-00001-PLAYBOOK-V1
title: Trading Playbook v1
owner: ML1
status: in_progress
created_date: 2026-02-08
last_updated: 2026-02-08
tags: [trading, strategy, playbook]
---

# Trading Playbook v1

## 1. Purpose & Governance

This playbook formalizes the trading doctrine into executable, auditable procedures. It is binding unless explicitly superseded by approved change control. Risk governance supersedes delivery velocity.

### Non-Negotiable Constraints

- Hard risk limits per-trade, daily, weekly
- No averaging down or position scaling
- Crypto exposure flat by session end
- Single active strategy instance per account

### Change Control

All changes require documented request, impact analysis, risk review, and sponsor approval. No change that increases risk is permitted without capital owner approval.

---

## 2. Operating Model

### Decision Hierarchy

- Strategy: Enduring principles (ML1 only)
- Approach: Procedural methodology
- Tactics: Executable checklists

### Time Horizons

- Strategic horizon: Multi-week to multi-month
- Tactical horizon: Intraday to multi-day (as defined per setup)
- Execution horizon: Session-level

### Trade Frequency

- Low frequency acceptable
- Standing aside is a valid outcome

---

## 3. Market Universe & Sessions

### In-Scope Markets

- FX majors: EUR/USD, USD/JPY, GBP/USD
- Optional crypto module: BTC, ETH (intraday only)

### Sessions

- Define session start/end times per asset
- Crypto exposure must be flat by session end

---

## 4. Market Conditions

### Valid Conditions Checklist

- Liquidity adequate for chosen venue
- Spread within acceptable bounds
- Data feeds healthy and consistent
- Volatility within expected regime

### Invalid Conditions / Stand-Aside Triggers

- Data errors or feed discrepancies
- Volatility spike outside defined regime
- Major scheduled events within defined blackout window
- Risk limits within 10% of daily or weekly cap

---

## 5. Signal & Entry Rules

### Setup Definition

- Setup type must be explicitly named and defined
- Entry trigger must be objective and observable

### Entry Conditions

- Setup checklist complete
- Risk gate approves size and exposure
- Order type matches venue constraints

### Order Placement

- Use limit or stop orders per setup definition
- No discretionary overrides in live trading

---

## 6. Risk Engine Rules (Hard Limits)

### Per-Trade Risk

- Max risk per trade: defined in risk profile

### Daily / Weekly Caps

- Max daily loss: defined in risk profile
- Max weekly loss: defined in risk profile

### Exposure Controls

- Aggregate exposure limits enforced
- No position scaling or averaging down

### Kill-Switch

- Auto-stand-down on breach of any hard limit

---

## 7. Stops & Targets

### Stops

- Invalidation-based stop required on entry
- Stop distance must be pre-approved by risk gate

### Targets

- Target logic defined in R-multiples
- Partial exits permitted only if codified in setup

---

## 8. Execution & Monitoring

### Execution Flow

1. Signal generated
2. Risk gate validation
3. Order placement
4. Post-trade logging

### Slippage & Drift Controls

- Conservative slippage assumptions used
- Execution drift monitored daily

### Monitoring

- Daily risk checkpoint
- Weekly performance and compliance review

---

## 9. Testing & Validation

### Backtesting

- Historical backtest required before paper trading
- Walk-forward tests required for robustness

### Paper Trading

- Minimum duration: defined in validation plan
- Pass/fail criteria predefined

---

## 10. Audit Trail & Logging

### Required Fields

- Setup ID
- Entry/exit timestamps
- Risk parameters at entry
- Rationale and checklist completion
- Execution venue and order type

### Versioning

- Every rule change must be versioned
- Logs must reference active rule version

---

## 11. Pilot & Scale-Up

### Pilot Constraints

- Capital caps enforced
- No leverage changes without approval

### Success Criteria

- Risk compliance 100%
- Performance metrics meet predefined thresholds

### Scale-Up Rules

- Only after successful pilot review
- Approved by ML1 and risk authority
