---
title: "Options Concentration Risk"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, portfolio-theory, correlation]
aliases: ["Options Portfolio Concentration", "Concentrated Options Book"]
related: ["[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[options-stress-testing]]", "[[vega-budgeting]]", "[[correlation]]", "[[tail-risk]]", "[[long-vol-vs-short-vol]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[correlation]]", "[[options-greeks]]"]
difficulty: advanced
---

Concentration risk in an options portfolio is the gap between *apparent* diversification (many tickers, many expiries, many strikes) and *actual* diversification (independent sources of P&L). A book of eight short strangles across [[nvidia|NVDA]], AVGO, AMD, TSM, MU, ASML, ARM, and MRVL looks like eight positions; in a vol shock or AI sector unwind it acts like one position with eight times the size. Ticker-level diversification deceives because it ignores [[correlation]], factor exposure, sector clustering, and the dominant truth that nearly every short premium book is just a single bet on vol staying contained. Recognizing and measuring these stacked exposures is what separates a [[options-portfolio-construction|professionally constructed book]] from a collection of trades.

## The Diversification Illusion

The retail intuition: "I have positions on eight different stocks, so I'm diversified." The professional reality: those eight positions share the same factor loadings, the same vol regime, often the same earnings-week catalyst, and the same correlation-spike-on-stress profile. They are not eight bets — they are eight expressions of one bet.

Consider a book of short strangles, sized "small" at $500 max risk per name:

| Position | Underlying | Sector | Beta to SPX | Short Vega ($) | Earnings |
|----------|------------|--------|-------------|----------------|----------|
| Short strangle 1 | NVDA | Semis / AI | 1.7 | -$240 | Aug 27 |
| Short strangle 2 | AVGO | Semis / AI | 1.4 | -$180 | Sep 4 |
| Short strangle 3 | AMD | Semis / AI | 1.9 | -$210 | Aug 5 |
| Short strangle 4 | TSM | Semis / AI | 1.2 | -$150 | Jul 17 |
| Short strangle 5 | MU | Semis / Memory | 2.1 | -$190 | Sep 25 |
| Short strangle 6 | ASML | Semi cap-eq | 1.5 | -$160 | Jul 16 |
| Short strangle 7 | ARM | Semis / IP | 1.8 | -$130 | Aug 6 |
| Short strangle 8 | MRVL | Semis / Networking | 1.7 | -$140 | Aug 28 |
| **Total** | — | — | **avg 1.7** | **-$1,400** | — |

The trader sized each position at $500 risk. The book's *apparent* risk: $4,000 (8 × $500). The book's *actual* risk:

- A single bad print from one of the leading names ([[nvidia|NVDA]], AVGO) drags every other name with it via [[correlation]] cascade — historically observed pairwise daily correlations within US semis run 0.6-0.8 in calm tape and spike to 0.9+ on stress days
- All 8 are short [[vega]]; an [[implied-volatility]] regime shift adds losses across every position simultaneously
- All 8 have above-1 beta; a 5% SPX drawdown produces an 8-9% sector drawdown, and short strangles with 16-delta strikes will be tested on roughly all of them at once
- Six of the eight earnings dates fall within a 60-day window — the book has a concentrated earnings cluster

A 2-sigma adverse vol-and-direction move on this book produces P&L closer to running *one* position at $4,000 of risk than eight positions at $500. The trader's [[options-position-sizing|sizing math]] was correct at the position level and wrong at the book level.

## Concentration Dimensions

Options concentration stacks across at least six dimensions. A position that looks innocuous on one axis can be heavy on another. The table below summarizes the dimensions, the question each one asks, and the primary metric used to measure it — the sections that follow expand each row.

