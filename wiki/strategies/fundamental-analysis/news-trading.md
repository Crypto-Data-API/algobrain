---
title: "News Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: review
tags: [news-trading, event-driven, volatility, crypto, fundamental-analysis, execution, day-trading]
aliases: ["News-Based Trading", "Event-Driven Trading", "Headline Trading", "Catalyst Trading"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto, forex]
complexity: advanced
backtest_status: untested
related: ["[[event-driven-trading]]", "[[scalping]]", "[[volatility]]", "[[sentiment-trading]]", "[[funding-rate]]", "[[liquidations]]", "[[dvol]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [informational, behavioral]
edge_mechanism: "Markets under-react to large fundamental surprises in the first seconds and over-react in the first minutes; the news trader either exploits the first-mover advantage on an unambiguous directional surprise (momentum) or fades the overreaction once the informed flow has dissipated (reversal), with crypto adding a second mechanism: macro releases now directly move BTC/ETH perp funding and open interest within minutes."

# Data and infrastructure requirements
data_required: [economic-calendar, ohlcv-intraday, funding-rates, liquidations, news-feed]
min_capital_usd: 5000
capacity_usd: 10000000
crowding_risk: high

# Performance expectations
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 10

# Kill criteria
kill_criteria: |
  - momentum win-rate falls below 40% over 30 qualifying events (market now fully pre-prices the release)
  - average slippage per event trade exceeds 15 bps (execution infrastructure sub-par; edge consumed by costs)
  - rolling 3-month news-trading Sharpe < 0
  - a single news-event loss exceeds 3% of book (position-sizing failure; halt and re-spec)
---

# News Trading

## Edge source

**Informational** and **behavioral**. See [[edge-taxonomy]].

The informational edge: markets do not fully price a large fundamental surprise in the first seconds; the first-mover who correctly reads the direction of a significant deviation from consensus and executes before the broader market repositions captures the initial price discovery move. This is a genuine informational edge — not forecasting the release, but faster interpretation and execution.

The behavioral edge: after the initial directional move, crowd behavior amplifies the reaction beyond what the news warrants. A CPI print that surprises by +0.3% may move BTC 4% — more than the fundamental impact justifies. The fade variant exploits this overreaction once the informed flow (algos and fast desks) has dissipated and only the momentum crowd remains.

**Crypto-specific news categories:**

1. **Macro (FOMC, CPI, NFP)** — BTC has become highly macro-sensitive post-ETF approval. US CPI and FOMC rate decisions now move BTC perps within seconds via the BTC/SPX correlation channel. High-impact US data releases require the same seconds-level execution as equity/FX news trading, but with a crypto-specific layer: perp funding and open interest begin repricing within the same minute.
2. **Crypto-native events** — ETF approval/rejection decisions, exchange solvency news (FTX-style), major protocol exploits, large token unlocks, regulatory announcements. These move crypto faster and further than macro, and have no equity equivalent in speed or magnitude.
3. **On-chain alerts** — large whale movements, exchange inflows/outflows, and smart-contract events can trigger price moves before public news. CryptoDataAPI `/api/v1/blockchain/exchange-flows` and whale-alert services provide early signals.
4. **Social/narrative catalysts** — viral posts from influential accounts, trending narratives (DeepSeek AI, Musk tweets) can move speculative tokens immediately and then reverse. The fade variant is most applicable here.

**Corporate earnings are out of scope.** This wiki does not cover single-name equities. News trading on equity earnings (SPY, individual stocks) is the TradFi origination context for the strategy but is not the target here.

## Overview

News Trading is a high-intensity strategy that capitalizes on the sharp price movements triggered by major news releases and crypto-native catalysts. The strategy has two primary mechanisms: **momentum trading** (enter in the direction of the initial move on a large, unambiguous surprise and ride the continuation), and **fade trading** (wait for the overreaction and trade the reversal once informed flow dissipates). Both require strict [[risk-management]] because [[volatility]] during news releases can be 5–10× normal levels, spreads widen dramatically, and [[slippage]] can be severe. In crypto, unlike equity news trading, there is no market close to contain a move — a post-FOMC cascade on a Friday evening continues into the weekend with thin order-book depth.

## Null hypothesis

Under the null, a large fundamental surprise is fully priced in the instant it becomes public — the bid/ask immediately jumps to the new equilibrium price and there is no follow-through to exploit. Under this null, momentum news trades enter after the move has already occurred (at the new price) and earn zero before costs. Empirical evidence against the pure null: CPI/FOMC events produce measurable 15–90-minute follow-through in BTC and ETH perps in the post-ETF-approval regime (2024–2026), consistent with gradual institutional repositioning. The null is, however, partially true for crypto-native events like minor token unlocks and social-media catalysts, where the edge is thinner and more crowded.

## Rules

### Entry (Momentum Approach — Crypto)
1. **Identify high-impact events.** For crypto: US CPI, FOMC decisions, NFP, ETF news, and major on-chain/protocol events. Use a macro calendar (Forex Factory, Investing.com) plus a crypto-specific calendar for unlock schedules and protocol governance votes.
2. **Wait for the release.** Do not enter before the number hits. Within 2–10 seconds of the release, identify: (a) direction of the macro surprise, and (b) immediate BTC/ETH perp price reaction on Binance/Bybit.
3. **Enter in the direction of the surprise** if the deviation is significant (CPI beats consensus by +0.3%+, FOMC language is materially more hawkish/dovish than priced). Market orders for speed; the first 30 seconds are the most fertile.
4. **Target the follow-through:** After the initial spike, there is typically a 15–60 minute follow-through as institutional traders (US ETF desks, CME traders) reposition BTC exposure. Monitor perp funding repricing — if funding flips sharply in the direction of the move, the follow-through is live.

### Entry (Fade Approach — Crypto)
1. **Let the initial spike complete.** Wait 5–15 minutes for the first wave of volatility to subside.
2. **Enter against the spike** if the move is disproportionate to the data surprise, or if it is a social/narrative catalyst with no fundamental underpinning (tweet, rumor, low-credibility news).
3. Confirm with perp funding: if funding is spiking in the direction of the move (crowd chasing), the fade is more compelling — latecomers are providing exit liquidity.
4. Use pre-news support/resistance as targets for the fade (a natural reversal anchor).

### Exit
1. **Momentum exit:** Take profits within 30–90 minutes. Most news-driven moves exhaust within the first hour; crypto volatility mean-reverts quickly.
2. **Fade exit:** Target a 50–75% retracement of the initial spike. Exit within the same session or within 4 hours for an intraday catalyst.
3. **Stop-loss:** Tight stops are essential. Risk no more than 1% of account per news trade. For momentum, stop beyond the pre-news price. For fades, stop beyond the spike extreme.

### Position Sizing
Small positions (0.5–1% risk per trade) due to extreme volatility and wide spreads at release time. Reduce further during the most volatile events (FOMC, exchange insolvency). Never size based on conviction in the news; size based on risk-per-trade.

## Indicators / Data Used

- **Economic calendar** — consensus estimates and prior readings (Forex Factory, Bloomberg)
- **CryptoDataAPI `/api/v1/derivatives/funding-rates`** — funding repricing immediately post-event: momentum signal
- **CryptoDataAPI `/api/v1/market-intelligence/liquidations`** — liquidation cascade early warning; a news-driven spike can chain-liquidate perp longs/shorts
- **[[volatility]] (ATR, DVOL)** — gauge pre-event calm and post-event spike magnitude; [[dvol]] is the 30-day backdrop, but 5-min implied moves from Deribit tell you the market's priced-in range
- **Bid-ask spread monitor** — wider spreads signal dangerous liquidity; avoid taker orders if spread > 3× normal
- **Pre-news support/resistance** — anchors for fade targets

## Example Trade

**Event:** US CPI release (crypto-primary framing), 8:30 AM ET.

**Setup:** BTC at $68,000. CPI consensus: +0.2% m/m. Actual prints: +0.5% m/m (hot inflation = higher rates = bearish risk assets).

**Momentum trade:**
1. BTC perp on Binance drops from $68,000 to $65,800 in 15 seconds.
2. Perp funding shifts from +0.01% to −0.02%/8h within 2 minutes (shorts aggressively opening, confirming bearish re-pricing).
3. Enter short BTC perp at $66,000 (first micro-pullback). Stop at $68,200 (above pre-release + 1 ATR buffer).
4. Target: $62,500 (pre-existing support level; 2:1 R:R on the $2,200 risk).
5. Over the next 45 minutes BTC drifts to $63,000 as US equity futures (ES, NQ) also decline. Close position at $63,500.
6. Result: +$2,500/BTC in 50 minutes.

**Fade example (overreaction scenario):**
1. Same CPI print. BTC drops 8% to $62,500 in 10 minutes — disproportionate to a 0.3% CPI beat.
2. Liquidation data shows $450M in BTC long liquidations (most of the forced selling complete).
3. Funding flips strongly negative (−0.08%) — retail shorts crowding in late; fade trigger.
4. Enter long BTC perp at $62,800. Stop $61,000. Target $66,000 (50% retracement).
5. BTC recovers to $65,200 within 2 hours as the liquidation cascade exhaust. Close at $64,800. R:R ≈ 1:1.1 — marginal, but the process identified the exhaustion correctly.

## Performance Characteristics

- **Win rate:** 45–55% momentum, 50–60% fade. High variance — some events produce large moves, others fizzle when data matches consensus.
- **Profit factor:** 1.5–2.5. A handful of large-surprise events account for most of the annual P&L.
- **Best conditions:** Large, unambiguous macro surprises (±0.3%+ CPI miss, hawkish/dovish FOMC pivot language) or definitive crypto-native catalysts (ETF approval, exchange insolvency). Low DVOL pre-event (compressed options pricing unwinds sharply).
- **Worst conditions:** Data matches consensus exactly (no surprise = no move). Conflicting signals (hot headline CPI but cool core CPI). Thin holiday or weekend liquidity where spreads make execution costly.
- **Frequency:** 4–8 qualifying macro events per month (CPI, FOMC, NFP, major GDP) plus variable crypto-native events.

## Capacity limits

News trading is inherently small-scale: the edge window is seconds to minutes, and the first $5–10M notional of a position already moves the BTC perp tape. Practical per-event position: $500K–$5M notional for a retail/small-fund operator. Beyond $10M, market impact in the news window exceeds the expected edge. The strategy is an intraday alpha layer, not a scalable fund strategy.

## What kills this strategy

1. **Market fully pre-prices the release** — as news trading becomes more crowded, the first-mover window shrinks. If the edge disappears (momentum win-rate <40% over 30 events), the strategy is dead.
2. **Execution infrastructure lag** — co-located HFT algos capture the first 500ms of a news move; a retail trader entering 5 seconds after the release is often chasing the move at the new equilibrium price.
3. **False/manipulated news** — in crypto, false rumors and artificially amplified social-media catalysts can produce large moves that reverse when the news is corrected, leaving the momentum trader holding a loss.
4. **Slippage exceeds edge** — wide spreads and market-impact on a taker order during a news release can consume more than the expected move per unit of risk. If average slippage > 15 bps, the strategy's edge is consumed by costs.
5. **Cascades** — a news-driven sell-off can chain-liquidate perp longs and produce a cascade that overshoots fair value dramatically, triggering the momentum trader's stop before the reversal.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Momentum win-rate below 40% over 30 qualifying events
- Average slippage per event trade exceeds 15 bps
- Rolling 3-month news-trading Sharpe < 0
- Single news-event loss exceeds 3% of book

## Advantages

- Very short exposure time reduces multi-day risk
- Clear, objective triggers (the data either surprises or it does not)
- News-driven moves can be enormous, offering outsized reward potential
- Works across crypto perps (primary) and FX/futures (secondary)
- Does not require prediction — you react to information after the fact

## Disadvantages

- **Execution risk is extreme:** spreads widen, orders slip, and platforms lag during high-impact releases
- Requires low-latency execution infrastructure; co-location or premium API access is a material edge
- **Whipsaws are common:** the initial spike often reverses within seconds before the "real" continuation
- Emotional intensity is very high — decisions must be made in seconds
- Many events produce no tradable move when data matches consensus
- Impossible to backtest accurately due to extreme spread conditions during live events
- Crypto crypto-native events (exchange insolvencies, protocol exploits) are inherently unpredictable in timing

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — post-event funding repricing: momentum or reversal confirmation
- `GET /api/v1/market-intelligence/liquidations` — liquidation cascade data: exhaustion signal for fade entries
- `GET /api/v1/market-data/short-term-price` — intraday momentum metrics for fade timing
- `GET /api/v1/volatility/regime` — pre-event vol regime: compressed vol → larger move on surprise

**Historical:**
- `GET /api/v1/backtesting/klines?symbol=BTCUSDT&interval=1m` — 1-minute OHLCV around past events for context
- `GET /api/v1/backtesting/liquidations` — historical liquidation data to identify post-event cascade patterns

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the confirmation and fade layers of this strategy (the first-seconds momentum window belongs to the exchange WS):

- **Calendar** — `GET /api/v1/event/calendar` lists scheduled catalysts up to 30 days out (macro prints, unlocks, depeg risk) with a directional bias per event — the agent's pre-positioning map
- **Confirmation** — `GET /api/v1/derivatives/funding-rates?coin=BTC` for the post-release funding repricing (momentum live vs exhausted) and `GET /api/v1/market-intelligence/liquidations` for the forced-flow exhaustion that arms the fade entry
- **Regime gate** — `GET /api/v1/volatility/regime`: a `compressed` pre-event state implies larger moves on surprise (the highest-EV events); already-`vol_shock` tape means the move is underway and only the fade applies
- **Backtest** — event studies on 1m bars from `GET /api/v1/backtesting/klines` are possible only since 2026-03-30 (1m grows forward); 1h bars back to 2017-08 cover coarser reaction windows. `GET /api/v1/backtesting/liquidations` (HL, since 2026-03-30) replays post-event cascades
- **Tips** — accept that the first 30-second momentum leg is not winnable via REST polling; the agent's realistic edge is the 5-15-minute fade decision, where funding + liquidation reads beat headline speed

## Related

- [[event-driven-trading]] — broader catalyst-trading framework
- [[scalping]] — similar ultra-short-term approach
- [[funding-rate]] — post-news funding repricing signal
- [[liquidations]] — cascade data for fade exhaustion
- [[dvol]] — pre-event vol regime context
- [[cryptodataapi]] — data layer for live and historical event-window analysis
