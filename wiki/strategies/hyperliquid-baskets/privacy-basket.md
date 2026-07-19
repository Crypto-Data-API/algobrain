---
title: "Privacy Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime, privacy]
aliases: ["Privacy Coin Basket", "Privacy Token Sector Basket", "Anonymity Crypto Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[regulatory-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "Privacy tokens co-move on regulatory cycle events (exchange delistings, FATF guidance changes, OFAC actions) and on counter-surveillance demand spikes; the basket captures the regulatory-risk narrative cycle and within-sector momentum when privacy demand rises, while managing the elevated delisting risk that is the primary threat to this sector."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 10000000
crowding_risk: low
expected_sharpe: 0.5
expected_max_drawdown: 0.45
breakeven_cost_bps: 40
kill_criteria: |
  - basket drawdown > 45% from peak on a rolling 6-month basis
  - any constituent receives OFAC designation or major exchange delisting → immediate remove that constituent and halve basket exposure
  - rolling 6-month Sharpe < -0.2
---

# Privacy Basket (Hyperliquid Basket)

A sector basket of privacy-focused cryptocurrency tokens with active Hyperliquid perpetuals. Captures the privacy-coin narrative cycle — driven by regulatory developments, surveillance-state events, and demand for financial anonymity. The basket carries elevated regulatory risk compared to all other sector baskets and must be sized accordingly.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + informational** (see [[edge-taxonomy]]). Privacy tokens react sharply to regulatory events (OFAC sanctions, exchange delistings, FATF travel rule tightening) in both directions — negative on crackdown news, positive on regulatory ambiguity lifting or counter-surveillance demand spikes. These events are observable (news-driven) and create short-term directional momentum.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Monero | XMR | The canonical privacy coin; highest privacy guarantees; delisting-sensitive |
| Zcash | ZEC | Optional shielded transactions; Grayscale product |
| Secret Network | SCRT | Privacy for smart contracts; programmable privacy narrative |
| Oasis Network | ROSE | Confidential compute / privacy L1 |
| Dusk Network | DUSK | Regulatory-compliant privacy; institutional angle |

**Constituent count:** 5. **Important caveat:** XMR and ZEC are delisted from most regulated exchanges. Verify Hyperliquid perp availability before deployment — HL perp listings for privacy coins are subject to sudden removal. Check `/api/v1/hyperliquid/meta` before every weekly screen.

## Selection Rule

Constituents must: (1) have an active HL perpetual at screen time (verify weekly — do not assume); (2) have a primary design objective of financial privacy or confidential computation; (3) ≥ $1M daily HL perp volume (lower threshold given the thin nature of this sector on HL).

## Weighting Scheme

**Equal-weight**. Given regulatory risk, no single constituent should exceed 25% of basket notional to cap headline-event concentration risk.

## Rebalance Cadence

Weekly. Immediate rebalance on any major regulatory action (OFAC designation, major exchange delisting, FATF guidance update) affecting any constituent.

## Regime Character

Counter-cyclical to regulatory clarity narratives. Performs when: crypto regulation perceived as uncertain or worsening (demand for privacy protection); privacy-adjacent tech narratives (ZK proofs, confidential compute) gain traction; exchange crackdown events create speculative demand. Weakest during crypto-regulation-positive periods (ETF approvals, regulatory clarity).

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long privacy sector in regulatory-uncertainty / counter-surveillance regimes
- [[cross-sectional-relative-value]] — long privacy leaders vs. short laggards within the sector
- [[narrative-position-vol-targeting]] — privacy as a distinct narrative overlay
- [[regulatory-arbitrage]] — privacy tokens as a regulatory-friction expression

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/meta` — verify current HL perp listings for privacy tokens before each screen
- `GET /api/v1/hyperliquid/candles?coin=ZEC&interval=1h&limit=168` — per constituent (where listed)
- `GET /api/v1/derivatives/funding-rates?coin=ZEC`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/meta"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[regulatory-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
