---
title: "1INCH"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["1INCH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://1inch.com/"
related: ["[[ai-solvers]]", "[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[defi]]", "[[dex-aggregator]]", "[[ethereum]]", "[[intent-based-trading]]", "[[mev-strategies]]", "[[solana]]", "[[uniswap]]"]
---

# 1INCH

**1INCH** (ticker 1INCH) is the governance token of the **1inch Network**, a leading [[dex-aggregator|DEX aggregator]] and [[defi|DeFi]] protocol that routes trades across many [[decentralized-exchange|decentralized exchanges]] and liquidity sources to find users the best execution price. Originally built on [[ethereum|Ethereum]], 1inch now spans 13+ EVM networks plus native [[solana|Solana]]↔EVM swaps, and its product suite includes the 1inch dApp, self-custodial wallet, and the Fusion intent-based / RFQ trading mode. The token is used for governance and protocol incentives.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | 1INCH |
| **Market Cap Rank** | #264 |
| **Market Cap** | $102.78M |
| **Current Price** | $0.073123 |
| **24h Volume** | $16.03M |
| **24h Change** | +0.36% |
| **7d Change** | +0.80% |
| **Circulating Supply** | ~1.41B 1INCH |
| **Total / Max Supply** | 1.50B 1INCH |
| **Fully Diluted Valuation** | ~$109.69M |
| **All-Time High** | $8.65 (Oct 2021) — now ~-99.2% |
| **All-Time Low** | $0.064981 — now ~+12.5% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

1INCH is essentially flat on both the day and the week, holding up notably better than many alts despite the crypto [[fear-and-greed-index|Fear & Greed Index]] sitting at **23 (extreme fear)** within an **Established Bear Market** as of 2026-06-21. Trading just ~12% above its all-time low of $0.065, the token sits near multi-year support. The 24h turnover (~$16M, ~16% of cap) is healthier than its low-rank float would suggest, reflecting steady CEX and DEX two-way flow in a mature DeFi governance token.

---

## Technology & Protocol

1inch is fundamentally a **routing and execution layer** over the fragmented DeFi liquidity landscape:

- **Pathfinder routing** — the core algorithm splits a single order across multiple pools and venues (Uniswap, Curve, Balancer, PancakeSwap, etc.) to minimize total slippage and gas-adjusted cost. Rather than swapping on one [[automated-market-maker|AMM]], a trade can be fractured across dozens of paths.
- **Fusion mode** — pushes execution toward [[intent-based-trading|intent-based trading]]. The user signs an *intent* (desired outcome) rather than a specific path; third-party "resolvers" ([[ai-solvers|solvers]]) compete in a Dutch-auction style to fill it, internalizing [[mev-strategies|MEV]] for the user's benefit and offering gasless swaps.
- **Limit Order Protocol** — a flexible on-chain order primitive used by Fusion, RFQ market makers, and external integrators.
- **Multi-chain footprint** — deployed across 13+ EVM networks (Ethereum, BNB Chain, Polygon, Arbitrum, Optimism, Base, Avalanche and more) plus native Solana↔EVM swaps via Fusion+.
- **1inch Wallet & Card** — a self-custodial mobile wallet and a crypto debit card extend the brand toward consumer DeFi.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.41B 1INCH |
| **Total Supply** | 1.50B 1INCH |
| **Max Supply** | 1.50B 1INCH |
| **Market Cap / FDV** | ~0.94 |

Max supply is **1.5 billion 1INCH**, with the large majority already circulating (MC/FDV ~0.94), so **future dilution is limited** compared to newer low-float tokens — the price already reflects nearly its fully-diluted value. The token launched via a December 2020 retroactive airdrop to past users. Holders can stake into the 1inch DAO to participate in governance and, historically, to earn rewards / fee-related benefits tied to the network's resolver and gas-refund systems.

---

## Market Structure & Derivatives

**Centralized spot venues:** Binance (1INCH/USDT), Kraken (1INCH/EUR), Upbit (1INCH/KRW), Bitget, KuCoin, and Crypto.com Exchange.

**On-chain spot:** Naturally deep on the very DEXs 1inch aggregates — [[uniswap|Uniswap]] V3/V2 on Ethereum (1INCH/WETH, 1INCH/LINK) are core markets, with liquidity also on BNB Chain and Base.

**Derivatives:** 1INCH has CEX perpetual markets; perp activity is modest given the token's mature, lower-volatility profile. There is no large, persistently active perp venue comparable to higher-beta names, and open interest / [[funding-rate|funding]] stay subdued outside of broad DeFi-sector moves.

---

## Use Case / Narrative / Category

1inch sits in the **DEX aggregator / DeFi infrastructure** category. The core product solves trade-execution fragmentation: rather than swapping on a single AMM, 1inch's Pathfinder routing algorithm splits an order across pools to minimize slippage and cost. The **Fusion** mode pushes this toward [[intent-based-trading|intent-based trading]], where third-party resolvers ([[ai-solvers|solvers]]) compete to fill user intents, internalizing [[mev-strategies|MEV]] for the user's benefit. The token narrative is governance over, and value-capture from, a high-volume routing layer of DeFi — adjacent to but distinct from the [[perp-dex-aggregation|perp-DEX aggregation]] thesis emerging around derivatives routing.

---

## Valuation Framing (qualitative)

At a ~$103M market cap and MC/FDV ~0.94, 1INCH is valued essentially on its fully-diluted basis, removing the unlock overhang that plagues newer peers. The harder question is **value accrual**: like most DeFi governance tokens, 1INCH does not automatically capture protocol fees, so its valuation is a bet on the DAO eventually directing routing economics to the token. Against multi-billion-dollar lifetime routing volume, a ~$100M cap can look cheap on a price-to-volume basis but expensive on realized cash flow to holders (near zero). The ~99% drawdown from ATH reflects a sector-wide de-rating of governance tokens rather than 1inch-specific failure.

---

## Peer Comparison

| Token | Category | MC Rank | Market Cap | MC/FDV | Notable |
|---|---|---|---|---|---|
| **1INCH** | DEX aggregator | #264 | ~$103M | ~0.94 | Multi-chain routing + Fusion intents |
| [[uniswap\|UNI]] | AMM DEX | top-50 | multi-$B | high | Largest spot DEX; UNI = fee-switch debate |
| [[jupiter-exchange\|Jupiter (JUP)]] | DEX aggregator | mid-cap | $100Ms+ | low–mid | Dominant Solana aggregator |
| [[dydx-chain\|dYdX (DYDX)]] | Perp DEX | #268 | ~$101M | ~0.84 | Order-book perps appchain |

1INCH competes for routing flow against CowSwap, ParaSwap, 0x/Matcha, and Jupiter on Solana; UNI is a liquidity venue 1inch aggregates rather than a direct router rival.

---

## Notable History

- 1inch launched in 2019; the 1INCH token debuted via a **December 2020 airdrop** to past users.
- It reached an all-time high near **$8.65 in October 2021** during the DeFi/altcoin bull market.
- Subsequent product launches included 1inch Fusion (intent-based swaps), the 1inch Wallet, and the 1inch Card. The token has drawn down more than 99% from its ATH as DeFi governance tokens broadly de-rated.

---

## Risks

- **Value-accrual question** — like many DeFi governance tokens, 1INCH does not automatically capture protocol fees; value accrual depends on DAO decisions.
- **Aggregator competition** — rivals such as CowSwap, ParaSwap, 0x/Matcha, and [[jupiter-exchange|Jupiter]] (Solana) compete for routing flow.
- **Fee compression / commoditization** — aggregation is increasingly commoditized, pressuring economics.
- **Regulatory exposure** — DeFi front-ends and DAOs face evolving regulatory scrutiny.
- **Bear-market beta** — small-cap DeFi token trading near its all-time low in an extreme-fear regime.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[dex-aggregator]]
- [[decentralized-exchange]]
- [[defi]]
- [[automated-market-maker]]
- [[uniswap]]
- [[intent-based-trading]]
- [[ai-solvers]]
- [[mev-strategies]]
- [[perp-dex-aggregation]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | 1INCH |
| **Market Cap Rank** | #254 |
| **Market Cap** | $104.58M |
| **Current Price** | $0.0744 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Automated Market Maker (AMM), FTX Holdings, Dex Aggregator, Governance, Base Native |
| **Website** | [https://1inch.com/](https://1inch.com/) |

---

## Overview

1inch is the DeFi ecosystem building financial freedom for everyone.

We research and develop cutting edge technology that allows our users and partners to realise the potential of decentralized finance, without workarounds or security risks.

And we bring the sector together to advocate for compliant DeFi as the future of global finance.

Our products:

We serve users and builders with products built on open-source, on-chain protocols.  

Access efficient, secure trading at the best rates through the 1inch dApp and self-custodial 1inch Wallet app, track your crypto with 1inch Portfolio, or spend and borrow against your digital assets with 1inch Card (powered by CryptoLife).

Builders and enterprise partners can access the core technologies powering 1inch to connect with an ecosystem that offers millions of tokens and tokenized RWAs, integrates 13+ networks and includes the first native swaps between Solana and the EVM

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.41B 1INCH |
| **Total Supply** | 1.50B 1INCH |
| **Max Supply** | 1.50B 1INCH |
| **Fully Diluted Valuation** | $111.61M |
| **Market Cap / FDV Ratio** | 0.94 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.65 (2021-10-27) |
| **Current vs ATH** | -99.14% |
| **All-Time Low** | $0.0650 (2026-06-06) |
| **Current vs ATL** | +14.29% |
| **24h Change** | -0.03% |
| **7d Change** | +5.11% |
| **30d Change** | -3.80% |
| **1y Change** | -78.47% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x111111111117dc0aa78b770fa6a738034120c302` |
| Base | `0xc5fecc3a29fb57b5024eec8a2239d4621e111cbe` |
| Binance Smart Chain | `0x111111111117dc0aa78b770fa6a738034120c302` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | 1INCH/USDT | N/A |
| Kraken | 1INCH/USD | N/A |
| Upbit | 1INCH/KRW | N/A |
| Bitget | 1INCH/USDT | N/A |
| KuCoin | 1INCH/USDT | N/A |
| Crypto.com Exchange | 1INCH/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X111111111117DC0AA78B770FA6A738034120C302/0X514910771AF9CA656AF840DFF83E8264ECF986CA | Spot |
| Uniswap V2 (Ethereum) | 0X111111111117DC0AA78B770FA6A738034120C302/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://1inch.com/](https://1inch.com/) |
| **Twitter** | [@1inch](https://twitter.com/1inch) |
| **Reddit** | [https://www.reddit.com/r/1inch/](https://www.reddit.com/r/1inch/) |
| **Telegram** | [OneInchNetwork](https://t.me/OneInchNetwork) (9,738 members) |
| **Discord** | [https://discord.com/invite/1inch](https://discord.com/invite/1inch) |
| **GitHub** | [https://github.com/1inch](https://github.com/1inch) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 67 |
| **GitHub Forks** | 43 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.67M |
| **Market Cap Rank** | #254 |
| **24h Range** | $0.0740 — $0.0758 |
| **CoinGecko Sentiment** | 0% positive |
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
- [[ethereum]]

---
