---
title: "IV Rank and IV Percentile"
type: concept
created: 2026-04-22
updated: 2026-06-21
status: excellent
tags: [options, indicators, volatility, greeks]
aliases: ["IV Rank", "IVR", "IV Percentile", "IVP", "Implied Volatility Rank"]
domain: [technical-analysis, options]
prerequisites: ["[[implied-volatility]]", "[[vix]]"]
difficulty: intermediate
related:
  - "[[implied-volatility]]"
  - "[[vix]]"
  - "[[iron-condor]]"
  - "[[credit-spread]]"
  - "[[tom-sosnoff]]"
  - "[[tastytrade]]"
  - "[[thinkorswim]]"
  - "[[vega-hedging]]"
  - "[[earnings-options-strategies]]"
---

**IV Rank** and **IV Percentile** are two metrics that measure whether an asset's current [[implied-volatility]] is historically high or low. They are the primary tools options traders use to determine whether to sell premium (when options are expensive) or buy premium (when options are cheap). Both were popularized by [[tom-sosnoff]] and the [[tastytrade]] methodology.

## IV Rank (IVR)

IV Rank measures where the current IV sits relative to its 52-week high and low:

```
IV Rank = (Current IV - 52-Week IV Low) / (52-Week IV High - 52-Week IV Low) x 100
```

**Example**: If a stock's IV has ranged from 20% to 60% over the past year, and current IV is 40%:

```
IV Rank = (40 - 20) / (60 - 20) x 100 = 50%
```

An IV Rank of 50% means current IV is exactly midway between the annual high and low.

### Characteristics of IV Rank

- Ranges from 0% to 100%
- Sensitive to outliers: a single IV spike (e.g., around earnings or a crash) can compress the rank for the rest of the year
- Simple to calculate and interpret
- Displayed on [[thinkorswim]] and [[tastytrade]] platforms by default

### IV Rank Limitation

IV Rank can be misleading when there has been a single extreme spike. If a stock's IV hit 100% once during a crash but normally trades between 20-30%, an IV of 30% would show an IV Rank of only 12.5% -- suggesting IV is "low" even though it is at the top of its normal range.

## IV Percentile (IVP)

IV Percentile measures the percentage of trading days in the past year where IV was **lower** than today's level:

```
IV Percentile = (Number of days IV was lower than current IV) / (Total trading days in period) x 100
```

**Example**: If current IV is 35%, and out of the past 252 trading days, 200 days had IV below 35%:

```
IV Percentile = 200 / 252 x 100 = 79.4%
```

An IV Percentile of 79.4% means that IV was lower than today's level about 80% of the time over the past year.

### Characteristics of IV Percentile

- Ranges from 0% to 100%
- More robust to outliers than IV Rank (a single spike does not distort the reading)
- Better reflects how "normal" or "abnormal" current IV is
- Requires daily IV data for the lookback period

## IV Rank vs IV Percentile

| Aspect | IV Rank | IV Percentile |
|--------|---------|---------------|
| Formula | Range-based (min/max) | Distribution-based (days count) |
| Sensitivity to spikes | High (one extreme day skews it) | Low (treats every day equally) |
| Common reading | Often lower than IVP | Often higher than IVR |
| Platform availability | [[thinkorswim]], [[tastytrade]] | [[tastytrade]], some third-party tools |
| Best for | Quick gauge of range position | Robust historical context |

In practice, [[tastytrade]] has shifted toward emphasizing IV Percentile over IV Rank because of its resistance to outlier distortion. Many traders use both in conjunction.

### Worked example — same data, two very different readings

A stock's 30-day ATM IV over the past year had a low of 18%, a high of 90% (one earnings-crash spike day), and current IV of 36%. Of 252 trading days, IV was below 36% on 205 of them.

```
IV Rank       = (36 - 18) / (90 - 18) × 100 = 25.0%   → "looks cheap"
IV Percentile = 205 / 252 × 100             = 81.3%    → "actually expensive"
```

The single 90% spike inflated the IV Rank denominator, dragging the rank down to 25% even though IV is in fact higher than it was on 81% of days. **The percentile is the honest reading here.** This divergence (low IVR, high IVP) is the classic fingerprint of a one-off spike in the lookback window — exactly the scenario the IV Rank limitation describes. Always reconcile the two before sizing a premium trade.

