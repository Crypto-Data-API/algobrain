---
title: "Bitcoin Cash Fork Arbitrage (August 2017)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [crypto, history, bitcoin, arbitrage, event-driven]
aliases: ["BCH Fork", "Bitcoin Cash Hard Fork", "August 1 Fork", "UAHF"]
event_date: 2017-08-01
markets_affected: [crypto]
impact: high
verified: true
sources_count: 4
related: ["[[triangular-arbitrage]]", "[[fork-airdrop-triangulation]]", "[[bitcoin-cash]]", "[[hard-fork]]"]
---

# Bitcoin Cash Fork Arbitrage (August 2017)

On **August 1, 2017 at 12:37 UTC (block 478,558)**, Bitcoin Cash (BCH) split from Bitcoin via a User-Activated Hard Fork (UAHF). Every BTC holder received an equivalent quantity of BCH. The fork created the **largest single coordinated airdrop in crypto history at that point** and produced a multi-week triangular arbitrage opportunity worth **$3-7B in extracted value** for sophisticated traders. Establishing the template for all subsequent contentious fork plays (BCH/BSV 2018, ETH/ETC reaction, BTC/BSV 2018, ETH/ETHPoW 2022).

## Background

The "Bitcoin block size war" (2015-2017) split Bitcoin community into:

- **Small-blockers** (Bitcoin Core, Blockstream): keep 1 MB blocks; scale via Lightning Network and SegWit.
- **Big-blockers** (Bitmain, Roger Ver, Jihan Wu): increase blocks to 8 MB+ for direct on-chain scaling.

After SegWit activation (August 2017), big-blockers split off, creating Bitcoin Cash with 8 MB blocks.

**The fork mechanic:**
- Anyone holding BTC at block 478,558 received the same quantity of BCH on the new chain.
- Coinbase, Kraken, Bitstamp, GDAX all initially refused to credit BCH; reversed positions over following weeks under pressure.
- Bitfinex, Bittrex, OKEx credited immediately and enabled BCH trading from August 1.
- Mining cycled between BTC and BCH based on profitability (difficulty adjustment lag created arb opportunities for miners too).

## The Triangular Arb

The fork created a textbook triangular arbitrage:

```
Pre-fork: 1 BTC = $2,800 (single asset)
Post-fork: 1 BTC + 1 BCH = total value
```

If pre-fork BTC was $2,800 and immediate post-fork:
- BTC = $2,750
- BCH = $300

Then: 1 pre-fork BTC = $3,050 post-fork value (8.9% premium).

**Trade 1: Long BTC into the fork, sell BCH immediately.**
- Buy BTC pre-fork at $2,800.
- Hold through block 478,558.
- Now have 1 BTC + 1 BCH.
- Sell BCH at $300 immediately.
- Net cost: $2,500 for 1 BTC = effective discount.

**Trade 2: Cross-exchange arbitrage.**
- Bitfinex enabled BCH immediately at $200-300; Coinbase didn't credit until December 2017.
- Move BTC to Bitfinex pre-fork → sell BCH → buy BTC back at Coinbase.
- Capture the entire BCH value.

**Trade 3: Triangular implied vs actual.**
- BTC futures (CME launched December 2017, but Bitfinex perpetuals existed) priced post-fork value.
- Spot BTC + BCH spot vs futures basis offered 3-leg arb.

**Trade 4: BCH/BTC pair cross-rate.**
- BCH/BTC, BTC/USD, BCH/USD were quoted on different exchanges with different lag.
- Cross-rate inconsistencies of 200-1000 bp existed for hours-days.

## The Move

| Date | BTC | BCH | BTC+BCH Value | Notes |
|------|-----|-----|---------------|-------|
| Jul 31 | $2,820 | n/a | $2,820 | Pre-fork |
| Aug 1 (fork) | $2,710 | $290 (immediate) | $3,000 | Snapshot |
| Aug 2 | $2,720 | $700 (Bitfinex peak) | $3,420 | BCH pump |
| Aug 19 | $4,200 | $300 | $4,500 | BTC rallied |
| Nov 12 | $5,820 | $2,800 (1st BCH peak) | $8,620 | BCH-BTC reversal squeeze |
| Dec 2017 | $19,000 | $4,000 | $23,000 | Both pumped to ATH |

Total airdropped BCH supply: ~16.5M coins at fork. At Nov 12, 2017 peak of $2,800 = **$46B total BCH market cap** — purely created from the fork.

