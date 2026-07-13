---
title: "SNB Swiss Franc Un-peg (January 15, 2015)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [news, forex, history, volatility, event-driven, risk-management]
aliases: ["Frankenshock", "SNB Floor Removal", "CHF Unpeg", "Swissie Tsunami"]
event_date: 2015-01-15
markets_affected: [forex, equities, bonds]
impact: high
verified: true
sources_count: 5
related: ["[[currency-peg-break-arbitrage]]", "[[crisis-currency-triangular-arbitrage]]", "[[triangular-arbitrage]]", "[[carry-trade]]"]
---

# SNB Swiss Franc Un-peg (January 15, 2015)

At **09:30 CET on Thursday, January 15, 2015**, the **Swiss National Bank (SNB)** announced — without warning and contradicting public guidance from just days earlier — that it was abandoning its **EUR/CHF 1.20 floor**, in place since September 6, 2011. The Swiss franc rallied **30% in 20 minutes** against the euro, bottoming intraday at EUR/CHF 0.85 before stabilizing near parity. The single largest one-day move in a major G10 currency in the modern post-Bretton-Woods era.

Estimated trader losses: **$3-5B** across retail FX brokers, hedge funds, and bank prop desks. Several FX brokers (FXCM, Alpari UK) became insolvent. A handful of well-positioned funds — most notably **Hayman Capital (Kyle Bass)**, **Brevan Howard**, and a few options-based traders — made meaningful profits.

## Background

The SNB had imposed the EUR/CHF 1.20 floor on September 6, 2011 to prevent CHF appreciation that was crushing Swiss exporters during the European sovereign debt crisis. The floor required the SNB to sell unlimited CHF for EUR at any rate ≤1.20 — meaning its balance sheet absorbed massive EUR inflows. By late 2014, SNB FX reserves had grown to ~CHF 500B (~80% of Swiss GDP).

**Pressures by late 2014:**
- ECB about to launch QE (announced January 22, 2015) — would push EUR weaker, requiring SNB to defend the floor more aggressively.
- Russian capital flight into CHF accelerated post-Crimea sanctions.
- Greek election (January 25, 2015) threatened euro exit risk.
- SNB balance sheet politically unsustainable in conservative Swiss politics.

**SNB public guidance was reassuring:**
- December 18, 2014: SNB confirmed the floor was "absolutely central."
- January 12, 2015 (3 days before): Vice-chair Jean-Pierre Danthine called the floor a "pillar."

This guidance was either dishonest or reflected a 72-hour decision pivot.

## The Move

| Time (CET) | EUR/CHF | Move from prior level |
|------------|---------|----------------------|
| 09:29 | 1.2010 | Steady at floor |
| 09:30 | Statement released | Floor abandoned |
| 09:31 | 1.10 | -8% |
| 09:35 | 0.95 | -21% |
| 09:50 | 0.85 (intraday low) | -29% |
| 10:00 | 0.95 | Recovery |
| 12:00 | 1.02 | Stabilizing |
| 17:00 | 1.04 | Day's close |

USD/CHF moved similarly: from 1.02 to 0.74 then back to 0.86.

Swiss equities (SMI) fell 9% on the day. SNB-held EUR reserves were marked-to-market at instant ~15-20% loss (~CHF 75-100B paper loss).

## Triangular Aspects

The cross-rate inconsistencies during the 09:30-09:50 window were extreme. Order books on EUR/CHF dried up entirely (no bids). USD/CHF and EUR/USD continued to trade — creating a 5-10 minute window where the **implied EUR/CHF via USD** differed from the (non-existent) direct EUR/CHF quote by 5-15%.

Sophisticated traders with low-latency multi-venue access executed:

```
1. Sell EUR/USD spot (long USD vs EUR).
2. Buy USD/CHF spot (long USD vs CHF).
3. Synthetic: short EUR/CHF.
```

Triangular arb in the chaos generated 3-8% in 5-10 minutes for those who could route across venues during the dislocation.

## Winners

**Hayman Capital (Kyle Bass)** — Pre-positioned via OTM CHF call options for months ahead of the un-peg. Reported profits ~$200M.

**Brevan Howard** — Long CHF positions ahead of decision; reported $300M+ profit.

**Marko Dimitrijevic / Everest Capital** — *Wrong* side; one of his funds was wiped out.

**Citadel** — Mixed outcomes across pods; net positive on options-based winners.

**Goldman Sachs prop / market-making** — Net positive after initial losses on direct floor positioning.

**Smaller options-based hedge funds** — Several boutique macro funds made 50-300% on dedicated CHF call books.

## Losers

| Loser | Approximate Loss | Outcome |
|-------|------------------|---------|
| FXCM | $225M loss vs $230M equity | Required emergency $300M loan from Leucadia |
| Alpari UK | Insolvent | Wound down |
| Citi | $150M | Absorbed |
| Deutsche Bank | $150M | Absorbed |
| Barclays | $50-100M | Absorbed |
| Everest Capital "Global" fund | ~$830M (entire fund) | Closed |
| Many retail traders | Bankrupt accounts | Some sued brokers |

Notable: many CHF-denominated mortgages in Hungary, Poland, Croatia (popular due to low CHF rates) became 30%+ more expensive overnight, triggering political crises in Eastern Europe.

## Lessons for Traders

1. **Defended pegs are not market prices** — they are policy commitments. Once questioned, they collapse violently.
2. **Central bank guidance can mislead.** The SNB's January 12, 2015 reassurance was effectively false.
3. **Options dominate spot in tail-risk events.** Spot short EUR/CHF capped at the floor (1.20); calls on CHF had unlimited convexity.
4. **Liquidity vanishes at the worst moment.** EUR/CHF order books were empty for ~20 minutes.
5. **Triangular routes survived even when direct quotes died** — the multi-venue arbs profited while direct-FX desks were paralyzed.
6. **Retail FX brokers are not capitalized for tail events.** FXCM and Alpari UK had insufficient client-account margin to absorb negative balances.

## Aftermath

- SNB introduced **negative interest rates** (-0.75%) to discourage CHF inflows — held until 2022.
- FX broker industry tightened margin requirements; banned negative balances post-event.
- ECB QE launched as expected one week later (January 22, 2015), validating the SNB's read.
- EUR/CHF settled into ~1.05-1.15 range for years.
- "Frankenshock" became case study in central-bank credibility risk and FX tail-event hedging.

## Sources

- SNB press release, January 15, 2015.
- *FXCM 8-K filing*, January 16, 2015.
- Sebastian Mallaby, *More Money Than God* — 2010 (later editions cover Bass).
- Brevan Howard / Hayman Capital LP letters Q1 2015.
- Bloomberg, Reuters, FT contemporaneous coverage.

## Related

[[currency-peg-break-arbitrage]] · [[crisis-currency-triangular-arbitrage]] · [[triangular-arbitrage]] · [[carry-trade]] · [[1992-black-wednesday-erm-crisis]] · [[volatility-arbitrage]] · [[1987-andy-krieger-nzd-short]]
