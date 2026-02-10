---
id: 26-001-00004-TRADING-STRATEGIES-MANUAL-V1
title: MooseCoin Trading Strategies Manual (v1)
owner: ML1
status: draft
created_date: 2026-02-09
last_updated: 2026-02-09
tags: [trading, strategy, strategies, manual, layer2]
---

# MooseCoin Trading Strategies Manual (v1)

**Owner:** ML1  
**Layer:** 2 (Strategy)  
**Purpose:** Define when trading is allowed to exist and why, independent of tools or setups.

---

## Current Strategy & Playbook Inventory

- **Strategy (active):** `07_REFERENCE/TRADING_STRATEGY1_RANGEBREAKHOLD.md`
- **Playbook (active):** `02_PLAYBOOKS/TRADING_PLAYBOOK_V2.md`
- **Playbook (archived):** `10_ARCHIVE/04_PROJECTS/26-001-00001 MooseCoin - Formalize Trading Strategy/TRADING_PLAYBOOK_V1.md`

## Documentation Inconsistencies (To Resolve)

1. **Playbook location mismatch**  
   - `04_PROJECTS/26-001-00001 MooseCoin - Formalize Trading Strategy/01_INITIATION DOCUMENTATION/DEFINITIONS.md` and `SCOPE_BOUNDARIES.md` specify playbooks live in `02_PLAYBOOKS/`, but the active playbook is in `04_PROJECTS/**/03_EXECUTION DOCUMENTATION/`.
2. **Authority language mismatch**  
   - `TRADING_PLAYBOOK_V2.md` states it is “binding unless superseded,” but playbooks are procedural and non‑binding per system governance.
3. **Terminology drift inside this manual**  
   - This is a strategy manual, but Section 11 ends with “No setup may weaken this playbook.” That should likely read “strategy.”

## 1. Strategy Objective

The objective of this strategy is selective participation in transitional market regimes where price moves from balance to imbalance under acceptable liquidity and volatility conditions.

The strategy prioritizes:
- Capital preservation
- Asymmetric opportunity
- Patience over activity

**Default state:** No position.

---

## 2. Strategy Thesis (The “Why”)

Markets spend most of their time in balance. Edge appears not in balance, and not in chaos, but in transition.

The strategy seeks to exploit:
- Failed continuation attempts
- Breaks from established balance
- Early-stage directional expansion

This edge is:
- Episodic
- Regime-dependent
- Fragile to liquidity and execution conditions

The strategy assumes missing trades is normal and preferable to forcing participation.

---

## 3. Market Universe

### In Scope
- FX majors:
  - EUR/USD
  - USD/JPY
  - GBP/USD

### Conditionally In Scope
- Crypto (BTC, ETH)
  - Intraday only
  - Flat by session end
  - Optional and deferrable

### Out of Scope
- Illiquid instruments
- Exotic pairs
- Overnight crypto exposure
- Instruments requiring discretionary hedging

---

## 4. Regime Framework (Core of the Strategy)

Markets are classified into three regimes:

### 4.1 Dormant (Do Nothing)

**Characteristics:**
- Compressed ranges
- Low volatility
- Overlapping candles
- Poor payoff potential

**Action:** Stand aside.

### 4.2 Transitional (Tradable)

**Characteristics:**
- Volatility expanding from compression
- Failed attempts to remain in balance
- Early directional resolution

**Action:** Strategy may participate, subject to all constraints.

### 4.3 Dislocated (Do Nothing)

**Characteristics:**
- Extreme volatility
- Event-driven repricing
- Spread instability
- Poor execution quality

**Action:** Stand aside.

**Invariant:** Only the Transitional regime is tradable.

---

## 5. Eligibility Gates (Must All Pass)

A trade is eligible to exist only if:
- Market is within a defined session
- Liquidity is normal for that session
- Volatility is not dormant or dislocated
- No macro or operational blackout applies
- Risk capacity is well below limits
- Execution conditions are stable

If any gate fails → **no trade**.

---

## 6. Risk Posture

- Risk is finite and valuable
- No averaging down
- No position scaling
- No recovery trades
- No discretionary overrides

Risk capacity governs whether the strategy participates at all, not just size.

---

## 7. Trade Archetypes (Conceptual Only)

The strategy expects to express itself through a small number of archetypes, such as:
- Resolution from compression into expansion
- Failure of attempted continuation at range extremes
- Directional follow‑through after balance break

These are conceptual patterns, not setups.

---

## 8. Failure & Invalidation

The strategy is **suspended**, not optimized, if:
- Transitional regimes stop producing asymmetric outcomes
- Execution costs overwhelm expected payoff
- Liquidity conditions structurally degrade
- Risk controls are approached repeatedly

Suspension requires review and re‑approval.

---

## 9. Capital Deployment Philosophy

- Low frequency is acceptable
- Inactivity is success
- Conviction is expressed through selectivity, not size
- Missing trades is preferable to forcing them

---

## 10. What This Strategy Refuses to Do

This strategy will not:
- Trade out of boredom
- Trade to “stay active”
- Trade through uncertainty
- Trade when rules are inconvenient

---

## 11. Relationship to Other Layers

- **Layer 1 (Governance):** Overrides everything here
- **Layer 3 (Setups):** Must declare:
  - Which regime they operate in
  - Why they fail outside that regime
  - How they respect eligibility gates

No setup may weaken this strategy.

---

## Strategy Invariant (Condensed)

We trade rarely, deliberately, and only when markets transition out of balance. Standing aside is the correct default.
