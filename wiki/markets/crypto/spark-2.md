---
title: "Spark"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["SPK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://spark.fi/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[makerdao]]", "[[sky-protocol]]", "[[binance]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-yield]]"]
---

# Spark

**Spark** (ticker **SPK**) is an on-chain capital allocator and lending/savings protocol within the **Sky** ecosystem (the protocol formerly known as **MakerDAO**). Spark borrows from Sky's multi-billion-dollar stablecoin reserves and deploys that capital across DeFi, CeFi, and Real World Assets (RWA), packaging the yield into products like **sUSDS** and **sUSDC**. SPK is the governance and staking token of the protocol, which runs on [[ethereum|Ethereum]] with deployments to chains such as Base.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | SPK |
| **Current Price** | $0.01699574 |
| **Market Cap** | $51.69M |
| **Market Cap Rank** | #442 |
| **24h Volume** | $15.57M |
| **24h Change** | -3.59% |
| **7d Change** | -13.67% |
| **Fully Diluted Valuation** | $169.91M |
| **All-Time High** | $0.184472 (2025-07-23) |
| **All-Time Low** | $0.01677201 (2026-06-20) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The snapshot falls in a sharp risk-off phase: the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] reads **≈23 (Extreme Fear)** and the backdrop is an **established bear market**. SPK is among the weaker performers in this cohort, down ~3.6% on the day and ~13.7% on the week, and is trading essentially at all-time-low territory (ATL $0.01677 printed 2026-06-20, ~91% below the July 2025 ATH of $0.1845). Daily volume (~$15.6M) is high relative to its $51.7M cap (~30% turnover), reflecting active two-way flow.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.04B SPK |
| **Total Supply** | 10.00B SPK |
| **Max Supply** | 10.00B SPK |
| **Fully Diluted Valuation** | $169.91M |
| **Market Cap / FDV** | ~0.30 |

Only ~30% of the fixed 10B max supply is circulating, so SPK carries significant unlock/dilution overhang — a likely contributor to its recent underperformance. SPK is used for governance over Spark's risk parameters and capital-allocation policy, and for staking. The token was distributed in part via Binance HODLer Airdrops.

---

## How & Where It Trades

**Spot — centralized:**
- Binance (SPK/USDT), Kraken (SPK/EUR), Bitget (SPK/USDT), KuCoin (SPK/USDT), Crypto.com Exchange (SPK/USD)

**Spot — decentralized:**
- [[decentralized-exchange|Uniswap V3]] (Ethereum, USDC/SPK)

**Derivatives:** No major perpetual venue (e.g., [[hyperliquid|Hyperliquid]]) is recorded for SPK in the 2026-06-20 snapshot, so no [[funding-rate|funding]] or [[open-interest|open-interest]] figures are available; Binance and other CEXs offer SPK perpetuals. Spot turnover is healthy, concentrated on Binance and the Uniswap pool.

---

## Use Case, Narrative & Category

Spark sits in the **DeFi lending / savings / RWA / stablecoin** category and is the yield and liquidity engine of the Sky (ex-MakerDAO) ecosystem. Its products:

