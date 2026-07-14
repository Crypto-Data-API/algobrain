---
title: "Funding-Aware Position Sizing"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, risk-management, position-sizing, kelly, funding-rate, perpetual-futures, derivatives]
aliases: ["Funding-Aware Sizing", "Funding-Adjusted Kelly", "Carry-Adjusted Position Sizing", "Funding-Adjusted Sizing"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[kelly-for-strategies]]", "[[funding-rate]]", "[[position-sizing]]"]
difficulty: advanced
related: ["[[kelly-for-strategies]]", "[[kelly-criterion]]", "[[funding-rate]]", "[[funding-by-hour]]", "[[position-sizing]]", "[[perpetual-futures]]", "[[liquidation-price-aware-sizing]]", "[[crypto-perpetual-futures]]", "[[basis-trade]]", "[[funding-rate-arbitrage]]", "[[liquidation-cascade]]"]
---

# Funding-Aware Position Sizing

**Funding-aware position sizing** folds the [[funding-rate|perpetual funding rate]] into the sizing objective, treating it as an *ongoing carry* — a near-certain, continuously-accruing return or cost — rather than an afterthought paid at the funding snapshot. For a [[perpetual-futures|perp]] position, the quantity that should drive [[kelly-for-strategies|Kelly-style sizing]] is not the expected price drift alone but the **carry-adjusted drift**: expected price move *net of funding you pay or receive*. Because funding on crowded crypto perps routinely reaches 50-100%+ annualized — a magnitude comparable to the expected edge itself — ignoring it can flip a position from Kelly-positive to Kelly-negative.

## Funding Is Carry, Not Noise

The continuous-return [[kelly-criterion|Kelly]] fraction is `f* = μ / σ²` (see [[kelly-for-strategies]]). For a spot position `μ` is just expected price drift. For a *perp*, holding the position also generates a funding cash flow every interval:

- **Long + positive funding** → you *pay* funding (longs pay shorts). Carry is a drag.
- **Long + negative funding** → you *receive* funding. Carry is a tailwind.
- **Short + positive funding** → you *receive* funding. Carry is a tailwind.
- **Short + negative funding** → you *pay* funding. Carry is a drag.

Let `μ` be the expected annualized price drift of the underlying (your directional view) and `φ` the annualized funding rate (positive = longs pay shorts; see [[funding-rate]] for the 8h/1h conversions). The **carry-adjusted drift** entering Kelly is:

```
long  perp:  μ_eff = μ − φ
short perp:  μ_eff = −μ + φ

f* = μ_eff / σ²          (then apply fractional Kelly)
```

So a long's optimal size shrinks as funding rises, and a short's optimal size grows. The funding term sits *inside* the numerator with the same units as expected return — that is the whole point.

## Why Funding Deserves More Weight Than Drift

A crucial asymmetry: **`φ` is observable now; `μ` is a noisy forecast.** [[kelly-for-strategies]] insists on heavy shrinkage of `μ` because backtested edges are overstated. Funding needs *no* such shrinkage — today's rate is a fact, and the near-term path is highly autocorrelated. In the carry-adjusted numerator, the funding term is therefore the *more reliable* component. When `φ` is large relative to a shrunken `μ`, funding dominates the sizing decision:

```
μ_eff = μ_shrunk − φ          # μ_shrunk = (1 − λ)·μ_estimated, λ ≈ 0.3–0.7
```

A modest, uncertain price edge can be entirely erased by a large, certain funding cost. This is why funding-aware sizing frequently concludes "don't be long here" even when the price view is bullish — the carry makes the bet negative-expectancy.

## Sizing a Funding-Positive Long

When funding is strongly positive (crowded longs paying to hold), a long faces a triple penalty:

1. **Carry drag** — `μ_eff = μ − φ` shrinks or goes negative, cutting Kelly size directly.
2. **Crowding / cascade risk** — extreme positive funding *is* a crowding signal: an overleveraged long book vulnerable to a [[liquidation-cascade]]. The effective tail of `σ` is fatter than the trailing estimate, so size should shrink *further* than the drift term alone implies.
3. **Mean-reversion of funding** — extreme funding tends to normalize, often via a sharp long unwind — the exact scenario that liquidates crowded longs.

Practical response: when `φ` is in the top decile of its trailing distribution, treat positive funding as both a carry cost *and* a volatility/tail multiplier — apply an extra haircut on top of the carry-adjusted Kelly, or stand aside. Being long into 100%+ annualized funding is paying a large, certain fee to hold the most crowded, most cascade-prone side of the book.

## Sizing a Funding-Negative Position

When funding is negative (shorts pay longs; often fear-driven or post-crash), a long is *paid to hold*:

- `μ_eff = μ + |φ|` — the carry adds to expected return, so Kelly sizes the long *up*.
- Negative funding often coincides with capitulation/oversold conditions, where the price edge and the carry point the same way — a genuinely favorable setup.
- This is the sizing logic beneath the delta-neutral [[funding-rate-arbitrage]] / [[basis-trade]] carry harvest: the "position" is the funding stream itself, sized to the *variance of the funding P&L and the residual basis risk*, not to price drift (which is hedged away). For the pure carry trade, `μ_eff ≈ φ_net` and `σ` is the basis/execution risk, giving a much larger Kelly fraction than any directional bet — which is why funding carry can be run at higher size than outright longs.

