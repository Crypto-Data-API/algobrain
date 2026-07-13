---
title: "Value Averaging"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, portfolio-theory, stocks, mean-reversion]
aliases: ["Value Averaging", "Value Path", "VA"]
related: ["[[dca-strategy]]", "[[portfolio-theory]]", "[[dollar-cost-averaging]]", "[[position-sizing]]", "[[mean-reversion]]", "[[rebalancing]]"]
strategy_type: quantitative
timeframe: long-term
markets: [stocks]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [behavioral, analytical]
edge_mechanism: "Mechanically buys more after declines and trims after rallies, harvesting short-horizon index mean reversion supplied by performance-chasing investors who buy high and sell low."
data_required: [ohlcv-daily]
min_capital_usd: 1000
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: 0.4          # ~market Sharpe; VA adds ~0.5-1.5%/yr IRR over DCA before tax/cash drag
expected_max_drawdown: 0.45   # equity-market drawdown, slightly dampened by counter-cyclical contributions
breakeven_cost_bps: 25
kill_criteria: |
  - required contribution exceeds 5x the base contribution and the cash reserve is exhausted
  - rolling 10-year IRR trails plain DCA on the same asset by > 1%/yr after tax and cash drag
  - realized tax drag from forced sales exceeds 1%/yr for 3 consecutive years
---

# Value Averaging

Value averaging (VA) is an investment strategy developed by Michael Edleson in his 1991 book *Value Averaging: The Safe and Easy Strategy for Higher Investment Returns*. Unlike [[dollar-cost-averaging|dollar-cost averaging (DCA)]], which invests a fixed dollar amount at regular intervals regardless of market conditions, value averaging sets a target portfolio *value* that grows by a fixed amount each period and adjusts contributions to meet that target. When the portfolio falls below the target path, the investor contributes more; when it rises above the target, the investor contributes less or even sells.

## Value averaging vs. dollar-cost averaging

VA and [[dollar-cost-averaging|DCA]] are the two canonical formula-investing schemes. The key conceptual difference: **DCA fixes the dollars in; VA fixes the portfolio value out.** DCA buys a constant amount; VA buys whatever amount is needed to hit a growing target, which automatically buys more when prices are low and less (or sells) when prices are high.

| Dimension | [[dollar-cost-averaging\|Dollar-cost averaging]] | **Value averaging** |
|---|---|---|
| What is held constant | Dollars contributed per period | Target portfolio *value* per period |
| Contribution in a down market | Same fixed amount | **Larger** (buys the dip mechanically) |
| Contribution in an up market | Same fixed amount | **Smaller**, or sells the excess |
| Cash flow predictability | High (constant) | Low (variable, can spike 3-5x) |
| Cash reserve needed | None | 30-50% of planned contributions |
| Avg cost per share | Lower than lump-sum-at-top | Typically lower than DCA |
| Tax events | Rare (buy-only) | Possible (forced sells in pure variant) |
| Behavioral demand | Low | High (largest buys when most frightened) |
| Best account type | Any | Tax-sheltered (no-sell variant) |
| Headline metric caveat | — | IRR advantage partly a dollar-weighting artifact |

VA is best thought of as **DCA plus a counter-cyclical rebalancing rule** bolted on. Everything that distinguishes it — the edge, the reserve drag, the liquidity risk — flows from that one addition.

## Edge source

Per the [[edge-taxonomy]], VA's claimed edge is **behavioral** with a secondary **analytical** component:

