---
title: "Buy and Hold"
type: strategy
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, position-trading, portfolio-theory, sp500]
aliases: ["Buy and Hold", "Buy-and-Hold", "Long-Term Investing", "Passive Long-Only"]
related: ["[[passive-investing]]", "[[index-funds]]", "[[dca-strategy]]", "[[value-investing]]", "[[diversification]]", "[[dollar-cost-averaging]]", "[[value-averaging]]", "[[efficient-market-hypothesis]]"]
strategy_type: fundamental
timeframe: long-term
markets: [stocks, crypto]
complexity: beginner
backtest_status: walk-forward-validated
edge_source: [risk-bearing]
edge_mechanism: "Harvests the equity risk premium: long-term holders are compensated for bearing market risk and providing patient capital, while avoiding the costs, taxes, and behavioral errors that erode the returns of active traders. The persistent counterparty is the active trader whose costs and timing mistakes transfer return to the patient holder."
data_required: [ohlcv-daily, fundamentals-pit]
min_capital_usd: 100
capacity_usd: 1000000000000
crowding_risk: low
expected_sharpe: 0.45
expected_max_drawdown: 0.55
breakeven_cost_bps: 5
---

Buy and hold is a long-term, low-turnover strategy in which an investor purchases a diversified basket of assets — most commonly a broad equity [[index-funds|index fund]] — and holds it for years or decades regardless of intervening market fluctuations, rather than attempting to time entries and exits. It is the foundational form of [[passive-investing|passive investing]] and the practical embodiment of the empirical claim that, after costs, most active timing and stock-picking underperforms simply owning the market. The strategy's return comes not from any forecasting skill but from harvesting the long-run **equity risk premium** while minimizing costs, taxes, and behavioral mistakes.

## Edge source

Buy and hold is a **risk-bearing** strategy from the [[edge-taxonomy]]. The investor is paid the equity risk premium for holding assets through volatility and providing patient capital that short-term participants are unwilling or unable to supply. There is no informational, analytical, or latency edge — and that is the point. The secondary, almost-free edge is *cost and behavior avoidance*: by trading rarely, the buy-and-hold investor sidesteps commissions, bid-ask [[spread|spreads]], short-term capital-gains taxes, and the well-documented gap between investor returns and fund returns caused by buying high and selling low.

## Why this edge exists

Stocks have historically returned more than bonds and cash because equity holders bear residual business and market risk; the long-run U.S. equity premium has averaged roughly 4–6% per year over bonds. This premium persists because risk is genuinely unpleasant — drawdowns of 30–50% recur, and most participants cannot or will not endure them, so they demand compensation to hold. Buy and hold collects that compensation in full by simply not selling. The "other side" is the cohort of active traders and market timers whose aggregate pre-cost return must equal the market (they hold the same assets in aggregate) but whose *after-cost* return is lower by exactly their trading costs and taxes — a return that transfers, in expectation, to patient holders and intermediaries. [[dalbar|Behavioral-gap studies]] repeatedly show the average investor underperforms the very funds they own by trading at the wrong times; buy and hold eliminates that gap by design.

## Null hypothesis

Buy and hold *is* close to the null for active strategies: under the [[efficient-market-hypothesis|efficient-market hypothesis]], no active strategy beats a low-cost, diversified buy-and-hold portfolio net of costs. The relevant test of buy-and-hold itself is whether the chosen assets carry a positive long-run risk premium. For broad, diversified equity indices this is strongly supported by a century of data. For a single stock or a narrow basket, the null is real: buy-and-hold of an undiversified position has no guaranteed premium and can go to zero (idiosyncratic risk is uncompensated), so concentration converts a risk-bearing edge into a gamble.

## Rules

- **Selection**: prefer broad, diversified, low-cost vehicles (total-market or S&P 500 index funds/ETFs) over individual stocks; if picking stocks, hold a diversified basket (see [[diversification]]).
- **Entry**: lump-sum when capital is available, or phase in via [[dollar-cost-averaging|dollar-cost averaging]] / [[dca-strategy]] to reduce timing regret.
- **Position sizing**: size to a long-horizon asset allocation (e.g., an age- or risk-appropriate stock/bond split) the investor can hold through a 50% drawdown without selling.
- **Holding**: do nothing in response to volatility, news, or forecasts. Reinvest dividends.
- **Rebalancing**: periodically (e.g., annually, or on a band such as ±5% drift) rebalance back to target weights — the only systematic "trade."
- **Exit**: only on a change in goals, time horizon, or a permanent impairment of the thesis — not on price moves.

## Implementation pseudocode

