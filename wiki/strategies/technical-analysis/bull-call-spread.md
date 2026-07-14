---
title: "Bull Call Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, bull-call-spread, debit-spread, bullish, defined-risk, bitcoin]
aliases: ["Call Debit Spread", "Call Spread", "Crypto Bull Call Spread", "Deribit Call Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[bear-put-spread]]", "[[bull-put-spread]]", "[[bear-call-spread]]", "[[vertical-spread]]", "[[iron-condor]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Bull Call Spread

## Overview

The bull call spread (a **call debit spread**) is a bullish, **defined-risk** options structure that pays a net debit at entry. You buy a lower-strike [[call-option|call]] and sell a higher-strike call at the same expiry; the long call gives the upside, the short call cheapens the position and caps the profit. It is the debit-based, directional cousin of the credit-collecting [[bull-put-spread]] and the bullish mirror of the [[bear-put-spread]].

On [[deribit]] — which holds the overwhelming majority of BTC and ETH options open interest — the bull call spread is the cleanest way to express a *bounded* bullish view on crypto with a loss that is fully known before you enter. Because you are a net premium *buyer*, the structure is net long [[vega]] and pays [[theta]]: it works best entered when [[dvol|DVOL]] (Deribit's 30-day implied-vol index) is **low**, so the long call is cheap, and a subsequent up-move plus a DVOL bump both help. It does **not** harvest the [[variance-risk-premium]]; the edge is a correct directional forecast, cheapened by giving up gains above the short strike.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Buy 1 call | ATM to slightly ITM (~50-65Δ) | the directional engine |
| 2 | Sell 1 call | OTM, at your price target (~30-40Δ) | finances the long, caps upside |

- **Strike selection:** buy the long call at-the-money to slightly in-the-money for a higher-probability, lower-leverage spread; buy slightly OTM for a cheaper, higher-payoff structure. Place the short call at or just past your BTC/ETH price target.
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net debit** = long-call ask − short-call bid. Discipline: pay no more than **~⅔ of the spread width** so max profit ≥ ~0.5× max loss.
- **Width** = short strike − long strike; roughly 5-15% of spot is typical.
- **Tenor:** 21-45 DTE. Longer tenors reduce [[theta]] drag on the long leg and give the thesis time; weeklies put the trade at the mercy of crypto's continuous [[gamma]] and gaps.

## Payoff & breakevens

- **Max profit** = width − net debit, when the underlying is at or above the short strike at expiry.
- **Max loss** = net debit, when the underlying is at or below the long strike at expiry (both calls expire worthless).
- **Breakeven** = long strike + net debit.

The expiry payoff is a ramp: flat at the max-loss floor below the long strike, rising between the strikes, flat at the max-profit ceiling above the short strike.

## Greeks profile

- **Delta:** net long (bullish) — the directional engine. Largest between the strikes near expiry.
- **Gamma:** net long from the bought leg, partly offset by the short leg — a muted version of a single long call.
- **Theta:** net negative — time decay works against you while spot sits below the long strike. This is the cost of being a premium buyer.
- **Vega:** net long — a **DVOL rise after entry helps**, a DVOL crush hurts. This is why you prefer to enter in a low-DVOL regime.

## Market view / when to use

- You are **moderately bullish** on BTC or ETH and expect spot at or above the short strike by expiry, ideally on an identifiable catalyst (ETF flow, halving-cycle continuation, macro pivot).
- **DVOL is low-to-moderate** (roughly the 10th-50th percentile of its trailing year) so the long call is cheap — the mirror of the credit-spread regime.
- You want **defined risk** rather than the open-ended cost-of-carry and [[theta]] bleed of an outright long call.
- You have a specific upside target that maps to the short strike; you accept capping gains beyond it in exchange for a cheaper entry.

## Adjustments & management

- **Profit target:** take profits at **50-75% of max value** rather than grinding into expiry-week [[gamma]].
- **Stop:** cut at roughly **−50-60% of the debit** or on thesis invalidation (catalyst passed without the move; a key level reclaimed to the downside).
- **Time stop:** close by **~10-14 DTE** if neither target nor stop is hit — crypto gamma accelerates into the 08:00 UTC expiry faster than equity gamma because gaps are unbounded and continuous.
- **Roll up-and-out** for additional debit only if the thesis strengthens; never chase a losing directional debit with more premium.
- **No early-assignment management needed** — Deribit options are European and cash-settled (see *Crypto specifics*), removing the ex-dividend assignment dance that equity call spreads require.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] is effectively "the market" for BTC/ETH options; OKX and Binance run smaller books. **Alt options (SOL and below) are too thin** to leg a clean spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options so the debit, width, and breakeven are clean USD numbers. **Inverse (coin-margined)** options settle in BTC/ETH and embed a quanto-like curvature — your collateral's USD value moves with spot, distorting the textbook payoff and adding wrong-way exposure. Use inverse only if the embedded coin delta is intended.
- **DVOL regime:** debit structures want **cheap** vol. Enter when [[dvol|DVOL]] is depressed; avoid buying the spread after a vol spike has already inflated both legs (you overpay and eat the subsequent DVOL crush).
- **24/7 & weekend gaps:** there is no close and no overnight gap protection, but also continuous trading. A thin-liquidity weekend headline can gap spot through your strikes at 03:00 UTC — defined risk means the worst case is still just the debit. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index, so there is **no exercise, assignment, or pin risk** the way US single-stock call spreads have.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — every leg is an ordinary short-term capital-gains event in the US, and CGT/income-dependent on trader status in AU. After-tax net is materially below an SPX call spread's.
- **Perp-funding interaction:** crypto call skew is set by the [[perpetual-futures|perp]] book. When [[funding-rate|funding]] is richly positive (leveraged longs paying), OTM call skew firms and the short call you sell is **richer** — better financing for the spread. Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheaper OTM short leg and is a real drag on a two-leg structure.

## Risks

- **Sideways/flat tape** — the most common killer: [[theta]] bleeds the long leg while BTC/ETH fails to reach the long strike; the debit erodes.
- **DVOL crush** — buying into elevated DVOL then suffering a vol collapse leaves the position underwater even on a small favorable move (net long [[vega]]).
- **Adverse gap down** — a weekend or overnight gap below the long strike realises the full debit; capped, but total.
- **Capped upside** — a violent melt-up earns no more than max profit; the give-up versus an outright call.
- **Execution/liquidity** — two legs in and (usually) two out; wide alt-option or far-OTM markets erode a thin edge. Use combo/RFQ execution ([[greeks-live]] / Paradigm), not legging in.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$60,000**; BTC DVOL **46** (~20th percentile, cheap); 40 DTE. Moderately bullish into a continuation thesis; funding mildly positive (call skew slightly firm).

**Trade (per 1-BTC contract):**
- Buy 55Δ call @ **$60,000** for **$3,400**.
- Sell 33Δ call @ **$66,000** for **$1,500**.
- **Net debit = $1,900.** Width = $6,000. **Max profit = $6,000 − $1,900 = $4,100.** **Max loss = $1,900.**
- **Breakeven = $60,000 + $1,900 = $61,900.** R:R ≈ 4,100 : 1,900 ≈ **2.16 : 1**.

**Path A — thesis works.** Over three weeks BTC grinds to $67,000 and DVOL ticks up to 50. The spread marks near full width (~$5,600); close at ~$4,200 realized (past the 75% target) rather than carry expiry gamma.

**Path B — chop.** BTC oscillates $58,000-$62,000 and DVOL drifts to 42. Theta and the DVOL fade erode the mark to ~$1,100; the time stop at 12 DTE closes it for **−$800/contract** (partial debit lost).

**Path C — adverse gap.** A macro headline gaps BTC to $54,000 overnight; both calls collapse. The position is worth ~$150; close for **≈ −$1,750/contract**, near the defined max loss the structure caps at.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on vertical-spread construction, payoff, and the [[implied-volatility]] impact on debit-spread pricing (mechanics port to crypto; costs, tails, and tax do not).
- tastytrade debit-spread management studies (50-75% profit-take, directional cost discipline) — mechanics port; sizing and stops tightened for crypto's continuous gaps.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the complementary volatility-regime, options-flow, dealer-gamma, and funding context used to *time* a debit spread (buy cheap vol) and read dealer positioning.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): the entry gate — you want *compressed* for a debit spread
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (dealer-positioning context for the short strike)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): whether spot is pinned or breakout-prone
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crypto call-skew driver

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history (find low-DVOL entry windows)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for trend context and realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

## Related

- [[bear-put-spread]] — the bearish debit-spread mirror
- [[bull-put-spread]] — the bullish *credit* alternative (sell rich DVOL instead of buying cheap)
- [[bear-call-spread]] — the bearish credit spread
- [[vertical-spread]] — the family this belongs to (debit and credit verticals)
- [[iron-condor]] — a neutral structure built from two credit verticals
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and surface source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[funding-rate]] — the perp linkage that shapes crypto call skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[delta]], [[theta]], [[vega]], [[gamma]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