### Interpreting divergence between the two metrics

| Pattern | Likely cause | Implication |
|---------|--------------|-------------|
| IVR ≈ IVP | Smooth IV distribution, no extreme outliers | Either metric is reliable |
| Low IVR, high IVP | A single historical spike inflated the range max | Trust IVP; IV is genuinely elevated |
| High IVR, low IVP | Recent push toward the top of range, but most days were higher historically | Possibly a fresh spike that may mean-revert; check the catalyst |
| Both > 80% | Genuinely rich vol across both measures | Strong premium-selling context (if no pending event) |
| Both < 20% | Genuinely cheap vol across both measures | Premium-buying / long-gamma context (with a catalyst) |

## Trading Applications

### Sell Premium When IV Is High

When IV Rank > 50% (or IV Percentile > 50%), options are historically expensive. This favors premium-selling strategies:

- **[[iron-condor|Iron condors]]**: Sell OTM call spread + OTM put spread, profit from time decay and IV contraction
- **Short strangles**: Sell OTM call + OTM put, undefined risk but highest theta
- **[[credit-spread|Credit spreads]]**: Directional premium selling with defined risk
- **[[jade-lizard]]**: Short put + short call spread, zero upside risk

The edge: selling expensive options provides a statistical advantage because [[implied-volatility]] tends to overstate realized volatility on average (the [[variance-risk-premium|variance risk premium]]).

### Buy Premium When IV Is Low

When IV Rank < 20% (or IV Percentile < 20%), options are historically cheap. This favors premium-buying strategies:

- **Long straddles/strangles**: Buy both calls and puts, profit if price moves significantly
- **Debit spreads**: Directional bets with limited risk
- **Calendar spreads**: Buy longer-dated (more vega exposure), sell shorter-dated
- **[[butterfly-spread|Butterfly spreads]]**: Low-cost bets on specific price targets

### Earnings Plays

IV Rank is especially relevant around [[earnings-options-strategies|earnings events]]:

- IV typically expands heading into earnings as uncertainty increases
- After the announcement, IV crushes sharply (often 30-60% overnight)
- Selling premium before earnings captures this crush -- but the underlying move must stay within the sold strikes
- IV Rank helps assess whether the pre-earnings IV expansion is above or below historical norms

### Strategy Selection Framework

| IV Rank | IV Percentile | Suggested Approach |
|---------|---------------|-------------------|
| > 50% | > 50% | Sell premium: [[iron-condor|iron condors]], strangles, [[credit-spread|credit spreads]] |
| 20-50% | 20-50% | Neutral zone: smaller positions, or directional debit/credit spreads |
| < 20% | < 20% | Buy premium: straddles, debit spreads, calendars |
| High IVR, low IVP | Divergence | Likely a recent spike; check if mean-reverting or structural |
| Low IVR, high IVP | Divergence | IV has been elevated for a long time; check regime |

## Calculating IV Rank and IV Percentile

### Data Requirements

- Daily closing IV for the underlying asset over the lookback period (typically 252 trading days / 1 year)
- Most platforms use the at-the-money 30-day [[implied-volatility]] as the reference IV
- Some use the [[vix]] methodology (variance swap approach) for index-level IV

### Platform Support

- **[[thinkorswim]]**: Displays IV Rank in the options chain and watchlist columns; available as thinkScript study
- **[[tastytrade]]**: Shows both IV Rank and IV Percentile prominently on the trade page
- **Third-party tools**: Market Chameleon, iVolatility, barchart.com provide IV Rank data
- **Custom calculation**: Straightforward to compute in Python using historical IV data from CBOE or options data providers

### Python Example

```python
import numpy as np

def iv_rank(current_iv, iv_history_252d):
    """IV Rank: position within 52-week range."""
    iv_high = max(iv_history_252d)
    iv_low = min(iv_history_252d)
    if iv_high == iv_low:
        return 50.0
    return (current_iv - iv_low) / (iv_high - iv_low) * 100

def iv_percentile(current_iv, iv_history_252d):
    """IV Percentile: % of days IV was lower than current."""
    days_lower = sum(1 for iv in iv_history_252d if iv < current_iv)
    return days_lower / len(iv_history_252d) * 100
```

