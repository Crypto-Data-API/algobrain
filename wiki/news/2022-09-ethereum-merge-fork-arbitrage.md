---
title: "Ethereum Merge / ETHW Fork Arbitrage (September 2022)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, ethereum, history, hard-fork, airdrop, triangular-arbitrage]
aliases: ["ETHW Fork", "ETH PoW Fork", "Merge Fork", "ETH/ETHW Split"]
event_date: 2022-09-15
markets_affected: [crypto]
impact: high
verified: true
sources_count: 5
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[fork-futures-spot-basis]]", "[[ethereum]]", "[[ethereum-pow-iou]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]"]
---

# Ethereum Merge / ETHW Fork Arbitrage (September 2022)

At **block 15,537,393, around 06:43 UTC on September 15, 2022**, Ethereum executed The Merge — transitioning from proof-of-work to proof-of-stake. A coalition of miners led by Chandler Guo refused to follow the transition and forked the chain, creating **Ethereum PoW (ETHW)**. Every pre-Merge ETH holder received an equivalent quantity of ETHW, generating a $2-5B aggregate airdrop and **the most actively pre-traded fork in crypto history** thanks to mature IOU futures markets at OKEx, Poloniex, MEXC, and Bybit.

## Background

The Merge had been roadmapped for 6+ years. Unlike the [[2016-07-ethereum-dao-fork-arbitrage|DAO fork]] or the [[2017-08-bitcoin-cash-fork-arbitrage|BCH fork]], it was **non-contentious from the developer/community standpoint** — the Ethereum Foundation, all major clients, and 90%+ of validators committed to the PoS chain.

What was contentious was the **miners' stake**. Roughly $19B/year of ETH issuance had flowed to miners under PoW; The Merge would reroute that to validators. A small coalition of miners, led by Chinese miner Chandler Guo and the f2pool/AntPool community, organized to fork the PoW chain rather than abandon their hashrate.

The fork was announced ~6 weeks pre-Merge (late July 2022). Exchanges began listing ETHW IOU futures within days.

## The Trade

The structural setup was the cleanest in fork-arb history:

- **Snapshot mechanics fully transparent.** Total Terminal Difficulty target was published; expected execution within ~24 hours of forecast.
- **Liquid pre-fork futures.** OKEx listed ETHW-USDT IOU perp at $58 in early September; Poloniex and MEXC followed.
- **Major exchanges committed credit policies in advance.** Binance, Kraken, Bitfinex, OKX all announced ETHW credit; Coinbase declined.
- **Replay protection built in.** ETHW used a distinct chain ID (10001), eliminating [[replay-attack]] risk.

### Trade 1: Long spot ETH + short ETHW pre-fork futures

The flagship arbitrage:

1. Buy spot ETH at ~$1,600 in early September.
2. Short ETHW-PERP on OKEx at $50-70 (notional value of expected airdrop).
3. Hold through Merge block.
4. Receive ETHW airdrop on participating exchanges.
5. Use airdropped ETHW to close the short.

The spread was significant — pre-fork ETHW IOU futures peaked at ~$140 in late August, well above the rational expectation of $20-50. Sophisticated desks shorted at $80-140 and covered at $5-10 within 6 weeks.

### Trade 2: Cross-exchange ETHW spread

Different exchanges enabled ETHW trading at different times:

- **Poloniex / MEXC:** Listed ETHW within hours.
- **OKX:** Within ~24 hours.
- **Binance:** Distributed ETHW airdrop but listed spot trading days later.
- **Coinbase:** Did not credit. Customers lost the airdrop.

ETHW traded $58 on Poloniex within 4 hours of the Merge while Binance customers couldn't transact for ~36 hours. Bridge-and-arb between venues captured 20-50% spreads in the first 48 hours.

### Trade 3: Mining-difficulty arbitrage

ETHW launched with the inherited Ethash difficulty from pre-Merge ETH (~10 PH/s effective hashrate target). Initial ETHW hashrate was ~30 TH/s — orders of magnitude below the target. Miners who pointed hashrate at ETHW captured **40-100% APY** in the first 2-3 weeks before difficulty caught up.

### Trade 4: Pre-fork mining redirection

ETC (Ethereum Classic) was the natural destination for displaced ETH miners. Pre-fork pair trade: long ETC / short ETHW pre-fork futures. ETC rallied from $26 to $40 in early September on the miner-influx narrative; ETHW collapsed from $58 to $5 over the following 6 weeks. The pair returned 200-400% in 6 weeks.

## Price Action

