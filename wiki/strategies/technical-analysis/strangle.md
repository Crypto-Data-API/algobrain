---
title: "Strangle"
type: strategy
created: 2026-05-07
updated: 2026-07-19
status: good
tags: [options, crypto, volatility, derivatives, swing-trading]
aliases: ["Crypto Strangle", "Long Strangle", "BTC Strangle", "ETH Strangle"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[short-strangle]]", "[[straddle]]", "[[short-straddle]]", "[[straddle-strangle]]", "[[crypto-options-volatility-selling]]", "[[iron-condor]]", "[[iron-fly]]", "[[gamma-scalping]]", "[[delta-hedging]]", "[[theta]]", "[[vega]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[iv-crush]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Strangle

A strangle is a two-leg [[options]] structure: an out-of-the-money [[call-option]] and an out-of-the-money [[put-option]] at **different strikes** but the **same expiration**. It is the canonical pure-volatility play — roughly zero net [[delta]] at entry, with large [[vega]] and [[gamma]] (long strangle) or large *negative* vega and gamma (short strangle). Where a [[straddle]] uses two ATM options at the *same* strike, the strangle separates the strikes to widen the structure: cheaper to buy, less premium to sell, with a wider zone of either profit or loss depending on direction. In crypto it is traded almost entirely on [[deribit]] BTC and ETH options.

This page is the **hub** for the strangle structure — construction, the long-vs-short comparison, and the crypto specifics common to both. The income-trader's full short-premium treatment lives on [[short-strangle]]; the long-vol playbook (long straddle and strangle together) lives on [[straddle-strangle]].

## Overview

The strangle's defining feature is the **gap between the two strikes** — a band of spot prices over which both options are OTM. The long-strangle owner *needs* spot to escape that band; the short-strangle seller *needs* it to stay inside.

| Variant | Action | Greeks at entry | Bet |
|---|---|---|---|
| **Long strangle** | Buy OTM call + buy OTM put | +vega, +gamma, −theta | Realized move exceeds what [[dvol|DVOL]] implies, in either direction |
| **Short strangle** | Sell OTM call + sell OTM put | −vega, −gamma, +theta | Realized move falls short of what DVOL implies |

Both share the same payoff *shape* — a "V" for the long, an inverted "V" with a flat top for the short — flipped in sign. The choice is fundamentally between paying for [[implied-volatility]] (long) or being paid for it (short). The two are **not** opposites in trader-time but in **regime-time**: the long is the trade for a [[volatility-regime|vol regime]] that has not yet expanded (DVOL low in its range, pre-catalyst); the short is the trade for a regime that has expanded and is now reverting (DVOL rich and stable).

## Construction

Strikes are chosen by [[delta]] rather than absolute distance from spot, which self-scales across underlyings and IV levels:

1. **Pick an expiry.** 21–45 [[time-to-expiration|DTE]] is the canonical window for short strangles; 30–90 DTE for long strangles, which need time for the thesis to play out.
2. **Pick a delta per side.** ~15–25 delta per wing is the crypto-standard band (wider than 16-delta equity strangles, because crypto's tail demands more distance). Long strangles are often bought closer (25–35 delta) to keep the breakeven moves attainable.
3. **Sell or buy each leg** on the same expiry: credit for the short, debit for the long.
4. **Breakevens at expiry** = upper strike + total premium (up); lower strike − total premium (down). The band between breakevens is wider than the strike gap by exactly the premium paid/received.

On Deribit each BTC option represents **1 BTC** and each ETH option **1 ETH**; options are **cash-settled to the Deribit index** at expiry — **no physical delivery, no assignment**. Premium is quoted/paid in the coin on inverse contracts, in USDC on the linear line (see *Crypto specifics*).

A typical BTC 30-DTE ~20-delta short strangle in a DVOL-50 environment might sell the 66,000 call and 54,000 put for a combined ~$3,300 credit per BTC. The corresponding *long* strangle, bought at the same strikes, costs that same $3,300 as a debit. The two are mirror images at entry.

## Payoff & breakevens

| Feature | Long strangle | Short strangle |
|---|---|---|
| Entry | Pay debit (call + put) | Receive credit (call + put) |
| Max profit | Large/unbounded as spot escapes the band | The credit received |
| Max loss | The debit paid (**defined**) | **Undefined** both directions |
| Wins when | Spot escapes the strike gap by more than the premium | Spot stays inside the breakevens |
| Breakevens | Upper strike + premium; lower strike − premium | Same formula, but the *profit* zone |

```
 Long strangle                Short strangle
 P&L                          P&L
  \                  /          ____________  <- max profit (credit)
   \                /          /            \
    \              /          /              \
 ____\____________/____      /                \____
     put K    call K        /  put K   call K   \
  (lose debit in the gap)   (lose without bound outside strikes)
```

Because crypto ATM IV is high (BTC DVOL commonly 40–60%), OTM premiums are rich and breakevens sit far apart in percentage terms — a high headline win rate for the short (paid for by larger tail losses), and a wide move required for the long (paid for by a smaller debit than the ATM straddle).

## Greeks profile

The two variants are exact reflections through the zero-P&L axis:

| Greek | Long strangle | Short strangle |
|---|---|---|
| [[delta]] | ≈ 0 at entry (rises with the move) | ≈ 0 at entry (non-directional) |
| Gamma | **Positive** — large moves accelerate gains | **Negative** — the tail that kills it in a shock |
| [[vega]] | **Positive** — a DVOL spike alone can profit it | **Negative** — a DVOL spike marks it down before spot moves |
| [[theta]] | **Negative** — the cost of waiting | **Positive** — the income engine |

The long variant is **long gamma / long vega / short theta**; the short is its mirror. The short harvests the [[variance-risk-premium]] that the long pays. See [[iv-crush]] for the DVOL contraction that helps the seller and hurts the buyer.

## Market view / when to use

| Condition | Long strangle | Short strangle |
|---|---|---|
| DVOL *low* in its trailing-year range | Favor — cheap convexity | Avoid — premium too thin |
| DVOL *high* and stable | Avoid — paying full price | Favor — rich premium, often crushes |
| A discrete crypto catalyst approaches (fork, ETF listing, unlock, FOMC/CPI) | Favor *if* DVOL not already bid up | Avoid until after the event |
| No directional view, range-bound tape | Either, by DVOL regime | Favor |
| Account too small for undefined risk | Long only (defined risk) | Use the [[iron-condor]] instead |
| A vol-shock just printed | Favor for the next leg | Favor *gradually*, into the post-shock DVOL decay |

The deeper rule: hold a long and a short strangle on the *same* expiry and they cancel; hold them across a **DTE ladder** and you have the foundation of [[calendar-spread|term-structure]] trades.

## Adjustments & management

- **Long — profit:** scale out half at ~100% gain on the debit; after a DVOL spike, sell *into* the spike (DVOL mean-reverts faster than price). **Time stop** at ~21 DTE if the catalyst has not fired; **loss stop** at −50% of the debit.
- **Short — profit:** buy back at ~50% of max credit; **time stop** before the final week; roll the tested wing away for a credit, or **cap the tail** by converting to an [[iron-condor]].
- **Both — delta-hedge on the perp:** flatten residual delta with the Deribit **perpetual**; the long variant harvests [[gamma-scalping|gamma]] around the hedge, the short pays it. The hedge leg pays/collects [[funding-rate|funding]].

## Crypto specifics

- **Venue & underlyings.** [[deribit]] is effectively "the market" for BTC/ETH options; liquid strangles beyond BTC/ETH are scarce. [[greeks-live]] is the standard workbench (surface, per-leg Greeks, block tape). Block minimums are 25 BTC / 200 ETH.
- **Inverse vs linear settlement.** Classic Deribit BTC/ETH options are **inverse (coin-margined)** — premium/P&L in the coin, so collateral moves with spot. **USDC-margined (linear)** options give clean USD P&L. Choose linear for pure vol exposure; inverse only if the embedded coin delta is intended.
- **[[dvol|DVOL]] regime.** DVOL is Deribit's 30-day forward IV index — the crypto VIX; it is the primary rich/cheap gauge for both variants. **DVOL and the IV surface come from Deribit / [[greeks-live]], not [[cryptodataapi|CryptoDataAPI]]** (CDA supplies the complementary regime/OI/GEX/funding context — see below).
- **24/7 and weekend gamma.** No session break: thin **weekend** liquidity produces air-pockets that are pure gamma — fuel for the long strangle, poison for the short. Gamma keeps working through weekends and holidays.
- **No [[section-1256-contracts|§1256]].** Offshore Deribit options get **no §1256 60/40 treatment** — US ordinary short-term rates; AU CGT/income by trader status. Coin-margined record-keeping is onerous.
- **Perp-funding interaction.** [[funding-rate|Funding]] shapes skew: richly positive funding firms call skew and cheapens puts, telling you which wing the leveraged crowd overbid and nudging strike selection.
- **Alt-option liquidity.** SOL and other alt options exist (Deribit; thinner OKX/Bybit) but are wide and shallow — express strangles on BTC/ETH, not illiquid alt chains.

## Risks

- **Short variant:** undefined tail — a gap/weekend move past a wing produces uncapped loss with no session break; DVOL spike (short vega); margin spiral / auto-liquidation; single-venue Deribit dependency; coin-margin non-linearity. Prefer the [[iron-condor]].
- **Long variant:** [[iv-crush|DVOL crush]] after a catalyst is the dominant way the long loses even on a real move; theta bleed in a quiet tape; wide bid-ask on wings plus taker fees (0.03% of underlying, capped at 12.5% of premium) raise the breakeven move; timing risk (too early bleeds theta, too late pays peak DVOL).
- **Both:** low base-rate discipline — the win/loss asymmetry (high win rate for the short, low for the long) rewards disciplined sizing over conviction.

## Worked crypto example

*Illustrative round numbers — not a recommendation or backtest.*

**Long strangle into a catalyst (BTC, 30 DTE).** BTC spot **$60,000**, [[dvol|DVOL]] **44** and in the lower third of its trailing-year range; a spot-ETF options-listing decision lands inside the month.
- Buy 1 BTC 66,000 call ≈ $1,900 + buy 1 BTC 54,000 put ≈ $1,900 → debit ≈ **$3,800**.
- Breakevens ≈ **$50,200 / $69,800**; max loss = $3,800.
- *Win:* the headline hits, BTC runs to $72,000 and DVOL pops to 55. The call is worth ≈ $6,300 plus remaining extrinsic; the structure marks ≈ $6,800 → profit ≈ **+$3,000 (+79%)**.
- *Loss:* both events pass quietly, BTC drifts to $61,000 and DVOL crushes 44 → 36. The structure marks ≈ $1,900 → loss ≈ **−$1,900 (−50%)** — the modal outcome, and why sizing is small.

**Short strangle in a quiet regime (BTC, 30 DTE).** BTC **$60,000**, DVOL **50** rich and stable, no catalyst. Sell the same 66,000 call / 54,000 put for a **$3,300 credit**; breakevens **$50,700 / $69,300**. If BTC stays $57k–$63k and DVOL drifts to 40, buy back at ≈ $1,500 → **+$1,800**. If BTC gaps to $72,000 on a weekend, buy back the tested call at ≈ $6,300 → **−$3,000+ uncapped** — the case the [[iron-condor]] wings exist to bound. Full treatment on [[short-strangle]].

## Getting the Data (CryptoDataAPI)

**DVOL and the raw IV surface come from Deribit / [[greeks-live]]** (Deribit products; CDA does not serve them). [[cryptodataapi|CryptoDataAPI]] supplies the **complementary** context for timing and sizing either variant — vol *regime*, options OI / max pain, dealer gamma, funding, and the catalyst calendar.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal); "compressed" flags cheap-vol setups to *buy*, "expanding/normal" flags rich-vol setups to *sell*
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory; short-gamma dealers amplify moves, long-gamma dealers dampen)
- `GET /api/v1/event/calendar` — forward catalyst calendar (buy vol before, avoid selling across)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (compare RV to DVOL)
- `GET /api/v1/backtesting/klines` — deep kline archive for RV backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run either strangle variant end-to-end (DVOL and the legs stay on Deribit / [[greeks-live]]):

