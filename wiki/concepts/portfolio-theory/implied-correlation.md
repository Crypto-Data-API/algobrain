---
title: "Implied Correlation"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [correlation, portfolio-theory, options, implied-volatility, dispersion, vega]
aliases: ["Implied Correlation", "Index-Implied Correlation", "CBOE Implied Correlation Index", "KCJ", "ICJ", "COR1M", "COR3M"]
domain: [portfolio-theory, options]
prerequisites: ["[[correlation]]", "[[implied-volatility]]", "[[options-greeks]]"]
difficulty: advanced
related:
  - "[[correlation]]"
  - "[[correlation-breakdown]]"
  - "[[implied-volatility]]"
  - "[[volatility-surface]]"
  - "[[options-concentration-risk]]"
  - "[[variance-risk-premium]]"
  - "[[vega]]"
  - "[[vix]]"
  - "[[skew]]"
  - "[[long-vol-vs-short-vol]]"
  - "[[diversification]]"
  - "[[modern-portfolio-theory]]"
---

Implied correlation is the average pairwise correlation among the components of an equity index that is implicit in the relative pricing of index options versus options on the components. It is to correlation what [[implied-volatility]] is to volatility: a market-derived expectation of a future statistical quantity, extracted by inverting an option-pricing relationship. Where [[correlation|realised correlation]] looks backward over a sample of returns, implied correlation looks forward over the residual life of a chosen option tenor — and like all forward-looking implied quantities, it carries a [[variance-risk-premium|risk premium]] that traders systematically harvest through dispersion structures.

## Definition and Derivation

The variance of an index return can be decomposed into the variances of its components and the pairwise correlations among them:

```
σ²_index = Σᵢ wᵢ² σᵢ² + 2 Σᵢ<ⱼ wᵢ wⱼ ρᵢⱼ σᵢ σⱼ
```

If we assume a *single* average pairwise correlation ρ across all component pairs (the "average implied correlation" approximation), the relation simplifies to:

```
σ²_index = Σᵢ wᵢ² σᵢ² + ρ × 2 Σᵢ<ⱼ wᵢ wⱼ σᵢ σⱼ
```

Solving for ρ:

```
ρ_implied = (σ²_index - Σᵢ wᵢ² σᵢ²) / (2 Σᵢ<ⱼ wᵢ wⱼ σᵢ σⱼ)
```

In this formula:

- σ_index is the at-the-money implied vol of the index option (e.g. SPX 30-day ATM)
- σᵢ is the at-the-money implied vol of single-name option i at the same tenor
- wᵢ is the index weight of component i

The numerator is the "extra" index variance not explained by the cap-weighted sum of squared single-name variances; the denominator is the maximum extra variance that would arise if every pair correlated at +1. The ratio is therefore the average pairwise correlation implied by the option market.

In practice, traders compute this on the top-N largest-weighted components of the index (typically top 30-50 of the S&P 500), which captures most of the index variance while keeping the calculation tractable.

### Worked example (illustrative, equal-weight toy basket)

Take a simplified 3-name equal-weight index (w = 1/3 each) with single-name ATM implied vols and an observed index ATM implied vol:

| Quantity | Value |
|----------|-------|
| σ₁, σ₂, σ₃ (single-name ATM IV) | 30%, 35%, 40% |
| weights w₁, w₂, w₃ | 1/3 each |
| σ_index (observed index ATM IV) | 24% |

Step 1 — idiosyncratic floor (Σ wᵢ² σᵢ²):
```
(1/9)(0.30² + 0.35² + 0.40²) = (1/9)(0.09 + 0.1225 + 0.16) = (1/9)(0.3725) = 0.04139
```
Step 2 — cross term denominator (2 Σᵢ<ⱼ wᵢ wⱼ σᵢ σⱼ):
```
2 × (1/9) × (0.30·0.35 + 0.30·0.40 + 0.35·0.40)
= (2/9) × (0.105 + 0.120 + 0.140) = (2/9)(0.365) = 0.08111
```
Step 3 — solve ρ_implied:
```
ρ = (σ²_index − floor) / cross = (0.24² − 0.04139) / 0.08111
  = (0.0576 − 0.04139) / 0.08111 = 0.01621 / 0.08111 ≈ 0.20
```

