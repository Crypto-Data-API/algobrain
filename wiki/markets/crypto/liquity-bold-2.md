---
title: "BOLD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["BOLD", "BOLD stablecoin", "Liquity BOLD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.liquity.org/"
related: ["[[cdp]]", "[[collateralization]]", "[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[liquid-staking]]", "[[liquity-usd]]", "[[liquity]]", "[[maker]]", "[[stablecoin]]"]
---

# BOLD

**BOLD** is the USD-pegged [[stablecoin]] issued by [[liquity|Liquity]] V2, the second generation of the Liquity decentralized borrowing protocol, on [[ethereum|Ethereum]]. Unlike the protocol's first-generation stablecoin [[liquity-usd|LUSD]] (which charged a fixed one-time borrowing fee), BOLD introduces **user-set interest rates**: each borrower chooses the annual rate they are willing to pay, and the protocol uses those rates to order redemptions, replacing LUSD's fixed-fee model with a market for borrowing cost. BOLD is fully crypto-collateralized and overcollateralized by ETH and liquid-staking tokens, and is distinct from both LUSD (Liquity V1) and the [[liquity|LQTY]] governance/incentive token.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, BOLD trades at **$0.999084** — effectively on its $1.00 peg — ranking **#627** by market capitalization with a market cap of **$31,627,917**. Movement is negligible: **+0.03% over 24h** and **+0.03% over 7 days**, exactly what one expects from a stablecoin holding peg. Notably, BOLD has stayed within a fraction of a cent of $1.00 even amid the prevailing risk-off backdrop (Bitcoin ~$64,508; Fear & Greed Index 21, "Extreme Fear"; long-horizon regime = Established Bear Market), underscoring steady demand for its collateralized model.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BOLD |
| **Market Cap Rank** | #627 |
| **Market Cap** | $31,627,917 |
| **Current Price** | $0.999084 (on-peg) |
| **24h / 7d Change** | +0.03% / +0.03% |
| **Issuer** | Liquity V2 |
| **Peg Mechanism** | Crypto-collateralized, redemption arbitrage |
| **Categories** | Stablecoins, Decentralized Finance (DeFi), USD Stablecoin, Optimism Ecosystem, Base Ecosystem, Crypto-backed Stablecoin |
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |

> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot); price/rank/cap above updated 2026-06-22.*

---

## Overview

BOLD is a fully redeemable USD-pegged stablecoin issued by the [[liquity|Liquity]] V2 protocol. It is minted when users open borrowing positions ("Troves") against ETH and liquid-staking-token collateral — wstETH (Lido) and rETH (Rocket Pool). Loans must maintain a minimum collateral ratio, and the system is backstopped by a Stability Pool holding deposited BOLD plus a redistribution mechanism in which solvent borrowers absorb the debt and collateral of liquidated positions, acting as guarantors of last resort. BOLD is a [[cdp|CDP]]-style (collateralized-debt-position) [[stablecoin]] in the same lineage as MakerDAO's DAI, but with Liquity's signature emphasis on decentralization and minimal governance.

### Architecture — Collateral and backing

BOLD is **fully crypto-backed and overcollateralized** — every BOLD in circulation is matched by more than $1 of ETH/LST collateral locked in Troves. There are no fiat reserves and no off-chain custodians; backing is verifiable on-chain. Liquity V2 separates collateral into distinct "branches" (one per collateral asset), so risk from any single asset is ring-fenced, and each branch has its own Stability Pool. This branched design is the structural upgrade over V1: a problem in one collateral type (e.g. an LST [[depeg|depeg]]) is contained to its branch rather than threatening the whole system.

### Peg-maintenance mechanism

BOLD holds its $1.00 [[collateralization|peg]] through **redemption arbitrage** rather than active intervention:

