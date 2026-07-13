---
title: "Gold-Silver Ratio Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, commodities, gold, mean-reversion, pairs-trading, history]
aliases: ["Bimetallic Arbitrage", "Gold-Silver Ratio Trade", "GSR Trade"]
strategy_type: fundamental
timeframe: position
markets: [commodities, futures]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [behavioral, structural]
edge_mechanism: "The gold-silver price ratio exhibits long-cycle mean reversion around an industrial-plus-monetary anchor; extremes at 80:1 or below 40:1 have historically reverted, with the other side of the trade being momentum traders who assume the latest trend will continue."
data_required: [ohlcv-daily, futures-curves, cot-reports, etf-premiums]
min_capital_usd: 25000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.35
breakeven_cost_bps: 20
decay_evidence: "Ratio has trended higher over decades as silver lost monetary role; absolute levels for 'extreme' keep rising. 2020 ratio of 125+ was unthinkable in the 1980s."
related: ["[[arbitrage]]", "[[commodities]]", "[[gold]]", "[[silver]]", "[[pairs-trading]]", "[[mean-reversion]]", "[[hunt-brothers-silver-corner]]", "[[edge-taxonomy]]", "[[etf-arbitrage]]", "[[limits-to-arbitrage]]", "[[behavioral-finance]]"]
---

# Gold-Silver Ratio Arbitrage

The **gold-silver ratio (GSR)** is the number of ounces of silver that one ounce of gold will buy. For most of recorded history, from Roman times until the late 19th century, governments fixed the ratio at roughly **15:1** under bimetallic monetary systems. Since silver was demonetized and gold went to a floating fiat era, the ratio has ranged widely -- from a low of **17:1** in January 1980 at the peak of the Hunt Brothers silver corner, to highs above **125:1** during the March 2020 COVID liquidation. Traders exploit this range by going long whichever metal is relatively cheap and short the other when the ratio hits historical extremes.

This is fundamentally a [[mean-reversion]] [[pairs-trading|pair trade]] on two correlated commodities ([[gold]] vs [[silver]]), with the added complication that the long-run mean itself drifts. Modern GSR strategies use rolling 5- or 10-year percentile bands rather than a fixed mean, and often express the trade via futures ([[gold]] GC and silver SI on COMEX), ETFs (GLD vs SLV), or physical trusts (Sprott PHYS vs PSLV). The ratio has also been repeatedly distorted by physical-market dislocations -- most famously when Sprott Physical Silver Trust (PSLV) briefly traded at a roughly 10% premium to NAV during the early-2021 "silver squeeze" Reddit campaign.

### The ratio through history (context anchors, not entry signals)

The single most important fact for sizing this trade is that "extreme" is a moving target. The table below is a chronology of notable GSR levels — it is historical context, not a backtest of returns:

