---
title: "Stablecoin Yields"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, stablecoin, defi, yield, income]
aliases: ["Stablecoin Yield", "Stablecoin Farming", "DeFi Yields"]
related: ["[[stablecoins]]", "[[defi-lending]]", "[[aave]]", "[[funding-rates]]", "[[impermanent-loss]]", "[[risk-management]]", "[[cryptocurrency-tax-australia]]", "[[usdc]]", "[[usdt]]", "[[dai]]", "[[ethena-usde]]", "[[ousg]]", "[[hashnote-usyc]]", "[[pendle]]", "[[automated-market-maker]]"]
domain: [defi, risk-management]
difficulty: intermediate
---

Stablecoin yield strategies allow traders and investors to earn returns on [[stablecoins|stablecoin]] holdings without taking directional exposure to volatile crypto assets. Yields range from 2-5% (low risk, comparable to traditional savings accounts) to 10-30%+ (high risk, requiring active management and DeFi expertise). Understanding where stablecoin yields come from -- and what risks they carry -- is essential for anyone holding significant stablecoin balances.

> **Reference hub.** This page maps *where stablecoin yield actually comes from* — T-bill RWA, lending demand, LP fees, and basis/funding — and tiers each by risk. It is not a single asset and carries no price block. Follow the wikilinks to specific instruments: [[ousg]], [[hashnote-usyc]], [[ethena-usde]], [[pendle]], [[dai]], [[aave]]. Macro context (qualitative, 2026-06-21): the broad crypto tape is in an **Established Bear Market** with the Crypto Fear & Greed Index around **23 ("Extreme Fear")**. Two yield-source implications follow directly: (1) **funding/basis yield compresses or inverts** in fear regimes (longs stop paying), so delta-neutral APYs ([[ethena-usde|USDe]]) fall hardest; (2) **T-bill RWA yield is regime-independent** — it tracks the policy rate, not crypto sentiment, which is why RWA stablecoins shine relatively in bear markets.

## Overview

The fundamental question for any yield opportunity is: **where does the yield come from?**

Legitimate stablecoin yields derive from one of these sources:

1. **Lending demand**: Leveraged traders borrow stablecoins to go long on crypto assets. They pay interest to lenders.
2. **Market making fees**: Liquidity providers earn a share of trading fees from decentralised exchanges.
3. **Real-world asset yield**: US Treasury yields (~4-5%) or other traditional finance yields passed through to on-chain stablecoin holders.
4. **Protocol incentives**: Temporary token emissions used to attract liquidity (not sustainable long-term).
5. **Funding rate arbitrage**: Exploiting the gap between spot and perpetual futures prices. See [[funding-rates]].

> **"If you can't identify the yield source, YOU are the yield."** -- Unsustainable or unexplained high yields almost always indicate hidden risks. The [[terra-luna-collapse|Terra/Luna collapse]] (Anchor Protocol offering 20% APY on UST) is the canonical example.

## Yield Sources in Detail

### 1. Centralised Exchange Savings/Earn Programs

| Platform | Typical APY | Mechanism |
|----------|-----------|-----------|
| [[binance|Binance]] Earn | 2-6% | Binance lends your stablecoins to margin traders and institutional borrowers |
| [[coinbase|Coinbase]] USDC Rewards | 4-5% | Coinbase shares a portion of USDC reserve yield with holders (Circle partnership) |
| Bybit Earn | 3-8% | Lending to Bybit's margin and derivatives traders |
| OKX Earn | 2-6% | Similar lending model |

**Risks**: Counterparty risk = the exchange itself. If the exchange becomes insolvent (as FTX did in November 2022), all deposited funds may be lost. Exchange "earn" products are unsecured loans to the exchange.

**Suitability**: Beginners; traders who already hold funds on exchange. Convenience over maximum yield.

### 2. DeFi Lending Protocols

Supply stablecoins to decentralised lending protocols and earn variable interest from borrowers:

