---
title: Gamma Exposure (GEX) Trading
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, alpha-edge, options, gamma, dealer-hedging, market-microstructure, volatility]
strategy_type: hybrid
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: [expiration-and-rebalancing-flows, cross-asset-signals, volatility-targeting, options-equity-overlay]
---

# Gamma Exposure (GEX) Trading

## The Edge

Options dealers do not speculate. They market-make, collecting the bid-ask spread, and then hedge their directional exposure away. This hedging is mechanical, predictable, and enormous in scale. When you know the dealer's gamma position, you know whether the market will be pinned or explosive -- before it happens.

**Gamma** is the rate of change of [[delta]]. When dealers are **long gamma** (net sold puts that moved in-the-money, or bought calls), they must buy dips and sell rips to stay delta-neutral. This stabilizes price -- the market feels "sticky," bouncing in a narrow range. When dealers are **short gamma** (net sold calls near the money, large put walls), they must sell into selloffs and buy into rallies to hedge -- amplifying the move. The market becomes a pinball machine.

The edge: by tracking aggregate dealer gamma exposure, you can predict whether the market will mean-revert or trend on any given day. This is not a guess. It is a consequence of the largest participants in the market being forced to hedge mechanically.

## Why It Persists

Options market-making is dominated by a handful of firms (Citadel Securities, Wolverine, Susquehanna). Their hedging activity moves billions of dollars daily. Yet most equity and crypto traders have never heard of gamma exposure. The edge persists because:

1. **Options literacy is rare** -- most traders learn price action and indicators, not Greeks-based market structure
2. **The data is fragmented** -- computing aggregate GEX requires processing the entire options chain across all strikes and expirations
3. **The effect is invisible on a price chart** -- you cannot see dealer hedging in [[candlestick-patterns]] or [[moving-averages]]. It operates beneath the surface
4. **Dealer behavior is non-discretionary** -- they MUST hedge, regardless of what technicals or fundamentals say. This makes GEX a pure structural signal

## How to Implement

### Step 1: Track GEX Data

Use specialized tools that calculate aggregate dealer gamma across all strikes:

- **SpotGamma** -- industry standard for S&P 500 and single-stock GEX levels
- **Squeezemetrics** -- publishes the DIX (dark pool indicator) and GEX daily
- **Unusual Whales / GammaLab** -- real-time GEX visualization
- **Manual calculation** -- pull open interest per strike from CBOE, multiply by gamma × contract size × 100, assume dealers are short calls and long puts (standard flow assumption)

### Step 2: Identify the Gamma Flip Level

The **gamma flip** is the price level where aggregate dealer gamma switches from positive to negative. Above this level, dealers stabilize the market. Below it, they amplify moves.

- **Price above gamma flip** → market is rangebound, mean-reverts. Strategy: sell [[options-premium-selling|premium]], fade extremes, trade [[mean-reversion]] setups
- **Price below gamma flip** → market is volatile, trends hard. Strategy: buy [[options-strategies|options]] for protection, trade [[breakout-trading|breakouts]], avoid fading moves

### Step 3: Trade the Regime

| GEX Regime | Market Behavior | Strategy |
|---|---|---|
| High positive GEX | Pinned, low vol, narrow range | Sell straddles, iron condors, fade SPX moves |
| Low positive GEX | Mild directional moves possible | Directional trades with moderate sizing |
| Negative GEX | Explosive, trending, high vol | Buy straddles, trade momentum, avoid mean-reversion |
| Deeply negative GEX | Crash/melt-up risk | Maximum hedging, tail-risk plays via [[asymmetric-barbell]] |

### Step 4: OpEx Pinning

Near options expiration (especially monthly OpEx on the third Friday), open interest concentrations create a magnetic effect. Dealers' hedging pulls price toward the strike with the largest open interest -- the "[[max-pain]]" level.

- **3-5 days before OpEx**: identify the max pain strike and the two largest OI call/put strikes
- **Expect price to gravitate** toward max pain as gamma hedging intensifies
- **Post-OpEx (Monday after)**: the pin releases. Gamma clears. Moves that were suppressed often accelerate -- this is the "OpEx volatility pop"

## Example Setup

**S&P 500 -- March 2025 GEX regime trade:**

1. SpotGamma shows gamma flip at 5,150. SPX trading at 5,220 (above flip = positive gamma regime)
2. GEX is $8B positive -- extremely high. Market has been pinned in a 30-point range for 4 days
3. Sell SPX 0DTE iron condors: sell 5190/5250 strangles, buy 5180/5260 wings. Collect $3.50 credit on $10 wide spreads
4. SPX oscillates between 5,195 and 5,245 all day (dealer hedging keeps it pinned)
5. Both short strikes expire OTM. Full credit collected. Repeat daily while high-GEX regime persists
6. **Regime shift**: FOMC meeting causes SPX to drop below 5,150 (gamma flip). GEX turns negative
7. **Switch to momentum**: stop selling premium immediately. Buy puts or trade breakdowns. The dealers are now amplifying the move

## Risk Management

- **GEX is a regime indicator, not an entry signal** -- it tells you HOW to trade, not WHEN. Combine with [[technical-analysis]] for entry timing
- **OpEx week is the highest-conviction GEX period** -- the rest of the month, GEX signals are weaker
- **GEX can shift intraday** -- a large options trade can flip dealer positioning. Monitor in real-time if possible
- **Do not fight negative gamma** -- when GEX flips negative, the market can move 2-3x its normal daily range. Cut losses fast, do not average down
- **The 0DTE explosion** has changed GEX dynamics since 2022 -- daily options expiration means gamma effects reset every day, not just monthly. Track 0DTE flows separately
- Maximum position size: 3% of portfolio in any single GEX-based trade. The regime is probabilistic, not certain

## Real-World Examples

- **January 2024 OpEx pin** -- SPX pinned within 10 points of the 4,800 strike (massive OI) for the entire expiration week, then rallied 50 points the following Monday when gamma cleared
- **Volmageddon (Feb 2018)** -- dealers were massively short gamma from structured products. When VIX spiked, their hedging amplified the selloff into a crash. Traders tracking GEX saw the negative gamma regime and stayed short
- **Meme stock squeezes (GME, AMC)** -- dealers who sold call options were short gamma. As price rose, they were forced to buy shares to hedge, which pushed price higher, forcing more buying -- a textbook gamma squeeze
- **Crypto options growth** -- Deribit and CME crypto options now create measurable GEX effects on BTC. Large strike expirations (e.g., $100K BTC calls) create observable pinning behavior near expiry
- **Quad witching** (simultaneous expiry of stock options, index options, index futures, stock futures) creates the highest GEX concentration of the year -- and the most predictable pinning and post-expiry moves

The core insight: in a market dominated by options hedging, understanding dealer positioning is not optional. It is the hidden hand moving price.
