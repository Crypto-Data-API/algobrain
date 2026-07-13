---
title: "Market-Cap Level Trading"
type: concept
created: 2026-05-04
updated: 2026-06-11
status: good
tags: [crypto, technical-analysis, behavioral-finance, memecoin, support-resistance]
aliases: ["MC levels", "market cap levels", "round-number MC trading", "MC S/R"]
domain: [technical-analysis, behavioral-finance]
difficulty: beginner
prerequisites: ["[[support-resistance]]", "[[market-cap]]"]
related: ["[[support-resistance]]", "[[memecoin-sniping]]", "[[pump-fun]]", "[[market-cap]]", "[[behavioral-finance]]", "[[low-cap-crypto-trading-map]]", "[[rug-detection-checklist]]"]
---

Market-cap level trading is a low-cap memecoin technique that treats psychologically round market-cap thresholds — $100k, $500k, $1M, $5M, $10M, $100M — as the primary support and resistance grid for entries and exits. The method was popularized by trader / educator Sajad as a deliberately minimalist "two-indicator" system: market-cap levels plus classical [[support-resistance|support and resistance]], and nothing else. Its core claim is that on tokens too young and too thinly traded for conventional indicators (RSI, MACD, moving averages) to mean anything, traders' attention focuses overwhelmingly on round MC numbers — and so those numbers become self-fulfilling levels.

## Why MC levels work

Low-cap memecoins, especially fresh [[pump-fun|Pump.fun]] launches, share several properties that break standard technical analysis but reinforce MC-level analysis:

- **Price per token is tiny and arbitrary.** A token might trade at $0.000037. Almost no one looks at the price chart in dollar terms; everyone looks at it in market-cap terms via Dexscreener / Birdeye / GMGN. The chart is effectively denominated in MC, not USD.
- **Round MC numbers are universally watched.** "$1M MC" is a meme in itself. Telegram alerts, Twitter callouts, leaderboard tiers, and bot triggers all key off these thresholds.
- **Bonding curve psychology.** Pump.fun's bonding curve graduates to [[raydium|Raydium]] / [[pumpswap|PumpSwap]] near ~$69k MC, anchoring traders to round MC milestones from the very first minute of a token's life.
- **No history.** A 20-minute-old token has no 50-day MA. MC levels are a coordination mechanism that requires no history to function.
- **Coordination over fundamentals.** In a market with no cash flows, the asset is a coordination game. Round numbers are Schelling points.

This is the same mechanism that makes round-dollar prices ($100, $1,000, $50,000) act as support and resistance in equities and Bitcoin, scaled down and applied to FDV/MC.

## The level grid

Sajad's framing uses a roughly half-decade ladder of MC levels, with each level acting as both potential resistance on the way up and potential support on the way back down:

| Tier | Level | Typical behavior |
|------|-------|------------------|
| Pre-bond | $20k, $40k, $69k | Bonding-curve milestones; $69k is the Pump.fun → Raydium graduation point |
| Micro | $100k, $250k, $500k | First "real" psychological tiers post-bond; many tokens die at $100k or $500k |
| Low | $1M, $2M, $5M | The "1M club" — first major resistance; breakthroughs draw fresh attention |
| Mid | $10M, $25M, $50M | Mid-cap memecoin tier; significant whale and CEX-listing interest |
| High | $100M, $250M, $500M | Major tier; failures here often cap a multi-day run |
| Macro | $1B+ | "Unicorn" memecoin status; reached by a tiny fraction of launches |

The exact rungs vary by trader, but the pattern is consistent: clusters of attention at round numbers, with the strongest reactions at $100k, $1M, $10M, and $100M.

## The two-indicator system

Sajad's claim is that on low-cap memecoins, two inputs are sufficient and adding more is noise:

1. **Market-cap levels** — the grid above, marked horizontally on the chart.
2. **Classical [[support-resistance|support and resistance]]** — drawn from the token's own short price history (the obvious wicks, consolidation zones, and prior reaction levels).

Where these two overlap — for example, an MC level at $1M coinciding with a prior reaction wick at $1.02M — is a high-confluence zone. Trades are taken at confluence; everywhere else is no-trade.