- **Variant selector** — `GET /api/v1/volatility/regime`: `compressed` → buy the strangle; `expanding`/`normal` with rich DVOL → sell it (or the defined-risk [[iron-condor]]); `vol_shock` → long side only.
- **Strike inputs** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (which wing the leveraged crowd overbid) + `GET /api/v1/market-intelligence/options` (OI walls near candidate strikes).
- **Catalyst calendar** — `GET /api/v1/event/calendar` — buy before dated events, never sell across them.
- **Kill switch (short side)** — `GET /api/v1/volatility/regime/score` + `GET /api/v1/market-intelligence/liquidations` — automate the flatten trigger; the wing breach arrives on weekends.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) for band-escape frequency at candidate strike gaps; `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time regime states.

## Related

- [[short-strangle]] — the dedicated income-trader's page; full short-premium setup, management, and risk
- [[straddle]] — the ATM-strike sibling structure (same-strike, more premium, narrower breakevens)
- [[short-straddle]] — the ATM short-vol equivalent
- [[straddle-strangle]] — the long-volatility playbook (buying straddles and strangles)
- [[crypto-options-volatility-selling]] — the systematic short-vol book the short strangle anchors
- [[iron-condor]] — the defined-risk version of the short strangle (bought wings)
- [[iron-fly]] — the defined-risk version of the short straddle
- [[gamma-scalping]], [[delta-hedging]] — monetizing (long) or managing (short) the gamma
- [[dvol]], [[implied-volatility]], [[realized-volatility]] — the vol inputs
- [[iv-crush]] — the DVOL contraction that helps sellers and hurts buyers
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that shapes crypto skew

## Sources

- Natenberg, *Option Volatility and Pricing* (2nd ed.) — the structural Greeks of strangles and their relationship to straddles.
- Bakshi & Kapadia (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium" — the academic anchor for the short variant's expectancy (ports to crypto; see [[variance-risk-premium]]).
- [[deribit]] / [[greeks-live]] documentation — DVOL construction, IV surface, cash settlement, block minimums (25 BTC / 200 ETH), inverse vs USDC-margined contracts.
