---
title: "Backspread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, backspread, long-volatility, directional, crypto, derivatives, advanced]
aliases: ["Call Backspread", "Put Backspread", "Reverse Ratio Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[ratio-spread]]", "[[straddle-strangle]]", "[[butterfly-spread]]", "[[risk-reversal]]", "[[implied-volatility]]", "[[gamma]]", "[[vega]]", "[[funding-rate]]", "[[deribit]]", "[[tail-risk-hedging]]", "[[event-driven]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Backspread

## Overview

A backspread (reverse ratio spread) is the **mirror image of a [[ratio-spread]]**: sell fewer near-the-money options and buy more further-OTM options. The classic **call backspread** sells 1 ATM call and buys 2 OTM calls; the **put backspread** sells 1 ATM put and buys 2 OTM puts. The short leg finances the longs, so entry is usually a small debit or even a credit — and the payoff is **unbounded on the long side with defined, limited risk**.

Backspreads are **long-[[volatility]]**, **long-[[gamma]]** trades that want *explosive* moves. They are the structural opposite of ratio spreads: where a ratio spread wants a calm drift, a backspread wants a violent break. That makes them a natural crypto structure — BTC/ETH tails are genuinely fatter than equities, and the market frequently **underprices convexity** ahead of binary catalysts (ETF decisions, unlocks, halving, macro prints). The worst outcome is a *moderate* move that finishes right at the long strike at expiry — the "valley of death."

## Construction

**Call backspread (bullish), on BTC or ETH [[deribit]] options:**

| Leg | Action | Qty | Strike (delta) |
|---|---|---|---|
| Short | Sell call | 1 | ATM / slightly ITM (~50Δ) |
| Long | Buy call | 2 | OTM (~30Δ) |

- **Put backspread (bearish):** sell 1 ATM/ITM put, buy 2 OTM puts at a lower strike.
- **Ratio:** 1:2 standard; 1:3 adds tail leverage at higher cost.
- **Net debit/credit:** aim for **zero cost or a small debit**. Entered for a **credit**, the structure also profits if the underlying moves *sharply against* the directional leg (both tails pay).
- **Tenor:** 30-60 DTE — the long legs need time; short tenors bleed the extra longs on [[theta]].

## Payoff & Breakevens

- **Max profit (call backspread):** **unbounded** to the upside — above the upper breakeven each extra long adds one unit of gain.
- **Max loss:** at the **long strike at expiry** = `(long strike − short strike) − net credit` (or `+ net debit`). Known and capped at entry.
- **Upper breakeven:** `long strike + (max loss / number of extra longs)`.
- **Lower "profit" (credit entry):** below `short strike − net credit`, a sharp drop leaves the position profitable on the retained credit.
- The loss profile is a valley centred on the long strike, flanked by unbounded upside and (on a credit entry) a profitable far-downside.

## Greeks Profile

- **[[delta]]:** directional in the trade's favour once price clears the long strikes.
- **[[gamma]]:** **net long** — profit accelerates as the move extends; this is the engine.
- **[[vega]]:** **net long** — rising [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] lifts the position even before spot moves.
- **[[theta]]:** **net negative** — two long options decay faster than the single short; time is the enemy, so backspreads are held for the move, not for carry.

## Market View / When to Use

- You expect a **large, fast directional move** and want **capped downside** if you are wrong.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] is low** (low percentile of its trailing year) and you expect it to expand — the long-vega tailwind.
- Ahead of a **binary crypto catalyst** where the market is underpricing the tail (spot-ETF rulings, major token unlocks, the halving, FOMC/CPI) — an [[event-driven]] use.
- As a cheap, defined-risk **convexity / [[tail-risk-hedging|tail hedge]]** overlay on a directional book.

## Adjustments & Management

- **Let winners run:** if the underlying is powering past the long strikes, the 2:1 ratio compounds gains — do not cut early.
- **Avoid the valley into expiry:** if price is drifting toward the long strike with time running down, close before the max-loss zone; a pin at the long strike at expiry is the worst case.
- **Harvest a vol spike:** a [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] jump can make the trade profitable on vega alone before spot moves — consider banking it.
- **Time stop:** if the move has not arrived with <14 DTE, close — [[theta]] on the extra longs accelerates in the final weeks.

## Crypto Specifics

