---
title: "Stablecoins"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["Stablecoin"]
related: ["[[defi]]", "[[terra-luna-collapse]]", "[[bitcoin]]", "[[ethereum]]", "[[usdc]]", "[[usdt]]", "[[dai]]", "[[usds]]", "[[ethena-usde]]", "[[gho]]", "[[frax]]", "[[pyusd]]", "[[other-stablecoins]]", "[[circle]]", "[[tether-limited]]", "[[makerdao]]", "[[stablecoin-regulation]]", "[[cbdc]]", "[[stablecoin-yields]]", "[[stablecoin-depegs]]", "[[stablecoin-use-cases]]", "[[stablecoin-competition]]", "[[stablecoin-attestations]]", "[[blackrock]]", "[[cctp]]"]
domain: [crypto, defi]
difficulty: beginner
---

Stablecoins are [[crypto|cryptocurrencies]] designed to maintain a stable value relative to a reference asset, most commonly the US dollar. They serve as the primary medium of exchange, unit of account, and settlement layer within [[defi|DeFi]] and crypto trading, enabling traders to move in and out of volatile positions without converting to fiat currency.

## Overview

Stablecoins solve a fundamental problem in crypto markets: the need for a stable-value asset on-chain. Before stablecoins, traders had to convert to fiat currency through exchange withdrawals to "de-risk" -- a slow, expensive process. Stablecoins allow instant settlement, 24/7 trading, and composability with DeFi protocols.

