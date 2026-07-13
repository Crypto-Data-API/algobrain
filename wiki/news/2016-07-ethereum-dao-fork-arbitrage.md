---
title: "Ethereum DAO Fork Arbitrage (July 2016)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [news, crypto, ethereum, history, arbitrage, event-driven]
aliases: ["DAO Fork Arb", "ETC Fork", "Ethereum Classic Split"]
event_date: 2016-07-20
markets_affected: [crypto]
impact: high
verified: true
sources_count: 3
related: ["[[hard-fork]]", "[[replay-attack]]", "[[fork-airdrop-triangulation]]", "[[2016-06-the-dao-hack]]", "[[ethereum-classic]]", "[[ethereum]]"]
---

# Ethereum DAO Fork Arbitrage (July 2016)

On **July 20, 2016 at block 1,920,000**, Ethereum executed a [[hard-fork]] to roll back The DAO hack — and a non-trivial minority of miners and users refused. The dissenting chain became **[[ethereum-classic|Ethereum Classic (ETC)]]**, the first major contentious split in crypto and the **template for every fork arbitrage that followed**. Where the [[2017-08-bitcoin-cash-fork-arbitrage|Bitcoin Cash split]] is the *operational* template, the DAO fork is the *philosophical* template — a community refusing to ratify a state-rollback created a chain whose primary value driver was ideological, not technical.

## Background

Following the [[2016-06-the-dao-hack|DAO hack of June 17, 2016]] (3.6M ETH drained via reentrancy), Vitalik Buterin and the Ethereum Foundation proposed a hard fork to redirect the stolen funds to a withdrawal contract. The community split:

- **Pro-fork (~85%):** Pragmatists — recover the funds; The DAO held ~15% of all ETH and a default would devastate the ecosystem.
- **Anti-fork (~15%):** "Code is law" purists — the attacker followed the contract's rules; rolling back state violates blockchain immutability.

A non-binding "carbonvote" (token-weighted) showed ~85% support for the fork. Activation was set for block 1,920,000.

When the fork activated, Poloniex (controversially) listed the unforked chain as **ETC** within hours, defying the assumption that miners and users would unanimously follow the canonical chain. The split became persistent.

## The Trade

The DAO fork created a textbook **forced-airdrop arbitrage**:

```
Pre-fork: 1 ETH (single asset)
Post-fork: 1 ETH (forked chain) + 1 ETC (unforked chain)
```

But unlike subsequent forks, **most market participants did not expect ETC to have meaningful value**. The pre-fork consensus assumed the unforked chain would die. When Poloniex listed ETC at ~$0.50-1.00 within 24 hours of the fork, the market discovered an unanticipated airdrop.

### Trade 1: Pre-fork accumulation

Sophisticated traders who recognized that an Ethereum split was probable accumulated ETH through July 2016, knowing they would receive 1:1 ETC at the snapshot. ETH traded $11-13 in the days before the fork; the post-fork ETH+ETC value briefly traded as high as $14-15 before settling.

### Trade 2: Cross-exchange listing arb

Poloniex was first to list ETC. Bitfinex followed within a week. Kraken delayed several weeks. **Coinbase did not credit ETC to customers for nearly a year**, which became a class-action lawsuit in 2017. Anyone who could move ETH from Coinbase to Poloniex pre-fork captured the entire ETC value; Coinbase customers lost it (until eventually credited).

### Trade 3: Replay-attack arbitrage

The fork launched **without replay protection** — see [[replay-attack]]. For the ~10 weeks until EIP-155 activated, transactions on either chain could be replayed on the other. Sophisticated parties:

- Drained customer ETC balances by replaying ETH withdrawals.
- Charged 0.5-1% for "splitting" services.
- Captured value during the operational confusion at exchanges that hadn't yet implemented protection.

### Trade 4: Philosophy premium trade

ETC's price was driven not by technology (it was identical to ETH at fork) but by community ideology. Long-only ETC bulls were a small but committed cohort. Cross-chain pair trading (long ETC / short ETH, betting on ETC's "true Ethereum" narrative) was profitable in late 2016 as ETC rallied from $1 to ~$2 while ETH stagnated near $10-12.

