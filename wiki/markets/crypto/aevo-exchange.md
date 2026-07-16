---
title: "Aevo"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["AEVO", "Aevo Exchange", "Ribbon Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.aevo.xyz/"
related: ["[[crypto-markets]]", "[[decentralized-exchange]]", "[[derivatives]]", "[[ethereum]]", "[[governance-token]]", "[[hyperliquid]]", "[[layer-2]]", "[[options]]", "[[order-book]]", "[[perpetual-futures]]"]
---

# Aevo

**Aevo** (AEVO) is a high-performance decentralized **derivatives** exchange offering both **[[options|options]]** and **[[perpetual-futures|perpetual futures]]**, built on its own Ethereum [[ethereum|Ethereum]] Layer 2 rollup. Aevo is the **2024 rebrand and evolution of Ribbon Finance**, the well-known DeFi structured-products / options-vaults protocol; the RBN token was migrated to AEVO. As of 2026-06-22 AEVO trades at **$0.01954606**, ranking **#875** by market capitalization with a market cap of roughly **$17.9M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.01954606 · rank #875 · market cap $17,899,750 · 24h -2.12% · 7d -2.76%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AEVO |
| **Market Cap Rank** | #875 |
| **Market Cap** | ~$17.90M |
| **Current Price** | $0.01954606 |
| **24h Change** | -2.12% |
| **7d Change** | -2.76% |
| **Products** | Options DEX, Perpetual-futures DEX, structured-product vaults |
| **Lineage** | Rebrand/evolution of Ribbon Finance (RBN → AEVO, 2024) |
| **Founder** | Julian Koh (Ribbon Finance) |
| **Architecture** | Custom Ethereum L2 rollup; off-chain orderbook + on-chain settlement |
| **Backers** | DragonFly Capital, Pantera Capital; launched via Binance Launchpool |
| **Categories** | DeFi, Derivatives, Perpetuals, Ethereum Ecosystem, Layer 2 (L2) |
| **Website** | [https://www.aevo.xyz/](https://www.aevo.xyz/) |

> In the 2026-06-22 [[crypto-market-regime|Extreme-Fear regime]] (Fear & Greed Index 21), AEVO fell -2.12% intraday and -2.76% over the week, tracking the soft derivatives-DEX tape.

---

## Overview

Aevo is one of the few decentralized venues that offers **on-chain options trading** alongside perpetual futures, addressing a market that remained dominated by centralized exchanges (Deribit, etc.). Its design pairs a **high-throughput off-chain orderbook and matching engine** with **on-chain settlement** on a custom Ethereum L2 rollup, aiming to deliver CEX-like speed and an order-book experience while keeping custody and settlement on-chain. Products include standardized **options** (calls/puts across strikes and expiries), **perpetual futures**, pre-launch token futures, and yield-bearing **vaults** inherited from Ribbon's structured-products heritage.

### Lineage: Ribbon Finance → Aevo

Ribbon Finance, founded by Julian Koh, became one of DeFi's best-known **structured-products** protocols, famous for **DeFi Option Vaults (DOVs)** that automated covered-call and put-selling strategies for depositors. The team built **Aevo** as a dedicated options + perps exchange, and in **2024 consolidated the ecosystem under the Aevo brand, migrating the RBN governance token to AEVO**. The vault products continued under the Aevo umbrella. This rebrand is essential context: AEVO's history, token distribution, and reputation inherit directly from Ribbon.

The **AEVO token** is the protocol's **governance** token (governing the exchange and its parameters) and is used in incentive/staking programs (e.g., locking AEVO for rewards and fee benefits) — it captures the value-accrual narrative tied to [[derivatives]] trading volume.

---

## Mechanism & Architecture

Aevo's design is a deliberate hybrid that tries to keep the strengths of a [[centralized-exchange|CEX]] while preserving non-custodial settlement:

- **Off-chain order book + matching engine** — orders are placed, cancelled and matched off-chain on a high-throughput engine. This is what makes an [[options]] book — which needs many strikes, expiries and rapid quote updates — actually usable on-chain. A naive fully on-chain [[order-book]] cannot support the quote churn an options market maker requires.
- **On-chain settlement on a custom Ethereum [[layer-2|L2]] rollup** — trades settle and collateral is custodied on Aevo's own rollup, so the matching engine cannot forge balances; users retain on-chain ownership of margin.
- **Unified cross-margin** — a single margin account can back both [[perpetual-futures|perps]] and [[options]] positions, with portfolio-style risk netting (e.g., an options hedge can offset perp exposure), improving capital efficiency for sophisticated traders.
- **Structured-product vaults** — inherited from Ribbon's **DeFi Option Vaults (DOVs)**: depositors earn yield from automated [[options]] strategies (covered calls, cash-secured puts) that the vault sells on a schedule.

### Worked example (illustrative)

A trader is long ETH perps on Aevo and wants downside protection ahead of a macro event. Instead of closing the position, they buy an ETH put option on the same venue. Because Aevo uses **unified cross-margin**, the put's hedging effect reduces the margin required against the perp — the portfolio is risk-netted rather than margined leg-by-leg. The order is matched off-chain in milliseconds, but the resulting positions and collateral live on Aevo's L2, so the trader never gives up custody. On the other side, a yield-seeking depositor in a covered-call vault is effectively the natural seller of similar optionality. Mechanics are illustrative; the architecture is the point.

---

## Comparison vs Competitors

| Venue | Type | Options? | Perps? | Distinctive edge | Main constraint |
|---|---|---|---|---|---|
| **Aevo (AEVO)** | Decentralized, custom L2 + off-chain book | Yes | Yes | Few DEXs with *liquid on-chain options* + cross-margin + DOV vaults | Options liquidity / open interest |
| Deribit | Centralized | Yes | Yes | Dominant crypto options liquidity | Custodial / centralized |
| [[hyperliquid\|Hyperliquid]] | Decentralized, own L1 CLOB | Limited | Yes | Captured large perp share; CEX-like on-chain book | Perps-centric |
| [[gmx\|GMX]] | Decentralized, oracle-priced pools | No | Yes | Zero-slippage oracle execution vs pooled LPs | No native options |
| [[dydx\|dYdX]] | Decentralized, app-chain book | No | Yes | Mature perps order book | Perps-only |
| [[woo-network\|WOOFi]] | Decentralized, sPMM | No | Yes | Multi-chain shared liquidity | Perps/spot only |

Aevo's genuine differentiator is **on-chain options liquidity** — a niche where most DeFi competitors simply do not play and where the main rival is centralized (Deribit). On the perps side it fights a crowded field; [[hyperliquid|Hyperliquid]] in particular captured outsized share, which is the binding pressure on Aevo's perp volumes.

---

## Governance & Value Accrual

- **Governance** — AEVO holders govern the exchange, its parameters and incentive allocation.
- **Staking / fee benefits** — locking AEVO grants rewards and fee discounts, the standard derivatives-DEX loyalty loop; value accrual scales with trading volume and open interest.
- **Inherited distribution** — because RBN was migrated 1:1-style into AEVO during the 2024 consolidation, the token's holder base, vesting and treasury inherit directly from Ribbon Finance — important context for both governance weight and ongoing supply dynamics.

The accrual story is revenue-reflexive and, for an options venue, especially **liquidity-gated**: thin books mean thin volume mean thin fees. Open interest and two-sided depth are the metrics that ultimately drive the token, more than headline TVL.

---

## History & Notable Events

- **2021** — **Ribbon Finance**, founded by **Julian Koh**, pioneers **DeFi Option Vaults (DOVs)**, automating covered-call and put-selling strategies for depositors and becoming one of DeFi's best-known structured-products protocols (RBN token).
- **2022–2023** — The team builds **Aevo** as a dedicated [[options]] + [[perpetual-futures|perps]] exchange on a custom [[layer-2|L2]] rollup, pairing an off-chain matching engine with on-chain settlement.
- **2024-03** — Aevo lists via **Binance Launchpool**; AEVO peaks at its all-time high of **$3.76 on 2024-03-28** during launch-period hype, then re-rates sharply lower as float expands — a textbook launch-top.
- **2024** — The ecosystem is **consolidated under the Aevo brand and the RBN governance token migrates to AEVO**; vault products continue under the Aevo umbrella.
- **2024–2026** — Operates through intensifying perp-DEX competition (notably [[hyperliquid|Hyperliquid]]'s rise); AEVO trades ~99% below its listing-era ATH, ~$0.0195 as of 2026-06-22 amid Extreme-Fear conditions (Fear & Greed 21).

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~916.32M AEVO |
| **Total Supply** | ~1.00B AEVO |
| **Max Supply** | 1.00B AEVO |
| **Fully Diluted Valuation** | ~$19M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.92 |

AEVO has a 1 billion max supply, most of which is already circulating (a high market-cap-to-FDV ratio of ~0.92), implying limited remaining unlock-driven dilution relative to lower-float peers.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.76 (2024-03-28) |
| **Current vs ATH** | ~-99% |
| **24h Change** | -2.12% |
| **7d Change** | -2.76% |

AEVO trades roughly 99% below its March 2024 listing-period ATH — a textbook example of a token that peaked at launch (during Binance Launchpool hype) and then re-rated sharply lower as the float expanded and derivatives-DEX competition intensified. Price action into 2026-06-22 was soft (-2.12% on the day, -2.76% on the week) in line with the Extreme-Fear tape.

---

## Competitive Position

Aevo's distinctiveness is being one of very few decentralized venues with **liquid on-chain options** in addition to perps. On the perps side it competes with a crowded field — [[gmx|GMX]], [[dydx|dYdX]], [[hyperliquid|Hyperliquid]], [[woo-network|WOOFi]], and others — where Hyperliquid in particular captured large share. On the options side its main competition is centralized (Deribit) plus a handful of DeFi options protocols. The structured-vault heritage from Ribbon gives it a differentiated product line, but liquidity and open interest are the binding constraints for an options venue.

---

## Risks

- **Derivatives complexity:** Options and perps protocols have intricate margining, liquidation, and oracle logic — a rich surface for bugs and exploits.
- **Liquidity dependence:** Options markets need deep, two-sided liquidity to be usable; thin order books undermine the product.
- **Intense perp competition:** Market share has consolidated toward a few perp DEXs, pressuring Aevo's volumes.
- **Custom L2 risk:** Reliance on its own rollup adds sequencer/bridge/upgrade trust assumptions.
- **Token overhang & rebrand baggage:** The RBN→AEVO migration and launch-era distribution shape ongoing sell pressure and sentiment.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb528edbef013aff855ac3c50b381f253af13b997` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AEVO/USDT | N/A |
| Kraken | AEVO/USD | N/A |
| Bitget | AEVO/USDT | N/A |
| KuCoin | AEVO/USDT | N/A |
| Crypto.com Exchange | AEVO/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48/0XB528EDBEF013AFF855AC3C50B381F253AF13B997 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.aevo.xyz/](https://www.aevo.xyz/) |
| **Twitter** | [@aevoxyz](https://twitter.com/aevoxyz) |
| **GitHub** | [https://github.com/aevoxyz](https://github.com/aevoxyz) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume (2026-04-09 snapshot)** | $10.73M |
| **Market Cap Rank** | #875 |
| **24h Range (2026-04-09 snapshot)** | $0.0238 — $0.0251 |
| **Last Updated** | 2026-06-22 (price/cap); volume/range from 2026-04-09 snapshot |

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
- [[decentralized-exchange]]
- [[perpetual-futures]]
- [[options]]
- [[derivatives]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
