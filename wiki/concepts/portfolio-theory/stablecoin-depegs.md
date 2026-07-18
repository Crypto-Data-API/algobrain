---
title: "Stablecoin De-Peg Events"
type: concept
created: 2026-04-07
updated: 2026-07-13
status: excellent
tags: [crypto, stablecoins, risk-management, history]
aliases: ["De-peg", "Stablecoin De-peg Events", "De-pegging"]
related: ["[[stablecoins]]", "[[terra-luna-collapse]]", "[[usdc]]", "[[usdt]]", "[[dai]]", "[[risk-management]]", "[[defi]]", "[[stablecoin-regulation]]", "[[cryptodataapi]]"]
domain: [risk-management, crypto]
difficulty: intermediate
---

A stablecoin de-peg occurs when a [[stablecoins|stablecoin]] trades significantly above or below its target price (usually $1.00). De-peg events range from brief deviations lasting minutes to catastrophic collapses destroying tens of billions in value. Understanding de-peg history is essential risk management knowledge for any trader or investor holding stablecoins.

## Overview

Stablecoins are designed to trade at a fixed price, but they are not guaranteed to do so. The peg is maintained through a combination of reserve backing, market arbitrage, algorithmic mechanisms, and -- ultimately -- confidence. When any of these fail, the stablecoin can trade below (or occasionally above) its target price.

The severity of de-pegs varies enormously:

- **Minor de-peg** (<2% deviation): Common during high-volatility periods, corrected within minutes to hours by arbitrageurs
- **Significant de-peg** (2-15% deviation): Indicates real stress on the stablecoin's backing or confidence. May take hours to days to resolve
- **Catastrophic de-peg** (>50% deviation / total collapse): The stablecoin's mechanism has fundamentally failed. Recovery is unlikely

## Stablecoin Designs and How the Peg Is Held

A de-peg is best understood by first understanding *how the peg is supposed to hold*. Different designs have different failure modes, and the design dictates whether a deviation is a recoverable liquidity event or a terminal solvency event.

| Design | How the peg is held | Examples | Dominant failure mode |
|--------|--------------------|----------|----------------------|
| **Fiat-backed (off-chain reserves)** | Issuer holds cash + T-bills 1:1; mint/redeem at $1 for KYC'd partners; arbitrage closes secondary-market gaps | [[usdc\|USDC]], [[usdt\|USDT]], FDUSD | Banking counterparty failure, reserve opacity, redemption friction |
| **Crypto-collateralized (overcollateralized)** | On-chain collateral > 100% of supply; liquidations and a peg-stability module defend $1 | [[dai\|DAI]], LUSD | Collateral crash, oracle failure, dependence on a centralized stablecoin as collateral |
| **Algorithmic / seigniorage** | A volatile sister token absorbs supply changes via mint/burn; *no* hard reserve floor | UST/[[terra-luna-collapse\|LUNA]], Iron/TITAN | Reflexive "death spiral" -- collapse feeds on itself |
| **Yield/synthetic (delta-neutral)** | Backed by a hedged position (e.g., spot + short perp); peg from collateral value + funding | USDe-style designs | Funding-rate inversion, exchange/counterparty risk, collateral custody |

The single most important distinction for risk management: **a fiat- or crypto-backed coin can de-peg on a *liquidity* shock and recover when arbitrage or redemption catches up; an algorithmic coin de-pegs on a *confidence* shock that its own mechanism then amplifies.** See [[stablecoins]] for the full taxonomy.

### The Arbitrage Loop That Normally Holds the Peg

For a redeemable stablecoin, arbitrage is the restoring force:

- **Below $1**: buy the stablecoin cheap on the open market, redeem with the issuer for $1, pocket the spread. This buying pushes the price back up.
- **Above $1**: mint new stablecoin from the issuer for $1, sell on the open market above $1. This selling pushes the price back down.

The loop only works if (1) redemption/minting is actually available and fast, (2) the reserves exist, and (3) there is enough on-chain liquidity to absorb the flow. A de-peg is, mechanically, a sign that one of those three has broken or that the market doubts it has. See [[arbitrage]].

## Major De-Peg Events

### UST / Terra Luna (May 2022) -- Catastrophic

The defining stablecoin failure. UST was an **algorithmic stablecoin** with no real reserve backing, maintaining its peg through a mint/burn mechanism with the LUNA token.

