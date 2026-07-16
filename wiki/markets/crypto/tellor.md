---
title: "Tellor Tributes"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle]
aliases: ["TRB", "Tellor"]
entity_type: protocol
headquarters: "Decentralized"
website: "http://www.tellor.io/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-manipulation]]", "[[pyth-network]]"]
---

# Tellor Tributes

**Tellor Tributes** (ticker **TRB**) is the staking and dispute token of Tellor, an [[ethereum|Ethereum]]-based decentralized oracle that brings off-chain data on-chain through a **crypto-economic, dispute-driven mechanism**. Originally a proof-of-work-style oracle where miners competed to submit data, Tellor now runs a **staking-based** model: reporters stake TRB to submit values, and any incorrect data can be challenged and slashed via on-chain disputes. Tellor's design prioritizes censorship resistance and permissionless reporting over update speed.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | TRB |
| **Current Price** | $13.78 |
| **Market Cap** | $38.52M |
| **Market Cap Rank** | #543 |
| **24h Volume** | $9.00M |
| **24h Change** | -1.25% |
| **7d Change** | +2.44% |
| **Fully Diluted Valuation** | $39.54M |
| **All-Time High** | $593.09 (2023-12-31) |
| **All-Time Low** | $0.0100 (2019-11-01) |
| **Chain** | [[ethereum\|Ethereum]] (+ Polygon, Arbitrum, Optimism, Gnosis, others) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

TRB is down ~1.3% on the day and up ~+2.4% over the week, holding up while the **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] reads 23 (extreme fear)** in an **established bear market**. At ~$13.78 the token trades roughly -98% below its late-2023 ATH of $593.09, but is up enormously (>137,000%) from its 2019 all-time low of $0.0100. Notably, daily volume (~$9.0M) is **~23% of the entire market cap** ($38.52M) — an unusually high turnover ratio that reflects TRB's reputation as a speculative, low-float trading vehicle rather than a buy-and-hold.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.79M TRB |
| **Total Supply** | ~2.87M TRB |
| **Max Supply** | Uncapped (inflationary reporting rewards) |
| **Fully Diluted Valuation** | $39.54M |
| **Market Cap / FDV** | ~0.97 |
| **All-Time High** | $593.09 (2023-12-31) |
| **All-Time Low** | $0.0100 (2019-11-01) |

TRB has a **small, low-float supply** (~2.8M tokens) and is **inflationary**: new TRB is minted as rewards for reporters who submit data and for tipping data requests. The low absolute supply makes TRB notoriously volatile and historically a target of squeeze/manipulation episodes. The MC/FDV near 0.97 reflects that nearly all supply is circulating. TRB is staked by **reporters** (collateral that can be slashed for bad data) and by **disputers** who challenge incorrect submissions.

---

## Technology — dispute-based oracle

