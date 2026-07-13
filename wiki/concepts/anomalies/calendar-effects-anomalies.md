---
title: "Calendar Effects"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [anomalies, calendar-effects, seasonality, behavioral-finance]
aliases: ["Calendar Effects", "Seasonal Anomalies", "Day-of-Week Effects", "Holiday Effects"]
domain: [anomalies]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[calendar-effects]]", "[[behavioral-finance]]", "[[seasonal-spread-trading]]", "[[expiration-and-rebalancing-flows]]", "[[momentum-factor]]"]
---

# Calendar Effects

A family of empirical regularities in which equity returns vary systematically by calendar position — day of the week, week of the month, month of the year, holidays, and so on. The most-studied class of "weak" anomalies in finance: they are real, replicated, and persistent, but the magnitude is small enough that capturing them after costs is difficult. Worth knowing about both as historical curiosities and as features that can be combined with other strategies for marginal improvements. See [[anomalies-overview]] for the broader catalogue and [[behavioral-finance]] for the mechanisms.

## At a Glance

| Effect | Pattern (direction) | Seminal study | Decay / status | Tradeable alone? |
|---|---|---|---|---|
| January effect | Small-caps outperform in January | Keim (1983) | Largely gone in US large-cap; weak abroad | No |
| Weekend / Monday | Monday returns negative | French (1980) | Faded; inconsistent post-1990s | No |
| Holiday effect | Pre-holiday day abnormally positive | Ariel (1990) | Reduced but detectable | Marginal |
| Turn-of-the-month | Returns cluster month-end → early-month | Ariel (1987) | Persistent (flow-driven) | Marginally |
| Sell-in-May / Halloween | Nov–Apr > May–Oct | Bouman & Jacobsen (2002) | Surprisingly robust, OOS + cross-country | As a tilt |
| Pre-FOMC drift | Abnormal returns before FOMC | Lucca & Moench (2015) | Held up post-publication | As an overlay |
| Overnight vs. intraday | Overnight returns ≫ intraday | Cliff, Cooper, Gulen (2008) | Robust, increasing | As a tilt |
| Closing-auction effect | Volume/price discovery at the close | (microstructure) | Mechanical, persistent | Microstructure only |

## The Major Calendar Effects

### 1. The January Effect

**Source:** Keim (1983) "Size-Related Anomalies and Stock Return Seasonality" — *Journal of Financial Economics*

**The pattern:** Small-cap stocks earn substantially higher returns in January than in other months. Roughly half of the entire small-cap "size premium" historically came from January alone.

**Mechanism:**
- *Tax-loss selling* in December — investors sell losers to harvest tax losses, depressing prices
- *January reinvestment* — those investors buy back in January, lifting prices
- *Window dressing* by institutional investors

**Decay:** The effect was strongest in 1925-1980. After publication and broader awareness, it compressed substantially. The January effect in US large caps is now indistinguishable from zero. It persists weakly in some international markets.

### 2. The Weekend / Monday Effect

**Source:** French (1980) "Stock Returns and the Weekend Effect" — *Journal of Financial Economics*

**The pattern:** Monday returns are negative on average, while other weekdays have positive returns. Originally documented for the S&P 500.

**Mechanism:** Unclear. Theories include:
- Investors process bad news over the weekend and sell on Monday
- Settlement timing differences between Friday and Monday
- Short-sellers establishing positions on Friday for weekend protection

**Decay:** The Monday effect has weakened substantially since the 1980s. In recent decades it is sometimes positive, sometimes negative, with no consistent pattern. It's largely considered a historical curiosity.

### 3. The Holiday Effect

**Source:** Ariel (1990) "High Stock Returns Before Holidays" — *Journal of Finance*

**The pattern:** The trading day before a market holiday has substantially higher returns than other days. Approximately 5x higher than average daily returns historically.

