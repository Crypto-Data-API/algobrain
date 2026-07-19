---
title: "AI Tokens Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime, ai-trading]
aliases: ["AI Sector Basket", "AI Narrative Basket", "AI Agent Tokens Basket", "Artificial Intelligence Crypto Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[alt-season-momentum-gate]]", "[[narrative-position-vol-targeting]]", "[[ai-agent-tokens]]", "[[bittensor-subnet-rotation]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "AI token prices are driven by narrative velocity around real-world AI breakthroughs (model releases, GPU allocation news, agent deployment milestones); these narrative shocks are observable before fully priced, and the sector co-moves strongly during AI hype cycles — creating momentum entries with defined narrative-reversal exit signals."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data, social-volume]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.7
expected_max_drawdown: 0.45
breakeven_cost_bps: 35
kill_criteria: |
  - basket drawdown > 45% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - AI narrative sentiment index falls below 30-day MA for > 20 consecutive days (narrative cycle end)
---

# AI Tokens Basket (Hyperliquid Basket)

A sector basket of artificial intelligence and AI-agent crypto tokens with active Hyperliquid perpetuals. Targets the AI narrative cycle — correlated with real-world AI hype events (major model releases, GPU supply stories, agent deployment milestones) — with exposure to both infrastructure AI tokens (compute, data) and AI-agent protocol tokens.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + informational** (see [[edge-taxonomy]]). AI tokens are highly narrative-driven; price reactions to real-world AI events (model launches, OpenAI announcements, GPU shortages) are observable before fully priced in the crypto market, creating momentum entries with 3–14 day persistence.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Bittensor | TAO | Decentralised ML network; the "AI L1"; see [[bittensor-subnet-rotation]] |
| Fetch.ai | FET | AI agent infrastructure; Artificial Superintelligence Alliance |
| Render | RNDR | Decentralised GPU compute; direct AI compute narrative |
| Worldcoin | WLD | AI identity verification; Sam Altman association |
| Akash Network | AKT | Decentralised cloud / GPU rental; AI compute infrastructure |
| The Graph | GRT | Data indexing for AI applications; established infrastructure |
| Artificial Superintelligence Alliance | ASI | FET/AGIX/OCEAN merger token; explicit ASI narrative |
| io.net | IO | GPU compute marketplace; direct AI inference narrative |

**Constituent count:** 8. High narrative-volatility assets; require $2M minimum daily HL volume (lower than sector default to maintain coverage).

## Selection Rule

Constituents must: (1) have ≥ $2M daily HL perp volume; (2) have an explicit AI or ML use case in the protocol design (not just a token name containing "AI"); (3) maintain > $100M market cap (filter out micro-cap AI meme tokens — route those to meme-coin-cycle basket instead).

## Weighting Scheme

**Equal-weight** across active constituents. The sector is high-dispersion; vol-weighting may reduce concentration in TAO (which is often 3–5× more volatile than other constituents). Review monthly.

## Rebalance Cadence

Weekly. Given the high narrative velocity of AI tokens, trigger an out-of-cycle rebalance if any constituent's 7-day return exceeds ±40% (narrative spike / crash).

## Regime Character

Strongest during AI hype cycles (major model releases, GPU allocation news, crypto AI narrative revival). Weakest during "crypto winter" macro risk-off and during AI regulation / model-release disappointment periods. Highly correlated with broader tech / Nasdaq sentiment (see [[crypto-beta-rotation]]).

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long AI tokens in the highest-momentum sector regime
- [[cross-sectional-relative-value]] — long AI winners (TAO, RNDR momentum) vs. short laggards
- [[narrative-position-vol-targeting]] — AI narrative exposure with vol-capped position
- [[alt-season-momentum-gate]] — AI tokens are a first-rotation alt-season target
- [[bittensor-subnet-rotation]] — TAO specifically; subnet rotation uses this basket as a BTC-beta hedge

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=TAO&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=TAO`
- `GET /api/v1/derivatives/open-interest?coin=TAO`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=TAO&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[alt-season-momentum-gate]] · [[ai-agent-tokens]] · [[bittensor-subnet-rotation]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
