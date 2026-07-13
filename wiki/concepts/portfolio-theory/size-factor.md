---
title: "Size Factor"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, quantitative, anomalies, fundamental-analysis]
aliases: ["Size Factor", "Small-Cap Premium", "SMB", "Size Effect"]
related: ["[[value-factor]]", "[[momentum-factor]]", "[[low-vol-factor]]", "[[quality-factor]]", "[[multi-factor-portfolio]]", "[[fama-french-three-factor-model]]", "[[capital-asset-pricing-model]]", "[[liquidity-risk]]", "[[options-risk-budgeting]]", "[[options-portfolio-construction]]", "[[implied-volatility]]", "[[bid-ask-spread]]", "[[diversification-in-options]]"]
domain: [portfolio-theory, anomalies]
prerequisites: ["[[fama-french-three-factor-model]]", "[[capital-asset-pricing-model]]"]
difficulty: intermediate
---

The **size factor** (or *small-cap premium*) is the long-running observation that smaller-capitalisation stocks have historically delivered higher average returns than large-capitalisation stocks, after adjusting for [[capital-asset-pricing-model|CAPM]] beta. First documented in Rolf Banz's 1981 *Journal of Financial Economics* paper *"The Relationship Between Return and Market Value of Common Stocks"*, and formalised as the **SMB** ("Small Minus Big") factor in Fama and French's 1992-1993 three-factor model, the size effect was once treated as one of the canonical anomalies. Subsequent decades have eroded the simple version — pure small-cap-vs-large-cap returns have been muted post-1980s — but the factor persists in carefully specified forms (microcaps, ex-junk small caps, and small × value or small × profitability interactions). The most common retail proxy is **IWM** (iShares Russell 2000); cleaner small-cap-only ETFs include **VIOO** and **IJR**.

## Overview

The size factor is the **most contested** of the canonical equity factors. The Banz (1981) result was striking; the Fama-French (1992) extension cemented it; but a series of papers from 1999 onward documented that the raw small-vs-large premium had largely disappeared. As of 2025, the consensus is roughly:

- Pure CRSP-decile size: the smallest decile *did* outperform 1926-1980, mostly disappeared 1980-2010, and has shown weak/inconsistent returns since.
- **Microcap effect**: outperformance survives in the smallest few percent of the market — but liquidity costs and short-selling frictions absorb most of the alpha for tradeable size.
- **Size interacts strongly with quality**: Asness et al. (2018) showed *"Size Matters, If You Control Your Junk"* — after removing the worst-quality (junk) small caps, the size premium re-emerges robustly.
- **Size is a useful conditioning variable** for value, momentum, and profitability — value works much better in small caps than large.

The factor is most useful in modern factor portfolios as an *interaction* (small × value, small × momentum, small × quality) rather than as a stand-alone bet. Size sits alongside value, momentum, quality, and low-volatility in the standard [[factor-investing|factor-investing]] stack, but it is the one whose stand-alone premium has decayed the most since publication.

### Size-premium decay by era (qualitative)

| Era | Raw small-vs-large premium | Status | Note |
|---|---|---|---|
| 1926–1980 | strong (Banz: ~1.5%/mo smallest vs largest) | robust | pre-publication, possibly liquidity/microcap-driven |
| 1981–2000 | sharply weakened | near-zero | classic "anomaly arbitraged after publication" pattern |
| 2001–2024 | weak, noisy | statistically insignificant raw | survives only conditioned on quality / in microcaps |
| Any era, junk-controlled | strong, persistent | robust | Asness et al. (2018) — re-emerges after removing low-quality small caps |

The decay story is the central interpretive theme: the *raw* factor is one of the canonical cases of a published anomaly fading, while the *conditioned* factor (size × quality) remains one of the more durable interactions in [[multi-factor-portfolio|multi-factor]] research.

## Definition / History

### Banz (1981)

Rolf W. Banz's *"The Relationship Between Return and Market Value of Common Stocks"* (*Journal of Financial Economics* 9 (1): 3-18) examined NYSE stocks 1926-1975, sorted into market-cap quintiles. The smallest quintile outperformed the largest by roughly **1.5% per month** on average — an enormous spread. Banz interpreted the result as a CAPM mis-specification, possibly compensating for an unobserved risk factor.

### Reinganum (1981) and the calendar effect

