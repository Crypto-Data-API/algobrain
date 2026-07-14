---
title: "Crypto Portfolio Heat"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, portfolio-theory, risk-management, correlation, altcoins, bitcoin, position-sizing]
aliases: ["Crypto Portfolio Heat", "Beta-Weighted Crypto Exposure", "Crypto Directional Heat", "BTC-Beta Budgeting"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[correlation-breakdown]]", "[[crypto-allocation]]", "[[diversification]]"]
difficulty: advanced
related: ["[[correlation-breakdown]]", "[[risk-budgeting]]", "[[crypto-allocation]]", "[[correlation]]", "[[correlation-regime]]", "[[diversification]]", "[[position-sizing]]", "[[capital-asset-pricing-model]]", "[[bitcoin]]", "[[multi-strategy-crypto-portfolio]]"]
---

# Crypto Portfolio Heat

**Crypto portfolio heat** is the aggregate *directional* crypto exposure of a book measured in **BTC-beta terms** — the effective size of the single risk-on/risk-off bet you are really holding once nominally-different altcoin longs are collapsed onto their common factor. A trader holding eight "diversified" alt longs across DeFi, L2s, AI tokens, and memecoins *feels* spread out, but in a crash those correlations spike toward +1 (the crypto instance of [[correlation-breakdown]]) and the book behaves as one large levered BTC-beta position. Heat is the discipline of measuring that true exposure and capping it, so the portfolio's stress loss matches what was intended rather than a multiple of it.

## The Core Problem: Fake Diversification

Crypto is unusually prone to fake diversification because its assets share a dominant common factor — overall crypto risk appetite, proxied by BTC — even in calm conditions, and almost exclusively in stress:

- **Calm regime:** large alts (ETH, SOL) run [[correlation]] to BTC of roughly 0.6-0.8; smaller alts and memecoins are noisier but still positively coupled. Some genuine idiosyncratic dispersion exists.
- **Stress regime:** pairwise correlations across the alt complex spike to ~0.85-0.95. Idiosyncratic stories evaporate; everything trades on one axis — down together, hard. This is the same [[correlation-breakdown]] mechanism documented in equities, but *faster and more complete* in crypto because the holder base, leverage, and liquidation plumbing are shared.

The consequence, straight from the [[correlation-breakdown|effective-number-of-bets]] formula:

```
N_effective = N / (1 + (N − 1) · ρ̄)
```

Eight alt longs with average crash correlation `ρ̄ = 0.9` give `N_eff = 8 / (1 + 7·0.9) ≈ 1.1` — barely more than one independent bet. The "diversified" book is a single BTC-beta position wearing eight tickers.

## Beta-Weighted Exposure

To measure heat, convert each position's dollar exposure into **BTC-equivalent** exposure via its beta to BTC:

```
β_i = beta of asset i to BTC (from regression of returns)
beta_weighted_exposure_i = w_i × β_i        # w_i = signed dollar (or % NAV) exposure

crypto_heat = Σ_i ( w_i × β_i )             # net directional heat
gross_heat  = Σ_i | w_i × β_i |             # gross single-factor exposure
```

- **Net heat** captures directional tilt (longs minus shorts, beta-adjusted). A book that looks market-neutral in dollars can carry large net heat if the longs are high-beta alts and the shorts are low-beta.
- **Gross heat** is what matters in a crash: when `ρ → 1`, longs and shorts on the *same* side of the risk-on/off axis stop offsetting, and even a "hedged" alt-vs-alt pair can lose on both legs. Gross beta-weighted exposure is the honest measure of how much single-factor risk is really on.

Crucially, **use stressed beta, not trailing calm beta.** Just as sizing on calm correlations understates crash variance, budgeting on calm beta understates crash exposure. A pragmatic recipe (mirroring the [[correlation-breakdown]] stress re-run): floor every alt's beta at ~1.0 and set correlations to 0.9 when computing the heat you must survive.

### Estimating Beta Robustly

Raw regression beta for small-cap alts is noisy and unstable, so the heat number needs robust inputs:

- **Downside (semi-)beta over full-sample beta.** Crypto betas are asymmetric — an alt that lags BTC on the way up often falls *harder* on the way down. Estimating beta on down-days only gives a more honest crash-exposure figure than a symmetric regression.
- **Shrink toward 1.0.** Thinly-traded alts produce unreliable betas; pull the estimate toward the sector average (≈1) rather than trusting a low point estimate that a crash will overturn.
- **Include the memecoin/small-cap "to-zero" risk.** Beta understates the tail for names that can lose 80-100% in a cascade regardless of BTC's move; treat such positions' effective downside beta as materially above their fitted value.
- **Refit on rolling and crash windows.** Track both a rolling calm-window beta and a crash-window beta (COVID, May 2021, the 2025 cascade); budget on the latter.

## Total Directional Heat Limits

Heat is a budget to be set and spent. Practical limits, layered:

- **Total gross heat cap** — e.g. beta-weighted crypto exposure ≤ 1.0-1.5× NAV for a directional book. This is the "how big is my real BTC bet, including everything?" ceiling.
- **Net heat cap** — bound the directional tilt separately (e.g. |net heat| ≤ 1.0× NAV), so a stack of correlated longs cannot quietly become a maximally-long book.
- **Per-narrative sub-limits** — cap heat *within* each theme (DeFi, L2, AI tokens, memecoins). Eight AI tokens are one bet, not eight; the sub-limit prevents a single narrative from consuming the whole budget under the illusion of ticker diversity.
- **Variance-share cap** — alternatively, size so crypto contributes no more than a target share of total portfolio variance (see [[crypto-allocation]]); because crypto vol is ~50-90% annualized, a small dollar weight already spends a large variance budget.

