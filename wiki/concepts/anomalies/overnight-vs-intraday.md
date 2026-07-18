---
title: "Overnight vs. Intraday Return Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [market-microstructure, quantitative, liquidity]
aliases: ["Overnight vs Intraday", "Overnight Drift", "Night-Day Anomaly", "Overnight Return Premium"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[market-microstructure]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[market-microstructure]]", "[[edge-taxonomy]]"]
---

# Overnight vs. Intraday Return Anomaly

Almost all of the long-run positive return on US equities has been earned *overnight* — from the previous day's close to the next day's open — while returns during the regular trading session have been approximately zero or slightly negative on average. The effect has widened in recent decades and is now one of the largest and most robust return decompositions in the literature.

## What

Decompose each day's close-to-close return into two parts:

```
close-to-close = (close_{t-1} → open_t)   [overnight]
               + (open_t → close_t)       [intraday]
```

In US large caps from 1993 to present, the cumulative overnight component has earned roughly the entire equity risk premium (~8% annualized), while the cumulative intraday component has earned near zero (some samples show it slightly negative). A strategy that buys SPY at the close and sells at the next open has outperformed a strategy that buys at the open and sells at the close by a factor of roughly 5x.

## Original Papers

- Cliff, Cooper, Gulen (2008) "Return Differences Between Trading and Non-Trading Hours: Like Night and Day" — SSRN working paper, widely cited
- Lou, Polk, Skouras (2019) "A Tug of War: Overnight Versus Intraday Expected Returns" — *Journal of Financial Economics*
- Bogousslavsky (2021) extends the effect into international markets and factor returns

## Mechanism

No single agreed-upon explanation. Leading theories:

- **Risk premium for overnight illiquidity** — holding equities when markets are closed and cannot be hedged is risky, so investors demand compensation in the form of higher expected overnight returns
- **Positive news flow during non-trading hours** — earnings releases, international news, and Fed communications are disproportionately released outside trading hours and are biased positive
- **Retail vs. institutional trading clientele** — institutions dominate opening and closing auctions and drive the price lower during the day; retail and momentum flows push prices up overnight
- **Short-covering and dealer inventory unwinding** at the open produces upward pressure that then fades during the day
- **Factor clientele** — Lou, Polk, Skouras find that different factors (momentum, size, value) have systematically different overnight vs. intraday patterns, suggesting distinct investor clienteles trade at different times

## Edge Category

**Structural** (liquidity premium + clientele segmentation — distinct investor groups trade at different times, and someone must hold risk overnight) + **risk-bearing** (the overnight return compensates for holding positions through the illiquid after-hours period when adverse news can arrive). See [[edge-taxonomy]].

## Replication Status

Strongly replicated, and the magnitude has *increased* in post-2000 data rather than decaying. One of the anomalies that has held up best despite wide awareness.

## Decay History

None or slight *strengthening*. Unlike most anomalies, publicizing this one has not compressed it — possibly because the mechanism is structural (you cannot trade continuously; someone has to hold risk overnight) rather than behavioral.

## Current Viability

Directly tradeable via overnight-only equity strategies. A long-only close-to-open strategy has outperformed buy-and-hold by a wide margin historically, though costs (transaction fees, bid-ask spread, and losing dividend accrual) must be carefully managed. Several ETFs explicitly implement overnight strategies.

**Caveats:**
- Overnight gaps can be large when realized, so drawdowns are lumpy
- Tail risk is concentrated overnight (overnight crashes, geopolitical events), which may be the premium you are being paid

## Related Strategies

- [[calendar-effects-anomalies]] — broader family
- [[time-series-momentum]] — overnight-only variants exist
- Overnight-only SPY-style ETFs (e.g., NSPY concept products)

## Sources

- Cliff, Cooper, Gulen (2008) — original
- Lou, Polk, Skouras (2019) — JFE paper, factor-level decomposition
- Bogousslavsky (2021) — international replication
- Kelly, Clark (2011) — overnight premium and news flow

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[market-microstructure]]
