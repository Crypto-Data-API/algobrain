---
title: "Chandelier Exit"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [indicators, technical-analysis, volatility, trend-following]
aliases: ["Chandelier Exit", "Chandelier Stop"]
domain: [indicators]
prerequisites: ["[[atr]]", "[[volatility]]"]
difficulty: intermediate
related: ["[[atr]]", "[[average-true-range]]", "[[trailing-stop]]", "[[stop-loss]]", "[[trend-following]]", "[[volatility]]", "[[parabolic-sar]]", "[[atr-trailing-stop]]"]
---

The **Chandelier Exit** is a volatility-based [[trailing-stop]] developed by Charles Le Beau and popularized in Alexander Elder's *Come Into My Trading Room*. It places a stop a multiple of the [[average-true-range|Average True Range (ATR)]] below the highest high (for long positions) or above the lowest low (for short positions) reached since entry, so the stop "hangs down" from the high like a chandelier from a ceiling -- giving the trend room to breathe while [[volatility]] is normal, then tightening only as the trend extends to new extremes.

## How It Works

The exit anchors to the extreme price of the trade and offsets it by a volatility buffer:

- **Long stop** = Highest High (over `n` periods) − ([[average-true-range|ATR]](`n`) × multiplier)
- **Short stop** = Lowest Low (over `n` periods) + (ATR(`n`) × multiplier)

Default parameters are **22 periods** (roughly one trading month) and a **3× ATR** multiplier. The stop only ratchets in the direction of the trade -- for a long, it can rise as new highs are made but never falls. Because the buffer scales with [[atr|ATR]], the stop automatically widens in turbulent markets (avoiding premature shake-outs) and tightens in calm markets (locking in gains).

The key contrast with a fixed-percentage stop is that the Chandelier Exit measures distance in units of recent [[volatility]] rather than a static price amount, so the same logic adapts across instruments and regimes without re-tuning.

### Parameter guide

| Multiplier | Periods | Behaviour | Best suited to |
|------------|---------|-----------|----------------|
| **2× ATR** | 22 | Tight; exits early | Choppy, noisy instruments; shorter holds |
| **3× ATR** | 22 | Default balance | Most swing/position trend trades |
| **4×+ ATR** | 22 | Loose; lets trends run far | Strong, low-noise trends; longer holds |
| 3× ATR | 10-14 | More reactive (shorter HH window) | Faster-moving / intraday systems |
| 3× ATR | 50+ | Very slow to ratchet | Long-term position trading |

A wider multiplier or longer period gives the trend more room (fewer whipsaws, but more open profit surrendered at the turn). A tighter setting protects profit sooner but increases the chance of being shaken out of a still-valid trend.

## Worked Example (long position)

Illustrative numbers for a long trade:

- Entry at **$50**; the trade runs and the highest high since entry reaches **$70**.
- Current ATR(22) = **$2.00**.
- Multiplier = **3×** -> buffer = 3 × $2.00 = **$6.00**.
- **Chandelier stop = $70 − $6 = $64.**

Now price pushes to a new high of **$76** while ATR rises to **$2.50** (volatility expanding):

- New buffer = 3 × $2.50 = **$7.50** -> raw stop = 76 − 7.50 = **$68.50**.
- Because the prior stop was $64 and the new computed level ($68.50) is higher, the stop **ratchets up to $68.50.** It can never move back down.

If price then pulls back and *closes* below $68.50, the long is exited -- having locked in roughly $18.50 of the move from a $50 entry. Note how the buffer *grew* in dollar terms ($6 -> $7.50) as ATR rose, automatically giving the trade more room precisely when the market got noisier.

## How Traders Use It

The Chandelier Exit is primarily a **[[trend-following]]** exit, designed to keep a trader in a winning trend until the move genuinely reverses rather than being stopped out by routine noise. Practical uses:

- **Profit protection** -- ride a trend with a stop that climbs behind price, converting an open profit into a defended one.
- **Mechanical exit discipline** -- removes the discretion (and emotion) from when to take profits, a common failure point for discretionary traders.
- **Multiplier tuning** -- a tighter multiplier (e.g. 2× ATR) exits sooner and suits choppier instruments; a wider multiplier (4×+) suits strong, low-noise trends.
- **Two-stage stops** -- many traders pair it with a separate, fixed initial [[stop-loss]] at entry and only *switch* to the Chandelier Exit once the trade is in profit, so the volatility trail manages the winner rather than the initial risk.

### Chandelier Exit vs. peers

| Method | Spacing logic | Strength | Weakness |
|--------|---------------|----------|----------|
| **Chandelier Exit** | ATR multiple below highest high | Volatility-adaptive; anchored to trade extreme | Gives back profit in sideways markets |
| [[parabolic-sar\|Parabolic SAR]] | Acceleration factor | Tightens automatically as trend ages | Whipsaws badly in chop; flips sides |
| Fixed % trailing stop | Static % of price | Simple, predictable | Ignores volatility regime; needs re-tuning per instrument |
| Chart-structure stop | Below swing low / structure | Respects market structure | Discretionary; no volatility scaling |

## Common Pitfalls and Risks

- **Profit give-back in ranges**: in a sideways or [[consolidation|consolidating]] market the Chandelier Exit gives back a meaningful slice of profit before triggering, because the highest high stalls while ATR keeps the buffer wide.
- **Gap risk**: like all trailing stops, it offers no protection against overnight or news gaps that leap past the stop level.
- **Repainting confusion**: the line moves as new highs print and ATR changes; backtests must use only data available at decision time to avoid look-ahead bias.
- **Wrong anchor on entry**: anchoring the "highest high" window to before the trade began can place an unrealistically loose stop -- most implementations reset the extreme from the entry bar forward.
- **Over-tight multipliers**: dropping below ~2× ATR in a normal trend converts the tool into a noise-triggered exit, defeating its purpose.
- **Single-tool reliance**: it manages exits, not entries or position sizing; it should sit inside a complete plan, not replace one.

## Sources

- Elder, Alexander. *Come Into My Trading Room: A Complete Guide to Trading.* Wiley, 2002.
- Le Beau, Charles & Lucas, David W. *Technical Traders Guide to Computer Analysis of the Futures Markets.* McGraw-Hill, 1992.
- StockCharts.com, "Chandelier Exit" (ChartSchool indicator reference).

## Related

- [[average-true-range]] / [[atr]] — the volatility measure the buffer is built from
- [[trailing-stop]] — the broader category of stops that follow price
- [[atr-trailing-stop]] — the generic ATR-trailing-stop family the Chandelier belongs to
- [[parabolic-sar]] — an alternative trend-following trailing stop
- [[stop-loss]] — the fixed initial stop often paired with the Chandelier Exit
- [[trend-following]] — the trading style the exit is designed to serve
- [[volatility]] — the regime variable the exit adapts to