Marc Reinganum (also 1981, *Journal of Financial Economics*) confirmed Banz's result and noted that much of the size effect concentrated in **January** ("January effect" — see [[january-effect]]), suggesting tax-loss selling and behavioural drivers rather than systematic risk.

### Fama-French (1992, 1993)

Eugene Fama and Kenneth French's 1992 paper *"The Cross-Section of Expected Stock Returns"* (*Journal of Finance*) documented that **size and book-to-market** explain the cross-section of US stock returns better than CAPM beta alone. The 1993 follow-up *"Common Risk Factors in the Returns on Stocks and Bonds"* (*Journal of Financial Economics*) constructed the **three-factor model** with Mkt-Rf, **SMB** (Small Minus Big), and **HML** (High Minus Low book-to-market = [[value-factor|value]]).

The SMB factor is constructed as:
- Sort all stocks (NYSE/AMEX/NASDAQ) by market cap into two groups (Small, Big) using NYSE median as breakpoint.
- Independently sort by book-to-market into three groups (Low, Medium, High).
- Form 6 portfolios at the intersection (S/L, S/M, S/H, B/L, B/M, B/H).
- SMB = average return of the 3 small portfolios − average return of the 3 big portfolios.

### Post-1980 erosion

A series of papers from the late 1990s documented that the raw small-cap premium had **largely vanished** after publication of Banz's result:
- Schwert (2003), *"Anomalies and Market Efficiency,"* in *Handbook of the Economics of Finance*, showed the size effect had effectively disappeared since 1981.
- Horowitz, Loughran, Savin (2000) confirmed small-cap excess returns were near-zero post-1982.
- Plausible explanations: (1) the anomaly was arbitraged away once published; (2) it was always primarily a microcap and survivorship-bias artefact; (3) the rise of small-cap mutual funds and indexing eliminated the liquidity premium.

### The revival: Asness et al. (2018) — *"Size Matters, If You Control Your Junk"*

Cliff Asness, Andrea Frazzini, Ronen Israel, Tobias Moskowitz, and Lasse Pedersen (*Journal of Financial Economics*) showed the size premium **reappears strongly** when one controls for **quality** (using a quality-minus-junk QMJ factor). Pure size is contaminated by an outsized weight to junk small caps (low-profitability, distressed, financially weak names) which destroy the average. After removing the worst-quality small caps, the size premium is large, persistent, and consistent across markets.

## Empirical Evidence

Selected results:
- **Banz (1981)**: smallest NYSE decile vs. largest, 1936-1975: ~1.5% per month size premium.
- **Fama-French SMB (1927-2024)**: annualised long-short return ~2-3%, Sharpe ~0.2-0.3 — much weaker than HML or UMD.
- **CRSP size deciles, 1980-2024**: smallest decile outperformed largest by roughly 1-2% per year on average, well within statistical noise.
- **Microcap-only studies (Crain 2011, Fama-French 2015)**: smallest microcap segment continues to show meaningful excess returns but is often un-investible due to liquidity.
- **Asness et al. (2018) controlled-for-quality SMB**: t-statistic > 5 across 24 international markets, monotonic premium across size deciles after junk control.

The takeaway: there *is* a size effect, but it is buried under noise unless properly conditioned. Naive small-cap-vs-large-cap allocation (IWM vs. SPY) has not reliably outperformed in the 21st century.

## Implementation

### ETFs

