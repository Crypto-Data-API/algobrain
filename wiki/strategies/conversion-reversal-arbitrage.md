---
title: "Conversion & Reversal Arbitrage"
type: strategy
created: 2026-04-15
updated: 2026-07-14
status: good
tags: [arbitrage, options, crypto, derivatives, market-microstructure, bitcoin, ethereum]
aliases: ["Conversion Reversal Arbitrage", "Conversion Arbitrage", "Reversal Arbitrage", "Synthetic Arbitrage", "Crypto Conversion Reversal"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[put-call-parity]]", "[[box-spread]]", "[[volatility-arbitrage]]", "[[cash-and-carry]]", "[[basis-trade]]", "[[deribit]]", "[[greeks-live]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[delta-neutral]]", "[[dvol]]", "[[skew]]", "[[section-1256-contracts]]", "[[leg-risk]]", "[[cryptodataapi]]"]
---

# Conversion & Reversal Arbitrage

## Overview

Conversion and reversal arbitrage exploit violations of **[[put-call-parity]]** — the no-arbitrage relationship linking a call, a put at the same strike/expiry, and the underlying's forward. When one leg drifts out of line, an arbitrageur builds a **delta-neutral synthetic** that offsets the mispriced leg and locks the difference. These are among the **purest structural arbitrages**: no forecast, no risk premium harvested, just the mechanical constraint that the synthetic and the real position must cost the same.

In crypto these run on [[deribit]] BTC/ETH options against Deribit **perpetual or dated futures** as the hedge leg (you cannot cheaply borrow-and-short spot coin the way you short equities). Two crypto facts reshape the trade versus equities: Deribit options are **European and cash-settled**, so there is **no early-exercise risk** — the single largest risk of equity conversions/reversals disappears; and crypto pays **no dividends**, so the dividend term drops out of parity entirely. What replaces the equity "interest − borrow − dividends" carry stack is a single clean term — the **futures basis / [[funding-rate|perp funding]]** — which *is* crypto's synthetic financing rate. The edge is real but structurally thin and latency-dominated: violations are small and fleeting, captured almost entirely by market-maker and prop desks running them continuously.

## Construction

The identity (European options, no dividends, forward `F` = the Deribit future for that expiry):

```
C − P = (F − K) · e^(−rT)

C = call price, P = put price, F = forward/futures price,
K = strike, r = USDC financing rate, T = time to expiry
```

When the executable market diverges from this, a conversion or reversal captures it.

**Conversion (synthetic short offset by a long future):**

| Leg | Position | Purpose |
|---|---|---|
| Buy future | Long 1 BTC/ETH future (or perp) | real long exposure |
| Buy put | Long 1 put (same `K`, same expiry) | + |
| Sell call | Short 1 call (same `K`, same expiry) | = synthetic short |

Delta-neutral; locked P&L ≈ `(C − P) − (F − K)` (discounting aside). Profitable when the synthetic short is **rich** to the future.

**Reversal (synthetic long offset by a short future):** the mirror — short future, long call, short put. Locked P&L ≈ `(F − K) − (C − P)`; profitable when the synthetic long is **cheap** to the future.

A **[[box-spread]]** = a conversion at `K1` + a reversal at `K2`. All directional exposure cancels and there is no future leg left — a pure lending/borrowing instrument whose payoff equals the strike width and whose implied yield **is** crypto's synthetic risk-free (USDC financing) rate.

## Payoff & breakevens

There is no tent-shaped payoff — the P&L is **locked at entry** and does not depend on where spot finishes:

- **Locked profit** = the captured parity violation net of all frictions, realised at the **08:00 UTC** cash settlement.
- **No directional breakevens:** a conversion's long future gains exactly offset its synthetic-short losses (and vice versa) at every price. The only "breakeven" is economic — the violation must exceed total costs.
- **Max loss scenario:** not a market move but an *operational* one — a bad fill on one leg (leg risk), the basis moving against you between legs, or an inverse-settlement mismodel. Correctly executed and held to European cash settlement, the position converges to its locked value regardless of the underlying's path.

## Greeks profile

- **[[delta]]:** ≈ 0 by construction — the synthetic and the future cancel. This is a [[delta-neutral]] structure with no directional stance.
- **[[gamma]], [[vega]], [[theta]]:** all ≈ 0 net at the same strike/expiry — the long and short option legs offset. The position is **not** a vol trade; [[dvol|DVOL]] moves do not drive it (they only affect the *size* of the parity gap you can find).
- **Residual exposure is rate/basis, not Greeks:** the real risk factor is the **futures basis / funding** carry to expiry and, on inverse contracts, the quanto curvature — not any option Greek.