| # | Dimension | Question it answers | Primary metric | Worst-case trigger |
|---|-----------|---------------------|----------------|--------------------|
| 1 | Single-name | How much of the book rides on one ticker? | % of [[delta]] / [[gamma]] / [[vega]] in one underlying | Single-stock gap (earnings, fraud, halt) |
| 2 | Sector | Are my "different" names the same GICS bet? | % of risk in one sector / sub-industry | Sector rotation, sector-specific shock |
| 3 | Factor | What style factors do I really load? | Barra-style factor exposure | Factor reversal (momentum crash, quality unwind) |
| 4 | Index / beta | Am I secretly just long/short the market? | Beta-weighted [[delta]] to SPX | Broad [[correlation]] spike, index drawdown |
| 5 | Vol regime | Is the whole book one [[volatility]] bet? | Net [[vega]] as % of gross vega | [[vix]] spike — every short-vol line loses at once |
| 6 | Tenor / expiry | Does everything pin on one date? | % of [[gamma]] / vega in one DTE bucket | Single-day [[gamma]] explosion + [[theta]] cliff |

The dangerous property is that these stack *multiplicatively*: a book that is 80% semis (sector), 90% short [[vega]] (vol regime), and 70% in the same monthly expiry (tenor) is not three separate 70–90% problems — it is one extremely concentrated bet that scores badly on every axis at once. Each axis is a lens on the same underlying truth measured by [[portfolio-greeks-aggregation|aggregated Greeks]].

### 1. Single-Name Concentration

The most obvious form: too many positions on one underlying. A long call, short put, and short calendar on TSLA across three different expiries is still "all TSLA." Limit single-name exposure as a hard cap (see [[options-position-sizing]] rules of thumb: no underlying contributes >20% of portfolio delta, gamma, or vega).

### 2. Sector Concentration

Names within the same GICS sector (or sub-industry) co-move. The semis example above is the canonical case: NVDA, AVGO, AMD, MU, TSM, ASML, MRVL, LRCX, AMAT all behave as a *single asset* on stress days. Software (MSFT, GOOGL, META, AMZN, ORCL, CRM) is similar. Banks (JPM, BAC, WFC, GS, MS, C) are similar. xlk, xlf, xle make the underlying exposure visible — if you can replace your book with a position in the sector ETF, you weren't diversified.

### 3. Factor Concentration

The deepest hidden concentration. Even a "diversified" book of NVDA + LLY + COST + WMT + JPM still loads heavily on:

- **Momentum** (NVDA, COST) — high realized 12-month return
- **Quality** (LLY, COST, WMT) — high ROE, low debt
- **Low-vol** (WMT, JPM) — low realized vol relative to peers
- **Mega-cap** (all) — top 50 by market cap

Barra-style risk decomposition exposes this. A short premium book on six "different" mega-caps is often 60%+ explained by exposure to two or three common factors. [[factor-investing]] research has documented this for decades on the equity side; options books inherit the same exposures via their underlying delta and vega loadings.

### 4. Index / Beta Concentration

Most large-cap US single-name options behave as levered SPX exposure. Beta-weight every delta in the book to SPX (or QQQ for tech-heavy books). A book showing $0 net SPX-beta-weighted delta is genuinely market-neutral; a book showing $50,000 of net long SPX-equivalent delta carries a $5,000 hit on a 10% SPX drawdown regardless of what the names "looked like" individually. See [[beta-weighted-delta]].

### 5. Vol Regime Concentration

The dimension retail traders rarely measure. Are *all* of your positions short vol? Long vol? Short skew? Long calendar spread (long back-month vol, short front-month vol)?

A book of:
- Short NVDA strangle
- Iron condor on SPY
- Short put spreads on JPM
- Short straddle on TSLA
- Short call spread on QQQ
- Naked short MSFT puts

is *one position*: short vol, broad market. There is no offset. When [[vix]] runs from 14 to 28 (Aug 2024, Apr 2024, Mar 2020, Feb 2018), every line item loses simultaneously and the portfolio's [[vega]] losses compound the [[delta]] and [[gamma]] losses.

### 6. Tenor / Expiry Concentration

A book where every position expires within the same 14-day window has a single pinned date of [[gamma]] explosion and [[theta]] cliff. Diversifying across 7 / 30 / 60 / 90 DTE smooths the exposure.

## Correlation in Stress

The single most important fact about options concentration: **diversification benefits collapse exactly when you need them**.

Pairwise correlation among US large-cap stocks is roughly 0.4 in normal regimes. In drawdowns it rises to 0.7-0.9. In tail events, single-name idiosyncratic risk effectively vanishes — everything is one trade.

