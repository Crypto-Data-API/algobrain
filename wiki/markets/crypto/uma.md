---
title: "UMA"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle]
aliases: ["UMA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://uma.xyz/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-disputes]]", "[[pyth-network]]"]
---

# UMA

**UMA** (ticker **UMA**) is the governance and dispute-resolution token of the UMA protocol, an [[ethereum|Ethereum]]-based oracle platform best known for its **Optimistic Oracle** — a mechanism that brings arbitrary off-chain data on-chain by assuming proposed values are correct unless economically challenged. UMA powers "priceless" financial contracts and is the data backbone of [[polymarket]] and other dispute-driven DeFi applications.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | UMA |
| **Current Price** | $0.417532 |
| **Market Cap** | $37.85M |
| **Market Cap Rank** | #549 |
| **24h Volume** | $5.06M |
| **24h Change** | +2.40% |
| **7d Change** | +3.41% |
| **Fully Diluted Valuation** | $53.82M |
| **All-Time High** | $41.56 (2021-02-04) |
| **All-Time Low** | $0.3036 (2020-04-29) |
| **Chain** | [[ethereum\|Ethereum]] (also Avalanche, Polygon, Optimism) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

UMA is trading modestly green on the day (+2.4%) and week (+3.4%), an outlier of relative strength against a backdrop where the broad **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] sits at 23 (extreme fear)** and analysts describe an **established bear market**. At ~$0.42 the token remains roughly -99% below its February 2021 all-time high of $41.56, but well above its 2020 cycle low of $0.30. Daily turnover of ~$5M against a $37.85M cap is a velocity of ~13% — typical for a low-cap infra token but thin enough that fills of size move the tape.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~90.67M UMA |
| **Total Supply** | ~128.93M UMA |
| **Max Supply** | Uncapped (governance-mintable) |
| **Fully Diluted Valuation** | $53.82M |
| **Market Cap / FDV** | ~0.70 |
| **All-Time High** | $41.56 (2021-02-04) |
| **All-Time Low** | $0.3036 (2020-04-29) |

UMA's supply is uncapped: the [[oracle-disputes|Data Verification Mechanism]] (DVM) can mint new tokens to fund the "51% attack is always more expensive than the corruptible value" security guarantee. In practice issuance is slow and governed by token-holder vote. The MC/FDV ratio near 0.70 reflects modest locked or treasury-held supply rather than aggressive future emissions.

The UMA token does two jobs:

- **Governance** — holders vote on supported contract types, asset whitelists, system parameters, and upgrades.
- **Dispute resolution** — when an Optimistic Oracle assertion is challenged, token holders are the final arbiters via the DVM, staking and voting on the correct value and earning rewards for honest participation.

---

## Technology — the Optimistic Oracle

UMA is not a price-feed oracle in the [[chainlink|Chainlink]] push model. Its core primitive is the **Optimistic Oracle (OO)**, which answers arbitrary questions — "did event X happen?", "what was the TWAP of asset Y?" — under an optimistic, game-theoretic assumption:

1. **Assertion** — a proposer posts an answer on-chain together with a **bond**.
2. **Challenge window** — a liveness period (often 2 hours to several days) during which anyone can dispute by posting a matching bond.
3. **Happy path** — if no dispute arrives, the assertion finalizes cheaply and the proposer recovers the bond. No on-chain computation of the "true" value is needed.
4. **Escalation** — a dispute escalates to the **Data Verification Mechanism (DVM)**, where UMA token holders stake and vote on the correct value over ~48-96 hours. The losing side forfeits its bond; honest voters earn rewards.

The economic security claim is that **the cost to corrupt always exceeds the value at stake**: the DVM can mint new UMA to keep the corruption cost above any single dispute's profit (see [[oracle-disputes]]). The trade-off versus push oracles is latency — the OO is built for **truth-on-demand**, not millisecond price streaming. This makes UMA ideal for subjective or hard-to-feed data: prediction-market resolution (it secures [[polymarket]]), insurance payouts, [[cross-chain]] [[bridge|bridges]], KPI options, and "priceless" synthetic tokens that track a reference index without a continuous on-chain feed.

