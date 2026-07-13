---
title: "Hard Fork"
type: concept
created: 2026-04-27
updated: 2026-06-11
status: good
tags: [crypto, market-microstructure, history, event-driven]
aliases: ["Chain Split", "Contentious Fork", "Hard Fork"]
related: ["[[fork-airdrop-triangulation]]", "[[replay-attack]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]", "[[2016-07-ethereum-dao-fork-arbitrage]]", "[[2018-11-bitcoin-cash-sv-fork-arbitrage]]", "[[2022-09-ethereum-merge-fork-arbitrage]]", "[[2017-10-bitcoin-gold-fork-arbitrage]]", "[[2020-03-steem-hive-fork-arbitrage]]", "[[2022-05-terra-luna-2-fork-arbitrage]]", "[[2026-fork-watchlist]]"]
domain: [market-microstructure]
prerequisites: ["[[bitcoin]]", "[[ethereum]]", "[[blockchain]]"]
difficulty: intermediate
---

# Hard Fork

A **hard fork** is a backwards-incompatible change to a blockchain's consensus rules. Nodes running the old software reject blocks produced under the new rules (and vice versa), causing the chain to split into two persistent histories whenever a non-trivial minority refuses to upgrade. For trading, the relevant property is that **every address holding the parent asset at the snapshot block automatically holds the same balance on the new chain** — a free distribution that creates the canonical fork-arbitrage opportunity.

## Hard Fork vs Soft Fork

| | Hard Fork | Soft Fork |
|---|-----------|-----------|
| Compatibility | Old nodes reject new blocks | Old nodes accept new blocks |
| Rule change | Loosens or fundamentally changes | Tightens existing rules |
| Chain split risk | High (if minority refuses upgrade) | Low (minority just produces invalid blocks under new rules) |
| Creates airdrop? | **Yes** if contentious | No |
| Examples | Bitcoin Cash (2017), ETH/ETC (2016), ETHW (2022) | SegWit (2017), Taproot (2021) |

