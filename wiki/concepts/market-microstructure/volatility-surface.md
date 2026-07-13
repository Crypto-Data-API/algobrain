---
title: "Volatility Surface"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [options, volatility, implied-volatility, pricing, derivatives]
aliases: ["Vol Surface", "IV Surface", "Implied Volatility Surface", "Volatility Smile", "Volatility Skew"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[implied-volatility]]", "[[options]]", "[[black-scholes]]", "[[moneyness]]"]
difficulty: advanced
related: ["[[implied-volatility]]", "[[black-scholes]]", "[[moneyness]]", "[[skew-trading]]", "[[options-implied-vol-skew]]", "[[second-order-greeks]]", "[[volatility-risk-premium]]", "[[vega]]"]
---

The volatility surface is a three-dimensional representation of [[implied-volatility]] across all available [[strike-price|strikes]] (x-axis) and expirations (y-axis), with IV as the z-axis. It captures the market's complete picture of expected future uncertainty — not a single number, but a rich surface of information that encodes supply/demand, tail risk expectations, event premiums, and structural market dynamics.

The [[black-scholes]] model assumes volatility is constant across strikes and time. In reality, it never is. The volatility surface is the empirical correction to that idealization.

## Anatomy of the Surface

### The Smile (Strike Dimension)

At any single expiration, IV plotted against strike typically forms one of these shapes:

**Equity Skew (Post-1987)**:
- OTM puts have higher IV than ATM options
- OTM calls have slightly lower IV than ATM
- The "smile" is really a "smirk" — asymmetrically tilted toward downside strikes
- Reflects persistent demand for portfolio hedges (institutional puts) and the empirical fact that equities crash more violently than they rally

**FX/Commodity Smile**:
- Both OTM puts and OTM calls have higher IV than ATM
- Forms a symmetric or near-symmetric U-shape
- Reflects two-sided tail risk — currencies and commodities can spike in either direction

**Earnings/Event Smile**:
- Elevated IV at all strikes for the expiration spanning the event
- Flatter skew (the event risk is roughly symmetric for many catalysts)
- Sharp IV difference between pre-event and post-event expirations

### The Term Structure (Time Dimension)

IV varies across expirations:

| Term Structure Shape | Meaning | Typical Condition |
|---------------------|---------|-------------------|
| **Contango** (upward-sloping) | Near-term IV < far-term IV | Normal/calm markets — longer horizons have more uncertainty |
| **Backwardation** (inverted) | Near-term IV > far-term IV | Stressed markets — immediate fear exceeds long-term uncertainty |
| **Humped** | Peak IV at a specific expiration | Event-driven — earnings, FOMC, or election concentrated at one date |

The term structure inverts during crises (March 2020, August 2024) because fear is concentrated in the immediate term. It steepens in calm markets as short-dated options are cheap relative to longer-dated ones.

## Key Measures Derived from the Surface

### Skew

The difference in IV between OTM puts and ATM options (or OTM calls), typically measured as:

```
25-delta skew = IV(25Δ put) - IV(25Δ call)
```

Positive skew (puts more expensive) is normal for equities. Extreme skew indicates either panic hedging or complacency in calls. See [[skew-trading]] and [[options-implied-vol-skew]] for trading applications.

### Term Structure Slope

```
Term slope = IV(60-day) - IV(30-day)
```

Or more commonly normalized by comparing the [[vix]] (30-day) to the VIX3M (90-day). A [[vix]] above VIX3M indicates inverted term structure — a historically reliable stress signal.

### Butterfly Spread (Curvature)

```
Butterfly = IV(25Δ put) + IV(25Δ call) - 2 × IV(ATM)
```

Measures the curvature (convexity) of the smile. High butterfly values mean the market prices extreme moves (both up and down) as more likely than a log-normal distribution would predict. This curvature is the source of [[vomma|vomma/volga]] risk.

## Why the Surface Exists

The [[black-scholes]] model assumes returns are log-normally distributed with constant volatility. Reality deviates in several ways:

1. **Fat tails**: Stock returns have fatter tails than the normal distribution — extreme moves happen more often than Black-Scholes predicts. OTM options compensate for this tail risk with higher IV.

2. **Leverage effect**: When stocks drop, their leverage (debt/equity) rises, making them riskier. This creates negative correlation between returns and volatility, steepening the put skew.

3. **Supply/demand imbalance**: Institutional investors are structural buyers of OTM puts (portfolio insurance) and structural sellers of OTM calls (overwriting). This persistent flow tilts the skew.

4. **Jump risk**: Sudden gaps (earnings surprises, geopolitical events) affect OTM options disproportionately. The market prices this jump risk into the wings.

5. **Volatility-of-volatility**: [[implied-volatility]] itself is volatile (vol-of-vol). Higher vol-of-vol lifts the wings of the smile (increasing butterfly/curvature). This is the [[vomma|vomma]] component.

