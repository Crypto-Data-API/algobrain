---
title: "Resupply USD"
type: market
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["REUSD", "Resupply USD", "reUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://resupply.fi/"
related: ["[[collateralization]]", "[[crypto-markets]]", "[[curve]]", "[[dai]]", "[[defi]]", "[[dola-usd]]", "[[ethereum]]", "[[stablecoin]]", "[[usdc]]"]
---

# Resupply USD

**Resupply USD** (ticker **REUSD / reUSD**) is a decentralized, **crypto-collateralized [[stablecoin]]** soft-pegged to the U.S. dollar on [[ethereum|Ethereum]], issued by the **Resupply** [[defi|DeFi]] protocol within the [[curve|Curve]] / Frax ecosystem. Its distinguishing feature is the *type* of collateral: rather than fiat or raw volatile crypto, REUSD is minted against **interest-bearing lending-market deposits** — receipt tokens from venues such as [[curve|Curve Lend]] and Fraxlend that are *already* earning yield. It is a [[collateralization|collateralized-debt-position]] (CDP) stablecoin layered on top of money markets: a "stablecoin of yield-bearing stablecoin positions."

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, REUSD trades at **$0.996253**, holds market-cap rank **#606**, and carries a market capitalization of **$32,792,642** (**24h −0.20%**, **7d −0.24%**). The slight discount to $1 is normal for a crypto-backed soft-peg stablecoin and was unremarkable against the risk-off backdrop (Fear & Greed 21, Extreme Fear; [[bitcoin|BTC]] ~$64,568).

> *Informational only, not investment advice. Crypto-collateralized soft-peg stablecoins can deviate from $1 under stress.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | REUSD (reUSD) |
| **Price (2026-06-21)** | $0.996253 |
| **Market Cap Rank** | #606 |
| **Market Cap** | $32,792,642 |
| **24h Change** | −0.20% |
| **7d Change** | −0.24% |
| **Peg target** | Soft peg, 1 REUSD ≈ 1 USD |
| **Backing model** | Crypto / debt-backed (CDP against lending-market deposits) |
| **Issuer** | Resupply (decentralized protocol) |
| **Native chain** | [[ethereum\|Ethereum]] |
| **Website** | [https://resupply.fi/](https://resupply.fi/) |

---

## Architecture — How It Works

Resupply is a decentralized protocol (associated with the [[curve|Curve]] / Frax DeFi ecosystem) that issues REUSD as **collateralized debt against yield-bearing collateral**. The mechanism stacks two layers of money-market exposure:

1. **Underlying deposit (layer 1).** A user supplies a stablecoin (e.g. [[usdc|USDC]] or another dollar token) into a partner **lending market** — [[curve|Curve Lend]] or Fraxlend — and receives an interest-bearing receipt token representing that deposit plus accruing interest.
2. **Mint against the receipt (layer 2).** Those yield-bearing positions are posted as **collateral** in Resupply to mint REUSD. Because the collateral is itself a dollar-denominated, interest-earning claim, the system can run at a high loan-to-value while still being economically over-collateralized.
3. **Borrow-rate design.** Terms are set so the REUSD borrow rate tracks roughly **the greater of: half the lending rate earned, half the risk-free rate, or 2%** — engineered so the collateral generally out-earns the cost of the REUSD debt, giving borrowers a positive carry to mint and hold the position.

### Peg & stability mechanism

REUSD is a **soft peg**, not a fiat-redemption dollar. It is defended by:

- **Over-collateralization** — debt is backed by more than $1 of yield-bearing deposit value per REUSD.
- **Liquidation** — unhealthy positions are liquidated to retire REUSD debt and protect solvency.
- **Arbitrage in REUSD liquidity pools** — minting/selling above peg and buying/repaying below peg pull the price back toward $1.

There is no 1:1 cash redemption, so the secondary price floats in a narrow band around $1 (current $0.9963) and can show visible discounts when DEX liquidity is thin.

### Emissions & incentives

Protocol **emissions** are directed at three groups — an **insurance pool** (backstop), **voting incentives** (to direct liquidity/governance), and **borrowers** (with borrower emissions scaling to the protocol revenue each borrower generates). This ties reward distribution to fee production rather than flat farming.

See [[collateralization]] and [[cdp]] for the general CDP framework.

---

## Tokenomics & Supply

REUSD supply is **demand-driven**: it expands as users mint against lending-market collateral and contracts on repayment/liquidation, with circulating REUSD always over-collateralized by the deposited positions. At a ~$33M cap it is a small, on-chain-native stablecoin. The protocol layers a separate emissions/governance token economy (insurance pool, vote incentives, borrower rewards) on top of the stablecoin itself; REUSD is the debt instrument, not the value-accrual token.

---

## Comparison vs Peer CDP / DeFi Stablecoins

| Stablecoin | Collateral type | Peg model | Distinguishing trait | Key risk |
|---|---|---|---|---|
| **REUSD** (this page) | Yield-bearing lending-market deposits (Curve Lend / Fraxlend receipts) | Soft peg, over-collateralized CDP | Collateral already earns yield; positive borrow carry | Layered dependency on underlying lending markets |
| **[[dai]] (DAI/USDS)** | Multi-collateral (crypto + RWA) | Over-collateralized CDP, soft peg | Largest decentralized CDP stable; deep liquidity | Collateral & governance complexity |
| **[[dola-usd]] (DOLA)** | Crypto via Inverse Finance FiRM | Over-collateralized, soft peg | Comparable DeFi-native CDP; *exploit history* | Smart-contract / exploit precedent |
| **[[frax-usd]] (Frax)** | Mixed / RWA-backed reserves | Hybrid, near-hard peg | Frax-ecosystem reserve dollar | Reserve & protocol governance |

REUSD's nearest design analogs are [[dai|DAI]] and [[dola-usd|DOLA]] (over-collateralized CDP soft-pegs). What sets it apart is that its collateral is **itself yield-bearing dollar debt** rather than raw ETH/crypto — boosting capital efficiency but adding a dependency layer that DAI's direct crypto collateral does not have.

---

## How & Where It Trades / Is Used

REUSD liquidity is concentrated in **[[defi|DeFi]] venues on [[ethereum|Ethereum]]**, primarily **[[curve|Curve]] pools** pairing REUSD with other stablecoins — consistent with its Curve/Frax-ecosystem origins. Centralized-exchange listings are limited. Composability runs through the same ecosystem: REUSD can be deployed in Curve pools, used as a borrowable/loopable dollar, and farmed via emissions. With a ~$33M cap it is a small-cap, on-chain-native stablecoin whose holders are predominantly DeFi participants running the mint-and-carry trade rather than spot traders.

---

## Narrative, Category & Catalysts

- **Category:** DeFi-native, yield-collateralized CDP stablecoin in the Curve/Frax orbit.
- **Bull catalysts:** rising lending-market yields (widening the positive carry that makes minting attractive); Curve/Frax ecosystem growth; deeper REUSD Curve liquidity tightening the peg; emissions directed to borrowers/LPs bootstrapping adoption.
- **Bear catalysts:** compression of underlying lending yields (erodes the borrow-carry incentive); stress or exploit in an underlying lending market propagating into REUSD collateral; thin DEX liquidity widening the discount; emissions slowing.

---

## History / Timeline

| Date | Event |
|---|---|
| (early trading) | Brief prints above $1 during thin-liquidity launch; stress-print low near **$0.96**. |
| 2026-06-21 | Trades $0.996253, rank #606, ~$32.8M cap; flat ~7d, small normal discount. |

*Only events with on-page provenance are listed. No confirmed reserve-driven depeg is recorded; the ~$0.96 low was a thin-liquidity stress print, not a documented collateral failure.*

---

## Risks

- **Collateral-chain / dependency risk** — REUSD's backing is itself exposed to the solvency and peg of the underlying deposit stablecoins and to the health of [[curve|Curve Lend]] / Fraxlend. A problem in any layer propagates upward — the central, structural risk of a stablecoin-of-stablecoin-positions.
- **Smart-contract risk** — Multiple interacting protocols (Resupply + the lending markets) enlarge the attack surface. DeFi CDP stablecoins from this ecosystem have an exploit history — see [[dola-usd|DOLA]] for a comparable cautionary case.
- **Soft-peg / liquidity risk** — No fiat redemption at par; the peg relies on DEX liquidity and the collateralization ratio, so thin liquidity can produce visible discounts like the current $0.9963.
- **Yield-mechanism risk** — The borrow-rate formula and emissions schedule depend on continued lending-market yields; compression of those yields weakens the incentive to mint and hold REUSD.
- **Redemption-gating risk** — There is no on-demand 1:1 cash redemption; exit is via liquidation/repayment of CDPs or secondary DEX sales, which can be costly in stress.
- **Governance risk** — Parameter and emissions decisions (collateral types, rates, insurance-pool sizing) directly affect peg stability.
- **Regulatory risk** — Evolving stablecoin rules may affect DeFi-native dollar issuance.

See [[stablecoin]], [[depeg]], and [[collateralization]] for the general framework.

---

## Trading / Usage Playbook

- **Core trade:** the REUSD position is a *carry trade* — supply a dollar token into Curve Lend/Fraxlend, mint REUSD against the receipt, and capture the spread between collateral yield and the (capped) REUSD borrow rate, optionally amplified by emissions. The edge lives or dies on lending-market yields staying above the borrow rate.
- **What to watch:** underlying Curve Lend / Fraxlend utilization and rates; the REUSD/USDC Curve pool peg and depth; emissions cadence; any exploit or peg stress in adjacent ecosystem protocols.
- **Risk-off framing:** in Extreme Fear, the layered-dependency design is least forgiving — a single underlying-market wobble can hit collateral value and the peg together, so size the carry for the worst link in the chain, not the average.

---

## Related

- [[stablecoin]]
- [[defi]]
- [[collateralization]]
- [[cdp]]
- [[curve]]
- [[dola-usd]]
- [[dai]]
- [[depeg]]
- [[usdc]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge (Resupply CDP-on-lending-markets mechanism, Curve Lend / Fraxlend collateral); no specific wiki source ingested yet.

## Overview

A decentralized stablecoin backed by Collateralized Debt Positions (CDP), leveraging the liquidity and stability of lending markets.

The Resupply stablecoin is backed by other stablecoins that are earning interest on other lending markets.

Designed to maximize yield returns by having the borrow rate always be half the lending rate being earned, half the risk-free rate, or two percent, whichever is greater.

Emissions are designed for long-term sustainability by directing at three groups: the insurance pool, voting incentives, and directly at borrowers.

The revenue that borrowers generate will directly correlate with the emissions directed towards them. The more revenue a borrower generates for Resupply, the greater the share of emissions it will receive.

Targeted platforms for launch are Curve Lend and Fraxlend.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 32.00M REUSD |
| **Total Supply** | 32.00M REUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $31.87M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.18 (2025-09-15) |
| **Current vs ATH** | -15.80% |
| **All-Time Low** | $0.9595 (2026-02-06) |
| **Current vs ATL** | +3.99% |
| **24h Change** | -0.44% |
| **7d Change** | -0.29% |
| **30d Change** | -0.32% |
| **1y Change** | +0.53% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x57ab1e0003f623289cd798b1824be09a793e4bec` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://resupply.fi/](https://resupply.fi/) |
| **Twitter** | [@ResupplyFi](https://twitter.com/ResupplyFi) |
| **Discord** | [https://discord.gg/resupplyfi](https://discord.gg/resupplyfi) |
| **Whitepaper** | [https://docs.resupply.fi/](https://docs.resupply.fi/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1,284.25 |
| **Market Cap Rank** | #613 |
| **24h Range** | $0.9861 — $1.00 |
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
