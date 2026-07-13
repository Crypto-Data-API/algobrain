---
title: "Dividend Yield"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, metrics, dividends, income-investing]
aliases: ["dividend yield", "yield", "dividend ratio"]
domain: [fundamental-analysis]
prerequisites: ["[[dividend]]"]
difficulty: beginner
related: ["[[dividend]]", "[[dividend-payout-ratio]]", "[[price-to-earnings-ratio]]", "[[earnings-per-share]]", "[[franking-credits]]", "[[fundamental-analysis]]"]
---

**Dividend yield** is the percentage of a stock's price returned to shareholders each year in the form of cash [[dividend|dividends]]. It is the core valuation metric for income investors, REITs, utilities, and any framework that treats equities as bond-like cash-flow instruments.

## Formula

```
Dividend Yield = (Annual Dividends Per Share / Current Stock Price) × 100%
```

A stock trading at $50 that pays $2 per year in dividends has a 4% yield. Because the denominator is the live price, yield moves inversely to price: a 20% price drop (with the dividend unchanged) pushes a 4% yield to 5%.

## Trailing vs. Forward Yield

- **Trailing yield (TTM)** sums the dividends actually paid over the last 12 months. Objective, but stale if the company just changed its payout.
- **Forward yield** uses the annualized current dividend rate (typically most-recent quarterly dividend × 4). Reflects today's policy but is only a projection.

Most quote pages default to trailing; brokerages often show forward. The two can diverge sharply during payout cuts or hikes.

## Typical Ranges

| Category | Typical Yield |
|---|---|
| S&P 500 average | 1.5% – 2.0% |
| Dividend Aristocrats | 2% – 4% |
| Utilities | 3% – 5% |
| REITs | 3% – 6% |
| MLPs / midstream energy | 6% – 10% |
| Tech growth stocks | 0% – 1% |
| BDCs, mortgage REITs | 8% – 14% |

Historical S&P 500 yields were much higher (4-6%) in the mid-20th century before buybacks replaced dividends as the dominant return-of-capital mechanism.

## The Yield Trap Warning

An unusually high yield is often a **warning signal, not a bargain**. The math is mechanical: if a stock's yield suddenly jumps from 4% to 10%, it's usually because the price collapsed — and the price collapsed because the market expects the dividend to be cut. Once the cut is announced, the yield normalizes and the holder has eaten both a capital loss and a dividend reduction.

Classic yield traps appear in declining industries (telecom, traditional retail, legacy media) and in over-leveraged financials heading into a downturn.

## Sustainability: The Payout Ratio

Always pair yield with the [[dividend-payout-ratio|dividend payout ratio]]:

```
Payout Ratio = Dividends / Net Income (or / Free Cash Flow)
```

| Payout Ratio | Interpretation |
|---|---|
| < 40% | Very safe, room to grow |
| 40% – 60% | Healthy, normal range |
| 60% – 80% | Stretched but sustainable |
| > 80% | Cut risk elevated |
| > 100% | Unsustainable — borrowing or burning cash to pay |

REITs are a structural exception (required to distribute 90%+ of taxable income).

## Dividend Growth Investing

Practitioners of **DGI** argue that chasing current yield is a mistake — the right strategy is to buy companies with long histories of consistently raising dividends (Dividend Aristocrats require 25+ consecutive years of increases). A 2% yield growing 10% per year compounds to a much higher yield-on-cost over a decade than a static 6% yield from a mature utility.

## Trading Relevance

Beyond income investing, dividend yield underpins several systematic strategies. The **high-dividend-yield factor** (e.g., the "Dogs of the Dow" rule of buying the ten highest-yielding Dow components each year) is a classic value tilt, though it is prone to the yield-trap problem above. Aggregate market dividend yield is a long-horizon **valuation and return-prediction** input: Shiller and others show the market's yield (and its inverse, price/dividend) has predictive power for multi-year forward returns. Yield is also central to **dividend-capture** trading (buying just before the [[ex-dividend-date|ex-dividend date]] to harvest the payout), though the stock typically drops by roughly the dividend amount on the ex-date, and transaction costs plus dividend taxation usually erode the apparent edge. In Australia, after-tax yield must incorporate [[franking-credits|franking credits]], which can lift the effective grossed-up yield by 30–40% for fully franked dividends.

## Related

- [[dividend]], [[dividend-payout-ratio]], [[earnings-per-share]]
- [[price-to-earnings-ratio]], [[franking-credits]], [[fundamental-analysis]]

## Sources

- Shiller, R., *Irrational Exuberance* — market dividend yield / price-dividend ratio as a long-horizon return predictor
- S&P Dow Jones Indices — S&P 500 Dividend Aristocrats index methodology (25+ years of consecutive increases)
- O'Higgins, M. (1991), *Beating the Dow* — origin of the "Dogs of the Dow" high-yield strategy
- Australian Taxation Office — dividend imputation and franking credit rules underpinning grossed-up yield
