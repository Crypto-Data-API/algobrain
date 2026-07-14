---
title: "The Wheel Strategy (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, income, premium-selling, cash-secured-put, covered-call, derivatives, bitcoin, ethereum]
aliases: ["The Wheel", "Options Wheel", "Crypto Wheel", "Triple Income Strategy"]
strategy_type: hybrid
timeframe: swing|position
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[cash-secured-put]]", "[[options-selling]]", "[[crypto-options-volatility-selling]]", "[[collar]]", "[[iron-condor]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[staking]]", "[[theta]]", "[[delta]]", "[[trade-repair-and-rolling]]", "[[cryptodataapi]]"]
---

# The Wheel Strategy (Crypto)

## Overview

The Wheel is a systematic [[options]] income cycle that alternates between selling [[cash-secured-put|cash-secured puts]] and [[covered-call|covered calls]] on coins the trader is willing to own — re-scoped here from equities to crypto ([[bitcoin|BTC]]/[[ethereum|ETH]] on [[deribit]], or via on-chain vaults and BTC-ETF options). It begins by selling a cash-secured put (collateralized in USDC). If the put expires OTM, the trader keeps the premium and sells another. If the put finishes ITM, the trader effectively acquires the coin at the strike (cost basis reduced by the premium collected), then sells covered calls against the coin until it is capped away, and the cycle repeats.

The Wheel suits fundamentally durable assets the trader is happy to hold long-term (BTC, ETH). It converts a buy-and-hold posture into a premium engine, generating income from put premiums, call premiums, and — for ETH — [[staking|staking yield]] while holding coin. Crypto's high [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] makes both premium streams far richer than the equity wheel, at the cost of a genuinely fatter tail. It is cash-intensive and lower-return-but-consistent, punctuated by the risk of being caught holding a coin through a deep decline.

## Construction

**Phase 1 — sell cash-secured puts.** Reserve USDC to cover the strike, sell an OTM put (delta 0.20-0.30, 21-45 DTE) at a level you consider a fair entry.

**Phase 2 — sell covered calls.** Once holding the coin, sell an OTM call (delta 0.25-0.35) at or above your effective cost basis. Repeat each cycle until the coin is capped away, then return to Phase 1.

Because Deribit options are **cash-settled European** (no delivery), the "assignment → own coin" transition is not automatic — see *Crypto specifics* for how the crypto wheel is actually operated (manual spot conversion, physically-settled ETF options, or on-chain vaults).

## Payoff & breakevens

Each leg is a short-premium position; the wheel is their sequence.

| Leg | Breakeven | Max profit | Max loss |
|---|---|---|---|
| Cash-secured put | Strike − premium | Premium (put expires OTM) | Strike − premium (coin → 0) |
| Covered call | Coin cost − premium | (Strike − cost) + premium | Coin cost − premium (coin → 0) |

The full-cycle economics: buy low (put premium discounts entry), collect call premium while held, sell higher (call strike ≥ cost). The dominant risk in both legs is simply owning the coin through a drawdown.

## Greeks profile

- **Phase 1 (short put):** delta positive (long-ish exposure), theta positive, vega negative, gamma negative near the strike.
- **Phase 2 (covered call):** delta positive but < 1.0, theta positive, vega negative, gamma negative near the strike.

Across the whole cycle the wheel is persistently **long delta + short vega + long theta** — a leveraged-long-with-income posture, harvesting the crypto [[variance-risk-premium|variance risk premium]] on both wings.

## Market view / when to use

- **Neutral-to-bullish** on BTC/ETH; you genuinely want to accumulate at your put strikes.
- DVOL elevated so both put and call premiums are rich.
- You have the USDC to fully cash-secure the put (no leverage) and can tolerate being assigned into a falling market.

## Adjustments & management

- **Roll a tested put down and out** (buy back, sell a lower-strike, later-dated put for a net credit) when spot approaches the strike and the thesis is intact.
- **Manage underwater coin:** sell calls at or above cost basis, never below, to avoid locking in the decline; wait for premium-funded recovery.
- **Manage before the last week:** with 24/7 markets and no session close, close/roll ATM legs ~7-14 DTE to avoid the hottest gamma on a weekend gap.
- **Abandon the wheel** if the asset's thesis breaks — do not keep selling calls into a structural collapse (the 2022 LUNA lesson).
- **Sizing:** diversify across BTC and ETH; cap any single wheel to a sensible book weight and keep full cash backing on the put leg.