Documented historical regimes:

| Event | Average Pairwise Correlation (S&P 500 names) |
|-------|----------------------------------------------|
| Calm regime (e.g. 2017) | 0.25-0.35 |
| Normal regime | 0.40-0.50 |
| October 1987 crash | ~0.85 |
| 2008 GFC peak | ~0.80 |
| March 2020 COVID crash | ~0.85 |
| February 2018 Volmageddon | ~0.75 |
| August 5, 2024 (yen carry / VIX spike to 65) | ~0.80 |

The implication for options books: a short premium book modeled on calm-regime correlations will mark losses *2-3x larger than expected* during a stress event. Portfolio variance is dominated by the off-diagonal terms of the covariance matrix; when correlations spike, those off-diagonal terms balloon.

This is the [[correlation-breakdown]] phenomenon, and it is the single most under-priced risk in retail options books.

## Measuring Concentration

A serious options book gets the following exposure reports daily. Before the prose, the formula reference below is the at-a-glance card — each metric, its formula, and the green/amber/red zones a discretionary book typically uses. The thresholds are *illustrative* guardrails (see [[options-risk-budgeting]]), not regulatory limits.

| Metric | Formula | Green | Amber | Red |
|--------|---------|-------|-------|-----|
| Single-name risk share | `max_i(|risk_i|) / Σ|risk|` | ≤10% | 10–20% | >20% |
| Sector risk share | `Σ|risk in sector| / Σ|risk|` | ≤25% | 25–40% | >40% |
| Beta-weighted [[delta]] | `Σ (deltaᵢ × betaᵢ × multiplier)` | ≤±10% of equity | ±10–20% | >±20% |
| Net [[vega]] share | `|Σ vega| / Σ|vega|` | ≤55% | 55–70% | >70% |
| Top-factor loading | `R² explained by one factor` | ≤30% | 30–50% | >50% |
| Single-expiry vega | `Σ vega in 14-day window / Σ|vega|` | ≤30% | 30–50% | >50% |
| Earnings-week vega | `Σ vega reporting same week / Σ|vega|` | ≤25% | 25–40% | >40% |
| Concentration penalty | `stress variance / baseline variance` | <1.5 | 1.5–2.0 | >2.0 |

(All numbers above are illustrative thresholds, not live data — calibrate to your own capital and [[risk-of-ruin]] tolerance. They tie directly to [[position-sizing]]: a single trade that pushes any metric into the red is, by definition, oversized at the book level even if it passed the per-trade test.)

### Beta-Weighted Delta

```
Beta-weighted delta to SPX = Σ (position delta × underlying beta)
```

Every position's delta is converted into SPX-equivalent shares. A $250K book should typically run between -$25K and +$25K of beta-weighted SPX delta unless the trader has an explicit directional view.

### Sector Exposure

```
Sector exposure % = (Σ |notional in sector| ) / (total |notional|)
```

A common professional rule of thumb: **no single GICS sector should hold more than 25% of the book's risk**. A 40% allocation to semis is a sector trade, not a diversified book.

### Factor Exposure (Barra-Style)

Project each underlying onto a small set of style factors:

- Market beta
- Size (large-cap vs small-cap)
- Value vs growth
- Momentum
- Quality
- Low-vol

Tools: axioma, barra, northfield, or open-source approximations using Fama-French + AQR factor data. For a discretionary trader without an institutional risk system, a simplified version is to bucket each name into 2-3 dominant factor labels and watch for over-loading.

### Single-Name Notional Limits

Hard cap: no single underlying contributes >10% of portfolio risk. A book where NVDA contributes 35% of total vega is a NVDA-vol bet with some other names attached.

### Vega Concentration by Vol Regime

```
Net vega = Σ position vegas
% of book in short vega = |Σ short vegas| / |Σ |vegas||
```

A book that is 95% short vega (regardless of which names) has no internal hedge against a vol spike. Aim for an explicit target: e.g., max 60% net short vega exposure, with the remainder in long vol overlays (long [[vix-futures]], long out-of-the-money puts, long [[tail-risk-hedging]] structures).

### Correlation-Adjusted Risk

