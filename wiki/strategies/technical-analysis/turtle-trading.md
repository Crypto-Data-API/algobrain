---
title: "Turtle Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [trend-following, breakout, position-sizing, systematic, turtle-traders, richard-dennis, crypto, perpetual-futures]
aliases: ["Turtle Trading System", "Turtle Breakout", "Dennis Turtle Strategy"]
strategy_type: algorithmic
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[donchian-channel-breakout]]", "[[atr]]", "[[position-sizing]]", "[[risk-management]]", "[[trend-following]]", "[[richard-donchian]]", "[[bill-eckhardt]]", "[[donchian-channels]]", "[[liquidations]]", "[[funding-rate]]"]
---

# Turtle Trading

The Turtle Trading system is one of the most famous systematic strategies in history and the canonical complete implementation of rule-based [[trend-following|trend following]]. In 1983 commodities trader Richard Dennis bet his partner William Eckhardt ([[bill-eckhardt]]) that trading could be taught rather than being an innate gift. He recruited a group of novices — the "Turtles" — handed them a fully specified rule set, and they went on to earn reportedly over $175 million. Curtis Faith, an original Turtle, later published the rules in *Way of the Turtle*. The system is a [[donchian-channel-breakout|Donchian channel breakout]] wrapped in [[atr|ATR]]-based [[position-sizing|position sizing]] and rigorous [[risk-management|risk management]]; its enduring lesson is that **the sizing and risk rules — not the entry — are the real edge.** This page keeps the full historical rule set and re-frames its application to crypto, where 24/7 [[perpetual-futures|perpetual futures]] make it directly implementable but introduce funding cost and liquidation dynamics the original commodity version never faced.

## Edge and Mechanism

The Turtle entry captures the positive-skew payoff of momentum: buy strength at new N-period highs, sell weakness at new N-period lows, accept that most breakouts fail for small losses, and let the rare sustained trend run into a very large winner. On its own the breakout is a coin-flip; the system is profitable because it (1) sizes every position to a *constant volatility-adjusted risk* so no single market dominates, (2) pyramids into winners to maximise exposure exactly when the trend is confirming, and (3) caps correlated exposure so a cluster of related markets cannot blow up the account together. The "N" unit — the 20-day ATR — is the linchpin that ties entry, stop, sizing, and pyramiding to a single volatility measure.

## Rules

### Entry — System 1 (short-term)
1. **Long:** buy when price exceeds the 20-day highest high (upper [[donchian-channel-breakout|Donchian channel]]).
2. **Short:** sell short when price breaks the 20-day lowest low.
3. **Filter:** skip the signal if the *previous* System-1 breakout in that market was profitable — this deliberately keeps you positioned for the big trend that often follows a failed breakout. (If skipped, the 55-day System-2 breakout still catches the move.)

### Entry — System 2 (long-term)
1. **Long:** buy above the 55-day highest high.
2. **Short:** sell below the 55-day lowest low.
3. **No filter:** take every signal regardless of the prior breakout's outcome.

### Exit
1. **System 1:** exit longs on a 10-day lowest low; exit shorts on a 10-day highest high.
2. **System 2:** exit longs on a 20-day lowest low; exit shorts on a 20-day highest high.
3. **Stop-loss:** 2N (2× the 20-day ATR) from entry. Non-negotiable — the hard risk cap on every unit.

### Position sizing (the key innovation)
1. **N** = 20-day exponential average of True Range (≈ [[atr|ATR(20)]]).
2. **Dollar volatility** = N × (dollars per point of the instrument).
3. **Unit size** = (1% of account) / dollar volatility. One "unit" therefore risks ~1% of equity per 1N move.
4. **Pyramiding:** add up to 4 units per market, one every **0.5N** of favourable movement, moving stops up as you add.
5. **Correlation caps:** max 4 units in one market, ~6 units in closely correlated markets, ~10–12 units in one direction across the whole portfolio.

## Indicators Used
- [[donchian-channel-breakout|Donchian channels]] (20-period and 55-period highs/lows)
- [[atr|ATR(20)]] — the "N" driving sizing and stops
- True Range for the N calculation

## Worked Crypto Example

**Asset:** BTC/USDT perpetual, daily chart. Account: **$100,000.**

1. **Compute N.** BTC 20-day ATR (N) = **$2,500.** Trading spot-equivalent BTC size, dollar volatility per 1 BTC = $2,500 (1 BTC moves $2,500 per N).
2. **Unit size** = ($100,000 × 1%) / $2,500 = **0.4 BTC per unit.**
3. BTC breaks the **20-day high at $64,000** (System 1). The prior breakout was a loser, so the filter permits entry. **Buy unit 1: 0.4 BTC at $64,000.**
4. **Pyramid** every 0.5N ($1,250): add unit 2 at **$65,250**, unit 3 at **$66,500**, unit 4 at **$67,750** (max 4 units = 1.6 BTC). Raise the stop toward each add.
5. **Stop** 2N ($5,000) below each entry; after the fourth add the aggregate stop sits near **$62,750**.
6. BTC trends to **$80,000** over five weeks. The System-1 exit is the **10-day low**; after a pullback it prints **$75,000** and **all units exit at $75,000.**
7. **Result:** average entry ≈ $65,875 across four units (1.6 BTC), exit $75,000 → **≈ +$14,600 gross.** Note the crypto-specific drag: holding a leveraged long through a positive-[[funding-rate|funding]] regime costs perp funding daily, which must be netted against trend profits — a cost the original commodity Turtles never paid.

