---
id: 26-001-00002-PLATFORM-SHORTLIST-PRICING
title: Platform Shortlist and Pricing Summary (Stage 3)
owner: ML1
status: draft
created_date: 2026-02-08
last_updated: 2026-02-08
tags: [execution, platform, shortlist, pricing]
---

# Platform Shortlist and Pricing Summary (Stage 3)

## Purpose

Summarize the current top‑10 candidate platforms and their pricing posture for Stage 3 execution screening. All platforms remain **unapproved** until they pass the gating checklist.

## Selection Criteria (Used for Shortlist)

- Mechanical enforceability of rules
- Auditability and logging
- Session/timeframe hard locks
- Deterministic rule logic
- Programmatic risk controls
- Backtest/paper parity

## Top‑10 Candidate Platforms (Preliminary, Unranked)

1. QuantConnect (LEAN)
2. Interactive Brokers (TWS API / FIX)
3. cTrader Automate (cAlgo)
4. MetaTrader 5 (MQL5)
5. TradeStation (EasyLanguage)
6. NinjaTrader (NinjaScript / ATI)
7. Saxo OpenAPI
8. OANDA REST‑v20
9. ProRealTime ProOrder
10. TradingView (Pine Script Strategies)

## Pricing Snapshot (High‑Level)

**Published pricing exists (verify exact plan/region):**
- QuantConnect (tiered plans)
- TradeStation (platform fee; brokerage may waive with activity)
- NinjaTrader (free + paid tiers; commissions vary)
- ProRealTime (plan tiers; pro vs non‑pro)
- TradingView (free + paid tiers)

**Broker‑dependent or quote‑based:**
- cTrader Automate (varies by broker)
- MetaTrader 5 (client access broker‑dependent; broker licensing quote‑based)
- Interactive Brokers (API usage depends on account/commissions; FIX sessions have higher fees)
- Saxo OpenAPI (fees tied to account tier/spreads)
- OANDA (pricing via spreads/commission model)

## Gating Rule (Non‑Negotiable)

If any single mandatory item in the platform gating checklist is unsupported, the platform is rejected — no workarounds.

## Next Step

Begin evidence‑based pass/fail evaluation for each platform against the gating checklist, documenting proof for each mandatory item.
