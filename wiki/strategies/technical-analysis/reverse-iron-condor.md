---
title: "Reverse Iron Condor"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, volatility, breakout, bitcoin, ethereum]
aliases: ["RIC", "Reverse Iron Condor Spread", "Long Iron Condor"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[iron-condor]]", "[[crypto-options-volatility-selling]]", "[[straddle-strangle]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Reverse Iron Condor

## Overview

The reverse iron condor (RIC) is the **mirror image of an [[iron-condor]]**: instead of selling the wings to collect premium, you **buy** OTM spreads on both sides to profit from a large move in either direction. Specifically you buy a bull call spread above spot and a bear put spread below it. The result is a **debit, defined-risk** structure that pays off when the underlying breaks out of its range — a directionally-agnostic breakout play. It is a **long-volatility** trade: the crypto version wants compressed DVOL (cheap options) and an imminent catalyst, the opposite regime to the short-premium [[iron-condor]].

On [[deribit]] BTC/ETH, the RIC is a cheaper, capped-risk alternative to buying a raw [[straddle-strangle|strangle]] outright: the short outer legs subsidize the long inner legs, lowering the debit at the cost of capping the upside. It shines going into a known volatility event when implied vol has *not* yet priced the move.

## Construction

Four legs, one expiry, cash-settled to the Deribit index:

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Buy 1 call | OTM above spot (~25Δ) | long side of call spread |
| 2 | Sell 1 call | further OTM (~10-12Δ) | subsidizes the long call |
| 3 | Buy 1 put | OTM below spot (~25Δ) | long side of put spread |
| 4 | Sell 1 put | further OTM (~10-12Δ) | subsidizes the long put |

- **Strike selection:** long strikes just OTM so the structure catches a realistic breakout; short strikes far enough out that you keep most of the move's payoff. Wider spreads = higher max profit but higher debit.
- **Ratios:** 1:1:1:1.
- **Net debit** = cost of both spreads combined = the maximum loss.
- **Tenor:** 30-60 DTE so the breakout has time to develop; or a tight expiry timed to a specific catalyst (FOMC, CPI, a large token unlock, an ETF decision).

## Payoff & breakevens

- **Max profit** = width of one spread − total debit, achieved when one side is fully ITM.
- **Max loss** = total debit paid, when spot stays between the two long strikes at expiry.
- **Upper breakeven** = long call strike + total debit.
- **Lower breakeven** = long put strike − total debit.

The payoff is a "valley": max loss across the middle (no move), rising to two capped-profit plateaus once spot clears either long strike.

## Greeks profile

- **Delta:** ~0 at entry (balanced); becomes strongly directional once spot leaves the range — long call spread wins on a rally, long put spread on a selloff.
- **Gamma:** **positive** throughout — the mirror of the iron condor. The position *likes* movement and its profit accelerates as spot runs toward a long strike. Positive gamma is the whole point.
- **Theta:** **negative** — time decay works against you on both spreads simultaneously; the enemy of the trade. Every quiet day costs money.
- **Vega:** **positive** — a rise in DVOL after entry (which usually accompanies a breakout) marks the position up. Buying into compressed DVOL is the ideal entry.

## Market view / when to use

- You expect a **breakout** but are genuinely unsure of direction.
- A high-impact catalyst is approaching (FOMC/CPI, ETF flows/decision, a major unlock, a halving-adjacent regime shift) that should drive a large move.
- **DVOL is compressed** (low percentile of its trailing year) so the debit spreads are cheap — you want to *buy* vol before it expands.
- You want the defined-risk, lower-cost profile that a naked long strangle does not offer.

## Adjustments & management

- **Take the winning side:** on a decisive move, the tested spread approaches max value while the other decays. Close the winner into strength rather than round-tripping it; the losing spread is already near zero.
- **Time stop:** if the catalyst passes with no move, close early to salvage residual premium — negative theta compounds and DVOL crush (post-event IV collapse) hurts the long vega. Do not hold a dead RIC hoping.
- **Leg into it:** in a compressed-vol setup you can buy the long inner legs first and sell the outer legs after a small initial move to improve pricing — advanced, and it re-introduces timing risk.
- **Roll out** only if the thesis (imminent volatility) is intact but slow to arrive; otherwise accept the capped debit loss.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] BTC/ETH only for a clean four-leg RIC; **alt options are too thin** to buy and sell spreads without paying a punishing bid-ask.
- **Inverse vs linear/USDC settlement:** use **USDC-margined (linear)** options so the debit, breakevens, and payoff are clean USD figures. Inverse (coin-margined) options add quanto curvature that distorts a symmetric breakout structure.
- **DVOL regime gate (inverted):** unlike the short-premium condor, the RIC wants **low/compressed DVOL** — buy when the vol-regime read is *compressed* and a catalyst looms. Buying a RIC at a high DVOL percentile means paying up for vol that is likely to *crush*, the classic long-vol trap.
- **24/7 & weekend gaps — a tailwind here.** Crypto's continuous, gap-prone tape is exactly what a long-gamma structure wants: a weekend liquidation cascade or melt-up that would gap a short condor into max loss instead gaps the RIC toward max profit. There is no close to cap the move, and expiry is **08:00 UTC**, cash-settled to the Deribit index (no pin/assignment mechanics).
- **No [[section-1256-contracts|§1256]]:** gains on the winning side are ordinary capital-gains events on offshore Deribit — no 60/40 US treatment; AU treatment is trader-status-dependent.
- **Perp funding interaction:** funding and [[gamma-exposure|dealer gamma]] help time entries. When dealers are **short gamma** (cascade-prone) and funding is stretched, a violent unwind is more likely — a favorable RIC backdrop. Positive gamma means you do *not* delta-hedge away the payoff; you let it run.
- **Event-timed vs generic:** the strongest crypto RICs are catalyst-timed (event calendar), because compressed DVOL + a scheduled shock is the cleanest long-vol setup.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$108,000**; BTC DVOL **38** (compressed, ~25th percentile); a scheduled FOMC + a large token-unlock cluster land inside 30 days. 35 DTE. You expect a big move, direction unknown.