**Mechanism:** Bullish positioning before extended market closures (don't want to be short over a holiday); short covering by traders who don't want gap risk during a closed market.

**Decay:** Reduced but still detectable in modern data. The effect is small per trade but compounds over many holidays per year.

### 4. The Turn-of-the-Month Effect

**Source:** Ariel (1987) "A Monthly Effect in Stock Returns" — *Journal of Financial Economics*

**The pattern:** The last few trading days of the month and the first few of the next month account for a disproportionate share of total monthly returns. Approximately the entire monthly return concentrates in this 4-5 day window.

**Mechanism:** 
- Pension fund inflows arriving at month-end
- 401(k) contributions invested at month-end
- Window dressing at quarter-end and year-end
- Index rebalancing flows

**Decay:** This effect has held up better than most calendar effects, possibly because the underlying flow mechanism (mandatory monthly contributions) hasn't gone away. It is still tradeable as a small positive bias.

### 5. The "Sell in May and Go Away" Effect (Halloween Indicator)

**Source:** Bouman & Jacobsen (2002) "The Halloween Indicator, 'Sell in May and Go Away'" — *American Economic Review*

**The pattern:** Stock returns from November through April are systematically higher than May through October across many countries.

**Mechanism:** Unclear. Theories include:
- Vacation effects (lower trading volume in summer)
- Seasonal-affective-disorder explanations (Kamstra, Kramer, Levi)
- Coincidence with the historical clustering of crashes (October bias)

**Decay:** Surprisingly persistent. The pattern has held up across decades and across countries, including out-of-sample after the original publication. It's one of the more robust calendar effects.

### 6. The FOMC Drift

**Source:** Lucca & Moench (2015) "The Pre-FOMC Announcement Drift" — *Journal of Finance*

**The pattern:** US equity returns are abnormally high in the 24 hours preceding FOMC announcements. Approximately 80% of the cumulative S&P 500 return since 1994 has occurred in those windows.

**Mechanism:** Unclear. Theories:
- Pre-positioning by informed investors who anticipate dovish surprises
- Risk premium for being long over the announcement
- Leakage of policy decisions

**Decay:** The effect has held up since publication, somewhat to researchers' surprise. The Fed has investigated potential leaks and found nothing definitive.

### 7. The Overnight vs. Intraday Effect

**Source:** Cliff, Cooper, Gulen (2008) and others

**The pattern:** Most of the long-run equity return comes from *overnight* sessions (close to next open), not from intraday trading hours. Intraday returns are slightly negative on average; overnight returns are strongly positive.

**Mechanism:** 
- Higher risk during illiquid overnight session demands premium
- Pre-market positioning by institutional investors
- After-hours news flow positively biased

**Persistence:** Robust and increasing in magnitude in recent years. A long-only strategy that holds equities only overnight outperforms a long-only strategy that holds them only intraday, by a wide margin.

### 8. End-of-Day / Closing Auction Effect

**The pattern:** A disproportionate share of daily volume and price discovery happens in the closing auction (last 5-10 minutes). Index funds and ETFs concentrate trading at the close, producing predictable flow patterns.

**Mechanism:** Mechanical — index fund execution at the official close to track the benchmark exactly.

**Use case:** [[expiration-and-rebalancing-flows]] strategies, intraday market-making.

## Why Most Calendar Effects Are Hard to Trade

The calendar effects are *real* — they show up consistently in academic studies — but they are also *small*. Most have effect sizes in the 5-50 basis points per occurrence range. After transaction costs:

- **Friction kills the simple version** — paying spread + commission per holiday is more than the holiday excess return
- **Capacity is limited** — every other quant knows about these and the predictable flow opportunities are small
- **Statistical noise dominates** — the per-occurrence effect is small relative to daily volatility, so meaningful sample sizes require decades

Where calendar effects *are* useful: as features in a multi-factor model. A [[momentum-factor|momentum]] strategy that's slightly long-biased in late October and slightly short-biased in mid-September captures the Halloween + September seasonality without needing to trade specifically for it.

### Why effects decay (and which survive)

| Decay driver | Effects most affected | Effects that resist |
|---|---|---|
| **Publication / arbitrage** — once documented, quants front-run it | January, Monday | Flow-mechanical ones (turn-of-month) |
| **Structural change** — the cause itself disappears | Monday (settlement-cycle changes) | — |
| **Persistent mechanical flows** — the cause is mandated and ongoing | — | Turn-of-month (pension/401k inflows), closing auction (index tracking) |
| **Hard-to-arbitrage risk** — capturing it requires holding overnight/event risk | — | Overnight effect, pre-FOMC drift |

The throughline: calendar effects rooted in **mandated, recurring flows** (turn-of-month contributions, closing-auction index execution) or in **risk premia** (overnight, pre-FOMC) persist; effects rooted purely in mispricing (January, Monday) erode once arbitraged.

## A Practical Example

Combine three effects:
1. Hold equities overnight, flat intraday (overnight effect)
2. Slight overweight in November-April (Halloween)
3. Slight overweight at month-end (turn-of-month)

A long-only equity portfolio implementing all three has historically outperformed buy-and-hold by 100-200 bps per year with similar volatility. None of the individual effects is large enough to be a strategy on its own; combined, they provide a meaningful improvement over passive.

## Calendar Effects in Crypto

Crypto markets have their own emerging calendar patterns:

- **Weekend effects** — different from equities because crypto trades 24/7. Weekends often see lower volumes and smaller moves; some research suggests positive weekend bias.
- **Asia-session effects** — early Asia hours (especially Sunday/Monday in Asia) often see large moves
- **Funding-rate-cycle effects** — perpetual futures funding rates settle on 8-hour cycles, producing predictable buying/selling pressure
- **Ethereum gas-price cycles** — diurnal patterns in gas prices and DeFi activity

These are less well-documented than equity calendar effects but follow similar logic. See [[seasonal-spread-trading]] for the commodity-futures analogue, where recurring seasonal supply/demand creates calendar-spread structure.

## Common Pitfalls

| Pitfall | Why it bites | Mitigation |
|---|---|---|
| Trading a single effect for its own sake | Per-occurrence edge (5-50 bps) is below round-trip cost | Stack effects as tilts inside an existing book |
| Data-mining the calendar | With enough slices, spurious "effects" appear | Demand OOS + cross-market replication (the Halloween test) |
| Ignoring decay | Published effects (January, Monday) are largely gone | Weight toward flow-/risk-driven effects that persist |
| Confusing seasonality with alpha | "Alpha" that vanishes after calendar controls was never alpha | Control for calendar effects when validating a backtest |
| Overnight tilt ignores execution | Capturing the overnight effect needs open/close execution discipline | Use closing-auction execution; account for gap risk |

## Why This Page Is Worth Reading

Even if you don't trade calendar effects directly, knowing them is useful for:

1. **Understanding why your strategy might be doing well or poorly in a given month** (it might be a calendar effect, not your alpha)
2. **Sanity checking backtests** — if your "alpha" disappears when you control for calendar effects, you don't have alpha
3. **Combining with other strategies** — even small biases compound when stacked correctly
4. **Knowing what other people are doing** — calendar-effect trading drives a meaningful share of institutional flow

## Sources

- Keim (1983) "Size-Related Anomalies and Stock Return Seasonality" — *Journal of Financial Economics*
- French (1980) "Stock Returns and the Weekend Effect" — *Journal of Financial Economics*
- Ariel (1987, 1990) — turn-of-month, holiday effects
- Bouman & Jacobsen (2002) "The Halloween Indicator" — *American Economic Review*
- Lucca & Moench (2015) "The Pre-FOMC Announcement Drift" — *Journal of Finance*

## Related

- [[anomalies-overview]]
- [[calendar-effects]]
- [[expiration-and-rebalancing-flows]]
- [[behavioral-finance]]
- [[seasonal-spread-trading]]
