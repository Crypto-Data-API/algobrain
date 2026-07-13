---
title: "Mezo USD"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, stablecoin, bitcoin]
aliases: ["MUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.mezo.org"
related: ["[[crypto-markets]]", "[[bitcoin]]", "[[stablecoin]]", "[[collateralization]]", "[[cdp]]", "[[depeg]]", "[[liquity-usd]]"]
---

# Mezo USD

**Mezo USD** (ticker **MUSD**) is the [[bitcoin]]-collateralized [[stablecoin]] of **Mezo**, a Bitcoin-centric economy/network. MUSD is minted when users deposit BTC as collateral and borrow against it at low, fixed rates, using a **collateralized debt position** ([[cdp]]) model: each MUSD is backed by over-collateralized BTC and can be redeemed against the system, helping it hold a 1:1 soft peg to the US dollar. MUSD is native to **Mezo** and bridged to [[ethereum|Ethereum]] and **Base**. It ranks **#658** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At the latest snapshot MUSD traded at **$0.99817** (market cap **$28,734,792**, rank **#658**), up **0.05% over 24h** and **0.04% over 7d**. A price of **~$1.00 is on-peg** — MUSD trades in a tight band around a dollar, as expected for an over-collateralized CDP stablecoin (Fear & Greed Index at 22 / Extreme Fear, [[bitcoin]] around $64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MUSD |
| **Market Cap Rank** | #658 |
| **Market Cap** | $28,734,792 |
| **Current Price** | $0.99817 (on-peg) |
| **24h Change** | +0.05% |
| **7d Change** | +0.04% |
| **Categories** | Stablecoins, USD Stablecoin, Bitcoin-backed, Ethereum Ecosystem, Base Ecosystem, Mezo Ecosystem |
| **Website** | [https://www.mezo.org](https://www.mezo.org) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

MUSD is Mezo's [[bitcoin]]-backed [[stablecoin]], minted when users deposit BTC as collateral and borrow against it at low, fixed rates. The system uses a **collateralized debt position** ([[cdp]]) model, where each MUSD is backed by over-collateralized BTC and can be redeemed against the system, helping MUSD maintain its 1:1 soft peg to USD.

**Mezo** positions itself as a Bitcoin-economy network — infrastructure designed to make BTC productive (borrowing, payments, yield) without selling it. MUSD is the unit of account that lets BTC holders unlock dollar liquidity against their coins, which is the core use case the network is built around.

## Architecture — Bitcoin-Backed CDP Pipeline

MUSD is produced by an over-collateralized borrowing system in the [[liquity-usd|Liquity]] lineage, but with **BTC** as the collateral asset rather than ETH:

1. **Deposit BTC collateral.** A user locks BTC into the protocol on Mezo.
2. **Borrow MUSD.** Against that collateral, the user mints/borrows MUSD at **low, fixed rates**, up to a high loan-to-value (the design allows roughly ~90% LTV for individual borrowers), while the **system as a whole stays over-collateralized**.
3. **Maintain the collateral ratio.** Each position must stay above a minimum collateral ratio; the system minimum is >110%, with a typical individual user expected to sit well above ~150% to leave a safety buffer against BTC volatility.
4. **Liquidate undercollateralized positions.** If a position falls below the minimum ratio, it is automatically liquidated — collateral is seized/sold to cover the debt — keeping aggregate MUSD fully backed even as individual borrowers are wound down.
5. **Redeem / arbitrage to par.** MUSD can be redeemed or unwound against the system; this redemption pressure pulls the price back toward $1 when it drifts.

Because the collateral is volatile [[bitcoin]], the **over-collateralization buffer and the liquidation engine — not a fiat reserve — are what keep MUSD fully backed**. See [[collateralization]].

## Peg-Maintenance & Liquidations

- **Over-collateralized minting.** New MUSD is created only against BTC collateral above the minimum ratio, so each unit enters circulation backed by more than $1 of BTC.
- **Liquidations.** Positions that fall below the minimum collateral ratio are automatically liquidated, with collateral seized/sold to cover the debt, keeping aggregate MUSD fully backed even as individual borrowers are wound down.
- **Redemptions / arbitrage.** The ability to redeem or unwind against the system provides the economic pressure that pulls MUSD back toward $1 when it drifts, which is why ~$1.00 is the normal, on-peg state.

---

## Value Accrual / Governance

MUSD is the **stablecoin/liability** side of the system, not a governance token — it does not capture protocol fees or carry voting rights; its job is to hold $1. Value accrues to the **Mezo ecosystem** through borrowing demand: interest paid by BTC borrowers and the utility of dollar liquidity drive system revenue, while MUSD itself remains a pass-through dollar unit. (Mezo's broader network token and incentive design sit outside MUSD; MUSD holders are exposed to peg stability and system solvency, not to upside in the protocol.)

---

## Comparison vs Other Collateralized Stablecoins

MUSD belongs to the **over-collateralized CDP stablecoin** family. Its distinguishing trait is using BTC (rather than ETH or a basket) as collateral, on a Bitcoin-native network.

| Token | Collateral | Model | Distinguishing trait |
|---|---|---|---|
| **MUSD** (Mezo) | BTC | Over-collateralized CDP, low fixed rate | Bitcoin-native; lets BTC holders mint dollars without selling |
| **[[liquity-usd|LUSD]]** (Liquity) | ETH | Over-collateralized CDP, one-time fee, 110% min | The canonical immutable, governance-minimized ETH-CDP stablecoin MUSD's design echoes |
| **[[dai|DAI]]** (Sky/MakerDAO) | Multi-collateral (incl. RWA, USDC) | Over-collateralized CDP + stability module | Largest decentralized stablecoin; broad collateral basket including off-chain assets |
| **[[crvusd|crvUSD]]** (Curve) | ETH/BTC/LSTs | LLAMMA soft-liquidation CDP | Continuous "soft" liquidation to smooth collateral drawdowns |

MUSD's edge is the **Bitcoin thesis** — it serves the large pool of BTC holders who want dollar liquidity or leverage against their coins without leaving the Bitcoin ecosystem. Its trade-off is the same as all crypto-collateral stablecoins: backing is volatile, so solvency depends on liquidations keeping up with price moves.

---

## How & Where It Trades / Where It's Used

- **Mint / redeem.** The primary path is the Mezo protocol itself — deposit BTC, borrow MUSD, repay to unlock collateral. This is also the main peg-restoring channel.
- **Secondary trading.** MUSD trades on DEXs, notably **Uniswap V3 (Ethereum)** against USDC, and on Base. Liquidity is modest given the ~$29M cap.
- **Use cases.** Dollar liquidity against BTC collateral, leverage on BTC (borrow MUSD, buy more BTC), and a dollar unit of account within the Mezo economy for payments and DeFi.

---

## Narrative, Category & Catalysts

MUSD sits at the intersection of two themes: **Bitcoin-DeFi / "productive BTC"** and **decentralized stablecoins**. Catalysts:

- **Mezo network growth.** More BTC deposited and more borrowing demand expands MUSD float and deepens liquidity.
- **BitcoinFi narrative.** Rising interest in making BTC productive (BTC L2s, restaking, BTC-backed credit) is a tailwind for BTC-collateralized stablecoins.
- **Rate environment.** Low, fixed borrowing rates are attractive when alternative dollar funding is expensive; the value proposition strengthens vs higher-cost borrowing elsewhere.
- **Regime caveat.** In an **Established Bear Market** with BTC ~16% below its 200-day MA (2026-06-22), BTC-collateralized systems face elevated liquidation risk — a headwind for aggressive borrowing, though on-peg behavior has held in the snapshot.

---

## History / Timeline

- **2025-10-08** — MUSD records its all-time high of **$1.05** (a brief minor depeg above par).
- **2025-11-04** — MUSD records its all-time low of **$0.9635** (a brief minor depeg below par).

*(MUSD is a stablecoin; these extremes are short off-peg episodes, not directional moves. No further dated protocol events are confirmed in the wiki source.)*

---

## Risks

- **Collateral (BTC) volatility.** Backing is volatile [[bitcoin]]; a sharp BTC drawdown can push positions into mass liquidation, the dominant solvency risk for any over-collateralized CDP stablecoin. This is especially pertinent in the current bear regime.
- **Depeg risk.** Minor depegs have occurred (ATL ~$0.96, ATH ~$1.05); during liquidity stress or BTC crashes MUSD can trade off-peg (see [[depeg]]).
- **Liquidation / oracle risk.** The system depends on timely liquidations and a reliable BTC price oracle; oracle failure or a fast crash that outruns liquidations can leave the system under-collateralized.
- **Reserve-counterparty / bridge risk.** MUSD is bridged to Ethereum and Base; bridge security and cross-chain representation add exposure beyond the core CDP.
- **New-protocol / ecosystem risk.** Mezo is a relatively young Bitcoin-economy network; smart-contract, bridge, and adoption risks apply, and TVL/usage can be incentive-driven.
- **Liquidity / size.** At roughly $29M market cap, MUSD is a small stablecoin with thinner secondary-market liquidity than fiat-backed majors.

---

## Trading / Usage Playbook

- **As BTC-backed dollar liquidity:** Borrow MUSD against BTC to access dollars without selling; keep the collateral ratio well above the minimum (toward ~200%+) in a bear regime to survive BTC drawdowns.
- **For leverage:** Borrow MUSD and buy more BTC for leveraged long exposure — high risk in the current Extreme-Fear, sub-200-day-MA environment.
- **Peg monitoring:** Watch for sustained deviation from $1, system collateralization ratio, and BTC price velocity (fast crashes are the liquidation-stress trigger).
- **Execution:** Prefer protocol mint/redeem for size; DEX pools are modest and can slip.

*This is not investment advice; figures above are point-in-time market data, not a valuation.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.92M MUSD |
| **Total Supply** | 18.92M MUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $18.92M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.05 (2025-10-08) |
| **All-Time Low** | $0.9635 (2025-11-04) |
| **Current Price** | $0.99817 (on-peg) |
| **24h Change** | +0.05% |
| **7d Change** | +0.04% |

*As a [[stablecoin]], MUSD's price history is a tight band around $1; the ATH/ATL above represent brief minor depeg episodes, not directional moves.*

---

## Platform & Chain Information

**Native Chain:** Mezo

### Contract Addresses

| Chain | Address |
|---|---|
| Mezo | `0xdd468a1ddc392dcdbef6db6e34e89aa338f9f186` |
| Ethereum | `0xdd468a1ddc392dcdbef6db6e34e89aa338f9f186` |
| Base | `0xdd468a1ddc392dcdbef6db6e34e89aa338f9f186` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48/0XDD468A1DDC392DCDBEF6DB6E34E89AA338F9F186 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.mezo.org](https://www.mezo.org) |
| **Twitter** | [@mezonetwork](https://twitter.com/mezonetwork) |
| **Telegram** | [mezonetwork](https://t.me/mezonetwork) (4,184 members) |
| **Discord** | [https://discord.com/invite/mezo](https://discord.com/invite/mezo) |
| **GitHub** | [https://github.com/mezo-org/musd](https://github.com/mezo-org/musd) |
| **Whitepaper** | [https://mezo.org/docs/users/musd](https://mezo.org/docs/users/musd) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 16 |
| **GitHub Forks** | 13 |
| **Pull Requests Merged** | 217 |
| **Contributors** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.99817 (on-peg) |
| **Market Cap** | $28,734,792 |
| **Market Cap Rank** | #658 |
| **24h Change** | +0.05% |
| **7d Change** | +0.04% |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[bitcoin]]
- [[stablecoin]]
- [[collateralization]]
- [[cdp]]
- [[depeg]]
- [[liquity-usd]]
- [[dai]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
