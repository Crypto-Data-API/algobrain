---
title: "Vertical Spread"
type: strategy
created: 2026-04-13
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, vertical-spread, credit-spread, debit-spread, defined-risk, volatility]
aliases: ["Vertical Spreads", "Bull Call Spread", "Bear Put Spread", "Bull Put Spread", "Bear Call Spread", "Debit Vertical Spread", "Credit Vertical Spread", "Crypto Vertical Spread"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[bull-call-spread]]", "[[bear-put-spread]]", "[[bull-put-spread]]", "[[bear-call-spread]]", "[[iron-condor]]", "[[put-spread]]", "[[credit-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Vertical Spread

## Overview

A vertical spread is the **building block** of most multi-leg options structures: buy and sell two options of the same type (both calls or both puts), same underlying, same expiry, different [[strike-price|strikes]]. The result is a **defined-risk, defined-reward** directional bet — both the maximum profit and the maximum loss are fixed and known before entry. There are four flavours, two debit (directional) and two credit (premium-selling):

- **[[bull-call-spread|Bull Call Spread]]** (debit): buy lower-strike call, sell higher-strike call. Profits when spot rises.
- **[[bear-put-spread|Bear Put Spread]]** (debit): buy higher-strike put, sell lower-strike put. Profits when spot falls.
- **[[bull-put-spread|Bull Put Spread]]** (credit): sell higher-strike put, buy lower-strike put. Profits when spot stays above the short strike.
- **[[bear-call-spread|Bear Call Spread]]** (credit): sell lower-strike call, buy higher-strike call. Profits when spot stays below the short strike.

On [[deribit]] — effectively "the market" for BTC and ETH options — the vertical spread is the workhorse defined-risk expression of a bounded directional or premium-selling view on crypto. Debit verticals monetise a correct forecast cheaply (net long [[vega]], entered when [[dvol|DVOL]] is low); credit verticals harvest the [[variance-risk-premium]] and crypto skew (net short vega, entered when DVOL is elevated). The wrapper defines risk; it does not by itself create expectancy.

## Construction

Two legs, one expiry, one underlying (BTC or ETH), cash-settled to the Deribit index. Contracts are 1 BTC or 1 ETH each; ratio is 1:1.

| Flavour | Long leg | Short leg | Enter for |
|---|---|---|---|
| Bull call (debit) | Buy lower-strike call | Sell higher-strike call | Net debit |
| Bear put (debit) | Buy higher-strike put | Sell lower-strike put | Net debit |
| Bull put (credit) | Buy lower-strike put | Sell higher-strike put | Net credit |
| Bear call (credit) | Buy higher-strike call | Sell lower-strike call | Net credit |

- **Debit verticals:** buy the ATM/first-ITM strike (~50-65Δ), sell the strike at your BTC/ETH price target (~30-40Δ). Pay no more than **~⅔ of the width** so max profit ≥ ~0.5× max loss.
- **Credit verticals:** sell the ~25-35Δ strike at/beyond a tested [[support-and-resistance|support/resistance]] level, buy the protective wing 1-3 strikes further out (~10-20Δ). Collect **~⅓ of the width**.
- **Width** = distance between strikes, typically 5-15% of spot; sets the risk/reward.
- **Tenor:** 30-45 DTE for credit verticals (theta-rich); 21-45 DTE for debit verticals. Avoid weeklies — crypto [[gamma]] is too hot given continuous gaps.

## Payoff & breakevens

| Flavour | Net | Max profit | Max loss | Breakeven |
|---|---|---|---|---|
| Bull call (debit) | Pay | Width − debit | Debit paid | Long strike + debit |
| Bear put (debit) | Pay | Width − debit | Debit paid | Long strike − debit |
| Bull put (credit) | Receive | Credit received | Width − credit | Short strike − credit |
| Bear call (credit) | Receive | Credit received | Width − credit | Short strike + credit |

Every vertical has the same expiry payoff *skeleton*: a sloped ramp between the two strikes that flattens into a floor on one side and a ceiling on the other. The credit-side headline risk/reward is unattractive (risk ~2-3 to make ~1) but is offset by a ~65-75% win rate; the debit side is the reverse — a lower hit rate carried by larger payoffs. Neither is free (see *Risks*).

## Greeks profile

The bought leg partly cancels the sold leg, so a vertical is a *muted* version of a single option's Greeks — closer to a price/probability bet than an outright.

| Greek | Credit vertical | Debit vertical |
|---|---|---|
| [[delta]] | Small (a probability bet) | Larger — the directional engine |
| [[gamma]] | Negative near the short strike (the DTE trap) | Net long from the bought leg, partly offset |
| [[theta]] | Positive — time decay is the income | Negative — the bought leg bleeds, partly financed by the short leg |
| [[vega]] | Negative — short vol; a DVOL spike marks it down | Positive — long vol; suffers a DVOL crush |

This drives the [[dvol|DVOL]]-regime rule: **sell credit verticals when DVOL is rich** (you are short vega and want it to fall), **buy debit verticals when DVOL is cheap** (long vega, cheap entry). The same variance risk premium that powers the [[iron-condor]] is what the credit vertical harvests — a vertical is one half of an iron condor.

## Market view / when to use

Pick the flavour by direction crossed with the DVOL regime:

| View | DVOL low (cheap) | DVOL elevated (rich) |
|---|---|---|
| Bullish | [[bull-call-spread]] (debit) | [[bull-put-spread]] (credit) |
| Bearish | [[bear-put-spread]] (debit) | [[bear-call-spread]] (credit) |

Use a vertical whenever you have a **bounded** directional or premium-selling view on BTC/ETH and want defined risk rather than an open-ended perp or naked-option position. Avoid holding short strikes through a scheduled binary catalyst (major unlock, macro print) unless the trade is explicitly an event trade.

## Adjustments & management

- **Credit verticals:** take profit at **50% of the credit**; manage/roll at **~21 DTE** to escape the gamma trap; defined-risk stop at a buy-back cost of **~2× the credit**. Roll out (and away) only for a net credit while the thesis holds.
- **Debit verticals:** take profit at **50-75% of max value** or at the price target; stop at **−50-60% of the debit** or on thesis invalidation; time-stop by ~10-14 DTE.
- **Sizing:** max loss is fixed at entry — risk ≤ 1-3% of the book per spread; cap *aggregate correlated short-premium* exposure (a single crypto-wide move can put every short strike ITM at once).
- **No early-assignment or ex-dividend management** — Deribit options are European and cash-settled (see *Crypto specifics*).

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the overwhelming majority of BTC/ETH options OI; OKX and Binance run smaller books. **Alt options (SOL and below) are too thin** to leg a clean vertical — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options so debit/credit, width, and breakeven are clean USD numbers. **Inverse (coin-margined)** options settle in BTC/ETH and embed a quanto-like curvature — collateral USD value moves with spot, distorting the payoff and adding wrong-way risk. Use inverse only if the embedded coin delta is intended.
- **DVOL regime:** buy debit verticals when [[dvol|DVOL]] is depressed (~10th-50th pct); sell credit verticals when DVOL is elevated (~40th-90th pct). Below ~40th the credit is too thin; above ~90th you are selling into a vol shock.
- **24/7 & weekend gaps:** no close and no gap protection, but continuous trading. A thin-liquidity weekend headline can gap spot through a short strike at 03:00 UTC — defined-risk wings cap the worst case. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index — **no exercise, assignment, or pin risk** the way US single-name spreads have.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — every leg is ordinary short-term capital-gains (US, full marginal rates) or trader-status-dependent CGT/income (AU). After-tax net is materially below an SPX vertical's.
- **Perp-funding interaction:** crypto skew is set by the [[perpetual-futures|perp]] book, not by equity hedgers. **Richly positive [[funding-rate|funding]] firms call skew** (favours selling a bear call spread); **after a selloff, put skew fattens** (favours selling a bull put spread). Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on cheap OTM legs and is a real drag on a two-leg structure.

## Risks

- **Debit side:** sideways/flat tape ([[theta]] bleed), a DVOL crush after entry, adverse gaps, and capped profit on a big favorable move.
- **Credit side:** a sharp adverse gap or trend through the short strike (max loss), a DVOL expansion before expiry (short [[vega]]), and *correlated tail losses* when many short-premium positions all lose together in a crypto-wide move.
- **Both:** the [[gamma]] trap if short strikes are carried inside ~21 DTE; edge compression in the wrong DVOL regime; and two-leg execution cost, which on wide alt or far-OTM markets can exceed the edge. Use combo/RFQ execution ([[greeks-live]] / Paradigm), never leg in.

## Worked crypto example

Both a debit and a credit vertical on **BTC**, USDC-margined/linear, per 1-BTC contract.

**Bull call spread (debit, bullish, DVOL 46 / cheap, 40 DTE).** BTC spot $60,000.
- Buy 55Δ $60,000 call @ **$3,400**; sell 33Δ $66,000 call @ **$1,500**.
- Net debit **$1,900**; width $6,000; **max profit $4,100**; **max loss $1,900**; breakeven **$61,900**; R:R ≈ 2.16:1.

**Bull put spread (credit, bullish-neutral, DVOL 56 / rich, 32 DTE).** BTC spot $60,000, support ~$57,000.
- Sell 30Δ $57,000 put @ **$1,700**; buy 15Δ $54,000 put @ **$800**.
- Net credit **$900**; width $3,000; **max profit $900**; **max loss $2,100**; breakeven **$56,100**; R:R ≈ 1:2.3 (high win probability).

| Structure | Net | Max profit | Max loss | Breakeven | Profits when |
|---|---|---|---|---|---|
| Bull call (debit) | −$1,900 | $4,100 | $1,900 | $61,900 | BTC rises to ≥ $66,000 |
| Bull put (credit) | +$900 | $900 | $2,100 | $56,100 | BTC stays ≥ $57,000 |

The debit example pays a small cost for an asymmetric directional payoff in a cheap-DVOL regime; the credit example collects premium for a high-probability, negatively-skewed payoff in a rich-DVOL regime.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, skew behavior, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on vertical-spread pricing, Greeks, and the relationship between spread width and risk (mechanics port to crypto; costs, tails, and tax do not).
- McMillan, L. *Options as a Strategic Investment* — standard treatment of bull/bear verticals, breakevens, and follow-up action.
- tastytrade credit-vertical management studies (50%-profit / 21-DTE / 2× stop) — mechanics port directly; sizing tightened for the crypto tail.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context that selects the flavour (debit vs credit) and times entry.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the debit-vs-credit selector (compressed → debit; elevated → credit)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (dealer-positioning context for strike selection)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): pin vs breakout/cascade
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crypto skew driver (firm call skew vs fat put skew)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the move that breaks a credit vertical

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for trend, realized-vol, and level mapping
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structures

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

## Related

- [[bull-call-spread]], [[bear-put-spread]] — the debit (directional) members
- [[bull-put-spread]], [[bear-call-spread]] — the credit (VRP) members
- [[iron-condor]] — two credit verticals combined into a neutral structure
- [[put-spread]] — the put-vertical family overview
- [[credit-spread]] — credit-spread strategies in depth
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime selects debit vs credit
- [[variance-risk-premium]] — the premium the credit side harvests
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[delta]], [[theta]], [[vega]], [[gamma]] — the Greeks that drive both families
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
