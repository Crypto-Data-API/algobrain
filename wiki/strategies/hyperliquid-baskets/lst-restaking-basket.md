---
title: "LST / Restaking Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, defi, market-regime]
aliases: ["Liquid Staking Basket", "LST Basket", "Restaking Token Basket", "LRT Basket", "Staking Derivatives Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[lst-depeg-arbitrage]]", "[[staking-yield-arbitrage]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "LST and restaking tokens share an Ethereum-staking yield narrative and compete for the same staked ETH capital; within-sector momentum tracks which protocols are winning the yield-maximisation race, creating cross-sectional dispersion while the sector as a whole co-moves with the Ethereum staking rate and re-staking narrative cycle."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 10000
capacity_usd: 25000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.38
breakeven_cost_bps: 30
kill_criteria: |
  - basket drawdown > 38% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - Ethereum staking APY falls below 2% for > 60 consecutive days (structural yield narrative collapse)
  - any constituent suffers a smart-contract exploit exceeding 5% of TVL → remove immediately
---

# LST / Restaking Basket (Hyperliquid Basket)

A sector basket of liquid staking token and restaking protocol tokens with active Hyperliquid perpetuals. Captures the Ethereum staking yield and restaking narrative — the "yield on yield" story that emerged post-Merge and expanded through EigenLayer and competing restaking protocols.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). LST tokens have structural support from Ethereum staking yield (holders earn ETH staking returns), but price momentum is driven by narrative rotation around which protocol wins the re-staking market. The structural yield anchor provides a floor; the behavioral narrative cycle creates momentum dispersion within the sector.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Lido DAO | LDO | Dominant liquid staking protocol; Lido stETH issuer |
| Rocket Pool | RPL | Decentralised staking alternative; governance token |
| Ether.fi | ETHFI | Largest liquid restaking protocol; EigenLayer native |
| Renzo | REZ | Liquid restaking; cross-chain restaking narrative |
| SSV Network | SSV | DVT-based staking; decentralised validator infrastructure |
| Swell Network | SWEL | Liquid staking and restaking; multi-protocol approach |
| Kelp DAO | KEP | Liquid restaking aggregator |

**Constituent count:** 7. Minimum $2M daily HL perp volume.

## Selection Rule

Constituents must: (1) be a liquid staking protocol (issues a derivative representing staked ETH or other PoS assets) OR a restaking protocol (builds additional economic security layers on staked ETH); (2) have verifiable on-chain TVL and staking mechanics; (3) ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. LDO is significantly larger than other constituents; consider vol-weighting to reduce LDO concentration and increase exposure to smaller restaking protocols where the cycle alpha is higher.

## Rebalance Cadence

Weekly. Smart-contract exploit monitoring is continuous; remove any constituent immediately on a material exploit.

## Regime Character

Performs in Ethereum-bullish, yield-positive regimes. Correlated with ETH price and Ethereum staking APY. The restaking narrative (LRT premium over LST) creates within-sector dispersion that cross-sectional strategies harvest. Weakest in bear markets and when re-staking narratives face regulatory scrutiny (SEC classification of staking tokens as securities).

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long LST/restaking when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long restaking leaders (ETHFI, REZ) vs. long-established LST (LDO) as a sector-rotation pair
- [[lst-depeg-arbitrage]] — monitors constituent depeg events; the basket provides the sector context
- [[staking-yield-arbitrage]] — yield context for the constituent tokens
- [[narrative-position-vol-targeting]] — LST/restaking as a structural Ethereum narrative

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=LDO&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=LDO`
- `GET /api/v1/derivatives/open-interest?coin=ETHFI`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=LDO&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[lst-depeg-arbitrage]] · [[staking-yield-arbitrage]] · [[narrative-position-vol-targeting]] · [[alt-season-momentum-gate]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
