---
title: "5% OTM Put Overlay (Crypto)"
type: strategy
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, risk-management, crypto, indicators, derivatives, volatility, hedging]
aliases: ["5% OTM Put Overlay", "BTC Put Overlay", "Deribit Put Overlay", "Shallow OTM Put Hedge", "Crypto Put Protection Program"]
related: ["[[protective-puts]]", "[[long-volatility-strategies]]", "[[tail-hedging]]", "[[tail-risk-hedging]]", "[[vix-calls]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[crypto-options-volatility-selling]]", "[[funding-rate]]", "[[variance-risk-premium]]", "[[volatility-regime]]", "[[liquidation-cascade-fade]]", "[[risk-management]]"]
strategy_type: hybrid
timeframe: position
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
---

# 5% OTM Put Overlay (Crypto)

A **5% OTM put overlay** in crypto maintains long [[protective-puts|put options]] roughly 5% out-of-the-money on [[bitcoin|BTC]]/[[ethereum|ETH]] via [[deribit]], rolled at 30–60 [[days-to-expiration|DTE]], sized to spend a fixed small % of NAV per year on premium. It is the shallow, fast-monetising end of the crypto protective-put spectrum — cheaper (and less convex) than a near-the-money put, but far more active than a deep 20–40% OTM "tail" hedge. It offsets the left-tail exposure of a long-BTC/ETH book or of short-premium sleeves elsewhere (e.g. [[crypto-options-volatility-selling]]). **Important scaling caveat:** because 30-day BTC vol runs roughly 3–5× the S&P's, a *5% OTM* strike is much closer to the money in standard-deviation terms in crypto than in equities — it monetises on routine moves and is correspondingly more expensive. The genuinely "middle of the spectrum" crypto equivalent of the equity 5% overlay sits closer to **10–20% OTM** (see the scaled table below).

## No "VIX" component — this is a pure put overlay

Unlike the [[vix-calls|crypto long-vol overlay]], this program uses **only long puts** — there is no volatility-index leg, so the absence of a tradeable crypto vol future (DVOL is a reference index, not an instrument) does not constrain it. The only adaptation from the equity version is the underlying (BTC/ETH instead of SPX), the venue (Deribit), the settlement mechanics (coin- vs USDC-margined), the tax treatment (no §1256), and the **volatility scaling** of the strike distance.

## Quick Reference

| Parameter | Value |
|---|---|
| **Instrument** | Long puts on BTC / ETH (Deribit) |
| **Strike** | ~5% OTM (shallow) — but see vol-scaling note; the equity-equivalent "middle" is ~10–20% OTM in crypto |
| **DTE** | 30–60 days, rolled at ~15–20 DTE remaining |
| **Margin type** | USDC-margined (linear) for clean USD protection; inverse only if the coin delta is intended |
| **Premium budget** | Fixed small % of NAV per year (a hard, pre-committed line item) |
| **Notional coverage** | 80–150% of long-book (beta/BTC-weighted) notional |
| **Standalone expectancy** | Negative — it is insurance, not alpha |
| **Portfolio effect** | Cuts long-book max drawdown; releases stablecoin exactly when the book is impaired |
| **Tax** | **No [[section-1256-contracts|§1256]] shelter** — offshore Deribit contracts are ordinary gains |
| **Venue risk** | Single-venue (Deribit) concentration; does not hedge Deribit's own solvency |

### Where it sits in the crypto protective-put spectrum

Strike distances are **vol-scaled to crypto** (roughly 3–5× the equity equivalents):

| Hedge | Strike (crypto) | Cost (indicative) | Monetises on | Convexity / payoff per $ |
|---|---|---|---|---|
| Near-the-money protective put | ~0–3% OTM | Very high | Every wiggle (crypto wiggles are large) | Low — pays for noise |
| **5% OTM overlay (this page)** | ~5% OTM | High for crypto | Routine −5% to −12% moves (frequent) | Low–medium — shallow, active |
| Middle-of-spectrum overlay | ~10–20% OTM | Moderate | Garden-variety −15% to −30% drawdowns | Medium — the true equity-5% analog |
| Deep tail hedge | 30%+ OTM | Low | Cascades / black swans (2020-03, LUNA, FTX, 2025-10-10) | Very high — explosive in true tails |

