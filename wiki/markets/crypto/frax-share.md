---
title: "Frax (prev. FXS)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, stablecoin, stablecoins]
aliases: ["FRAX", "FXS", "Frax Finance", "Frax Share", "frxETH", "frxUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://frax.finance"
related: ["[[automated-market-maker]]", "[[binance]]", "[[crypto-markets]]", "[[curve-finance]]", "[[dai]]", "[[defi]]", "[[ethereum]]", "[[governance-token]]", "[[lido]]", "[[liquid-staking]]", "[[mint-parity-arbitrage]]", "[[rocket-pool]]", "[[stablecoin]]", "[[stablecoin-depeg-profit-capture]]"]
---

# Frax (prev. FXS)

**FRAX** (formerly ticker **FXS**) is the governance and value-accrual token of **Frax Finance**, one of the longest-running [[stablecoin]] and [[defi|DeFi]] protocols on [[ethereum|Ethereum]]. Frax began in 2020 as a fractional-algorithmic stablecoin project and has since expanded into a full "decentralized central bank" stack spanning a stablecoin, a [[liquid-staking|liquid-staking]] ETH derivative, a lending market, an [[automated-market-maker|AMM]], and its own [[ethereum|Ethereum]] Layer-2 chain, Fraxtal. The token trades at **$0.268447**, ranking **#723** by market capitalization (**$25,126,264** market cap), down **-1.53%** over 24h and down **-5.44%** over the past 7 days.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## The 2025 "North Star" Rebrand (read this first)

In 2025 Frax executed a major rebrand known as the **Frax North Star** plan that **renamed its tokens**, which is critical to avoid confusion:

- The **old governance token, FXS** (originally "Frax Share"), was **renamed to FRAX** and became the protocol's single flagship gas/governance/value-accrual asset. This is the token described on this page (CoinGecko id `frax-share`).
- The **legacy FRAX stablecoin** (the $1-pegged unit) was **renamed to frxUSD** to free up the FRAX ticker for the governance token and to position frxUSD as a fully-collateralized, institutionally-backed stablecoin.

So as of 2025+, "FRAX" = the governance token (ex-FXS), and "frxUSD" = the stablecoin (ex-FRAX). The CoinGecko id `frax-share` preserves the historical FXS lineage. Older documentation, exchange listings (some still show `FXS/USD`), and articles predating the rebrand use the inverted naming.

---

## Overview

Frax Finance positions itself as a vertically integrated decentralized stable-money ecosystem. Its core products are:

- **frxUSD** — the protocol's stablecoin (formerly the FRAX stablecoin). Originally a fractional-algorithmic design that was partially backed by collateral and partially stabilized algorithmically, Frax governance progressively raised the collateral ratio to 100% and moved toward a fully-collateralized, RWA/T-bill-backed model marketed for institutional use.
- **frxETH / sfrxETH** — Frax's [[liquid-staking|liquid-staking]] ETH derivatives. frxETH tracks ETH 1:1, while sfrxETH accrues Ethereum staking rewards, competing with [[lido|Lido]]'s stETH and [[rocket-pool|Rocket Pool]]'s rETH.
- **Fraxlend** — an isolated-pair lending/borrowing market.
- **Fraxswap** — a native [[automated-market-maker|AMM]] featuring a time-weighted average market maker (TWAMM) for executing large orders over time.
- **Fraxtal** — Frax's own [[ethereum|Ethereum]] Layer-2 rollup (OP-Stack based), where FRAX is used for gas and ecosystem incentives.

---

## Token Role: FRAX (ex-FXS)

FRAX is the governance and value-capture layer of the protocol:

- **Governance** — FRAX holders vote on protocol parameters (collateral ratios, new collateral types, fee switches, emissions) through Frax governance.
- **veFRAX / vote-escrow** — Frax historically used a vote-escrow model (veFXS) where locking the token granted boosted rewards and governance weight, and a share of protocol revenue. This vote-escrow value-accrual design carries into the renamed token.
- **Value accrual** — protocol revenue (AMO yields, lending interest, stablecoin reserve yield, L2 fees) is directed toward the token via buybacks/distributions, making FRAX a claim on the cash flows of the broader Frax stack.
- **Gas on Fraxtal** — FRAX serves as the gas/utility token of the Fraxtal L2.

A defining Frax mechanism is the **Algorithmic Market Operations Controller (AMO)** — autonomous smart contracts that deploy idle stablecoin collateral into yield strategies (e.g., [[curve-finance|Curve]] liquidity, lending) without changing the peg, generating revenue that ultimately benefits FRAX holders.

### How an AMO works (worked illustration)

Suppose the protocol holds idle USDC collateral backing frxUSD. A **Curve AMO** can mint new frxUSD and pair it with that USDC to deepen a Curve stable pool. This earns trading fees and CRV/CVX incentives while *tightening* the peg (more on-chain liquidity to arbitrage against). Crucially, the minted frxUSD is "owned" by the protocol and is not circulating in user hands as unbacked supply — it is collateralized by the matched USDC in the pool, and the AMO can unwind (burn the frxUSD, reclaim collateral) if the peg drifts. The four classic AMO properties are: **decollateralize** (deploy collateral for yield), **market operations** (provide/withdraw liquidity), **recollateralize** (pull collateral back to defend the peg), and **FXS/FRAX buybacks** (route profits to the governance token). This turns the stablecoin reserve from a dead pile of T-bills into a yield engine whose profits accrue to FRAX.

### The Frax product stack at a glance

| Product | What it is | Competes with |
|---|---|---|
| **frxUSD** (ex-FRAX) | $1-pegged stablecoin; now collateralized / RWA-backed | [[dai\|DAI]], USDC, USDT, [[liquity\|LUSD/BOLD]] |
| **frxETH / sfrxETH** | [[liquid-staking\|liquid-staking]] ETH; sfrxETH accrues yield | [[lido\|Lido]] stETH, [[rocket-pool\|Rocket Pool]] rETH |
| **Fraxlend** | Isolated-pair lending market | [[aave\|Aave]], [[euler\|Euler]], Morpho |
| **Fraxswap** | AMM with TWAMM (time-weighted average market maker) | [[uniswap\|Uniswap]], [[curve-finance\|Curve]] |
| **Fraxtal** | OP-Stack [[ethereum\|Ethereum]] Layer-2; FRAX is gas | Base, Optimism, Arbitrum |
| **FRAX** (ex-FXS) | Governance + value-accrual + Fraxtal gas token | — |

The **TWAMM** in Fraxswap is itself a notable innovation: it splits a large order into many infinitesimal trades executed continuously over a chosen window, minimizing price impact and front-running — useful for the protocol's own large AMO operations and for whales.

---

## Competitive Position

Frax competes across several DeFi verticals simultaneously: against [[stablecoin|stablecoins]] like [[dai|DAI]], USDC, and USDT in stable money; against [[lido|Lido]] and [[rocket-pool|Rocket Pool]] in liquid staking; and against general-purpose L2s with Fraxtal. Its differentiator is integration — collateral, staking, lending, AMM and an L2 are designed to reinforce one another and route yield back to a single token. The trade-off is complexity and surface area: a protocol this broad has more components that can fail and a token whose value depends on many moving parts performing.

---

## Risks

- **Stablecoin/depeg risk** — Frax's history as a partly-algorithmic stablecoin means it carries reputational and structural baggage from the broader 2022 algorithmic-stablecoin collapses (e.g., UST/Terra); a frxUSD depeg would directly impair the ecosystem's value.
- **Rebrand confusion** — the FXS→FRAX and FRAX→frxUSD renaming creates real risk of users transacting the wrong asset; listings and tooling lag the rename.
- **Smart-contract & complexity risk** — AMOs, Fraxlend, Fraxswap, and the Fraxtal bridge are all attack surfaces.
- **Collateral/RWA risk** — moving toward T-bill/RWA backing introduces off-chain counterparty and custody dependencies.
- **Token performance** — FRAX trades ~99% below its 2022 all-time high (~$42.80), reflecting both the broad DeFi-governance-token drawdown and the dilution/repricing around the rebrand. The market context as of 2026-06-22 is risk-off ([[bitcoin|BTC]] ~$64,508; Fear & Greed Index 21, "Extreme Fear").
- **Governance-concentration / vote-escrow risk** — value accrual depends on the veFRAX model and DAO decisions to switch on/route fees; concentrated lockers can dominate governance, and any change to the AMO or fee-switch policy materially affects the token thesis.

> *This page is for informational purposes only and is not investment advice. Crypto assets are highly volatile.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FRAX (formerly FXS) |
| **Market Cap Rank** | #723 |
| **Market Cap** | $25,126,264 |
| **Current Price** | $0.268447 |
| **24h Change** | -1.53% |
| **7d Change** | -5.44% |
| **Categories** | Decentralized Finance (DeFi), Stablecoin Issuer, Liquid Staking Governance Tokens, Automated Market Maker (AMM), Curve Ecosystem, Fraxtal Ecosystem, Governance |
| **Website** | [https://frax.finance](https://frax.finance) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 95.40M FRAX |
| **Total Supply** | 99.68M FRAX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $42.66M |
| **Market Cap / FDV Ratio** | 0.96 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $42.80 (2022-01-12) |
| **Current vs ATH** | -99.00% |
| **All-Time Low** | $0.3846 (2026-04-07) |
| **Current vs ATL** | +11.27% |
| **24h Change** | +5.81% |
| **7d Change** | +3.42% |
| **30d Change** | -31.20% |
| **1y Change** | -73.97% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` |
| Fantom | `0x7d016eec9c25232b01f23ef992d98ca97fc2af5a` |
| Polygon Zkevm | `0x6b856a14cea1d7dcfaf80fa6936c0b75972ccace` |
| Moonriver | `0x6f1d1ee50846fcbc3de91723e61cb68cfa6d0e98` |
| Evmos | `0xd8176865dd0d672c6ab4a427572f80a72b4b4a9c` |
| Solana | `6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct` |
| Harmony Shard 0 | `0x0767d8e1b05efa8d6a301a65b324b6b66a1cc14c` |
| Polygon Pos | `0x1a3acf6d19267e2d3e7f898f42803e90c9219062` |
| Binance Smart Chain | `0xe48a3d7d0bc88d552f730b62c006bc925eadb9ee` |
| Arbitrum One | `0x9d2f299715d94d8a7e6f5eaa8e654e8c74a988a7` |
| Avalanche | `0x214db107654ff987ad859f34125307783fc8e387` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | FRAX/USDT | N/A |
| Kraken | FXS/USD | N/A |
| Bitget | FRAX/USDT | N/A |
| Crypto.com Exchange | FRAX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X3432B6A60D23CA0DFCA7761B7AB56459D9C964D0/0X853D955ACEF822DB058EB8505911ED77F175B99E | Spot |
| Uniswap V3 (Ethereum) | 0X3432B6A60D23CA0DFCA7761B7AB56459D9C964D0/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://frax.finance](https://frax.finance) |
| **Twitter** | [@fraxfinance](https://twitter.com/fraxfinance) |
| **Telegram** | [fraxfinance](https://t.me/fraxfinance) (14,901 members) |
| **Discord** | [https://discord.gg/MTZu6Hf57d](https://discord.gg/MTZu6Hf57d) |
| **GitHub** | [https://github.com/fraxfinance/frax-solidity](https://github.com/fraxfinance/frax-solidity) |
| **Whitepaper** | [https://github.com/FraxFinance/frax-solidity/blob/master/frax_whitepaper_v1.pdf](https://github.com/FraxFinance/frax-solidity/blob/master/frax_whitepaper_v1.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.93M |
| **Market Cap Rank** | #684 |
| **24h Range** | $0.4040 — $0.4512 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Notable Events

- **December 2020** — Frax launches as the first **fractional-algorithmic** stablecoin: FRAX (the stablecoin) was partly backed by collateral (USDC) and partly stabilized algorithmically, with the **collateral ratio** moving up or down with market demand. FXS (Frax Share) was the governance/seigniorage token absorbing volatility.
- **January 2022** — FXS reaches its all-time high near **$42.80** during the DeFi bull market.
- **May 2022 — Terra/UST collapse.** The implosion of the algorithmic stablecoin UST cast a shadow over *all* algo-stablecoins. Frax, which had a meaningful algorithmic component, weathered the storm without depegging but the event accelerated a strategic pivot toward full collateralization.
- **2023** — Frax governance votes to move the collateral ratio to **100%**, effectively ending the "algorithmic" portion and recasting FRAX as a fully-backed stablecoin. The protocol expands frxETH/sfrxETH and Fraxlend.
- **2024 — Fraxtal launch.** Frax ships its own OP-Stack [[ethereum|Ethereum]] Layer-2 ("Fraxtal"), using the token for gas and incentives — a major expansion of scope.
- **2025 — "North Star" rebrand.** FXS is renamed **FRAX** (single flagship token) and the legacy FRAX stablecoin is renamed **frxUSD**, repositioned as a fully-collateralized, RWA/T-bill-backed stablecoin aimed at institutions. (See the section at the top of this page.)
- **2025–2026** — FRAX trades deep in the post-bull drawdown (~99% off ATH), with the investment thesis hinging on frxUSD adoption, Fraxtal traction, and fee routing to the token.

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

> *Scope note: this page's asset is FRAX, the **governance / value-accrual token** (ex-FXS), which is a directional, volatile asset — not itself $1-pegged. The peg-oriented framing below applies to the Frax **stablecoin (frxUSD)** whose stability, backing and arbitrage the FRAX token governs and derives revenue from. Read the strategies as peg/cash-management plays on the Frax stablecoin leg of the ecosystem, monitored via the `FRAXUSDT` market on Binance.*

### Venues & liquidity

The Frax stablecoin leg is treated as a **USD-pegged, cash-management instrument** rather than a directional bet — the relevant questions are peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. On centralized venues the pair is available on [[binance|Binance]] (FRAX/USDT), with additional listings on Kraken, Bitget and Crypto.com; on-chain, deep [[curve-finance|Curve]] and [[uniswap|Uniswap]] stable pools (partly seeded by protocol AMOs) provide the primary arbitrage surface. Because peg instruments trade in a razor-thin band around 1.00, edge comes from size and low fees rather than leverage: applying leverage to a near-par asset is inefficient and mostly amplifies funding/borrow cost, so sizing is driven by available depth and redemption/mint capacity. Venue availability shapes execution — CEX legs give fast entry/exit for depeg capture, while on-chain pools and the protocol's mint/redeem path define where parity arbitrage actually closes.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — buy the Frax stablecoin below 1.00 during a stress/depeg episode and hold for reversion to par, exiting on peg recovery.
- [[stablecoin-pair-arbitrage]] — arbitrage the Frax stable unit against USDT/USDC/[[dai|DAI]] across Binance and on-chain [[curve-finance|Curve]]/[[uniswap|Uniswap]] pools when relative pricing dislocates.
- [[mint-parity-arbitrage]] — exploit the Frax protocol's collateralized mint/redeem path: mint or redeem against reserves whenever the market price diverges from the 1.00 collateral parity.
- [[stablecoin-yield]] — deploy the Frax stable unit into AMO-fed liquidity and lending (Fraxlend, Curve) to earn reserve/incentive yield on an otherwise flat, cash-like position.
- [[synthetic-stablecoin-depeg-arbitrage]] — trade dislocations rooted in Frax's fractional-algorithmic heritage and now-collateralized backing model, where synthetic/backing mechanics can lag market price during stress.

### Volatility & regime character

The stablecoin leg is characterized by peg tightness rather than trend: in normal regimes it holds within a very narrow band around 1.00, punctuated by rare depeg episodes tied to collateral stress, contagion (e.g., the 2022 Terra/UST-driven repricing of all algo-stablecoins), or reserve concerns. The backing model has shifted materially — from a fractional-algorithmic design toward a fully-collateralized, RWA/T-bill-backed model — which alters redemption mechanics and the plausibility of arbitrage closing at par. The FRAX governance token itself, by contrast, is high-volatility and directional (deep post-2022 drawdown), so the two legs must not be conflated when sizing peg trades.

### Risk flags

- **Depeg risk** — historical algorithmic heritage and contagion sensitivity mean the stable unit can trade away from 1.00 faster than redemption can restore it.
- **Reserve / backing transparency** — value depends on the reported collateral ratio and RWA/T-bill backing; opacity or off-chain custody failure directly undermines any parity trade.
- **Redemption gating** — mint/redeem parity arbitrage assumes the collateralized redemption path stays open; governance or contract-level gating can strand an arbitrage.
- **Regulatory** — stablecoin and RWA-backing regimes are an evolving regulatory surface that can affect redemption, listing, and custody.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=FRAXUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=FRAXUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=FRAXUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=FRAXUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoin]]
- [[liquid-staking]]
- [[defi]]
- [[curve-finance]]
- [[automated-market-maker]]
- [[dai]]
- [[lido]]
- [[rocket-pool]]
- [[liquity]]
- [[governance-token]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko)
- General market knowledge; protocol mechanics (AMO, TWAMM, Fraxtal) and the 2025 North Star rebrand from public Frax documentation. No additional specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
