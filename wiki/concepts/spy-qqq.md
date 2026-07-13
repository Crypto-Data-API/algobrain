---
title: "SPY vs QQQ"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [stocks, etf, sp500, nasdaq, sector-rotation]
aliases: ["Spy Qqq", "SPY QQQ", "SPY vs QQQ", "QQQ/SPY ratio"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[etf]]", "[[equity-index]]"]
difficulty: beginner
related: ["[[spy]]", "[[qqq]]", "[[sp500]]", "[[nasdaq]]", "[[sector-rotation]]", "[[relative-strength]]", "[[etf]]", "[[options]]", "[[momentum-anomaly]]"]
---

**SPY** and **QQQ** are the two most-traded equity-index [[etf|ETFs]] in the world and the default benchmarks for US large-cap exposure. [[spy|SPY]] tracks the broad [[sp500|S&P 500]]; [[qqq|QQQ]] tracks the [[nasdaq|Nasdaq-100]], a tech- and growth-concentrated subset. The pair is the canonical "market vs growth" comparison: traders use the **QQQ/SPY ratio** as a real-time gauge of risk appetite and the rotation between broad-market and mega-cap-tech leadership. Both are cornerstone instruments of low-cost [[index-investing]].

> **Data note:** All figures below (expense ratios, betas, concentrations, sector weights) are *approximate and illustrative* of the historical relationship between the two funds. Exact, current values change continuously and should be confirmed against each issuer's live fund documentation before trading.

## The Two Instruments

| | [[spy\|SPY]] | [[qqq\|QQQ]] |
|---|---|---|
| Index | S&P 500 (500 large caps) | Nasdaq-100 (100 largest non-financial Nasdaq names) |
| Issuer | State Street | Invesco |
| Inception | Jan 1993 | Mar 1999 |
| Expense ratio | ~0.09% | ~0.20% |
| Sector tilt | Diversified, includes financials, energy, industrials, staples | Heavily tech / communications / consumer discretionary; no financials |
| Concentration | Top 10 ~35% of index | Top 10 ~50%+, dominated by the "Magnificent 7" |
| Typical beta | ~1.0 (the market) | ~1.1-1.2 vs S&P 500 — more volatile |
| Dividend yield | ~1.3% | ~0.5% |

QQQ is essentially a higher-beta, tech-concentrated expression of the same large-cap universe. Roughly 80%+ of the Nasdaq-100's weight also sits inside the S&P 500, so the two are highly correlated (often 0.9+ on daily returns) — the *difference* between them is the tradeable signal, not their levels.

### Composition and Sector Tilt (illustrative)

The headline structural difference is *what's in* and *what's out*. The Nasdaq-100 excludes financials entirely and skews far more to technology and communication services; the S&P 500 is broad and includes the value/cyclical and defensive sectors that QQQ lacks.

| Dimension | [[spy\|SPY]] (S&P 500) | [[qqq\|QQQ]] (Nasdaq-100) |
|---|---|---|
| Information technology | High | Very high (dominant) |
| Communication services | Moderate | High |
| Consumer discretionary | Moderate | High |
| Financials | Present | **Excluded** |
| Energy / materials / utilities | Present | Minimal / excluded |
| Healthcare, staples, industrials | Present (defensive ballast) | Underweight |
| Weighting scheme | Float-cap weighted, broad | Modified market-cap weighted, concentrated |

Because QQQ omits whole defensive and cyclical sectors, it is *not* a diversified market proxy — it is a concentrated growth/tech bet that happens to look like one. A portfolio holding both SPY and QQQ has far more overlap (the same mega-caps, double-counted) than the two tickers suggest; see [[diversification]].

## The QQQ/SPY Ratio

Dividing QQQ by SPY produces a [[relative-strength]] line that strips out broad-market direction and isolates **tech/growth leadership versus the rest of the market**:

- **Rising ratio** — growth and mega-cap tech are outperforming; risk-on, "QQQ leadership." Typical of expansions, easing financial conditions, and AI/secular-growth themes (e.g., the 2023-2024 [[2024-nvidia-ai-boom|AI rally]]).
- **Falling ratio** — broad market or value/cyclicals are outperforming; often a [[sector-rotation]] out of growth, rising-rate regimes, or risk-off where high-multiple names get hit hardest (e.g., the 2022 rate shock, when QQQ fell ~33% vs SPY ~19%).

The ratio is a cleaner regime indicator than either ETF alone because it removes the common market factor.

### Worked example: isolating the spread

Suppose over a quarter SPY returns **+5%** and QQQ returns **+9%**. Both rose with the market, but the QQQ/SPY ratio climbed roughly **+3.8%** (1.09/1.05 − 1), signalling growth leadership independent of broad direction. In a risk-off quarter the reverse appears: SPY **−10%**, QQQ **−15%**, the ratio falls ~5.6% — high-multiple names took the bigger hit even though *both* fell. The ratio extracts the leadership signal that the raw prices bury.