Tellor is a **dispute-based oracle**, conceptually closer to [[uma|UMA's]] optimistic model than to the always-on push feeds of [[chainlink|Chainlink]]. The lifecycle of a data point:

- **Data request & report** — A dApp tips (in TRB) for a data point (e.g., ETH/USD); **staked reporters** submit values on-chain. Each reporter must lock TRB collateral to participate.
- **Dispute window** — Any party can stake TRB to dispute a value they believe is wrong; disputes are resolved by TRB-holder vote, with the loser's stake slashed.
- **Security via cost-to-corrupt** — Manipulating Tellor requires acquiring and risking TRB stake, and bad actors can be slashed. The model trades latency for **censorship resistance and permissionlessness** — there is no privileged node-operator set.

**Evolution from PoW.** Tellor originally ran a **proof-of-work-style** competition where miners raced to submit data (the source of the "Tributes" name). The **Tellor X / Tellor 360** upgrades (2022) replaced mining with the current **stake-and-dispute** model, removing energy-intensive mining and tightening the crypto-economic design. Tellor is deployed across [[ethereum|Ethereum]], Polygon, Arbitrum, Optimism, Gnosis and other EVM chains, and is frequently used as a **fallback / backup feed** for protocols that want redundancy against a single oracle's failure.

This positions Tellor as a more decentralized, slower oracle option versus the higher-frequency [[chainlink]], [[pyth-network]], and [[redstone-oracles]].

---

## Market Structure & Derivatives

**Spot venues.** TRB lists on Binance (TRB/USDT), Bitget, KuCoin, and Crypto.com. On-chain liquidity sits on [[uniswap]] V3 against WETH.

**Derivatives.** A **TRB-PERP** perpetual trades on [[hyperliquid]] and several CEX futures venues. Given TRB's tiny ~2.8M float and history of violent squeezes, the perp can see extreme funding swings and rapid liquidations; open interest and funding should be checked live before trading, as the low float makes the contract prone to dislocation from spot.

**Liquidity / float dynamics.** TRB's defining market feature is its **~2.8M-token float** combined with high relative turnover (~$9M/day, ~23% of cap). This makes the token exceptionally squeeze-prone: a relatively small amount of buying pressure against thin order books and crowded shorts can drive outsized moves, as in the December 2023 spike to $593. Traders should treat TRB as a high-beta, manipulation-prone instrument where price action often decouples from oracle-protocol fundamentals.

---

## Use Case, Narrative & Category

Tellor sits in the **oracle / DeFi-infrastructure** category. Its narrative emphasizes **maximal decentralization and censorship resistance**: anyone can report or dispute data without permission, and there is no privileged node operator set. This makes it attractive as a fallback or backup oracle and for protocols that prioritize trust-minimization over speed. The TRB token itself is also widely known among traders as a **high-volatility, low-float instrument** that has repeatedly seen dramatic price spikes and squeezes, somewhat independent of protocol fundamentals.

### Peer comparison — oracle protocols

| Protocol | Token | Model | Update latency | Specialism | Mkt cap rank |
|---|---|---|---|---|---|
| [[chainlink]] | LINK | Decentralized push feeds + CCIP | Fast (heartbeat) | Blue-chip standard | Top-20 |
| [[pyth-network]] | PYTH | Pull (first-party publishers) | Sub-second | High-frequency price feeds | Top-100 |
| [[redstone-oracles]] | RED | Modular pull (signed data) | On-demand | LST/LRT collateral | #476 |
| **Tellor** | **TRB** | **Stake + dispute (ex-PoW)** | **Slow (dispute window)** | **Censorship-resistant fallback** | **#543** |
| [[uma]] | UMA | Optimistic, dispute-based | Slow (challenge window) | Arbitrary assertions | #549 |

Tellor and UMA occupy the **slow, dispute-based, trust-minimized** corner of the oracle landscape, contrasting with the fast push/pull feeds of Chainlink, Pyth, and RedStone. Tellor's edge is being a credibly neutral, permissionless **backup**, not a primary high-frequency feed.

### Valuation framing (qualitative)

TRB trades at ~$38.5M with MC/FDV near 0.97 (almost fully circulating), so dilution is minimal — unlike high-FDV peers such as [[redstone-oracles|RED]]. The challenge is **value accrual**: Tellor's actual protocol revenue (tips for data requests) is small relative to the token's trading float, and much of TRB's price is driven by its low-float squeeze dynamics rather than fundamental oracle demand. A sober frame treats TRB as a **niche decentralization premium plus a high-volatility trading instrument**, where the protocol's "backup oracle" positioning is real but monetarily thin, and the token's price is unusually disconnected from usage.

---

## Notable History

- **2019** — Tellor launches as a proof-of-work-style oracle; TRB sets its all-time low of $0.0100 (2019-11-01). Backed by YZi Labs (formerly Binance Labs) among others.
- **2020-2021** — Adoption as a decentralized oracle and backup feed across DeFi; deployment to multiple chains (Polygon, Arbitrum, Optimism, Gnosis, etc.).
- **2022 ("Tellor X" / "Tellor 360")** — Migration from PoW mining to a **staking-and-dispute** model, removing energy-intensive mining and tightening the crypto-economic security design.
- **2023-12-31** — TRB spiked to its all-time high of **$593.09**, a move widely attributed to a low-float squeeze rather than fundamentals; the price subsequently collapsed.
- **2026** — Trades around $13.78 in the broad bear market, far below its ATH but resilient on the week.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — Tellor's security rests on the cost to acquire TRB stake and on disputers catching bad data within the window. A motivated actor could submit false values and try to ride out the dispute window, or accumulate stake to influence dispute votes. See [[oracle-manipulation]].
- **Latency risk** — The dispute-based model is slower than push feeds; protocols using Tellor for fast-moving prices (e.g., liquidations) must account for the delay and dispute period.
- **Low-float volatility / squeeze risk** — With only ~2.8M tokens, TRB is extremely volatile and has a documented history of squeezes (notably the 2023 spike to $593); the [[hyperliquid]] perp amplifies this with leverage.
- **Reporter-set concentration risk** — If too few reporters stake, data availability and decentralization suffer.
- **Macro risk** — In an extreme-fear, established-bear regime ([[crypto-fear-and-greed-index|Fear & Greed]] 23), thin low-cap oracle tokens are prone to liquidity drought despite Tellor's recent weekly strength.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[chainlink]]
- [[pyth-network]]
- [[redstone-oracles]]
- [[api3]]
- [[uma]]
- [[oracle-manipulation]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TRB |
| **Market Cap Rank** | #499 |
| **Market Cap** | $41.97M |
| **Current Price** | $15.00 |
| **Categories** | Decentralized Finance (DeFi), Oracle, Made in USA |
| **Website** | [http://www.tellor.io/](http://www.tellor.io/) |

---

## Overview

Smart contracts on Ethereum are fully self contained and any information or access to off-chain data is restricted.  Tellor solves this problem by creating a system where parties can request the value of an off-chain data point (e.g. ETH/USD) and miners compete to add this value to an on-chain data bank, accessible by all Ethereum smart contracts.  Inputs to a data series are secured by a network of staked miners. The main Tellor smart contract creates a time series of each requested data series and aims to become the standard source of high value data for decentralized applications. This oracle, “Tellor”,  utilizes similar incentive mechanisms to other cryptocurrency systems through the issuance of Tellor’s token, Tributes, that are used to request a particular data series from miners.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.80M TRB |
| **Total Supply** | 2.88M TRB |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $43.14M |
| **Market Cap / FDV Ratio** | 0.97 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $593.09 (2023-12-31) |
| **Current vs ATH** | -97.46% |
| **All-Time Low** | $0.0100 (2019-11-01) |
| **Current vs ATL** | +150182.99% |
| **24h Change** | +1.55% |
| **7d Change** | -4.98% |
| **30d Change** | +4.89% |
| **1y Change** | -64.18% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0` |
| Xdai | `0xaad66432d27737ecf6ed183160adc5ef36ab99f2` |
| Lisk | `0x665060707c3ea3c31b3eabad7f409072446e1d50` |
| Polygon Pos | `0xe3322702bedaaed36cddab233360b939775ae5f1` |
| Arbitrum One | `0xd58d345fd9c82262e087d2d0607624b410d88242` |
| Optimistic Ethereum | `0xaf8ca653fa2772d58f4368b0a71980e9e3ceb888` |
| Manta Pacific | `0x8d7090ddda057f48fdbbb2abcea22d1113ab566a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TRB/USDT | N/A |
| Bitget | TRB/USDT | N/A |
| KuCoin | TRB/USDT | N/A |
| Crypto.com Exchange | TRB/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X88DF592F8EB5D7BD38BFEF7DEB0FBC02CF3778A0/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://www.tellor.io/](http://www.tellor.io/) |
| **Twitter** | [@WeAreTellor](https://twitter.com/WeAreTellor) |
| **Discord** | [https://discord.gg/n7drGjh](https://discord.gg/n7drGjh) |
| **GitHub** | [https://github.com/tellor-io](https://github.com/tellor-io) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.80M |
| **Market Cap Rank** | #499 |
| **24h Range** | $14.75 — $15.31 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