As of 2025, the stablecoin market exceeds $150 billion in total market capitalization, with Tether (USDT) and USD Coin (USDC) dominating. Stablecoins are the most traded crypto assets by volume, often exceeding [[bitcoin|Bitcoin]] in daily transaction value. This page is the **reference hub** for the stablecoin topic — see the [[#Deep Dive Pages]] section for individual coins, issuers, and analysis pages.

### Why Stablecoins Matter to Traders

- **The on-chain dollar** — they are the unit of account for nearly all crypto trading. Quote currencies, collateral, and PnL are denominated in stablecoins.
- **Settlement rail** — instant, 24/7, borderless transfer of dollar value without touching the banking system or waiting on wire windows.
- **Yield base** — the "risk-free-ish" rate of crypto. Lending, RWA, and basis strategies all benchmark against stablecoin yield (see [[stablecoin-yields]]).
- **Macro signal** — aggregate stablecoin supply growth is a proxy for capital flowing **into** the crypto ecosystem; contraction signals capital leaving. In an [[market-cycles|established bear market]] (Fear & Greed ~23), watching net mint/burn of USDT and USDC is a key risk-on/risk-off tell.

### Landscape at a Glance

| Stablecoin | Type | Issuer / Protocol | Page |
|---|---|---|---|
| **USDT** (Tether) | Fiat-backed | [[tether-limited\|Tether Limited]] | [[usdt\|tether]] (mention only) |
| **USDC** | Fiat-backed | [[circle\|Circle]] | [[usdc]] |
| **USDS** (formerly DAI) | Crypto + RWA | [[makerdao\|Sky / MakerDAO]] | [[usds]] |
| **DAI** | Crypto-collateralised | [[makerdao\|MakerDAO]] | [[dai]] |
| **USDe** | Synthetic / delta-neutral | Ethena | [[ethena-usde]] |
| **GHO** | Crypto-collateralised | [[aave\|Aave]] | [[gho]] |
| **FRAX / frxUSD** | Hybrid → collateralised | Frax Finance | [[frax]] |
| **PYUSD** | Fiat-backed | PayPal / Paxos | [[pyusd]] |
| **crvUSD, LUSD, FDUSD, EURC, …** | Various | Curve, Liquity, FDT, Circle | [[other-stablecoins]] |

## Peg Mechanism Comparison

The single most important property of a stablecoin is **how it holds its peg** — and what happens when that mechanism is stressed. The four families differ fundamentally in their failure modes.

| Mechanism | How the Peg Holds | Capital Efficiency | Censorship Risk | Primary Failure Mode | Examples |
|---|---|---|---|---|---|
| **Fiat-backed** | 1:1 redeemable for reserves held off-chain | High (1:1) | High (issuer can freeze) | Reserve bank failure / freeze (USDC @ SVB) | [[usdc]], [[usdt\|tether]], [[pyusd]] |
| **Crypto-collateralised** | Over-collateralised crypto, arbitraged via mint/redeem + liquidations | Low (130-170%) | Low (on-chain) | Collateral crash + liquidation cascade | [[dai]], [[gho]], LUSD, crvUSD |
| **Synthetic / delta-neutral** | Long spot crypto hedged with short perps; peg from arbitrage of the hedge | Medium | Medium | Negative [[funding-rates]], exchange/custody failure | [[ethena-usde]] |
| **Algorithmic (seigniorage)** | Mint/burn a sister token to expand/contract supply; **no hard collateral floor** | Very high | Low | Reflexive death spiral (UST/LUNA) | UST (failed), Iron/Titan (failed) |

The market verdict after 2022: **collateral is non-negotiable.** Purely algorithmic designs are dead; the frontier has moved to *synthetic* models (Ethena) that are over-collateralised in substance but earn yield from the basis trade rather than holding idle reserves.

## Types of Stablecoins

### Fiat-Backed (Centralized)

Backed 1:1 by reserves of fiat currency (or equivalent) held by a centralized issuer.

| Stablecoin | Issuer | Market Cap | Backing |
|-----------|--------|-----------|---------|
| **[[usdt|USDT]]** (Tether) | [[tether-limited|Tether Limited]] | ~$110B+ | US Treasuries, cash, commercial paper |
| **[[usdc|USDC]]** (USD Coin) | [[circle|Circle]] | ~$30B+ | US Treasuries, cash deposits |
| **BUSD** | Paxos (for [[binance|Binance]]) | Declining | US Treasuries, cash (wind-down ordered by NYDFS, 2023) |
| **[[pyusd|PYUSD]]** | PayPal / Paxos | Growing | US Treasuries, cash deposits |

> **See also**: [[usdc]], [[usdt]], [[pyusd]], [[other-stablecoins]] for detailed individual pages.

**Advantages**: Simple mechanism, high confidence in peg stability, deep liquidity.
**Risks**: Centralized -- issuers can freeze/blacklist addresses, regulatory risk, counterparty risk (trust the issuer's reserves).

### Crypto-Collateralized (Decentralized)

Backed by over-collateralized crypto deposits locked in [[smart-contracts|smart contracts]].

| Stablecoin | Protocol | Mechanism |
|-----------|----------|-----------|
| **[[dai|DAI]]** | [[makerdao|MakerDAO]] | Users deposit ETH, WBTC, or other crypto as collateral (typically 150%+ ratio) and mint DAI against it |
| **[[usds|USDS]]** | [[makerdao|Sky (formerly MakerDAO)]] | The rebranded successor to DAI under the Sky/Endgame restructuring; backed by crypto **and** tokenised RWA (Treasuries); offers the Sky Savings Rate |
| **[[gho|GHO]]** | [[aave|Aave]] | Native over-collateralised stablecoin minted against Aave deposits; borrow rate set by Aave governance |
| **LUSD** | Liquity | ETH-only collateral, 110% minimum ratio, fully immutable |
| **crvUSD** | Curve Finance | Uses "soft liquidation" (LLAMMA) with continuous rebalancing |

**Advantages**: Decentralized, transparent on-chain reserves, censorship-resistant.
**Risks**: Requires over-collateralization (capital inefficient), liquidation risk during rapid price drops, smart contract risk.

### Synthetic / Delta-Neutral

A newer category that earns yield from the [[basis-trading|basis trade]] rather than holding idle fiat reserves. The issuer holds spot crypto collateral and shorts an equal notional of perpetual futures, making the position **delta-neutral** (insensitive to price) while collecting [[funding-rates|funding]].

| Stablecoin | Protocol | Mechanism |
|-----------|----------|-----------|
| **[[ethena-usde|USDe]]** | Ethena | Backed by staked ETH/BTC spot **plus** short perp positions; the funding spread is passed to holders of sUSDe (staked USDe). Grew to multi-billion supply by 2024-2025 |

**Advantages**: Capital efficient, censorship-resistant, native yield without lending out the reserve.
**Risks**: Depends on positive or neutral [[funding-rates]] — prolonged negative funding erodes backing; relies on centralised exchanges for the hedge (custody + counterparty risk); not "risk-free." See [[ethena-usde]] for the full risk breakdown.

### Algorithmic (Largely Failed)

Attempt to maintain peg through algorithmic supply adjustment rather than collateral backing.

- **UST/Terra (2022)**: The most prominent example. UST maintained its peg through a mint/burn mechanism with LUNA. When confidence collapsed in May 2022, both UST and LUNA entered a "death spiral," with UST losing its peg and LUNA's price crashing from $80+ to near zero. The [[terra-luna-collapse|Terra/Luna collapse]] wiped out approximately $40 billion in value and became a defining cautionary tale for algorithmic stablecoins.
- **[[frax|FRAX]]**: Hybrid model -- originally partially collateralized, partially algorithmic via the FXS share token. Has since moved toward full collateralization (the "frxUSD" era), effectively abandoning the algorithmic portion. A rare survivor of the seigniorage era precisely because it walked back the algorithmic design.
- **Iron/Titan (2021)**: Partially algorithmic stablecoin that collapsed to zero.

**Verdict**: Purely algorithmic stablecoins have failed in practice. The market has largely concluded that meaningful collateral backing is required for a stable peg. See [[terra-luna-collapse]] for the canonical death-spiral case study and [[stablecoin-depegs]] for the broader depeg history.

## Role in Trading

### Settlement and Pairs

- Most [[crypto|crypto]] trading pairs are quoted against USDT or USDC (e.g., BTC/USDT, ETH/USDC)
- Stablecoins replaced BTC-denominated pairs as the standard quote currency on exchanges
- Enable dollar-denominated PnL tracking without fiat banking

### DeFi Applications

- **Lending/borrowing**: Depositing stablecoins on [[aave|Aave]], Compound, or MakerDAO to earn yield or borrow against crypto collateral
- **Liquidity provision**: Stablecoin pairs (USDC/USDT) in [[automated-market-maker|AMM]] pools have minimal [[impermanent-loss]]
- **Yield farming**: Many DeFi yield strategies are denominated in stablecoins
- **Payments**: Increasingly used for real-world payments and cross-border transfers

### Risk Considerations

- **De-peg risk**: USDC briefly traded at $0.87 in March 2023 when Circle disclosed $3.3 billion in reserves held at the failing Silicon Valley Bank
- **Regulatory risk**: Stablecoins are a major focus of global financial regulation; BUSD was forced to wind down by New York regulators
- **Concentration risk**: Tether's dominant market position and historically opaque reserve disclosures remain a systemic concern
- **Sanctions compliance**: USDC and USDT issuers comply with OFAC sanctions, freezing blacklisted addresses

## Key Metrics Traders Watch

| Metric | What It Tells You | Where to Find It |
|---|---|---|
| **Aggregate supply (mint/burn)** | Net capital flowing into/out of crypto. Rising USDT+USDC supply = risk-on; contraction = capital leaving | DeFiLlama, Glassnode |
| **Peg deviation** | A coin trading at $0.997 or $1.003 signals stress, redemption friction, or a yield premium | CEX/DEX order books, Curve pool balances |
| **Curve / Uniswap pool balance** | An imbalanced stablecoin pool (e.g. 80/20) is an early depeg warning before the spot price moves | Curve.fi pool pages |
| **Reserve attestations** | Confirms 1:1 backing exists. Frequency and auditor reputation matter | [[stablecoin-attestations]], issuer sites |
| **Funding rates (for USDe)** | Determines whether synthetic stablecoins are earning or bleeding | [[funding-rates]], exchange dashboards |
| **Dominance ratio (USDT vs USDC)** | Shifts reflect regulatory perception and venue preference (offshore vs US-regulated) | CoinGecko, DeFiLlama |

## Consolidated Risk Reference

| Risk | Affects | Example | Mitigation |
|---|---|---|---|
| Reserve / bank failure | Fiat-backed | USDC @ SVB (Mar 2023) | Diversify issuers; monitor attestations |
| Issuer freeze / blacklist | Fiat-backed | OFAC-sanctioned addresses | Hold decentralised alts ([[dai]], [[gho]]) for censorship resistance |
| Liquidation cascade | Crypto-collateralised | March 2020 "Black Thursday" on MakerDAO | Prefer conservatively collateralised coins; watch collateral mix |
| Negative funding | Synthetic | USDe in prolonged bear funding | Monitor [[funding-rates]]; size exposure |
| Death spiral | Algorithmic | [[terra-luna-collapse\|UST/LUNA]] (May 2022) | Avoid uncollateralised seigniorage designs entirely |
| Smart-contract bug | All on-chain | Various DeFi exploits | Use audited, battle-tested protocols |
| Regulatory shutdown | All | BUSD wind-down (NYDFS, 2023) | Track [[stablecoin-regulation]], MiCA, GENIUS Act |

## Deep Dive Pages

This page serves as the hub for the stablecoin topic. See these pages for detailed coverage:

### Individual Stablecoins
- [[usdc]] -- USD Coin (Circle) -- the regulated standard
- [[usdt|tether]] -- Tether -- the liquidity king (mention only; deepest spot/perp liquidity)
- [[dai]] -- MakerDAO DAI -- the decentralised stablecoin
- [[usds]] -- USDS -- the Sky/MakerDAO successor to DAI (crypto + RWA backed)
- [[ethena-usde]] -- USDe -- synthetic delta-neutral stablecoin (basis-trade yield)
- [[gho]] -- GHO -- Aave's native over-collateralised stablecoin
- [[frax]] -- FRAX / frxUSD -- hybrid model that moved to full collateralisation
- [[pyusd]] -- PayPal USD -- mainstream TradFi entry
- [[other-stablecoins]] -- BUSD, FDUSD, LUSD, crvUSD, EURC, and more

### Issuers
- [[circle]] -- Circle Internet Financial (USDC issuer)
- [[tether-limited]] -- Tether Limited / iFinex (USDT issuer)

### Issuers (continued)
- [[blackrock]] -- BUIDL tokenised money-market fund; increasingly the reserve backbone behind on-chain dollars

### Concepts and Analysis
- [[stablecoin-regulation]] -- Country-by-country regulatory frameworks (US GENIUS Act, EU MiCA, UK, Australia, Singapore, Japan, and more)
- [[cbdc]] -- Central bank digital currencies -- government alternatives to private stablecoins
- [[stablecoin-yields]] -- How to earn yield on stablecoins (lending, LP, RWA, basis trade)
- [[stablecoin-depegs]] -- History of de-peg events and risk management
- [[stablecoin-use-cases]] -- Remittances, dollarisation, B2B payments, payroll, and real-world adoption
- [[stablecoin-competition]] -- Market-share dynamics between USDT, USDC, and challengers
- [[stablecoin-attestations]] -- Reserve attestation and audit practices by issuer
- [[cctp]] -- Circle's Cross-Chain Transfer Protocol for native USDC bridging

## Related

- [[defi]]
- [[terra-luna-collapse]]
- [[makerdao]]
- [[automated-market-maker]]
- [[impermanent-loss]]
- [[bitcoin]]
- [[ethereum]]
- [[coinbase]]
- [[binance]]
- [[regulation]]
- [[aave]]
- [[defi-lending]]
- [[funding-rates]]

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