## Performance Characteristics
- **Win rate:** ~35–40% — most breakouts fail; the system takes many small losses.
- **Profit factor:** historically ~2.0–3.0, driven by a handful of large trend winners that dwarf the losses.
- **Expectancy:** positive via strict risk caps plus pyramiding into confirmed winners.
- **Drawdowns:** can be deep (30–40%) during extended choppy periods; the original Turtles endured painful losing streaks. Crypto's violent, frequent ranges make these stretches, if anything, more punishing.

*(No Sharpe is quoted: the historical figures come from 1980s diversified futures, and no validated crypto backtest exists on this page — `backtest_status: untested`.)*

## Crypto Application

- **Perps make it directly implementable.** 24/7 [[perpetual-futures]] on BTC, ETH and liquid alts let you run both the long and short side continuously, with none of the exchange-close gap risk of commodity futures — the Donchian channels are unbroken.
- **Funding is a carry cost the original lacked.** Long trend positions held through positive funding, and shorts held through negative funding, bleed the daily funding payment. Over a multi-week trend this can materially erode the ATR-normalised edge; net it into expectancy and prefer venues/timing with favourable funding. See [[funding-rate]].
- **Liquidation vs the 2N stop.** With leverage, price can gap through the 2N stop during a [[liquidations|liquidation cascade]], and an under-collateralised account can be force-liquidated *before* the strategy stop triggers. Keep exchange leverage well below the point where the 2N stop and the liquidation price collide, and treat the 2N rule — not the exchange's maintenance margin — as the true stop.
- **Correlation caps bind harder in crypto.** The system's diversification assumes many *uncorrelated* markets. In crypto almost everything correlates to BTC, especially in risk-off moves, so a "diversified" alt basket is effectively one concentrated long-BTC-beta bet. Apply the correlation caps aggressively and count correlated alts as near-duplicate units.
- **Volatility scaling matters more.** Crypto ATR swings enormously between compressed and expanding regimes; because N recalculates daily, unit sizes shrink automatically as volatility spikes — a desirable, built-in de-risking that must be trusted rather than overridden.
- **Edge decay.** The rules have been public since 1993 and are widely coded; the raw breakout is heavily arbitraged. Any crypto edge now lives in execution, market/parameter selection, funding management, and disciplined risk — not the entry itself.

## Advantages
- Fully systematic — removes emotion and discretion.
- Volatility-based ([[position-sizing|N-unit]]) sizing equalises risk across BTC and volatile alts automatically.
- Pyramiding compounds strong trends; strict stops cap every loss.
- Among the most documented, historically validated trend systems ever published.
- Teaches [[risk-management]] lessons transferable to any strategy.

## Disadvantages
- **Low win rate** is psychologically hard to sustain.
- **Extended drawdowns** during range-bound markets can last months.
- Needs genuinely uncorrelated markets to diversify — scarce in crypto.
- **Public since 1993** — the raw entry edge is largely arbitraged away.
- Perp **funding cost** and **liquidation risk** degrade the naive commodity-era edge.

## Leverage and Risk Profile

Turtle sizing via ATR-normalised N units historically produced effective gross leverage of ~4×–10× across a diversified futures book, each unit risking ~1% of equity per 1N of ATR — leverage was a by-product of futures margin, not a target. Crypto perps offer even higher nominal leverage (often 10×–50×+), which makes the discipline more important, not less: the edge is the *volatility-scaled risk cap*, and the 2N stop must sit inside the liquidation price at all times. As Wilder ([[j-welles-wilder|J. Welles Wilder]]) stressed, ATR-based sizing — not raw leverage — is what separates durable trend systems from blow-ups (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Getting the Data (CryptoDataAPI)

Everything the system needs derives from OHLCV (Donchian highs/lows, N/ATR), plus derivatives data for the crypto-specific funding and liquidation overlays. See [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], and [[cryptodataapi-derivatives]].

- **OHLCV for channels, N and backtests** — `GET /api/v1/market-data/klines` (live) and `GET /api/v1/backtesting/klines` (full archive from 2020) to compute 20/55/10-day extremes and ATR(20), and to backtest the two-system rule set.
- **Funding carry** — `GET /api/v1/derivatives/funding-rates` to net perp holding cost into trend-trade expectancy; historical funding via `GET /api/v1/backtesting/funding`.
- **Liquidation/stop-collision context** — `GET /api/v1/market-intelligence/liquidations` to see cascade risk around the 2N stop.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d&limit=1000"
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

## Related
- [[donchian-channel-breakout]] — the channel system at the core of Turtle entries
- [[donchian-channels]] — the N-period high/low channel concept
- [[atr]] — the volatility measure behind the "N" calculation
- [[position-sizing]] — the Turtle N-unit approach is a masterclass
- [[risk-management]] — the true edge of the system
- [[trend-following]] — the broader philosophy
- [[funding-rate]] — the crypto carry cost of holding perp trends
- [[liquidations]] — the cascade/stop-collision risk on leveraged perps
- [[richard-donchian]] — creator of the underlying channels
- [[bill-eckhardt]] — Dennis's partner who argued trading required innate talent

## Sources
- *Way of the Turtle* (Curtis Faith) and [[book-market-wizards]] — the original rule set and the Dennis/Eckhardt experiment
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — ATR-based sizing (Wilder) as the durability factor in trend systems