| Protocol | Typical APY (variable) | Notes |
|----------|----------------------|-------|
| [[aave|Aave]] v3 | 2-10% | Largest DeFi lending protocol. Multi-chain. See [[defi-lending]] |
| Compound v3 | 2-8% | Ethereum-focused, battle-tested |
| Morpho | 3-12% | Optimised lending aggregator, matches lenders/borrowers peer-to-peer |
| Spark Protocol | 3-8% | MakerDAO's lending protocol, closely integrated with [[dai|DAI]] |

**How it works**: You deposit stablecoins (e.g., [[usdc|USDC]]) into a lending pool. Borrowers deposit crypto collateral (e.g., ETH) and borrow your stablecoins, paying variable interest. If their collateral value drops below the liquidation threshold, it is automatically sold to repay lenders.

**Risks**: Smart contract risk (code bugs, exploits), oracle manipulation, liquidity risk during extreme volatility, governance risk. Major blue-chip protocols (Aave, Compound) have sustained billions in TVL through multiple market cycles without significant losses.

### 3. Liquidity Provision (AMM Pools)

Provide stablecoins to [[automated-market-maker|AMM]] pools on decentralised exchanges and earn a share of trading fees:

| Pool Type | Typical APY | IL Risk | Examples |
|-----------|-----------|---------|---------|
| Stablecoin/stablecoin | 3-15% | Very low | USDC/USDT, USDC/DAI on Curve |
| Stablecoin/volatile asset | 5-30%+ | HIGH | USDC/ETH on Uniswap |

**Stable-stable pools**: Pools pairing two stablecoins (e.g., USDC/USDT) have minimal [[impermanent-loss]] because both assets maintain the same ~$1 peg. Yields come from trading fees and, frequently, additional protocol incentive tokens. Curve Finance specialises in these pools.

**Stable-volatile pools**: Pools pairing a stablecoin with a volatile asset (e.g., USDC/ETH) have high impermanent loss risk. While APY may appear attractive, IL can exceed trading fee income during large price moves.

**Risks**: Impermanent loss (for volatile pairs), smart contract risk, de-peg risk (if one stablecoin in a stable pair loses its peg, the pool absorbs it). See [[impermanent-loss]].

### 4. Yield Aggregators

Protocols that automatically compound and optimise stablecoin yields across multiple DeFi strategies:

| Protocol | Strategy | Notes |
|----------|---------|-------|
| Yearn Finance | Auto-compounds best available yield across Aave, Compound, Curve, etc. | Pioneer of yield aggregation. "Set and forget." |
| Beefy Finance | Multi-chain yield aggregation and auto-compounding | Widest chain coverage |
| Sommelier Finance | Algorithmic yield strategies managed by "strategists" | More active management |

**Risks**: Smart contract risk is **compounded** -- you are exposed to the aggregator's smart contract risk PLUS the risk of every underlying protocol it interacts with. More layers = more potential failure points.

### 5. Real-World Asset (RWA) Yield

A growing category of stablecoins and protocols that pass through yield from traditional financial assets (primarily US Treasuries):

| Product | Issuer/Protocol | Yield Source | APY | Notes |
|---------|----------------|-------------|-----|-------|
| **sDAI** | MakerDAO | DSR (US Treasuries, stability fees) | 5-8% | See [[dai]]. Auto-rebasing token |
| **sFRAX** | Frax Finance | US Treasuries | 4-5% | Frax's yield-bearing stablecoin; see [[frax]] |
| **USDY** | Ondo Finance | Tokenised US Treasury portfolio | 4-5% | Requires KYC, 40-day lockup for new purchases |
| **OUSG** | Ondo Finance | Tokenised short-term US Treasuries (BlackRock BUIDL / fund wrappers) | 4-5% | Institutional/KYC-gated; near-instant mint/redeem in updated versions. See [[ousg]] |
| **USYC** | Hashnote / Circle | Tokenised T-bill / reverse-repo yield | 4-5% | Institutional cash-management token, acquired into the Circle orbit. See [[hashnote-usyc]] |
| **USDM** | Mountain Protocol | US Treasuries | 4-5% | ERC-20 rebasing token, no lockup |
| **bUIDL** | BlackRock/Securitize | Tokenised Treasury fund | 4-5% | Institutional-grade, $5M minimum; backs several other RWA products |

