---
title: "Cosmos / IBC Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["Cosmos Ecosystem Basket", "IBC Basket", "Cosmos Hub Basket", "Interchain Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[alt-season-momentum-gate]]", "[[narrative-position-vol-targeting]]", "[[l1-blockchains-basket]]", "[[interoperability-basket]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Cosmos ecosystem tokens share the IBC interoperability narrative and compete for the same sovereign-chain developer mindshare; ATOM acts as the economic center of the ecosystem while appchain tokens (OSMO, INJ, TIA, DYDX) move on sector-specific catalysts, creating both directional co-movement and within-sector cross-sectional dispersion."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 20000000
crowding_risk: low
expected_sharpe: 0.6
expected_max_drawdown: 0.42
breakeven_cost_bps: 35
kill_criteria: |
  - basket drawdown > 42% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - IBC transaction volume falls > 60% from 90-day average for > 30 consecutive days
---

# Cosmos / IBC Basket (Hyperliquid Basket)

A sector basket of Cosmos ecosystem and IBC-connected chain tokens with active Hyperliquid perpetuals. Cosmos is the "internet of blockchains" — a network of sovereign application-specific chains connected via IBC (Inter-Blockchain Communication). The basket captures the Cosmos cycle: periods when ATOM and ecosystem tokens outperform on interchain narrative momentum.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). Cosmos tokens share IBC activity as a structural driver. Behavioral momentum arises from Cosmos-specific narrative cycles (new appchain launches, IBC expansion to Ethereum, ATOM economic zone narrative).

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Cosmos Hub | ATOM | The IBC hub; economic center of Cosmos ecosystem |
| Osmosis | OSMO | Largest Cosmos DEX; IBC-native AMM |
| Injective | INJ | Finance-focused Cosmos appchain; DeFi + derivatives |
| Celestia | TIA | Data availability Cosmos chain; fastest-growing IBC chain |
| dYdX | DYDX | Moved to Cosmos appchain; perp DEX on Cosmos |
| Axelar | AXL | Cosmos-based cross-chain gateway; IBC bridging |

**Constituent count:** 6. Minimum $2M daily HL perp volume.

## Selection Rule

Constituents must: (1) be a Cosmos SDK chain or IBC-connected protocol; (2) have ≥ $2M daily HL perp volume; (3) have verifiable IBC transaction volume or on-chain activity.

## Weighting Scheme

**Equal-weight**. INJ and TIA are currently higher-momentum within the ecosystem; ATOM is the most liquid but lowest-beta. Equal-weight balances hub exposure with appchain growth.

## Rebalance Cadence

Weekly.

## Regime Character

Distinct from Ethereum and Solana cycles. Cosmos season can occur independently of Solana or Ethereum narrative cycles. Performs when: new IBC integrations are announced, major appchain launches, or when the "sovereign chain" narrative gains traction vs. Ethereum L2 rollup thesis. Weakest when L2 rollup narrative dominates and appchain model is questioned.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long Cosmos when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long Cosmos momentum leaders vs. short laggards
- [[interoperability-basket]] — AXL and cross-chain infrastructure overlaps
- [[narrative-position-vol-targeting]] — Cosmos ecosystem as a sovereign-chain narrative position

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=ATOM&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=ATOM`
- `GET /api/v1/derivatives/open-interest?coin=INJ`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ATOM&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[l1-blockchains-basket]] · [[interoperability-basket]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[alt-season-momentum-gate]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
