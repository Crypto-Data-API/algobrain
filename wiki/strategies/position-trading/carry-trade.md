---
title: "Carry Trade"
type: reference
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [carry-trade, forex, interest-rates, macro, position-trading, yield-differential]
aliases: ["Currency Carry Trade", "Interest Rate Carry", "JPY Carry Trade"]
strategy_type: fundamental
timeframe: position|long-term
markets: [forex]
complexity: advanced
backtest_status: untested
related: ["[[forex]]", "[[risk-management]]", "[[interest-rates]]", "[[macroeconomics]]", "[[position-sizing]]"]
---

# Carry Trade

## Overview

The carry trade is a macroeconomic strategy that profits from the **interest rate differential** between two currencies. The trader borrows (sells) a low-interest-rate currency and invests (buys) a high-interest-rate currency, earning the spread between the two rates as ongoing income. This "carry" accrues daily in [[forex]] markets through the **swap rate** or **rollover** mechanism.

The most iconic version is the **JPY carry trade**: borrow Japanese Yen at near-zero rates and invest in higher-yielding currencies like the Australian Dollar (AUD), New Zealand Dollar (NZD), or emerging market currencies. For decades, Japan's ultra-low interest rates made the Yen the world's primary funding currency.

The carry trade is attractive because it generates positive returns even when exchange rates are flat. In theory, the interest rate differential should be offset by currency depreciation of the high-yielder (covered interest rate parity). In practice, this relationship frequently breaks down -- a phenomenon known as the **forward premium puzzle** -- allowing carry trades to be profitable for extended periods.

The risk is catastrophic: carry trades unwind violently during [[risk-off]] events. When fear spikes, traders rush to close carry positions (repay borrowed Yen), causing the funding currency to surge and the investment currency to crash. The 2008 financial crisis and the **July-August 2024 JPY carry trade unwind** are stark examples, with the Yen appreciating 10-15% in weeks, wiping out years of carry income.

## Rules

### Entry
1. **Identify the Pair:** Select a currency pair with a significant positive interest rate differential. The base currency should have the higher rate, the quote currency the lower rate.
2. **Go Long the High-Yielder:** Buy AUD/JPY, NZD/JPY, USD/JPY, or MXN/JPY (examples). You earn the daily swap/rollover.
3. **Macro Filter:** Enter when global risk sentiment is favorable ([[vix]] low, equity markets rising, credit spreads narrow). The carry trade thrives in "risk-on" environments.
4. **Central Bank Alignment:** Ensure the interest rate differential is stable or widening. Monitor central bank statements for signals of rate cuts (high-yielder) or rate hikes (low-yielder), which would narrow the differential.

