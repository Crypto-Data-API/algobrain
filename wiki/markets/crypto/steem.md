---
title: "Steem"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["STEEM", "Steemit"]
entity_type: protocol
founded: 2016
headquarters: "Decentralized"
website: "https://steem.com/"
related: ["[[crypto-markets]]", "[[delegated-proof-of-stake]]", "[[hive]]", "[[justin-sun]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[tron]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[range-mean-reversion]]"]
---

# Steem

**Steem** (STEEM) is the original social/content-rewards **[[layer-1|layer-1 blockchain]]**, launched in 2016, that pays users in cryptocurrency for posting and curating content. It runs **[[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]]** consensus and was the foundation for **Steemit**, an early blockchain-based social network. Steem is historically significant as the chain that, after being acquired by [[justin-sun]] / [[tron]] in 2020, split: the community migrated to a new fork, **[[hive]]**, while Steem continued under Tron-aligned governance. It ranks **#750** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* STEEM trades at **$0.04247555**, with a market cap of **$23,384,722** (rank **#750**), down **-1.88%** over 24h and down **-5.34%** over the past 7 days. Conditions are risk-off (Fear & Greed 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | STEEM |
| **Market Cap Rank** | #750 |
| **Market Cap** | $23,384,722 |
| **Current Price** | $0.04247555 |
| **24h Change** | -1.88% |
| **7d Change** | -5.34% |
| **Genesis Date** | 2016-03-24 |
| **Consensus** | [[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]] |
| **Categories** | SocialFi, [[layer-1|Layer 1 (L1)]] |
| **Website** | [https://steem.com/](https://steem.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Steem is a cryptocurrency that rewards users for community building by posting and upvoting valuable content for others. Steem was inspired from the success of Reddit where the community helped enrich the shareholders. Steem aims to help distribute the rewards to the community members who help create the community in the first place. Steem aims to provide various services to its members such as a source of curated news, Q&amp;A, job boards etc. The founders of Steem came from BitShares with Dan Larimer involved as well.

Steem’s main platform, called Steemit, is a social media network built on top of the Steem blockchain. Steemit is similar to popular content-driven social networks like Reddit and Medium, but it rewards users with cryptocurrency for their participation. Fundamentally, the more value a particular piece of content provides to a greater number of people, the more the individuals responsible for creating and curating that content can earn.

Users cast votes, creating a hierarchy of content. The more upvotes a post gets, the more it will earn. The platform also allows for downvotes, giving participants more flexibility when it comes to rating content. Steemit is meritocratic, meaning users that hold more currency can cast votes with greater influence.

The Steemit community even has another service to offer to its customers. D.tube, which is considered to be very similar to YouTube, is Blockchain based and the users can realize the difference between the traditional video publishing websites and D.tube, as the amount of money earned is also displayed beside the post apart from likes shares and comments. The Steemit community is accused of posting plagiarize contents on their publishing website. The irony seems to be reaching highest levels when the original content doesn’t receive much appreciation and income than the copied versions of it."

### Architecture and tokens

Steem runs **[[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]]** (see [[delegated-proof-of-stake]]), in which token holders vote for "witnesses" that produce blocks. Transactions are **feeless**, with bandwidth allocated according to staked tokens. The Steem economy historically used a three-token model that Hive later mirrored:

- **STEEM** — the liquid base token.
- **Steem Power (SP)** — staked STEEM granting governance/voting weight and curation influence; powering down is gradual.
- **Steem Dollars (SBD)** — an algorithmic stable-value token loosely pegged to USD.

Co-founders **Ned Scott** and **Dan Larimer** built Steem; Larimer (also behind BitShares and later EOS) pioneered the DPoS model used here. The on-chain "ninja-mined" stake — tokens mined by the founders in the chain's earliest blocks — later became the flashpoint of the 2020 governance dispute.

### Consensus mechanics in detail

Steem uses a **21-block production schedule**: the top 20 witnesses by stake-weighted vote produce blocks, plus one rotating slot drawn from the remaining ("backup") witnesses, with new blocks roughly every **3 seconds**. Because consensus is a small elected set rather than open [[proof-of-work|mining]], throughput is high and confirmation is fast — but security ultimately rests on the distribution of [[proof-of-stake|staked]] Steem Power across honest witnesses, which is exactly the assumption the 2020 takeover violated.

Spam control uses a **bandwidth/Resource-Credit** allowance proportional to staked SP rather than per-transaction fees, so heavy users must "power up" more STEEM to keep transacting — a model Hive inherited verbatim at the fork.

### Smart contracts and second layers

Like [[hive]], the Steem base layer is **not** a general-purpose [[smart-contracts|smart-contract]] VM; it exposes a fixed set of social/economic operations (post, vote, transfer, escrow, witness vote) plus a custom-JSON mechanism that second-layer systems interpret. Token and DeFi functionality historically lived on the community **Steem Engine** sidechain. After 2020, most of the active second-layer development momentum migrated to Hive's equivalents.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 544.17M STEEM |
| **Total Supply** | 544.21M STEEM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $31.50M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.19 (2018-01-03) |
| **Current vs ATH** | -99.29% |
| **All-Time Low** | $0.0450 (2026-02-06) |
| **Current vs ATL** | +28.69% |
| **24h Change** | +1.32% |
| **7d Change** | -2.66% |
| **1y Change** | -47.12% |

STEEM trades roughly **-99%** below its January 2018 all-time high of ~$8.19, one of the deeper drawdowns among surviving social tokens.

---

## History — The Tron Takeover and the Hive Fork (2020)

The pivotal episode in Steem's history is the 2020 governance conflict, presented here honestly because it is the same event covered from the other side on the [[hive]] page:

- In **February 2020**, [[justin-sun]]'s [[tron]] Foundation acquired **Steemit Inc.**, gaining control of the dominant Steemit front-end and the large founder ("ninja-mined") stake of STEEM.
- The Steem community had treated that stake as not to be used in governance. Fearing Sun would vote it to control the witnesses, witnesses enacted a soft fork to freeze it.
- In response, Sun — reportedly with cooperation from major exchanges including **Binance, Huobi, and Poloniex** — **used exchange customers' staked STEEM** to vote out the existing witnesses and install a new set aligned with him. Using customer deposits for governance voting drew heavy criticism across the industry; the exchanges later unwound much of their involvement under public pressure.
- On **20 March 2020**, much of the community **hard-forked away to create [[hive]]**, copying balances and content but excluding the disputed Steemit stake, and airdropping HIVE to existing holders (other than that contested stake).

After the fork, **Steem continued under Tron-aligned governance** while the community-governance lineage moved to Hive. The two chains remain mirror images of the same dispute, and much of the original developer community and flagship apps migrated to Hive.

The episode is now a canonical case study in two areas: (1) **DPoS governance-attack risk**, showing that a large, concentrated stake combined with cooperating custodians can override a witness set in a single voting round; and (2) **exchange custody ethics**, because using customer-deposited STEEM to vote drew industry-wide criticism and prompted the exchanges to reverse course under public pressure. See the [[hive]] page for the community-fork side of the same events.

---

## Governance

- **Witness governance:** Stake-weighted (Steem Power) votes elect the 20+1 witness schedule; a hard fork ships when a supermajority of top witnesses upgrade. After 2020 this set has been associated with [[justin-sun]]/[[tron]]-aligned actors.
- **Stake concentration legacy:** Steem's pre-2020 history carried a large founder ("ninja-mined") stake. The acquisition of that stake by Tron is precisely what enabled the contested governance shift — a structural contrast to [[hive]], which launched without that overhang.
- **Treasury / rewards:** Issuance funds a content-reward pool (authors + curators) and witness pay; there is no hard supply cap.

---

## Steem vs. Peer Social / DPoS Chains

| Dimension | Steem (STEEM) | [[hive]] (HIVE) | [[tron]] (TRX) | BitShares (BTS) |
|---|---|---|---|---|
| **Primary use** | SocialFi, blogging | SocialFi, gaming | DeFi/stablecoins | DEX / synthetic assets |
| **Consensus** | [[delegated-proof-of-stake|DPoS]] (21 witnesses) | [[delegated-proof-of-stake|DPoS]] (21 witnesses) | DPoS (27 SRs) | [[delegated-proof-of-stake|DPoS]] |
| **User fees** | Feeless (bandwidth) | Feeless (Resource Credits) | Low gas | Low fees |
| **Stable token** | SBD (algorithmic) | HBD (algorithmic) | USDD / USDT | bitAssets (collateralized) |
| **Governance** | SP-weighted witnesses (Tron-aligned post-2020) | HP-weighted witnesses + DHF DAO | Sun/Tron-aligned SRs | BTS-weighted committee |
| **Founder/Larimer link** | Co-founded by Dan Larimer | Forked from Steem | — | Founded by Dan Larimer |
| **Origin** | 2016 original chain | 2020 community fork | 2017 ICO | 2014 |

Steem and Hive are technically near-identical, having shared a codebase until the 2020 split. The defining divergence is **governance legitimacy and stake distribution**, not the technology stack. Several DPoS chains in this comparison trace back to **Dan Larimer**, who pioneered the model at BitShares before co-founding Steem and later EOS.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | STEEM/USDT | N/A |
| Upbit | STEEM/BTC | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://steem.com/](https://steem.com/) |
| **Twitter** | [@SteemNetwork](https://twitter.com/SteemNetwork) |
| **Reddit** | [https://www.reddit.com/r/steem/](https://www.reddit.com/r/steem/) |
| **GitHub** | [https://github.com/steemit/steem](https://github.com/steemit/steem) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,957 |
| **GitHub Forks** | 795 |
| **Pull Requests Merged** | 1,251 |
| **Contributors** | 68 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.04247555 |
| **Market Cap (2026-06-22)** | $23,384,722 |
| **Market Cap Rank** | #750 |
| **24h Change** | -1.88% |
| **7d Change** | -5.34% |
| **Last Updated** | 2026-06-22 |

---

## Risks

- **Post-fork community drain:** Much of the active developer base and flagship apps migrated to [[hive]] after 2020, leaving Steem with a smaller, more fragmented ecosystem.
- **Governance / centralization concerns:** The Tron-takeover episode demonstrated how concentrated stake and exchange cooperation can override DPoS witness governance.
- **Inflationary supply:** STEEM has no hard cap; ongoing issuance funds rewards and can dilute holders.
- **SBD peg risk:** The Steem Dollars stable-value token is algorithmic and can de-peg under stress; defending the peg can mint and dilute STEEM.
- **Single-sponsor alignment:** Post-2020 governance is associated with [[justin-sun]]/[[tron]], reducing the credibly-neutral, community-owned narrative that the [[hive]] fork claimed.
- **Liquidity / small-cap risk:** ~$23M market cap with thin order books; weekly move of -5.34% (2026-06-22) is steeper than the broader cohort.
- **Cycle risk:** Down ~99% from ATH in an Extreme Fear market (Fear & Greed 21 on 2026-06-22); small-caps underperform in risk-off regimes.

> Not investment advice. Figures are point-in-time; verify on-chain and project claims independently.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

STEEM is tradable on **[[binance]]** as both **spot** (STEEM/USDT) and a **USD-margined [[perpetual-futures|perpetual]]**, which exposes a full [[funding-rate|funding-rate]], [[open-interest|open-interest]], and [[liquidations|liquidation]] surface for a coin this small. It is **NOT** listed on Hyperliquid, so Binance is effectively the **primary leveraged venue** and the reference price for the perp. With only a ~$23M market cap and thin order books (see Trading Characteristics), leverage should be treated cautiously: sizeable perp positions can move the underlying spot, and stops or liquidations can gap. Venue concentration means execution and hedging both route through a single dominant exchange, so cross-venue arbitrage or basis capture is constrained to Binance spot-vs-perp rather than a broad multi-venue book. Size positions to available depth and expect meaningful slippage on market orders.

### Applicable strategies

- [[funding-rate-harvest]] — a small, sentiment-driven perp can run persistent one-sided funding, letting a delta-neutral book harvest the carry between STEEM spot and the Binance perp.
- [[cash-and-carry]] — hold spot STEEM against a short perp to bank basis/funding when the perp trades at a premium, a clean structure given both legs live on Binance.
- [[crowded-long-funding-fade]] — thin retail-driven rallies in a down-99%-from-ATH social token frequently over-extend perp longs; fade the crowd when funding spikes positive.
- [[liquidation-cascade-fade]] — low liquidity makes STEEM prone to sharp liquidation wicks; fading forced-selling flushes on the Binance perp can capture the mean-reverting snapback.
- [[range-mean-reversion]] — a beaten-down micro-cap grinding near ATL often chops in a range, favoring reversion around support/resistance rather than trend entries.
- [[breakout-trading]] — narrative or [[justin-sun|Sun]]/[[tron|Tron]]-driven catalysts can trigger violent expansions from the range, where a confirmed breakout captures the impulsive move.

### Volatility & regime character

STEEM is a **micro-cap SocialFi/[[layer-1|L1]]** token with high idiosyncratic volatility and strong reflexivity typical of low-float, retail-driven coins. It carries **high beta to BTC/ETH** in risk-off regimes (small-caps bleed hardest, as the -5.34% weekly move on 2026-06-22 shows) while also reacting to Steem/Hive/Tron-specific narrative and [[justin-sun]] headlines. Liquidity is shallow, so realized volatility clusters around catalysts and liquidation events rather than being evenly distributed.

### Risk flags

- **Liquidity / venue concentration:** ~$23M cap with thin books; Binance is the dominant venue, so a listing/delisting or depth shift there materially changes tradability.
- **Inflationary emissions:** no hard supply cap; ongoing issuance to reward pools and witnesses can dilute holders and pressure price.
- **Narrative dependence:** price is sensitive to [[justin-sun]]/[[tron]] governance news and the ongoing Steem-vs-[[hive]] narrative; headline-driven gaps are common.
- **Governance/centralization overhang:** the 2020 Tron takeover episode is a standing reminder that concentrated stake plus exchange cooperation can move this chain — a latent event risk for holders.
- **Leverage fragility:** low depth means perp liquidations and stops can cascade and gap; conservative sizing and wide-but-defined risk are warranted.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=STEEMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=STEEMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=STEEM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=STEEM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=STEEMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=STEEMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=STEEM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[hive]] — the community fork that split from Steem in 2020
- [[justin-sun]]
- [[tron]]
- [[delegated-proof-of-stake]]
- [[layer-1]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific dedicated Steem source has been ingested into the wiki yet.
