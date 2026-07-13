---
title: Mean Reversion
type: strategy
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags:
  - quantitative
  - mean-reversion
  - stocks
  - swing-trading
aliases:
  - mean-reversion-strategy
  - reversion-to-mean
  - short-term reversal
related: ["[[rsi-mean-reversion]]", "[[bollinger-band-reversion]]", "[[pairs-trading]]", "[[momentum]]", "[[statistical-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Impatient or forced traders overshoot fair value when demanding immediate liquidity; the reversion trader is paid to absorb that flow and hold until prices snap back."
data_required: [ohlcv-daily]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.20
breakeven_cost_bps: 15
---

# Mean Reversion

A trading strategy that bets prices will return to their historical average after deviating significantly. Common indicators used include [[bollinger-bands]] and [[rsi]] to identify overbought or oversold conditions. Mean reversion is one of the two great families of systematic trading (the other being [[trend-following]]/[[momentum]]) and underpins [[pairs-trading]], [[statistical-arbitrage]], and most market-making.

## Edge source

Per the [[edge-taxonomy]], mean reversion draws primarily on two edge categories:

- **Behavioral** — investors systematically overreact to news, extrapolating short-term moves too far. De Bondt and Thaler (1985) documented long-horizon overreaction; Lehmann (1990) and Jegadeesh (1990) showed that weekly and monthly equity returns exhibit strong short-term reversal.
- **Risk-bearing (liquidity provision)** — a large fraction of short-horizon reversion profit is compensation for absorbing temporary order-flow imbalances. When a fund must sell a position *now*, it pays a concession; the reversion trader collects that concession and carries inventory risk until the price normalizes.

## Why this edge exists

Mean reversion rests on the observation that asset prices tend to oscillate around a long-term average (the "mean"). When prices deviate significantly from this average — due to overreaction, liquidity shocks, or temporary supply/demand imbalances — they tend to snap back. This contrasts with [[momentum]] strategies, which bet that trends will continue.

Who is on the other side, and why do they keep losing (or paying)?

- **Forced and impatient flow**: margin calls, fund redemptions, index rebalances, and stop-loss cascades all generate price-insensitive selling (or buying). These participants are not "losing" out of stupidity — they are paying for immediacy, and they will keep paying because the need for immediacy never disappears.
- **Emotional retail and narrative-chasing traders** who buy after sharp rallies and sell after sharp drops, supplying the overshoot that reverts.
- **Slow-moving institutional constraints** (mandates, tracking-error limits) that prevent natural buyers from stepping in immediately, leaving a window in which prices stay dislocated.

The edge persists because the cost of providing this liquidity — fat-tailed inventory risk, the occasional dislocation that *doesn't* revert — deters enough capital to keep the premium positive.

### Variants across timeframe and instrument

| Variant | Horizon | Signal | Capacity | Notes |
|---------|---------|--------|----------|-------|
| Intraday reversal | minutes–hours | VWAP / micro z-score | Low | Closest to market-making; heaviest cost sensitivity |
| Short-term single-name | days | 2–4 day z-score, [[rsi]](2) | Medium ($20–100M) | The canonical implementation on this page |
| [[pairs-trading]] | days–weeks | Spread z-score (cointegration) | Medium-high | Spreads revert more reliably than single names |
| [[statistical-arbitrage]] | days | PCA/factor residual reversion | High | Many names; residuals after factor removal |
| Index / futures reversion | days | Index z-score, [[bollinger-band-reversion]] | High | More capacity, weaker per-trade edge |
| Cross-sectional reversal | weeks | Rank past-week losers vs winners | High | Lehmann (1990) style; long-short market-neutral |

All variants share the same economics — being paid to provide immediacy — but trade off **capacity against per-trade edge** and against **cost sensitivity** (see [[#Performance characteristics]] and [[#Capacity limits]]).

## Null hypothesis

If prices followed a random walk (Hurst exponent ≈ 0.5, no serial correlation), buying after declines and selling after rallies would produce zero expected gross return, and a *negative* net return equal to round-trip transaction costs times turnover. Concretely: a daily z-score reversal system with ~200% annual turnover per side and 10 bps round-trip costs would bleed roughly 2–4% per year under the null. Any backtest must beat this cost drag with statistical significance — and must also beat a "short volatility" benchmark, since naive reversion P&L is highly correlated with simply selling [[volatility]].

## Rules

A representative single-name equity z-score implementation:

**Universe and filters**
- Liquid large/mid-cap stocks (e.g., top 500 by dollar volume); exclude stocks with earnings or other scheduled announcements within the holding window (news-driven moves revert far less reliably).
- Confirm the traded series is statistically mean-reverting (see [[#Indicators / data used]]) — spreads and indices revert more reliably than single names.

**Entry**
- Compute z = (price − 20-day SMA) / 20-day standard deviation.
- Buy when z ≤ −2 (price stretched ~2σ below its mean); short when z ≥ +2.
- Optional confirmation: 2-period [[rsi]] < 10 for longs (> 90 for shorts), and price above the 200-day SMA for longs (trade reversion only in the direction of the long-term trend).

**Exit**
- Take profit when z crosses back through 0 (price returns to the 20-day mean).
- Time stop: exit after 10 trading days regardless of P&L — if it hasn't reverted by then, the dislocation is probably informational.
- Hard stop: exit if the position moves a further 1.5σ against entry.

**Position sizing**
- Risk a fixed fraction (e.g., 0.5% of equity) per position to the hard stop; cap any single name at 5% of portfolio and run 10–30 concurrent positions for diversification.
- Scale gross exposure down by 50% when realized index volatility (e.g., 20-day) exceeds twice its 1-year median — reversion failure risk clusters in high-vol regimes.

## Implementation pseudocode

```python
for stock in liquid_universe:
    if has_event_within(stock, days=10):    # skip earnings/news windows
        continue
    sma   = mean(close[stock][-20:])
    sigma = std(close[stock][-20:])
    z     = (close[stock][-1] - sma) / sigma

    pos = positions.get(stock)
    if pos is None:
        if z <= -2 and close[stock][-1] > sma200(stock):
            buy(stock, size=risk_budget(0.005, stop_dist=1.5 * sigma))
        elif z >= +2 and close[stock][-1] < sma200(stock):
            sell_short(stock, size=risk_budget(0.005, stop_dist=1.5 * sigma))
    else:
        crossed_mean = (pos.side == LONG and z >= 0) or (pos.side == SHORT and z <= 0)
        stopped      = pos.adverse_move() > 1.5 * pos.entry_sigma
        expired      = pos.days_held >= 10
        if crossed_mean or stopped or expired:
            close_position(stock)

if realized_vol(index, 20) > 2 * median(realized_vol(index, 20), lookback=252):
    scale_gross_exposure(0.5)
```

## Indicators / data used

Several technical tools are used to identify mean-reverting opportunities:

- **RSI (Relative Strength Index)**: Values below 30 suggest oversold conditions (buy signal); above 70 suggests overbought (sell signal). Short-lookback variants (2–4 period) are more common in systematic reversion. See [[rsi-mean-reversion]] for specific strategy implementations.
- **Bollinger Bands**: When price touches or breaches the lower band, mean reversion traders buy; when it touches the upper band, they sell. See [[bollinger-band-reversion]].
- **Z-score**: Measures how many standard deviations the current price is from its moving average. A z-score beyond +/-2 often signals a reversion opportunity.
- **Moving average distance**: The percentage deviation of price from its 20-day, 50-day, or 200-day moving average.

Data requirement is modest: clean daily OHLCV plus an earnings/event calendar for filtering.

### Identifying mean-reverting assets

Not all assets mean-revert. Statistical tests help determine whether a price series is mean-reverting:

- **Augmented Dickey-Fuller (ADF) test**: Tests for stationarity. A statistically significant result (p-value < 0.05) suggests the series is mean-reverting.
- **Hurst exponent**: Values below 0.5 indicate mean reversion, 0.5 indicates a random walk, and above 0.5 indicates trending behavior.
- **Half-life of reversion** (from an Ornstein-Uhlenbeck fit): tells you the natural holding period; a half-life of 5 days suits swing trading, 50 days does not.

Equities tend to mean-revert on short timeframes (days to weeks) but trend on longer timeframes. Spreads between related assets (see [[pairs-trading]]) are often more reliably mean-reverting than individual prices.

Summary of the three core stationarity / reversion diagnostics:

| Test | What it measures | Mean-reverting signal | Caveat |
|------|------------------|------------------------|--------|
| Augmented Dickey-Fuller (ADF) | Presence of a unit root | p-value < 0.05 (reject unit root) | In-sample only; can break out of sample |
| Hurst exponent (H) | Long-memory / persistence | H < 0.5 | Estimate is noisy on short windows |
| Half-life (Ornstein-Uhlenbeck fit) | Speed of reversion | Short half-life (≈ matches holding period) | Assumes a constant mean; regime shifts invalidate it |

A robust workflow runs all three and trades only series that pass on multiple measures, then re-tests periodically because mean-reversion is **regime-dependent** — the same series can flip from H < 0.5 to H > 0.5 when the [[market-regime]] turns from range-bound to trending (the primary kill mechanism in [[#What kills this strategy]]).

## Example trade

A liquid S&P 500 industrial trades at $100 with a 20-day SMA of $104 and 20-day σ of $2. A large fund's quarter-end rebalance pushes the stock down 4% in two days on no news; z = (100 − 104)/2 = −2.0, 2-period RSI is 6, and price remains above its 200-day SMA. The trader buys, risking 0.5% of equity to a stop at $97 (1.5σ below entry). Over the next four sessions the selling pressure exhausts and the stock drifts back to $103.5 as z crosses zero. Exit at $103.5: +3.5% on the position, roughly +1.2R, holding period 4 days, round-trip cost ~6 bps in a liquid name.

## Performance characteristics

- **Gross edge is small per trade**: typical single-name daily/weekly reversion signals earn 20–80 bps gross per round trip with 55–65% win rates. The edge is harvested through high trade frequency and breadth, not big winners.
- **Cost sensitivity is the defining feature**. Lehmann (1990) and Lo & MacKinlay (1990) showed large *gross* contrarian profits in weekly US equities, but subsequent work (e.g., Avellaneda & Lee 2010 on stat-arb decay) showed net profitability shrank dramatically after the 2000s as spreads compressed and competition grew. At 200–400% annualized turnover per side, every 10 bps of round-trip cost removes roughly 2–4 points of annual return.
- **Realistic net expectation** for a careful daily-bar implementation in liquid equities: Sharpe ~0.5–1.0 (frontmatter assumes 0.7), with a negatively skewed return profile — many small wins, occasional sharp losses when dislocations turn out to be informational.
- **Drawdowns cluster in crises**: reversion books were hit hard in August 2007 (the quant unwind) and March 2020, when "oversold" kept getting more oversold. Expect peak drawdowns around 15–25% of allocated capital (frontmatter assumes 20%).

## Capacity limits

Short-horizon reversion is capacity-constrained because the strategy *is* liquidity provision: the bigger you trade, the more you become the impatient flow you are trying to fade. For a daily-bar single-name equity book holding 10–30 positions for ~5 days each, market impact begins to dominate somewhere in the **$20–100M** range (frontmatter assumes $50M); participation above ~1–2% of a name's average daily volume measurably erodes the per-trade edge. Intraday variants have far less capacity; index-level and futures reversion somewhat more.

## Mean reversion vs momentum

Mean reversion and [[momentum]]/[[trend-following]] are the two great systematic families and are near-opposites — which is precisely why they diversify each other:

| Dimension | Mean reversion | Momentum / trend |
|-----------|----------------|------------------|
| Bets that | Deviations snap back | Trends persist |
| Best regime | Range-bound, choppy | Persistent, directional |
| Hurst exponent of edge | H < 0.5 | H > 0.5 |
| Return skew | **Negative** (small wins, sharp losses) | **Positive** (small losses, big wins) |
| Implicit vol exposure | Short volatility | Long volatility / convexity |
| Worst environment | Trending breakouts, crisis deleveraging | Whippy, mean-reverting chop |
| Holding period | Short (days) | Longer (weeks–months) |

Because the two profiles are mirror images on skew and vol exposure, combining them — sizing each by [[market-regime]] — smooths the equity curve far more than either alone. Detecting which regime is active (e.g., via the rolling Hurst exponent or realized-vol filters) is the practical key to running both.

## What kills this strategy

Mean reversion strategies are vulnerable to **trending markets** where deviations from the mean persist and widen rather than reverting. What appears to be an oversold condition may actually be the beginning of a structural decline. Risk management through stop-losses, position sizing, and regime detection is essential. The principal failure modes (see [[failure-modes]]):

1. **Regime change** — a market shifts from range-bound to trending (e.g., the 2020 COVID crash, the 2022 rate-hiking cycle in bonds) and every fade loses. The Hurst exponent of the traded series drifting above 0.5 is the statistical fingerprint.
2. **Informational dislocations** — fading a move that was actually justified by news (fraud revelation, guidance cut). Event filters reduce but never eliminate this.
3. **Crowding and deleveraging spirals** — when many reversion/stat-arb books hold similar inventory, one fund's forced unwind moves prices *against* everyone else's positions, triggering further unwinds (the August 2007 quant crisis mechanism).
4. **Cost creep** — spread widening, borrow fees on shorts, or slippage growth quietly pushing per-trade cost above the ~15 bps breakeven.
5. **Short-vol blowup** — unhedged reversion is implicitly short volatility; a vol regime shift produces correlated losses across the whole book at once.

## Kill criteria

- Rolling 12-month Sharpe < 0 net of costs.
- Drawdown > 20% of allocated capital.
- Hit rate falls below 50% over the trailing 200 trades (vs. ~55–65% design expectation).
- Median realized round-trip cost exceeds 15 bps for a full quarter.
- Hurst exponent of the traded universe's residual returns > 0.55 for 6 consecutive months (the universe has stopped mean-reverting).

See [[when-to-retire-a-strategy]].

## Advantages

- High trade frequency gives statistical significance quickly — you learn fast whether the edge is real.
- Positive expectancy in flat/choppy markets where trend strategies bleed; natural diversifier to [[momentum]] and [[trend-following]] books.
- Short holding periods limit exposure to overnight/gap and macro risk per position.
- Conceptually simple, cheap data requirements (daily OHLCV), and well-grounded in both behavioral and liquidity-provision economics.

## Disadvantages

- Negatively skewed: steady small gains punctuated by sharp losses when reversion fails; "picking up nickels in front of a steamroller" if unmanaged.
- Extremely sensitive to transaction costs and slippage; an edge that exists on paper often vanishes at retail spreads.
- Implicitly short volatility and crowding-exposed; losses correlate with broader market stress exactly when liquidity is worst.
- Single-name reversion has decayed materially since the 1990s as electronic market-making absorbed the easiest flow.

## Sources

- De Bondt, W. & Thaler, R. (1985). "Does the Stock Market Overreact?" *Journal of Finance*.
- Lehmann, B. (1990). "Fads, Martingales, and Market Efficiency." *Quarterly Journal of Economics*.
- Jegadeesh, N. (1990). "Evidence of Predictable Behavior of Security Returns." *Journal of Finance*.
- Lo, A. & MacKinlay, A.C. (1990). "When Are Contrarian Profits Due to Stock Market Overreaction?" *Review of Financial Studies*.
- Avellaneda, M. & Lee, J-H. (2010). "Statistical Arbitrage in the US Equities Market." *Quantitative Finance*.
- Chan, E. (2013). *Algorithmic Trading: Winning Strategies and Their Rationale* — ADF/Hurst/half-life testing methodology.

## Related

- [[rsi-mean-reversion]]
- [[bollinger-band-reversion]]
- [[pairs-trading]]
- [[momentum]]
- [[statistical-arbitrage]]
- [[bollinger-bands]]
- [[rsi]]
- [[contrarian-extremes]] -- a mean-reversion variant trading sentiment and positioning extremes
- [[trend-following]] -- the opposite systematic family; natural diversifier
- [[market-regime]] -- regime detection determines when reversion vs trend is favored
- [[regime-detection]] -- the Hurst/vol filters that switch the strategy on and off
- [[volatility]] -- reversion is implicitly short vol; vol regime drives drawdowns
- [[ornstein-uhlenbeck]] -- the model behind half-life estimation
- [[cointegration]] -- the basis for spread reversion in [[pairs-trading]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
