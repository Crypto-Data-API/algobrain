---
title: "Seagull Option"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, seagull, hedging, directional, three-leg, low-cost, skew]
aliases: ["Seagull Spread", "Bullish Seagull", "Bearish Seagull", "Crypto Seagull"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[risk-reversal]]", "[[collar]]", "[[iron-condor]]", "[[covered-call]]", "[[butterfly-spread]]", "[[jade-lizard]]", "[[skew-trading]]", "[[implied-volatility]]", "[[funding-rate]]", "[[delta]]", "[[deribit]]", "[[greeks-live]]", "[[cryptodataapi]]"]
---

# Seagull Option

## Overview

The **seagull** is a **three-leg** structure that provides **cheap directional exposure or protection** with an asymmetric, three-strike payoff (the wings-and-body shape that gives it the name). A **bullish seagull** is a call spread (buy lower call, sell higher call) plus a **short put**; a **bearish seagull** is a put spread (buy higher put, sell lower put) plus a **short call**. The short option finances the spread, typically creating a **zero-cost or near-zero-cost** structure with a **capped** favourable move and a **naked-leg tail** on the opposite side. It is the natural extension of the [[risk-reversal]]: take a risk reversal and *cap* the long wing into a spread, cheapening it enough to self-finance. In crypto it fits two roles — cheap leveraged directional bets on [[deribit]] BTC/ETH, and low-cost hedging of a spot bag or a corporate/fund **BTC/ETH treasury**.

## Construction

Three OTM legs, same expiry `T`, on Deribit BTC/ETH:

- **Bullish seagull** — buy 1 call (strike `A > S`), sell 1 further-OTM call (strike `B > A`), sell 1 OTM put (strike `C < S`). The call spread `A→B` is the payoff; the short put `C` funds it.
- **Bearish seagull** — buy 1 put (strike `A < S`), sell 1 further-OTM put (strike `B < A`), sell 1 OTM call (strike `C > S`). The put spread `A→B` is the payoff; the short call `C` funds it.
- **Zero-cost tuning**: set the strikes so the short-wing credit ≈ the spread's debit. Strikes are commonly placed at delta targets (e.g. buy 25-delta, sell 10-delta wing, sell 25-delta funding leg).

Deribit contracts are 1 BTC / 1 ETH, **European-exercise and cash-settled** (no early assignment). Tenor 30–90 DTE for hedging, 21–45 for speculation. USDC-margined (linear) gives clean USD P&L; inverse (coin-margined) embeds a coin delta on the short-wing collateral.

## Payoff & breakevens

Bullish seagull, with spread width `W = B − A`:

- **Above `B`**: **max profit = `W`** (± net credit) — capped by the short call.
- **Between `A` and `B`**: profit rises from ~0 to `W`.
- **Between `C` and `A`**: flat, P&L ≈ net credit/debit (the "dead zone").
- **Below `C`**: **loss grows ~1:1 with spot** (the short put) — the naked tail.
- **Breakevens**: near `A + |debit|` on the upside; near `C − credit` on the downside.
- **Max loss**: essentially the full downside below `C` (short put to zero), minus any credit.

The bearish seagull is the mirror: capped profit as spot falls into the `A→B` put spread, flat dead zone, and a naked short-call tail on a rally above `C`.

## Greeks profile

A seagull is a directional/skew structure with capped convexity on the payoff side:

| Greek | Bullish seagull | Comment |
|---|---|---|
| [[delta]] | **Positive** | Synthetic-long lean, capped above `B` |
| Gamma | Small, mixed | Long-spread gamma partly offsets short-put gamma; flips sign near strikes |
| [[vega]] | Small, **short skew** | Net short the funding wing's vega; sensitive to the put-vs-call skew like a risk reversal |
| [[theta]] | Small, sign per net credit/debit | A credit seagull collects small theta |

Like the [[risk-reversal]], the dominant secondary exposure is **skew** — a bullish seagull is short put-skew (it sold the put) and long a capped slice of call-skew.

## Market view / when to use

- **Cheap capped directional bet.** You expect a move toward `A→B` but want to pay little or nothing — you accept the capped upside and the tail on the funding side. Bullish seagull for an up-move you are willing to buy dips into; bearish seagull for a down-move you are willing to short rallies into.
- **Hedging a crypto treasury.** A fund or company holding spot BTC/ETH can buy downside protection **for free** with a bearish seagull: buy a protective put spread, finance it by selling an upside call (giving up gains above `C`). This is the crypto analogue of the corporate FX seagull and a cheaper cousin of the [[collar]] (the put *spread* costs less than an outright put, at the cost of a protection floor).
- **Skew harvest with a cap.** When one wing is richly bid (funding-driven crypto skew — see [[skew-trading]]), sell it as the funding leg and take the cheaper capped spread on the other side.

## Adjustments & management

- **Manage the naked funding leg** — the whole risk lives there. Buy it back or roll it away-and-out if spot approaches it; this is the crypto weekend-gap hazard.
- **Take the capped gain** — once spot pushes past `B`, the profit is maxed; close to free capital and remove the short-wing risk.
- **Widen or narrow the spread** to trade off cost vs payoff: a wider `A→B` needs more funding (a closer/riskier short wing).
- **Convert a hedge as exposure rolls off** — for a treasury hedge, unwind when the spot exposure is realized or the thesis changes.
- **Delta-hedge on the perp** if you only want the skew slice; the hedge pays/collects [[funding-rate|funding]].

## Crypto specifics

