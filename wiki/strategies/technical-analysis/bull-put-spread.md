---
title: "Bull Put Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, bull-put-spread, credit-spread, bullish, defined-risk, volatility, ethereum]
aliases: ["Put Credit Spread", "Short Put Spread", "Crypto Bull Put Spread", "Deribit Put Credit Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[bear-call-spread]]", "[[bull-call-spread]]", "[[bear-put-spread]]", "[[iron-condor]]", "[[vertical-spread]]", "[[put-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[delta]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Bull Put Spread

## Overview

The bull put spread (a **put credit spread**) is a bullish-to-neutral, **defined-risk** structure that collects a net credit at entry. You sell a higher-strike [[put-option|put]] and buy a lower-strike put at the same expiry; the short put generates premium, the long put caps the loss. The position keeps the full credit when the underlying stays above the short strike at expiry. It is the bullish mirror of the [[bear-call-spread]] and the lower half of an [[iron-condor]] — one of the most widely traded credit structures because of its simplicity and favorable win probability.

On [[deribit]] BTC and ETH options, the bull put spread is a defined-risk way to sell **overpriced downside** — harvesting the [[variance-risk-premium]] and the persistent crypto put skew that fattens after selloffs. The long wing hard-caps the tail a naked short put leaves open, which in crypto is essential: BTC/ETH have printed −50% in 24h. It works best entered when [[dvol|DVOL]] is **elevated** and you expect BTC/ETH to hold above a support level; it bleeds in a crash or a vol shock.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Sell 1 put | OTM below spot (~25-35Δ), at/below support | the income leg |
| 2 | Buy 1 put | further OTM (~10-20Δ) | protective lower wing, defines risk |

- **Strike selection:** sell the short put around 25-35 delta (≈65-75% probability of expiring OTM), at or below a tested support level. Buy the long wing one to a few strikes lower to define the loss.
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net credit** = short-put bid − long-put ask. Aim to collect **~⅓ of the width** as credit; crypto put skew often makes the short put richer.
- **Width** = short strike − long strike; sets max loss.
- **Tenor:** 21-45 DTE is the theta-rich zone. Avoid weeklies (gamma too hot for crypto's continuous gaps).

## Payoff & breakevens

- **Max profit** = net credit, when the underlying is at or above the short strike at expiry.
- **Max loss** = width − net credit, when the underlying is at or below the long wing at expiry.
- **Breakeven** = short strike − net credit.

The expiry payoff is flat at the max-profit ceiling above the short strike, sloping down between the strikes, flat at the capped-loss floor below the long wing.

## Greeks profile

- **Delta:** net long (bullish) — the position wants spot to hold or rise.
- **Gamma:** net short near the short strike — it accelerates against you as spot falls toward the short put into expiry (the crypto gamma trap; no market close to cap an overnight move).
- **Theta:** net positive — time decay is the income engine.
- **Vega:** net short — a **DVOL crush after entry helps**, a DVOL spike (which accompanies selloffs) hurts.

## Market view / when to use

- You are **bullish-to-neutral** on BTC or ETH and expect spot to hold above a support level through expiry.
- **DVOL is elevated** (roughly the 40th-90th percentile of its trailing year): the put is rich enough to pay for the wing and the tail, without selling into an active vol shock.
- You want **defined-risk** downside-premium selling rather than a naked short put or [[cash-secured-put]] — essential in crypto's fat-tailed selloffs.
- The crypto **put skew is fat** (typically after a shakeout), making the short put you sell richer.

## Adjustments & management

- **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly).
- **Time stop / roll:** manage or roll at **~21 DTE** to limit end-of-life [[gamma]]; roll down-and-out for a credit only while the bullish/neutral thesis holds.
- **Defined-risk stop:** close on a tested spread when the buy-back cost reaches **~2× the credit received**, or flatten on a DVOL vol-shock signal.
- **No early-assignment management** — Deribit options are European and cash-settled; the ex-dividend early-assignment risk of equity short puts does not exist here.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the vast majority of BTC/ETH options OI. **Alt options (SOL and below) are too thin** for a clean two-leg credit spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options for clean USD credit, width, and breakeven. **Inverse (coin-margined)** options settle in BTC/ETH and embed quanto curvature — your coin collateral's USD value *falls with spot exactly as the short put loses*, compounding the drawdown on the tested put wing. Use inverse only if the embedded coin delta is intended.
- **DVOL regime gate:** open new put-credit spreads inside the ~40th-90th [[dvol|DVOL]] percentile band. Below ~40th the credit is too thin to pay for the tail; above ~90th you are likely selling into a vol shock.
- **24/7 & weekend gaps:** no close, no gap protection, but continuous trading. A thin-liquidity weekend headline can gap spot through the short strike at 03:00 UTC with no chance to react — the reason the protective long wing (not a naked short put) is mandatory. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index, so there is **no assignment or pin risk**.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — the credit is ordinary short-term income in the US, trader-status-dependent in AU. After-tax net is materially below an SPX put-credit spread's.
- **Perp-funding interaction:** crypto skew is set by the [[perpetual-futures|perp]] book. After a selloff, **put skew fattens** (leveraged longs unwind, downside demand rises), making the short put richer to sell — the best entry window. Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheap OTM long wing and is a real drag on a two-leg structure.

## Risks

- **Sharp gap down** through the long wing (macro shock, deleveraging cascade): realises max loss with no chance to manage, correlated across a market-wide selloff — the dominant tail for premium sellers.
- **Volatility expansion** — a rising-DVOL selloff marks the spread to a large unrealised loss before expiry (net short [[vega]]).
- **Over-sizing / correlation** — many correlated short-put spreads turn one bad day into an account-threatening loss ("picking up pennies in front of a steamroller").
- **Gamma trap** — holding the short put inside ~21 DTE amplifies delta swings.
- **Edge compression** — a persistently low-DVOL regime offers premium too thin to cover costs and tail risk.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **58** (~65th percentile, put skew fat after a shakeout); 30 DTE; support near $2,800.

**Trade (per 1-ETH contract):**
- Sell 30Δ put @ **$2,800** for **$72**.
- Buy 15Δ put @ **$2,600** for **$28**.
- **Net credit = $44.** Width = $200. **Max loss = $200 − $44 = $156.**
- **Breakeven = $2,800 − $44 = $2,756.** R:R ≈ 44 : 156 ≈ **1 : 3.5** (high win probability, small reward, large tail).

**Path A — base case (holds).** ETH ranges $2,900-$3,150 and DVOL fades to 50. The short put decays; close at 50% for **+$22/contract**.

**Path B — tested but holds.** ETH dips to $2,820, just above the short strike; DVOL ticks up. At 21 DTE the mark is ~$70 loss; roll down-and-out to a $2,650/$2,450 spread for a small credit, or close for a small loss.

**Path C — flush.** A deleveraging cascade gaps ETH to $2,500 overnight; DVOL 58 → 95. The short $2,800 put is deep ITM but the long $2,600 wing caps the loss near the **−$156/contract** floor — the exact scenario the defined-risk wing exists to survive.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, put-skew behavior, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on put-credit-spread construction, gamma near expiry, and the [[variance-risk-premium]] these structures harvest (mechanics port to crypto; costs, tails, and tax do not).
- tastytrade 25-35Δ credit-spread / 50%-profit / 21-DTE management studies — mechanics port directly; sizing and stops must be tightened for the crypto crash tail.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context used to *time* the credit spread and read the downside tail.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate (want elevated/expanding, not vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (downside dealer positioning; short-strike context)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): cascade risk below spot
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the put-skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; early warning for the deleveraging flush that breaks a put-credit spread

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for realized-vol and support mapping
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

## Related

- [[bear-call-spread]] — the bearish credit-spread mirror
- [[bear-put-spread]] — the bearish *debit* put spread
- [[bull-call-spread]] — the bullish debit alternative (buy cheap DVOL instead of selling rich)
- [[iron-condor]] — combines a bull put spread and a [[bear-call-spread]] into a neutral structure
- [[vertical-spread]], [[put-spread]] — the families this belongs to
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[variance-risk-premium]] — the structural source of the credit-spread edge
- [[funding-rate]] — the perp linkage that fattens crypto put skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning and cascade context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