- **Venue & settlement.** [[deribit]] BTC/ETH options are **European, cash-settled** to the Deribit index — no early assignment on the short leg, no delivery. A gap **through** the valley into deep-ITM territory simply marks at settlement; there is no session close to interrupt a favourable overnight run.
- **Fatter tails, underpriced convexity.** Crypto's realized-move distribution has heavier tails than equities (2020-03, LUNA, FTX, 2025-10-10). Backspreads are built to monetise exactly those tails, and crypto's tendency to under-price OTM convexity in calm regimes is the recurring setup.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] as the entry filter.** Enter when DVOL sits in a **low percentile** — cheap long vega with room to expand. Buying backspreads into already-elevated DVOL overpays for the longs.
- **Inverse vs linear.** **USDC-margined (linear)** contracts give clean USD tail P&L. **Coin-margined (inverse)** contracts embed a coin delta: a call backspread on inverse options gains on both the option payoff *and* the rising collateral value — an amplifier on the upside but a complication to model. Match settlement to intent.
- **[[funding-rate|Perp-funding]] / skew.** Funding-driven skew tells you which wing is cheap: when funding is negative and put skew is bid, call convexity can be relatively cheap (and vice-versa) — buy the underpriced wing.
- **24/7 & continuous gaps.** No overnight halt means the big move the backspread needs can happen at any hour — a structural fit for a long-gamma trade — but it also means the valley-of-death drift can grind through a weekend uninterrupted.
- **No [[section-1256-contracts|§1256]].** No 60/40 treatment; gains are ordinary/short-term.
- **Alt-option liquidity limits.** BTC/ETH have the depth for the extra long legs; alt options are usually too thin and wide to buy convexity efficiently.

## Risks

- **The valley of death:** a moderate move to the long strike at expiry is the maximum-loss outcome — the most probable single price, unfortunately.
- **[[theta]] bleed:** two long options decay daily; a slow market erodes the position even if direction is eventually right.
- **Needs a *big* move:** most backspreads expire without the tail arriving — low probability of full max profit, offset by unbounded payoff when it does.
- **Vega give-back:** if DVOL was high at entry and then collapses, the long vega works against you.
- **Financing drag** if hedging or rolling on the perp in an adverse funding regime.

## Worked Crypto Example

**Setup.** BTC at **$60,000** on [[deribit]] (USDC-margined), 45 DTE, [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] low (~40, ~20th percentile) ahead of a spot-ETF decision. You expect a large move up and want capped downside.

1. **Sell 1 BTC $60,000 call** at **$2,800**.
2. **Buy 2 BTC $66,000 calls** at **$1,400** each → **$2,800**.
3. **Net cost = $0** (zero-cost entry).
4. **Max loss at $66,000 at expiry:** short $60k call worth $6,000; the two $66k calls worthless → **−$6,000** per structure (the valley).
5. **Upper breakeven:** `$66,000 + $6,000 = $72,000`.
6. **Path A — big move up:** BTC rips to **$78,000**. Short $60k call worth $18,000 (−$18,000); two $66k calls worth $12,000 each = $24,000 (+$24,000). **Net ≈ +$6,000** and climbing with any further upside.
7. **Path B — flat:** BTC stays at $60,000 → all legs expire worthless → **P&L = $0**.
8. **Path C — sharp drop:** BTC falls to $50,000 → all legs worthless → **P&L = $0** (zero-cost entry, no downside).
9. Loss only occurs in the **$60,000-$72,000** band, worst at $66,000.

## Getting the Data (CryptoDataAPI)

The [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] level and strike/wing pricing come from [[deribit]] / [[greeks-live]]. [[cryptodataapi]] supplies the **volatility-regime timing, event calendar, funding/skew, and dealer-gamma** context for entering long convexity cheaply into an expected expansion.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime; enter longs when *compressed* / *mean_reverting*
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100); low readings favour buying convexity
- `GET /api/v1/event/calendar` — forward catalysts (unlocks, macro) up to 30 days out — the binary-event setups
- `GET /api/v1/event/regime/score` — Event Risk composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding / skew read for wing selection
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (short-gamma dealers amplify the move the backspread wants)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/backtesting/klines` — deep OHLCV archive to study tail frequency and payoff

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: volatility-regime and event-regime detail on [[cryptodataapi]]. IV/DVOL surface is Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — enter when `GET /api/v1/volatility/regime` reads `compressed` and `GET /api/v1/event/calendar` shows a binary catalyst inside the option tenor — the cheap-convexity-into-expansion setup this structure exists for
- **Regime gate** — `GET /api/v1/quant/market`: rising `vol_spike`/`squeeze` probabilities support paying for tail exposure; a settled `range_low_vol` book with no catalyst is pure theta bleed on the long wings
- **Backtest** — study tail-move frequency with `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); replay entry timing against point-in-time vol/event scores in `/api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid lookahead
- **Tips** — the 60-day history on `/api/v1/volatility/regime/{symbol}` shows how long `compressed` states persist — enter late in the compression, not early; a short-dealer-gamma read from `/api/v1/quant/gex` is the amplifier the backspread wants behind its breakout.

## Related

- [[ratio-spread]] — the mirror structure: sell more than you buy, profiting from calm, moderate moves
- [[straddle-strangle]] — non-directional long-vol alternatives
- [[tail-risk-hedging]] — the convexity-buying discipline the backspread expresses cheaply
- [[event-driven]] — the binary-catalyst context backspreads are built around
- [[butterfly-spread]] — a defined-risk structure for a specific price target (opposite volatility view)
- [[funding-rate]] — the perp linkage that prices crypto skew and cheap wings
- [[deribit]] — venue; European cash settlement, DVOL source
- [[section-1256-contracts]] — the tax treatment crypto options do **not** receive