This distinction is the load-bearing one for traders: **only contentious hard forks create distributable airdrops**. Cooperative hard forks (e.g., Ethereum's roadmap upgrades like Berlin, London, Shanghai) are treated as software upgrades, not as splits, because no significant minority preserves the old chain.

## Mechanics

1. **Announcement.** Developers publish a target activation block height and the new consensus rules. Examples: Bitcoin's UAHF specification preceded the BCH split by ~2 weeks; Ethereum's Merge had a target Total Terminal Difficulty (TTD) instead of a block height.
2. **Snapshot.** At the activation block, every UTXO (Bitcoin-style) or account balance (Ethereum-style) is preserved on both chains.
3. **Replay risk window.** Until [[replay-attack|replay protection]] is in place, a transaction signed for one chain may be valid on the other, leaking coins.
4. **Difficulty adjustment.** New chains often start with adjusted or rolling difficulty mechanisms (BCH's Emergency Difficulty Adjustment, ETC's Modified ETC) to attract hashrate without freezing the chain.
5. **Exchange credit.** Each centralized exchange independently decides whether to credit, when to enable trading, and whether to distribute or sell on customers' behalf.

## Why Forks Create Airdrops

Because consensus rules disagree only about *which blocks are valid going forward*, the historical chain (including everyone's balances) is shared. Splitting the rule set without splitting the ledger means **the same key controls coins on both chains**. There is no minting event — just two histories diverging from a common root. From a holder's perspective this looks identical to a free distribution proportional to pre-snapshot holdings.

## Trading Implications

The structural inefficiencies that hard forks expose:

- **Exchange credit asymmetry.** [[fork-airdrop-triangulation|Fork triangulation]] depends on this — Coinbase delayed BCH crediting until December 2017 while Bitfinex enabled trading on August 1, creating a multi-month venue arb.
- **Pre-fork futures (IOUs).** Markets like Bitfinex, OKEx, Poloniex, and later Hyperliquid list "I Owe You" tokens that pre-trade the forked asset. See [[fork-futures-spot-basis]].
- **Mining-difficulty arb.** Asymmetric difficulty adjustment between chains rewards miners who flip hashpower based on real-time profitability (BCH's EDA created multi-day windows where mining BCH paid 2-3x BTC).
- **Replay-attack arbitrage.** Until [[replay-attack|replay protection]] activates, sophisticated actors can exploit the fact that one signed transaction can move coins on both chains.
- **Claim-and-dump.** Holders abandon the minor fork; sell the airdropped coin into thin launch liquidity. Retail typically dumps at 30-70% discount to peak within 30 days.

## Major Hard Forks (Trader's Perspective)

| Date | Parent → Fork | Outcome | Arb Window |
|------|---------------|---------|------------|
| 2016-07-20 | ETH → ETC ([[2016-07-ethereum-dao-fork-arbitrage|DAO fork]]) | Split persisted; ETC ~5-10% of ETH initially | 2-6 weeks (exchange listing lag) |
| 2017-08-01 | BTC → BCH ([[2017-08-bitcoin-cash-fork-arbitrage|UAHF]]) | $46B BCH peak market cap; persistent | 4-6 months (Coinbase credit delay) |
| 2017-10-24 | BTC → BTG ([[2017-10-bitcoin-gold-fork-arbitrage|Bitcoin Gold]]) | Premine controversy + 51% attack May 2018; faded to <1% of BTC | 1-2 weeks fork; multi-year tail |
| 2017-11-24 | BTC → BCD (Bitcoin Diamond) | Promotional/scammy; <$10M arb | <1 week |
| 2018-02-28 | BTC + ZCL → BTCP (Bitcoin Private) | Hidden 3M premine discovered May 2018; collapsed 95% | 4-6 weeks |
| 2018-02-18 | LTC → LCC (Litecoin Cash) | 10:1 ratio; promotional; <$0.15 peak | <2 weeks |
| 2018-11-15 | BCH → BSV ([[2018-11-bitcoin-cash-sv-fork-arbitrage|hash war]]) | Both chains survived; failure case for arbs | 2-3 weeks of volatility |
| 2018-2019 | XMR semi-annual anti-ASIC forks | Network-unified; no chain-split | Mining-difficulty arb (1-2 weeks per fork) |
| 2020-03-20 | STEEM → HIVE ([[2020-03-steem-hive-fork-arbitrage|Hive]]) | Defensive fork against exchange-coordinated 51% attack | 2-4 weeks |
| 2020-11-15 | BCH → BCHA / BCH (IFP miner-tax dispute) | BCHA collapsed 90% in 4 weeks | 2-4 weeks |
| 2022-05-28 | LUNA → Luna 2.0 / LUNC ([[2022-05-terra-luna-2-fork-arbitrage|Terra revival]]) | Chain-swap with bifurcated snapshot; Luna 2.0 collapsed 90% in 30 days | 2-6 weeks |
| 2022-09-15 | ETH → ETHW ([[2022-09-ethereum-merge-fork-arbitrage|Merge]]) | ETHW collapsed 90% in 6 weeks | 2-4 weeks |

## What Kills the Fork-Arb Edge

- **Standardized exchange policies.** Major exchanges have largely converged on "we credit but may delay listing," compressing the cross-venue spread.
- **Liquid pre-fork derivatives.** IOU futures on Hyperliquid, OKEx, and dYdX increasingly price the fork value efficiently before the snapshot.
- **Fewer contentious forks.** Post-2022, major chains have avoided controversial splits — the airdrop frontier has shifted to [[airdrop-farming|protocol airdrops]].

## Related

[[fork-airdrop-triangulation]] · [[replay-attack]] · [[fork-futures-spot-basis]] · [[airdrop-farming]] · corporate-action-arbitrage · [[2017-10-bitcoin-gold-fork-arbitrage]] · [[2020-03-steem-hive-fork-arbitrage]] · [[2022-05-terra-luna-2-fork-arbitrage]] · [[2026-fork-watchlist]] · [[bitcoin-cash]] · [[ethereum-classic]] · [[ethereum-pow-iou]]

## Sources

- Bitcoin Cash UAHF specification (Bitcoin ABC, 2017).
- Ethereum DAO fork: Ethereum Foundation blog, July 2016.
- ETHW fork: Ethereum Foundation Merge announcement, August 2022.
- Andreas Antonopoulos, *Mastering Bitcoin* (2nd ed., 2017), Ch. 10 — fork mechanics.
