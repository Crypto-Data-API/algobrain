---
title: "Rebalancing"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [portfolio-theory, risk-management, slippage]
aliases: ["Rebalancing", "Portfolio Rebalancing"]
domain: [portfolio-theory]
prerequisites: ["[[asset-allocation]]"]
difficulty: beginner
related: ["[[asset-allocation]]", "[[portfolio-theory]]", "[[tax-loss-harvesting]]", "[[transaction-cost-modeling]]", "[[capital-gains]]", "[[diversification]]"]
---

Rebalancing is the process of realigning a portfolio's actual asset weights back to their target [[asset-allocation|allocation]] after market movements have caused drift. A 60/40 stock/bond portfolio that drifts to 70/30 after an equity rally has quietly taken on more risk than intended; rebalancing — selling stocks and buying bonds to return to 60/40 — is fundamentally a [[risk-management]] discipline that prevents a portfolio from becoming inadvertently concentrated in its best-performing (and often most overvalued) asset.

## Why Drift Happens

Different assets earn different returns, so weights diverge from target over time. Left unchecked, the highest-returning asset comes to dominate, and the portfolio's risk profile silently migrates toward that asset's volatility. Rebalancing is the mechanical counter-force: it is a systematic "sell high, buy low" rule that enforces the original risk budget regardless of recent performance or market emotion.

## Rebalancing Methods

There are two primary triggers, plus a hybrid:

- **Calendar-based** — rebalance at fixed intervals (monthly, quarterly, semi-annual, annual) regardless of drift size. Simple and predictable, but rebalances even when drift is trivial and ignores drift that builds between dates.
- **Threshold-based (percentage-of-portfolio bands)** — rebalance whenever any asset drifts beyond a predefined band, e.g. whenever equities exceed 65% or fall below 55% around a 60% target. Responds promptly to large moves and avoids needless trading when drift is small.
- **Hybrid (calendar + threshold)** — check at regular intervals but only trade when a band is breached. This is the approach most academic research (notably Vanguard's) favours, capturing the discipline of both while minimising turnover.

| Method | Trigger | Pros | Cons |
|---|---|---|---|
| **Calendar** | Fixed date (e.g. quarterly) | Simple, predictable, easy to automate | Trades on trivial drift; misses mid-period drift |
| **Threshold** | Drift past a band (e.g. ±5%) | Responds to real moves; no needless trades | Requires monitoring; can cluster trades in volatile periods |
| **Hybrid** | Check on calendar, trade only if band breached | Low turnover + discipline; research-favoured | Slightly more complex to specify |

## Worked Example: Drift and Restore

Start with a **$100,000** portfolio at a 60/40 target — $60k equities, $40k bonds. Equities rally +25% while bonds are flat:

| | Before drift | After equity +25% | After rebalance |
|---|---|---|---|
| Equities | $60,000 (60%) | $75,000 (**65.2%**) | $69,000 (60%) |
| Bonds | $40,000 (40%) | $40,000 (**34.8%**) | $46,000 (40%) |
| Total | $100,000 | $115,000 | $115,000 |

The portfolio drifted to 65/35 — meaningfully riskier than intended. A ±5% absolute band around the 60% target (trade if equities exit the 55%-65% range) is breached at 65.2%, so the rule fires: **sell ~$6,000 of equities, buy ~$6,000 of bonds** to restore 60/40. Note the mechanical "sell-high" action — trimming the asset that just ran.

## The Rebalancing Bonus

In volatile, mean-reverting markets the mechanical act of selling winners and buying losers can capture a small return premium — the "rebalancing bonus" or "diversification return" — estimated at roughly 0.5-1.5% annually in diversified portfolios, scaling with asset volatility and *inversely* with [[correlation]] (the more independent and volatile the assets, the larger the bonus). The bonus is not free money; it is compensation for taking the contrarian side of [[momentum]], and it can turn negative in strongly trending markets where letting winners run would have paid more.

The bonus is closely related to [[diversification]]'s "free lunch": the same low-correlation, high-volatility ingredients that make diversification reduce risk also feed the rebalancing premium. A useful intuition — the diversification return is approximately the gap between a portfolio's *arithmetic* (rebalanced) and *geometric* (buy-and-hold) average returns; volatility drag on individual assets is partly recovered at the portfolio level by rebalancing.

## Costs: Why You Should Not Rebalance Too Often

Rebalancing carries real frictions that erode or reverse the bonus:

- **Transaction costs** — commissions and [[bid-ask-spread|bid-ask spreads]], material in less liquid asset classes (see [[transaction-cost-modeling]]).
- **Taxes** — in taxable accounts, selling appreciated assets triggers [[capital-gains|capital gains tax]], which can more than offset the rebalancing bonus.

Tax-efficient alternatives:

1. **Cash-flow rebalancing** — direct new contributions (or dividends) into underweight assets, restoring balance without selling.
2. **Rebalance inside tax-advantaged accounts** — IRAs/401(k)s in the US, superannuation in Australia, where trades are not taxable events.
3. **Pair with [[tax-loss-harvesting]]** — realise offsetting losses in the same window to neutralise gains.
4. **Lot selection** — sell highest-cost-basis (or long-term) lots first to minimise the realised gain per share sold.

### Cost / benefit trade-off

The decision to rebalance is a contest between the **rebalancing bonus** (and risk control) on one side and **drag** on the other:

| Driver | Pushes toward MORE frequent rebalancing | Pushes toward LESS frequent |
|---|---|---|
| Asset volatility | High — drift accumulates fast | Low |
| [[correlation\|Correlation]] between assets | Low — bigger bonus | High |
| Transaction costs / [[bid-ask-spread\|spreads]] | Low | High — friction dominates |
| Tax status | Tax-advantaged account | Taxable — [[capital-gains\|gains]] drag |
| Risk tolerance for drift | Low (want tight tracking) | High |

Because over-trading reliably bleeds more than the bonus pays, the practical answer for most portfolios is *infrequent* rebalancing — annual or threshold-triggered — not monthly.

## Trading Relevance

For long-term investors, rebalancing is the single most important ongoing portfolio discipline after the initial [[asset-allocation]] decision — it controls risk and removes emotion. For systematic traders, rebalancing schedules are an explicit design choice with measurable cost: more frequent rebalancing tracks the target risk profile tighter but bleeds turnover, so the optimal frequency balances tracking error against trading and tax drag. Note that predictable calendar rebalancing by large funds (e.g. month-end and index-reconstitution flows) is itself a tradable phenomenon — see [[rebalancing-flows]].

## Related

- [[asset-allocation]] — defines the targets rebalancing restores
- [[portfolio-theory]] — the framework justifying fixed risk budgets
- [[tax-loss-harvesting]] — pairs with rebalancing for tax efficiency
- [[transaction-cost-modeling]] — quantifying the cost side
- [[rebalancing-flows]] — trading the predictable rebalancing of large funds
- [[diversification]] — the source of the rebalancing bonus

## Sources

- Vanguard Research, "Getting back on track: A guide to smart rebalancing" (2010, updated) — the standard study comparing calendar vs threshold methods.
- Bernstein, W. & Wilkinson, D., "Diversification, Rebalancing, and the Geometric Mean Frontier" (1997) — the rebalancing bonus / diversification return.
- Daryanani, G., "Opportunistic Rebalancing" (Journal of Financial Planning, 2008) — threshold-band optimisation.
- Markowitz, H., "Portfolio Selection" (Journal of Finance, 1952) — the mean-variance foundation.