The option market is pricing an **average pairwise implied correlation of ~0.20** — a "quiet tape / stock-pickers' market" reading. If the index IV instead printed 32% (σ²_index = 0.1024), ρ would solve to ≈ 0.75 — a stress-level reading from the *same* single-name vols, illustrating how implied correlation is the lever that translates index vol into a systematic-vs-idiosyncratic split. (Figures are illustrative arithmetic, not market data.)

## CBOE Implied Correlation Indices

The CBOE has published several official implied correlation indices that institutionalise this calculation:

| Symbol | Index | Tenor | Status |
|--------|-------|-------|--------|
| KCJ | S&P 500 Implied Correlation (Jan-expiry methodology) | ~1 year | Discontinued |
| ICJ | S&P 500 Implied Correlation (Jul-expiry methodology) | ~1 year | Discontinued |
| JCJ | S&P 500 Implied Correlation (Jan-expiry, alt vintage) | ~1 year | Discontinued |
| COR1M | CBOE 1-Month Implied Correlation | 30 days | Current methodology (post-2021) |
| COR3M | CBOE 3-Month Implied Correlation | 90 days | Current methodology |

The original KCJ / ICJ / JCJ series (introduced 2009) anchored on a fixed-expiry methodology and were widely cited in the 2010s. CBOE replaced them in 2021 with the constant-maturity COR1M and COR3M indices, which provide a more stable rolling reference. Bloomberg, Refinitiv, and most options analytics platforms publish equivalent series.

Typical historical range:

| Regime | COR1M (approx) |
|--------|----------------|
| Quiet tape | 0.20-0.35 |
| Normal | 0.35-0.55 |
| Elevated | 0.55-0.70 |
| Stress / crisis | 0.70-0.95 |

Implied correlation moves in the same direction as [[vix|VIX]] but is a separate axis: VIX measures the level of expected index vol; implied correlation measures the share of that vol attributable to systematic (vs idiosyncratic) movement. It is possible for VIX to fall while implied correlation rises (single-name vol falling faster than index vol) or for VIX to rise while implied correlation falls (single-name vol rising faster than index vol — a "stock-pickers' market").

## Why Implied Correlation Differs from Realised

Implied correlation has consistently traded *above* realised correlation, which is the empirical anchor of the variance / [[variance-risk-premium|correlation risk premium]]. Several mechanisms drive the gap:

- **Index put demand.** Asset managers, pension funds, and corporate hedgers buy SPX puts as portfolio hedges. This buying pressure inflates index IV without affecting single-name IVs proportionally, which mechanically raises implied correlation.
- **Single-name dispersion bid.** Hedge funds and retail traders buy single-name calls (and to a lesser extent puts) for directional and earnings exposure, which inflates single-name IVs less than index IV, again widening the gap.
- **Risk premium for correlation tail risk.** Selling implied correlation is short the [[correlation-breakdown|correlation-spike]] tail. Holders of that short position demand a premium, just as short-vol sellers demand the [[variance-risk-premium]].

The historical gap between COR1M and 30-day realised correlation has averaged roughly 10-20 percentage points in normal regimes, widening in calm vol and narrowing (or briefly inverting) during stress.

## Trading Angle: Dispersion

Dispersion is the explicit harvesting of the implied-correlation premium. The textbook structure:

```
Sell index options (e.g. SPX 30-day ATM straddle)
Buy weighted basket of single-name options on the largest index components
Construct vega-neutral so the trade is neutral to a parallel shift in the entire vol surface
```

P&L drivers:

- **Realised correlation < Implied correlation**: profits as single-name moves are idiosyncratic, the long single-name vol legs harvest realised gamma, and the short index vol expires with less realised vol than was implied
- **Realised correlation = Implied correlation**: roughly breakeven before costs
- **Realised correlation > Implied correlation**: losses as the short index vol pays out more than the single-name vol legs collected

Equivalently: dispersion is *short implied correlation*. A trader who is long dispersion is paid when realised correlation comes in low and is hurt when realised correlation spikes (the [[correlation-breakdown]] event). This is the structural risk profile, and it is the reason dispersion books have historically been damaged in [[gfc|2008]], [[volmageddon|2018]], [[covid-crash|2020]], and the [[vix-august-2024-spike|August 2024]] yen-carry unwind.

