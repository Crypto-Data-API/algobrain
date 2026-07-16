---
title: "dYdX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["DYDX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://dydx.trade"
related: ["[[cosmos]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[lighter]]", "[[perp-dex-aggregation]]", "[[perpetual-futures]]"]
---

# dYdX

**dYdX** (DYDX) is one of DeFi's longest-running perpetual-futures [[decentralized-exchange|DEXs]], originally launched as an [[ethereum|Ethereum]] L2 (StarkEx) order-book perp venue and since migrated to **dYdX Chain**, a sovereign application-specific blockchain built with the [[cosmos|Cosmos]] SDK. The protocol runs a fully on-chain central limit order book (CLOB) operated by validators, offering high-leverage [[perpetual-futures|perpetual futures]] with off-chain-grade matching speed and on-chain settlement. The DYDX token is used for staking/security of the chain, validator delegation, governance, and trading-fee/rewards mechanics.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | DYDX |
| **Market Cap Rank** | #268 |
| **Market Cap** | $100.72M |
| **Current Price** | $0.119307 |
| **24h Change** | -1.27% |
| **7d Change** | -1.08% |
| **24h Volume** | $3.86M |
| **Circulating Supply** | ~844.08M DYDX |
| **Total Supply** | ~958.34M DYDX |
| **Max Supply** | 1.00B DYDX |
| **Fully Diluted Valuation** | ~$114.35M |
| **All-Time High** | $4.52 (2021) — now ~-97.4% |
| **All-Time Low** | $0.078815 — now ~+51.4% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broad market is in **extreme fear** (Crypto Fear & Greed Index = 23) within an **Established Bear Market** long-horizon regime as of 2026-06-21. DYDX sits well below mid-cap status (rank #268) with thin daily turnover (~$3.9M, under 4% of cap) relative to its float, typical of a DeFi-governance token deep in a bear cycle. It trades ~51% above its all-time low but ~97% below its 2021 ATH.

---

## Technology & Protocol

dYdX Chain is a **purpose-built Cosmos SDK appchain for derivatives** rather than a smart contract on a shared L1:

- **On-chain CLOB** — unlike AMM-based perp DEXs, dYdX runs a true central limit order book. Validators each maintain an in-memory order book and matching engine; orders and cancellations propagate off-chain at high speed, while *fills* settle on-chain. This delivers limit orders, tight spreads, and a maker/taker fee schedule closer to a CEX.
- **Validator-operated matching** — the ~60-validator [[cosmos|Cosmos]] proof-of-stake set both secures the chain and runs the matching infrastructure, giving dYdX a sovereign "own-the-full-stack" architecture (matching, settlement, fee capture) rather than renting blockspace.
- **USDC collateral** — perps are margined and settled in USDC; DYDX is the staking/governance asset, not the quote or margin asset.
- **dYdX Unlimited** — a major upgrade adding instant/permissionless market listings, the **MegaVault** liquidity engine (pooled USDC backstopping new markets), and revamped trading-rewards programs.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~844.08M DYDX |
| **Total Supply** | ~958.34M DYDX |
| **Max Supply** | 1.00B DYDX |
| **Market Cap / FDV** | ~0.84 (circ / max-supply basis) |

The token migrated from an Ethereum ERC-20 (ethDYDX) to the native dYdX Chain token, where it secures the proof-of-stake chain. Stakers and validators earn a share of **protocol trading fees paid in USDC**, making DYDX one of the few governance tokens with a direct, fee-driven cash-flow link rather than pure emissions. Roughly **84% of max supply is already circulating** (MC/FDV ~0.84), so future dilution pressure is comparatively modest versus newer perp-DEX tokens such as [[lighter|Lighter]] (~25% float).

---

## Market Structure & Derivatives

**Spot venues (CEX):** DYDX trades on major centralized exchanges including Binance, KuCoin, and others, predominantly against USDT.

**The protocol's own venue:** dYdX itself is a perp DEX — DYDX is the governance/staking asset, *not* a quote or margin asset on the platform (perps are collateralized in USDC). dYdX Chain runs an on-chain order book matched by validators, which differentiates it from AMM-based DEXs: it offers limit orders, tight spreads on liquid pairs, and a maker/taker fee schedule closer to a CEX. The MegaVault liquidity engine and trading-rewards programs route protocol economics back toward DYDX stakers.

**Derivatives on DYDX itself:** DYDX is listed as a perpetual on [[hyperliquid|Hyperliquid]] (DYDX-PERP) and other perp venues. As a low-rank, lower-liquidity token, its perp [[funding-rate|funding rate]] and open interest tend to be volatile — funding can swing sharply when speculative flows concentrate, and thin spot liquidity makes the perp prone to liquidation cascades during fast moves. Traders watch funding/OI here as a sentiment gauge given the small spot float.

---

## Use Case / Narrative / Category

dYdX is positioned as "DeFi's pro trading platform" — a category leader in **decentralized perpetual futures**. Historically it was the highest-volume perp DEX before the rise of competitors like [[hyperliquid|Hyperliquid]], [[lighter|Lighter]], and GMX. Its narrative now centers on the **app-chain thesis**: owning the full stack (matching, settlement, fee capture) on a sovereign Cosmos chain rather than renting blockspace. The investment case is essentially a bet on decentralized derivatives volume migrating on-chain and DYDX stakers capturing a slice of that fee flow. It is a core reference point in the [[perp-dex-aggregation|perp-DEX]] landscape.

---

## Valuation Framing (qualitative)

DYDX is unusual among governance tokens in having a **real, USDC-denominated fee link** to stakers, so a valuation case can be built on protocol trading fees rather than pure narrative. At a ~$101M cap with ~84% float, the unlock overhang is modest. The bear case is *displacement*: once the dominant perp DEX, dYdX has ceded volume share to Hyperliquid, which compresses the fee stream that justifies the token. The ~97% drawdown from its 2021 ATH prices in years of lost dominance; re-rating depends on dYdX Unlimited / MegaVault recapturing volume rather than on macro alone.

---

## Peer Comparison

| Token | Architecture | MC Rank | Market Cap | MC/FDV | Edge |
|---|---|---|---|---|---|
| **dYdX (DYDX)** | Cosmos appchain, on-chain CLOB | #268 | ~$101M | ~0.84 | Sovereign full-stack; USDC fee link |
| [[hyperliquid\|Hyperliquid (HYPE)]] | Own L1, on-chain order book | top-tier | multi-$B | high | Volume leader; deep liquidity |
| [[lighter\|Lighter (LIT)]] | ZK-rollup, verifiable matching | #120 | ~$382M | ~0.25 | Provable fair execution; low float |
| GMX | Oracle/AMM perps (Arbitrum) | mid-cap | $100Ms | high | Pool-backed, no order book |

---

## Notable History

- **2017–2018:** Founded by Antonio Juliano; early DeFi margin/derivatives pioneer.
- **2021:** Launched perpetuals on an Ethereum StarkEx L2; became the dominant perp DEX by volume; DYDX ATH ~$4.52.
- **2023–2024:** Migrated from the Ethereum L2 to the standalone **dYdX Chain** ([[cosmos|Cosmos]] SDK) with an on-chain order book and validator-run matching.
- **dYdX Unlimited** introduced instant market listings, the MegaVault liquidity engine, revamped trading rewards, and permissionless market creation.

---

## Risks

- **Competitive displacement:** Hyperliquid and other newer perp DEXs have eroded dYdX's once-dominant volume share — a structural risk to fee capture.
- **Token-value capture:** Governance/staking tokens often struggle to accrue value even when the underlying protocol generates fees; DYDX has traded down >97% from its ATH.
- **Liquidity / bear-market risk:** Low rank (#268), thin spot volume, and the current Established Bear Market / extreme-fear backdrop amplify downside volatility and slippage.
- **App-chain risk:** A sovereign chain must bootstrap and retain its own validator security and liquidity, unlike protocols that inherit Ethereum security.
- **Regulatory risk:** Decentralized perps with high leverage are an obvious target for derivatives regulators.

---

## Related

- [[crypto-markets]]
- [[hyperliquid]]
- [[lighter]]
- [[perpetual-futures]]
- [[perp-dex-aggregation]]
- [[funding-rate]]
- [[decentralized-exchange]]
- [[cosmos]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DYDX |
| **Market Cap Rank** | #255 |
| **Market Cap** | $103.16M |
| **Current Price** | $0.1217 |
| **Categories** | Decentralized Exchange (DEX), Smart Contract Platform, Exchange-based Tokens, Decentralized Finance (DeFi), Perpetuals, Layer 1 (L1), Appchains, Made in USA (+1 more) |
| **Website** | [https://dydx.trade](https://dydx.trade) |

---

## Overview

dYdX is DeFi’s pro trading platform and a pioneer in decentralized finance, known for being the first to offer decentralized margin trading and derivatives, as well as inventing flash loans and DEX aggregators in 2018. Built on a custom Layer-1 blockchain using the Cosmos SDK, dYdX provides a professional-grade, decentralized trading experience with high leverage, deep liquidity, and low fees. Governed by the community through the DYDX token, dYdX is focused on delivering a transparent and user-driven financial system. This November, dYdX Unlimited launches, bringing instant market listings, the MegaVault liquidity engine, revamped trading rewards, and lifetime affiliate commissions, setting a new standard for decentralized trading

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 848.61M DYDX |
| **Total Supply** | 958.34M DYDX |
| **Max Supply** | 1.00B DYDX |
| **Fully Diluted Valuation** | $116.50M |
| **Market Cap / FDV Ratio** | 0.89 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.52 (2024-03-07) |
| **Current vs ATH** | -97.30% |
| **All-Time Low** | $0.0788 (2026-03-08) |
| **Current vs ATL** | +54.56% |
| **24h Change** | +0.96% |
| **7d Change** | -9.50% |
| **30d Change** | -0.72% |
| **1y Change** | -80.95% |

---

## Platform & Chain Information

**Native Chain:** Cosmos

### Contract Addresses

| Chain | Address |
|---|---|
| Cosmos | `ibc/831F0B1BBB1D08A2B75311892876D71565478C532967545476DF4C2D7492E48C` |
| Osmosis | `ibc/831F0B1BBB1D08A2B75311892876D71565478C532967545476DF4C2D7492E48C` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DYDX/USDT | N/A |
| KuCoin | DYDX/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://dydx.trade](https://dydx.trade) |
| **Twitter** | [@dydxfoundation](https://twitter.com/dydxfoundation) |
| **Discord** | [https://discord.com/invite/dydx](https://discord.com/invite/dydx) |
| **GitHub** | [https://github.com/dydxprotocol](https://github.com/dydxprotocol) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.71M |
| **Market Cap Rank** | #255 |
| **24h Range** | $0.1191 — $0.1231 |
| **CoinGecko Sentiment** | 80% positive |
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