## Relationship to VIX

The [[vix]] is often described as the market's "fear gauge," but it is essentially the IV of the S&P 500 index. VIX Rank and VIX Percentile apply the same logic:

- **VIX Rank > 50%**: Broad market options are expensive; favorable for selling SPX/SPY premium
- **VIX Rank < 20%**: Market complacency; options are cheap but a [[volatility]] spike could be imminent

Historical VIX averages around 19-20, but this varies by regime. The long-term median is more useful than the mean because VIX has a right-skewed distribution.

## Relationship to Strategy Selection

IV rank / percentile is the **regime gauge** that sits upstream of most options strategies in this wiki:

| Metric reading | Vol view | Favored posture | Wiki strategy |
|----------------|----------|-----------------|---------------|
| High IVR/IVP, no event | IV likely > future RV | **Sell** vol, delta-hedge | [[delta-hedging]], [[iron-condor]], [[credit-spread]] |
| Low IVR/IVP + catalyst | IV may be < future RV | **Buy** vol, scalp gamma | [[gamma-scalping]], long [[straddle]] |
| Neutral (20-50%) | Ambiguous | Smaller size, directional spreads | debit/credit verticals |

This is also why IVR feeds [[options-buying-power-reduction|BPR]] discipline: high IVR means undefined-risk BPR is already inflated, so vol-shock headroom matters more. And because IV rank summarizes the level (not the structure) of vol, it is complementary to [[implied-correlation]] — a low single-name IVR can coexist with a high implied correlation, meaning index vol is rich relative to its components even when each name looks "cheap."

### Absolute level vs relative rank

IVR/IVP are *relative* measures. A 90% IVR on a name whose IV range is 15-25% still represents little dollar premium; a 30% IVR on a meme stock with a 60-200% range can be richly priced in absolute terms. Always pair the rank with the absolute IV and the dollar premium of the actual structure before trading. This is the most common sizing error among newer premium sellers.

## Common Mistakes

1. **Using IV Rank alone without checking IV Percentile**: A single-day spike can make IV Rank misleading for months
2. **Ignoring absolute IV levels**: An IV Rank of 80% on a stock with 15-25% IV range still means relatively low premium in dollar terms
3. **Not adjusting for events**: IV is legitimately higher before earnings, FDA decisions, and macro events -- selling premium purely because IVR is high ignores the reason for the elevation
4. **Applying equity IVR rules to crypto**: Crypto [[implied-volatility]] regimes are structurally different; lookback periods may need adjustment

## Related

- [[implied-volatility]] -- The underlying measure that IVR and IVP contextualize
- [[vix]] -- IV Rank applied to the S&P 500 options market
- [[iron-condor]] -- Primary strategy deployed when IV Rank is high
- [[credit-spread]] -- Directional premium selling
- [[tom-sosnoff]] -- Popularized IV Rank as a trading filter
- [[tastytrade]] -- Platform and methodology centered on IV Rank-driven trading
- [[thinkorswim]] -- Platform where IV Rank is prominently displayed
- [[vega-hedging]] -- Managing vega exposure based on IV levels
- [[earnings-options-strategies]] -- Using IV Rank to time earnings trades
- [[gamma-scalping]] -- Long-vol strategy screened by low IV rank
- [[delta-hedging]] -- Short-vol strategy screened by high IV rank
- [[variance-risk-premium]] -- Why selling high-IV options has a statistical edge
- [[options-buying-power-reduction]] -- How IV level reprices margin
- [[implied-correlation]] -- The level-vs-structure complement to index IV rank
- [[realized-volatility]] -- What IV is compared against to find an edge
- [[market-regime]] -- IV rank as a coarse vol-regime classifier

## Sources

- tastytrade research archive — origin and popularization of IV Rank and IV Percentile as premium-selling filters
- CBOE — VIX methodology white paper (variance-swap construction of index implied volatility)
- iVolatility / Market Chameleon — third-party IV rank and percentile data
- Sheldon Natenberg, *Option Volatility and Pricing* — implied vs. realized volatility and the variance risk premium