## Crypto specifics

- **Assignment is cash, not delivery.** On [[deribit]], a cash-secured put that finishes ITM settles in cash (strike − index); it does **not** deliver coin. To run a true wheel you either (a) buy spot at the strike level when the put settles ITM, then sell calls against that spot; (b) use **physically-settled BTC-ETF options** (American-style, deliver ETF shares — the closest analogue to the equity wheel); or (c) use **on-chain put-selling / covered-call vaults** that automate the coin acquisition and call-writing. There is **no early assignment** on Deribit's European options.
- **Inverse vs linear settlement.** Cash-secure and write in **USDC (linear)** for clean USD P&L, or use **coin-margined (inverse)** contracts to keep collateral in coin (quanto-like non-linearity). The put leg is naturally USDC-collateralized (you are reserving fiat-equivalent to buy).
- **DVOL-rich premium.** Crypto's high [[implied-volatility|IV]] makes wheel yields far exceed the equity wheel, but the same IV signals the fatter tail you are underwriting on the put leg.
- **24/7 markets.** Continuous theta and continuous gap risk; weekend liquidity is thin. No overnight "market-closed" gap — the gap can come at any hour.
- **No [[section-1256-contracts|§1256]].** Every put and call is an ordinary short-term capital event; frequent wheeling generates heavy, unfavorable tax reporting versus a §1256 SPX program.
- **Perp-funding interaction.** Positive [[funding-rate|funding]] firms call skew (richer Phase-2 premium) and signals crowded leverage; the wheel's short-put leg competes with simply earning funding via [[cash-and-carry]].
- **Staking-yield interaction.** In Phase 2 on ETH, stack **staking yield + call premium** on the held coin; cash settlement means locked staked ETH never has to be delivered.

## Risks

- **Bag-holding:** assigned on the put, then the coin keeps falling 30-70% — the defining failure. Months of small call premiums against a large unrealized loss.
- **Capped upside in Phase 2:** a coin that rips after you are holding it gets capped away.
- **No hedge:** the wheel offers no protection against a catastrophic decline — it is long the coin throughout.
- **Capital intensity:** full cash-securing locks up USDC.
- **Venue concentration & margin spirals** on Deribit during vol shocks.

## Worked crypto example

**Setup (illustrative).** ETH spot $3,050, DVOL rich.
1. **Phase 1:** sell a 35-DTE $2,800 put (~0.25 delta) for $90; reserve $2,800 USDC.
2. ETH dips to $2,760 at expiry — put settles ITM. You buy 1 ETH spot near $2,800; effective cost basis $2,800 − $90 = **$2,710**.
3. **Phase 2:** sell a 30-DTE $3,000 call for $85. Adjusted basis $2,710 − $85 = **$2,625**.
4. ETH recovers to $3,050; call settles ITM, coin effectively capped at $3,000. Cycle profit ≈ ($3,000 − $2,710) + $85 = **$375/ETH** (~13% on deployed capital) before fees; add ETH staking yield if the coin was staked in Phase 2.
5. Return to Phase 1 and repeat.

## Getting the Data (CryptoDataAPI)

DVOL and the IV surface come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the flow, regime, and funding context for strike selection and cycle timing.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (strike-selection context)
- `GET /api/v1/volatility/regime` — per-asset vol regime for entry gating
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (call-skew and leverage read)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for cost-basis and realized-vol tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

## Related

- [[covered-call]] — Phase 2 of the wheel in isolation
- [[cash-secured-put]] — Phase 1 of the wheel in isolation
- [[options-selling]] — the premium-selling family
- [[crypto-options-volatility-selling]] — the systematic short-vol book behind the premiums
- [[collar]] — add a protective put to cap the wheel's tail risk
- [[iron-condor]] — a defined-risk alternative that does not require holding coin
- [[trade-repair-and-rolling]] — the rolling framework for both phases
- [[funding-rate]] — the perp linkage shaping crypto skew
- [[staking]] — stackable yield in Phase 2
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement (no delivery/early assignment), coin-margined vs USDC-margined mechanics, DVOL
- [[crypto-options-volatility-selling]] — the crypto variance-risk-premium engine both wheel legs harvest