Adjacent products built on the OO include **oSnap** (an optimistic governance executor that lets DAOs execute Snapshot votes on-chain without a multisig), **KPI options**, and **success tokens**.

---

## Market Structure & Derivatives

**Spot venues.** UMA lists on major centralized exchanges including Binance (UMA/USDT), Kraken (UMA/USD), Bitget, KuCoin, and Crypto.com. On-chain liquidity sits on [[uniswap]] V2/V3 and SushiSwap against WETH across Ethereum, Polygon, and Optimism.

**Derivatives.** A **UMA-PERP** perpetual trades on [[hyperliquid]], giving leveraged/short access to a token with a relatively thin ~$5.1M daily spot tape. Open interest and funding on a name this size are small and can swing sharply, so perp pricing can dislocate from spot during volatility. Treat UMA as a primarily spot-driven instrument; verify perp depth and funding live before sizing.

**Liquidity profile.** With ~$5M daily volume on a $37.85M cap, UMA is a low-cap, moderate-velocity infra token. Bid/ask depth thins quickly beyond a few tens of thousands of dollars on most venues.

---

## Use Case, Narrative & Category

UMA sits in the **oracle / DeFi-infrastructure** category alongside [[chainlink]], [[pyth-network]], [[api3]], [[redstone-oracles]], and [[tellor]]. Its differentiator is the optimistic, dispute-based design: instead of streaming prices, it provides truth-on-demand for arbitrary assertions at very low gas when unconfirmed. The dominant current narrative is its role as the **canonical resolution layer for prediction markets** — most visibly Polymarket — which ties UMA's relevance to the growth of event-driven and political/sports betting markets on-chain. Related products include KPI options, success tokens, and the oSnap optimistic governance executor used by DAOs.

### Peer comparison — oracle protocols

| Protocol | Token | Model | Specialism | Mkt cap rank |
|---|---|---|---|---|
| [[chainlink]] | LINK | Decentralized push feeds + CCIP | General-purpose, blue-chip standard | Top-20 |
| [[pyth-network]] | PYTH | Low-latency pull (first-party publishers) | High-frequency price feeds | Top-100 |
| **UMA** | **UMA** | **Optimistic, dispute-based** | **Arbitrary assertions / prediction-market resolution** | **#549** |
| [[tellor]] | TRB | Staking + dispute (ex-PoW) | Censorship-resistant fallback feeds | #543 |
| [[redstone-oracles]] | RED | Modular pull (signed off-chain data) | Yield-bearing / LST-LRT collateral | #476 |
| [[api3]] | API3 | First-party (dAPIs), OEV capture | First-party data + OEV | — |

UMA is the outlier: it is the only major oracle whose flagship product resolves **subjective, non-price assertions** rather than streaming numerical feeds — a different market than the price-feed competition.

### Valuation framing (qualitative)

UMA trades at a ~$38M market cap and a low MC/FDV (~0.70) with no aggressive emission schedule, so dilution is not the headline risk. The bull case is optionality on **prediction-market growth**: UMA is the de-facto resolution layer for [[polymarket]], and event-driven on-chain betting has structural tailwinds around elections and sports. The bear case is that the OO's relevance is **concentrated** in a single vertical, value accrual to the token is indirect (security/governance rather than fee capture), and the broad oracle market is dominated by [[chainlink]]. At -99% from ATH the token reflects deep skepticism; a re-rating likely requires demonstrable fee/usage growth or a major new OO integration, not just market beta.

---

## Notable History

