---
title: "Return on Equity (ROE)"
type: concept
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, profitability, metrics, financial-statements]
aliases: ["ROE", "roe", "return on equity"]
domain: [fundamental-analysis]
difficulty: beginner
related: ["[[return-on-assets]]", "[[return-on-invested-capital]]", "[[earnings-per-share]]", "[[debt-to-equity]]", "[[financial-statement-analysis]]"]
---

Return on Equity (ROE) measures how efficiently a company generates profit from the capital contributed by its common shareholders. It is one of the most widely cited profitability ratios in [[fundamental-analysis]] and a core input to quality-investing screens.

## Formula

$$\text{ROE} = \frac{\text{Net Income}}{\text{Average Shareholders' Equity}}$$

Average equity is typically the mean of beginning-of-period and end-of-period book equity. Using the average (rather than ending) equity avoids distortions from buybacks, issuances, or large retained-earnings moves during the period.

## DuPont Decomposition

The DuPont identity decomposes ROE into three intuitive drivers:

$$\text{ROE} = \text{Net Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

That is: (Net Income / Revenue) × (Revenue / Assets) × (Assets / Equity). This separates **profitability** (margin), **efficiency** (turnover), and **leverage** (equity multiplier). Two firms can post identical 20% ROE via very different paths — one through fat margins, another through aggressive leverage. The full mechanics live at [[dupont-analysis]].

| DuPont term | Formula | What it measures |
|---|---|---|
| Net profit margin | Net Income / Revenue | Profitability — pricing power, cost control |
| Asset turnover | Revenue / Assets | Efficiency — sales generated per dollar of assets |
| Equity multiplier | Assets / Equity | Financial leverage — how much debt funds the assets |

There is also a **five-step DuPont** that further splits net margin into tax burden, interest burden, and operating margin (EBIT/Revenue), isolating how much of ROE comes from operations versus tax and financing structure.

### Worked Example: Same ROE, Different DNA

Two companies each post **18% ROE** but get there differently:

| | Company V (premium brand) | Company W (discount retailer) |
|---|---|---|
| Net margin | 18% | 3% |
| Asset turnover | 0.5× | 3.0× |
| Equity multiplier | 2.0× | 2.0× |
| **ROE** | 0.18 × 0.5 × 2.0 = **18%** | 0.03 × 3.0 × 2.0 = **18%** |

Identical headline ROE, opposite business models: V earns fat margins on slow-turning assets; W earns thin margins on fast-turning inventory. DuPont makes the difference visible — and tells you which lever is at risk (V's margin to competition, W's turnover to a demand slowdown).

### Worked Example: Leverage Inflating ROE

A firm earns **$10M** net income. With **$100M** equity, ROE = **10%**. It borrows $50M and buys back stock, cutting equity to **$50M**; if net income holds near $10M, ROE jumps to **20%** — doubled with zero operational improvement. The DuPont equity multiplier rose from ~1.0 to ~3.0× (assuming flat assets), which is the entire source of the "improvement."

## Leverage Distortion

Because the equity multiplier appears as a direct factor, adding debt mechanically boosts ROE even if the underlying business is unchanged. A company that buys back stock with borrowed money shrinks equity, raises leverage, and inflates ROE without improving operational performance. This is why analysts cross-check ROE with [[return-on-assets]] and [[return-on-invested-capital]], which strip out or penalize leverage effects.

### ROE vs ROA vs ROIC

| Metric | Numerator | Denominator | Treats leverage as |
|---|---|---|---|
| **ROE** | Net income | Shareholders' equity | A *benefit* (boosts the ratio) |
| **[[return-on-assets\|ROA]]** | Net income | Total assets | Neutral (debt-funded assets in denominator) |
| **[[return-on-invested-capital\|ROIC]]** | NOPAT (after-tax operating profit) | Debt + equity (invested capital) | Neutral; the cleanest read of operating quality |

A wide gap between high ROE and modest ROA/ROIC is the tell-tale sign that leverage — not operating excellence — is doing the work. Quality investors prize businesses where ROIC comfortably exceeds the [[weighted-average-cost-of-capital|cost of capital]], because that is what creates value as the firm reinvests.

## How Investors and Analysts Use ROE

- **Quality / moat screens.** Sustained high ROE (with low leverage) is the quantitative fingerprint of a durable competitive advantage; it is a core filter in [[quality-factors|quality]] and [[factor-investing|factor]] strategies.
- **Sustainable growth rate.** ROE × retention ratio (1 − payout) estimates how fast a firm can grow earnings funding itself — the basis of the sustainable-growth formula used in [[fundamental-analysis]] and [[discounted-cash-flow|DCF]] terminal-value assumptions.
- **Trend over time.** Rising ROE driven by *margin* expansion is healthier than rising ROE driven by the *equity multiplier* (leverage). DuPont reveals which.
- **Peer comparison.** Only meaningful *within* an industry, because capital structures and asset intensity differ enormously across sectors.

## Typical Ranges

Across the broad market, sustained ROE in the 15–20% range is considered strong. ROE consistently above 25% is exceptional and often signals a durable competitive moat — though it should be verified against [[debt-to-equity]] to confirm it is not leverage-driven. Capital-light software and consumer-brand firms routinely post 30–60%+ ROE; capital-intensive utilities and industrials live in the 8–12% band. Financial sector ROE typically clusters around 10–15%.

## Buffett's Preference

Warren Buffett has repeatedly cited sustained ROE above 15% (without excessive leverage) as a hallmark of the "wonderful businesses" he seeks. In his framework, a business that can reinvest capital at high incremental returns compounds intrinsic value far faster than peers.

## Limitations

- Book equity can be distorted by goodwill, write-downs, and buybacks (buybacks at prices above book can push equity negative, making ROE meaningless).
- Cyclical companies show wildly varying ROE across the cycle — use normalized multi-year averages.
- ROE is not comparable across industries with different capital structures.
- High ROE achieved through leverage is fragile in downturns.

## Related

- [[dupont-analysis]] — the full margin × turnover × leverage decomposition
- [[return-on-assets]]
- [[return-on-invested-capital]]
- [[debt-to-equity]]
- [[earnings-per-share]]
- [[financial-statement-analysis]]
- [[quality-factors]] — ROE as a quality signal in factor investing
- [[fundamental-analysis]]

## Sources

- DuPont Corporation — the DuPont identity, originated internally in the 1920s and now a standard analytical framework.
- Buffett, W., Berkshire Hathaway shareholder letters — return-on-equity as a hallmark of "wonderful businesses."
- CFA Institute, *Financial Statement Analysis* curriculum — DuPont decomposition and leverage effects.
- Damodaran, A., *Investment Valuation*, 3rd ed. — limitations of book-value-based equity returns.
- Investopedia, "Return on Equity (ROE)" — definition, formula, and benchmark ranges.