Indicators explicitly *not* used (because they are uninformative on tokens this young / illiquid): RSI, MACD, moving averages, Bollinger Bands, volume profile, Fibonacci retracements, Ichimoku.

## How traders use it

### Entries

- **Bounce off a MC level acting as support.** Token drops to $500k MC, wicks below, reclaims — long with a stop just below the level.
- **Break-and-retest of a MC level as new support.** Token closes above $1M MC, pulls back to $1M, holds — long the retest with a stop below.
- **Confluence entries** — only take the trade when an MC level lines up with a price-derived S/R from the token's own history.

### Exits

- **Take profit at the next MC level.** Long from $500k → first take-profit at $1M, scale out further at $2M and $5M.
- **Trail stops behind reclaimed MC levels.** Once $1M holds as support, move the stop to just below $1M.
- **Hard-exit on a clean break-and-fail of a major MC level** ($10M → $5M with no reclaim is a process exit, regardless of P&L).

### Sizing

- **Smaller size at lower MC levels** (more rug risk, more illiquidity, wider stops).
- **Larger size at higher MC tiers** ($10M+) where slippage is bearable and remaining rug risk is mostly soft-rug / dev-sell.
- **Pre-trade [[rug-detection-checklist|rug check]] always runs first.** No level setup matters on a token that fails the basic safety filters.

## Example workflow

1. Token surfaces on Dexscreener / Pump.fun leaderboard at $300k MC.
2. Run the [[rug-detection-checklist]] and [[holder-concentration-analysis]] — pass.
3. Mark MC grid: $500k, $1M, $2M, $5M.
4. Mark price-derived S/R from the (short) chart history.
5. Wait for a setup at confluence — e.g., a retest of $500k MC after a clean break.
6. Enter, stop just below the level, first take-profit at $1M, scale out at $2M+, trail behind reclaimed levels.
7. Exit fully on a clean break-and-fail of the most recent reclaimed MC level.

The whole process is intentionally boring; the edge is in repetition, ruthless filtering of bad setups, and refusing to use any of the indicator stack that works on higher-timeframe, more-liquid markets.

## Why the minimalism

Sajad's case for two indicators (and against more) rests on three claims specific to the low-cap memecoin regime:

- **Indicators built for liquid markets are noise on illiquid ones.** A 14-period RSI on a 30-minute-old token computed off 200 trades from 40 wallets is not measuring anything real.
- **More indicators = more confirmation bias.** Given enough overlays, every chart will show a setup. The discipline is in *not* trading.
- **The actual driver is attention.** MC levels track attention more directly than price-derived indicators do. In an attention-driven market, track attention.

This is a regime-specific claim — the same trader does not argue for a two-indicator system on BTC perps or equities.

## Limitations

- **Levels work until they don't.** A weak token will slice through every MC level on its way to zero. The technique is a structure, not a probability.
- **Useless without rug filtering.** Buying a "$500k MC bounce" on a bundled rug just makes you exit liquidity at a round number.
- **Slippage and MEV erode the edge.** Round-number entries are crowded; sandwich bots and other snipers stack at the same levels. Use limit orders where supported, accept partial fills, and avoid being the marginal buyer at the exact tick of the level.
- **Survivorship bias in the canonical examples.** Tokens that *did* respect MC levels on their way to $100M are the ones shown in tutorials. The thousands that died at $100k are not.
- **Migration discontinuities.** Pump.fun → Raydium / PumpSwap migrations introduce price gaps that can invalidate the MC-level structure that existed pre-bond.
- **Regime-specific.** The technique is for low-cap memecoins on Solana / EVM launchpads. Applying it unchanged to BTC, ETH, blue-chip alts, or equities is unwise.

## Related

- [[support-resistance]] — the underlying technical concept
- [[market-cap]] — definition and FDV vs. circulating distinctions
- [[memecoin-sniping]] — the parent strategy class
- [[pump-fun]] — the venue where this technique was popularized
- [[behavioral-finance]] — round-number bias and Schelling-point coordination
- [[low-cap-crypto-trading-map]] — the broader low-cap workflow this slots into
- [[rug-detection-checklist]] — the safety filter that must run before any MC-level setup

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]] — Sajad's two-indicator system and Pump.fun MC-level workflow
- Public Sajad YouTube content on Pump.fun MC-level / S/R trading