## When to Use Which

| You want… | Lean | Why |
|---|---|---|
| Broad, diversified US large-cap core | **SPY** (or lower-cost VOO/IVV) | 500 names, all sectors, lower [[volatility]], cheaper to hold |
| Concentrated growth / tech upside | **QQQ** (or QQQM) | Higher [[beta]], mega-cap-tech tilt, larger up-capture in expansions |
| Defensive ballast in a downturn | **SPY** | Holds staples, healthcare, utilities; smaller [[maximum-drawdown\|drawdowns]] |
| Express a growth-vs-market view | **Long QQQ / short SPY** | Hedges most market [[beta]], isolates the tech-growth spread |
| Lowest long-term holding cost | VOO/IVV, QQQM | SPY/QQQ carry slightly higher fees and UIT drag; their cousins are for *buy-and-hold* |
| Maximum trading liquidity / deepest [[options]] | **SPY or QQQ** | The two most liquid equity ETFs; tightest spreads, richest options chains |

Rule of thumb: **QQQ outperforms in risk-on, easing, secular-growth regimes and underperforms in rate-shock or risk-off regimes** — it is SPY with the volatility and concentration dialled up.

## Trading Relevance

- **Regime / risk-appetite gauge.** The QQQ/SPY ratio is a fast read on whether the market is rewarding duration-sensitive growth or defensive breadth. Breadth divergences (SPY holding up while QQQ rolls over, or vice versa) often precede broader turns.
- **Pairs / relative-value trade.** Long QQQ / short SPY (or the reverse) is a low-friction way to express a growth-vs-market view with much of the market beta hedged out — a simple [[sector-rotation]] expression that does not require single-stock selection.
- **Options and volatility.** Both have the deepest options markets in the world. QQQ implied vol typically runs above SPY's because of its higher beta and concentration; the QQQ-SPY implied-vol spread is itself a positioning signal, and 0-DTE flow concentrates in both.
- **Concentration risk.** Because QQQ is ~50% top-10 weighted, it is effectively a leveraged bet on a handful of mega-cap tech names — outperformance and drawdowns are both amplified relative to SPY. A trader "diversifying" across both holds far more overlap than the names suggest.
- **Cost and structure.** SPY is structured as a unit investment trust (slight dividend-reinvestment drag) and is cheaper to hold; for long-term holders VOO/IVV (S&P) and QQQM (Nasdaq-100) are lower-cost cousins, while SPY/QQQ dominate for *trading* liquidity.

## Pitfalls and Risks

- **False diversification.** Owning both is not diversification — the same mega-caps dominate both indices, so a "SPY + QQQ" portfolio is an *overweight* tech bet, not a hedged one. See [[diversification]] and the systematic-vs-idiosyncratic distinction.
- **Hidden concentration.** With the top 10 names ~50%+ of QQQ (and ~35% of SPY), both have drifted toward single-stock-like risk; a stumble in one or two mega-caps drags the whole ETF.
- **Pairs-trade beta residual.** A long-QQQ/short-SPY pair is *not* market-neutral — QQQ's ~1.1-1.2 [[beta]] leaves residual net long exposure unless the SPY leg is up-sized to beta-balance the legs.
- **Regime inversion.** The growth tilt that wins in easing cycles is the same tilt that gets punished in rate-shock regimes (e.g. 2022); the QQQ/SPY ratio can trend hard against a position for quarters.
- **Tracking and structure drag.** SPY's UIT structure cannot reinvest dividends intraday, a small long-term performance drag versus open-end funds (VOO).

## Related

- [[spy]] — the SPDR S&P 500 ETF fact sheet
- [[qqq]] — the Invesco Nasdaq-100 ETF fact sheet
- [[sp500]] / [[nasdaq]] — the underlying indices
- [[sector-rotation]] — what the ratio measures
- [[relative-strength]] — the ratio-line technique
- [[momentum-anomaly]] — QQQ's growth tilt as a momentum proxy
- [[etf]] — instrument structure
- [[index-investing]] — the passive strategy both ETFs serve
- [[diversification]] — why holding both is not as diversified as it looks
- [[beta]] — QQQ's higher market sensitivity

## Sources

- State Street Global Advisors, SPDR S&P 500 ETF (SPY) fund documentation — index, structure, expense ratio.
- Invesco, QQQ Trust fund documentation — Nasdaq-100 methodology, holdings concentration, expense ratio.
- S&P Dow Jones Indices / Nasdaq — index construction methodologies for the S&P 500 and Nasdaq-100.
- General market knowledge for the qualitative regime, beta, and sector-tilt characterization. Specific numeric values (expense ratios, betas, concentrations) are illustrative approximations — verify against live issuer documentation before trading.