All cost figures are indicative and regime-dependent — crypto skew and DVOL level drive them; see the disclaimer in Performance Characteristics.

## Why This Edge Exists

The overlay is *not* a positive-expectancy trade in isolation — it pays the [[variance-risk-premium|VRP]] to crypto vol sellers. Its portfolio value comes from timing and survivorship:

1. **Crypto drawdowns are frequent and violent.** BTC has drawdowns of 10%+ several times a year — an order of magnitude more often than the S&P. A shallow put rolled continuously monetises on most of them, providing cash without touching the core book.
2. **Long-crypto books cannot cheaply de-risk in a cascade.** Selling spot into a −20% weekend gap crystallises losses and pays wide spreads; a pre-positioned put monetises into cash instead. And unlike equities, leveraged crypto positions face *auto-liquidation* — the survivorship value of pre-positioned protection is larger.
3. **Favourable skew windows.** In positive-[[funding-rate|funding]] euphoria, crypto skew flips to *call*-skew, so downside puts can be bought relatively cheap — the opposite of equities' near-permanent put-skew.

The overlay is *not* an arbitrage — it costs money in expectation. It works because the buyer values cash in a stress event more than the premium in calm weeks.

## Null Hypothesis

Under the null that Deribit puts are fairly priced and the book has no special covariance with shocks, the overlay is a pure cost — a fixed % of NAV per year forgone, with breakeven only when realised tail magnitude exceeds implied. The crypto VRP is real and runs against the buyer. The program is justified only if (a) the holder believes their realised tail risk exceeds the market's implied tail (a defensible view given the 2020-03 / LUNA / FTX / 2025-10-10 record), or (b) they value cash payoff in a cascade at higher utility than premium cost in calm.

## Rules

### Sizing

| Parameter | Value | Notes |
|---|---|---|
| Strike distance | 5% OTM (shallow) | At BTC $60,000, buy $57,000 strike — but consider 10–20% OTM for the equity-equivalent "middle" |
| DTE at entry | 30–60 days | Shorter than the equity version because crypto vol is higher and reverts faster |
| Annual premium budget | Fixed small % of NAV | Hard "insurance line item"; fund from short-vol carry where possible |
| Notional coverage | 80–150% of BTC-weighted long book | Slight over-hedge for convexity |
| Margin type | USDC-margined (linear) | Clean USD payoff; inverse only if coin delta is intended |
| Rolling frequency | ~15–20 DTE remaining or −50% premium loss | Whichever first |

### Entry Mechanics

1. **Compute long-book notional.** Sum long BTC/ETH exposure; BTC-weight tilted alt books first (alt options are thin — hedge with BTC/ETH).
2. **Choose venue/margin.** Deribit BTC/ETH options; **USDC-margined (linear)** for USD protection.
3. **Strike selection.** Nearest listed strike ~5% below spot (or deeper per the vol-scaling note). Round to the Deribit strike interval.
4. **Expiry selection.** 30–60 DTE. Avoid weeklies (theta too hot for a continuous hedge) and 90+ DTE (vega too large for a shallow hedge).
5. **Position size.** N puts where N × strike × contract-size ≈ 80–150% of long-book notional.

### Rolling Mechanics

The overlay is continuously maintained — you do not "let it expire."

1. **Review at least weekly** (crypto moves fast; monthly is too slow).
2. **Roll trigger.** DTE ≤ ~15–20, OR premium decayed to ≤ 50% of entry value.
3. **Roll mechanics.** Sell the existing put, buy a new 30–60 DTE ~5% OTM put — a debit in calm regimes, possibly a credit if DVOL has expanded.
4. **Layer for smoothness.** Split into 3–4 tranches rolled on different weeks so the program is never wholly expiring at once (a hedge gap in crypto is dangerous — gaps happen on weekends).
5. **Vol-regime adjustment.** When [[dvol|DVOL]] is structurally elevated (high percentile / backwardation), trim size 25–50% (puts are expensive and skew rich) or float the strike deeper OTM; restore when DVOL normalises.

