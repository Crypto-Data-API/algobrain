---
title: "FX Skewness Risk Premia"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [forex, quantitative, tail-risk, statistics, crypto, altcoins]
aliases: ["Risk Premia in Forex Markets", "Skewness Risk Premium", "Negative Skew Premium"]
strategy_type: quantitative
timeframe: swing
markets: [forex, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing]
edge_mechanism: "Investors dislike negatively skewed assets (small steady gains, rare crashes) and demand extra return to hold them; buying negative-skew and selling positive-skew assets collects that premium in exchange for crash exposure."
data_required: [ohlcv-daily]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.2
expected_max_drawdown: 0.3
breakeven_cost_bps: 20
decay_evidence: "QuantConnect's four-pair FX port reported about -0.33% per year over a decade; the underlying Lemperiere et al. result relies on broader cross-asset universes."
kill_criteria: |
  - rolling 24-month net Sharpe < 0
  - a single crash week costs more than 12 months of accumulated premium
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[skewness]]", "[[carry-trade]]", "[[max-anomaly]]", "[[crash-fear-premium]]", "[[volatility-risk-premium]]"]
---

# FX Skewness Risk Premia

**FX skewness risk premia** goes long currency pairs whose recent returns are strongly negatively skewed and short pairs with strongly positive skew. The premise, from Lemperiere et al. ("Risk Premia: Asymmetric Tail Risks and Excess Returns"), is that many risk premia are really compensation for negative [[skewness]] — the carry trade is the canonical example. [[quantconnect|QuantConnect]]'s Strategy Library implements it on four FX majors; this page also sketches the cross-sectional crypto analog (Source: [[quantconnect-strategy-library]]).

## Edge Source

**Risk-bearing** per [[edge-taxonomy]]: the trader is paid to hold crash risk others avoid.

## Why This Edge Exists

Negative skew means frequent small gains and rare large losses. Leveraged investors with drawdown limits cannot hold those exposures through a crash, so they demand a premium. [[carry-trade|Carry]] currencies (AUD, emerging-market FX) and short-volatility positions ([[volatility-risk-premium]]) are negatively skewed and have historically paid for it. The seller of skew — the side the strategy takes the other end of — is the investor buying crash protection or lottery-like upside. In crypto the mirror image is well documented: coins with lottery-like positive skew are overpriced and subsequently underperform ([[max-anomaly]]), so being short positive skew is the more reliable leg there.

## Null Hypothesis

If skewness carries no premium, returns of the long-negative-skew/short-positive-skew book average zero after costs, and the strategy's P&L is uncorrelated with its skew exposure. Testable: sort assets into skew quintiles and check whether next-period returns are monotone in skew.

## Rules

### Source rules (FX)
1. Universe: EURUSD, AUDUSD, USDCAD, USDJPY.
2. Compute the skewness of each pair's daily returns over a trailing window.
3. **Long** pairs with skewness < -0.6; **short** pairs with skewness > 0.6.
4. Equal-weight the selected positions; rebalance weekly.

### Crypto adaptation (not from the source)
1. Universe: the top 30-50 liquid perps as of each date (point-in-time).
2. Rank by 60-90-day daily-return skewness.
3. Short the top quintile (most positive skew, lottery-like), optionally long the bottom quintile; BTC-beta-neutralize the book.
4. Rebalance weekly; volatility-weight positions.

## Implementation Pseudocode

```python
LOOKBACK, THRESH = 90, 0.6
def weekly_rebalance(returns):                 # returns: DataFrame[date x asset]
    skew = returns.iloc[-LOOKBACK:].skew()
    longs  = skew[skew < -THRESH].index
    shorts = skew[skew >  THRESH].index
    n = len(longs) + len(shorts)
    w = {a: 1/n for a in longs} | {a: -1/n for a in shorts} if n else {}
    return w                                    # execute next bar; subtract fees + funding
```

## Indicators / Data Used

- Sample [[skewness]] of daily returns over a trailing window
- FX: interest-rate differentials to separate skew from [[carry-trade|carry]]
- Crypto: perp [[funding-rate]], which is often correlated with skew (crowded longs)

## Example Trade

Illustrative (FX): over the trailing window, AUDUSD skew is -0.9 (grinding up, sharp risk-off drops) and USDJPY skew is +0.8. The strategy is long AUDUSD and short USDJPY, 50/50, for one week. A quiet risk-on week earns the carry-like drift; a risk-off shock loses on both legs at once — the risk the premium pays for.

## Performance Characteristics

- **Source claim** (QuantConnect, four FX pairs, ~10 years, pre-cost): about -0.33% annual return. The authors blame the tiny universe, untuned thresholds and a short history relative to weekly rebalancing, and invite refinements (Source: [[quantconnect-strategy-library]]).
- The FX version ran on LEAN's zero-fee Forex default; add ~1-2 pips per side.
- With only four instruments, most weeks have zero or one position; the sample is too small to measure a premium.

## Capacity Limits

FX majors: effectively unlimited at weekly frequency. Crypto cross-section: limited by the short leg in small-cap perps with positive skew (often thin and expensive to short when funding is negative).

## What Kills This Strategy

- Crash clustering: all negative-skew longs fall together in a risk-off event ([[tail-risk-hedging]]).
- Skew estimates are noisy — a single outlier day flips the sign ([[overfitting]]).
- Crypto: short-squeezes in positive-skew coins; see [[failure-modes]].

## Kill Criteria

Retire per [[when-to-retire-a-strategy]] on the frontmatter conditions.

## Advantages

- Grounded in a broad theory of risk premia.
- Crypto short-lottery leg has independent anomaly support ([[max-anomaly]]).
- Simple ranking signal.

## Disadvantages

- Negative published result on the FX port.
- Designed to lose in crashes.
- Sample skewness needs long windows to be stable.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=120` — daily returns per coin for skewness
- `GET /api/v1/derivatives/funding-rates` — funding cost for the short leg

**Historical data:**
- `GET /api/v1/backtesting/klines` — daily OHLCV archive for the skew ranking
- `GET /api/v1/backtesting/funding` — historical funding to cost positions

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=SOLUSDT&interval=1d&limit=1000"
```

CryptoDataAPI does not serve FX; the crypto adaptation is the testable version. Full catalogs: [[cryptodataapi-backtesting]], [[cryptodataapi-derivatives]].

### AI agent workflow

Using the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Signal** — weekly, pull 120 daily klines per universe coin and rank by 90-day skew
- **Regime gate** — cut the long-negative-skew leg when `GET /api/v1/volatility/regime` shows a vol shock; that is when the premium is paid out as losses
- **Backtest** — build the universe from `/backtesting/symbols` and `/backtesting/daily-snapshots/{date}` so delisted lottery coins stay in the short leg's history
- **Execution** — avoid shorting positive-skew coins whose `/derivatives/funding-rates` is deeply negative; the short pays the crowd's squeeze

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "Risk Premia in Forex Markets", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[skewness]] · [[commodity-skewness-strategy]] · [[carry-trade]] · [[volatility-risk-premium]] · [[crash-fear-premium]] · [[max-anomaly]]