Symmetrically, a funding-positive short is paid to hold; size it up, but respect that a crowded-long unwind can gap the price *up* against a short before the funding accrues.

## Choosing the Venue to Hold the Carry

Because funding is dispersed across venues (and settles on different clocks — 8h on CEXes, 1h on Hyperliquid), the *same* net exposure can carry very different funding depending on where it is held. Funding-aware sizing therefore has a routing corollary: once Kelly has set the size, **park the held leg on the venue whose funding is most favorable for your side**, subject to that venue's depth and per-venue capital limits (see [[cross-venue-execution-crypto]]). A long sized to `μ_eff` at one venue's funding may deserve a larger `f*` if it can be held where funding is less positive — the sizing and the venue choice are jointly optimized, not sequential.

Note also the distinction between the *predictable* and *realized* carry. The next funding payment is essentially known from the current rate; the carry over a multi-day hold is a forecast of a mean-reverting, stochastic series. Size the near-term carry with confidence, but do not extrapolate an extreme rate as if it will persist — it usually decays, often violently.

## Worked Example

Long ETH perp. Estimated annualized price drift `μ = 20%` (already shrunk from a rawer backtest number); realized vol `σ = 70%`.

| Scenario | Funding `φ` (annualized) | `μ_eff` | `f* = μ_eff/σ²` | Half-Kelly | Read |
|---|---|---|---|---|---|
| Neutral funding | +11% (baseline) | 20% − 11% = 9% | 0.09/0.49 ≈ 0.18 | ~9% | Small long; carry eats half the edge |
| Crowded longs | +60% | 20% − 60% = −40% | negative | 0 | **No long** — carry dwarfs edge; also cascade risk |
| Fear / capitulation | −40% | 20% + 40% = 60% | 0.60/0.49 ≈ 1.2 | ~60% | Large long — paid to hold, edge aligned |

The *same* bullish price view produces sizes ranging from a large long to no position at all, purely from the funding term. (Figures illustrative; `σ` for ETH runs ~60-90% annualized, funding extremes per [[funding-rate]].) Always apply fractional Kelly and cap leverage — see [[kelly-for-strategies]] — and cap size independently for [[liquidation-price-aware-sizing|liquidation distance]].

## Practical Workflow

1. **Pull current funding** for the venue you will trade (and the venue you will *hold* on — see [[funding-by-hour]] and cross-venue funding dispersion).
2. **Annualize it** to match `μ` and `σ` units (8h rate × 3 × 365; 1h rate × 24 × 365).
3. **Compute carry-adjusted drift** `μ_eff` with the sign rules above; keep funding un-shrunk, shrink `μ`.
4. **Kelly-size on `μ_eff/σ²`**, then apply half/quarter Kelly.
5. **Add a funding-extreme haircut** when `φ` is in its tail (crowding/cascade overlay).
6. **Re-check as funding drifts** — funding is dynamic; a position sized at neutral funding must be re-underwritten if funding spikes while held (funding accrues against you every interval regardless of price).
7. **Bound by liquidation distance**, not just Kelly — funding debits equity and can push a marginal position into liquidation absent any price move (see [[liquidation-price-aware-sizing]]).

## Common Mistakes

1. **Sizing on price view alone** and paying 60-100% annualized funding that erases the edge.
2. **Shrinking funding like you shrink `μ`** — funding is observed, not forecast; do not discount it.
3. **Forgetting funding accrues while held** — a position that was carry-neutral at entry can bleed if funding spikes mid-hold.
4. **Ignoring the crowding signal** — treating extreme funding as pure carry and missing that it flags cascade-prone positioning.
5. **Using the wrong interval** — mixing an 8h CEX rate with a 1h Hyperliquid rate without annualizing both.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — cross-exchange funding (Binance + Hyperliquid)
- `GET /api/v1/hyperliquid/funding-rates?coin=ETH&limit=100` — current + historical Hyperliquid funding (hourly)
- `GET /api/v1/derivatives/summary?coin=ETH` — all-in-one derivatives overview (funding, OI, long/short)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ETHUSDT&limit=500` — funding history for backtesting the carry term
- `GET /api/v1/backtesting/funding` — deep funding archive
- `GET /api/v1/derivatives/binance/history?days=90` — daily funding/OI/long-short series

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Category page: [[cryptodataapi-derivatives]] (funding), [[cryptodataapi-hyperliquid]] (hourly HL funding), [[cryptodataapi-backtesting]] (funding archive).

## Related

- [[kelly-for-strategies]] — the sizing objective this extends with a carry term
- [[kelly-criterion]] — the single-bet `f* = μ/σ²` foundation
- [[funding-rate]] — the carry being folded into the numerator
- [[funding-by-hour]] — snapshot timing that determines when carry is paid
- [[position-sizing]] — the broader sizing discipline
- [[liquidation-price-aware-sizing]] — the second binding constraint on perp size
- [[perpetual-futures]] / [[crypto-perpetual-futures]] — the instrument funding applies to
- [[basis-trade]] / [[funding-rate-arbitrage]] — the delta-neutral carry harvest sized on funding variance
- [[liquidation-cascade]] — the tail risk that extreme positive funding flags

## Sources

- Kelly (1956); Thorp (2006) — the log-growth sizing objective funding-adjusted here.
- General crypto derivatives knowledge; funding magnitudes and intervals per [[funding-rate]] and Binance/Hyperliquid documentation.
- CryptoDataAPI derivatives and backtesting funding endpoints for the data mapping.