### Monetisation Rules

1. **Threshold trigger.** If spot falls ~5%+ from entry, the put is ATM/ITM — decide to monetise or hold for further downside.
2. **Partial monetisation.** Sell half when spot is 7–12% below entry strike; hold the rest as a continuing tail hedge. **Monetise faster than an equity hedger** — crypto vol reverts within days, sometimes hours.
3. **Re-establish the overlay.** Re-buy ~5% OTM puts at the *new* lower spot to keep the program alive through a multi-leg cascade — the "reset" that compounds the hedge.
4. **Cash deployment.** Add monetised cash back to the book at lower prices, buy more hedges, or hold as stablecoin dry powder.

## Implementation Pseudocode

```python
def crypto_put_overlay(
    long_book_notional_usd: float,
    nav_usd: float,
    annual_premium_budget_pct: float = 0.03,   # crypto is dearer than SPX; budget higher
    otm_pct: float = 0.05,                      # 0.05 shallow; 0.10-0.20 for equity-equivalent "middle"
    target_dte: int = 45,
    layers: int = 4,
):
    chain = deribit_chain("BTC")                # USDC-margined (linear)
    spot  = chain.spot
    strike = round_to_strike(spot * (1 - otm_pct))
    expiry = today + timedelta(days=target_dte)

    contracts_total = ceil(long_book_notional_usd / (strike * chain.contract_size))
    contracts_per_layer = ceil(contracts_total / layers)

    quote = chain.quote(strike=strike, expiry=expiry, right="P")
    annualised_cost = quote.mid * chain.contract_size * contracts_total * (365 / target_dte)
    if annualised_cost / nav_usd > annual_premium_budget_pct * 1.5:
        warn("Overlay over budget — DVOL/skew rich; float strike deeper OTM or trim size.")

    return Order("BUY", "BTC", "P", strike, expiry, qty=contracts_per_layer, margin="USDC")
```

## Indicators / Data Used

- BTC/ETH spot (continuous, 24/7)
- [[implied-volatility|IV]] / [[dvol|DVOL]] of 30–60 DTE ~5% OTM puts (the entry premium)
- **Put-side skew and [[funding-rate|funding]]** — informs whether the strike is rich or cheap (positive funding → cheaper downside puts)
- DVOL percentile — "buy" vs "wait" regime check
- BTC-weighted long-book notional — sizing denominator
- Realised drawdown of the long book — monetisation trigger

## Example Trade

**Reference: $5M long-BTC book, deploying overlay with BTC at $60,000.**

- Long book notional $5M. Annual premium budget 3% of NAV = $150K. Funding richly positive → downside puts relatively cheap.
- Buy ~5% OTM ($57,000-strike) BTC puts, 45 DTE, USDC-margined, sized to ~100% of book notional; this tranche costs ~$40K (≈0.8% of NAV — note how much dearer than the SPX equivalent, because 5% OTM is near-the-money in crypto vol terms).
- **Cascade:** an exchange-solvency headline gaps BTC −11% to $53,400 over a weekend; DVOL spikes 55 → 95. The $57K puts are deep ITM: the tranche marks ~3–4×.
  - Sell half at ~$120K captured; re-establish a new $50,700-strike (5% OTM at $53,400) overlay for the next leg.
  - Cash captured this leg net of the re-buy ≈ a meaningful fraction of the book's drawdown.
- Long book down ~11% = −$550K on the move; the overlay offsets a portion **and** funds a rebalance into cheaper BTC without a forced sale.
- **Recovery:** BTC bounces to $58K; overlay puts decay, roll forward as scheduled.

The overlay is *not* a profit centre — it offsets part of the drawdown and, crucially, supplies stablecoin liquidity to rebalance into the dip while leveraged longs are being liquidated around you.

## Performance Characteristics