## Market view / when to use

- **No market view at all** — this is a relative-value / financing trade, not a directional or vol bet. You run it whenever an executable parity violation exceeds costs.
- **Who is on the other side:** whoever created the dislocation — a large directional buyer lifting one option, a forced liquidation dumping a leg, a market maker skewing quotes to manage inventory, or retail routed at a stale price. They are paying for immediacy; the conversion/reversal desk supplies it.
- **Why it is structurally thin:** the relationship is mechanical and monitored by many automated systems, so violations are tiny (typically **~0.05-0.3% of notional** in crypto — wider than equities because financing is messier and books are thinner, but still fleeting). A "fat" violation almost always means an un-modeled cost (basis, inverse quanto, funding spike) masquerading as profit. **If it looks too good, you are missing a cost.**
- **Practically a market-maker / prop strategy:** it needs low latency, cheap USDC financing, and near-simultaneous multi-leg execution — barriers that keep it from being fully arbitraged away but also capture almost all of it for professionals.

## Adjustments & management

- **Hold to expiry:** the profit is locked at entry; the position converges at the 08:00 UTC cash settlement. There is no active exit decision in the base case.
- **Leg sequencing:** fill the **hardest leg first** — usually the less-liquid option strike — then hedge with the future, which is the deepest, tightest book. Never leg into the future first and hope the option fills.
- **Exit early only if** the funding/basis regime flips hard against a perp-hedged build (see Risks) or you can close the whole package for more than the locked value net of costs.
- **Roll the hedge** if you built the long/short leg with a **perp** rather than a dated future — the perp must be carried and its funding managed until the option expiry.

## Crypto specifics