- **Venue & underlyings**: [[deribit]] BTC/ETH; [[greeks-live]] for the three-leg Greeks and skew. Alt seagulls are impractical (thin, wide chains).
- **Skew-driven funding leg.** Which wing self-finances best depends on crypto skew, which flips with [[funding-rate|perp funding]]: richly positive funding firms call skew (a bearish seagull's short call funds richly); post-crash put skew firms (a bullish seagull's short put funds richly). Read funding before placing the funding leg.
- **Inverse vs linear settlement.** On inverse (coin-margined) contracts the short wing's exposure and collateral are both in the coin — a double hit on a wrong-way move; **USDC-margined (linear)** keeps it clean.
- **European, cash-settled → no early assignment**, but the naked funding leg still carries full undefined tail risk to the index at expiry.
- **24/7 & weekend gaps.** The short funding leg can be blown through by an unbounded weekend gap with no chance to trade out — size it for a Black-Thursday move (2020-03-12, 2025-10-10), not an average session.
- **No §1256.** Offshore Deribit contracts get no [[section-1256-contracts|§1256]] 60/40 treatment — relevant for corporate/treasury hedgers weighing after-tax cost.
- **Treasury use is real in crypto.** Corporate and fund BTC/ETH treasuries make the "free downside protection" bearish seagull a genuine institutional use case, replacing the FX-exporter role it plays in traditional markets.

## Risks

- **Naked funding-leg tail** — the defining risk; loss grows 1:1 with spot beyond the short wing, and crypto gaps are unbounded.
- **Capped payoff** — the favourable move is limited to the spread width, unlike an outright long option or a plain [[risk-reversal]].
- **Not truly free** — "zero cost" hides meaningful directional risk in the sold wing.
- **Three-leg slippage** — wider aggregate bid-ask across three Deribit legs; work the order or use an RFQ / block.
- **Skew regime shift** — the wing you sold can richen before it reverts.
- **Coin-margin wrong-way risk** on inverse contracts.

## Worked crypto example

**Setup (ETH, 60 DTE, bullish, willing to accumulate on a dip).** ETH spot **$3,000**. You want cheap, capped upside and are happy to buy ETH if it falls to $2,600.

**Trade — bullish seagull (USDC-margined):**
- **Buy** 1 ETH **3,200 call** @ **$180**
- **Sell** 1 ETH **3,800 call** @ **$70** (caps the upside; `W = $600`)
- **Sell** 1 ETH **2,600 put** @ **$110** (funds the spread)
- **Net cost = 180 − 70 − 110 ≈ $0** (zero-cost).

**Path A — rally into the cap (the target).** ETH to **$3,800+**. The call spread is worth its full **$600**; short put expires worthless. **Profit ≈ +$600** on ~zero capital.

**Path B — partial rally.** ETH to **$3,500**. Call spread worth ≈ $300, short put worthless → **profit ≈ +$300**.

**Path C — dead zone.** ETH finishes at **$2,900** (between $2,600 and $3,200). All legs expire worthless → **P&L ≈ $0**.

**Path D — crash (the tail).** ETH gaps to **$2,300** over a weekend. The short 2,600 put is ≈ $300 ITM → **loss ≈ −$300**, growing the further ETH falls — exactly as if you had been long spot below $2,600 (which was the intent: accumulate on the dip, but sized for the gap).

## Getting the Data (CryptoDataAPI)

The **skew** that decides which wing self-finances a seagull — the 25-delta risk-reversal number and the IV surface — is a **Deribit / [[greeks-live]]** product, *not* served by CryptoDataAPI. [[cryptodataapi]] supplies the drivers and context: funding (the skew driver), options OI/max-pain, dealer gamma, and vol regime.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding; sets which wing is rich to sell as the funding leg
- `GET /api/v1/derivatives/open-interest?coin=BTC` — perp OI (crowded-positioning context)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] strike
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory / cascade risk into the short wing)
- `GET /api/v1/volatility/regime` — vol regime (context for wing pricing)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history (skew-driver backtest)
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]]

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the seagull's decision loop end-to-end (wing pricing and skew stay on Deribit / [[greeks-live]]):

- **Funding-leg selection** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — sell whichever wing funding says is rich: positive funding firms call skew (a bearish seagull's short call funds well), post-crash put skew funds the bullish build.
- **Naked-leg watch** — `GET /api/v1/quant/gex` + `GET /api/v1/derivatives/open-interest?coin=BTC` — dealer gamma and crowded positioning flag cascade risk into the short funding leg; size it for a Black-Thursday gap, not an average session.
- **Regime gate** — `GET /api/v1/volatility/regime` — do not initiate the naked wing in `vol_shock`.
- **Backtest** — `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` plus `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05) for the skew-driver history; `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) for how often spot breaches the funding-leg strike within tenor.
- **Tips** — automate a spot-vs-short-wing distance alert; the whole risk of a "zero-cost" seagull lives in that one leg.

## Related

- [[risk-reversal]] — the two-leg parent (seagull caps its long wing into a spread)
- [[collar]] — related spot-hedging structure; the seagull is its put-spread, self-funded cousin
- [[iron-condor]] — defined risk on both sides for range-bound markets
- [[butterfly-spread]] — another low-cost structure for a price target
- [[jade-lizard]] — short put + call spread, a related credit structure
- [[skew-trading]] — choosing which wing to sell as the funding leg
- [[funding-rate]] — the perp linkage that flips crypto skew
- [[deribit]], [[greeks-live]] — venue and skew/surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — three-leg combination structures and their risk.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — skew-financed structures and wing selection.
- [[deribit]] / [[greeks-live]] documentation — European cash settlement, contract specs, inverse vs USDC-margined contracts, 25-delta skew quoting.