```
Portfolio variance = Σᵢ Σⱼ wᵢ wⱼ ρᵢⱼ σᵢ σⱼ
```

Re-run with stress correlations (ρ = 0.85 for same-sector pairs, 0.75 for same-factor pairs). Compare stress portfolio variance to baseline portfolio variance. The ratio is your concentration penalty: stress variance / baseline variance > 2.0 means you have a hidden concentrated bet.

## Rules of Thumb

Professional trade construction embeds concentration limits directly into [[options-portfolio-construction|portfolio construction]]:

| Limit | Rule |
|-------|------|
| Single name | ≤10% of portfolio risk in one underlying |
| Single sector | ≤25% of portfolio risk in one GICS sector |
| Single factor | ≤30% of portfolio risk on one Barra-style factor |
| Net vol exposure | Net short vega ≤60% of total vega |
| Net market exposure | Beta-weighted SPX delta ≤±20% of equity |
| Single expiry | ≤30% of book vega in any 14-day expiry window |
| Earnings cluster | ≤25% of book has earnings in any single calendar week |

These are not laws of physics; they are guardrails calibrated to keep the worst plausible day under ~5% drawdown for a properly capitalized book. Tightening or loosening depends on capital, conviction, and account [[risk-of-ruin]] tolerance.

## How to Audit Your Book for Concentration

A repeatable weekly (or daily, for active books) checklist. The goal is to surface the *one bet* hiding behind the ticker list. Run it top to bottom; any item that lands in the amber/red zone of the formula-reference table is a flag to address before adding new risk.

1. **Export every open position** into one sheet: ticker, structure, signed [[delta]], [[gamma]], [[vega]], [[theta]], notional, sector, beta, earnings date, expiry.
2. **Convert to dollar Greeks and beta-weight the delta** so positions are comparable across underlyings — this is [[portfolio-greeks-aggregation]]. Raw per-contract Greeks are not additive across tickers.
3. **Single-name check** — sort by `|risk|` per underlying. Is any one ticker >10–20% of total delta, gamma, or vega? If yes, that name *is* the book.
4. **Sector check** — group by GICS sector. Is any sector >25%? Ask the killer question: *could I replace most of this book with one position in the sector ETF (xlk, xlf, xle)?* If yes, you weren't diversified.
5. **Factor check** — tag each name with 2–3 dominant style factors ([[factor-investing|momentum, quality, low-vol, size, value]]). Count how many names share each tag. A book where 70%+ of names are "mega-cap momentum" is one factor bet.
6. **Index/beta check** — sum the beta-weighted [[delta]]. Is the book accidentally net long or short the market versus your stated view?
7. **Vol-regime check** — compute net [[vega]] as a share of gross vega. Is the whole book short [[volatility]] with no long-vol offset? See [[long-vol-vs-short-vol]].
8. **Tenor check** — bucket [[gamma]] and vega by DTE (7 / 30 / 60 / 90). Is more than ~30% of risk pinned to a single 14-day window?
9. **Catalyst-cluster check** — bucket every position's earnings date and the macro calendar ([[fomc-meetings|FOMC]], [[cpi-release|CPI]], [[nonfarm-payrolls|NFP]]) by week. Any week holding >25% of book vega is a hidden concentration.
10. **Stress-correlation re-run** — recompute portfolio variance with same-sector ρ forced to 0.85 and same-factor ρ to 0.75. Concentration penalty (stress/baseline variance) >2.0 means a hidden concentrated bet. Then run the full scenario battery in [[options-stress-testing]].
11. **The integration test** — would the book survive *all* of its red-zone exposures hitting at once (the realistic crash, where sector + factor + vol-regime + correlation all move together)? If the answer requires hope, reduce size — see [[position-sizing]] and [[trade-repair-and-rolling]] for how to unwind concentration without panic-dumping.

## Hidden Concentration

Concentration that doesn't show up in standard reports.

### Earnings Clusters

A book of short strangles on NVDA, AVGO, AMD, MU, ARM with earnings dates spread over 60 days looks fine on calendar averages. But if 4 of the 5 report within a single week (typical for semis earnings), the book has *one trade* on "consensus is roughly right about AI demand this quarter."