### Exit
1. **Risk-Off Signal:** Close positions when [[vix]] spikes above 25-30, equity markets sell off sharply, or credit spreads widen. Speed is critical -- carry unwinds are fast.
2. **Rate Convergence:** Exit if central banks signal a narrowing of the interest rate differential (e.g., the high-yielding central bank begins cutting rates, or the funding currency's central bank begins hiking).
3. **Technical Stop:** Place a stop-loss based on [[atr]] or key [[support-and-resistance]] levels to limit damage during sudden unwinds. Carry trades should never be held without stops.
4. **Seasonal/Calendar Risk:** Reduce or close positions before major risk events: central bank meetings, elections, geopolitical flashpoints.

### Position Sizing
- Keep leverage conservative: 2x-5x maximum. Many carry trade blowups involve excessive leverage (10x+).
- Risk no more than 1-2% of capital on any single carry position.
- Diversify across multiple carry pairs to reduce single-currency event risk.

## Indicators Used
- **Interest rate differential** (central bank policy rates, swap rates)
- [[vix]] (CBOE Volatility Index) as a risk sentiment gauge
- **Credit spreads** (investment-grade vs. high-yield bond yields)
- [[moving-average-crossover|Moving averages]] on the currency pair for technical trend confirmation
- **COT (Commitment of Traders) reports** to gauge carry trade crowding
- **Central bank forward guidance** and rate decision calendars

## Popular Carry Pairs (Historically)
| Pair | Funding Currency | Investment Currency | Typical Carry |
|------|-----------------|---------------------|---------------|
| AUD/JPY | JPY (0-0.5%) | AUD (3-5%) | 3-5% annualized |
| NZD/JPY | JPY | NZD (3-5.5%) | 3-5.5% annualized |
| USD/JPY | JPY | USD (4-5.5%) | 4-5% annualized |
| MXN/JPY | JPY | MXN (8-11%) | 8-11% annualized |
| USD/CHF | CHF (0-1.5%) | USD (4-5.5%) | 3-4% annualized |

## Example Trade
**Pair:** AUD/JPY, position trading
1. **Macro Setup:** Global risk is "on." VIX is at 14. The RBA rate is 4.35%, the BOJ rate is 0.10%. Differential: 4.25%.
2. Enter long AUD/JPY at 98.00. Position size: 100,000 AUD (1 standard lot). Leverage: 3x.
3. **Daily carry:** ~11.6 AUD per day ($7.50 USD equivalent), credited via the overnight swap.
4. Over 6 months (180 days), the carry income = ~$1,350.
5. AUD/JPY appreciates to 102.00 (price gain). Price profit = 400 pips x ~$6.80/pip = $2,720.
6. **Total Return:** $1,350 (carry) + $2,720 (price) = **$4,070** on ~$33,000 margin (3x leverage on 100k AUD). Return: ~12.3% in 6 months.
7. **Risk scenario:** A global risk-off event sends AUD/JPY from 98.00 to 88.00 in 3 weeks. Loss = 1,000 pips = $6,800, wiping out the carry and then some. This is why stops and position sizing are essential.

## Historical Unwinds
- **2008 Global Financial Crisis:** AUD/JPY fell from 107 to 55 (-49%) in months. Carry traders suffered catastrophic losses.
- **2011 Tohoku Earthquake/Tsunami:** Yen surged as Japanese investors repatriated capital and carry trades unwound. Coordinated G7 intervention was required.
- **August 2024 JPY Carry Unwind:** The [[bank-of-japan|BOJ]] unexpectedly raised rates while global recession fears spiked. USD/JPY dropped from 162 to 142 in weeks. The Nikkei crashed 12% in a single day. Trillions in carry positions were forcibly closed.

## Performance Characteristics
- **Win Rate:** 65-75% on a monthly basis during risk-on environments. Near 0% during unwinds.
- **Sharpe Ratio:** 0.5-1.0 for simple carry strategies. Higher with risk filters (VIX, trend).
- **Return Profile:** Steady small gains punctuated by sudden large losses -- "picking up pennies in front of a steamroller."
- **Best Market Conditions:** Low volatility, growing global economy, stable interest rate differentials, and accommodative central bank policies.
- **Worst Market Conditions:** Financial crises, geopolitical shocks, sudden central bank policy shifts, liquidity crises.

## Advantages
- Earns income even when exchange rates are flat (the "carry" is paid daily)
- The forward premium puzzle means carry trades have been historically profitable beyond what theory predicts
- Can be combined with technical trend-following for enhanced returns (carry + trend = one of the strongest known FX strategies)
- Diversifiable across many currency pairs
- Exploits a structural feature of global interest rate differentials

## Disadvantages
- **Asymmetric risk:** "Picking up pennies in front of a steamroller." Steady gains, sudden catastrophic losses.
- **Correlation to risk:** All carry trades correlate to global risk sentiment. In a crisis, diversification across pairs provides minimal protection because everything unwinds simultaneously.
- **Leverage dependence:** Meaningful returns typically require leverage, which amplifies losses during unwinds
- **Central bank risk:** A single unexpected rate decision can eliminate the carry differential overnight
- **Crowding risk:** When carry trades become very popular, the eventual unwind is more violent (2024 JPY unwind)
- **Not suitable for small accounts:** Requires significant capital and low leverage to survive drawdowns

## See Also
- [[forex]] -- the market where carry trades primarily operate
- [[risk-management]] -- essential for surviving carry trade drawdowns
- [[interest-rates]] -- the fundamental driver of carry returns
- [[macroeconomics]] -- understanding the macro environment is critical for carry timing
- [[vix]] -- the primary risk sentiment indicator for carry trade management
