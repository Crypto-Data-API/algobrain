---
title: "Bancor Network"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, ethereum, liquidity]
aliases: ["BNT", "Bancor", "Carbon DeFi"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://www.bancor.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[automated-market-maker]]", "[[decentralized-exchange]]", "[[impermanent-loss]]", "[[uniswap]]", "[[liquidity-pool]]", "[[governance-token]]", "[[defi]]"]
---

# Bancor Network

**Bancor Network** ([[bnt|BNT]]) is one of the original [[decentralized-exchange|decentralized exchanges]] (DEX) and is widely credited as the first major on-chain [[automated-market-maker]] (AMM). Launched in 2017 after one of the largest [[ico|ICOs]] of that era (~$153M raised in June 2017), Bancor pioneered the use of bonded-curve [[liquidity-pool|liquidity pools]] and the connector-token model that later inspired [[uniswap]] and the broader [[defi]] AMM landscape. The protocol's central innovation through its history was **single-sided liquidity** with **impermanent-loss protection**, allowing liquidity providers to deposit a single asset rather than a paired 50/50 position.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, BNT trades at **$0.267812**, ranked **#661** by market capitalization with a market cap of **$28,888,240**. The token was slightly down over the prior day (**-0.89%** 24h) and down over the week (**-2.65%** 7d), consistent with the broader bear-market regime (BTC ~$64,508; Fear & Greed Index 21, "Extreme Fear"). BNT remains down more than 97% from its January 2018 all-time high near $10.72.

The Bancor ecosystem today centers on **Carbon DeFi**, a decentralized trading protocol allowing users to execute automated on-chain strategies using custom limit orders and range orders, with the option of combining orders to create automated "buy low, sell high" strategies. All protocols are governed by the **BancorDAO** via staked BNT (see [[governance-token]]).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BNT |
| **Market Cap Rank** | #661 |
| **Market Cap** | $28,888,240 |
| **Current Price** | $0.267812 |
| **24h Change** | -0.89% |
| **7d Change** | -2.65% |
| **Genesis Date** | 2017-06-12 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Automated Market Maker (AMM), Ethereum Ecosystem, DeFiance Capital Portfolio, Energi Ecosystem, Governance |
| **Website** | [https://www.bancor.network/](https://www.bancor.network/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Bancor is an ecosystem of decentralized, open-source protocols that promote on-chain trading and liquidity on [[ethereum]] and EVM-compatible chains. Bancor's 2017 whitepaper introduced the concept of "smart tokens" with built-in [[liquidity-pool|liquidity]] via a continuous bonding curve, removing the need for a counterparty or order book and establishing the AMM design pattern that now dominates [[defi]].

The current ecosystem is composed of several protocols:

- **Carbon DeFi** — the flagship protocol, a decentralized trading engine for automated on-chain strategies (custom limit and range orders).
- **Fast Lane** — a separate open-source arbitrage protocol that lets any user perform arbitrage between Bancor ecosystem protocols and external on-chain exchanges, redirecting arbitrage profits back to the ecosystem.
- **BancorDAO** — governs all ecosystem protocols via staked BNT.

### What makes Bancor unique

Carbon allows users to perform automated trading strategies on-chain with greater control than typical AMM-based DEXs. Existing on-chain liquidity solutions suffer from two key drawbacks: (1) executed orders can effectively be reversed when prices move back, and (2) a single liquidity position must execute both buys and sells using the same pricing curve, exposing providers to [[impermanent-loss]] and traders to [[maximal-extractable-value|MEV]] sandwich attacks.

Carbon introduces **Asymmetric Liquidity**, allowing users to create individual liquidity positions with two distinct pricing curves — one for buying and one for selling. This enables buy and sell orders that execute in specific price ranges, with the option to combine them into automated "buy low, sell high" strategies. By design, Carbon orders are irreversible on execution, adjustable directly on-chain, and resistant to MEV sandwich attacks.

---

## Mechanism & Architecture

Bancor's original design (Bancor v1/v2.1/v3) used **single-sided liquidity**: a provider could deposit just one token (e.g., [[ethereum|ETH]] or a partner project's token) into a whitelisted pool rather than the paired 50/50 deposit that [[uniswap]] and most AMMs require. The protocol co-invested its own BNT alongside user deposits, and BNT served as the universal "connector" routing trades between any two whitelisted pools.

Bancor v2.1/v3 also offered **impermanent-loss protection (ILP)**: the protocol promised to compensate liquidity providers for [[impermanent-loss]] after a vesting period, funding the guarantee with trading-fee revenue and BNT emissions. This was the protocol's signature differentiator — but it became a structural liability when fee revenue could not keep pace with the IL liabilities accruing during the 2022 market downturn (see History).

Carbon DeFi represents the architectural reset: rather than promising IL protection, it gives users explicit, range-bound, irreversible orders so that liquidity provision behaves more like algorithmic limit-order trading than passive AMM exposure.

---

## Token Role (BNT)

BNT is Bancor's native [[governance-token]] and historically its core utility token:

- **Governance** — staked BNT is used to vote in the BancorDAO on protocol parameters, whitelisting, and upgrades.
- **Connector / liquidity** — in earlier versions BNT acted as the intermediary asset co-invested into every pool, making it central to routing and to the IL-protection backstop.
- **Fees & incentives** — protocol fee revenue and historic BNT emissions funded liquidity-mining rewards and (in v2.1/v3) the IL-protection guarantee.

Supply is effectively fully circulating (~109M BNT, market-cap/FDV ≈ 1.0), so there is little remaining token-unlock dilution overhang relative to many peers.

---

## History & Notable Events

- **June 2017** — Bancor's ICO raised ~$153M in ETH in roughly three hours, one of the largest token sales to that date.
- **2017** — Bancor whitepaper popularizes the AMM / bonding-curve model later adopted across DeFi.
- **July 2018** — Bancor suffered a security incident in which roughly $13.5M in tokens (including ~$10M of BNT and ETH) were drained from a wallet used to upgrade smart contracts. Bancor was able to freeze the stolen BNT, drawing both relief and criticism over the centralization implied by a freeze function.
- **2020–2021** — Bancor v2.1 introduces single-sided staking and impermanent-loss protection.
- **June 2022** — Amid the [[crypto-winter|2022 market downturn]] and the [[terra-luna-collapse|Terra/3AC contagion]], Bancor **paused impermanent-loss protection** on Bancor v3, citing "hostile" market conditions and manipulative behavior. The pause damaged user trust and the protocol's TVL fell sharply; it marked the practical end of the IL-protection era.
- **2023 onward** — The ecosystem pivots to **Carbon DeFi** (asymmetric, range-order liquidity) and **Fast Lane** arbitrage as the path forward.

---

## Competitive Position

Bancor is historically significant as the AMM pioneer, but it has been decisively overtaken in volume and TVL by later AMMs — [[uniswap]], [[curve-finance|Curve]], [[balancer]], and [[pancakeswap]] — and by aggregators. Its single-sided-liquidity and IL-protection model was a genuine differentiator, but the 2022 IL-protection pause severely eroded its competitive standing and brand. The Carbon DeFi pivot repositions Bancor away from passive AMM liquidity toward programmable on-chain strategy execution, a niche where it competes with limit-order and intent-based protocols rather than head-on with the largest spot AMMs.

| Protocol | Core model | LP deposit | IL handling | Bancor's relationship |
|---|---|---|---|---|
| **Bancor (legacy v2.1/v3)** | Bonding-curve AMM | **Single-sided** (one token) | Promised **IL protection** (paused 2022) | The pioneer; now legacy |
| **Carbon DeFi** (current Bancor) | Asymmetric range/limit orders | Single-sided, range-bound | No passive IL — explicit, irreversible orders | The pivot product |
| [[uniswap\|Uniswap]] v2/v3 | Constant-product / concentrated liquidity | Paired (v2) or ranged (v3) | LP bears IL | The dominant successor it inspired |
| [[curve-finance\|Curve]] | StableSwap invariant | Paired/multi-asset | Low IL for like-assets | Leads stable-asset swaps |
| [[balancer\|Balancer]] | Weighted pools (e.g., 80/20) | Multi-asset, custom weights | LP bears IL | Generalized AMM rival |

The key conceptual shift: classic AMMs (including Bancor's own legacy design) force a single passive curve that *must* both buy and sell, guaranteeing [[impermanent-loss]] when price trends. Carbon instead lets a provider define **two separate, range-bounded curves** — effectively on-chain limit orders — so liquidity behaves like an active trading strategy rather than a passive pool, and the position is not forcibly reversed when price retraces.

### Worked illustration: a Carbon "buy low, sell high" strategy

A user holding ETH wants to sell ETH near $4,000 and re-buy near $3,000, automatically and on-chain. In Carbon they create a single strategy with two linked orders: a **sell order** with a price range around $3,900–$4,100 (denominated in the quote token) and a **buy order** ranged around $2,900–$3,100. As price rises into the sell range, the strategy sells ETH for stablecoins; as price falls into the buy range, it spends those stablecoins to re-accumulate ETH. Unlike a Uniswap v3 LP position, the executed leg is *not* automatically reversed if price whipsaws back through the same range, and the order is MEV-sandwich-resistant by construction. The trade-off is that the user must actively choose ranges and rebalance — this is algorithmic trading, not passive yield.

---

## Risks

- **Reputational / trust risk** — the 2022 suspension of impermanent-loss protection left many liquidity providers worse off than promised and remains the central knock against the protocol.
- **Competitive decline** — low relative volume and TVL versus dominant AMMs; network effects favor incumbents.
- **Smart-contract risk** — as with all [[defi]] protocols; Bancor has a prior exploit (2018) in its history.
- **Microcap liquidity risk** — at a ~$29M market cap and modest 24h volume, BNT is thinly traded and prone to slippage and volatility.
- **Token-utility risk** — as the ecosystem moves away from the BNT-as-connector model toward Carbon, the long-term value-accrual path for BNT depends on Carbon/Fast Lane adoption and DAO fee capture.

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 108.96M BNT |
| **Total Supply** | 108.96M BNT |
| **Max Supply** | 110.54M BNT |
| **Fully Diluted Valuation** | $31.78M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $10.72 (2018-01-09) |
| **Current vs ATH** | -97.28% |
| **All-Time Low** | $0.1209 (2020-03-13) |
| **Current vs ATL** | +141.21% |
| **24h Change** | -3.11% |
| **7d Change** | +0.26% |
| **30d Change** | +3.14% |
| **1y Change** | -12.43% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c` |
| Energi | `0x9419e8edcf570a71eb0dd006602949742b711a80` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BNT/USDT | N/A |
| Kraken | BNT/USD | N/A |
| Crypto.com Exchange | BNT/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BNT-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.bancor.network/](https://www.bancor.network/) |
| **Twitter** | [@Bancor](https://twitter.com/Bancor) |
| **Reddit** | [https://www.reddit.com/r/Bancor](https://www.reddit.com/r/Bancor) |
| **Telegram** | [bancor](https://t.me/bancor) (3,998 members) |
| **Discord** | [https://discord.com/invite/bancor](https://discord.com/invite/bancor) |
| **GitHub** | [https://github.com/bancorprotocol/contracts](https://github.com/bancorprotocol/contracts) |
| **Whitepaper** | [https://www.carbondefi.xyz/whitepaper](https://www.carbondefi.xyz/whitepaper) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 883 |
| **GitHub Forks** | 394 |
| **Pull Requests Merged** | 504 |
| **Contributors** | 16 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.267812 |
| **Market Cap** | $28,888,240 |
| **Market Cap Rank** | #661 |
| **24h Change** | -0.89% |
| **7d Change** | -2.65% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Related

- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[liquidity-pool]]
- [[impermanent-loss]]
- [[defi]]
- [[uniswap]]
- [[curve-finance]]
- [[governance-token]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge (publicly documented Bancor history: 2017 ICO, 2018 hack, 2022 IL-protection pause, and the Carbon DeFi pivot); no specific narrative wiki source ingested yet.