- **SparkLend** — a stablecoin lending market with governance-defined (not utilization-driven) rates, fed by the Spark Liquidity Layer
- **Spark Savings** — converts USDC / USDS (and planned USDT) into yield-bearing sUSDS / sUSDC
- **Spark Liquidity Layer (SLL)** — a backend allocator that routes liquidity to Aave, Morpho, and RWAs (e.g., BlackRock's BUIDL)

The thesis is that Spark acts as a two-sided capital allocator — sourcing from [[sky|Sky]]'s reserves and deploying across DeFi/CeFi/RWA to provide deep, consistent liquidity and packaged yield — rather than competing with other protocols.

---

## Peer Comparison — Stablecoin Yield / DeFi Lending & RWA Allocators

| Protocol | Token | Role | Backing / source |
|---|---|---|---|
| **Spark** | SPK | Capital allocator + lending/savings | [[sky\|Sky]] (ex-MakerDAO) reserves → DeFi/CeFi/RWA |
| Aave | AAVE | General-purpose money market | Utilization-driven rates; Spark routes liquidity *into* Aave |
| Morpho | MORPHO | Peer-to-peer lending optimizer | Spark allocates via Morpho vaults |
| [[huma-finance\|Huma Finance]] | HUMA | PayFi receivable financing | Real-world payment flows |
| Ethena | ENA | Synthetic-dollar yield (sUSDe) | Basis trade / funding capture |

Spark's distinction is that it is **not primarily a deposit-taking money market** competing for retail TVL — it is a **backend allocator** that sources cheap balance-sheet liquidity from [[sky|Sky]]'s multi-billion-dollar reserves and pushes it into Aave, Morpho and RWAs (e.g. BlackRock's BUIDL), capturing the spread. This gives it a structural funding advantage over standalone lenders, at the cost of deep dependence on its parent protocol.

---

## Valuation Framing (qualitative)

- **Unlock overhang dominates:** with only ~30% of the fixed 10B supply circulating (MC/FDV ~0.30) and SPK printing fresh all-time lows, scheduled vesting is the clearest driver of underperformance — the ~3.3x gap between FDV (~$170M) and cap (~$52M) is the key risk number.
- **Backed by real balance-sheet, not just emissions:** unlike pure governance tokens, SPK governs a protocol that earns a real spread on [[sky|Sky]] reserves deployed across DeFi/CeFi/RWA — there is a tangible fee engine, but token fee-capture vs that activity is the open question.
- **Parent-coupled beta:** SPK's value is tightly coupled to [[sky|Sky]]/MakerDAO's reserve size, risk appetite, and governance decisions; it is effectively a leveraged bet on the Sky ecosystem's growth.
- **Versus Huma:** both are heavily-locked stablecoin-yield plays, but Spark *allocates an existing reserve* while [[huma-finance|Huma]] *originates* real-world receivables — Spark trades scale/funding advantage for parent dependency; Huma trades origination upside for off-chain credit risk.

---

## Notable History

- **2025-07-23** — Reached its all-time high of **$0.184472** shortly after launch / token generation, distributed in part via a Binance HODLer Airdrop.
- **2025–2026** — Sustained decline (~-91% from ATH) under unlock pressure and the broader DeFi drawdown.
- **2026-06-20** — Printed a fresh all-time low of **$0.01677**.
- **2026-06-21** — Trading at ~$0.0170, hugging all-time lows, after a ~14% weekly drop amid extreme-fear conditions.

---

## Risks

- **Unlock / dilution risk** — with only ~30% of supply circulating and MC/FDV ~0.30, scheduled unlocks are a major overhang.
- **Parent-protocol dependency** — Spark relies on the [[sky|Sky]] / MakerDAO ecosystem for reserves; governance or risk changes at Sky flow directly to Spark.
- **RWA / CeFi counterparty risk** — deploying into CeFi and RWAs introduces off-chain counterparty and custody exposure beyond pure DeFi.
- **Smart-contract risk** — lending markets and liquidity routing carry exploit and liquidation-cascade risk.
- **Macro / regime risk** — in an established bear market with [[crypto-fear-and-greed-index|Fear & Greed]] at ≈23, recently launched DeFi tokens with heavy unlocks are especially vulnerable.

---

## Platform & Chain Information

**Native Chain:** Ethereum (with Base deployment)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc20059e0317de91738d13af027dfc4a50781b066` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://spark.fi/](https://spark.fi/) |
| **Twitter** | [@sparkdotfi](https://twitter.com/sparkdotfi) |
| **Discord** | [https://discord.com/invite/sparkdotfi](https://discord.com/invite/sparkdotfi) |

---

## Trading Profile

### Venues & liquidity

A USD-pegged stablecoin traded on [[binance|Binance]]. It is a PEG / cash-management instrument, NOT a directional asset — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. Because the target price is a fixed 1.00, position sizing and leverage are governed by depeg tail-risk rather than trend, so any leverage should be sized for gap moves around the peg rather than percentage swings. Venue availability shapes execution and sizing: concentration on a single primary CEX means redemption/mint access and on-venue depth set the practical clip size, and thinner books amplify slippage precisely during the depeg stress windows when exit matters most.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — buy SPK below 1.00 during a depeg and hold for reversion to par, the core play for a peg instrument.
- [[stablecoin-pair-arbitrage]] — trade SPK against other stablecoins (e.g. USDT/USDC) when their relative pegs diverge on-venue.
- [[stablecoin-yield]] — deploy idle SPK into yield venues as a cash-management overlay rather than holding it flat.
- [[mint-parity-arbitrage]] — arbitrage the gap between the secondary-market SPK price and its mint/redemption parity value.
- [[synthetic-stablecoin-depeg-arbitrage]] — hedge or arbitrage SPK depegs against synthetic-dollar exposure when backing model diverges from market price.
- [[carry-trade]] — capture the yield/funding differential of holding SPK versus the cost of the offsetting leg while the peg holds.

### Volatility & regime character

Qualitatively, the instrument's character is defined by peg tightness rather than directional volatility: in normal regimes it trades in a narrow band around 1.00 with low realized volatility, and its "regimes" are peg-hold versus depeg episodes. Backing model and redemption mechanics determine how quickly deviations mean-revert — transparent, redeemable reserves support fast reversion to par, while opaque or gated backing lengthens and deepens depeg episodes.

### Risk flags

- **Depeg risk** — the dominant risk; a break below 1.00 can be abrupt and, in a loss-of-confidence scenario, may not revert.
- **Reserve / backing transparency** — limited visibility into reserve composition and quality raises the odds and severity of a depeg.
- **Redemption gating** — if direct mint/redemption is paused or gated, the arbitrage that anchors the peg breaks down and deviations persist.
- **Regulatory** — stablecoins face evolving regulatory treatment that can affect issuance, venue listing, and redemption access.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SPKUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=SPKUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SPKUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=SPKUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[makerdao]]
- [[sky]]
- [[sky-protocol]]
- [[real-world-assets]]
- [[stablecoins]]
- [[huma-finance]]
- [[decentralized-exchange]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko, `raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SPK |
| **Market Cap Rank** | #414 |
| **Market Cap** | $53.18M |
| **Current Price** | $0.0177 |
| **Categories** | Decentralized Finance (DeFi), Lending/Borrowing Protocols, Stablecoin Issuer, Binance HODLer Airdrops, Governance |
| **Website** | [https://spark.fi/](https://spark.fi/) |

---

## Overview

Spark is an onchain capital allocator, with $3.86B deployed across DeFi, CeFi, and RWA. It unlocks capital efficiency at scale, auto-balancing allocations based on market conditions while maintaining a conservative risk profile. Spark was created to solve DeFi’s core inefficiencies: fragmented liquidity, unstable yields, and idle stablecoin capital. It acts as a two-sided capital allocator—borrowing from Sky’s $6.5B+ reserves and deploying across DeFi, CeFi, and RWAs to provide deep, consistent liquidity. This yield is packaged into products like sUSDS and sUSDC, offering users programmable, fee-free income. Rather than competing with protocols, Spark powers them as the liquidity and yield infrastructure for onchain finance.

Access to Deep, Scalable Liquidity: Spark taps into Sky’s $6.5B+ stablecoin reserves, enabling large-scale capital deployment across DeFi, CeFi, and RWAs. User-Friendly Yield Products: Yield is delivered through stablecoins like sUSDS and sUSDC—fully composable, fee-free, and available across chains.

SparkLend: A stablecoin lending market. Unlike other lending protocols where rates fluctuate based on utilization or loan size, SparkLend offers governance-defined rates that do not vary based on those factors. This is made possible by Spark’s Liquidity Layer (SLL), which supplies consistent stablecoin liquidity to the protocol.

Spark Savings: A product for earning yield on stablecoins like USDC, and USDS (and soon, USDT) by converting them into yield-bearing sUSDS or sUSDC. These yield tokens are composable with other DeFi protocols, making it easy to put capital to work while maintaining exposure to onchain yield at a competitive risk-adjusted rate.

Spark Liquidity Layer (SLL): A backend capital allocator that routes liquidity to other protocols like Aave, Morpho, and even RWAs (e.g., BlackRock’s BUIDL). One of the most important SLL deployments on Base is the Spark USDC Morpho Vault, which currently supplies $95M USDC, making it the largest l...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.99B SPK |
| **Total Supply** | 10.00B SPK |
| **Max Supply** | 10.00B SPK |
| **Fully Diluted Valuation** | $177.58M |
| **Market Cap / FDV Ratio** | 0.30 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1845 (2025-07-23) |
| **Current vs ATH** | -90.36% |
| **All-Time Low** | $0.0161 (2026-06-24) |
| **Current vs ATL** | +10.72% |
| **24h Change** | +3.06% |
| **7d Change** | +2.24% |
| **30d Change** | -13.59% |
| **1y Change** | -46.23% |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SPK/USDT | N/A |
| Kraken | SPK/USD | N/A |
| Upbit | SPK/KRW | N/A |
| Bitget | SPK/USDT | N/A |
| KuCoin | SPK/USDT | N/A |
| Crypto.com Exchange | SPK/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XC20059E0317DE91738D13AF027DFC4A50781B066/0X6B175474E89094C44DA98B954EEDEAC495271D0F | Spot |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $15.40M |
| **Market Cap Rank** | #414 |
| **24h Range** | $0.0172 — $0.0184 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