```python
def buy_and_hold_year(portfolio, target_weights, new_cash, rebalance_band=0.05):
    # 1. invest any new cash at current target weights
    for asset, w in target_weights.items():
        portfolio[asset] += new_cash * w
    # 2. reinvest dividends/coupons (assumed already credited to portfolio)
    # 3. rebalance only if drift exceeds band
    total = sum(portfolio.values())
    for asset, w in target_weights.items():
        actual_w = portfolio[asset] / total
        if abs(actual_w - w) > rebalance_band:
            portfolio[asset] = total * w     # trade back to target
    # 4. otherwise: hold. No reaction to price, news, or forecasts.
    return portfolio
```

## Indicators / data used

- None for entries/exits by design — the strategy explicitly avoids timing signals.
- Long-horizon asset-allocation target (the only real input).
- For stock-pickers: point-in-time fundamentals and [[diversification]] checks at purchase.
- Periodic prices only for rebalancing and reporting.

## Example trade

In January 2000 an investor places $10,000 in a total-market S&P 500 index fund and never sells, reinvesting dividends. They endure the dot-com crash (−49% peak-to-trough), the 2008 financial crisis (−57%), the 2020 COVID crash (−34%), and other drawdowns. By 2024 the position has compounded to roughly $35,000–$45,000 (≈9–10% annualized with dividends reinvested), despite three brutal bear markets — because the investor never crystallized the losses by selling. An active trader who exited near the 2009 or 2020 bottoms and re-entered after the recovery would, on the historical evidence, very likely have ended with less.

## Performance characteristics

Broad-equity buy-and-hold has historically delivered roughly 7–10% nominal annualized total return (≈6–7% real) over multi-decade horizons, with annual volatility around 15–20% and recurring drawdowns of 30–55%. The realized Sharpe of a single equity index is modest (~0.4–0.5); a stock/bond mix raises risk-adjusted return. Costs are minimal — a few basis points of fund expense plus occasional rebalancing trades — which is the strategy's structural advantage: it keeps essentially the entire gross risk premium. The dominant cost is *behavioral*, not financial: the discipline to hold through deep drawdowns.

## Capacity limits

Effectively unlimited for broad indices — buy-and-hold of the market portfolio is the aggregate position of all passive investors and scales to trillions. There is no capacity constraint at the strategy level. (Concerns about passive investing's *market-wide* effects on price discovery are a separate, macro question, not a constraint on an individual's capacity.)

## What kills this strategy

- **Selling at the bottom**: capitulating during a drawdown converts a temporary decline into a permanent loss — the single most common failure (see [[failure-modes]] and [[loss-aversion]]).
- **Concentration**: holding a single stock or narrow basket exposes uncompensated idiosyncratic risk; the company can permanently impair or go to zero.
- **Wrong time horizon**: needing the money during a drawdown forces a sale at the worst time.
- **Secular stagnation / lost decades**: an asset or market can deliver near-zero real returns for 10–20 years (e.g., Japan post-1989), so the premium is not guaranteed over any finite horizon.

## Kill criteria

- Time horizon shrinks below ~5–7 years (the holding can no longer reliably ride out a drawdown) → shift toward lower-risk assets.
- A single position grows beyond a concentration limit (e.g., >10–15% of the portfolio) → trim for diversification, not for timing.
- Permanent, fundamental impairment of a held company's business (not a price drop) → exit that position.
- The investor's demonstrated behavior shows they cannot hold through drawdowns → reduce equity allocation to a level they can actually stick with.

## Advantages

- Captures the full equity risk premium with minimal cost and tax drag.
- Beats most active strategies after costs (strong empirical support).
- Trivial to implement and maintain; no forecasting required.
- Tax-efficient (defers capital gains) and time-efficient.

## Disadvantages

- Endures the full depth of bear-market drawdowns (no downside protection).
- Requires strong behavioral discipline through long, painful declines.
- No guaranteed premium over any finite horizon — "lost decades" happen.
- Dangerous if applied to concentrated or undiversified positions.

## Sources

- Burton Malkiel, *A Random Walk Down Wall Street* — the classic case for passive, long-horizon, diversified holding.
- John C. Bogle, *The Little Book of Common Sense Investing* — cost-minimizing index buy-and-hold.
- SPIVA (S&P Indices Versus Active) scorecards — recurring evidence that most active funds underperform their benchmark over long horizons.
- Dimson, Marsh & Staunton, *Credit Suisse / UBS Global Investment Returns Yearbook* — long-run equity risk premium data.

## Related

- [[passive-investing]]
- [[index-funds]]
- [[dca-strategy]]
- [[dollar-cost-averaging]]
- [[value-averaging]]
- [[value-investing]]
- [[diversification]]
- [[efficient-market-hypothesis]]