**Timeline:**
- **May 7, 2022**: Large UST sell-offs (~$285M) on Curve Finance pushed UST to $0.985
- **May 8-9**: UST dropped to $0.90 as panic selling accelerated. The Luna Foundation Guard (LFG) deployed ~$1.5B in [[bitcoin|Bitcoin]] reserves trying to defend the peg -- and failed
- **May 10-11**: The death spiral began. UST lost its peg entirely. LUNA was hyperinflated by the mint/burn mechanism (minting LUNA to absorb UST redemptions). LUNA price crashed from $80+ toward zero
- **May 12-13**: UST traded at $0.10-0.20. LUNA's supply inflated from 350 million to 6.5 trillion tokens. Market cap collapsed from ~$40B to near zero
- **Aftermath**: UST eventually settled near ~$0.02. ~$40 billion in combined UST/LUNA value destroyed. Do Kwon (Terra founder) arrested in Montenegro (March 2023). Multiple lawsuits and criminal investigations. The collapse triggered contagion that contributed to the failures of Three Arrows Capital, Celsius, Voyager, and ultimately FTX

**Lessons:**
- Algorithmic stablecoins without meaningful collateral are inherently fragile -- "reflexive death spirals" are a feature, not a bug, of these designs
- 20% APY yield on Anchor Protocol (UST's primary use case) was unsustainable and attracted deposits ($20B+) without corresponding revenue to support it
- The phrase "too big to fail" does not apply in crypto -- $40B can evaporate in days

See [[terra-luna-collapse]] for full analysis.

### USDC / Silicon Valley Bank (March 2023) -- Significant

The most significant de-peg of a major **fiat-backed** stablecoin, demonstrating that even "fully backed" stablecoins carry real risks.

**Timeline:**
- **March 10, 2023 (Friday)**: Silicon Valley Bank (SVB) failed -- the second-largest US bank failure in history. [[circle|Circle]] disclosed that approximately **$3.3 billion** of [[usdc|USDC]] reserves (~8% of total) were held at SVB
- **March 10-12 (Weekend)**: Panic selling of USDC on decentralised exchanges. USDC traded as low as **$0.87** on DEXs. Curve 3pool became heavily imbalanced (USDC flooded the pool, USDT drained out). CEX prices lagged the DEX de-peg
- **March 12**: [[dai|DAI]] also de-pegged to ~$0.89 because a significant portion of DAI collateral was USDC (via the Peg Stability Module). Contagion from one stablecoin to another
- **March 13 (Monday)**: Federal Reserve and FDIC announced that **all SVB depositors would be made whole** regardless of the $250K FDIC insurance limit. USDC peg was restored within hours

**Lessons:**
- "Fully backed" stablecoins carry **banking counterparty risk** -- if the bank holding reserves fails, the stablecoin's backing is at risk
- Concentration of reserves at a single bank creates systemic vulnerability -- Circle subsequently diversified its banking relationships
- DEX prices are the "real-time" price during stress events. CEX prices can lag significantly
- Government intervention (FDIC backstop) was what ultimately restored the peg -- the market could not self-correct without it
- [[dai|DAI]]'s de-peg exposed the centralisation paradox: a "decentralised" stablecoin was dependent on a centralised stablecoin ([[usdc|USDC]]) as major collateral

### USDT (May 2022) -- Brief

During the [[terra-luna-collapse|Terra/Luna collapse]], fear spread to all stablecoins:

- **May 12, 2022**: [[usdt|USDT]] briefly traded at **~$0.95** on some exchanges as panic selling affected the entire stablecoin market
- Recovery was swift -- within hours, USDT returned to $0.99-1.00
- [[tether-limited|Tether]] processed **$7 billion+ in redemptions** in the following week without issue
- Paradoxically, this event **strengthened** confidence in USDT -- Tether proved it could handle massive redemption demand during a market-wide panic

**Lessons:**
- Even the most liquid stablecoin is vulnerable to confidence crises during systemic events
- Tether's ability to process billions in redemptions under stress was a crucial test of its reserves
- Contagion between stablecoins is real -- the failure of one can cause panic in others

### USDT (October 2018) -- Moderate

An earlier, more severe USDT de-peg:

- **October 15, 2018**: Amid growing concerns about Tether's banking relationships and reserve adequacy, USDT traded at **~$0.92-0.95** on multiple exchanges
- The de-peg lasted several days before gradually recovering
- [[bitcoin|Bitcoin]] price actually spiked during this event as traders fled USDT into BTC (a "flight to quality" within crypto)
- This event preceded the NYAG investigation into Tether

### Iron/Titan (June 2021) -- Catastrophic

A partially algorithmic stablecoin on Polygon that collapsed to zero:

- **Iron Finance** used a partial algorithmic mechanism similar to (but preceding) Terra/UST
- On June 16, 2021, a bank run triggered the algorithmic component to death-spiral
- TITAN token collapsed from ~$60 to near zero within hours
- IRON stablecoin lost its peg permanently
- Notable because **Mark Cuban** was a prominent liquidity provider and publicly lost money -- he subsequently called for stablecoin regulation
- Total value lost: relatively small (~$2B) compared to Terra, but foreshadowed the UST collapse a year later

### sUSD -- Synthetix (Chronic)

The Synthetix protocol's stablecoin sUSD has experienced **repeated de-pegs**:

- sUSD has frequently traded at $0.95-0.98 or below for extended periods
- Causes: Low liquidity, complex debt-pool mechanism, limited redemption arbitrage
- sUSD demonstrates that stablecoin mechanism design matters enormously -- even backed stablecoins can persistently trade below peg if the arbitrage mechanism is insufficient

### HUSD -- Huobi (2022) -- Permanent

- HUSD, associated with the Huobi exchange, lost its peg in August 2022
- Traded as low as $0.80 before being de-listed from most exchanges
- Reserve composition and management were unclear
- Highlights the risk of exchange-affiliated stablecoins with poor transparency

### FDUSD Stress (March 2025)

- Justin Sun publicly alleged that First Digital Trust (FDUSD issuer) had inadequate reserves
- FDUSD briefly dipped to ~$0.97 before First Digital denied the claims and initiated legal action
- Peg was restored relatively quickly
- Demonstrated that even public allegations (regardless of merit) can cause brief de-pegs

## Common Causes of De-Pegs

| Cause | Examples | Severity |
|-------|---------|----------|
| **Reserve inadequacy** | Algorithmic stablecoins with no reserves (UST), undisclosed reserve composition | Catastrophic |
| **Banking counterparty failure** | USDC/SVB | Significant (recoverable if deposits are insured) |
| **Confidence crisis / bank run** | USDT Oct 2018, contagion during Terra collapse | Variable -- depends on whether redemptions are honoured |
| **Mechanism design flaw** | Iron/Titan death spiral, sUSD chronic under-peg | Catastrophic for algorithmic; chronic for poorly designed |
| **Oracle failure** | Flash loan attacks manipulating price feeds | Usually brief, protocol-specific |
| **Liquidity crisis** | Low DEX liquidity amplifies selling pressure during stress | Variable -- worse for smaller stablecoins |
| **Contagion** | DAI de-pegging because of USDC de-peg, USDT de-pegging during Terra collapse | Depends on underlying exposure |
| **Regulatory action** | BUSD ordered to wind down by NYDFS (orderly decline, not sudden de-peg) | Managed decline rather than sudden de-peg |

## De-Peg Detection and Monitoring

Traders should monitor for early warning signs:

### On-Chain Indicators

- **Curve 3pool ratio**: The USDC/USDT/DAI pool on Curve Finance is a key barometer. A heavily imbalanced pool (e.g., 70% USDC / 15% USDT / 15% DAI) indicates stress on the over-represented stablecoin as holders dump it for alternatives
- **DEX price vs CEX price**: If a stablecoin trades at $0.98 on Uniswap but $1.00 on [[binance|Binance]], the DEX price is the "real" price -- CEX prices lag during stress
- **Large redemptions**: On-chain data showing massive burns of a stablecoin (issuers redeeming for USD) can indicate either healthy arbitrage or early panic
- **Reserve wallet monitoring**: For transparent stablecoins, monitoring the issuer's reserve wallets for unusual outflows

### Market Indicators

- **Funding rates**: Extremely negative [[funding-rates|funding rates]] on stablecoin pairs can indicate severe selling pressure
- **Options implied volatility**: Rising IV on stablecoin-related assets
- **Social media sentiment**: Rapid shift in Crypto Twitter sentiment about a specific stablecoin often precedes or accompanies de-pegs
- **Exchange withdrawal suspensions**: If exchanges suspend stablecoin withdrawals, this is a major red flag

## Worked Example (Illustrative) — Reading a Fiat-Backed De-Peg in Real Time

*The figures below are illustrative and used to demonstrate the decision process, not a record of a specific trade.*

Suppose a major fiat-backed stablecoin (call it "XUSD") trades at **$0.96 on a [[decentralized-exchanges|DEX]]** while still showing **$1.00 on a centralized exchange**, over a weekend, after news that one of its banking partners is in trouble.

A trader works the problem in this order:

1. **Liquidity event or solvency event?** Identify *what fraction* of reserves is exposed to the troubled bank. If the disclosure is "~8% of reserves at one bank" and the rest is in T-bills, the *expected* impairment is small even in a bad outcome — this looks like a liquidity/confidence shock, not insolvency.
2. **Where is the real price?** During stress the **DEX price leads** and the CEX price lags. The $0.96 DEX print is the market-clearing price; the $1.00 CEX quote is stale. Trust the DEX.
3. **Is redemption open?** If the issuer is still redeeming 1:1 (or credibly will once banks reopen), then buying at $0.96 and redeeming at $1.00 is a ~4% edge *conditional on* the redemption channel reopening.
4. **Size for the tail.** The reason the discount exists is that the market assigns nonzero probability to a worse outcome (redemption frozen, larger impairment). Position sizing must survive the scenario where $0.96 becomes $0.85 before it becomes $1.00.
5. **Watch the contagion vector.** If a "decentralized" coin uses XUSD as collateral, *that* coin will de-peg next (this is exactly the [[dai|DAI]]/[[usdc|USDC]] linkage from March 2023). Either avoid it or trade the second-order de-peg.

**Outcome logic:** if a government or issuer backstop restores confidence (as the FDIC backstop did for [[usdc|USDC]] in March 2023), the peg snaps back within hours and the discount buyers are paid. If instead it is a UST-style solvency/mechanism failure, the same "buy the dip" reflex is catastrophic. The entire edge lives in correctly diagnosing step 1.

## Risk Management Strategies

### Diversification

**Never hold 100% of your portfolio in a single stablecoin.** A reasonable diversification strategy:

- 40-50% in [[usdc|USDC]] (most transparent, regulatory compliance)
- 30-40% in [[usdt|USDT]] (deepest liquidity, widest acceptance)
- 10-20% in [[dai|DAI]] or other decentralised stablecoins (censorship resistance)
- Consider non-stablecoin cash equivalents: actual fiat on exchange, bank deposits

### Exit Plan

Have a pre-planned response for de-peg scenarios:

1. **Set price alerts**: Configure alerts for any stablecoin trading below $0.995 on DEXs
2. **Know your swap routes**: Identify the fastest path to swap from a de-pegging stablecoin to an alternative (Curve, Uniswap, 1inch)
3. **Accept the trade-off**: Selling a de-pegging stablecoin at $0.95 may be better than holding and watching it go to $0.50 (or $0.02 in UST's case). However, if the stablecoin is fiat-backed with real reserves, holding through a temporary de-peg and redeeming at $1.00 may be optimal
4. **Consider hedging**: During high-risk periods, short stablecoin perpetual futures to hedge de-peg exposure

### Due Diligence

Before holding significant amounts of any stablecoin:

- Understand the backing mechanism (fiat reserves? crypto collateral? algorithmic?)
- Review reserve attestation/audit history
- Assess the issuer's regulatory status and jurisdiction
- Check the redemption mechanism (can you redeem 1:1 for USD? How quickly?)
- Monitor on-chain reserve data where available

## Common Pitfalls

| Pitfall | Why it bites |
|---------|-------------|
| **Treating all de-pegs as buy-the-dip** | Works for redeemable coins on liquidity shocks; fatal for algorithmic coins in a death spiral (UST) |
| **Trusting the CEX quote** | CEX prices lag the DEX during stress; the stale $1.00 quote masks the real risk |
| **Ignoring collateral linkages** | A "decentralized" coin backed by a centralized one inherits the latter's de-peg (DAI/USDC, March 2023) |
| **Underestimating the withdrawal/redemption queue** | The redemption arbitrage only works if redemption is open and timely; queues can stretch days under stress |
| **Over-concentration** | Holding 100% of cash in one stablecoin turns a single issuer's bad day into a portfolio-level loss |
| **Chasing yield as a peg signal** | Unsustainable yield (Anchor's 20% on UST) is a *cause* of fragility, not a reward for it |
| **Confusing soft and hard pegs** | A staked-ETH derivative like [[lido\|stETH]] trades on redeemability, not a $1 reserve — different mechanics, see [[steth]] |

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/security/events` — recent hacks/depegs (10d lookback, filterable)
- `GET /api/v1/security/regime/score` — security-stress composite (45% hack, 30% flow, 25% depeg)
- `GET /api/v1/security/regime/{symbol}` — per-symbol security overlay

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshots

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/security/events"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[stablecoins]] -- Stablecoin market overview and types
- [[terra-luna-collapse]] -- Detailed analysis of the UST catastrophe
- [[usdc]] -- USDC and the SVB de-peg
- [[usdt]] -- USDT de-peg history
- [[dai]] -- DAI and its centralisation paradox
- [[risk-management]] -- Portfolio risk management principles
- [[defi]] -- DeFi ecosystem context
- [[stablecoin-regulation]] -- How regulation is shaped by de-peg events
- [[arbitrage]] -- The restoring force that normally holds a peg
- [[steth]] / [[lido]] -- A soft, redeemability-based peg (contrast with fiat pegs)
- [[decentralized-exchanges]] -- Where the real-time stress price prints first

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