> **No fabricated backtest.** The figures below are *qualitative orders of magnitude* describing the well-understood shape of a continuous crypto put-overlay (negative standalone carry, frequent shallow monetisations, drawdown compression at the portfolio level). They are illustrative, not the output of a specific backtest, and realised numbers depend heavily on the crypto [[volatility-skew|skew]] regime, DVOL level, roll discipline, and the drawdown path.

Characteristic profile of a ~5% OTM, 45-DTE rolling BTC/ETH overlay:

- **Calm-regime drag:** higher than the SPX analog — a shallow crypto put is expensive and monetises often, so continuous theta cost is material (potentially several % of NAV/year at full size). Floating the strike deeper OTM (10–20%) cuts this sharply.
- **Cascade monetisation:** a multiple (order of several×) on the premium spent *that cycle* — convex payoff, and it fires *frequently* in crypto.
- **Long-book max-drawdown reduction:** materially lower combined drawdown; the overlay clips the left tail and funds rebalancing while perp liquidations clear.
- **Standalone expectancy:** negative — by construction; insurance, not alpha.
- **Combined book + overlay:** typically improves risk-adjusted return vs the unhedged book because the hedge releases stablecoin exactly when the book is impaired.
- **Tax:** **no §1256 shelter** — offshore Deribit gains are ordinary; after-tax economics are worse than the SPX/XSP version, and coin-margined P&L record-keeping is onerous.

The takeaway is regime-dependent: in calm regimes a steady, budgeted drag; in cascades a fast, convex source of stablecoin. Judging it on calm-regime carry alone is the central error — it is a portfolio component, not a standalone strategy.

## Crypto specifics

- **Vol-scaled strikes** — 5% OTM is *near-the-money* in crypto vol terms; the equity-5% behaviour (monetise on garden-variety drawdowns, not noise) sits at ~10–20% OTM in crypto.
- **24/7 + weekend gaps** — the worst moves hit in thin weekend liquidity with no close; layered rolling to avoid a weekend hedge gap is essential.
- **Inverse (coin-margined) settlement** — coin-collateralised puts pay in a crashing currency; use USDC-margined (linear) for clean USD protection.
- **Perp-funding skew** — positive-funding euphoria makes downside puts cheap; the best entry windows are when the leveraged crowd is long calls.
- **Frequent monetisation** — crypto's high drawdown frequency means the overlay pays out far more often than an SPX overlay, but each payout is smaller relative to the (larger) drawdown.
- **Single-venue counterparty tail** — Deribit concentration; the overlay does not hedge Deribit's own solvency (an FTX-type venue failure needs a spot-put or exchange-token short).
- **On-chain / depeg tail** — stablecoin depegs and DeFi exploits are crypto-native left tails a spot price put only partially covers.
- **No §1256** — unlike SPX/XSP puts, no 60/40 blended tax treatment.

## Monitoring Checklist

Run at least weekly (and intraday during a cascade):

1. **Coverage ratio** — put notional still 80–150% of BTC-weighted long book?
2. **Strike distance** — has spot moved so the active layer is no longer ~5% OTM? Re-strike on the next roll.
3. **DTE ladder** — layers staggered, or bunched into one expiry (a hedge gap)?
4. **Budget tracking** — YTD premium vs the annual budget; if on pace to breach, float the strike deeper OTM rather than overspend.
5. **Roll trigger status** — any layer ≤ 15–20 DTE or ≤ 50% of entry premium? Roll it.
6. **Monetisation readiness** — if spot is within ~5% of the active strike, pre-decide the partial-monetisation and re-establishment plan before the move.
7. **Regime check** — [[dvol|DVOL]] percentile and [[funding-rate|funding]]; in elevated-DVOL regimes trim 25–50% or float the strike.

## What Kills This Strategy

1. **Skew steepening** — in bear/cascade regimes crypto put skew steepens and the 5% strike balloons in cost; cap the budget and float the strike deeper OTM.
2. **Slow grinding alt bleed** — a multi-month grind where each put expires before the strike is hit; deeper compounding-roll hedges address this better than a shallow overlay.
3. **Boring-vol regime** — frequent −5% moves but no large cascade means continuous theta cost with modest payoffs.
4. **Roll-timing / hedge gaps** — a weekend gap that hits just after a roll, before the new put has gamma, is the crypto version of the 2015 flash-crash overlay failure.
5. **Operational decay** — unreviewed programs drift in size vs the book.
6. **Inverse-settlement wrong-way risk** and **Deribit single-venue failure** — crypto-specific.