## Trading the Surface

### Skew Trades

Profiting from changes in the slope of the smile:
- **Long skew** (buy OTM puts, sell OTM calls): Profits when put IV rises relative to call IV (typically during selloffs). See [[risk-reversal]].
- **Short skew** (sell OTM puts, buy OTM calls): Profits when skew flattens — often after panic subsides.
- [[skew-trading]] details systematic approaches.

### Term Structure Trades

Profiting from changes in the time dimension:
- **[[calendar-spread]]**: Sell near-term, buy far-term (same strike). Profits from contango steepening or near-term IV declining.
- **Reverse calendar**: Buy near-term, sell far-term. Profits from term structure inversion — typically an event or crisis trade.
- **[[diagonal-spread]]**: Combines strike and time differences.

### Curvature Trades

Profiting from changes in the smile's convexity:
- **[[butterfly-spread]]**: Profits from curvature changes at specific strike zones.
- Long butterfly = short curvature (profits if the smile flattens locally).
- **[[iron-butterfly]]**: The credit version of curvature trades.

### Surface Arbitrage

Professional firms use the volatility surface for:
- **Relative value**: Comparing IV across related assets (e.g., single-stock vol vs index vol to derive [[implied-correlation]])
- **Calendar arbitrage detection**: The surface must satisfy no-arbitrage constraints — total variance must be increasing in time. Violations signal mispricings.
- **Sticky-strike vs sticky-delta**: Different models for how the surface moves when the underlying moves, with implications for dynamic hedging.

## The Surface and Second-Order Greeks

The shape of the volatility surface directly creates [[second-order-greeks]] exposure:

| Surface Feature | Greek Affected | Mechanism |
|----------------|---------------|-----------|
| Skew slope | [[second-order-greeks|Vanna]] | As the underlying moves, options cross different IV levels on the surface |
| Curvature (butterfly) | [[second-order-greeks|Vomma]] | Vol changes move options up/down the curvature, changing vega non-linearly |
| Term structure | [[second-order-greeks|Charm]] | Different expirations decay at different rates, shifting relative Greeks |

This is why traders who ignore the surface and use flat-vol Greeks get hedging errors — the actual Greeks depend on the full surface, not just ATM IV.

## Modeling the Surface

### Common Models

| Model | Approach | Strengths | Weaknesses |
|-------|---------|-----------|------------|
| **Black-Scholes** | Flat vol (no surface) | Simple, closed-form | Ignores smile/skew entirely |
| **Local volatility** | Deterministic vol function σ(S,t) | Fits surface exactly | Unrealistic smile dynamics |
| **Stochastic volatility** (Heston) | Vol follows its own random process | Captures vol-of-vol, mean reversion | Harder to calibrate, limited skew control |
| **SABR** | Stochastic vol with correlation | Industry standard for rates/FX | Less common for equities |
| **Jump-diffusion** (Merton) | Normal diffusion + random jumps | Captures fat tails, earnings gaps | Additional parameters to estimate |

No single model dominates. Practitioners often use local volatility for pricing and stochastic volatility for risk management and exotic option hedging.

## Practical Usage

### Reading the Surface

1. **Check ATM IV**: Overall level of fear/complacency
2. **Check skew**: How much more expensive puts are vs calls — extreme skew = high hedging demand
3. **Check term structure**: Inverted = stress; steep contango = complacency
4. **Check curvature**: High butterfly = market pricing tail events
5. **Compare to recent history**: Is the surface richer or cheaper than its recent range?

### Tools

- **[[tradingview-platform|TradingView]]**: Basic IV plots by strike
- **[[spotgamma|SpotGamma]]**: Dealer-centric surface analysis with gamma/vanna flows
- **ORATS**: Professional vol surface analytics, skew metrics, historical surface data
- **OptionMetrics**: Academic-grade historical surface data (IvyDB)
- **Bloomberg OVDV**: Institutional standard for vol surface analysis

## Related

- [[implied-volatility]] — the variable that defines the surface
- [[black-scholes]] — the model whose constant-vol assumption the surface corrects
- [[moneyness]] — the natural x-axis for the strike dimension
- [[skew-trading]] — trading the slope of the smile
- [[options-implied-vol-skew]] — skew as a return predictor
- [[second-order-greeks]] — surface shape creates vanna, vomma exposure
- [[calendar-spread]] — trading the term structure dimension
- [[volatility-risk-premium]] — the surface's overall level relative to realized vol
- [[vix]] — derived from the SPX volatility surface

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's practical treatment of the volatility smile, skew, and term structure
- [[book-options-futures-other-derivatives]] — Hull's formal treatment of volatility surfaces, local volatility, and stochastic volatility models