The limits bind on the *stressed* heat number. A book at 0.8× net heat on calm betas can be 1.3× on stressed betas — the second figure is the one that will actually show up in a drawdown.

## Beta-Weighted Exposure Budgeting

Heat integrates with [[risk-budgeting]] by spending a fixed beta-weighted budget rather than a dollar budget:

1. **Set the heat budget** — the maximum gross beta-weighted crypto exposure the book will carry (the cap above).
2. **Price each candidate position in heat** — `w_i × β_i^stressed`, not dollars.
3. **Allocate against the budget** — every new long spends heat; the budget is full when gross beta-weighted exposure hits the cap, regardless of how many tickers or narratives are involved.
4. **Reserve budget for convexity/hedges** — a BTC or index short, or long-vol structure, *returns* heat to the budget (negative beta-weighted exposure) and buys room for more idiosyncratic longs.
5. **Re-measure on regime change** — when a [[correlation-regime|correlation regime]] shift or fragility spike is flagged, recompute heat with crash betas; positions that looked cheap in heat get expensive as betas converge.

This reframes "how many coins can I hold?" as "how much single-factor risk can I hold?" — the correct question, because in a crash the ticker count is irrelevant and only the beta-weighted total survives contact.

## Worked Example

A $1M book holds five "diversified" alt longs, sized 20% NAV each ($200k), plus a $150k BTC short as a "hedge":

| Position | Dollar exposure | Calm β to BTC | Stressed β | Heat (stressed) |
|---|---|---|---|---|
| ETH long | +$200k | 1.0 | 1.1 | +$220k |
| SOL long | +$200k | 1.2 | 1.3 | +$260k |
| DeFi basket long | +$200k | 1.3 | 1.4 | +$280k |
| AI-token long | +$200k | 1.5 | 1.6 | +$320k |
| Memecoin long | +$200k | 1.8 | 2.0 | +$400k |
| BTC short ("hedge") | −$150k | 1.0 | 1.0 | −$150k |
| **Net heat** | | | | **+$1.33M** |

The book *feels* like $1M of exposure with a hedge; in stress it is **1.33× NAV of net BTC-beta** — the small BTC short barely dents it, and the high-beta memecoin/AI longs dominate. If the heat cap is 1.0× NAV, the book is ~33% over-budget on stressed heat and must cut the highest-beta longs (or grow the BTC short) before the next drawdown. (Betas illustrative.)

## Common Mistakes

1. **Counting tickers as bets** — eight alts in one narrative is ~1 effective bet in a crash.
2. **Budgeting in dollars, not beta** — equal dollar weights hide that a memecoin long is 2× the heat of an ETH long.
3. **Using calm beta** — trailing beta understates the crash exposure the limit is supposed to control.
4. **Treating alt-vs-alt as a hedge** — when `ρ → 1`, both legs can lose; only genuinely negative-beta exposure (a BTC/index short, long vol, cash) removes heat.
5. **Ignoring leverage in the heat total** — beta-weighted exposure must include notional from perps and margin, not just spot dollars.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/altcoin-breadth` — % of coins above their MA; a market-wide proxy for how uniformly the alt complex is moving (breadth collapse ≈ correlations converging)
- `GET /api/v1/quant/coins/risk` — bulk per-coin risk model for the perp universe
- `GET /api/v1/liquidity/regime/score` — composite fragility band (when to switch to stressed betas)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=365` — daily returns to estimate each asset's beta to BTC (calm and stressed windows)
- `GET /api/v1/backtesting/klines` — deep OHLCV archive to fit crash-window betas across drawdowns

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-market-health]] (breadth), [[cryptodataapi-regimes]] (fragility/quant risk), [[cryptodataapi-market-data]] / [[cryptodataapi-backtesting]] (klines for beta estimation).

## Related

- [[correlation-breakdown]] — why the alt complex converges to one bet in stress
- [[risk-budgeting]] — the framework heat plugs into (beta-weighted, not dollar-weighted)
- [[crypto-allocation]] — sizing the crypto sleeve on a risk-contribution basis
- [[correlation]] / [[correlation-regime]] — the coupling that drives heat and its regime dependence
- [[diversification]] — the benefit that fails inside a single asset class
- [[position-sizing]] — the per-position discipline heat aggregates
- [[capital-asset-pricing-model]] — the beta concept borrowed for BTC-beta weighting
- [[bitcoin]] — the common factor everything is weighted to
- [[multi-strategy-crypto-portfolio]] — the book-level strategy that enforces heat limits across sleeves

## Sources

- Longin & Solnik (2001); Ang & Chen (2002) — correlation asymmetry in stress (via [[correlation-breakdown]]).
- Crypto internal-correlation observations (2020-2025 drawdowns): alt-BTC correlations 0.6-0.8 calm, 0.85-0.95 in crashes.
- General portfolio-theory knowledge; CryptoDataAPI breadth/klines endpoints for beta estimation.