- **2018-2020** — Founded by Hart Lambur and Allison Lu; backed by Blockchain Capital, Bain Capital Ventures, Placeholder, and others. Mainnet and the DVM launched in 2020.
- **2021** — UMA hit its ATH of $41.56 amid the DeFi "summer" expansion of synthetic-asset interest.
- **2021 onward** — Pivot from priceless synthetics toward the **Optimistic Oracle** as the flagship product, broadening UMA into a general-purpose data layer.
- **2022-2024** — UMA became the standard dispute-resolution oracle for [[polymarket]]; OO usage grew with the prediction-market boom around major elections.
- **Dispute incidents** — High-profile Polymarket resolution disputes (e.g., ambiguously worded markets) have periodically stress-tested the DVM and drawn debate over whether token-holder voting can be subverted on contentious questions.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — The optimistic model is only as safe as its economic bonds and the honesty of the DVM voter majority. A sufficiently large, motivated coalition could in theory vote a false outcome on a high-value market; ambiguous market wording amplifies this. See [[oracle-manipulation]] and [[oracle-disputes]].
- **Governance-capture risk** — Because resolution is token-vote-based, concentrated UMA holdings could sway outcomes; the security model assumes the cost to corrupt always exceeds the value at stake, which can fail for very large single disputes.
- **Concentration / dependency risk** — A large share of UMA's relevance is tied to [[polymarket]] and prediction-market volume; a downturn in that vertical would weigh on demand.
- **Liquidity risk** — ~$5.6M daily volume is thin; the [[hyperliquid]] perp can see outsized funding/price swings.
- **Macro / regime risk** — In an extreme-fear, established-bear backdrop ([[crypto-fear-and-greed-index|Fear & Greed]] 23), low-cap infrastructure tokens tend to underperform and suffer liquidity drought.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[chainlink]]
- [[pyth-network]]
- [[api3]]
- [[tellor]]
- [[oracle-disputes]]
- [[oracle-manipulation]]
- [[polymarket]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | UMA |
| **Market Cap Rank** | #584 |
| **Market Cap** | $33.83M |
| **Current Price** | $0.3689 |
| **Categories** | Decentralized Finance (DeFi), Oracle, Derivatives, Synthetic Issuer, Synthetic, Made in USA, Governance |
| **Website** | [https://uma.xyz/](https://uma.xyz/) |

---

## Overview

UMA is a decentralized financial contracts platform built to enable Universal Market Access.

UMA builds infrastructure for “priceless” financial contracts: DeFi contracts that minimize oracle usage, avoiding many of the security and scalability issues that have plagued decentralized finance. The first contracts built with UMA are priceless synthetic tokens: ERC20 tokens that can track anything while minimizing the need for on-chain price data.

The UMA project token powers the system in two ways:

Governance: UMA token holders govern what types of contracts can access the system, which asset types are supported, and key system parameters and upgrades.

Price requests: the priceless methodology minimizes on-chain price requests but doesn’t eliminate them — when contract interactions are disputed, UMA token holders fulfill price requests via the Data Verification Mechanism, or DVM.

UMA tokens enable the holder to participate in community governance and resolve contract disputes through the DVM. The tokens are not an investment opportunity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 91.70M UMA |
| **Total Supply** | 129.14M UMA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $47.64M |
| **Market Cap / FDV Ratio** | 0.71 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $41.56 (2021-02-04) |
| **Current vs ATH** | -99.11% |
| **All-Time Low** | $0.3036 (2020-04-29) |
| **Current vs ATL** | +21.45% |
| **24h Change** | +0.07% |
| **7d Change** | -0.82% |
| **30d Change** | -14.96% |
| **1y Change** | -69.76% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x04fa0d235c4abf4bcf4787af4cf447de572ef828` |
| Avalanche | `0x3bd2b1c7ed8d396dbb98ded3aebb41350a5b2339` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | UMA/USDT | N/A |
| Kraken | UMA/USD | N/A |
| KuCoin | UMA/USDT | N/A |
| Crypto.com Exchange | UMA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X04FA0D235C4ABF4BCF4787AF4CF447DE572EF828/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X04FA0D235C4ABF4BCF4787AF4CF447DE572EF828/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://uma.xyz/](https://uma.xyz/) |
| **Twitter** | [@UMAprotocol](https://twitter.com/UMAprotocol) |
| **Discord** | [https://discord.com/invite/jsb9XQJ](https://discord.com/invite/jsb9XQJ) |
| **GitHub** | [https://github.com/UMAprotocol/protocol](https://github.com/UMAprotocol/protocol) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 478 |
| **GitHub Forks** | 213 |
| **Pull Requests Merged** | 3,649 |
| **Contributors** | 53 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.49M |
| **Market Cap Rank** | #584 |
| **24h Range** | $0.3666 — $0.3734 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
