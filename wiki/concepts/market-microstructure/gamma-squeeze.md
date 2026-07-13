---
title: Gamma Squeeze
type: concept
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [options, market-microstructure, volatility, derivatives]
aliases: ["gamma exposure squeeze", "dealer hedging squeeze", "gamma squeeze"]
domain: [market-microstructure]
prerequisites: ["[[options-greeks]]", "[[delta-hedging]]", "[[short-squeeze]]"]
difficulty: advanced
related:
  - "[[cryptodataapi]]"
  - "[[short-squeeze]]"
  - "[[short-interest]]"
  - "[[float]]"
  - "[[trading-volume]]"
  - "[[delta-hedging]]"
  - "[[options-greeks]]"
  - "[[dealer-gamma-positioning]]"
  - "[[implied-volatility]]"
---

# Gamma Squeeze

A gamma squeeze occurs when options market makers are forced to buy increasing amounts of the underlying stock to hedge their short call positions as the stock price rises, creating a self-reinforcing feedback loop that drives prices higher.

## Mechanics

1. Traders buy large quantities of call options (especially short-dated, out-of-the-money)
2. Market makers who sell these calls hedge by buying the underlying stock (delta hedging)
3. As the stock rises, the calls move closer to being in-the-money, and their delta increases
4. **Gamma** (the second derivative of option value with respect to spot, Γ = ∂²V/∂S² = ∂Δ/∂S) measures how fast delta changes -- high gamma means market makers must buy more stock for each price increment. Gamma peaks for at-the-money, near-expiry options, exactly where retail call-buying concentrates during a squeeze.
5. This additional buying pushes the price up further, requiring even more hedging
6. The cycle accelerates until options expire or buying pressure subsides

The hedging quantity is mechanical: a dealer short calls with aggregate delta Δ and gamma Γ holds +Δ shares, and for a price move dS must buy approximately Γ·dS more shares. When dealers are net **short gamma** (short the calls retail is buying), hedging is *pro-cyclical* -- they buy as price rises and sell as it falls, amplifying moves. When net **long gamma**, hedging is counter-cyclical and dampens moves. See [[dealer-gamma-positioning]].

## Key Conditions

- Large open interest in call options relative to the stock's [[float]]
- Concentrated call buying in near-term, out-of-the-money strikes
- Low float and limited share availability
- Often occurs alongside a [[short-squeeze]], amplifying the effect

## Notable Examples

- **GameStop (January 2021)** - Massive call option buying by retail traders forced dealer hedging that compounded the [[short-squeeze]]
- **AMC (June 2021)** - Similar dynamics with heavy call option activity driving dealer buying

## Trading Relevance

Gamma squeezes produce extreme, non-linear price moves that defy fundamental valuation. They are short-lived and collapse rapidly when the feedback loop breaks (options expire, traders sell, or implied volatility spikes enough to deter new call buying). Trading these events is extremely risky -- the reversal can be as violent as the squeeze itself. Practitioners track aggregate dealer gamma exposure (GEX) to gauge whether dealer hedging will amplify or dampen moves around a given price/expiry, and watch the largest open-interest strikes ("gamma walls") that can act as magnets or pinning levels into expiration. See [[dealer-gamma-positioning]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/quant/gex` — gamma exposure: MM inventory + liquidation profile (per-coin optional)
- `GET /api/v1/quant/positioning` — trader-type split (market maker / whale / other)

**Historical data:**
- `GET /api/v1/quant/history` — point-in-time quant records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Sources

- Hull, John C. *Options, Futures, and Other Derivatives*, 11th ed. (Pearson, 2021) — delta/gamma hedging mechanics.
- Baltussen, Da, Lammers & Swinkels, "Hedging demand and market intraday momentum," *Journal of Financial Economics* (2021) — dealer hedging flows and price impact.
- SEC, *Staff Report on Equity and Options Market Structure Conditions in Early 2021* (Oct. 2021) — official analysis of the GameStop episode including options activity.
- Squeezemetrics, *The Implied Order Book* / GEX whitepaper — practitioner framework for dealer gamma exposure.