**Trade (per 1-BTC contract):**
- Buy 25Δ call @ **$114,000** for **$1,700**; sell 12Δ call @ **$122,000** for **$700** → call spread debit $1,000.
- Buy 25Δ put @ **$102,000** for **$1,900**; sell 12Δ put @ **$94,000** for **$850** → put spread debit $1,050.
- **Net debit = $2,050 = max loss.** Spread width = $8,000 each. **Max profit = $8,000 − $2,050 = $5,950** (one side fully ITM).
- **Breakevens:** $114,000 + $2,050 = **$116,050** (up); $102,000 − $2,050 = **$99,950** (down).

**Path A — breakout up.** FOMC surprises dovish; BTC rips to $121,000 and DVOL 38 → 55. The call spread approaches its $8,000 width; the put spread is near zero. Close the call spread for ~$7,400 → **+$5,350/contract** (positive vega added to the intrinsic gain).

**Path B — breakout down.** A large unlock triggers a liquidation cascade; BTC gaps to $96,000 over a weekend. The put spread nears full width; close for ~$7,600 → **+$5,550/contract**. The 24/7 gap *helped* — the long-gamma structure caught it.

**Path C — no move (the loss path).** BTC chops $104,000-$112,000; the catalysts pass quietly and DVOL crushes 38 → 32. Both spreads decay; theta and IV crush compound. Close at ~10 DTE for ~$700 to salvage value → **−$1,350/contract** (a fraction of the $2,050 max loss). This is the RIC's failure mode: right structure, no volatility.

## Sources

- [[greeks-live]] / [[deribit]] documentation — DVOL construction and its mean-reverting behavior around events, IV surface, USDC-margined vs inverse settlement, 08:00 UTC cash settlement.
- [[book-option-volatility-and-pricing]] — Natenberg on long-gamma/long-vega debit structures and event volatility (mechanics port to crypto).
- Deribit Insights / event-vol research — DVOL compression-then-expansion around scheduled crypto catalysts.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the complementary volatility-regime, dealer-gamma, funding, and *event-calendar* context used to time a long-vol breakout.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime; the RIC wants a **compressed** read
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100); a low reading flags cheap vol to buy
- `GET /api/v1/event/calendar` — filterable forward catalysts (unlock/macro/depeg) up to 30 days out: the trigger set for a catalyst-timed RIC
- `GET /api/v1/quant/gex` — Gamma Exposure; short-dealer-gamma regimes are cascade-prone (favorable for long gamma)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, a positioning/skew read
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (walls that may pin price and stall a breakout)

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history (spot compressed-vol windows)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol/range context
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting breakout timing

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the RIC timing loop end-to-end (legs and DVOL stay on Deribit / [[greeks-live]]):

- **Setup screen** — `GET /api/v1/volatility/regime` (want `compressed`) + `GET /api/v1/volatility/regime/score` (a low reading = cheap vol to buy).
- **Catalyst trigger** — `GET /api/v1/event/calendar` — filter unlock/macro/depeg events landing inside the tenor; compressed vol plus a dated catalyst is the entry condition.
- **Cascade context** — `GET /api/v1/quant/gex` — short-dealer-gamma regimes are cascade-prone, the favorable backdrop for long gamma; `GET /api/v1/market-intelligence/options` warns of OI walls that could pin price and stall the breakout.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) to measure breakout frequency and magnitude after compression windows vs the debit paid; `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) replays regime + event context point-in-time.
- **Tips** — automate the time-stop: if the calendar's catalyst passes with no expansion, salvage the residual debit instead of bleeding theta into a dead structure.

## Related

- [[iron-condor]] — the short-premium mirror; profits from range, not breakout
- [[crypto-options-volatility-selling]] — the short-vol context this trade sits opposite to
- [[straddle-strangle]] — the uncapped long-vol alternative with higher cost
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[gamma-exposure]] — positioning/cascade context that times a breakout
- [[max-pain]] — OI walls that can pin price and stall a move
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