Check: pull every position's earnings date and bucket by week. Any week containing >25% of book vega is a hidden concentration.

### Fed / Macro Event Clusters

[[fomc-meetings|FOMC]], [[cpi-release|CPI]], [[nonfarm-payrolls|NFP]], [[ecb|ECB]], [[bank-of-japan|BOJ]] meetings all produce [[implied-volatility]] mean-reversion. A book with positions expiring the day after FOMC across multiple names has stacked event exposure — every position is a bet on "the Fed says nothing surprising."

### Ex-Dividend Clusters

Less common but matters for short call books on dividend-paying names — early assignment risk concentrates around ex-div dates. Multiple short calls on JPM, BAC, WFC, C all running into a quarterly ex-div week stack assignment risk.

### Implied Correlation Concentration

Selling index puts (SPX, NDX) while also selling single-name puts on the largest index components is a hidden short [[implied-correlation]] position. If realized correlation rises (a stress event), single-name vol rises *less* than index vol — the dispersion shrinks against you.

### Skew Concentration

A book of all short put spreads (no short call spreads) is short [[skew|put skew]] across the entire portfolio. A skew steepening event hits every position. Mix in some short call spreads or call ratios to get a more neutral skew exposure.

## Diversifying Short Premium

Genuine diversification of a short premium book requires reaching across:

### 1. Asset Classes

A short premium program that runs in equity options only is a single-asset bet. Add:

- **Rate vol**: short premium on tlt, ief, or [[move-index|MOVE]]-driven structures
- **Commodity vol**: short gld, uso, uup options
- **FX vol**: short [[eurusd]], [[usdjpy]] options (lower vol, smaller premium, but uncorrelated to equity vol regimes)

Equity vol, rate vol, FX vol, and commodity vol have meaningful but imperfect correlation. Spreading across them reduces the single-vol-regime concentration.

### 2. Tenors

Mix 7 DTE / 30 DTE / 60 DTE / 90 DTE positions. Front-month vol mean-reverts quickly; back-month vol is sticky. A spike that crushes 7 DTE short premium often only modestly damages 90 DTE. The opposite is true for slow grinding regime shifts.

### 3. Long-Vol Overlays

Allocate 5-15% of the book's vega budget to long vol structures:

- Long [[vix-call-spreads]]
- Long out-of-the-money spx-puts
- Long [[put-tree|put trees]]
- Long [[calendar-spread|long-vol calendar spreads]]
- Tail risk products from [[universa]]-style approaches

These bleed during calm periods (negative carry) but pay multiples of premium during stress. The tradeoff: small persistent drag for catastrophic protection. See [[tail-risk-hedging]].

### 4. Long Vol *Single-Name* Pairs

Within a short premium book, going long vol on the most-likely-to-break name in a sector creates a dispersion structure. Short index vol, long the messiest single-name vol. The hedge pays exactly when concentration risk materializes.

## Worked Example

A $250K options account, run by a discretionary trader who spent the last six months bullish AI semis and accumulated short premium on the leaders.

**Apparent book** (looks diversified — 6 different tickers, varied expiries):

| Position | Structure | Net Vega | Net Delta | Sector | Beta |
|----------|-----------|----------|-----------|--------|------|
| Short NVDA call spread | -1×450C / +1×460C | -$180 | -8 | Semis | 1.7 |
| Short AVGO call spread | -1×170C / +1×175C | -$140 | -6 | Semis | 1.4 |
| Short AMD call spread | -1×185C / +1×190C | -$160 | -7 | Semis | 1.9 |
| Short MU put | -1×95P | +$110 | +12 | Semis | 2.1 |
| Short TSM call spread | -1×185C / +1×190C | -$120 | -5 | Semis | 1.2 |
| Short ASML call spread | -1×850C / +1×860C | -$200 | -9 | Semi cap-eq | 1.5 |
| **Net** | — | **-$690** | **-23** | **100% semis** | **avg 1.6** |

The trader believes this is a "balanced semis short call spread book with a long-bias kicker (short MU put)." On any reasonable measure of concentration, it is **a single $100,000-of-risk bet on AI semis cooling down**:

- 100% in one sector
- ~95% loaded on the same factor (AI capex / hyperscaler demand)
- Pairwise correlation in the underlyings: ~0.7 in calm, ~0.9 in stress
- Net short vega: ~80% of book vega
- All six names have earnings within ~6 weeks (concentrated catalyst window)

**An AI sector unwind** (e.g., a single hyperscaler issuing weak forward guidance) drives all six names down 10-20% with [[implied-volatility|IV]] spiking 10+ points across the complex. The book's modeled stress P&L: -$25K to -$45K — far worse than the per-trade "max risk" sums imply, because realized correlations spike and the short call spreads on multiple names lose simultaneously despite the short put gain.

**Reconstructed book** with same total vega budget and same directional view, but properly diversified:

| Position | Structure | Underlying | Sector / Asset | Why |
|----------|-----------|------------|----------------|-----|
| Short call spread | -1×475C / +1×485C | SPX | Index equity | Express macro view at index level |
| Short put spread | -1×400P / +1×395P | TLT | Rates | Uncorrelated vol regime |
| Short strangle | varied | GLD | Commodities | Different macro driver |
| Short put | -1×140P | USDJPY equiv | FX | Different vol surface |
| Short NVDA call spread | -1×450C / +1×460C | NVDA | Semis (only) | Express specific AI-cooling view, sized smaller |
| Long VIX call spread | +1×22C / -1×26C | VIX | Long vol overlay | Tail hedge |

Same total premium collected. Net vega similar. But:

- 4 different asset classes (no single asset class >40%)
- Concentration in semis cut from 100% to ~20%
- Net short vega cut from 80% to 55% (long VIX overlay)
- Stress P&L on AI sector unwind: -$8K to -$15K instead of -$25K to -$45K

The directional view is *still expressed* (the NVDA position remains), but it is no longer the only thing in the book.

## Connection to Position Sizing & Risk Budgeting

Concentration risk is the bridge between *single-trade* [[position-sizing]] and *book-level* [[options-risk-budgeting|risk budgeting]]. The two operate at different altitudes, and concentration is what falls through the gap if you only mind one of them:

- **[[position-sizing]] answers "how big is this one trade?"** — usually a 1–2% max-loss-per-trade rule. It is necessary but blind to correlation. Eight trades each sized correctly to 1% can sum to a single 8% bet if they are the same bet wearing eight tickers.
- **[[options-risk-budgeting]] answers "how is risk allocated across the whole book?"** — it sets ceilings on aggregate Greeks ([[vega-budgeting|vega budget]], net [[delta]], net [[gamma]]) and on the concentration metrics above. This is the layer that catches the eight-ticker-one-bet problem.
- **Concentration analysis is the diagnostic** that tells the risk-budgeting layer whether the position-sizing layer has quietly produced a concentrated book.

The correct sequence, integrated with the rest of the wiki:

1. Size each candidate trade with [[position-sizing]] (per-trade max loss).
2. Add it *on paper* to the book and re-aggregate via [[portfolio-greeks-aggregation]].
3. Check the new book against the concentration formula-reference and [[options-risk-budgeting|risk-budget]] ceilings.
4. Stress the proposed book with [[options-stress-testing]] under correlated-crash scenarios.
5. Only then commit. If the trade passes step 1 but fails step 3, it is *correctly sized as a trade and incorrectly sized as an addition to this book* — shrink it, swap the underlying for a diversifying one, or skip it.

Two further connections: on a [[portfolio-margin]] account the broker's own scenario engine penalizes single-name concentration with margin add-ons, so a concentrated book is *also* a capital-inefficient and margin-fragile book (concentration and margin expansion arrive together in a stress). And [[theta-targeting|theta targets]] should never be met by piling more premium into the same concentrated theme — chasing income is one of the most common ways a book silently becomes concentrated. The discipline is to harvest the target [[theta]] across *independent* sources of premium, not by deepening the one bet that is already too large.

## Common Mistakes

The recurring patterns in retail and semi-pro options books:

