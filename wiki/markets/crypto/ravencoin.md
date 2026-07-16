---
title: "Ravencoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, technical-analysis]
aliases: ["RVN"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://ravencoin.org/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[proof-of-work]]"]
---

# Ravencoin

**Ravencoin** (ticker **RVN**) is a [[proof-of-work|Proof-of-Work]] [[layer-1|Layer 1]] blockchain forked from [[bitcoin|Bitcoin]]'s codebase and dedicated to the creation and peer-to-peer transfer of digital assets ("tokens") on its own chain. Launched on 2018-01-03 with no pre-mine, no ICO, and no founder allocation, it is positioned as a fair-launch, [[real-world-assets|asset-issuance]] chain rather than a general-purpose smart-contract platform. It trades under the ticker RVN on its own UTXO-based, non-EVM mainnet.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | RVN |
| **Market Cap Rank** | #356 |
| **Market Cap** | $69.05M |
| **Current Price** | $0.00423 |
| **24h Volume** | $3.44M |
| **24h Change** | +0.40% |
| **7d Change** | -4.33% |
| **All-Time High** | $0.285 (2021-02-20) — **-98.5%** |
| **All-Time Low** | $0.00392 (2026-06-06) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The reading lands against an **extreme-fear** market backdrop ([[fear-and-greed-index|Fear & Greed Index]] = 23) and a long-horizon regime classified as an **"Established Bear Market"** as of 2026-06-21. RVN's roughly flat 24h move with a soft 7-day drift is consistent with a low-beta small cap drifting sideways-to-down in a risk-off tape. Note that RVN printed a fresh **all-time low of $0.00392 on 2026-06-06**; current pricing sits just above that floor, ~98.5% beneath its 2021 peak.

---

## Tokenomics & Supply

Ravencoin uses a fixed-issuance, Bitcoin-like emission schedule but with a far larger cap and faster block time.

| Metric | Value |
|---|---|
| **Circulating Supply** | ~16.30B RVN |
| **Total Supply** | ~16.31B RVN |
| **Max Supply** | 21.00B RVN |
| **MC / FDV Ratio** | ~1.00 (fully diluted ~$69.1M) |
| **Block Reward** | 2,500 RVN (halving on a ~4-year schedule) |
| **Block Time** | ~1 minute |
| **Consensus** | Proof of Work (KAWPOW algorithm, ASIC-resistant by design) |

About **78%** of the 21B max supply (~16.3B RVN) is already mined. Because emission is fixed and mined (not unlocked from an insider schedule), MC ≈ FDV — there is no vesting overhang. Remaining issuance enters via block rewards that halve roughly every four years, so forward dilution decelerates over time, unlike emission/airdrop tokens such as [[movement]] or [[plasma]].

- **Fair launch:** no pre-mine, no founder/VC allocation, no ICO. All RVN entered circulation through mining, mirroring [[bitcoin|Bitcoin]]'s distribution ethos.
- **Asset issuance fees:** creating a new asset on Ravencoin burns RVN (e.g., 500 RVN to issue a main asset), giving the token a built-in deflationary sink tied to network usage.
- Originally launched on the X16R algorithm, Ravencoin migrated to **KAWPOW** in 2020 to resist ASIC centralization and favor GPU miners.

---

## Market Structure & Derivatives

RVN is a **spot-only** asset with no significant perpetual-futures market. Liquidity is concentrated on centralized exchanges; it does not have a meaningful native DEX presence because it runs on its own non-EVM UTXO chain.

| Venue | Type | Typical Pair |
|---|---|---|
| Binance | CEX (spot) | RVN/USDT |
| Upbit | CEX (spot) | RVN/KRW |
| Bitget | CEX (spot) | RVN/USDT |
| KuCoin | CEX (spot) | RVN/USDT |
| Crypto.com | CEX (spot) | RVN/USD |

- Trading is dominated by Korean (Upbit/KRW) and global USDT pairs. With ~$3.44M of 24h volume against a ~$69M cap (~5% turnover), RVN trades a modest fraction of its float daily, so slippage on larger orders can be material.
- There is no liquid [[hyperliquid|Hyperliquid]]/perp listing for RVN, so [[funding-rate]] and open-interest dynamics are not a primary driver of price the way they are for the perp-listed alts in this group. RVN is best treated as a spot, low-liquidity name.

---

## Use Case / Narrative / Category

Ravencoin's thesis is narrow and deliberate: **tokenized asset creation and transfer on a dedicated PoW chain**.

- **Asset issuance:** anyone can mint named, fungible or non-fungible assets (e.g., security tokens, gaming items, collectibles, reward shares) without writing smart-contract code.
- **Categories:** Proof of Work, [[real-world-assets|Real World Assets (RWA)]], asset-issuance / "tokenization," Made-in-USA. It is frequently grouped with RWA and PoW narratives rather than DeFi.
- **Differentiation:** unlike [[ethereum|Ethereum]]-based token standards, RVN's asset layer is built into the base protocol, and its fair-launch PoW design appeals to users who distrust pre-mined, VC-heavy chains.

---

## Valuation Framing (qualitative)

RVN is valued as a **legacy, fair-launch PoW asset-issuance chain** competing in an [[real-world-assets|RWA]]/tokenization category now dominated by far larger and better-capitalized players ([[ethereum]] L2s, institutional RWA chains). Its appeal is structural integrity — no pre-mine, no VC allocation, a hard 21B cap, MC ≈ FDV — rather than growth. Trading near all-time lows at a ~$69M cap and ~98.5% below ATH, the market prices RVN as a faded narrative with a small, durable community but limited new-issuance traction. The bull case is narrow: a renewed tokenization wave that favors a credibly neutral base-layer asset registry; the base case is continued small-cap drift tracking the broader PoW-alt decline. As a GPU-mined chain, RVN's valuation also has a soft floor/ceiling tied to miner economics and hashrate.

---

## Peer Comparison

| Asset | Ticker | Mkt-cap rank | Category | Consensus | Supply | From ATH |
|---|---|---|---|---|---|---|
| **Ravencoin** | RVN | #356 | PoW asset-issuance / RWA | PoW (KAWPOW) | 21B cap, ~78% mined | -98.5% |
| [[bitcoin]] | BTC | #1 | Store of value | PoW (SHA-256) | 21M cap | below ATH |
| [[nockchain]] | NOCK | #294 | ZK "useful PoW" | ZKPoW | 2^32 cap | -81% |
| [[ethereum]] | ETH | top 2 | Smart-contract / RWA settlement | PoS | ~Net-flat | below ATH |

RVN shares Bitcoin's fair-launch, capped-supply PoW ethos but applies it to a niche asset-issuance use case; within the PoW cohort it is an older, GPU-mined chain rather than a new ZK-compute entrant like NOCK.

---

## Notable History

- **2018-01-03:** Mainnet launch (fair launch, no pre-mine). Early backing came from Overstock/Medici Ventures, whose then-CEO Patrick Byrne publicized a multi-million-dollar investment into the project's commercial development.
- **2018:** Asset layer ("Raven Assets") activated, enabling on-chain token issuance.
- **2020:** Algorithm migration from X16R to **KAWPOW** to maintain GPU-miner decentralization and resist ASICs.
- **2021-02-20:** RVN reached its all-time high of **$0.285**, benefiting from the GPU-mining and tokenization narratives.
- **2026-06-06:** Printed a fresh all-time low of **$0.00392** during the broad small-cap bear.
- **2026:** Trading deep in a multi-year drawdown (~98.5% below ATH), reflecting the risk-off regime and rotation away from older PoW alts.

---

## Risks

- **Single-narrative dependency:** the entire thesis rests on asset issuance / RWA adoption, a category dominated by far larger competitors (institutional RWA chains, [[ethereum|Ethereum]] L2s). Limited mainstream issuance traction is a persistent overhang.
- **PoW security budget:** as a smaller-cap GPU-mined chain, RVN's hashrate-backed security is modest and could be vulnerable to 51% pressure if interest fades; smaller PoW coins have historically suffered reorg attacks.
- **Liquidity / small-cap beta:** thin volume relative to cap (~$3.44M/day, ~5% turnover) means high volatility and slippage; in an **extreme-fear (F&G 23), established-bear** regime, low-conviction small caps like RVN are prone to sharp, illiquid drawdowns. RVN is trading just above its 2026-06-06 all-time low.
- **No smart-contract programmability:** the deliberately narrow design limits composability versus EVM ecosystems, capping the addressable use cases.
- **Stalled developer momentum:** as a volunteer-led open-source project without a funded foundation, development cadence depends on community contributors.

> *Risk note: small-cap, low-liquidity PoW asset trading deep below its all-time high during an established bear market. Position sizing and slippage assumptions should reflect thin order books.*

---

## Related

- [[crypto-markets]]
- [[bitcoin]]
- [[nockchain]]
- [[proof-of-work]]
- [[real-world-assets]]
- [[ethereum]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RVN |
| **Market Cap Rank** | #367 |
| **Market Cap** | $62.91M |
| **Current Price** | $0.00384781 |
| **Genesis Date** | 2018-01-03 |
| **Hashing Algorithm** | x16r |
| **Categories** | Smart Contract Platform, Real World Assets (RWA), Proof of Work (PoW), Made in USA |
| **Website** | [https://ravencoin.org/](https://ravencoin.org/) |

---

## Overview

Ravencoin is a blockchain specifically dedicated to the creation and peer-to-peer transfer of assets. Just as Monero is solely focused on privacy, Ravencoin specializes in asset transfer – nothing more, nothing less. Although you can exchange assets over other blockchains, like Bitcoin and Ethereum, that’s not their intended purpose. And the lack of specialization leads to problems that are specific to transferring assets. Ravencoin enables you to create and trade any real-world (e.g., gold bars, land deeds) or digital (e.g., gaming items, software licenses) assets on a network with only that in mind.

Ravencoin doesn’t have an established team. It’s an open-source project led by the core developers: RavoncoinDev, Tron, and Chatturga (discord usernames). Bruce Fenton, Board Member of The Bitcoin Foundation, advises the team. The core developers launched Ravencoin on January 3rd, 2018 and Fenton kicked off the launch with a Tweet announcing the start of mining. The project gained some notoriety when Overstock CEO Patrick Byrne announced that his company had made a multi-million dollar investment into the team. Since then, the team has been building out the core functionality of asset support and rewards capabilities.

The release of the Ravencoin mainnet and increase in activity on the platform should help the price. Any news of notable companies or financial institutions utilizing the platform should also have a positive effect. Ravencoin offers just one thing: tokenized asset transfer. And that singular focus isn’t a bad thing. When projects attempt to solve a bunch of problems at once, they often create a bunch of half-baked solutions. Ravencoin is avoiding that. As a young project with seemingly endless competition, it’s difficult to predict how successful Ravencoin will be. An active community and backing from one of the most respected names in online retail are positive indicators, though. There’s a clear trend toward the tokenization of all types of assets. Ho...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.35B RVN |
| **Total Supply** | 16.35B RVN |
| **Max Supply** | 21.00B RVN |
| **Fully Diluted Valuation** | $62.92M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2852 (2021-02-20) |
| **Current vs ATH** | -98.65% |
| **All-Time Low** | $0.00362196 (2026-07-01) |
| **Current vs ATL** | +6.44% |
| **24h Change** | +0.16% |
| **7d Change** | +3.20% |
| **30d Change** | -13.59% |
| **1y Change** | -73.60% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RVN/TRY | N/A |
| Upbit | RVN/KRW | N/A |
| Bitget | RVN/USDT | N/A |
| KuCoin | RVN/USDT | N/A |
| Crypto.com Exchange | RVN/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ravencoin.org/](https://ravencoin.org/) |
| **Twitter** | [@ravencoin](https://twitter.com/ravencoin) |
| **Reddit** | [https://www.reddit.com/r/Ravencoin](https://www.reddit.com/r/Ravencoin) |
| **Telegram** | [RavencoinDev](https://t.me/RavencoinDev) (6,101 members) |
| **Discord** | [https://discordapp.com/invite/CqbfUZd](https://discordapp.com/invite/CqbfUZd) |
| **GitHub** | [https://github.com/RavenProject/Ravencoin](https://github.com/RavenProject/Ravencoin) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,054 |
| **GitHub Forks** | 648 |
| **Pull Requests Merged** | 544 |
| **Contributors** | 53 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.12M |
| **Market Cap Rank** | #367 |
| **24h Range** | $0.00383157 — $0.00392117 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
