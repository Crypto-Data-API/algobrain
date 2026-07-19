---
title: "Collar (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, hedging, collar, defined-risk, risk-management, derivatives, bitcoin, ethereum]
aliases: ["Zero-Cost Collar", "Protective Collar", "Collar Strategy", "Crypto Collar", "collar-strategy"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[protective-put]]", "[[married-put]]", "[[covered-call]]", "[[risk-reversal]]", "[[synthetic-long]]", "[[hedging]]", "[[tail-risk-hedging]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[staking]]", "[[delta]]", "[[trade-repair-and-rolling]]", "[[cryptodataapi]]"]
---

# Collar (Crypto)

## Overview

The collar combines a long spot [[bitcoin|BTC]]/[[ethereum|ETH]] position with a purchased OTM [[put-option|put]] (a floor on losses) and a sold OTM [[call-option|call]] (a cap on gains that funds the put). When the call premium equals the put premium the hedge is a **zero-cost collar**. The result is a bounded risk/reward profile that protects existing coin gains without a net cash outlay — the crypto analogue of the equity executive's concentrated-stock hedge, used here by long-term holders, miners, treasuries, and DAOs to ride out uncertain windows while keeping their coins.

Structurally the collar is a [[protective-put|protective put]] (downside insurance) plus a [[covered-call|covered call]] (income/upside cap): the call finances the put, capping gains at the call strike and flooring losses at the put strike. In crypto the skew that governs the cap-versus-floor tradeoff is not the static put-skew of equities — it swings with [[funding-rate|perp funding]] and can even invert to call-skew in leveraged bull runs, which sometimes lets a zero-cost crypto collar be struck on unusually favorable terms.

## Construction

1. **Hold** spot BTC/ETH (or a BTC-ETF position).
2. **Buy 1 OTM put** ~5-15% below spot on [[deribit]] → sets the floor.
3. **Sell 1 OTM call** ~5-15% above spot → premium funds the put. Adjust strikes until the net premium ≈ 0 for a zero-cost collar.
4. Both legs **same expiration**, 30-90 DTE; match the tenor to the risk window (a macro event, unlock, or halving aftermath).

Prefer **USDC-margined (linear)** legs for a clean USD floor/cap; coin-margined (inverse) legs introduce quanto-like non-linearity in the hedge.

## Payoff & breakevens

| Scenario | Outcome |
|---|---|
| Spot below put strike | Loss floored at (put strike − spot entry) ± net premium |
| Spot between strikes | Coins retained; small net debit/credit |
| Spot above call strike | Upside capped at the call strike ± net premium |

- **Max profit** = call strike − spot entry + net credit (if any)
- **Max loss** = spot entry − put strike + net debit (if any)

## Greeks profile

Net of the three legs (long coin, long put, short call):

| Greek | Sign | Note |
|---|---|---|
| [[delta]] | Positive, reduced | Long coin, trimmed by the long put and short call; flattest between the strikes |
| [[gamma]] | Near-flat to slightly negative | Long-put gamma partly offsets short-call gamma |
| [[theta]] | Small (put decay vs call decay net) | The put bleeds; the sold call's decay largely offsets it |
| [[vega]] | Roughly neutral | Long put vega vs short call vega — the collar is far less vega-sensitive than an outright put or covered call |

The near-vega-neutrality is a feature: the collar is a directional-risk truncation, not a volatility bet.

## Market view / when to use

- You hold coins with **significant unrealized gains** and want protection through a defined uncertain window (macro print, election, major unlock, exchange-solvency scare).
- You are willing to **sacrifice upside** to eliminate downside tail risk at near-zero cash cost.
- **Concentrated exposure:** miners, treasuries, DAOs, early holders, or founders with an outsized single-coin allocation who cannot or will not sell.
- Approaching a **liquidity event** (token vesting cliff, planned sale) where a drawdown would be damaging.

## Adjustments & management

- **Roll up** the put (and call) after a rally to lock in more of the gain.
- **Roll out** in time to extend protection through a longer window.
- **Near the call strike:** decide to accept the cap (cash settlement on Deribit — you keep the coin and pay the cap) or roll the call up-and-out for a debit to free upside.
- **Adjust width:** widen for more room (more risk), narrow for tighter protection (a steep-skew regime may force a narrow band).
- Remove the collar once the catalyst passes if you want full upside back.

## Crypto specifics