The variant trades:

- **Vega-neutral dispersion**: standard structure
- **Gamma-neutral dispersion**: fewer index options, more single names; harvests pure correlation rather than realised vol
- **Calendar dispersion**: long single-name vol on near-term, short index vol on slightly longer-term
- **Correlation swap**: synthetic exposure to (implied - realised) correlation; cleaner but more expensive and less liquid

See dispersion-trading for the full strategy treatment.

## Concentration-Risk Angle

The implied-correlation lens reveals a hidden exposure in [[options-concentration-risk|stacked short-premium books]] that is invisible from per-position Greeks.

A trader who:

- Sells SPX puts (or put spreads, or strangles)
- AND sells single-name puts on the largest SPX components (NVDA, AAPL, MSFT, AMZN, etc.)

is structurally **long implied correlation** (selling index vol relatively more than single-name vol means the implicit ρ in the trader's pricing is *high*, and they take losses when realised correlation comes in lower than that).

But also and more dangerously, the same book is structurally **short the correlation-spike tail**: if realised correlation rises sharply, single-name vols rise less than index vols (because dealers and hedgers chase index protection), so the single-name puts mark losses but not enough to offset the index-put losses. Both legs lose simultaneously when correlation breaks down.

This is the mechanism by which a "diversified" short-premium book — diversified across tickers, sectors, even tenors — can be a single concentrated short-correlation bet. Looking at [[implied-correlation]] alongside per-position [[vega]] is the diagnostic test.

The practical rule of thumb: if your book contains both short index put exposure and short single-name put exposure on >25% of the index by weight, you are structurally short implied correlation, and you should size as if you are running a reverse-dispersion book — because that is what you are.

## Reading the VIX × Implied-Correlation Plane

Because [[vix|VIX]] measures the *level* of index vol and implied correlation measures the *share* of that vol that is systematic, the two form a 2D plane that classifies the regime more richly than either alone:

| VIX | Implied correlation | Regime read | Dispersion stance |
|-----|---------------------|-------------|-------------------|
| Low | Low | Calm, idiosyncratic ("stock-pickers' market") | Long dispersion attractive |
| Low | High | Complacent index, but moves are systematic | Selling index vol is rich; dispersion entry pricier |
| High | Low | Vol up but driven by single names | Index hedges relatively cheap; dispersion can profit |
| High | High | Crisis / everything-down-together | [[correlation-breakdown]] realized; short-corr books bleed |
| Falling | Rising | Single-name vol falling faster than index | Implied-corr premium widening |
| Rising | Falling | Single-name vol rising faster than index | Implied-corr premium compressing |

This is why a trader who "sells vol because VIX looks cheap" can still be selling *expensive correlation* — see [[#Common Mistakes]].

## Decision / Diagnostic Table for Short-Premium Books

| Book characteristic | Hidden exposure | Diagnostic | Mitigation |
|---------------------|-----------------|------------|------------|
| Short SPX puts only | Short index vol + short corr tail | Per-position [[vega]] | Tail hedge / defined risk |
| Short single-name puts only | Short idiosyncratic vol | Sum single-name vega | Diversify across low-corr names |
| Short index **and** single-name puts | **Structurally short implied correlation** | Index vega vs Σ single-name vega; weight coverage | Size as reverse-dispersion; cap index leg |
| Long single-name, short index vol | Long dispersion (long implied corr) | Vega-neutral check | Standard dispersion risk controls |

## Historical Regimes

Selected historical points for the CBOE 1-month implied correlation (COR1M, or its KCJ/ICJ/JCJ predecessors before 2021):

| Date / Period | Approx. Value | Context |
|---------------|---------------|---------|
| 2007 (pre-GFC) | 0.40-0.50 | Quiet vol, normal correlation |
| Sep-Oct 2008 | 0.85-0.95 | GFC peak; index puts bid; single-name vol could not keep up |
| 2013-2014 | 0.30-0.40 | "Stock-pickers' market" — low implied correlation, hedge fund alpha era |
| Aug 2015 | 0.65-0.70 | China devaluation shock |
| Feb 2018 (Volmageddon) | 0.70-0.80 | Vol-ETP unwind; correlation spiked alongside VIX |
| Q4 2018 | 0.55-0.65 | Risk-off into year-end |
| March 2020 (COVID) | 0.85-0.95 | Liquidity panic; everything sold together |
| 2021-2022 (recovery) | 0.30-0.50 | Tech-led idiosyncratic moves; meme-stock dispersion |
| Aug 2024 (yen-carry) | 0.70-0.85 | [[vix-august-2024-spike|VIX spike]] correlation rise |

The persistent feature: implied correlation rises with stress, falls with calm, and consistently runs 10-20 percentage points above same-tenor realised correlation as a structural premium.

## Differences from Realised Correlation

| Property | Realised Correlation | Implied Correlation |
|----------|----------------------|---------------------|
| Direction | Backward-looking | Forward-looking |
| Source | Historical returns | Option prices |
| Tenor flexibility | Any window post-hoc | Determined by chosen option tenor |
| Risk premium | None | Yes, structurally above realised |
| Stability | Smooth | Jumps with vol regimes |
| Tradability | Not directly tradeable | Tradeable via dispersion / correlation swaps |

Realised correlation is what *happened*. Implied correlation is what the option market *expects to happen and charges a premium for*. The premium is the persistent edge for dispersion traders and the persistent risk for stacked short-premium books.

## Common Mistakes

1. **Conflating implied vol with implied correlation.** A book that sees VIX at 18 and assumes "vol is cheap" may not realise that implied correlation is at 0.7 — a level at which selling index vol against single-name vol is structurally rich, not cheap.
2. **Sizing dispersion on calm-regime stats.** The premium is structural but the tail can be terminal; dispersion books need [[risk-of-ruin|RoR-aware]] sizing and [[tail-risk-hedging|tail hedges]].
3. **Ignoring weighting.** A simple "average single-name IV" without index-weighting produces a number that systematically over-states or under-states the relevant implied correlation. Use index weights.
4. **Treating implied correlation as a forecast.** Like implied vol, implied correlation is the risk-neutral expectation plus a risk premium. It is not a clean forecast of future realised correlation.
5. **Confusing CBOE implied correlation indices across vintages.** KCJ/ICJ/JCJ used a fixed-expiry methodology and have different historical levels than the constant-maturity COR1M / COR3M. Splicing the series without adjustment produces spurious regime conclusions.

## Related

- [[correlation]] — the underlying statistical concept
- [[correlation-breakdown]] — the stress-regime mechanism that elevates realised correlation toward implied
- [[implied-volatility]] — the analogue concept on the volatility axis
- [[volatility-surface]] — the full IV grid that implied correlation summarises
- [[options-concentration-risk]] — the book-level structure that is structurally short implied correlation
- [[variance-risk-premium]] — the parallel premium on the volatility axis
- [[vix]] — the index-vol level that moves alongside but separately from implied correlation
- [[vega]] — the Greek that drives dispersion P&L through index-vs-single-name pricing
- [[skew]] — the option-pricing axis that interacts with implied correlation in tail moves
- [[long-vol-vs-short-vol]] — the regime framework
- [[diversification]] — the calm-regime benefit that erodes when implied correlation is realised
- [[gamma-scalping]] — single-name-vs-index gamma structures interact with implied correlation
- [[delta-hedging]] — the hedging machinery behind dispersion legs
- [[iv-rank-and-iv-percentile]] — the level metric that complements the correlation (structure) metric
- [[market-regime]] — the regime axis implied correlation helps classify
- [[options-buying-power-reduction]] — margin impact of stacked index + single-name short-premium books

## Sources

- CBOE Implied Correlation Index methodology white papers (KCJ 2009 launch; COR1M / COR3M 2021 redesign)
- Driessen, Maenhout, Vilkov (2009) "The Price of Correlation Risk: Evidence from Equity Options," *Journal of Finance* — academic foundation of the correlation risk premium
- Marabel Romo (2012) "Dispersion Trading: Empirical Evidence from US Equity Options" — empirical study of dispersion P&L
- [[vix-august-2024-spike]] — case study where implied correlation and realised correlation both spiked
- Sell-side derivatives research on implied vs realised correlation (Goldman Sachs, JPMorgan, Barclays Equity Volatility Insights, 2010-2024)
