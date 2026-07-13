---
title: "Bitcoin Cash / BSV Hash War Fork Arbitrage (November 2018)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, bitcoin, history, arbitrage, event-driven]
aliases: ["BCH/BSV Split", "Hash War", "BCH ABC vs BSV"]
event_date: 2018-11-15
markets_affected: [crypto]
impact: high
verified: true
sources_count: 4
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]", "[[bitcoin-cash]]", "[[replay-attack]]"]
---

# Bitcoin Cash / BSV Hash War Fork Arbitrage (November 2018)

On **November 15, 2018**, Bitcoin Cash hard-forked into **Bitcoin Cash ABC (BCHA, later just BCH)** and **Bitcoin SV (BSV — "Satoshi's Vision")**. The split was driven by an irreconcilable conflict between Roger Ver / Bitmain (BCHA) and Craig Wright / Calvin Ayre (BSV) over block-size scaling and protocol changes. Unlike the [[2017-08-bitcoin-cash-fork-arbitrage|2017 BCH fork]] — a clean template that minted billions in extracted value — the BSV fork is the **canonical failure case** for fork arbitrage: a hash-war environment where directional volatility overwhelmed the structural arb edge.

## Background

After the 2017 BCH fork, control of the Bitcoin Cash protocol fragmented between two camps:

- **Bitcoin Cash ABC (Roger Ver / Amaury Séchet / Bitmain):** Wanted to add a Canonical Transaction Ordering Rule (CTOR), DSV opcode, and a "miner tax" funding development.
- **Bitcoin SV (Craig Wright / Calvin Ayre / nChain):** Wanted to remove the block-size cap, restore original Satoshi opcodes, and revert any post-Satoshi protocol changes.

Both sides committed major hashrate to the fork. The result was a **hash war** — each side mining empty/dummy blocks on the other's chain to disrupt confirmations. Both Coinbase and Binance suspended BCH trading hours before the split.

## The Trade That Failed

A trader applying the [[2017-08-bitcoin-cash-fork-arbitrage|2017 BCH playbook]] would expect:

```
Pre-fork: 1 BCH = $400
Post-fork: 1 BCHA + 1 BSV = expected $400+ combined
```

Reality:

| Date | BCH (pre) | BCHA (post) | BSV | Combined |
|------|-----------|-------------|-----|----------|
| Nov 14, 2018 | $425 | — | — | $425 |
| Nov 15, 2018 (fork day) | — | $290 | $90 | $380 |
| Nov 16, 2018 | — | $250 | $115 | $365 |
| Nov 22, 2018 | — | $185 | $80 | $265 |
| Dec 15, 2018 | — | $90 | $58 | $148 |
| Apr 2019 | — | $300 | $63 | $363 |

**Crypto markets crashed in mid-November 2018**. BTC dropped from $6,300 to $4,200 in the same window — a ~33% drawdown. The fork arbitrage edge (a ~3-5% premium over the parent chain) was annihilated by **a 30%+ directional move in the underlying** during the hold-through-fork period.

## Why It Failed

1. **Macro tape-bomb timing.** Crypto's 2018 bear market accelerated mid-fork. The mark-to-market loss on holding the parent BCH dwarfed the fork value.
2. **Hash war disrupted exchanges.** Coinbase, Kraken, and others suspended BCH deposits/withdrawals for days, freezing arbitrage capital exactly when it needed to move.
3. **No clear winner for hours.** The chain with the most cumulative proof-of-work was unclear for ~12 hours post-fork. Both BCHA and BSV claimed to be "the real BCH." Exchanges initially listed both as separate tickers, then some retroactively renamed.
4. **BSV ideological discount.** The market priced BSV at ~30% of BCHA, reflecting its lower exchange support and Craig Wright's reputational problems. The combined value was lower than the pre-fork BCH, not higher.
5. **Mining death spirals.** BSV's hashrate collapsed when the war ended; BCHA's hashrate also fell sharply. Mining-difficulty arbitrage was minimal because both chains were unprofitable for most miners.

## What Did Work

A subset of trades still extracted value:

- **Pre-fork short BCH / long BTC.** Predicting that the hash war would damage BCH credibility worked: BCH dropped from $425 to $90 within 4 weeks. A short BCH / long BTC pair captured ~50%+ even after the fork airdrop.
- **Long BCHA / short BSV.** Once the chains stabilized, BCHA was the clearer "winner" for liquidity reasons (Coinbase, Kraken supported BCHA primary). BCHA outperformed BSV from December 2018 onward.
- **Replay-attack splitter services.** As with prior forks, splitting services charged 0.5-1% during the [[replay-attack|replay window]]; this was profitable in absolute terms.

## Winners

- **Binance** — Captured first-listing advantage on both BCHA and BSV; fees on hash-war volatility surged.
- **Short-BCH macro traders** — The bear-market timing made BCH a high-conviction short.
- **Calvin Ayre** — His long-BSV position absorbed initial losses but rallied to $400+ in 2019-2020 when BSV briefly captured ideological "Satoshi" momentum.

## Losers

- **Naive fork-arb traders** — Anyone applying the 2017 BCH playbook without a directional hedge lost 20-40% of capital deployed in the fork window.
- **Bitmain** — Devoted significant treasury to the hash war; reported ~$700M loss in 2018; IPO failed.
- **Long-BSV ideologues** — BSV's price collapsed 95%+ from 2021 highs after Craig Wright lost successive court cases (2024-2025).

## Lessons for Fork Arbitrage

1. **Directional risk dominates fork value when timing collides with bear markets.** The 2017 BCH fork worked partly because crypto was in mid-bull-run; the 2018 BSV fork failed partly because it landed mid-bear. Always hedge the parent asset directionally before the snapshot.
2. **Hash wars freeze the exchange layer.** When trading is suspended, fork-credit-arb capital is stranded. Diversify across exchanges that less reliant on emergency suspensions.
3. **Multiple-chain forks halve the per-asset opportunity.** A 2-way split distributes value across BCHA + BSV; a 3-way split would be even worse. The simpler the fork, the cleaner the arb.
4. **Ideological divisions are a failure mode for fork value.** When a fork is about *who controls the protocol* rather than *what the protocol does*, both sides bleed credibility and the combined value can be lower than the parent.
5. **The 2017 BCH success was not the median — it was the outlier.** Fork-arb desks that benchmarked off BCH 2017 over-allocated to BSV 2018. Realistic benchmarking needs survivorship-bias correction.

## Aftermath

- **2018-2019:** BCHA renamed to just BCH; BSV traded at 20-30% of BCH for years.
- **2020-2021:** BSV briefly rallied as Craig Wright pursued legal claim to be Satoshi.
- **2024:** UK High Court ruled Wright is not Satoshi; BSV collapsed below $50.
- **Fork-arb desks:** Most reduced fork-arb allocation post-2018; refocused on protocol airdrops (UNI 2020, ARB 2023) where the mechanics are cleaner.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2022-09-ethereum-merge-fork-arbitrage]] · [[bitcoin-cash]] · [[replay-attack]] · [[failure-modes]]

## Sources

- Binance blog: "BCH Fork Suspension," November 14, 2018.
- Coinbase blog: "Bitcoin Cash hard fork," November 13, 2018.
- *CoinDesk* coverage of the BCH/BSV hash war, November 2018.
- Court filings, Kleiman v. Wright, 2019-2024 — Craig Wright reputation timeline.