- **European cash settlement — no early-exercise risk:** Deribit options are European, cash-settled to the ~30-minute index TWAP at **08:00 UTC**. Neither leg can be assigned early, so the **biggest risk of equity conversions/reversals is gone** and the trade is genuinely closer to riskless. It also means the [[box-spread]] does **not** carry the American short-box blow-up risk (the 2019 equity "infinity squeeze") — a Deribit box is a clean synthetic-rate instrument.
- **No dividends:** crypto pays none, so the dividend term vanishes from parity — no ex-dividend early-exercise trap, no dividend-timing risk, no special-dividend surprise. (ETH staking yield is not passed through to Deribit's USDC-settled contracts, so it does not enter the parity either.)
- **Futures basis / [[funding-rate|perp funding]] IS the carry:** the equity "interest − borrow − dividends" stack collapses to one clean term. A conversion's long future **pays away** a contango basis; a reversal's short future **earns** it. On a perp-hedged build the carry is realised as **funding** paid/collected each interval. A steep contango basis can *make* a reversal profitable (the earned basis is the trade) or *kill* a conversion.
- **Inverse vs linear/USDC settlement:** on **USDC-margined (linear)** options and futures, parity is clean textbook. On **inverse (coin-margined)** contracts both the options and the future are BTC/ETH-settled and embed a **quanto-like curvature** — parity must be expressed in the inverse contract's own terms, and mismodeling it is a classic way to book a phantom "violation" that is really a coin-delta exposure. Prefer linear for a clean lock.
- **[[perpetual-futures|Perp]] vs dated future as the hedge:** a **dated future** locks the basis to expiry (cleanest); a **perp** is deeper but leaves you carrying variable funding until the option expires — a source of drift a dated future avoids.
- **24/7 & single-venue concentration:** continuous trading means dislocations can appear any hour, but also that Deribit is effectively the only deep venue — collateral and counterparty risk concentrate on one offshore exchange, an operational tail the equity version (multiple regulated venues) does not have.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US treatment** — the thin locked profit is ordinary/short-term (US) or trader-status-dependent (AU), which matters more here than elsewhere because the margins are so small.
- **Alt-option liquidity:** only BTC/ETH have the option depth *and* the matching future for a clean multi-leg lock — alt parity gaps look bigger precisely because they cannot be executed at size.

## Risks

- **Leg / execution risk:** the profit lives in a few tens of bps; a bad fill on the harder option leg, or the basis moving between legging the option and the future, can erase or invert it. See [[leg-risk]].
- **Inverse-quanto mismodel:** treating an inverse-settled violation as textbook parity books a hidden coin-delta as "arbitrage" profit.
- **Funding / basis drift (perp builds):** a funding spike after entry on a perp-hedged conversion/reversal erodes or reverses the locked carry before the option expires.
- **Settlement mismatch:** the option settles to Deribit's TWAP index while your future/perp hedge marks continuously — a small basis at the 08:00 UTC print is residual slippage.
- **Counterparty / venue risk:** single-exchange concentration (Deribit) — the dominant operational tail versus the multi-venue equity trade.
- **Cost floor:** commissions plus two option crossings plus the future leg; at retail latency and fees the honest expectancy is usually **negative** — this is a professional, low-cost-base strategy.

## Worked crypto example

**Reversal on Deribit (BTC, USDC-margined/linear), hypothetical.** Crash-hedgers have bid the ATM put, pushing the synthetic long *cheap* to the future.

- BTC spot **$60,000**; 30-day future **$60,290** (basis +$290 ≈ +0.5%/30d ≈ ~6% annualised — the earned carry).
- 30-day options at `K = $60,000`: call ask **$1,700**, put bid **$1,560**.
- Fair `C − P` = `(F − K)·e^{−rT}` ≈ $290 · 0.995 ≈ **$289**.
- Executable `C − P` for a reversal (buy call at ask, sell put at bid) = 1,700 − 1,560 = **$140** — the synthetic long costs $140 versus a fair ~$289, so it is **~$149 cheap**: do the reversal.

**Trade (per 1-BTC contract):**
1. Short 1 BTC 30-day future at $60,290 (locks the +$290 basis as it converges to settlement).
2. Buy 1 BTC $60,000 call at $1,700.
3. Sell 1 BTC $60,000 put at $1,560 → net options debit $140.
4. **Locked gross** ≈ basis $290 − options debit $140 = **$150 per BTC**.
5. **Fees:** two option legs (taker 0.03%, capped at 12.5% of premium) + future leg ≈ $25-40 round trip.
6. **Locked net** ≈ **$110-125 per BTC** (~0.2% of the $60k notional), realised at the 08:00 UTC settlement regardless of where BTC finishes.

**At expiry:** the long call + short put form a synthetic long at $60,000 that exactly offsets the short future; the basis is earned; the net is the locked figure. No early-exercise risk (European), no dividend to pay (crypto) — the two equity hazards are simply absent.

## Sources

- [[greeks-live]] / [[deribit]] documentation — European cash settlement (08:00 UTC TWAP), USDC (linear) vs inverse settlement mechanics, futures/perp specs, taker-fee premium cap; the basis for treating funding/basis as crypto's synthetic financing rate.
- Put-call parity and box-spread theory (Natenberg, *Option Volatility & Pricing*; McMillan, *Options as a Strategic Investment*) — mechanics port to crypto; the dividend and early-exercise terms drop out on Deribit's dividend-free European contracts.
- [[box-spread]] failure-mode history (2019 equity short-box losses) — the American-assignment risk that Deribit's European settlement removes.

## Getting the Data (CryptoDataAPI)

Live option quotes, per-strike IV/[[skew]], and the exact forward come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the **funding / basis, open-interest, and dislocation-trigger** context — the carry side of the trade and the flow that opens parity gaps.

**Live:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding: the carry on a perp-hedged build and the synthetic-financing read
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange OI (positioning behind basis moves)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (which strikes carry the flow that dislocates parity)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations: the forced-unwind flow that transiently pushes one leg out of parity
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — spot reference for computing the futures basis vs the Deribit future

**Historical:**
- `GET /api/v1/backtesting/funding` — historical funding for basis/carry backtests
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — spot OHLCV to reconstruct the basis series
- `GET /api/v1/backtesting/klines` — deep OHLCV archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; funding/OI detail on [[cryptodataapi]]. Live option prices, the forward, and skew come from Deribit / [[greeks-live]].

## Related

- [[put-call-parity]] — the pricing identity being arbitraged
- [[box-spread]] — conversion + reversal combined; the synthetic-rate instrument (no American short-box risk on Deribit)
- [[cash-and-carry]] / [[basis-trade]] — the futures-basis carry that *is* crypto's financing leg
- [[volatility-arbitrage]] — a different mechanism (IV vs RV), not parity
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; option quotes and the forward
- [[perpetual-futures]], [[funding-rate]] — the perp/funding hedge and carry
- [[delta-neutral]] — the position's directional stance (none)
- [[dvol]], [[skew]] — vol context that sizes the parity gaps (not a P&L driver here)
- [[leg-risk]] — the dominant residual risk: multi-leg execution
- [[section-1256-contracts]] — the tax treatment crypto options do *not* get
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
