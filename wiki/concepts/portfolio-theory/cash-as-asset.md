---
title: "Cash as Asset"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [portfolio-theory, risk-management, liquidity, education]
aliases: ["Cash as an Asset Class", "Dry Powder", "Cash Optionality"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[diversification]]", "[[liquidity]]"]
difficulty: beginner
related: ["[[fred-mcnaught]]", "[[alfred]]", "[[portfolio-construction]]", "[[diversification]]", "[[two-portfolio-strategy]]", "[[correlation-breakdown]]", "[[drawdown]]", "[[real-interest-rates]]", "[[opportunity-cost]]"]
---

The principle that cash should be treated as a distinct asset class within a portfolio, not simply as "uninvested funds." Holding cash deliberately gives the investor a position with zero correlation to risk assets, a low-variance store of value, and an embedded option to deploy capital when prices overshoot to the downside. The cost of holding cash is its negative real yield and opportunity cost; the value is its optionality and its role as a [[drawdown]] circuit-breaker.

## Fred McNaught's Principle

> "Always keep cash as an asset. To take advantage of opportunities, you must have cash available."

Fred views cash as an intentional portfolio allocation, not a sign of indecision. The purpose is readiness — when pessimism peaks and prices overshoot downward, the investor with cash can buy quality stocks at discounted prices. Without cash reserves, the investor is forced to watch from the sidelines or sell existing holdings at depressed prices to fund new purchases.

(Source: [[fred-sam-session-2024-01-02]])

## Cash as an Asset Class: Properties at a Glance

| Property | Cash / [[cash-equivalents]] | Why it matters |
|---|---|---|
| Expected return | Low (the [[risk-free-rate]]) | Sets the [[opportunity-cost]] of holding it |
| Volatility | ~0 nominal | Anchors portfolio variance down |
| Correlation to risk assets | ~0, and stable in stress | The rare diversifier immune to [[correlation-breakdown]] |
| Drawdown | ~0 nominal (real value erodes with inflation) | Acts as a [[drawdown]] circuit-breaker |
| Embedded optionality | High in volatile markets | A strike-less call on every asset you might buy |
| Real return | Can be negative (inflation) | The hidden cost; see [[real-interest-rates]] |
| Liquidity | Maximal | The whole point — instant deployability |

## Cash as a Portfolio-Theory Position

In mean-variance terms, cash (or a short-dated T-bill) is the closest real-world proxy for the risk-free asset that anchors the [[capital-asset-pricing-model|CAPM]] and the [[efficient-frontier|capital market line]]. Its key properties:

- **Near-zero variance and near-zero correlation** with risk assets. Unlike most "diversifiers," cash does not suffer [[correlation-breakdown|correlation breakdown]] — it stays uncorrelated precisely in the stress regimes where stock-bond and cross-equity correlations spike toward +1.
- **Optionality value.** Holding cash is economically equivalent to owning a perpetual, strike-less call on every asset the investor might want to buy. The value of that option rises with volatility: in dislocations, the ability to buy at distressed prices can be worth far more than the foregone carry.
- **Drawdown control.** A 10-30% cash buffer mechanically caps portfolio [[drawdown]]: a portfolio that is 80% invested falls 80% as far as a fully invested one in a crash, and recovers from a shallower hole (recovery math is convex — a 50% loss needs a 100% gain to break even).

### The Cost: Cash Drag and Negative Real Yield

Cash is not free to hold. Its drawbacks are:

- **Cash drag** — over long horizons equities compound well above cash, so a permanent large cash allocation lowers expected terminal wealth (see [[compounding]]).
- **Negative real yield** — when the nominal cash rate is below inflation, real purchasing power erodes. Cash held through the 2021-2022 inflation spike lost ~8-15% of real value. The relevant metric is the [[real-interest-rates|real rate]], not the headline nominal rate.
- **Opportunity cost** — capital in cash is capital not earning the [[equity-risk-premium]].

The optimal cash level is therefore a trade-off: enough to fund opportunities and absorb drawdowns, not so much that drag dominates. Practitioners often size it as a function of perceived valuation (more cash when markets are expensive) rather than a fixed percentage.

### Worked Example: Why a Cash Buffer Helps Recovery

Recovery math is convex — a deeper hole needs a disproportionately larger gain to climb out:

| Portfolio | Equity weight | Loss in a -50% crash | Gain needed to recover |
|---|---|---|---|
| Fully invested | 100% | -50% | +100% |
| 20% cash buffer | 80% | -40% | +67% |
| 40% cash buffer | 60% | -30% | +43% |

The 20%-cash portfolio not only falls less, it needs a far smaller rebound — and the cash itself can be *deployed at the bottom*, buying more shares per dollar. The deployed cash converts a defensive position into an offensive one precisely when [[expected-return]] is highest. This is the mechanism behind "dry powder." (Figures illustrative; ignores the cash drag in the years before the crash, which is the offsetting cost.)

## The Buffett and Marks Cash Stance

Two of the most-cited investors treat cash as a deliberate strategic holding, not residue:

- **Warren Buffett.** [[berkshire-hathaway|Berkshire Hathaway]] has repeatedly built very large cash and [[treasuries|T-bill]] piles when Buffett finds few attractively-priced opportunities, then deployed aggressively into dislocations (e.g., 2008 deals with Goldman Sachs and GE). Buffett frames cash as "optionality" and famously compared it to oxygen — unnoticed until absent. The willingness to *under-perform in late-cycle melt-ups* in exchange for ammunition in the bust is the discipline most retail investors lack.
- **Howard Marks** (*The Most Important Thing*, 2011) argues the value of cash is **the option it embeds**: patience plus liquidity lets a contrarian buy from forced sellers at distressed prices. Marks ties this to his "where are we in the cycle?" framework — hold more cash when risk is being underpriced, less when it is being over-punished.

Both views agree with Fred's principle: cash is held *for what it lets you do later*, and its worst feature (low yield) is the premium paid for that option.

## When to Deploy Cash

- **Market-wide dips** — Buy quality stocks when the broader market falls and drags down all prices
- **Individual stock dips** — Accumulate positions in companies on your watch list when they temporarily decline
- **Capital raises** — Participate in discounted capital raises from companies you already hold

## Relationship to Other Concepts

Cash as asset connects to Fred's broader framework:
- [[two-portfolio-strategy]] — Cash serves both portfolios: core (buying dips in quality stocks) and trading (opportunistic entries)
- [[diversification]] — Cash is itself a diversification across asset classes
- Behavioural discipline — Holding cash prevents the impulse to be "fully invested" and forced to sell at the worst time

## Pitfalls and Risks

Treating cash as an asset is powerful but easy to get wrong:

- **Permanent over-allocation (chronic cash drag).** A large *structural* cash weight held through a multi-year bull market is the single biggest drag on long-run [[compounding]]. Cash is a tactical and optionality tool, not a default home for the bulk of a long-horizon portfolio.
- **Market timing in disguise.** "Raising cash because stocks feel expensive" is timing the market, which is notoriously hard. Tie cash levels to observable [[valuation]] signals and a written rule rather than mood.
- **Inflation erosion.** In zero- or negative-real-rate regimes, idle cash quietly loses purchasing power; the 2021-22 inflation spike cost cash-holders roughly 8-15% in real terms.
- **Never deploying.** The option only has value if exercised. Investors who hoard cash through every dip "waiting for the bottom" capture the cost (drag) without the benefit (buying low). A pre-committed deployment plan (see [[#When to Deploy Cash]]) counters this.
- **Reaching for yield in the cash sleeve.** Chasing a few extra basis points pushes cash down the [[cash-equivalents|liquidity ladder]] into [[commercial-paper]] or prime funds that can gap or gate in a crisis — defeating the buffer's purpose. Keep the buffer genuinely liquid.

## Related

- [[portfolio-construction]]
- [[risk-management]]
- [[cash-equivalents]] — the instruments that implement the cash sleeve
- [[opportunity-cost]], [[real-interest-rates]], [[liquidity-risk]]
- [[two-portfolio-strategy]], [[diversification]], [[drawdown]]
- [[fred-mcnaught]]

## Sources

- [[fred-sam-session-2024-01-02]] — Clip 1: "Always keep cash as an asset"
- [[fred-sam-session-2024-01-18]] — Investing concepts
- Sharpe, W. (1964). "Capital Asset Prices" — the risk-free asset and the capital market line.
- Marks, H. *The Most Important Thing* (2011) — cash, patience, and the optionality of "dry powder" in distressed markets.
- General market knowledge; the recovery-math and carry tables are illustrative, and Buffett/Berkshire cash behaviour is drawn from widely reported public record.
