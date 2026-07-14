---
title: "Trend Following + Tail Risk Hedge"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [combinations, meta-strategy, trend-following, tail-risk, crisis-alpha, hedging, managed-futures]
strategy_type: hybrid
timeframe: medium to long-term (weeks to months)
markets: [futures]
complexity: advanced
backtest_status: untested
related: ["[[trend-following]]", "[[managed-futures]]", "[[tail-risk-hedging]]", "[[protective-puts]]", "[[vix-calls]]", "[[risk-parity]]", "[[cta-strategies]]", "[[crisis-alpha]]", "[[dragon-portfolio]]", "[[convexity]]", "[[mark-spitznagel]]", "[[universa-investments]]", "[[antifragility]]", "[[fat-tails]]", "[[commodities]]"]
---

# Trend Following + Tail Risk Hedge

## Overview

Trend following and tail risk hedging are two of the most powerful crisis-fighting strategies, but they cover different types of crises. [[trend-following]] generates "crisis alpha" — profits during sustained market declines — because it systematically goes short as downtrends develop. It caught the 2008 financial crisis, the 2020 COVID crash (after the initial shock), and multiple bear markets. But trend following is reactive: it needs time to detect and position for a trend. A flash crash, a sudden gap down, or a one-day 10% drop happens too fast for trend signals to respond.

[[tail-risk-hedging]] — deep out-of-the-money puts and [[vix-calls]] — provides instant protection against exactly these sudden shocks. But tail hedging is expensive: the constant premium bleed in normal markets can consume 3-5% of portfolio value annually, which is a crushing drag during the majority of time when markets are calm.

**The combination solves both weaknesses.** Trend following covers extended crises and actually profits during most of the year. Tail hedges cover the sudden shocks that trend following misses. The income from trend following in normal markets offsets the cost of tail hedges. Together, they create a portfolio that is protected against both slow and fast crises.

## The Synergy

**Complementary crisis coverage.** Crises come in two speeds:

*Slow crises* (2000-2002 dot-com bust, 2007-2009 financial crisis, 2022 rate hiking cycle): Markets decline over months or years with identifiable trends. Trend following captures these beautifully — CTA indices were up 20-40% in 2008 while the S&P 500 fell 37%. But the initial move can be missed.

*Fast crises* (Black Monday 1987, COVID March 2020, Flash Crash 2010): Markets collapse in days or hours. No trend signal is fast enough. Deep OTM puts and VIX calls explode in value during these events — a VIX call bought at $15 strike might pay out at $80. But between fast crises, these hedges expire worthless month after month.

The combination covers the full speed spectrum of market disaster.

**Cost efficiency through trend-following profits.** The biggest objection to tail risk hedging is cost. If you spend 3% annually on puts and the market goes up, you have a 3% drag that compounds painfully over time. But trend following generates positive returns in normal trending environments (not just crises). In typical years, a diversified trend-following strategy earns 5-15% annually. This income more than offsets the tail hedge premium cost, making the combined portfolio self-funding.

**Portfolio-level convexity.** Trend following has moderate convexity — it profits more in large moves than small ones. Tail hedges have extreme convexity — they are worth nearly zero in normal markets and worth 10-100x in crashes. Combined, the portfolio develops a powerful convex return profile: small losses in choppy markets, reasonable gains in trending markets, and explosive gains in crises.

## Component Strategies

| Component | Allocation | Role | Return Profile |
|-----------|-----------|------|---------------|
| [[trend-following]] (multi-asset CTA) | 70-80% | Core strategy, crisis alpha, trend capture | Positive in trends, negative in chop |
| [[tail-risk-hedging]] (deep OTM puts) | 10-15% | Sudden crash protection | Bleed 90% of the time, 10-50x in crashes |
| [[vix-calls]] | 5-10% | Volatility spike protection | Bleed in low-vol, explosive in vol spikes |
| Cash/short-term bonds | 5-10% | Collateral and rebalancing reserve | Small positive carry |

## Implementation

**Step 1 — Trend-Following Core (80% allocation)**

Deploy a systematic trend-following strategy across diversified futures markets:

- **Markets:** Equity indices (S&P 500, Nasdaq, Euro Stoxx), bonds (US 10-year, Bund), [[commodities]] ([[crude-oil]], [[gold]], [[copper]]), currencies (EUR/USD, JPY/USD). Minimum 15-20 markets for diversification.
- **Signal:** Use a dual moving average crossover — 50-day and 200-day [[moving-averages]], or an exponential equivalent. Go long when the short MA is above the long MA. Go short when below. Some implementations use a faster signal (10/50 day) for a portion of the allocation to capture quicker moves.
- **Position sizing:** Use [[atr-position-sizing]] — risk 0.5-1% of portfolio per market based on the 20-day Average True Range. This equalizes risk across volatile and calm markets.
- **Diversification:** Equal risk allocation across the four asset class groups. No single market should represent more than 10% of total risk.

If you cannot trade futures directly, managed futures ETFs or funds provide access: DBMF, KMLM, or allocations to CTA managers.

**Step 2 — Tail Risk Layer (15% allocation)**

Deploy two tail risk instruments:

*Deep OTM S&P 500 Puts (10%):*
- Buy puts 20-30% out of the money on SPX or SPY
- Use 60-90 DTE (quarterly expiry) to reduce roll cost
- Spend approximately 0.3-0.5% of total portfolio per month on put premium
- These puts are nearly worthless most of the time. In a 30% crash, they can be worth 10-30x their cost.
- Roll quarterly: sell existing puts (recapture any remaining value) and buy new ones