- **Hard floor (redemptions):** Anyone can redeem BOLD against the protocol for $1.00 of underlying collateral at any time. If BOLD trades below $1.00, arbitrageurs buy cheap BOLD on the open market and redeem it for a full dollar of ETH/LST, pocketing the difference and pushing the price back up. Redemptions hit the Troves paying the **lowest interest rates** first — this is the key V2 innovation, since borrowers effectively bid (via the rate they set) to avoid being redeemed against.
- **Soft ceiling (minting):** If BOLD trades above $1.00, borrowing becomes attractive (you receive a dollar's worth of BOLD for sub-dollar effective cost), so new minting increases supply and pulls the price back toward $1.00.
- **Stability Pool & liquidations:** Under-collateralized Troves are liquidated; the Stability Pool burns BOLD to absorb the bad debt and receives the liquidated collateral at a discount, keeping the system solvent and total backing intact.

The on-peg reading of $0.999084 on 2026-06-22 reflects this machinery functioning normally — a sub-0.1% discount is well within the band where redemption arbitrage operates and is not a [[depeg]] event.

### User-set interest rates — the V2 mechanism

The defining feature of Liquity V2 is the **borrower-set interest rate**:

- Each borrower picks the annual rate they pay on their BOLD debt. Higher rates buy **redemption protection** (you are further back in the redemption queue); lower rates are cheaper but expose you to being redeemed first.
- The protocol thus runs a continuous **market for borrowing cost**, replacing V1's blunt fixed fee. In effect, borrowers self-sort by their willingness to pay for peg stability.
- Interest collected from borrowers is **routed to Stability Pool depositors** (and protocol), giving BOLD holders who deposit in the Stability Pool a real yield — a sharp contrast to LUSD, where holders earned nothing natively.

### How BOLD differs from LUSD

| Dimension | [[liquity-usd|LUSD]] (Liquity V1) | BOLD (Liquity V2) |
|---|---|---|
| Borrowing cost | Fixed one-time fee | User-set annual interest rate |
| Collateral | ETH only | ETH + wstETH + rETH (branches) |
| Redemption ordering | By collateral ratio | By interest rate (lowest first) |
| Interest to holders | None native | Yield routed to Stability Pool depositors |
| Risk isolation | Single system | Ring-fenced per-collateral branches |

---

## Competitive Position

BOLD competes among decentralized, crypto-backed stablecoins, differentiating on yield, LST collateral, and Liquity's decentralization ethos:

| Stablecoin | Backing | Yield to holders | vs BOLD |
|---|---|---|---|
| **BOLD** (Liquity V2) | ETH + wstETH + rETH (branches) | Yes (via Stability Pool) | Yield-bearing, LST collateral, user-set rates |
| **[[liquity-usd|LUSD]]** (Liquity V1) | ETH only, immutable | None native | Same lineage; simpler, ETH-only, no yield |
| **DAI / USDS** ([[maker|Maker/Sky]]) | Multi-collateral incl. RWA/USDC | Via savings rate | Larger, more centralized collateral |
| **crvUSD** | ETH/LSTs (soft-liquidation LLAMMA) | Indirect | Different liquidation design |

BOLD's edge is combining LST collateral, a borrowing-cost market, and native Stability-Pool yield while staying credibly decentralized; its constraint is small size (~$31.6M cap) and LST collateral risk.

---

## How & Where It Trades

BOLD is primarily an Ethereum-native stable with bridged presence on Optimism and Base. Secondary liquidity is concentrated in DEX pools (Uniswap V3). As a stablecoin, the meaningful metric is peg adherence and redemption depth, not price action.

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | BOLD/USDC | Spot |

---

## Narrative, Category & Catalysts

- **Category:** Decentralized, yield-bearing, crypto-backed [[stablecoin]] — the "DeFi-native dollar with native yield" narrative.
- **Bull catalysts:** Demand for decentralized stables that *pay* holders (via Stability Pool); growth of LST collateral (wstETH/rETH) deepening backing; migration of borrowing demand from V1 [[liquity-usd|LUSD]] to V2; integrations across DeFi.
- **Bear catalysts:** LST [[depeg|depeg]] or smart-contract incidents impairing a branch; thin liquidity limiting large redemptions; competition from larger yield-bearing stables.
- The peg's stability through Extreme-Fear tape is itself the headline: BOLD is functioning as designed in a stressed market.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 30.86M BOLD |
| **Total Supply** | 31.26M BOLD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $31.35M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## History / Timeline

| Date | Event |
|---|---|
| 2025-10-01 | BOLD all-time low of **$0.9829** (brief sub-peg). |
| 2026-03-23 | BOLD all-time high of **$1.02** (brief above-peg). |
| 2026-06-22 | Trades ~$0.999 (on-peg), rank #627, ~$31.6M cap. |

*Only dated events with on-page provenance are listed; as a stablecoin, BOLD's history is a tight band around $1.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.02 (2026-03-23) |
| **Current vs ATH** | -1.34% |
| **All-Time Low** | $0.9829 (2025-10-01) |
| **Current vs ATL** | +2.04% |
| **24h Change** | -0.01% |
| **7d Change** | -0.15% |
| **30d Change** | -0.28% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6440f144b7e50d6a8439336510312d2f54beb01d` |
| Base | `0x03569cc076654f82679c4ba2124d64774781b01d` |
| Optimistic Ethereum | `0x03569cc076654f82679c4ba2124d64774781b01d` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | BOLD/USDC | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |
| **Twitter** | [@LiquityProtocol](https://twitter.com/LiquityProtocol) |
| **GitHub** | [https://github.com/liquity/bold](https://github.com/liquity/bold) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 128 |
| **GitHub Forks** | 132 |
| **Pull Requests Merged** | 733 |
| **Contributors** | 19 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.11M |
| **Market Cap Rank** | #626 |
| **24h Range** | $1.00 — $1.00 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Collateral volatility:** Backing is ETH and LSTs, whose value swings with the crypto market. Sharp drawdowns can push Troves below their minimum ratio and trigger cascading liquidations.
- **Liquid-staking-token risk:** wstETH and rETH carry their own smart-contract, slashing, and (in stress) [[depeg]] risk against ETH, which feeds through to BOLD's collateral quality.
- **Smart-contract risk:** As a fully on-chain protocol, BOLD depends on the correctness of Liquity V2 contracts; a bug could impair backing or redemptions.
- **Redemption pressure on borrowers:** Borrowers who set low interest rates are first in line to be redeemed against, an intentional design that nonetheless can surprise users who do not actively manage their rate.
- **Liquidity / capacity:** With a market cap near $31.6M and modest on-chain depth, large redemptions or swaps can incur slippage relative to fiat-backed majors like USDC or USDT.

> *This is informational, not financial advice. Stablecoins are not risk-free; even overcollateralized designs can deviate from peg under extreme stress.*

---

## Trading Playbook

- **Regime behavior:** BOLD is a yield-bearing decentralized dollar. In risk-off tape it holds peg by design; the variable to watch is supply (contracts as borrowers close Troves when ETH/LST falls) and the Stability-Pool yield available to depositors. It does not appreciate directionally.
- **What to watch:** peg deviation (sustained moves outside ~$0.99–$1.01); ETH and LST (wstETH/rETH) prices and any LST [[depeg]]; per-branch Stability Pool depth; the prevailing borrower interest-rate distribution (low-rate Troves are redemption-first); BOLD supply trend vs [[liquity-usd|LUSD]].
- **In this tape:** with ETH ~27% below its 200-day MA and Extreme Fear, the key risk is collateral stress — monitor LST pegs and branch-level Stability Pool adequacy. For a holder, the appeal is sitting in a decentralized dollar that pays yield via the Stability Pool; the trade is the yield and redemption arbitrage, not price.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[liquity]] — the issuing protocol (V1 and V2) and LQTY token
- [[liquity-usd]] — LUSD, the Liquity V1 stablecoin
- [[stablecoin]] · [[collateralization]] · [[cdp]] · [[depeg]] · [[liquid-staking]] · [[maker]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; market figures as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.
