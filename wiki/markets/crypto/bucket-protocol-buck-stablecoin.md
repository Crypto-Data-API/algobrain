---
title: "Bucket Protocol BUCK Stablecoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["BUCK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bucketprotocol.io/"
related: ["[[cdp]]", "[[collateralization]]", "[[crypto-markets]]", "[[depeg]]", "[[liquidation]]", "[[stablecoin]]", "[[sui]]"]
---

# Bucket Protocol BUCK Stablecoin

**BUCK** is the over-collateralized [[stablecoin]] of **Bucket Protocol**, a **collateralized debt position** ([[cdp]]) protocol on the [[sui]] blockchain. Bucket supports multiple assets as collateral — including SUI, BTC, ETH, and liquid-staking tokens (LSTs) — and BUCK is minted when users lock that collateral. Unlike the RWA dollars in this cluster (USDO, FIDD, USDY), BUCK is **crypto-collateralized**, not backed by off-chain Treasuries or cash; its "real-world asset" is none — it is a decentralized, on-chain dollar. It targets a 1:1 soft peg to the US dollar and ranks **#703** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At the latest snapshot BUCK traded at **$0.99898** (market cap **$25,907,941**, rank **#703**), down **0.04% over 24h** and up **0.10% over 7d**. A price of **~$1.00 is on-peg** — BUCK trades in a tight band around a dollar, as expected for an over-collateralized CDP stablecoin (Fear & Greed Index at 22 / Extreme Fear, [[bitcoin]] around $64,180 at the snapshot).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BUCK |
| **Peg** | 1 BUCK ≈ 1 USD (soft peg) |
| **Type** | Over-collateralized crypto-backed CDP stablecoin |
| **Chain** | Sui |
| **Collateral** | SUI, BTC, ETH, liquid-staking tokens (LSTs) |
| **Market Cap Rank** | #703 |
| **Market Cap** | $25,907,941 |
| **Current Price** | $0.99898 (on-peg) |
| **24h Change** | -0.04% |
| **7d Change** | +0.10% |
| **Categories** | Stablecoins, Sui Ecosystem, Crypto-backed Stablecoin |
| **Website** | [https://bucketprotocol.io/](https://bucketprotocol.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Bucket Protocol is a **collateralized debt position** ([[cdp]]) protocol on the [[sui]] network, supporting multiple assets as collateral — including SUI, BTC, ETH, and liquid-staking tokens (LSTs). **BUCK** is the over-collateralized [[stablecoin]] minted when users deposit and lock that collateral. The design lineage is the Liquity/MakerDAO family of decentralized, crypto-backed dollars: no fiat reserve, no off-chain custodian — solvency is enforced entirely on-chain by over-collateralization and a liquidation engine.

---

## Architecture — How It Works

### Collateral model — over-collateralized, crypto-backed
BUCK is **over-collateralized**: every unit is backed by more than $1 of crypto collateral locked in the protocol. Multi-asset collateral (SUI, BTC, ETH, LSTs) gives borrowers flexibility but also exposes the system to the volatility and liquidity profile of each accepted asset. As with all crypto-backed CDP stablecoins, the over-collateralization buffer plus the liquidation engine — **not** a fiat reserve — are what keep BUCK fully backed. See [[collateralization]].

### Peg mechanism
- **Over-collateralized minting.** BUCK can only be minted against collateral above the protocol's minimum ratio, so each unit enters circulation backed by surplus value.
- **Redemption / arbitrage pressure.** When BUCK drifts below $1, arbitrageurs can acquire it cheaply and redeem/unwind against collateral; when it drifts above, minting and selling expands supply — both forces pull BUCK back toward its $1 target, which is why ~$1.00 is the normal, on-peg state.

### Liquidations
Positions that fall below the minimum collateral ratio are **liquidated**, with collateral used to repay the outstanding BUCK debt, preserving aggregate backing. Bucket has historically used a **stability-pool-style** mechanism plus tank/redemption flows to absorb liquidations and arbitrage the peg — depositors to the pool earn liquidation proceeds, and the pool provides instant liquidity to retire under-collateralized debt. See [[liquidation]].

### No external/RWA dependency
There is no off-chain custodian or Treasury reserve. The trade-off versus RWA dollars: BUCK avoids issuer/custody counterparty risk but inherits full crypto-collateral volatility and oracle dependence.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 26.13M BUCK |
| **Total Supply** | 26.13M BUCK |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $26.11M |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **demand-driven**: BUCK is minted on collateral deposit and burned on debt repayment, so circulating supply equals outstanding CDP debt. There is no pre-mine or emission schedule for the stablecoin itself (a separate protocol/governance token typically handles incentives in this design family).

---

## Comparison vs Peers

| Stablecoin | Chain | Backing | Type | Notes |
|---|---|---|---|---|
| **BUCK** (Bucket) | Sui | Crypto (SUI/BTC/ETH/LSTs) | Over-collateralized CDP | Multi-collateral, Sui-native |
| **LUSD** (Liquity) | Ethereum | ETH only | Over-collateralized CDP | Min 110% ratio; design ancestor |
| **DAI** (MakerDAO/Sky) | Ethereum | Crypto + RWA mix | Over-collateralized CDP | Largest decentralized stablecoin |
| **USDO** ([[openeden-open-dollar]]) | Eth/Base | US T-bills (off-chain) | RWA-backed (rebasing) | Off-chain reserve, yield-bearing |

BUCK's closest design ancestors are **LUSD** and **DAI** — on-chain, over-collateralized, liquidation-secured dollars. It differs by living on **Sui** and accepting a broader multi-asset collateral set (including BTC and LSTs). Against RWA dollars (USDO/FIDD), BUCK trades issuer/custody risk for crypto-collateral volatility and oracle risk.

---

## How & Where It Trades / Is Used

- **Minting:** open over-collateralized minting on Bucket Protocol against SUI/BTC/ETH/LST collateral.
- **Secondary market:** primarily Sui-native DEX liquidity; CoinGecko shows no major centralized-exchange listings. At ~$26M cap it is a small stablecoin with thin secondary-market depth.
- **Composability:** as a Sui-native $1 unit, BUCK is used across the Sui DeFi stack (DEX pairs, lending, yield) as a stable settlement leg.
- **Stability pool:** users can deposit BUCK to the stability pool to backstop liquidations and earn liquidation rewards.

---

## Narrative / Category & Catalysts

BUCK is a play on **Sui-ecosystem DeFi** and the **decentralized stablecoin** category. Drivers:
- **Sui adoption:** BUCK's addressable market grows with overall Sui DeFi TVL and activity.
- **Multi-collateral expansion:** adding BTC/LST collateral broadens minting demand but raises risk-management complexity.
- **Decentralization premium:** in regimes where users distrust centralized/off-chain dollars, on-chain over-collateralized stablecoins gain appeal.
- **Regime context:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market. Bear markets stress crypto-collateralized stablecoins most — falling collateral prices drive liquidations and can pressure the peg, the opposite of how RWA dollars behave.

---

## History / Timeline

| Date | Event |
|---|---|
| 2024-09-22 | All-time-low print of $0.000978 (a brief illiquid/erroneous print, not a sustained de-peg) |
| 2025-10-10 | All-time-high print of $1.23 (brief illiquid print) |
| 2026-04-09 | Captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $0.99898 (on-peg), market cap ~$25.91M (rank #703) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.23 (2025-10-10) |
| **All-Time Low** | $0.00097800 (2024-09-22) |
| **Current Price** | $0.99898 (on-peg) |
| **24h Change** | -0.04% |
| **7d Change** | +0.10% |

*As a [[stablecoin]], BUCK's price history is a tight band around $1; the extreme ATH/ATL above reflect brief illiquid prints/depeg episodes, not directional moves.*

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0xce7ff77a83ea0cb6fd39bd8748e2ec89a3f41e8efdc3f4eb123e0ca37b184db2::buck::BUCK` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bucketprotocol.io/](https://bucketprotocol.io/) |
| **Twitter** | [@bucket_protocol](https://twitter.com/bucket_protocol) |
| **Telegram** | [bucketprotocol](https://t.me/bucketprotocol) (1,133 members) |
| **Discord** | [https://discord.com/invite/nYCnNJE6Tr](https://discord.com/invite/nYCnNJE6Tr) |
| **GitHub** | [https://github.com/orgs/Bucket-Protocol](https://github.com/orgs/Bucket-Protocol) |
| **Whitepaper** | [https://github.com/Bucket-Protocol/whitepaper/blob/main/BucketProtocolWhitepaper.pdf](https://github.com/Bucket-Protocol/whitepaper/blob/main/BucketProtocolWhitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.99898 (on-peg) |
| **Market Cap** | $25,907,941 |
| **Market Cap Rank** | #703 |
| **24h Change** | -0.04% |
| **7d Change** | +0.10% |
| **Last Updated** | 2026-06-21 |

---

## Risks

- **Depeg risk.** Like all crypto-backed stablecoins, BUCK can trade off-peg during liquidity stress or collateral crashes (see [[depeg]]); the brief ATL print illustrates how thin liquidity can produce extreme momentary deviations.
- **Multi-collateral volatility.** Backing spans SUI, BTC, ETH, and LSTs; a sharp drop in any major collateral asset (especially the more volatile or less liquid ones) can trigger mass liquidations.
- **Liquidation / oracle risk.** Solvency depends on timely liquidations and reliable price oracles for each collateral type; oracle failure or a fast crash can leave the system under-collateralized.
- **Stability-pool depletion.** If the stability pool is drained during a large liquidation cascade, the protocol must fall back to redistribution mechanisms, raising contagion risk among borrowers.
- **Sui-ecosystem / smart-contract risk.** BUCK lives entirely on [[sui]]; chain-level issues, bridge risk, and protocol smart-contract bugs all apply, and the asset is exposed to overall Sui DeFi adoption.
- **Liquidity / size.** At roughly $26M market cap with limited centralized-exchange listings, BUCK is a small stablecoin with thin secondary-market liquidity.

---

## Trading / Usage Playbook

- **Use as a Sui-native settlement dollar.** BUCK is best used inside the Sui DeFi stack where a decentralized $1 unit is wanted.
- **Mind collateral health in bear regimes.** As a borrower, keep a generous buffer above the minimum ratio — Extreme-Fear regimes are exactly when liquidations cluster.
- **Stability-pool yield = liquidation risk premium.** Depositing BUCK to backstop liquidations earns rewards but means accepting discounted collateral during crashes.
- **Fade small peg deviations cautiously.** Arbitrage pulls BUCK to $1, but thin liquidity means size moves the price; do not assume deep order books.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[sui]]
- [[stablecoin]]
- [[collateralization]]
- [[cdp]]
- [[liquidation]]
- [[depeg]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 25.97M BUCK |
| **Total Supply** | 25.97M BUCK |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $25.98M |
| **Market Cap / FDV Ratio** | 1.00 |

---