**How it works**: These products hold US Treasury securities and distribute the yield to token holders. The yield approximates the risk-free rate (~4-5% in 2024) minus fees.

**Significance**: RWA yield represents the intersection of traditional finance yield and on-chain stablecoin utility. For the first time, holding a stablecoin can earn a return comparable to a money market fund -- without a brokerage account.

**Regulatory risk**: Yield-bearing stablecoins may be classified as **securities** by the [[sec|SEC]], since they offer an investment return. This is a critical distinction: "payment stablecoins" (no yield) are likely to be regulated as money transmission, while "yield-bearing stablecoins" face potential securities regulation. See [[stablecoin-regulation]].

### 6. Funding Rate Arbitrage (Basis Trade)

One of the most sophisticated stablecoin yield strategies, sometimes called the "basis trade" or "cash and carry":

- **Mechanism**: Go long spot crypto (e.g., buy [[bitcoin|BTC]]), simultaneously go short BTC perpetual futures. When [[funding-rates|funding rates]] are positive (bullish market), shorts receive periodic payments from longs.
- **Yield**: 10-30% APY during bullish periods when funding rates are consistently positive. Near-zero or negative during bearish periods.
- **Market-neutral**: The long spot and short perp positions offset each other, resulting in zero directional exposure. Profit comes purely from funding payments, denominated in stablecoins.
- **Risks**: Exchange counterparty risk, funding rate reversal (rates can go negative), liquidation risk if not properly hedged, basis risk between spot and perp prices during extreme volatility
- **Where**: Primarily executed on centralised exchanges ([[binance|Binance]], Bybit, OKX) or decentralised perp protocols
- **Tokenised version**: [[ethena-usde|Ethena's USDe/sUSDe]] packages exactly this delta-neutral basis trade into a single ERC-20 token — holders earn the funding + staking yield without running the hedge themselves. The same engine powers Binance's [[bfusd|BFUSD]] margin asset. The trade-off: you inherit funding-inversion risk and the protocol's custody/exchange exposure rather than running it yourself

See [[funding-rates]] for detailed mechanics.

### 7. Yield Tokenization (Pendle and fixed-rate stablecoin yield)

[[pendle|Pendle]] splits any yield-bearing token into two tradeable parts: a **Principal Token (PT)** redeemable for the underlying at maturity, and a **Yield Token (YT)** that captures the variable yield until maturity. For stablecoin holders this unlocks strategies the raw yield products cannot:

- **Fixed-rate yield**: Buy a PT at a discount and hold to maturity → a *locked, fixed* APY on a stablecoin position (e.g., fixed yield on sUSDe, sDAI, or an RWA token), insulating you from the variable-rate volatility that plagues lending and basis yield
- **Yield speculation / leverage**: Buy YT to take a leveraged, directional bet that the underlying yield will stay high (e.g., that [[ethena-usde|USDe]] funding stays positive) — high upside, total loss of the YT premium if yield collapses
- **LP on PT/YT pools**: Provide liquidity and earn swap fees plus PENDLE incentives

| Pendle leg | What you get | Best when |
|---|---|---|
| **PT (Principal)** | Fixed yield to maturity, discounted entry | You want predictable, locked stablecoin yield |
| **YT (Yield)** | Leveraged exposure to the variable yield stream | You expect underlying APY to stay elevated |
| **LP** | Fees + incentives, mixed PT/YT exposure | Range-bound yield, want to harvest emissions |

**Risks**: Pendle smart-contract risk *plus* the underlying protocol's risk (you are layered on top of sUSDe, sDAI, etc.), maturity/rollover risk, and YT time-decay (YT trends to zero as maturity approaches). It is a sophisticated overlay, not a beginner product.

## Risk Tiers

| Risk Tier | Yield Range | Sources | Key Risks |
|-----------|-----------|---------|-----------|
| **Low** | 2-5% | CEX savings (reputable exchange), T-bill-backed yield (sDAI, USDY), Coinbase USDC rewards | Exchange insolvency, smart contract risk (minimal for T-bills), interest rate changes |
| **Medium** | 5-12% | Blue-chip DeFi lending (Aave, Compound), Stable-stable LP (Curve), Yield aggregators (Yearn) | Smart contract risk, oracle risk, protocol governance risk |
| **High** | 12-30%+ | Leveraged farming, New/unaudited protocols, Volatile-pair LP, Funding rate arbitrage | Smart contract exploits, impermanent loss, liquidation, counterparty risk, leverage risk |
| **Unsustainable** | 30%+ (consistent) | Ponzi mechanics, Token emissions with no revenue backing, "Too good to be true" | Total loss. If a protocol consistently offers 30%+ APY without a clear revenue source, the yield is coming from new depositors (Ponzi) or temporary token emissions that will collapse |

## Due Diligence Checklist

Before deploying stablecoins into any yield opportunity:

1. **Identify the yield source**: Who is paying you, and why? If the answer is "token emissions" -- those will decline over time
2. **Check audit status**: Has the protocol been audited by reputable firms? Multiple audits are better than one
3. **Assess TVL history**: Large, stable TVL over months/years is more trustworthy than rapidly growing TVL
4. **Understand liquidation mechanics**: For lending -- what happens during extreme volatility?
5. **Check governance**: Who controls the protocol? Can they change parameters (interest rates, fees, collateral requirements) unilaterally?
6. **Diversify**: Never put all stablecoin holdings in a single yield source. Spread across protocols, chains, and risk tiers
7. **Monitor**: DeFi yields are variable. What pays 10% today may pay 2% tomorrow (or the protocol may be exploited)

## Tax Treatment

Stablecoin yield is generally taxable as **ordinary income** in most jurisdictions:

- **Australia**: Stablecoin interest, lending income, and LP fees are taxable as ordinary income when received. See [[cryptocurrency-tax-australia]]
- **United States**: Taxed as ordinary income at receipt. Staking/lending rewards are income
- **UK**: Income tax on DeFi yields, with some ambiguity around LP positions
- **Record-keeping**: Track every yield payment, its value at receipt, and the protocol/chain it was earned on. DeFi yield tracking is complex -- tools like CoinTracker, Koinly, and CryptoTaxCalculator can help

## Related

- [[stablecoins]] -- Stablecoin market overview
- [[defi-lending]] -- DeFi lending protocols in detail
- [[aave]] -- Major DeFi lending protocol
- [[automated-market-maker]] -- AMM mechanics for liquidity provision
- [[impermanent-loss]] -- Key risk for LP positions
- [[funding-rates]] -- Funding rate mechanics and arbitrage
- [[ethena-usde]] -- Tokenised delta-neutral basis yield (USDe/sUSDe)
- [[ousg]] -- Tokenised short-term Treasuries (Ondo)
- [[hashnote-usyc]] -- Tokenised T-bill / repo yield
- [[pendle]] -- Yield tokenization (fixed-rate and leveraged yield)
- [[frax]] -- sFRAX RWA yield-bearing stablecoin
- [[dai]] -- DAI/sDAI yield-bearing stablecoin
- [[usdc]] -- Most common stablecoin for yield strategies
- [[risk-management]] -- Portfolio risk management
- [[cryptocurrency-tax-australia]] -- Australian tax treatment
- [[stablecoin-regulation]] -- Regulatory implications of yield-bearing stablecoins

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