1. **Sizing each position independently** — checking each trade's max loss against the 1-2% per-trade rule but never checking the *book's* aggregate exposure. The right test: if every position lost simultaneously (correlated stress), what's the drawdown?
2. **Assuming low realized correlation persists** — the book is sized on 0.4 correlations measured during calm tape. The stress regime runs at 0.85.
3. **Ignoring factor exposure** — "I have NVDA, COST, LLY, JPM" feels diversified but is 70%+ explained by mega-cap momentum + quality factors.
4. **Treating short index puts and short single-name puts as independent** — when SPX falls 5%, AAPL falls 6%; the index puts and single-name puts both lose.
5. **Mistaking ticker count for risk count** — the metric that matters is "how many independent bets" not "how many positions."
6. **Confusing defined risk with diversified risk** — eight defined-risk iron condors are still one short-vol bet, even if each individually caps loss.
7. **Letting earnings clusters accumulate unmonitored** — the book grows organically as new short-premium opportunities appear and earnings dates pile up.
8. **No long-vol overlay** — the book has zero [[tail-risk-hedging]] because long vol "always loses money" — until the day it doesn't.
9. **Beta-weighted delta drift** — the book accumulates net long or short SPX delta over time as positions are added without adjusting for aggregate market exposure.
10. **Same-trade-different-clothes** — a short call spread, a covered call, a cash-secured put, and a credit put spread on the same underlying are four different ways to express one short-vol view. Treat them as one position for sizing.

## Tools

Practical tools for measuring and managing concentration:

- **[[ibkr-risk-navigator|IBKR Risk Navigator]]** — built-in stress views including SPX shock, single-name shocks, and IV shocks across the entire book; sector exposure breakdown; beta-weighted deltas. Free if you trade with Interactive Brokers.
- **orats** — implied vol surface analytics; useful for spotting when your book is concentrated on a single skew shape.
- **OptionMetrics IvyDB** — institutional-grade historical options data; correlation regime studies.
- **tastytrade** beta-weighted delta and net vega views — adequate for medium books.
- **[[thinkorswim]]** beta-weighted analysis — usable for sector concentration.
- **[[pivolio|PiVolio]] / [[convex-trading]] / [[trade-machine]]** — third-party concentration and Greek aggregation across complex options books.
- **Custom risk system** — at sufficient scale, in-house Python with [[pyfolio]] / [[empyrical]] / Barra factor data for full factor decomposition.
- **[[bloomberg-terminal]] PORT function** — institutional standard, full risk decomposition.

For most discretionary traders the workflow is: IBKR Risk Navigator daily, supplemented by a manual sector/factor spreadsheet updated weekly, with stress correlation re-runs monthly.

## Related

- [[options-portfolio-construction]] — the parent topic; how to build the book in the first place
- [[options-position-sizing]] — sizing individual positions; this page is the book-level companion
- [[position-sizing]] — the general single-trade sizing discipline this page sits above
- [[options-risk-budgeting]] — allocating risk across positions and themes
- [[portfolio-greeks-aggregation]] — converting per-contract Greeks into a comparable book-level picture
- [[options-stress-testing]] — running the scenarios that reveal concentration
- [[value-at-risk]] — statistical risk measure that concentration inflates in the tails
- [[portfolio-margin]] — broker margin engine that penalizes single-name concentration
- [[theta-targeting]] — income discipline that must not be met by deepening one concentrated bet
- [[trade-repair-and-rolling]] — how to unwind a concentrated position without panic-dumping
- [[volatility]] — the regime axis on which most options books are secretly one bet
- [[vega-budgeting]] — sub-topic on vega allocation across the book
- [[correlation]] — foundational concept
- [[correlation-breakdown]] — the stress-regime phenomenon
- [[tail-risk]] — what concentration produces when it materializes
- [[tail-risk-hedging]] — how to overlay protection
- [[long-vol-vs-short-vol]] — the fundamental vol-regime axis
- [[beta-weighted-delta]] — measuring market exposure across underlyings
- [[implied-correlation]] — the index-component correlation as priced by options
- [[factor-investing]] — equity factor framework that translates to options books
- [[risk-management]] — broader risk framework
- [[risk-of-ruin]] — what concentration ultimately threatens

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on portfolio risk
- [[vix-august-2024-spike]] — case study of correlation breakdown event
