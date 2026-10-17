---
title: "Married Put (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, hedging, protective-put, married-put, insurance, defined-risk, derivatives, bitcoin, ethereum]
aliases: ["Crypto Married Put", "Bullet Hedge", "Protected Entry"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[protective-put]]", "[[collar]]", "[[covered-call]]", "[[synthetic-long]]", "[[hedging]]", "[[tail-risk-hedging]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[staking]]", "[[delta]]", "[[theta]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_spot_plus_put
    role: universe
    rule: "Buy spot BTC or ETH and one Deribit put per unit of coin in the same ticket"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied vol served. Put quotes come from Deribit itself."
  - id: put_strike_atm_or_otm
    role: entry
    rule: "Put strike ATM for maximum protection, or 5-15% OTM to cut cost and accept a deductible"
    runnable: partial
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "The strike target follows from spot (oracle_price is a CEX spot composite close to Deribit's index); the listed strikes and put quotes come from Deribit."
  - id: tenor_30_90_dte
    role: entry
    rule: "Tenor 30-90 DTE to cover the intended hold or risk window"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: risk_window_catalyst
    role: entry
    rule: "A new position into an uncertain window: an FOMC print, an unlock or a halving aftermath"
    runnable: partial
    endpoint: /api/v1/event/calendar?window_days=30&symbol={coin}
    field: items[].date
    note: "Macro prints and unlocks are on the calendar (30 days out); the halving is not."
  - id: vol_not_spiking
    role: filter
    rule: "Buy while the vol regime reads compressed or normal; a vol_shock state means insurance is at its most expensive"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "From the page's AI-agent workflow. No history of the per-coin label is served for replay; DVOL itself is items[].dvol on /api/v1/volatility/implied."
  - id: hedge_ratio
    role: sizing
    rule: "One put per unit of coin for full protection; partial hedges of 50-75% cut cost"
    runnable: true
    input: position
  - id: monetize_on_spike
    role: exit
    rule: "If a sharp, high-DVOL selloff drives the put deep ITM, sell it to harvest intrinsic plus vega"
    runnable: partial
    endpoint: /api/v1/volatility/regime/score
    field: composite_score
    note: "The AI workflow's trigger is a spike in the vol-stress composite off baseline; the page gives no size for the spike or for 'deep ITM'."
  - id: tail_building_watch
    role: exit
    rule: "Cascade activity and stretched funding flag the left tail building: the moment to monetize a deep-ITM put"
    runnable: partial
    endpoint: /api/v1/market-intelligence/squeeze-alerts?symbol={coin}&include_quiet=true
    field: alerts[].direction
    note: "A triggered long_flush alert is the cascade read; funding is binance.current_rate on /api/v1/derivatives/funding-rates?coin={coin}. The page gives no thresholds."
  - id: roll_up_after_rally
    role: exit
    rule: "After a rally, roll the put to a higher strike to lock in a new floor (or sell a call to convert into a collar)"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "The page gives no rally size that triggers the roll."
  - id: no_reflexive_roll
    role: exit
    rule: "Let the put expire and re-underwrite only if protection is still needed; do not roll a catalyst hedge reflexively"
    runnable: true
    input: position
---

# Married Put (Crypto)

## Overview

A married put pairs a **newly established** long spot [[bitcoin|BTC]]/[[ethereum|ETH]] position with a put bought **at the same time** — the coin and the put are "married" at inception. It functions as insurance with a known deductible: the put guarantees a minimum exit price, capping the maximum loss at (spot entry − put strike) + [[premium]] paid, while upside stays **unlimited**. It is the same downside structure as the [[protective-put|protective put]]; the distinction is timing and intent — the married put is a *protected entry* (buy the coin and its insurance together), whereas the protective put is typically *added later* to an existing holding. This page focuses on the entry-timing use; see [[protective-put]] for systematic rolling, monetization, and the premium-drag critique.

Establishing coin and put together is attractive in crypto precisely because entry timing is treacherous: 24/7 markets, weekend gaps, and fat left tails mean a new position can be down 20% before you would otherwise react. The married put lets a trader take a bullish position through a known-risky window with a hard, pre-set floor.

## Construction

1. **Buy spot** BTC/ETH and **buy 1 put per unit of coin** on [[deribit]] in the same order ticket / block.
2. **Strike:** ATM for maximum protection (expensive in crypto's high [[implied-volatility|IV]]), or 5-15% OTM to cut cost and accept a deductible.
3. **Tenor:** 30-90 DTE to cover the intended hold/risk window; longer-dated for multi-month coverage.
4. Prefer **USDC-margined (linear)** puts for a clean USD floor. Enter when DVOL is not spiking — buying insurance after a vol spike overpays.

## Payoff & breakevens

The married put has the payoff of a **long call**: floored downside, full upside above breakeven.

| Point | Value |
|---|---|
| **Max loss** | (Spot entry − put strike) + premium paid |
| **Breakeven** | Spot entry + premium paid |
| **Max profit** | Unlimited (coin can rise; put expires worthless) |
| **Floor** | Put strike − premium (effective worst-case exit) |

## Greeks profile

Net of long coin + long put:

| Greek | Sign | Note |
|---|---|---|
| [[delta]] | Positive, < 1.0 | Long coin trimmed by the long put's negative delta; falls toward the floor |
| [[gamma]] | Positive | The put's convexity — protection accelerates in a fast, deep drop |
| [[theta]] | Negative | The daily insurance cost; the put bleeds if spot holds or rises |
| [[vega]] | Positive | The put gains as DVOL rises (typically in a selloff) — a second crash payoff that lets the put be monetized on a vol spike |

## Market view / when to use

- **Bullish long-term** on the coin but taking a **new position into an uncertain window** (a fresh allocation ahead of an FOMC print, an unlock, or a halving aftermath).
- You want a **hard floor from day one** rather than a mental stop that a weekend gap can jump.
- DVOL is not elevated, so the insurance is affordable.
- You prefer unlimited upside over the capped-upside [[collar]] and are willing to pay the premium for it.

## Adjustments & management

- **Monetize on a spike:** if a sharp, high-DVOL selloff drives the put deep ITM, sell it to harvest intrinsic + vega rather than riding it back down in a recovery.
- **Roll down after a rally** to a higher strike to lock in gains as a new floor (or convert to a [[collar]] by selling a call to offset the next put).
- **Let it expire** and re-underwrite only if you still need protection — do not roll a catalyst hedge reflexively.
- **Sizing:** one put per unit of coin for full protection; partial hedges (50-75%) cut cost.

## Crypto specifics

- **Protected entry on spot BTC/ETH or via Deribit.** Buy the coin and the Deribit put together; on-chain, some structured-product vaults offer principal-protected entries with a similar shape.
- **Cash settlement, no early assignment.** Deribit puts are European, cash-settled — if spot is below the strike at expiry the put pays cash (strike − index), which offsets your spot loss; you **keep the coins** (and any staked position). No early [[assignment]] to manage. (BTC-ETF puts are American-style and physically settled — different mechanics.)
- **Inverse vs linear settlement.** USDC-margined puts give a clean USD floor; coin-margined (inverse) puts pay in coin and are non-linear in USD (the payoff and collateral both move with spot).
- **DVOL makes insurance dear.** Crypto puts cost far more than equity puts (high IV), so the deductible tradeoff matters more — most married-put buyers use OTM strikes.
- **24/7 gap risk is the whole point.** A hard floor set at entry is more valuable in crypto than equities precisely because a devastating move can arrive on a weekend with no session close.
- **No [[section-1256-contracts|§1256]].** Ordinary treatment; the put's cost and any monetization are ordinary capital events.
- **Perp/staking interaction.** An alternative "floor" is to short the [[funding-rate|perp]] against the coin, but that also caps upside (a synthetic reduction) and pays/collects funding — the married put preserves the full upside the perp-short gives away. On staked ETH the put hedges price while **staking yield** continues to accrue.

## Risks

- **Premium drag:** the put is a direct cost that erodes returns if the coin rises or stays flat.
- **Theta bleed:** time works against the long put every day.
- **Expensive in high DVOL:** protection is priciest exactly when fear is highest.
- **Failure to monetize:** holding an ITM put through a V-shaped recovery gives the hedge profit back.
- **Coin-margined non-linearity** if inverse puts are used.

## Worked crypto example

**Setup (illustrative).** Take a new 2 BTC position at $68,000 into a 60-day window, insured from day one.

- **Buy** 2 BTC spot at $68,000
- **Buy** 2 × $61,000 puts (60 DTE) at ~$3,400 each → $6,800 total (5.0% of the $136,000 position)

| Outcome at expiry | Net P&L |
|---|---|
| BTC to $50,000 | Put pays (61,000 − 50,000) × 2 = $22,000; spot loses $36,000 → net **−$20,800** (floored; max loss ≈ (68k−61k+3.4k)×2 = $20,800) |
| BTC at $68,000 | Put expires worthless → **−$6,800** (the insurance cost) |
| BTC to $85,000 | Put expires worthless; spot gains $34,000 → net **+$27,200** (full upside minus premium) |

Max loss is capped at $20,800 (≈15% of the position) no matter how far BTC falls; upside is uncapped above the $71,400 breakeven.

## Getting the Data (CryptoDataAPI)

IV/DVOL and skew come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the vol-regime, funding, and liquidation context that tells you when insurance is cheap and when a tail is building.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (buy insurance when compressed, not into a vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (left-tail early warning)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew and leverage read)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for floor/breakeven tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this overlay end-to-end (put pricing itself stays on Deribit / [[greeks-live]]):

- **Entry timing** — `GET /api/v1/volatility/regime` — marry the coin and put while the read is `compressed`/`normal`; a `vol_shock` state means insurance is at its most expensive.
- **Tail watch** — `GET /api/v1/market-intelligence/liquidations` + `GET /api/v1/derivatives/funding-rates?coin=BTC` — cascade activity and stretched funding flag the left tail building, i.e. the moment to monetize a deep-ITM put rather than ride it back through a recovery.
- **Monetization trigger** — `GET /api/v1/volatility/regime/score` — a spike off baseline marks the vega payoff window for selling the put.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) to replay floor/breakeven outcomes across strike/tenor grids; CDA holds no historical options chains, so premium history must come from Deribit.
- **Tips** — poll the cached `GET /api/v1/daily` bundle hourly for vol/funding/liquidation context in one call instead of four separate requests.

## Related

- [[protective-put]] — the same downside structure added to an existing holding, with rolling/monetization and the premium-drag critique
- [[collar]] — offsets the put's cost by selling a call (caps upside)
- [[covered-call]] — the opposite posture (income for capped upside)
- [[synthetic-long]] — an unhedged, capital-efficient way to be long
- [[hedging]] / [[tail-risk-hedging]] — the broader protection discipline
- [[funding-rate]] — the perp-short alternative to a put floor
- [[staking]] — yield that continues while the coin is insured
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin-margined vs USDC-margined puts, DVOL
- [[protective-put]] — companion page covering systematic rolling, monetization, and the Israelov-style premium-drag evidence
