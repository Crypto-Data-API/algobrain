---
title: "Short Straddle"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, short-straddle, premium-selling, volatility, neutral, derivatives]
aliases: ["Crypto Short Straddle", "BTC Short Straddle", "Selling the Straddle", "ATM Premium Selling"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[short-strangle]]", "[[straddle]]", "[[straddle-strangle]]", "[[crypto-options-volatility-selling]]", "[[iron-condor]]", "[[iron-fly]]", "[[gamma-scalping]]", "[[delta-hedging]]", "[[theta]]", "[[vega]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[iv-crush]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Short Straddle

## Overview

The short straddle is the **maximum-premium-collection** option structure: sell an at-the-money [[call-option]] and an at-the-money [[put-option]] at the **same strike** and expiration, banking both credits. In crypto this is traded almost entirely on [[deribit]] BTC and ETH options. The position profits when spot stays pinned near the strike so both legs decay via [[theta]] and — the crypto-specific tailwind — when [[dvol|DVOL]] contracts after entry. It is the concentrated, ATM expression of [[crypto-options-volatility-selling|selling volatility]]: the seller collects the [[variance-risk-premium]] the [[straddle-strangle|long-straddle]] buyer pays, and wins only when realized volatility comes in under the implied vol embedded in the premium.

The catch is severe and crypto makes it worse: the short straddle is **short gamma and short vega with undefined risk in both directions**. A large move turns one leg into an uncapped liability, and crypto's 24/7, gap-prone tape (2020-03, LUNA, FTX, 2025-10-10) delivers exactly the moves that punish it. It is the archetypal *high-win-rate, negatively-skewed* trade — "picking up pennies in front of a steamroller" — and demands hard sizing and active management. The wider, more forgiving cousin is the [[short-strangle]]; the defined-risk version is the [[iron-fly]].

## Construction

Sell one ATM call and one ATM put, same strike `K ≈ S` (spot), same expiry `T`:

- Sell 1 ATM call (strike `K`, delta ≈ +0.5)
- Sell 1 ATM put (strike `K`, delta ≈ −0.5)
- Credit = call premium + put premium. Because both legs are ATM, the credit ≈ the market's expected absolute move over `T` (the Black-Scholes ATM-straddle approximation) — so the credit *is* your read on how much movement DVOL is pricing.

On Deribit each BTC option represents **1 BTC** and each ETH option **1 ETH**; options are **cash-settled to the Deribit index** at expiry — there is **no physical delivery and no assignment mechanics**, a genuine structural advantage over US single-stock short puts/calls. Premium on classic inverse contracts is quoted and paid **in the coin** (BTC/ETH); on the USDC-margined line it is quoted in **USDC** (see *Crypto specifics*).

| Choice | Short straddle | Short strangle |
|---|---|---|
| Strikes | Both at `K ≈ S` | Split OTM (`K_p < S < K_c`) |
| Credit collected | Higher (ATM is dearest) | Lower |
| Profit zone | Narrow (a point) | Wide (a band) |
| Short gamma | Highest, concentrated at `K` | Lower, spread across two strikes |

## Payoff & breakevens

Defined, capped reward (the credit) and **undefined risk** both ways. Payoff at expiry, credit `C`:

- P&L = `C − max(S_T − K, 0) − max(K − S_T, 0)`
- Max profit = `C`, at `S_T = K` (both legs expire worthless)
- Upper breakeven = `K + C`
- Lower breakeven = `K − C`
- Max loss = **unbounded** as `S_T` runs away from `K` in either direction — an inverted "V" that falls without limit.

Because crypto ATM implied vol is high (BTC DVOL commonly 40–60%, versus [[vix|VIX]] in the teens), the credit is large and the breakevens are **wide in percentage terms** — a 30-day BTC straddle can bank ~10–13% of spot as credit. That fat premium is the appeal; the fat tail that justifies it is the risk.

## Greeks profile

A short straddle is a stacked short-call + short-put, so the Greeks add with the sign flipped versus a long straddle:

| Greek | Short straddle | Comment |
|---|---|---|
| [[delta]] | ≈ 0 at inception | ATM call −0.5 offsets ATM put +0.5; a non-directional bet |
| Gamma | **Negative** (largest ATM) | The danger: losses accelerate as spot moves, worst into expiry |
| [[vega]] | **Negative** | A DVOL/IV spike marks the book down *before* spot even moves |
| [[theta]] | **Positive** | The engine: both legs decay every day spot stays near `K` |
| Rho | Small | Minor in crypto's typical tenors |

The position is **short gamma / short vega / long theta**. Two ways to win: spot pins the strike (theta accrues) and/or DVOL contracts (vega gain), letting you buy the structure back cheaper. The enemy is a decisive move (short gamma bleeds via the tested leg) or a DVOL spike (short vega loses even if you are eventually right on direction). See [[iv-crush]] for the mechanism working *for* the seller — and its violent reverse.

## Market view / when to use

Sell a short straddle when you expect **realized vol to come in under implied**, specifically:

- **When [[dvol|DVOL]] sits in the upper part of its range** (say > ~60–70th percentile of the trailing year) so implied vol is *rich* and the [[volatility-regime|vol regime]] is "expanding/normal" rather than a live vol-shock. Selling rich vol is the whole edge; selling cheap vol has no cushion.
- **Into a range-bound, catalyst-free window.** Avoid selling ATM straddles across a known discrete catalyst (major protocol upgrade or hard fork, spot-ETF option-listing decision, large token unlock, US [[fomc]]/CPI print) unless the *post-event DVOL crush* is explicitly the trade and you have sized for the gap.
- **Straddle vs strangle choice:** the short straddle when you want maximum credit and DVOL is very rich, and you can defend a narrow profit zone actively; the [[short-strangle]] when you want a wider, higher-probability zone at the cost of less premium; the [[iron-fly]] when you want the same ATM concavity with a defined, capped tail.

Do not sell into an already-spiking DVOL — that is selling a falling knife of vega, exactly the regime where the tail is arriving. The ideal entry is rich-but-stable vol that is about to mean-revert down.

## Adjustments & management

- **Profit target:** buy back at ~**25–50% of max credit**; do not hold ATM into the final days for the last few percent while gamma balloons.
- **Roll the tested side:** as spot pushes toward one strike, roll that leg out/away for a credit to recenter, or roll the whole straddle out in time.
- **Delta-hedge on the perp:** flatten the residual delta with the Deribit **perpetual** (or dated future). This converts the static short-vol bet into a managed one; note the hedge leg pays/collects [[funding-rate|perp funding]] — a tailwind when you are short delta into positive funding.
- **Time stop:** close or roll before the [[theta]]-heavy final week; crypto gamma accelerates hard into expiry because gaps are unbounded and continuous.
- **Cap the tail:** convert to an [[iron-fly]] by buying protective wings, or to a [[short-strangle]] by rolling the strikes apart — both trade credit for survivability, strongly preferred in crypto.
- **Kill on a DVOL spike:** if DVOL jumps hard intraday, flatten rather than average down — this is the tail the structure exists to avoid.

## Crypto specifics

- **Venue & underlyings.** [[deribit]] is effectively "the market" for BTC and ETH options; liquid ATM straddles beyond BTC/ETH barely exist. [[greeks-live]] is the standard workbench for building and monitoring the position (surface, per-leg Greeks, block tape). Block minimums are 25 BTC / 200 ETH.
- **Inverse vs linear settlement.** Classic Deribit BTC/ETH options are **inverse (coin-margined)**: premium and P&L are denominated in the coin, so your *collateral itself* moves with spot — a short straddle held in BTC collateral carries an embedded currency effect. Deribit's **USDC-margined (linear)** options give clean USD P&L. Use linear when you want the payoff to be pure short-vol; use inverse only if the embedded coin delta is intended.
- **[[dvol|DVOL]] regime as the "rich/cheap" gauge.** DVOL is Deribit's 30-day forward implied-vol index — the crypto VIX. Sell when DVOL is high in its own history and stable. **DVOL and the raw IV surface come from Deribit / [[greeks-live]], not from [[cryptodataapi|CryptoDataAPI]]** (CDA supplies the complementary regime/OI/GEX/funding context — see below).
- **24/7 and weekend gamma.** Crypto never closes, so there is no overnight-gap *cap* the way equities gap only at the open. Thin **weekend** liquidity produces sudden air-pockets — pure short-gamma poison for a naked straddle, because there is no session break to halt the move.
- **No [[section-1256-contracts|§1256]].** Offshore Deribit options get **no §1256 60/40 treatment**. In the US these are ordinary capital-gains events (short-term at full marginal rates); AU treatment is CGT/income depending on trader status. Coin-margined P&L record-keeping is onerous.
- **Perp-funding interaction.** [[funding-rate|Perp funding]] shapes the skew: richly positive funding (crowded leveraged longs) firms call skew and cheapens puts, nudging where the ATM structure is most exposed and mattering when you delta-hedge on the perp.
- **Alt-option liquidity.** Options on SOL and other alts exist (Deribit, thinner OKX/Bybit) but bid-ask is wide and depth shallow; short straddles on alts are gap-prone and best avoided in favor of BTC/ETH.

## Risks

- **Gap / weekend move** past a breakeven — the dominant failure mode; short gamma turns a move into an uncapped loss with no session break to stop it.
- **[[iv-crush|DVOL/IV spike]]** (short vega) that marks the position down before spot even moves — you can be right on direction and still lose.
- **Margin spiral / auto-liquidation:** a DVOL spike multiplies Deribit portfolio-margin; if you cannot top up, the venue force-closes at the worst tick.
- **Coin-margin non-linearity** on inverse contracts — collateral and payoff both move with spot.
- **Single-venue concentration:** a Deribit outage during a vol event is an un-hedgeable risk.
- **Low base-rate discipline:** the high win rate masks negative skew; one gap can erase months of credits, so size risk small (≤ 1–2% of book stress loss per structure) and prefer the defined-risk [[iron-fly]].

## Worked crypto example

*Illustrative round numbers — not a recommendation or backtest.*

**Setup (BTC, 30 DTE).** BTC spot **$60,000**. [[dvol|DVOL]] **55** and sitting in the upper third of its trailing-year range (a rich, stable [[volatility-regime|vol regime]]); no discrete catalyst inside the window. Direction range-bound.

**Trade — short straddle (USDC-margined, linear):**
- Sell 1 BTC 60,000 call ≈ **$3,750**
- Sell 1 BTC 60,000 put ≈ **$3,750**
- Credit ≈ **$7,500** per 1-BTC straddle (≈ 12.5% of spot)
- Breakevens: **$52,500** and **$67,500**; max profit = $7,500 at $60,000; max loss unbounded.

**Path A — pin + DVOL crush (the win).** Over three weeks BTC oscillates $58k–$61k and DVOL drifts 55 → 42. The call marks ≈ $2,600, the put ≈ $1,700 → buy back for ≈ $4,300. Profit ≈ **+$3,200 (≈43% of credit)** — close at the profit target rather than holding ATM gamma into expiry.

**Path B — weekend gap (the loss).** BTC gaps to **$70,000** over a thin weekend. Call ≈ $10,000, put ≈ $0 → buy back for ≈ $10,000. Loss ≈ **−$2,500**, and had it run to $75,000 the loss would be **−$7,500+** with no cap. This is why the structure is sold small, delta-hedged, and — in crypto — usually run as a defined-risk [[iron-fly]] instead of naked.

## Getting the Data (CryptoDataAPI)

**DVOL and the raw IV surface come from Deribit / [[greeks-live]]** (the 30-day DVOL index and the IV surface are Deribit products; CDA does not serve them). [[cryptodataapi|CryptoDataAPI]] supplies the **complementary** context used to time and manage a short-vol entry — the vol *regime*, options OI / max pain, dealer gamma, funding, and the catalyst calendar.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal); sell into "expanding/normal", stand aside on "vol_shock"
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (pin/positioning context)
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory; long-gamma dealers dampen the tape a short straddle wants pinned)
- `GET /api/v1/event/calendar` — forward catalyst calendar (unlocks / macro / listings) to *avoid* selling across events
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning for the kill decision)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (compare RV to DVOL to judge whether vol is rich)
- `GET /api/v1/backtesting/klines` — deep kline archive for RV backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[short-strangle]] — the wider, more forgiving short-premium cousin
- [[straddle]] — the conceptual umbrella (long vs short, definition, Greeks)
- [[straddle-strangle]] — the long-volatility mirror (buying this structure)
- [[crypto-options-volatility-selling]] — the systematic short-vol book this ATM structure sits inside
- [[iron-fly]] — the defined-risk version of the short straddle
- [[iron-condor]] — defined-risk version of the short strangle
- [[gamma-scalping]], [[delta-hedging]] — how to manage the short gamma
- [[dvol]], [[implied-volatility]], [[realized-volatility]] — the vol inputs
- [[iv-crush]] — the DVOL contraction the seller wants (and its reverse)
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that shapes crypto skew

## Sources

- Natenberg, *Option Volatility and Pricing* (2nd ed.) — straddle mechanics, the implied-vs-realized relationship, and gamma's role in short-volatility positions.
- McMillan, *Options as a Strategic Investment* (5th ed.) — straddle construction, management, and defense.
- [[deribit]] / [[greeks-live]] documentation — DVOL construction, IV surface, cash settlement, block minimums (25 BTC / 200 ETH), inverse vs USDC-margined contracts.