| Date | ETH | ETHW (IOU/spot) | Notes |
|------|-----|-----------------|-------|
| Aug 1, 2022 | $1,690 | $30 (early IOU) | ETHW IOUs first listed |
| Aug 31, 2022 | $1,540 | $138 (peak IOU) | Speculative IOU pump |
| Sep 5, 2022 | $1,560 | $63 | Post-pump fade |
| Sep 14, 2022 (pre-Merge) | $1,635 | $54 | T-1 day |
| Sep 15, 2022 (Merge) | $1,470 | $58 (Poloniex listing) | Sell-the-news ETH dip |
| Sep 22, 2022 | $1,330 | $11 | Week 1 collapse |
| Oct 15, 2022 | $1,300 | $5.50 | Stabilization |
| End 2022 | $1,200 | $3.20 | Long-tail decline |
| End 2024 | $3,400 | $2.30 | ETHW persistent at minimal value |

ETHW lost **96%+ of peak IOU value** within 3 months. The total airdropped ETHW supply (~120M) at September 15 launch price ($58) implied a $7B market cap that compressed to <$300M by year-end.

## Winners

- **Pre-Merge IOU shorts.** Desks shorting ETHW at $80-140 in August captured 90%+ on $billions of notional. Estimated $1-3B in extraction.
- **OKEx.** Built first-mover advantage in ETHW trading; fees during the IOU period were enormous.
- **Mining-difficulty arbs.** Hashrate rebalancing between ETHW and ETC delivered 40-100% APY in the first weeks.
- **Cross-exchange arbs.** First 48 hours of post-Merge listings had 20-50% spreads.
- **Long ETH / short ETHW pair traders.** Captured the airdrop value cleanly without parent-chain directional risk.

## Losers

- **Long-only ETHW IOU buyers.** Anyone who bought IOUs at $80-140 lost 90%+ within weeks.
- **Coinbase customers.** Did not receive ETHW airdrop. Class-action discussions but no major suit.
- **Miners who didn't pivot.** ETHW absorbed only ~20% of pre-Merge hashrate; most ETH miners faced 80%+ revenue collapse.
- **Naive fork-arb retail.** Many users bought spot ETHW at $58 expecting "fork narrative" pumps that never materialized.

## Lessons

1. **Mature pre-fork derivatives compress the structural edge.** Unlike BCH 2017 (where IOUs barely existed), ETHW IOUs traded for 6 weeks pre-fork. Sophisticated money already priced ~80% of the airdrop value into futures. The remaining edge was operational (cross-exchange listing lag, mining-difficulty arb).
2. **Pre-fork IOU markets often over-price the airdrop.** Peak ETHW IOU was $140 vs realized post-fork value of $5-10. The over-pricing reflected speculative narrative + retail hype, not fundamentals. The reverse-arb (short the IOU) was the highest-Sharpe trade.
3. **Replay protection is now standard.** ETHW launched with chain ID 10001; no [[replay-attack]] risk. The operational moat that benefited 2016-2017 desks has fully disappeared.
4. **Non-contentious forks generate weaker forks.** ETHW had only ~10% community support and ~20% hashrate. The fork persisted but at minimal economic value. Contrast BCH 2017 (~30% community support, $46B peak market cap).
5. **PoS transitions create one-time mining-displacement arbitrage.** ETH→PoS was the largest such event in crypto history. Future PoS transitions (if any) are likely smaller in scale.

## Aftermath

- **Ethereum:** Merged successfully; PoS validator set grew from 400k to 1.1M+ validators by 2024; net ETH issuance turned negative under EIP-1559.
- **ETHW:** Persists but with minimal economic activity; market cap typically <$300M; trading volume <$5M/day.
- **Mining ecosystem:** Most ETH miners pivoted to ETC, alternative PoW chains, or shut down. ETC hashrate 5x'd in late 2022 then partially decayed.
- **Fork-arb desks:** Largely retired the dedicated fork-arb book post-ETHW; refocused on [[airdrop-farming|protocol airdrops]] (ARB, OP, JTO, EIGEN). The fork-arb playbook now requires either (a) a major contentious fork (rare) or (b) a PoS transition on a major chain (none on horizon).

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[fork-futures-spot-basis]] · [[ethereum]] · [[ethereum-pow-iou]] · [[ethereum-classic]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2018-11-bitcoin-cash-sv-fork-arbitrage]]

## Sources

- Ethereum Foundation: "The Merge" announcement, August 24, 2022.
- OKEx blog: "ETHW Listing and Snapshot Policy," September 12, 2022.
- Binance blog: "ETHW Distribution to ETH Holders," September 15, 2022.
- Chandler Guo Twitter, July 2022 — fork organizing.
- Galaxy Research, "Post-Merge Fork Tracker," October 2022.