## Price Action

| Date | ETH | ETC | ETH+ETC | Notes |
|------|-----|-----|---------|-------|
| Jul 19, 2016 | $12.50 | n/a | $12.50 | Pre-fork |
| Jul 20, 2016 | $12.20 | $0.75 (Poloniex initial) | $12.95 | Fork day |
| Jul 27, 2016 | $11.80 | $1.85 | $13.65 | ETC pump on listings |
| Aug 17, 2016 | $11.40 | $1.45 | $12.85 | Replay-attack period winds down |
| Dec 31, 2016 | $8.10 | $1.45 | $9.55 | Crypto-bear bottom |
| Jun 2017 | $370 | $20 | $390 | ICO-mania bull |
| 2021 ATH | $4,800 | $170 | — | Both peaked in 2021 supercycle |

ETC settled to roughly **5-15% of ETH's market cap** for most of its history — a remarkably stable ratio given the divergent technical roadmaps.

## Winners

- **Poloniex** — Captured first-mover advantage in ETC listing; volume soared in summer 2016.
- **Pre-fork ETH accumulators** — Long ETH desks (Polychain Capital was rumored to have been positioned) captured the unanticipated ETC distribution.
- **Splitter operators** — Companies like ETC.split charged 0.5-1% to safely split coins during the replay window.
- **Anti-fork mining pools** — Continued mining ETC at low difficulty initially (the chain didn't immediately retarget), capturing block rewards during the chaos.

## Losers

- **Coinbase customers** — Coinbase did not credit ETC until ~9 months later; class-action litigation followed.
- **Replay-attack victims** — Users who withdrew ETH without splitting first sometimes lost their ETC (or vice versa) when transactions were replayed.
- **Anti-fork ideological holders** — Many "code is law" purists who held ETC long-term saw it underperform ETH dramatically (5-10x relative drawdown over 2016-2024).

## Lessons

1. **The market often misprices fork value pre-snapshot.** ETC was assumed to be worthless; the pre-fork ETH price did not include the ETC option premium. The same mispricing recurred at BCH (2017) and ETHW (2022) but in the opposite direction (pre-fork futures over-priced the airdrop).
2. **Exchange listing decisions create persistent value.** Poloniex's unilateral ETC listing arguably *created* ETC's market value — without it, the unforked chain might have died. Similar dynamics would later play out for BSV (Binance), ETHW (OKEx), and minor airdrops.
3. **Replay protection is now table stakes.** The DAO fork's lack of replay protection burned customers and exchanges; every subsequent contentious fork has launched with chain-ID-bound signing.
4. **Philosophy is a tradeable factor in crypto.** ETC's "code is law" community supported a multi-billion-dollar market cap for years despite minimal technical innovation. Similar dynamics have appeared with BSV and other "purist" forks.
5. **Pre-fork pair trades work.** Long ETH / Short ETH-future-perp captures the airdrop without directional risk. This template was refined in the 2022 ETHW Merge fork.

## Aftermath

- **2017-2018 ICO bull:** ETC rallied to $45 alongside ETH's $1,400. Diverged thereafter.
- **2020 Halving meta:** ETC retained PoW, became briefly attractive after Ethereum's Merge.
- **51% attacks:** ETC suffered multiple successful 51% attacks (January 2019, August 2020) due to low hashrate, structurally undermining its credibility.
- **Post-Merge (2022+):** ETC briefly benefited from displaced ETH miners but failed to attract development, settling at ~5% of ETH's market cap.

## Sources

- Vitalik Buterin, "Hard Fork Completed," **Ethereum Foundation blog**, July 20, 2016.
- Coinbase blog and class-action filings on ETC distribution to customers (2017).
- **EIP-155** (Vitalik Buterin), October 2016 — replay protection.
- *Mastering Ethereum* (Antonopoulos & Wood, 2018), Ch. 6 on the DAO fork.

## Related

[[hard-fork]] · [[replay-attack]] · [[fork-airdrop-triangulation]] · [[2016-06-the-dao-hack]] · [[ethereum-classic]] · [[ethereum]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2022-09-ethereum-merge-fork-arbitrage]]