| Ticker | Name | Approach | Notes |
|---|---|---|---|
| **IWM** | iShares Russell 2000 | Russell 2000 (#1001-#3000 by cap) | Most liquid small-cap ETF; ~$60B AUM |
| **VIOO** | Vanguard S&P Small-Cap 600 | S&P 600 — has a profitability screen | "Cleaner" than IWM (no junk) |
| **IJR** | iShares S&P Small-Cap 600 | S&P 600 with profitability screen | Same index as VIOO, larger AUM |
| **VB** | Vanguard Small-Cap | CRSP US small-cap | Slightly larger size cutoff than IWM |
| **IWC** | iShares Microcap | Russell Microcap | Pure microcap exposure; highly illiquid |
| **VTWO** | Vanguard Russell 2000 | Same index as IWM | Lower expense |

The **S&P 600** (IJR/VIOO) historically *outperforms* the Russell 2000 (IWM) by 1-2% per year — largely because the S&P 600 includes a positive-earnings screen that filters junk small caps. This is the Asness et al. (2018) result in retail-vehicle form.

### Factor portfolio construction

Standard SMB-style factor:
- Universe: all US-listed common stocks above a minimum-liquidity threshold.
- Signal: log market cap.
- Construction: long bottom decile (or quintile), short top decile, value-weighted within bucket.
- Rebalance: monthly to annual; size is a slow-moving signal.
- Turnover: low (~20-40% per year for decile portfolios).

### As an interaction

In modern multi-factor portfolios, size is most often used as a **conditioning** factor:
- **Small × value**: value premium is much larger in small caps than large caps (Fama-French).
- **Small × momentum**: ditto.
- **Small × quality**: the Asness et al. (2018) cleaned-size premium.
- **Small × low-vol**: low-vol works in small caps too, often more dramatically.

A small-cap-only [[multi-factor-portfolio|multi-factor portfolio]] (e.g. small-cap value + small-cap quality + small-cap momentum) has been a more reliable alpha source than pure size.

### Worked SMB construction (illustrative)

> *Illustrative walk-through, not a backtest.* To replicate the Fama-French SMB leg on a US universe:
>
> 1. **Breakpoint** — rank all NYSE/AMEX/Nasdaq common stocks by market cap and split at the NYSE median into Small and Big.
> 2. **Independent value sort** — separately split book-to-market into Low / Medium / High (bottom 30% / middle 40% / top 30%).
> 3. **Six intersection portfolios** — S/L, S/M, S/H, B/L, B/M, B/H, each value-weighted internally.
> 4. **SMB** = ⅓(S/L + S/M + S/H) − ⅓(B/L + B/M + B/H). The double-sort *neutralises* value, so SMB is a cleaner size bet than a raw small-minus-large spread.
> 5. **Rebalance** annually (size is slow-moving); turnover stays low (~20–40%/yr).
>
> A practitioner improving on this would add a **profitability/quality screen** to the Small leg — dropping the worst-quality small caps — which is the Asness et al. (2018) "control your junk" adjustment that revives the premium. In retail-vehicle form this is exactly the difference between IWM (Russell 2000, no screen) and IJR/VIOO (S&P 600, positive-earnings screen).

### When to use size — interpretation table

| Use case | Verdict | Why |
|---|---|---|
| Stand-alone raw small-vs-large tilt | weak / avoid | premium statistically insignificant post-1981 |
| Size × quality (junk-controlled) | strong | Asness et al. (2018), robust internationally |
| Size as conditioning variable for value/momentum | strong | value & momentum both larger in small caps |
| Pure microcap harvest | theoretically strong, practically hard | liquidity, spreads, borrow make it near-uninvestible |
| Retail vehicle choice | prefer S&P 600 (IJR/VIOO) over Russell 2000 (IWM) | earnings screen filters junk |

## Limitations / Failure Modes

1. **The naive size premium has weakened.** Post-1981, raw small-vs-large is statistically insignificant in most specifications.
2. **Liquidity drag.** Small-cap factor portfolios incur 2-5x the transaction costs of large-cap factor portfolios. A "5% gross return" looks more like 1-2% net for a fast-rebalancing strategy.
3. **Junk concentration in pure size.** Without a quality screen, small-cap portfolios load up on financially distressed, low-profitability names that destroy the average.
4. **Procyclical drawdowns.** Small caps underperform sharply in recessions and credit stress: 2008 (-37% IWM vs. -36% SPY but with bigger intra-year drawdown), 2020-Q1 (-35% in five weeks), 2022 (-22% vs. SPY's -19%). Small-cap betas to credit spreads are high.
5. **Concentration in non-earners.** The Russell 2000 contains a large fraction of unprofitable companies (40-50% in some years post-2020). The "small-cap rally" of 2020-2021 was largely a junk-small-cap rally.
6. **Microcaps are largely un-tradeable.** Where the cleanest size premium lives (the smallest 1-2% of the market), spreads, market-impact, and short-availability make extracting it difficult.
7. **Survivorship bias in early data.** Some of the Banz-era result is attributable to imperfect pre-CRSP data on delisted small caps.

## Connection to Options Books

The size factor has direct, important consequences for options portfolio construction — mostly in the form of **structural disadvantages** for trading single-name small-cap options:

### Wide spreads, thin chains

Small-cap options have **dramatically wider bid-ask spreads** than large-cap options — often 5-20¢ vs. 1-3¢ on AAPL or SPY ATMs — with round-trip transaction costs 5-10x higher in basis terms. Many small caps have **no weekly options**, only monthly cycles; OTM strikes are often missing; multi-leg structures (iron condors, butterflies, calendars) are difficult to fill at fair mid-prices; and short-volatility positions in illiquid small-cap options can become un-exitable in a [[volatility-spike|vol spike]].

### Higher IV, higher realised vol, dispersion

Small caps trade at materially higher [[implied-volatility|IV]] than large caps (median Russell-2000 single-name IV ~30-50% vs. ~20-30% for S&P 500 names). The premium looks rich but realised vol is also much higher; the [[variance-risk-premium]] edge per unit of risk is often *smaller* after costs. There is a **dispersion trade** between IWM index vol and single-name small-cap vol — the index trades at a correlation discount to the constituent average — exploitable for [[volatility-arbitrage|vol-arb]] desks with single-name infrastructure.

### Implications for [[options-portfolio-construction|options portfolio construction]]

1. **Concentration limits**. [[options-risk-budgeting]] recommends caps on sector and factor concentration. A small-cap-heavy options book has hidden factor exposure to size *and* a hidden exposure to liquidity risk.
2. **Tail-hedge cost**. Hedging a small-cap-skewed book with IWM puts is more expensive than hedging a large-cap book with SPY puts because of higher IWM vol — but it is the appropriate hedge for the actual risk.
3. **Earnings concentration**. Small-cap earnings IV crushes are larger in percentage terms than large-cap, making earnings premium-selling tempting but tail-risky.
4. **Avoid single-name small-cap shorts unless liquidity is verified**. The standard ITPM-style discipline is to either use IWM/IJR for index-level small-cap exposure *or* to limit single-name small-cap options to a small allocation with strict liquidity screens.

## Related

- [[value-factor]] — combines especially well with size (small-value)
- [[quality-factor]] — Asness et al. (2018) "junk control"
- [[momentum-factor]] — momentum works well in small caps
- [[low-vol-factor]] — small caps tend to be high-vol; low-vol screen interacts
- [[multi-factor-portfolio]] — how size fits into modern factor stacks
- [[factor-investing]] — the broader discipline size belongs to
- [[fama-french-three-factor-model]] — formal SMB construction
- [[capital-asset-pricing-model]] — the model size effect contradicts
- [[liquidity-risk]] — small-cap liquidity drag
- [[options-risk-budgeting]] — caps factor and concentration exposure
- [[options-portfolio-construction]] — small-cap options-specific considerations
- [[bid-ask-spread]] — execution cost dimension
- [[january-effect]] — early empirical companion to size
- [[anomalies-overview]] — index of cross-sectional anomalies

## Sources

- Banz, R. W. (1981). *"The Relationship Between Return and Market Value of Common Stocks."* *Journal of Financial Economics* 9 (1): 3–18.
- Reinganum, M. (1981). *"Misspecification of Capital Asset Pricing: Empirical Anomalies Based on Earnings' Yields and Market Values."* *Journal of Financial Economics* 9 (1): 19–46.
- Fama, E. F. and French, K. R. (1992). *"The Cross-Section of Expected Stock Returns."* *Journal of Finance* 47 (2): 427–465.
- Fama, E. F. and French, K. R. (1993). *"Common Risk Factors in the Returns on Stocks and Bonds."* *Journal of Financial Economics* 33 (1): 3–56.
- Schwert, G. W. (2003). *"Anomalies and Market Efficiency."* In *Handbook of the Economics of Finance*, vol. 1B.
- Horowitz, J., Loughran, T., Savin, N. E. (2000). *"Three Analyses of the Firm Size Premium."* *Journal of Empirical Finance*.
- Asness, C., Frazzini, A., Israel, R., Moskowitz, T., Pedersen, L. H. (2018). *"Size Matters, If You Control Your Junk."* *Journal of Financial Economics* 129 (3): 479–509.
- Crain, M. (2011). *"A Literature Review of the Size Effect."* SSRN working paper.
- AQR research notes on small-cap factor performance.