- **Behavioral**: the strategy hard-codes counter-cyclical behaviour — buying more after declines, trimming after rallies — which is the opposite of the documented performance-chasing pattern in retail fund flows (Morningstar's "Mind the Gap" studies consistently measure investor dollar-weighted returns 1-2%/yr below fund time-weighted returns). VA converts a behavioural discipline problem into a mechanical rule.
- **Analytical**: to the extent broad equity indexes exhibit modest multi-month [[mean-reversion]], a rule that scales purchases inversely to recent performance achieves a lower average cost per share than fixed-dollar buying.

This is a weak, low-frequency edge measured in tens of basis points per year, not a market-beating alpha strategy.

## Why this edge exists

The counterparty is the aggregate of return-chasing investors: flows into equity funds reliably peak after strong trailing returns and bottom after drawdowns. They keep losing because the behaviour is driven by emotion (fear after crashes, FOMO after rallies) and by institutional frictions (committees de-risk after losses), neither of which is corrected by the losses themselves. A VA investor is structurally on the other side of those flows — contributing 3-5x the base amount near panic lows and selling into euphoric highs.

The edge persists because it is behaviourally hard to execute: the rule demands the largest cash outlays precisely when the investor is most frightened and their income/liquidity is most likely to be impaired (recessions). The cash-reserve requirement is the "cost" that keeps the edge from being arbitraged away.

## Null hypothesis

If index prices follow a random walk with drift (no mean reversion), VA's average-cost-per-share advantage over DCA shrinks toward zero, and the strategy is equivalent to DCA plus a noisy, path-dependent rebalancing rule. Worse, the apparent IRR advantage found in many simulations is partly a **measurement artifact**: Hayley (Cass Business School) showed that dynamic strategies which invest more after declines mechanically inflate IRR relative to DCA *without* increasing expected terminal wealth — IRR is dollar-weighted, so concentrating dollars in periods that happen to precede recoveries flatters the metric. Under the null, VA delivers market beta, plus cash-reserve drag (holding 20-40% in reserve at T-bill yields), minus extra transaction and tax costs — i.e., it slightly **underperforms** lump-sum investing.

## Rules

**Entry (contribution rule)**
1. Define a value path: target value `V(t) = C × t × (1 + r/n)^t` where `C` is the base periodic contribution, `r` the assumed annual growth rate (Edleson recommends building in 8-10% annualised for equities so contributions don't grow without bound), and `n` periods per year. Simplest form: `V(t) = C × t` (linear path).
2. At the start of each period (monthly or quarterly), compute the gap: `gap = V(t) − current portfolio value`.
3. If `gap > 0`, buy `gap` dollars of the target fund.

**Exit (trim rule)**
4. If `gap < 0` (portfolio above the path), either contribute nothing ("no-sell VA", tax-friendlier) or sell `|gap|` and park proceeds in the cash reserve (pure VA).

**Position sizing / reserves**
5. Maintain a side cash reserve of roughly 30-50% of cumulative planned contributions, since a 30-40% market decline can require contributions 3-5x the base amount.
6. Cap any single contribution at a pre-set multiple (e.g., 5x base) to bound liquidity risk.
7. Use broad index funds or ETFs only — the [[mean-reversion]] assumption does not hold for individual stocks, where averaging down can concentrate into a deteriorating business.

### Choosing the value path

The shape of `V(t)` determines how aggressive the rule is and how fast required contributions can balloon:

| Path type | Formula | Behavior | Trade-off |
|---|---|---|---|
| Linear | `V(t) = C × t` | Target grows by a constant each period | Simple; ignores expected compounding, so later contributions drift down in real terms |
| Growth-adjusted | `V(t) = C × t × (1 + r/n)^t` | Target compounds at assumed rate `r` | Edleson's recommended form; keeps real contributions stable |
| No-sell variant | Same path, `gap < 0` ⇒ skip | Never sells; only buys when below path | Tax-friendlier; gives up the trim discipline |
| Capped | Any path, contribution ≤ `MAX_MULT × C` | Bounds the worst-case outlay | Sacrifices some edge in deep drawdowns to bound liquidity risk |

Edleson recommends building an 8-10% annualised growth assumption into `r` for equities so the target — and therefore required contributions — doesn't grow without bound over long horizons.

## Implementation pseudocode

```python
# Run once per period (monthly or quarterly)
C = base_contribution          # e.g. $1,000/month
r = 0.08                       # assumed annual growth built into the path
n = 12                         # periods per year
MAX_MULT = 5                   # contribution cap

def value_target(t):
    return C * t * (1 + r / n) ** t

def rebalance(t, portfolio_value, cash_reserve):
    gap = value_target(t) - portfolio_value
    if gap > 0:                            # below path -> buy
        buy_amt = min(gap, MAX_MULT * C, cash_reserve + C)
        place_order("BUY", index_etf, dollars=buy_amt)
    elif gap < 0:                          # above path -> trim (or skip if no-sell variant)
        if not NO_SELL_VARIANT:
            place_order("SELL", index_etf, dollars=abs(gap))
            cash_reserve += abs(gap)
        # else: contribute nothing this period
```

## Indicators / data used

- Current portfolio market value (the only live input)
- The pre-computed value path `V(t)`
- Index fund/ETF prices (daily OHLCV is more than sufficient)
- No technical indicators; the strategy is purely a function of portfolio value vs. target

## Example trade

Investor sets a linear path of $1,000/month into an S&P 500 ETF.

| Month | Market move | Portfolio before | Target `V(t)` | VA buys (gap) | DCA buys |
|---|---|---|---|---|---|
| 1 | — | $0 | $1,000 | $1,000 | $1,000 |
| 2 | −10% | $900 | $2,000 | **$1,100** | $1,000 |
| 3 | +20% | $2,400 | $3,000 | $600 | $1,000 |
| 4 | rally | $3,450 | $4,000 | $550 | $1,000 |
| 5 | melt-up | $4,600 | $5,000 | $400 (or sell excess) | $1,000 |

Versus DCA's fixed $1,000/month, the VA investor automatically bought more shares in the cheap month 2 ($1,100) and fewer in the expensive months ($400-600) — lowering average cost per share. Note also the cash-flow contrast: VA's monthly outlay ranged $400-$1,100 here; a sharper drawdown would have pushed it well above $1,000, which is exactly why the cash reserve exists. *(Figures are illustrative of the mechanics, not a backtest.)*

## Performance characteristics

- Simulations and academic comparisons (Marshall 2000; Edleson's own backtests) typically show VA achieving a lower average cost per share than DCA and a **0.5-1.5%/yr higher IRR** over long horizons — but see the IRR-bias caveat under [[#Null hypothesis]]; expected terminal wealth differences are much smaller.
- Realistic cost overlay: with commission-free ETFs and ~1-2 bps spreads on liquid index ETFs, direct transaction costs are negligible (turnover is low, mostly one-way buying). The real costs are (a) **cash-reserve drag** — 30-50% of planned contributions sitting in T-bills typically costs 1-3%/yr in foregone equity premium on that sleeve, and (b) **tax drag** from forced sales in the pure variant (short/long-term capital gains on trims).
- Net of these, VA over a full cycle is roughly a wash against DCA for taxable investors and a modest improvement in tax-sheltered accounts using the no-sell variant.
- Risk profile is equity beta: expect drawdowns near the market's (frontmatter assumes ~45%, slightly below the index because contributions arrive counter-cyclically).

## Capacity limits

Effectively unconstrained at individual scale: the strategy trades the most liquid instruments in the world (broad index ETFs/funds) on a monthly cadence. Capacity in the hundreds of millions per investor before order slicing even becomes a consideration (frontmatter conservatively states $100M). The binding constraint is not market impact but the investor's own cash-reserve capacity during drawdowns.

## What kills this strategy

- **Liquidity failure at the worst moment**: a 40%+ bear market demands the largest contributions exactly when income and credit are most likely to be impaired (2008-09); skipping the big buys destroys the entire mechanism.
- **A non-mean-reverting underlying**: applied to a single stock or sector in secular decline (e.g., averaging down into a Nikkei-style multi-decade bear), VA concentrates capital into a falling asset far more aggressively than DCA.
- **Prolonged melt-up**: years above the value path leave the investor under-invested and trailing both DCA and lump sum, with tax bills from trims.
- **Behavioural abandonment**: the strategy's value is the discipline; overriding the rule during a panic converts it to ad-hoc timing.

## Kill criteria

- Required contribution exceeds **5x** the base amount and the cash reserve is exhausted → switch to no-sell DCA at base rate.
- Rolling **10-year** IRR trails plain DCA on the same asset by **> 1%/yr** after taxes and cash drag.
- Tax drag from forced sales exceeds **1%/yr for 3 consecutive years** in a taxable account → switch to no-sell variant or abandon.

## Advantages

- Systematically buys more at lower prices and less at higher prices
- Historically produces modestly better IRR than DCA in most simulated periods
- Imposes disciplined, rules-based investing; removes timing emotion
- Reduces the impact of poor market timing
- Near-zero direct transaction costs with modern commission-free ETFs

## Disadvantages

- Requires variable and potentially very large cash contributions during downturns (3-5x base after a 30-40% decline)
- Cash reserve drag reduces overall portfolio returns by an estimated 1-3%/yr on the reserve sleeve
- More complex to implement and track than DCA
- Selling during up-markets creates taxable events (pure variant)
- Less suitable for individual stocks (concentration risk)
- The headline IRR advantage is partly a dollar-weighting artifact, not extra terminal wealth

## Sources

- Edleson, M. (1991). *Value Averaging: The Safe and Easy Strategy for Higher Investment Returns*. Wiley reissue 2006, ISBN 978-0470049778.
- Marshall, P. S. (2000). "A Statistical Comparison of Value Averaging vs. Dollar Cost Averaging and Random Investment Techniques." *Journal of Financial and Strategic Decisions*, 13(1).
- Hayley, S. (Cass Business School). "Value Averaging and How Dynamic Strategies Bias the IRR and Modified IRR." Working paper / *Journal of Investment Strategies* — the IRR-bias critique.
- Morningstar, "Mind the Gap" annual studies — investor return gap evidence for the behavioural counterparty.

## Related

- [[dca-strategy]] -- dollar-cost averaging, the simpler alternative
- [[dollar-cost-averaging]]
- [[portfolio-theory]] -- portfolio construction and rebalancing
- [[position-sizing]] -- managing contribution amounts
- [[mean-reversion]] -- the return property VA implicitly bets on
- [[rebalancing]] -- the closely related portfolio discipline
- [[edge-taxonomy]] -- classification of where edges come from
