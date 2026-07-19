---
title: "Protective Put (Crypto)"
type: strategy
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [options, crypto, hedging, risk-management, protective-put, tail-risk, derivatives, bitcoin, ethereum]
aliases: ["Protective Puts", "Portfolio Insurance", "Crypto Protective Put", "protective-puts"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[married-put]]", "[[collar]]", "[[covered-call]]", "[[hedging]]", "[[tail-risk-hedging]]", "[[variance-risk-premium]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[staking]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[cryptodataapi]]"]
---

# Protective Put (Crypto)

A protective put is a [[hedging]] overlay in which a holder of spot [[bitcoin|BTC]]/[[ethereum|ETH]] (or a BTC-ETF position) buys a [[put-options|put]] on the same coin to floor downside risk while keeping full upside. The put is insurance: below its strike it gains value roughly one-for-one, capping the position's loss at (spot entry − strike) + premium. Unlike most pages in this wiki, the protective put is a **risk-transfer overlay, not an alpha source** — in isolation it has negative expected return, and its value is convexity, survival, and constraint relief, not edge over a counterparty. Where the [[married-put]] is a *protected entry* bought with the coin, the protective put is the same structure **added to and rolled on an existing holding** — so this page carries the systematic-hedging detail: rolling, monetization, cost, and the premium-drag critique.

## Overview

The protective put is the options-market equivalent of an insurance policy. The holder keeps long spot exposure and buys a put at or below spot; if the coin gaps down, the put offsets the loss below the strike. The payoff profile is identical to a **long call**: unlimited upside, defined maximum loss. Above breakeven (spot entry + premium) the position tracks the coin minus the insurance cost.

Protective puts are most relevant for **concentrated crypto holders who cannot or will not sell** — miners, treasuries/DAOs, funds with lockups, or individuals facing a hard liquidity deadline — and for hedging a known catalyst (an unlock, a macro print, an exchange-solvency scare). The honest framing carries over from equities: *if you have no concentration, leverage, or liquidity constraint, the cheaper "hedge" is usually to hold fewer coins.*

## Construction

1. **Hold** spot BTC/ETH; **buy 1 put per unit of coin** on [[deribit]] (or an ETF put for an ETF holding).
2. **Strike:** 5-15% OTM is the practical default — ATM protection in crypto's high [[implied-volatility|IV]] can cost 20-40%+ annualized and is rarely justified. The OTM strike is your deductible.
3. **Tenor:** cover the risk window plus a buffer — typically 1-3 months; buy slightly longer than needed and exit early rather than holding into the final-30-day theta acceleration.
4. **Timing:** prefer entry when DVOL is low (insurance cheap); avoid initiating after a vol spike.
5. Prefer **USDC-margined (linear)** puts for a clean USD floor.

## Payoff & breakevens

| Point | Value |
|---|---|
| **Max loss** | (Spot entry − put strike) + premium paid |
| **Breakeven** | Spot entry + premium paid |
| **Max profit** | Unlimited |
| **Effective floor** | Put strike − premium |

## Greeks profile

The long-put leg drives the hedge's behavior:

| Greek | Sign (long put) | Meaning for the hedge |
|---|---|---|
| [[delta]] | Negative (−0.10 to −0.90) | Offset grows as spot falls and the put goes ITM; ~0 when far OTM (the deductible zone) |
| [[gamma]] | Positive | Convexity — protection *accelerates* in a fast, deep drop; the reason to buy the put rather than just de-risk |
| [[theta]] | Negative | The daily carry cost — the bleed that makes the standalone position negative-expectancy |
| [[vega]] | Positive | The put gains when DVOL rises (typically in a selloff) — a second crash payoff that lets the put be monetized on a vol spike before it is deeply ITM |

Convexity plus the vega-spike payoff are why a protective put beats an equivalent static coin reduction *only* in fast, deep, vol-expanding declines. In a slow grind lower with stable IV, theta dominates and the put underperforms simple de-risking — the crypto version of Israelov's "pathetic protection" critique.

## Market view / when to use

- **Concentrated position** (>15-20% of net worth in one coin) you cannot diversify (miner/treasury/insider/locked).
- A **known catalyst** — unlock, FOMC, election, or exchange-risk event — over a defined window.
- A **hard liquidity deadline** where a drawdown would be devastating.
- **Low-DVOL environments** where protection is cheap.

Least attractive when DVOL is elevated (puts expensive) and when the holder has a long horizon and can tolerate interim drawdowns — then holding fewer coins is cheaper.

## Adjustments & management

- **Monetize on spikes:** if a selloff drives the put delta beyond ~−0.60 with elevated DVOL, sell the put (or roll it down) to harvest convexity — riding an ITM put back up in a recovery gives the gains back.
- **Roll at ~30 DTE** if continuous protection is required, resetting the strike to the target OTM distance.
- **Stop paying when the catalyst passes** — do not roll a one-off catalyst hedge "just in case."
- **Sizing / budget:** full hedge = one put per unit of coin; partial hedges (50-75%) cut cost. Cap systematic hedging spend at **≤2% of NAV per year**; if the desired protection costs more, widen the deductible or hedge fewer coins.

## Crypto specifics