- **Hedging spot BTC/ETH or via Deribit.** Long spot + Deribit put + Deribit short call is the standard build; BTC-ETF options can collar an ETF holding.
- **Cash settlement, no early assignment.** Deribit's European options settle in cash: the cap and floor are realized as cash payments at expiry — **you keep your coins** (and any staked position) rather than having them called away or delivered. No early [[assignment]] risk on either leg.
- **Inverse vs linear settlement.** USDC-margined legs give a clean USD floor and cap; coin-margined (inverse) legs make both the collateral and the hedge payoff move with spot (quanto-like), muddying the floor.
- **Skew swings with funding — the crypto twist.** Equity collars are dear on the put side (persistent put skew). Crypto skew oscillates: in richly positive [[funding-rate|funding]] (leveraged-long) regimes, call skew can trade rich to puts, so the sold call finances the put unusually well — a favorable zero-cost collar. After a crash, put skew dominates and the cap must sit closer to spot. Read the 25-delta [[risk-reversal]] before striking the collar.
- **24/7 gap risk makes the floor valuable.** Weekend and overnight gaps (there is no market close) are exactly what the put floor protects against — a stronger case for collaring crypto than equities.
- **No [[section-1256-contracts|§1256]].** No 60/40 treatment; cap-assignment and put settlement are ordinary capital events.
- **Staking-yield interaction.** A collar on staked/liquid-staked ETH lets you keep earning **staking yield** while bounding price risk; cash settlement means the (possibly locked) staked ETH never needs delivery.

## Risks

- **Capped upside** — the dominant long-run cost; repeatedly capping underperforms unhedged holding in crypto's big rallies.
- **Skew cost** — a steep post-crash put skew forces an uncomfortably tight cap to stay zero-cost.
- **No alpha** — a risk-transfer, not a return edge; expected return falls with volatility.
- **Mismatched expiration** — protection expiring before the risk window leaves you unhedged at the worst moment.
- **Coin-margined non-linearity** if inverse legs are used.
- **Venue concentration** on Deribit during a vol event.

## Worked crypto example

**Setup (illustrative).** Hold 5 BTC bought at $52,000, now $68,000 — a $16,000/BTC unrealized gain to protect through a 45-day macro window. BTC DVOL moderate; funding mildly positive (call skew firm).

- **Buy** 5 × $61,000 puts (45 DTE) at ~$2,000 each
- **Sell** 5 × $78,000 calls (45 DTE) at ~$2,000 each → **net ≈ $0 (zero-cost collar)**

| Outcome at expiry | P&L per BTC |
|---|---|
| BTC to $45,000 | Put floors at $61,000 → **+$9,000** (vs −$7,000 unhedged) |
| BTC at $68,000 | Both expire worthless → **+$16,000** |
| BTC to $85,000 | Capped at $78,000 → **+$26,000** (forgo the move above $78k) |

The collar guarantees keeping at least $9,000 of the $16,000 gain per BTC, at the cost of capping the upside at $26,000.

## Getting the Data (CryptoDataAPI)

IV/DVOL and the 25-delta [[risk-reversal|risk reversal]] (skew) come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the funding, regime, and flow context for striking and rolling the collar.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (the crypto skew driver; positive funding → richer sold call)
- `GET /api/v1/volatility/regime` — per-asset vol regime for timing the hedge
- `GET /api/v1/market-intelligence/options` — BTC options OI / [[max-pain]] for strike context
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (tail-risk early warning the floor guards against)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for strike/floor tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL and skew from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — strike the collar off `GET /api/v1/derivatives/funding-rates?coin=BTC` (positive funding richens the sold call, tightening the zero-cost cap) with `GET /api/v1/market-intelligence/options` max pain/OI walls locating natural cap and floor strikes
- **Regime gate** — `GET /api/v1/quant/market`: rising `strong_trend_bear`/`vol_spike` probability argues for collaring *now*; `GET /api/v1/volatility/regime` reading `compressed` makes the bought put cheap — the best moment to add the floor
- **Backtest** — replay floor/cap outcomes per roll cycle on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); validate hedge-timing rules against point-in-time regimes in `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — a collar is maintenance-light: fold checks into an hourly cached `GET /api/v1/daily` poll and act only at roll dates or on a `/api/v1/market-intelligence/liquidations` tail event that tests the floor.

## Related

- [[protective-put]] — the downside-only leg (floor without the cap)
- [[married-put]] — long coin + long put established together
- [[covered-call]] — the upside-cap-for-income leg (cap without the floor)
- [[risk-reversal]] — the options-only analogue and the skew gauge for striking the collar
- [[synthetic-long]] — the collar's cousin without the stock leg's insurance
- [[hedging]] / [[tail-risk-hedging]] — the broader protection discipline
- [[funding-rate]] — the perp linkage that shapes crypto skew and collar economics
- [[staking]] — stackable yield while collared
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin-margined vs USDC-margined legs, DVOL and 25-delta risk reversal (skew)
- [[crypto-options-volatility-selling]] — how funding-driven crypto skew differs from static equity put skew
