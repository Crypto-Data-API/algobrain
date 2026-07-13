---
title: "Earnings Per Share (EPS)"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation, metrics, earnings, financial-statements]
aliases: ["EPS", "eps", "earnings per share", "diluted EPS", "basic EPS"]
prerequisites: ["[[financial-statement-analysis]]"]
domain: [fundamental-analysis]
difficulty: beginner
related: ["[[price-to-earnings-ratio]]", "[[diluted-eps]]", "[[forward-pe]]", "[[peg-ratio]]", "[[earnings]]", "[[financial-statement-analysis]]", "[[return-on-equity]]", "[[free-cash-flow]]", "[[fundamental-analysis]]", "[[post-earnings-announcement-drift]]"]
---

Earnings Per Share (EPS) is the portion of a company's net profit allocated to each outstanding share of common stock. It is the single most-watched profitability figure in equity markets and forms the denominator of the [[price-to-earnings-ratio]], making it a cornerstone of [[fundamental-analysis]] and [[valuation]].

## Formula

$$\text{EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Common Shares Outstanding}}$$

Preferred dividends are subtracted because EPS represents earnings available to common shareholders only. The share count is time-weighted across the reporting period to reflect buybacks and issuances.

### Worked Example (illustrative numbers)

Assume a hypothetical company reports, for its fiscal year:

- Net income: **$520 million**
- Preferred dividends: **$20 million**
- Weighted-average basic shares: **250 million**
- Dilutive securities (in-the-money options, RSUs, convertibles): **+15 million** share equivalents

| Step | Calculation | Result |
|------|-------------|--------|
| Earnings to common | $520M − $20M | $500M |
| **Basic EPS** | $500M ÷ 250M | **$2.00** |
| Diluted share count | 250M + 15M | 265M |
| **Diluted EPS** | $500M ÷ 265M | **$1.89** |

The 5.7% gap between basic and diluted EPS is the "dilution overhang" — the claim that option- and convertible-holders have on each dollar of profit. If the stock trades at $40, the trailing [[price-to-earnings-ratio|P/E]] on diluted EPS is $40 ÷ $1.89 ≈ **21.2x**, the more conservative (and more honest) figure to quote.

## Basic vs. Diluted EPS

**Basic EPS** uses only currently outstanding common shares. **[[diluted-eps|Diluted EPS]]** adds the effect of all potentially dilutive securities: stock options, warrants, convertible bonds, convertible preferred stock, and restricted stock units. Diluted EPS is always less than or equal to basic EPS and is the figure serious analysts prefer because it reflects the fully-loaded claim on earnings. The dilution is computed via the **treasury-stock method** for options/warrants (assume proceeds buy back shares at the average price) and the **if-converted method** for convertibles (assume conversion, add back the related interest/dividend, net of tax). Anti-dilutive securities — those that would *raise* EPS — are excluded by rule.

## EPS Variants at a Glance

| Variant | What it uses | When it's quoted |
|---------|--------------|------------------|
| **Basic EPS** | Outstanding common shares only | Floor figure; required disclosure |
| **[[diluted-eps|Diluted EPS]]** | + all dilutive securities | Conservative, analyst-preferred |
| **GAAP EPS** | Net income per accounting rules | Audited, legally reported |
| **Adjusted / non-GAAP EPS** | Excludes "one-off" items | Beat/miss headlines, guidance |
| **TTM EPS** | Last four reported quarters | Trailing [[price-to-earnings-ratio|P/E]] denominator |
| **Forward EPS** | Next-year consensus estimate | [[forward-pe|Forward P/E]], [[peg-ratio|PEG]] |

## GAAP vs. Adjusted (Non-GAAP) EPS

GAAP EPS follows strict accounting rules. Adjusted or "non-GAAP" EPS excludes items management deems non-recurring: restructuring charges, stock-based compensation, acquisition costs, impairments. Adjusted EPS is usually higher and is what analysts quote in "beat/miss" headlines, but it can mask genuine ongoing costs — stock-based compensation in particular is a real economic expense.

## TTM vs. Forward EPS

**Trailing Twelve Months (TTM)** EPS sums the last four reported quarters and anchors the trailing [[price-to-earnings-ratio]]. **Forward EPS** is the analyst consensus estimate for the next fiscal year and drives [[forward-pe|forward P/E]] and the [[peg-ratio]]. Forward EPS powers price targets and is revised constantly through earnings season. TTM is fully objective (reported numbers) but backward-looking; forward EPS is forward-looking but subjective and systematically optimistic, so the two views often disagree on whether a stock is "cheap."