| Period | GSR level | Driver | Lesson for the strategy |
|---|---|---|---|
| Roman era – late 1800s | ~12:1 to 15:1 | Fixed by bimetallic statute | The "natural ratio" myth that still anchors retail today |
| Jan 1980 (Hunt peak) | ~17:1 | Hunt Brothers silver corner; silver ~$50 | A short-silver trade at the low was a generational winner |
| Mid-1991 | ~100:1 | Silver demonetization fully priced | "Extreme high" kept rising decade over decade |
| 2011 (silver spike) | ~32:1 | QE-era silver mania, silver ~$49 | Even modern lows can be violent and brief |
| Mar 2020 (COVID) | ~125:1 | Risk-off + industrial-demand collapse for silver | New record high; old "80 is extreme" rule was stale |
| 2021 (#SilverSqueeze) | ~65-70:1 | Reddit retail buying; PSLV premium ~10% | Physical/paper basis can dislocate the trade |

The secular drift (silver losing its monetary role) means a static threshold like "15:1 is fair" would have produced 40+ years of continuous losses — the core reason the rules below use *rolling percentile bands*, not a fixed mean.

## Edge Source

**Behavioral** and **structural**. Behavioral: trend-following and momentum traders push the ratio to extremes as one metal outperforms the other, creating oversold/overbought readings that mean-revert. Structural: silver has a larger industrial demand component (~50% of supply) versus gold (~10%), so GSR compression tends to coincide with global growth upturns while expansion reflects flight-to-safety. See [[edge-taxonomy]].

## Why This Edge Exists

When gold rallies in a risk-off move while silver lags (industrial demand falls), momentum traders chase gold, pushing GSR to extremes. The counterparty is a slower, reversion-oriented trader willing to wait quarters or years for normalization. Retail precious-metals enthusiasts -- "silver stackers" and "goldbugs" -- often anchor to historical bimetallic ratios (15:1) that no longer reflect industrial reality, but their collective buying at GSR extremes does put a floor under silver. See [[behavioral-finance]].

## Null Hypothesis

Under random-walk conditions, the log ratio should be indistinguishable from Brownian motion, with no predictive power from the current level. Empirical evidence since 1970 shows **modest** mean reversion at multi-year horizons, but at monthly horizons the ratio can continue to trend. The null outcome is: you buy the ratio at 100, it goes to 120, you get stopped out before it reverts to 65.

## Rules

### Entry

1. **Compute rolling-window GSR percentile** (e.g., 10-year rolling). Define extremes as >95th percentile (silver cheap relative to gold) or <5th percentile (gold cheap).
2. **Confirm with absolute levels**: historically, >80:1 was extreme; post-2019, >100:1 is the new extreme. Use both.
3. **Signal long silver / short gold**: GSR in the top 5% of 10-year rolling window AND gold/silver futures curve not in extreme backwardation (which can signal supply crisis, not behavioral overshoot).
4. **Signal long gold / short silver**: GSR below 5th percentile AND silver speculative long positioning (COT report) near record highs.
5. **Dollar-neutral or volatility-parity sizing**: equal dollar notional on each side, OR size so each leg has the same realized-volatility contribution. Silver is ~1.5x as volatile as gold, so vol-parity sizing leaves a larger gold position.

### Exit

1. **Mean reversion target**: close the trade when GSR returns to 50th percentile of the rolling window.
2. **Time stop**: 24-month maximum holding period; if not mean-reverted, re-evaluate thesis.
3. **Stop-loss**: exit if GSR moves another full standard deviation further from the mean (e.g., from 100 to 120).

### Position Sizing

Risk 1-3% of capital per full-sized trade. Because the trade has historically had drawdowns to 50% of max ratio extension before reverting, do not size larger than 10% of capital notional per side.

## Implementation Pseudocode

```python
def gsr_signal(gold_price, silver_price, lookback_years=10):
    gsr_series = gold_history / silver_history
    current_gsr = gold_price / silver_price
    pct = percentile_rank(current_gsr, gsr_series[-lookback_years*252:])

    if pct > 0.95 and not silver_supply_crisis():
        # silver is historically cheap
        return {"long": "silver_futures", "short": "gold_futures",
                "silver_notional": vol_parity_size(silver_vol, gold_vol)}
    elif pct < 0.05 and not gold_speculative_short_squeeze():
        # gold is historically cheap
        return {"long": "gold_futures", "short": "silver_futures"}
    else:
        return None

def exit_condition(entry_gsr, current_gsr, days_held):
    target_gsr = rolling_median_gsr()
    if sign(current_gsr - target_gsr) != sign(entry_gsr - target_gsr):
        return "reversion_hit"
    if days_held > 504:  # 2 years
        return "time_stop"
    if abs(current_gsr - target_gsr) > 2 * std_gsr:
        return "stop_loss"
```

## Indicators / Data Used

- **Daily gold and silver spot and futures prices** (COMEX GC, SI)
- **Rolling percentile rank** of GSR over 5- and 10-year windows
- **COT (Commitments of Traders) reports** for speculator positioning extremes
- [[etf-arbitrage]] / premium data for GLD, SLV, PHYS, PSLV (physical-trust premiums signal supply stress)
- **Industrial silver demand** proxies (solar-panel shipments, electronics)
- **Gold-to-mining-equity ratio** as a secondary confirmation

## Example Trade

**March 2020 GSR Extreme.** On 18 March 2020, during the COVID liquidation, gold held near $1,480/oz while silver collapsed to $12.00/oz -- a GSR of **123:1**, the highest recorded since futures data began. This was in the 99.5th percentile of the 10-year rolling window.

- Entry (18 Mar 2020): long 5 SI contracts (25,000 oz silver at $12.00 = $300,000 notional), short 3 GC contracts (300 oz gold at $1,480 = $444,000 notional) -- approximately vol-parity.
- By August 2020, silver rallied to $29 while gold hit $2,075 -- GSR compressed to **71:1**.
- Silver P&L: ($29 - $12) * 25,000 = **+$425,000**.
- Gold P&L: ($1,480 - $2,075) * 300 = **-$178,500**.
- Net: **+$246,500** on combined margin of roughly $80,000 -- a multi-hundred-percent return in five months.
- By 2021-2022 the ratio oscillated 70-90, and the trade would have been closed at the 50th percentile target.

Compare to the **1980 Hunt Brothers** episode, where Nelson and William Hunt accumulated 150 million ounces of silver, driving the ratio to 17:1 on 17 Jan 1980 at silver's $50 peak. A trader long gold / short silver at 17:1 would have earned enormous returns as the ratio widened back to 50:1 by mid-1981 after COMEX's "Silver Rule 7" (the January 1980 liquidation-only rule) and margin hikes forced the Hunt liquidation.

## Performance Characteristics

- **Hit rate**: 60-70% of trades entered at historical extremes revert within 24 months.
- **Average holding period**: 6-14 months; outliers take 2-3 years.
- **Sharpe**: 0.3-0.6 net of futures roll costs, which are non-trivial (both contracts are often in contango).
- **Max drawdown**: 30-50% of capital deployed during adverse ratio extension (e.g., 2019-2020 GSR went from 80 to 125 before reverting).
- **Best conditions**: regime changes between risk-on and risk-off, commodity super-cycles, post-crisis normalization.
- **Worst conditions**: sustained one-way monetary easing that favors gold over silver; industrial demand collapse; short silver squeezes (2021 Reddit campaign).

### Cost and friction overlay

Unlike a true risk-free arb, this is a *statistical* convergence trade — the "edge" is a mean-reversion tendency, not an identity — so it must clear real carrying costs over a multi-quarter hold. The frictions are why `breakeven_cost_bps` is set relatively high (20) and why over-trading destroys the strategy:

| Friction | Magnitude / nature | Mitigation |
|---|---|---|
| Futures roll (contango) | Recurring drag each contract roll, both legs | Use longer-dated contracts; net roll between the two legs |
| Financing / margin on two legs | Two-sided futures margin tied up for 6-24 months | Vol-parity sizing to minimize notional |
| Borrow on short leg (if ETF expression) | SLV/GLD borrow can be non-trivial | Prefer futures or inverse-ETF expression |
| Physical/paper basis (PSLV/PHYS premium) | Up to ~10% dislocation (2021) | Trade paper-vs-paper; avoid mixing physical and futures legs |
| Adverse excursion before reversion | 30-50% drawdown of deployed capital observed | Size small per side; long time horizon |

The trade only makes sense for patient capital: the holding period is measured in quarters to years, so any per-trade friction is amortized — but a trader who churns in and out at the first wiggle pays the roll and slippage repeatedly and bleeds the edge away. See [[limits-to-arbitrage]] for why a "known" mean-reverting spread can still hurt patient arbitrageurs.

## Capacity Limits

GSR arb is highly scalable. COMEX silver open interest is roughly $25 billion notional; gold futures are ~$200 billion. A $500 million position in the spread is less than 1% of gold OI and perhaps 2% of silver OI, easily absorbed. Capacity is ultimately limited by physical-metal delivery mechanics -- if scaled to multiple billions, delivery disputes (as in March 2021 COMEX silver delivery concerns) become a real risk.

## What Kills This Strategy

1. **Silver monetary comeback** or industrial demand shift that permanently re-rates the ratio. A strategy anchored to "15:1 is the natural ratio" would have lost money continuously for 40 years. See [[failure-modes]].
2. **Short squeezes** like the January 2021 #SilverSqueeze Reddit campaign, which drove PSLV premium to 10%+ and caused dislocations for traders short physical silver.
3. **Exchange / regulatory intervention** -- COMEX's Silver Rule 7 (liquidation-only orders, January 1980) forcibly unwound the Hunt corner, and similar position-limit or margin changes can whipsaw the spread.
4. **Structural ratio drift**: the 10-year rolling percentile approach partially addresses this but does not fully solve it if the world is in a permanent re-rating regime.
5. **Correlation breakdown**: gold and silver correlation drops to ~0.4-0.6 during crises, making the pair trade less "neutral" than it appears.

## Kill Criteria

- Three consecutive losing trades with losses > 2x expected per-trade profit
- 10-year rolling GSR mean moves by >50 (signaling structural re-rating)
- Maximum drawdown > 40% of allocated capital
- Rolling 3-year Sharpe < 0

## Advantages

- Long history (50+ years of modern data, centuries of context) supporting mean reversion at extremes
- Dollar-and-vol-neutral construction removes most directional commodity risk
- Large, liquid futures markets on both legs with tight spreads
- Naturally hedged against most macro shocks that affect both metals similarly
- Accessible via ETFs for smaller accounts (GLD/SLV pairs trade)

## Disadvantages

- Long holding periods and large adverse excursions require patience and deep pockets
- Structural drift in the ratio invalidates static-threshold rules
- Futures roll costs can accumulate meaningfully over 12+ month holding periods
- Silver is dramatically more volatile than gold; vol-parity sizing tilts the trade heavily toward gold
- Can be crowded: when the same signal appears on every commodity trader's screen, the reversion can be delayed
- Physical-market dislocations (2021 Sprott PSLV premium, COMEX delivery issues) create basis risk between paper and physical

## Sources

- Fay, S., *Beyond Greed: The Hunt Family's Bold Attempt to Corner the Silver Market* (1982) — definitive account of the 1980 episode.
- CFTC Commitments of Traders (COT) reports — positioning data.
- LBMA gold and silver price history — long-run GSR series.
- Sprott Physical Trust (PHYS/PSLV) NAV and premium disclosures.
- CME Group COMEX GC/SI contract specifications and open-interest data.

## Related

- [[arbitrage]] -- parent concept
- [[pairs-trading]] -- structurally identical construction
- [[mean-reversion]] -- underlying principle
- [[gold]], [[silver]] -- underlyings
- [[commodities]] -- market context
- [[hunt-brothers-silver-corner]] -- historical extreme
- [[etf-arbitrage]] -- related vehicles (GLD/SLV, PHYS/PSLV)
- [[limits-to-arbitrage]] -- why a known mean-reverting spread can still hurt
- [[edge-taxonomy]], [[failure-modes]] -- methodology
- [[behavioral-finance]] -- mechanism
