---
title: "Reserve Rights"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["RSR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://reserve.org/"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[stablecoin]]"]
---

# Reserve Rights

**Reserve Rights** (ticker **RSR**) is an [[ethereum|Ethereum]] ERC-20 token that powers the **Reserve protocol**, a platform for creating asset-backed, overcollateralized [[stablecoin|stablecoins]] called **RTokens**. RSR serves two core functions: (1) it is **staked as first-loss capital** to overcollateralize and backstop RTokens against collateral defaults, and (2) it is the **[[governance-token|governance token]]** used to propose and vote on RToken configurations. Stakers earn a share of RToken revenue in exchange for absorbing collateral risk.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | RSR |
| **Native Chain** | [[ethereum|Ethereum]] (also Base, Arbitrum) |
| **Market Cap Rank** | #306 |
| **Market Cap** | $81.35M |
| **Current Price** | $0.00130061 |
| **24h Change** | +0.58% |
| **7d Change** | -5.58% |
| **24h Volume** | $5.76M |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: with the market in **extreme fear** (Crypto [[fear-and-greed-index|Fear & Greed Index]] = 23) and an **Established Bear Market** regime as of 2026-06-21, RSR trades as a small-cap (#306) sub-cent token — fractionally green on the day but down ~5.6% on the week. Critically, at ~$0.00130 it sits **barely above its all-time low of $0.001214** (only ~7% above ATL), reflecting deep multi-year erosion. Turnover (~$5.8M, ~7% of cap) is reasonable for its float.

---

## Technology & Protocol

Reserve is a **stablecoin factory**, not a lending market or [[dex|DEX]]. Anyone can permissionlessly deploy an **RToken** — an [[stablecoin|asset-backed stablecoin]] defined by a configurable basket:

- **Collateral baskets** — an RToken (e.g., eUSD, an ETF-style index dollar) is fully backed by a basket of collateral that can include yield-bearing stablecoins (aUSDC, cUSDC), tokenized real-world assets, and other tokens. The basket earns yield, a portion of which flows to RSR stakers and RToken holders.
- **Mint / redeem arbitrage** — RTokens are minted by depositing the underlying basket and redeemed for it 1:1, so arbitrageurs keep the RToken near the value of its backing — the peg mechanism is *collateral redemption*, not an order book or algorithmic seigniorage.
- **RSR overcollateralization (staking)** — RSR staked on a given RToken acts as **first-loss capital**. If a collateral token defaults or depegs, the protocol seizes staked RSR to make RToken holders whole; in normal operation stakers earn a cut of the RToken's revenue. This is genuine **risk capital**, not passive yield.
- **Basket reconfiguration & governance** — RToken governors (RSR-weighted) can vote to swap out impaired collateral, adjust the basket, and tune parameters, with a delay mechanism that protects holders.

The model is deployed across Ethereum, Base, and Arbitrum.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~62.55B RSR |
| **Total Supply** | 100.00B RSR |
| **Max Supply** | 100.00B RSR |
| **Market Cap / FDV** | ~0.63 |
| **All-Time High** | $0.117424 (Apr 2021) |
| **All-Time Low** | $0.00121354 |

RSR has a very large fixed supply (100B max), with ~62.55B circulating — about 63% — leaving a **meaningful but capped dilution overhang** (FDV ~1.6x market cap; ~37B RSR, much of it in a "slow wallet," still to enter circulation). The token's economic role is **overcollateralization staking**: RSR holders stake on specific RTokens to provide first-loss protection and, in return, earn a portion of that RToken's revenue. APYs generally scale with the size/revenue of the RToken staked on. Importantly, Reserve's staking model is designed so late participants do not subsidize early ones, distinguishing it from many emission-driven "staking" schemes. With price hovering just above its all-time low, the token reflects deep derating despite the live RToken framework.

---

## Market Structure & Derivatives

**Spot venues (CEX):** RSR trades on **Binance**, **Kraken**, **Upbit** (BTC pair), **Bitget**, **KuCoin**, and **Crypto.com** Exchange.

**On-chain spot:** Liquid on [[uniswap|Uniswap]] V2/V3 ([[ethereum]], vs WETH); also deployed to Base and Arbitrum.

**Protocol context:** Reserve is **not a [[dex|DEX]]** — RSR's primary on-chain "use" is staking to overcollateralize RTokens, not trading on a native venue. RTokens themselves are baskets of collateral (yield-bearing stablecoins, tokenized real-world assets) that can be minted/redeemed against their backing, which is the protocol's core arbitrage / peg-maintenance mechanism rather than an order book.

**Derivatives:** RSR is listed as a perpetual on [[hyperliquid|Hyperliquid]] (RSR-PERP). As a low-priced, small-cap token, its perp [[funding-rate|funding rate]] and open interest can be volatile, especially around RWA-narrative momentum or [[stablecoin]]-sector news; the sub-cent price and thin spot depth make the perp prone to sharp liquidation moves (see [[perpetual-futures]]).

---

## Narrative & Category

Reserve sits in the **[[stablecoin]] infrastructure + Real World Assets (RWA)** category — a framework for permissionlessly launching overcollateralized, yield-bearing stablecoins backed by diversified collateral baskets including tokenized RWAs. RSR's narrative is leveraged to two strong themes: the growth of on-chain stablecoins and the tokenization of real-world assets. The token thesis is that as RTokens grow in market cap and revenue, demand to stake RSR (for yield and governance) rises with the collateral backstop required.

---

## Valuation Framing

RSR is a **leveraged call option on RToken adoption**. Its value should, in theory, scale with the total backstop demand created by RTokens: the more (and larger) the RTokens, the more first-loss RSR staking those baskets require and the more revenue stakers capture. Today, with RToken aggregate supply still modest, the ~$81M market cap mostly prices the *option* on stablecoin/RWA growth rather than realized staking cash flows — which is why the token trades near its all-time low despite a live, differentiated protocol. The downside is structural: if RTokens fail to scale, RSR has limited intrinsic value capture, and a 100B supply makes per-token appreciation arithmetically demanding.

---

## Peer Comparison

| Protocol | Token | Model | MC Rank | Market Cap | Notes |
|---|---|---|---|---|---|
| **Reserve** | RSR | Overcollateralized RToken factory | #306 | ~$81M | RSR = first-loss capital + governance |
| MakerDAO / Sky | MKR / SKY | CDP stablecoin (DAI/USDS) | top-tier | multi-B | Largest decentralized stablecoin issuer |
| Frax | FXS | Fractional-algorithmic stable | mid-cap | — | Hybrid collateral + governance |
| [[olympus\|Olympus]] | OHM | Treasury-backed money | #149 | ~$238M | Different model: treasury-backed token |

*Figures for non-Reserve peers are illustrative category placement, not snapshot data.*

---

## Notable History

- **May 2019:** RSR launched via an initial exchange offering (IEO) on Huobi Prime.
- Co-founded by **Nevin Freeman** and **Matt Elder**; the project has long framed its mission around stable, asset-backed currency and "solving coordination problems."
- Evolved from an early dual-token stablecoin design into the current **RToken** factory model, where anyone can deploy overcollateralized stablecoins governed and backstopped by RSR.
- RSR reached an all-time high near $0.117 in April 2021 and has since traded far below that.

---

## Risks

- **First-loss / collateral-default risk:** RSR stakers explicitly absorb losses if an RToken's collateral defaults — staking is genuine risk capital, not passive yield.
- **Stablecoin peg risk:** RTokens depend on the integrity and liquidity of their underlying collateral baskets; depeg or RWA-collateral failure would impair the system and RSR demand.
- **Large supply / sub-cent price:** A 100B max supply and sub-cent price mean large nominal moves on small dollar changes; ~37% of supply is not yet circulating.
- **Regulatory risk:** Stablecoins and tokenized RWAs face intense and evolving regulatory scrutiny.
- **Bear-market / liquidity risk:** Small-cap status (#306), trading near its all-time low, plus the current extreme-fear (F&G 23), Established Bear Market backdrop heightens volatility and [[slippage]].

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoin]]
- [[defi]]
- [[olympus]]
- [[hyperliquid]]
- [[funding-rate]]
- [[decentralized-exchange]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RSR |
| **Market Cap Rank** | #308 |
| **Market Cap** | $76.86M |
| **Current Price** | $0.00122872 |
| **Categories** | Decentralized Finance (DeFi), Real World Assets (RWA), Made in USA, Base Native |
| **Website** | [https://reserve.org/](https://reserve.org/) |

---

## Overview

What Is Reserve Rights (RSR)?

Reserve Rights (RSR) is an ERC-20 token that serves two main purposes for the Reserve protocol: overcollateralization of Reserve stablecoins (RTokens) through staking and governing them through proposing &amp; voting on changes to their configuration.

The Reserve Rights (RSR) token was launched in May 2019 following a successful initial exchange offering IEO on the Huobi Prime platform.

What is Reserve Rights (RSR) used for?

Besides being the governance token for Reserve stablecoins (RTokens), by which changes to RTokens can be proposed &amp; voted for with RSR, Reserve Rights exists as a backstop to make Reserve stablecoin (RToken) holders whole in the unlikely event of a collateral token default. In order for RSR holders to provide this overcollateralization, they can decide to stake on any one RToken, or divide their RSR tokens by staking on multiple RTokens. RSR holders can also decide not to stake their RSR at all.

In return for providing this first-loss capital, RSR stakers can expect to receive a portion of the revenue the RToken they stake on makes. As a general rule, RSR stakers can expect higher returns (APYs) the bigger the market cap of the RToken they stake on becomes.

In contrast with the “staking” you see in a lot of other projects these days, RSR staking is built to last. In Reserve’s model, late participants do not pay for early participants, nor is a trust in staking of other parties required.

For more detailed information on RSR staking, please refer to the RSR staking section in the protocol documentation: https://reserve.org/protocol/reserve_rights_rsr/#reserve-rights-staking.

Who are the founders of Reserve?

Reserve was co-founded by Nevin Freeman and Matt Elder. Freeman is a seasoned entrepreneur. He describes his life goal as "solving the coordination problems that are stopping humanity from achieving its potential."

Matt Elder, on the other hand, is an experienced engineer who previously worked for Goo...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 62.55B RSR |
| **Total Supply** | 100.00B RSR |
| **Max Supply** | 100.00B RSR |
| **Fully Diluted Valuation** | $122.87M |
| **Market Cap / FDV Ratio** | 0.63 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1174 (2021-04-16) |
| **Current vs ATH** | -98.95% |
| **All-Time Low** | $0.00104688 (2026-07-01) |
| **Current vs ATL** | +17.23% |
| **24h Change** | +0.35% |
| **7d Change** | -4.14% |
| **30d Change** | -15.30% |
| **1y Change** | -85.38% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x320623b8e4ff03373931769a31fc52a4e78b5d70` |
| Base | `0xab36452dbac151be02b16ca17d8919826072f64a` |
| Energi | `0xfce13bb63b60f6e20ed846ae73ed242d29129800` |
| Arbitrum One | `0xca5ca9083702c56b481d1eec86f1776fdbd2e594` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RSR/USDT | N/A |
| Kraken | RSR/USD | N/A |
| Upbit | RSR/BTC | N/A |
| Bitget | RSR/USDT | N/A |
| KuCoin | RSR/USDT | N/A |
| Crypto.com Exchange | RSR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X320623B8E4FF03373931769A31FC52A4E78B5D70/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X320623B8E4FF03373931769A31FC52A4E78B5D70/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://reserve.org/](https://reserve.org/) |
| **Twitter** | [@reserveprotocol](https://twitter.com/reserveprotocol) |
| **Telegram** | [reservecurrency](https://t.me/reservecurrency) (7,192 members) |
| **GitHub** | [https://github.com/reserve-protocol/rsr](https://github.com/reserve-protocol/rsr) |
| **Whitepaper** | [https://reserve.org/protocol/introduction/](https://reserve.org/protocol/introduction/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 19 |
| **GitHub Forks** | 4 |
| **Pull Requests Merged** | 1 |
| **Contributors** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.60M |
| **Market Cap Rank** | #308 |
| **24h Range** | $0.00122348 — $0.00126143 |
| **CoinGecko Sentiment** | 100% positive |
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