## Triangular Aspects

The fork generated multiple distinct triangular arb opportunities over 4-6 weeks:

**Triangle 1: BTC-BCH-USD across exchanges.** Coinbase (no BCH initially) vs Bitfinex (immediate BCH) created a structural arb where moving BTC to Bitfinex netted BCH that could be sold for USD then BTC repurchased on Coinbase.

**Triangle 2: BTC futures vs BTC spot vs BCH spot.** BCH "value" was either priced into BTC futures (some) or not (others). Arbs traded the inconsistency.

**Triangle 3: BTC-BCH-BCC (the alternate ticker for early days).** Different exchanges used BCC vs BCH ticker briefly, creating short-window mispricing for those who could see both feeds.

**Triangle 4: BCH/BTC ratio swings.** From 0.05 to 0.50 over 4 months. Cross-rate dislocations between exchanges providing BCH/BTC vs USD-derived implied rates were 100-500 bp.

## Winners

**Roger Ver / Jihan Wu / Bitmain** — Pumped BCH publicly; dominated mining; presumed to have monetized large BCH allocations.

**Bitfinex / Bittrex** — Captured trading volume from "I want my BCH NOW" customers from Coinbase migration.

**Cross-exchange arbitrageurs** — Estimated 10-15 sophisticated trading desks (Jump, Cumberland-DRW, Alameda Research) extracted $50-200M each from the BCH cross-exchange/cross-time arb over the 4-6 week window.

**Early Coinbase customers** (eventually) — When Coinbase finally credited BCH in December 2017 at $1,800/BCH, customers received massive windfall — but by then the trading arb opportunity had compressed.

**Miners with flexible hashpower** — BCH had a "Emergency Difficulty Adjustment" mechanism initially that made BCH mining periodically much more profitable than BTC; miners who flipped between chains captured 30-100% APY in mining returns.

## Losers

**Long-only BTC funds that hadn't planned for the fork** — Some early-2017 BTC ETFs (Grayscale GBTC) faced operational complications crediting BCH to LPs; took weeks to resolve. Some lost the BCH value to operational gaps.

**Coinbase early-customer trust** — Coinbase's initial refusal to credit BCH cost them retail trust. Class-action lawsuits filed.

**BSV holders later (Nov 2018)** — Those who tried the same playbook on the BCH/BSV split lost; BSV traded at a fraction of BCH and the hash-war noise drowned out arb gains.

## Aftermath

- **November 2017:** BCH rallied to $2,800 in a "flippening" attempt.
- **December 2017:** Crypto bull-run peak; BTC $19k, BCH $4k.
- **November 2018:** BCH fork into BCH (ABC) and BSV (Satoshi's Vision) — Craig Wright vs Roger Ver hash war.
- **2019-2024:** BCH gradually lost relevance; price ~$200-500 range.
- **Subsequent forks:** ETC (2016 already done), BTG (Oct 2017), BCD, BCN — each created smaller arb opportunities.

## Lessons for Crypto Traders

1. **Forks create one-time triangular windfalls** — pre-position long the parent chain, capture the fork token immediately.
2. **Exchange behavior fragmented = arb opportunity.** When some exchanges credit immediately and others lag, multi-venue setups capture the spread.
3. **Plan for fork-credit operational risk.** Coinbase's initial refusal cost their customers (and some institutional funds) the BCH value.
4. **Mining-difficulty-adjustment lag is exploitable.** BCH's EDA created multi-day windows where mining BCH paid 2-3x BTC; flexible miners profited.
5. **The fork-arb playbook has been re-applied** to dozens of subsequent splits — ETHW/ETHS (2022), Solana memecoin "rugs," etc.

## Sources

- Andreas Antonopoulos, *Mastering Bitcoin* (2nd ed. 2017) — fork mechanics.
- Coinbase blog posts August-December 2017 on BCH crediting.
- Bitfinex / Bittrex announcements July-August 2017.
- Cumberland-DRW, Jump Crypto contemporaneous market commentary (Twitter, conference talks).
- *Bitcoin Cash whitepaper* and UAHF specification.

## Related

[[triangular-arbitrage]] · [[fork-airdrop-triangulation]] · [[bitcoin-cash]] · [[ethereum-classic]] · [[hard-fork]] · [[2013-04-cyprus-banking-crisis-btc-pump]] · [[2013-2014-mtgox-premium-arbitrage]]
