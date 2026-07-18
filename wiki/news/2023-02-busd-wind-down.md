---
title: "BUSD Wind-Down — February 2023"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [crypto, stablecoins, depeg, history, regulation, busd, paxos, sec]
aliases: ["BUSD Halt", "Paxos Wells Notice", "BUSD Regulatory Shutdown"]
event_date: 2023-02-13
markets_affected: [crypto]
impact: high
verified: true
sources_count: 6
related: ["[[stablecoin-pair-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[depeg-risk]]", "[[paxos]]", "[[busd]]", "[[2023-03-usdc-svb-depeg]]", "[[stablecoin-depeg-history]]"]
---

# BUSD Wind-Down — February 2023

On **February 13, 2023**, two regulatory actions effectively ended **Binance USD (BUSD)**:
1. The U.S. SEC issued a **Wells Notice** to Paxos Trust Company (BUSD's issuer) signaling intent to take enforcement action
2. The **New York Department of Financial Services (NYDFS)** ordered Paxos to **halt new BUSD minting**

BUSD did **not** experience a panic depeg. Instead, it slowly bled circulation over months 2023-2024 as users migrated to USDC, USDT, and FDUSD. **This is the canonical "regulatory shutdown without panic" case** — important because it shows that not all regulatory action triggers tradable depegs, and sometimes the right trade is to **not trade**.

## Timeline

| Date | Event |
|------|-------|
| Sep 2019 | BUSD launched by Paxos in partnership with Binance |
| 2020-2022 | BUSD scales to ~$23B circulation by peak (Q3 2022) |
| **Feb 13, 2023** | SEC issues Wells Notice to Paxos; NYDFS orders halt to new BUSD minting |
| Feb 13-16, 2023 | BUSD trades $0.998-1.000 — **no panic depeg**. Existing redemption mechanism remained operational |
| Mar 2023 | Paxos confirms continued redemption of existing BUSD; circulation begins steady decline |
| Q2-Q3 2023 | Circulation drops from $16B to $3-4B as users migrate |
| Q4 2023 | BUSD largely sunset; <$1B circulation |
| 2024 | Paxos formally winds down BUSD operations; First Digital Labs launches FDUSD as Binance's preferred stable |

## Why No Panic Depeg

Three factors prevented a USDC/SVB-style depeg:

1. **Paxos reserves were not in question.** The regulatory action was about classification (SEC's view that BUSD was an unregistered security) and trust-company licensing (NYDFS's prudential concern), NOT about whether BUSD's USD reserves existed. Reserves were undisputed.

2. **Redemption channel stayed open.** Paxos continued processing BUSD redemptions throughout the wind-down. Users who wanted USD got USD. The slow drain reflected user choice, not forced selling.

3. **Sufficient time was given.** Unlike a banking-partner failure, the regulatory wind-down had a clear timeline (months, not weekends). Users could redeem in an orderly fashion without market panic.

The combination of these factors meant BUSD held its peg within 20bp throughout the wind-down — even as circulation declined 95%.

## What Trades Worked (and Didn't)

### What WORKED:

**Slow redemption-arb during the wind-down**: a small but persistent BUSD discount existed during the wind-down period (typically -10 to -50bp on major venues) due to:
- Liquidity migrating away
- Some venues delisting BUSD
- Yield differential vs USDC/USDT

Trade: buy BUSD at $0.997, redeem via Paxos at $1.00, capture 30bp. Repeat throughout wind-down period. Per-trade returns small but cumulative; capacity-bounded by Paxos redemption capacity.

### What DIDN'T WORK:

**Panic-depeg trades** that worked on USDC/SVB did NOT work on BUSD:
- Buying BUSD at $0.998 expecting reversion to $1.00 (already at fair value; no upside)
- Shorting BUSD expecting depeg to $0.50-0.70 (peg held; short paid funding for nothing)
- Pair trade long-BUSD / short-USDT (no spread to capture; both at par throughout)

**The lesson**: regulatory action ≠ panic depeg. The "trade" was sometimes to recognize that there *isn't* a trade.

## Comparison: BUSD vs USDC/SVB

| Dimension | BUSD Feb 2023 | USDC March 2023 |
|-----------|---------------|-----------------|
| Trigger | Regulatory (SEC + NYDFS) | Banking partner (SVB) |
| Reserve question | Reserves undisputed | $3.3B at SVB at risk |
| Redemption channel | Continuous | Closed weekend; reopened Mon |
| Lowest price | $0.998 | $0.8774 |
| Recovery time | n/a (no depeg) | 48 hours |
| Trade outcome | Small slow capture | Major event capture |
| Lesson | Regulatory ≠ panic | Banking failure = arb |

## Counterintuitive Insight

For a savvy depeg trader, **BUSD was a teaching opportunity disguised as a non-event**: the Wells Notice + NYDFS halt happened on a Monday morning. Many participants expected a USDC/SVB-style 5-15% depeg the following days. **They piled into "buy the depeg" positions that didn't materialize**, paying carry costs (in cases where they used leverage) without payoff.

**The infrastructure response** (Paxos's calm communication; reserve continuity; orderly wind-down) was the actual signal — and a small minority of traders recognized this and *avoided* the trade, redeploying capital elsewhere.

This case study is a reminder that **the absence of a depeg is itself a tradable signal**: it tells you the issuer is stable and the regulatory action is procedural rather than existential.

## Lessons for Modern Stable Depeg Trading

This case study informs three principles for [[stablecoin-depeg-profit-capture]]:

1. **Verify the trigger type before sizing.** Regulatory shutdowns ≠ banking failures ≠ mechanism breaks. Each has a different expected price reaction. Wrong-categorization → wrong trade.

2. **The "no depeg" outcome is a real outcome.** Always model the case where the mechanism holds. Position size should reflect the probability of trade-not-happening, not just trade-happening.

3. **Slow drains can still be tradable.** Even when no panic depeg occurs, persistent small spreads (10-50bp) can be captured via redemption-arb during the wind-down period. Lower per-event return but extended capture window.

4. **Regulatory clarity often **calms** stables, not destabilizes them.** A stable that survives a regulatory action with redemption channel intact may end up *more trusted*, not less. The trade is sometimes to long the post-clarity stable, not short.

## Modern Parallels

The BUSD wind-down has echoes in:
- **EU MiCA stablecoin regulations** (2024-2026) — multiple stables faced similar regulatory transitions; most maintained pegs without panic depegs
- **TerraUSD attempts to relaunch in regulated form** (2023-2024) — different mechanism, different outcome
- **PYUSD launch and growth** (2023-2026) — PayPal stable; high regulatory scrutiny, peg held throughout

These cases reinforce: regulatory action without reserve-question = no panic. Worth re-reading on every new regulatory event.

## Sources

- SEC Wells Notice public records (February 13, 2023)
- NYDFS press release on Paxos halt (February 13, 2023)
- Paxos public communications (February-December 2023)
- The Block coverage of BUSD wind-down (multiple articles, 2023)
- CoinMetrics on-chain data for BUSD circulation timeline
- Binance announcements on BUSD migration to alternatives

## Related

- [[stablecoin-pair-arbitrage]] — strategy hub
- [[stablecoin-depeg-profit-capture]] — Method 1 spot-buy and Method 2 redemption-arb both apply (slow capture)
- [[depeg-risk]] — risk framework
- [[paxos]] · [[busd]] — entity pages
- [[2023-03-usdc-svb-depeg]] — banking-failure parallel (different trigger, different outcome)
- [[stablecoin-depeg-history]] — master timeline