## Kill Criteria (risk discipline, not an alpha spec)

- Annual hedging cost exceeds the pre-set budget → float strike deeper OTM (10–20%) or pause.
- Zero effective monetisation across many months while the book has materially shrunk → review sizing/appropriateness.
- Combined book + overlay risk-adjusted return materially worse than unhedged over a long window → audit.

## Advantages

- **Frequent, fast monetisation** — crypto's high drawdown frequency means cash is realised often, on garden-variety moves.
- **Strict premium budget** — bounded, predictable cost.
- **Favourable entries** in positive-funding euphoria (cheap downside puts).
- **Liquid majors** — BTC/ETH Deribit puts execute at meaningful size.
- **Composable with short-vol income** — offsets the tail of [[crypto-options-volatility-selling|strangle/condor]] sleeves.
- **Preserves book compounding** without forcing realisation into a cascade.

## Disadvantages

- **Negative standalone expectancy** — costs money in calm regimes, and dearer than the SPX version because 5% OTM is near-the-money in crypto vol terms.
- **Lower convexity than deep-tail hedges** — a 40%+ cascade pays out less per dollar than a 30%+ OTM tail hedge.
- **Path-dependent monetisation** — slow grinds may never trigger a clean payout.
- **Roll mechanics matter** — naive fixed-date rolling loses to layered rolling; weekend gaps punish hedge gaps.
- **Skew can make the shallow strike unaffordable** in stressed regimes.
- **Inverse-settlement wrong-way risk, single-venue (Deribit) concentration, and no §1256 shelter** — crypto-specific drawbacks.

## Getting the Data (CryptoDataAPI)

The tradeable put chain, [[dvol|DVOL]], and IV surface come from **[[deribit|Deribit]]** / [[greeks-live|Greeks.live]] — CryptoDataAPI does **not** serve the option chain or DVOL. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, funding, and liquidation context used to time, size, and monetise the overlay.

**Live:**
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]]
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew driver; cheap-downside signal)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (monetisation timing)

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/backtesting/klines` — OHLCV archive for drawdown / realized-vol study

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

For DVOL and the full IV surface, use the Deribit API or [[greeks-live]]. Full catalog: [[cryptodataapi-market-intelligence]] and [[cryptodataapi-regimes]].

## Sources

- [[deribit]] / [[greeks-live]] documentation — BTC/ETH option chain, coin-margined vs USDC-margined (linear) settlement, DVOL.
- Equity origins (for the overlay logic that ports): Spitznagel, *Safe Haven* (2021); Cboe PUT/BXM index research; AQR research on the VRP and put-buying cost. Cited as the *methodological ancestor* — the crypto version changes underlying, venue, settlement, tax, and strike-scaling.
- Crypto tail record: 2020-03-12 ([[covid-crash]]), 2022-05 [[terra-luna-collapse|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 ([[2025-10-crypto-liquidation-cascade|liquidation cascade]]).

## Related

- [[protective-puts]] — the parent structure
- [[long-volatility-strategies]] — broader category this overlay sits within
- [[tail-hedging]], [[tail-risk-hedging]] — the deep-tail comparison and the broad discipline
- [[vix-calls]] — the long-vol (straddle/put-wing) overlay with an explicit vega leg
- [[dvol]] — the crypto vol benchmark that prices the puts
- [[deribit]], [[greeks-live]] — venue and analytics
- [[crypto-options-volatility-selling]] — the short-premium sleeve this overlay offsets
- [[funding-rate]] — the crypto skew driver (cheap-downside signal)
- [[variance-risk-premium]] — the premium the overlay buyer pays
- [[volatility-regime]] — regime detection for entry/trim decisions
- [[liquidation-cascade-fade]] — the cascade dynamic the overlay monetises into
- [[risk-management]] — portfolio-protection framework