*VIX Calls (5%):*
- Buy [[vix-calls]] at strikes of 25-35 (when VIX is at 12-18)
- Use 30-60 DTE
- Spend approximately 0.1-0.2% of total portfolio per month
- VIX calls profit from any volatility spike, not just equity declines. They also protect against correlation spikes and cross-asset crises.
- These are the first-responder hedge — VIX reacts faster than any other instrument in a crisis

**Step 3 — Monthly Rebalancing**

On the first trading day of each month:
1. Mark all positions to market
2. Rebalance trend-following positions based on updated signals
3. Roll any expiring tail risk positions
4. Sweep any realized trend-following profits above target allocation into cash or into replenishing the tail hedge budget
5. If a tail hedge paid off big in a crisis, rebalance profits back into trend-following positions to reload

**Step 4 — Crisis Execution**

When a crisis hits:
- Tail hedges pay off immediately (within hours/days)
- Take partial profits on puts and VIX calls (sell 50-70%) — do not hold for maximum payout, as the timing of crisis lows is unpredictable
- Trend-following signals will start flipping to short positions within days to weeks
- Use tail hedge profits to fund new trend-following entries on the short side
- The cascade: tail hedges buy time while trend-following catches up

## Example Setup

**$1,000,000 portfolio:**

- **$800,000 in trend-following:** Allocate across 20 futures markets using 50/200 MA crossover system. Current positions: long gold, long bonds, short crude oil, short EUR/USD (based on current trends). Using 0.75% risk per market via ATR sizing.
- **$100,000 in SPX puts:** Buy 10x SPX 3600 puts (30% OTM if SPX at 5100), 90 DTE, at ~$8.00 each = $80,000 cost per quarter. Remaining $20K reserved for rolling and opportunistic adds.
- **$50,000 in VIX calls:** Buy VIX 30 calls, 60 DTE, at ~$2.50 each. Buy 100 contracts = $25,000. Reload monthly as they decay.
- **$50,000 cash reserve:** Collateral for futures margins and rebalancing buffer.

**Annual cost of tail hedge layer:** Approximately $150,000-200,000 (2-3% of portfolio). In a normal year, the trend-following core targets 8-15% return ($80,000-$150,000), making the combination roughly self-funding.

**In a 2008-style crisis:** Trend following earns 20-40% ($200,000-$400,000) as it goes short equities and long bonds. Tail hedges pay 10-30x ($1,000,000-$3,000,000 on the put position alone). The combined portfolio potentially doubles while the market falls 35%.

## When It Excels

- **Major bear markets and crises** — this is what the combination is built for. Both components profit during extended declines, and the tail hedge catches the sudden onset.
- **Volatile, trending environments** where trend following has clear signals and tail hedges are occasionally triggered by sharp moves.
- **As a portfolio diversifier** — this combination has extremely low (often negative) correlation to traditional stock/bond portfolios, making it ideal as a 15-25% allocation within a broader [[asset-allocation]].
- **For institutional investors** and family offices who need to protect against catastrophic drawdowns while still generating positive returns.

## When It Fails

- **Low-volatility, sideways markets** (2017 was a prime example). Trend-following signals whipsaw with small losses, and tail hedges bleed premium month after month. The combined drag can be 5-10% in a single calm year.
- **V-shaped recoveries** — if the market crashes 20% and recovers within weeks (March 2020), trend following may go short just before the reversal, giving back gains. The tail hedge profits on the down move but the trend component loses on the whipsaw.
- **Rising rate environments** where bond trend-following enters a prolonged downtrend that also causes equity weakness — correlation between bonds and stocks increases, reducing diversification benefit within the trend-following component.
- **Persistent low VIX** where tail hedge costs are relatively low but opportunities are few, creating a slow bleed that tests investor patience.

## Real-World Usage

**[[universa-investments|Universa Investments]]** ([[mark-spitznagel|Mark Spitznagel]], advised by [[nassim-taleb|Nassim Taleb]]) is the most famous tail risk fund. They reportedly returned over 4,000% in March 2020. Their core strategy is buying deep OTM puts — pure tail risk. But Universa as a standalone is extremely difficult to hold through the years of bleed. The combination with trend-following makes the overall portfolio tolerable in normal years.

**Man AHL, Winton, and other major CTAs** run diversified trend-following strategies that form the natural core of this combination. Many CTA funds have started adding explicit tail hedging overlays in recent years, recognizing that trend following alone is too slow for flash crashes.

**Bridgewater's All Weather** uses a different but related concept — [[risk-parity]] with trend overlays. The idea of combining multiple strategies to cover different market environments is central to Bridgewater's philosophy.

**The "Dragon Portfolio"** concept (Artemis Capital) specifically advocates combining trend following + tail risk hedging + equities + gold + commodity trend as the optimal long-term portfolio. Research by Chris Cole shows this combination outperformed traditional portfolios across 100 years of data, including periods of inflation, deflation, growth, and crisis.

**See also:** [[trend-following]], [[managed-futures]], [[tail-risk-hedging]], [[protective-puts]], [[vix-calls]], [[risk-parity]], [[crisis-alpha]], [[dragon-portfolio]], [[convexity]], [[mark-spitznagel]], [[universa-investments]], [[antifragility]], [[fat-tails]], [[drawdown]], [[commodities]]
