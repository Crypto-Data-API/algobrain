---
title: "Iron Butterfly"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, mean-reversion, bitcoin, ethereum]
aliases: ["Iron Fly", "Ironfly", "Crypto Iron Butterfly", "ATM Iron Condor"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[crypto-options-volatility-selling]]", "[[iron-condor]]", "[[butterfly-spread]]", "[[short-strangle]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[variance-risk-premium]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Iron Butterfly

## Overview

The iron butterfly ("iron fly") is a **defined-risk, credit** options structure: a short ATM straddle wrapped in long OTM protective wings. You **sell 1 ATM call and 1 ATM put** at the same strike, then **buy 1 OTM call** above and **buy 1 OTM put** below to cap the tails. It collects a large credit and reaches maximum profit if the underlying pins the short strike at expiry. It is the highest-theta, highest-gamma member of the defined-risk [[crypto-options-volatility-selling|short-vol]] family — the most concentrated way to sell the [[variance-risk-premium]] in a capped-risk wrapper.

Relative to the [[iron-condor]], the iron fly has a **tighter profit zone but a much richer credit** because the short strikes are at-the-money (peak extrinsic value) rather than OTM. On [[deribit]] BTC/ETH it is a bet that realized volatility over the holding period undershoots the DVOL (Deribit's 30-day implied-vol index) priced into the ATM straddle — attractive when DVOL is elevated, dangerous into a trend or a vol shock because the body's gamma is unforgiving.

## Construction

Four legs, one expiry, cash-settled to the Deribit index:

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Sell 1 call | ATM (nearest spot) | short straddle body |
| 2 | Sell 1 put | ATM (same strike) | short straddle body |
| 3 | Buy 1 call | OTM above, one wing width up | upper protective wing |
| 4 | Buy 1 put | OTM below, same width down | lower protective wing |

- **Strike selection:** body at the strike nearest spot; balanced wings equidistant from the body (equal wing width up and down).
- **Ratios:** 1:1:1:1.
- **Net credit** = (short call + short put) − (long call + long put). Target a credit **50-75% of the wing width** — much higher credit-to-width than a condor's 25-35%. (With balanced wings the credit is always *less* than the wing width; a credit exceeding the width would be a risk-free arbitrage and does not occur.)
- **Tenor:** 21-45 DTE. Shorter maximizes theta but concentrates the body's gamma; never carry ATM shorts into crypto's continuous expiry-week gamma.

## Payoff & breakevens

- **Max profit** = net credit, only on a near-perfect pin at the ATM short strike at expiry.
- **Max loss** = wing width − net credit, at or beyond either wing.
- **Upper breakeven** = short strike + net credit.
- **Lower breakeven** = short strike − net credit.

The payoff is a sharp **tent**: a single peak at the body, sloping linearly to two capped-loss floors at the wings. The breakevens sit well *inside* one expected move, which is why breakeven touches are frequent and the body's gamma dominates the P&L path.

## Greeks profile

- **Delta:** ~0 at entry; flips fast once spot leaves the body — the tent has steep sides.
- **Gamma:** **strongly negative** — the highest of the common short-premium structures. A modest adverse move re-marks a large fraction of the credit; near expiry the ATM gamma is violent. In 24/7 crypto this is a continuous exposure with no overnight cap.
- **Theta:** **strongly positive** — the richest per dollar at risk (~2× a same-width condor). It accelerates sharply inside ~21 DTE.
- **Vega:** **negative** — a large share of early P&L is DVOL crush rather than raw theta; a DVOL spike marks the short body to a loss before expiry.

## Market view / when to use

- You expect BTC/ETH to **pin or barely move** around the current price through expiry.
- **DVOL is elevated** (rich ATM straddle to sell), roughly the 40th-90th percentile — the higher DVOL is, the richer the body.
- **VRP confirmation:** DVOL − 30-day realized vol comfortably positive; the whole thesis is realized < implied.
- You want **maximum credit per trade** in a defined-risk wrapper and will accept the low probability of the perfect pin.
- Post-shock, vol-mean-reverting tape (high DVOL, range-bound) is the ideal regime.

## Adjustments & management

- **Profit target:** close at **25-50% of max credit** — do *not* chase the perfect pin. The body's gamma means realized P&L deteriorates fast past the easy-money zone.
- **Time stop:** manage/close at ~21 DTE; **hard exit by 7-10 DTE** if spot is near a wing — never carry ATM shorts into expiry-week gamma.
- **Stop-loss:** cut if the loss reaches ~1.5× the credit (or define max loss = wing width − credit and accept it).
- **Convert to an [[iron-condor]]:** if spot drifts off the body with time remaining, buy back the tested ATM leg and sell a new OTM option to widen the zone into a condor.
- **Vol-shock kill:** flatten if DVOL rises **> 50% in a session** — the short ATM gamma is the canonical crash exposure.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] BTC/ETH only. ATM strikes are the most liquid on the chain, which helps fills — but the four-leg structure still crosses multiple spreads. **Alt options lack the ATM depth** to fly cleanly.
- **Inverse vs linear/USDC settlement:** strongly prefer **USDC-margined (linear)** options — the tent's breakevens and max loss are clean USD numbers. Inverse (coin-margined) options warp the symmetric tent because collateral value moves with spot; the "pin" strike in coin terms drifts against you.
- **DVOL regime gate:** sell the fly only inside the ~40th-90th DVOL percentile band; below that the ATM credit is too thin to pay for the gamma, above it you are selling into a shock. The fly is the **most DVOL-sensitive** short structure — a DVOL spike hurts most here.
- **24/7 & weekend gaps:** the body's gamma is a continuous liability — a weekend gap through a breakeven at 03:00 UTC cannot be managed until you wake. This is why the wings (defined risk) and the mechanical 7-10 DTE exit are non-negotiable in crypto. Expiry is **08:00 UTC**, cash-settled to the Deribit index: settling *at* the body is the **max-profit** outcome, and there is **no assignment/pin-risk** the way US single-stock flies carry — a genuine advantage.
- **No [[section-1256-contracts|§1256]]:** the rich credit is taxed as ordinary capital gains on offshore Deribit — no 60/40 US shelter; the after-tax net is well below an SPX fly's.
- **Perp funding interaction:** funding-driven skew shifts the *effective* ATM richness — richly positive [[funding-rate|funding]] fattens call-side vol; you can bias the body slightly or lean the wings toward the overbid side.
- **Fees:** four legs in and four out — up to eight crossings per round trip; the 0.03%/12.5%-of-premium cap bites on the cheap long wings.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **55** (elevated); expecting a quiet range. 35 DTE. Wings **$400** wide ($2,600 / $3,000 / $3,400).

**Trade (per 1-ETH contract):**
- Sell $3,000 call for **$210**.
- Sell $3,000 put for **$200**.
- Buy $3,400 call for **$70** (upper wing).
- Buy $2,600 put for **$85** (lower wing).
- **Net credit = ($210 + $200) − ($70 + $85) = $255.** Wing width = $400. Credit-to-width = **64%**.
- **Max profit = $255** on a $3,000 pin. **Max loss = $400 − $255 = $145** at or beyond a wing.
- **Breakevens:** $3,000 + $255 = **$3,255**; $3,000 − $255 = **$2,745**.

Payoff at expiration:

| ETH at expiry | Short straddle value | Net cost to close | P&L (per contract) |
|---|---|---|---|
| ≤ $2,600 | $400 | $400 | −$145 (max loss) |
| $2,745 | $255 | $255 | $0 (lower breakeven) |
| $3,000 | $0 | $0 | +$255 (max profit, perfect pin) |
| $3,150 | $150 | $150 | +$105 |
| $3,255 | $255 | $255 | $0 (upper breakeven) |
| ≥ $3,400 | $400 | $400 | −$145 (max loss) |

**Management in practice:** with ETH near $3,050 a few days in and DVOL crushing 55 → 48, the fly might mark ~$120 to close — capturing ~53% of max. Close it; do not carry the ATM gamma into the final week hoping for the exact pin.

## Sources

- [[greeks-live]] / [[deribit]] documentation — DVOL construction, IV surface, USDC-margined vs inverse settlement, 08:00 UTC cash settlement (body pin = max profit, no assignment), taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on the iron fly's gamma profile and the body-vs-wings relationship (mechanics port to crypto).
- [[variance-risk-premium]] — the structural source of the edge; ATM strikes carry the richest premium on the chain.
- tastytrade iron-fly management studies (25%-of-max-profit, 21-DTE) — port directly; the exits must be enforced harder given crypto gamma.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the complementary options-flow, volatility-regime, dealer-gamma, and funding context used to time the fly.

**Live:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (where the market is likely to pin — directly relevant to an ATM-bodied fly)
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate (sell only when elevated, not vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure; long-dealer-gamma regimes dampen spot and favor a pin
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the vol shock that breaks the body

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

## Related

- [[crypto-options-volatility-selling]] — the parent short-vol book
- [[iron-condor]] — the wider, lower-credit, lower-gamma cousin
- [[butterfly-spread]] — the debit version of the same tent payoff
- [[short-strangle]] — the iron fly is the defined-risk version of a short ATM straddle
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]], [[variance-risk-premium]] — the vol inputs and the edge
- [[funding-rate]], [[gamma-exposure]], [[max-pain]] — positioning and pin context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that define this structure
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