## EPS Growth and Compounding

Because absolute EPS is meaningless across companies, the rate of EPS growth is what valuation hangs on. If a company earns $2.00 today and grows EPS at a steady 12% per year, in five years it earns approximately:

$$ \text{EPS}_{5} = 2.00 \times (1.12)^5 \approx \$3.52 $$

If the market continues to award the same multiple, the share price roughly tracks that 76% earnings gain — the engine behind long-run equity compounding. This is why the [[peg-ratio]] divides the [[price-to-earnings-ratio|P/E]] by the growth rate: a 20x P/E backed by 20% growth (PEG = 1.0) is treated very differently from a 20x P/E backed by 5% growth (PEG = 4.0).

## Buybacks and Artificial Growth

Share repurchases shrink the denominator, mechanically boosting EPS even when net income is flat. A company growing EPS at 10% annually while growing net income at only 2% is engineering the gap through buybacks — a fact critics of financial engineering frequently highlight. The reverse is also true: dilutive secondary offerings or heavy stock-based compensation expand the share count and *suppress* EPS growth, which is why diluted share-count trends deserve as much attention as the EPS headline itself.

## Common Pitfalls and Quality Red Flags

- **Adjusted-EPS inflation** — adding back recurring stock-based compensation, "restructuring" charges that recur every year, or amortization of acquired intangibles can turn a GAAP miss into a non-GAAP beat. Always reconcile adjusted to GAAP.
- **Buyback-driven growth** — rising EPS with flat or falling net income is financial engineering, not operating improvement.
- **Low earnings quality** — EPS backed by accruals rather than [[free-cash-flow|cash flow]] is fragile; compare net income to operating cash flow.
- **One-time gains** — asset sales or tax windfalls can spike a single quarter's EPS; normalize them out.
- **Negative or near-zero EPS** — makes the [[price-to-earnings-ratio|P/E]] meaningless; fall back on sales, cash-flow, or book-value multiples.
- **Share-count timing games** — late-period buybacks can flatter the weighted-average denominator.

## Typical Ranges and Limitations

Absolute EPS values are meaningless in isolation — a $0.50 EPS stock can be vastly more expensive than a $50 EPS stock. What matters is EPS **growth** (mature firms: 5–10%, growth firms: 15–30%+) and EPS **quality** (backed by cash flow, not accruals). EPS ignores capital intensity, debt levels, and cash generation, so pair it with [[return-on-equity]], [[return-on-invested-capital]], and [[free-cash-flow]].

## Trading Relevance

EPS is the single most market-moving data point in the equity calendar. The quarterly "earnings surprise" — reported EPS versus the [[earnings-per-share|consensus]] estimate compiled by data vendors — drives some of the largest single-day moves in individual stocks, and the resulting **[[post-earnings-announcement-drift|post-earnings-announcement drift (PEAD)]]** is one of the most durable documented [[anomalies-overview|anomalies]] in finance: stocks that beat continue to outperform for weeks, and stocks that miss keep underperforming. Earnings-revision momentum (trading the direction in which analysts are changing their forward EPS estimates) is a workhorse signal in quantitative equity. For valuation, EPS is the denominator of the [[price-to-earnings-ratio]] and [[forward-pe|forward P/E]], and forward EPS feeds the [[peg-ratio]]. Traders must watch the basic-vs-diluted and GAAP-vs-adjusted distinctions carefully: a "beat" on adjusted EPS that adds back recurring stock-based compensation can mask a GAAP miss.

## Related

- [[price-to-earnings-ratio]]
- [[earnings]]
- [[return-on-equity]]
- [[financial-statement-analysis]]
- [[fundamental-analysis]]

## Sources

- US GAAP ASC 260 / IFRS IAS 33 — *Earnings Per Share* (accounting standards governing basic and diluted EPS calculation and presentation)
- SEC Regulation G — rules governing the reconciliation of non-GAAP (adjusted) EPS to GAAP figures
- Bernard, V. & Thomas, J. (1989), "Post-Earnings-Announcement Drift" — foundational research on the EPS-surprise anomaly
- CFA Institute curriculum, *Financial Reporting and Analysis* — EPS computation and quality of earnings