- **Hedging spot BTC/ETH or via Deribit.** Long spot + Deribit put is the standard build; ETF puts hedge an ETF holding; on-chain, some vaults offer put-protection wrappers.
- **Cash settlement, no early assignment.** Deribit puts are European, cash-settled — a put finishing ITM pays cash (strike − index), offsetting the spot loss while you **keep the coins** (and any staked position). Nothing is delivered; there is no early [[assignment]]. (BTC-ETF puts are American-style, physically settled — different mechanics.)
- **Inverse vs linear settlement.** USDC-margined puts give a clean USD floor; coin-margined (inverse) puts pay in coin and are non-linear in USD.
- **DVOL makes insurance expensive.** Crypto IV runs far above equity IV, so the premium drag is heavier — the OTM-deductible tradeoff and the ≤2%-of-NAV budget matter even more than in equities.
- **Fatter tail raises the payoff — sometimes.** Crypto's genuinely fatter left tail (2020-03, LUNA, FTX, 2025-10-10) means the convexity pays off in the specific fast-gap scenarios the put is built for; but the same fat tail is priced into DVOL, so you pay up front.
- **24/7 gap risk.** No session close — a devastating move can arrive at any hour or over a weekend, which is exactly the path-independent-floor benefit of a put over a mental stop.
- **No [[section-1256-contracts|§1256]].** Ordinary treatment; put cost and monetization are ordinary capital events (no 60/40 shelter).
- **Perp/staking interaction.** Shorting the [[funding-rate|perp]] is a cheaper "hedge" but caps upside (a synthetic reduction) and pays/collects funding — the put preserves full upside. On staked ETH, the put floors price while **staking yield** keeps accruing on the (possibly locked) coin.

## Risks

- **Premium bleed compounding:** the most common failure is slow death — years of 2-5%+ annual drag in rising markets, then abandonment at the first real drawdown.
- **Buying insurance after the fire starts:** initiating after a DVOL spike locks in the most expensive protection.
- **Path / roll mismatch:** a market that falls a few percent per month, each put expiring just OTM, produces large losses with near-zero hedge payoff.
- **Failure to monetize** an ITM put through a V-recovery.
- **Coin-margined non-linearity** if inverse puts are used.
- **Behavioral abandonment:** insurance that "never pays" gets cancelled — often a cycle before it would have paid.

## Worked crypto example

**Setup (illustrative).** A fund holds 20 ETH at $3,050 (a concentrated sleeve) and wants 3-month protection through an unlock window without selling.

- **Buy** 20 × $2,750 puts (90 DTE, ~10% OTM) at ~$160 each → $3,200 total (5.2% of the $61,000 position for 3 months)

| Outcome | Net effect |
|---|---|
| ETH to $2,200 | Put pays (2,750 − 2,200) × 20 = $11,000; spot loses $17,000 → net loss ≈ **−$9,200** (capped near (3,050−2,750+160)×20 = $9,200) |
| ETH at $3,050 | Put expires worthless → **−$3,200** (insurance cost) |
| ETH to $3,600 | Put worthless; spot gains $11,000 → net **+$7,800** (full upside minus premium) |

Below the $2,750 strike the loss is floored regardless of depth; the cost is the $3,200 premium and a $3,210 breakeven at $3,210.

## Getting the Data (CryptoDataAPI)

IV/DVOL and skew come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies vol-regime, funding, and liquidation context for cheap-insurance timing and tail detection.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (buy when compressed, not into a vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (left-tail early warning)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (leverage/skew read)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for floor/breakeven tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can automate the hedging cycle (put pricing stays on Deribit / [[greeks-live]]):

- **Cheap-insurance timing** — `GET /api/v1/volatility/regime` — initiate or roll only in `compressed`/`normal`; buying after a spike locks in the most expensive protection.
- **Monetization trigger** — `GET /api/v1/volatility/regime/score` + `GET /api/v1/market-intelligence/liquidations` — a score spike with cascades running is when the ITM put's intrinsic + vega should be harvested, not held through the V-recovery.
- **Budget check** — `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` tracks floor/breakeven against the ≤2%-of-NAV annual hedge budget.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) to replay roll schedules and deductible choices across the 2018/2020/2022 drawdowns; CDA holds no historical option premiums — cost series come from Deribit.
- **Tips** — a scheduled ~30-DTE roll check plus a score-threshold alert covers the whole management loop; `?format=markdown` keeps regime payloads compact for reasoning.

## Related

- [[married-put]] — the same structure bought together with a new position (protected entry)
- [[collar]] — offsets the put's cost by selling a call (caps upside)
- [[covered-call]] — the opposite posture (income for capped upside)
- [[hedging]] / [[tail-risk-hedging]] — the broader protection discipline; the deep-OTM tail variant
- [[variance-risk-premium]] — the structural cost the put buyer pays
- [[funding-rate]] — the perp-short alternative to a put floor
- [[staking]] — yield that continues while the coin is insured
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin-margined vs USDC-margined puts, DVOL
- Israelov, R. — "Pathetic Protection: The Elusive Benefits of Protective Puts" (AQR, 2017; *Journal of Alternative Investments*, 2019) — the monthly-rolled-puts-vs-de-risking critique that ports directly to crypto
- Carr, P. & Wu, L. (2009), "Variance Risk Premiums," *Review of Financial Studies* — the negative variance risk premium the put buyer pays (see [[variance-risk-premium]])
