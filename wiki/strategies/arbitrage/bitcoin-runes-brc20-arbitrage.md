---
title: "Bitcoin Runes / BRC-20 Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-10
status: good
tags: [arbitrage, crypto, bitcoin, nft]
aliases: ["BRC-20 Sniping", "Runes Arb", "Bitcoin Token Arbitrage", "Ordinals Trading"]
related: ["[[nft-arbitrage]]", "[[bitcoin-ordinals]]", "[[fork-airdrop-triangulation]]", "[[memecoin-sniping]]"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto, bitcoin]
complexity: advanced
backtest_status: live
edge_source: [structural, latency, informational]
edge_mechanism: "Bitcoin Runes (April 2024) and BRC-20 (March 2023) introduced fungible tokens to Bitcoin via two competing standards. Cross-marketplace arbitrage (UniSat, OKX, Magic Eden, Ordinals Wallet, Best in Slot) and cross-standard triangulation (Runes vs BRC-20 vs wrapped-on-Ethereum versions) opened a new fragmented market analogous to early Ethereum DEX arb."
data_required: [marketplace-orderbooks, mempool-monitoring, indexer-feeds, mint-event-feeds]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 1.5
expected_max_drawdown: 0.4
breakeven_cost_bps: 200
decay_evidence: "BRC-20 TVL peaked April 2024 around halving; declined sharply 2024 H2 as Runes launched. Runes peaked May 2024; both categories declined to ~$1B combined by Q1 2025."
---

# Bitcoin Runes / BRC-20 Arbitrage

Trading the **fungible-token markets on Bitcoin** introduced by two competing standards:

- **BRC-20 (March 2023, Domo)** — token standard built on top of Ordinals via JSON inscriptions in transaction witnesses.
- **Runes (April 20, 2024, Casey Rodarmor)** — UTXO-native token standard launched at the Bitcoin halving block.

Both standards spawned thousands of memecoin-style tokens with **fragmented marketplace liquidity** (UniSat, OKX Web3, Magic Eden, Ordinals Wallet, Best in Slot, Saturn) and complex **cross-standard triangulation** (Runes vs BRC-20 vs wrapped-on-Ethereum versions). For arbitrageurs, the era from March 2023 through mid-2024 generated **the largest new arbitrage surface since DeFi Summer 2020**.

## Edge Source

**Structural** + **latency** + **informational**.

- **Structural:** Bitcoin's UTXO model + lack of native AMMs forces all token trades through orderbook marketplaces. Each marketplace has its own liquidity, fees, and indexer.
- **Latency:** New mints on Runes appear in mempool seconds before confirmation; snipers pre-position.
- **Informational:** Runes etching (creation) decisions, Twitter/X social signals, BTC halving date drove flow.

## Why This Edge Exists

The Bitcoin token-standards landscape:

| Standard | Launched | Mechanism | Market Cap Peak |
|----------|----------|-----------|-----------------|
| **Ordinals (NFTs)** | Jan 2023 | Inscription on satoshis | $5B (Mar 2024) |
| **BRC-20** | Mar 2023 | JSON inscriptions | $2B (Apr 2024) |
| **Runes** | Apr 20 2024 | UTXO-native | $1B (May 2024) |
| **Atomicals (ARC-20)** | Sep 2023 | Alternative to BRC-20 | $200M peak |
| **Stamps (SRC-20)** | Mar 2023 | Bitcoin Stamps | $50M peak |

Each standard creates fungible tokens — but with different protocols, indexers, and marketplace support.

Marketplace fragmentation:
- **UniSat** — dominant Chinese-language marketplace; first to support BRC-20 and Runes.
- **Magic Eden** — major US marketplace; supports both standards.
- **OKX Web3** — exchange-affiliated marketplace.
- **Ordinals Wallet** — Bitcoin-native wallet with marketplace.
- **Best in Slot** — rare Ordinals + token marketplace.

Same token traded at different prices on different marketplaces for hours-days. Same project sometimes existed as both BRC-20 and Runes (e.g., DOG, PUPS, RSIC) creating cross-standard triangulation.

Counterparty: latency-disadvantaged retail holders; users stuck on one marketplace; speculative buyers chasing mints.

## Null Hypothesis

Under the null, observed cross-marketplace spreads are not free money — they exactly compensate the costs of capturing them: 10-60 minute Bitcoin confirmation lag, on-chain transfer fees (which spike to $50-200+ per transaction in exactly the high-activity windows when spreads are widest), and adverse selection (the spread that survives until your transfer confirms is the one where the rich-side bid was already stale or pulled). For mint sniping, the null is that mint allocations have zero expected markup once the full universe — including the thousands of spam mints that never trade — is counted, so apparent profitability is survivorship bias on ORDI/SATS-class winners. The test: paper-trade the *complete* launch universe with realistic confirmation delay and fee-rate-at-time-of-trade, not end-of-day quotes; under no-edge, gross spread capture minus fees and failed-transfer losses nets to ≤ 0. Indexer-discrepancy "arbs" have an additional null: the discrepancy reflects genuine state ambiguity, and the trade is simply buying tokens whose validity is disputed.

## Variants

| Variant | Description | Holding Period |
|---------|-------------|----------------|
| **Mint sniping** | Detect new BRC-20/Runes mints; race to claim allocation | Seconds-minutes |
| **Cross-marketplace arb** | Same token, different prices on different marketplaces | Hours-days |
| **Cross-standard triangulation** | Same project as BRC-20 + Runes; arb between standards | Days-weeks |
| **Wrapped-version arb** | Runes/BRC-20 wrapped on Ethereum (e.g. Multibit bridges); cross-chain arb | Hours-days |
| **Halving-event sniping** | Pre-position for Runes etching at halving block 840,000 | One-time event |
| **Indexer-discrepancy arb** | Different indexers (UniSat, OrdScan, OKLink) sometimes show different token state; trade the gap | Minutes-hours |

## Rules

1. **Marketplace coverage:** API integration with UniSat, Magic Eden, OKX Web3, Ordinals Wallet, Best in Slot.
2. **Mempool monitoring:** Bitcoin mempool feeds (Mempool.space, custom node) for new mint detection.
3. **Indexer parity check:** verify token state across multiple indexers; trade discrepancies.
4. **Mint participation:** automated bidding for new mint allocations.
5. **Cross-marketplace execution:** route trades to cheapest venue.
6. **Position sizing:** small per-token (these are illiquid memecoins); scale across many positions.

## Implementation Pseudocode

```python
on new_mint_event(token_data):
    if mint_eligible(token_data):
        bid_for_allocation(token_data, max_size=$500)
    
on marketplace_price_update(token):
    prices = {mkt: get_price(token, mkt) for mkt in [unisat, magic_eden, okx, ord_wallet]}
    spread = max(prices.values()) - min(prices.values())
    if spread / max(prices.values()) > 200bp:
        cheap_mkt = min(prices, key=prices.get)
        rich_mkt = max(prices, key=prices.get)
        buy(token, cheap_mkt, sized_for_liquidity)
        # transfer + sell on rich market (10-30 min Bitcoin confirmation lag)
        transfer_to(rich_mkt)
        sell(token, rich_mkt)
```

## Indicators / Data Used

- Mempool.space (Bitcoin mempool feed).
- UniSat / Magic Eden / OKX Web3 APIs.
- BestInSlot rare-Ordinals tracker.
- OrdScan, OKLink indexers.
- Discord/Telegram channels for new mint announcements.

## Example Trades

**ORDI launch (March 2023).** First major BRC-20 token. Launched at sub-$1; rallied to $80+ within about a year (the November 2023 Binance listing was the major catalyst; peak ~$96 in March 2024). Early UniSat snipers captured 100x. Cross-marketplace arb (UniSat vs OKX) had 5-15% spreads for weeks.

**SATS BRC-20 (mid-2023).** Sat-denominated meme; rallied 50x in 3 months. Cross-marketplace + cross-indexer arbs frequent.

**Runes launch April 20, 2024 (Bitcoin halving).** Casey Rodarmor's Runes protocol activated at halving block 840,000, which alone carried ~37.6 BTC (~$2.4M) in fees — the most valuable block ever mined — and Runes generated an estimated $135M+ in transaction fees in its first week, the highest fee period in Bitcoin history. Runes "etching arb" — predicting which Runes would have value vs which were spam — was the day's main game.

**RSIC (RSIC Metaprotocol)** — Rare Ordinals project; both BRC-20 and Runes versions. Cross-standard arb between RSIC variants captured 200-500 bp during peak launch.

**DOG•GO•TO•THE•MOON (Runes)** — Most-traded Rune post-launch. Cross-marketplace arb spreads of 3-8% common in May 2024 launch period.

## Performance Characteristics

Specialist Bitcoin-token arb desks reported 30-150% annualized returns 2023-2024 (concentrated in BRC-20 and Runes launch periods). Sharpe 1.0-1.8. Highly variable; ~70% of token-specific trades lose money, but big winners offset.

## Capacity Limits

Per-trade capacity bound by single-token liquidity (typically $1-50K per trade). Strategy-level capacity ~$50M for top operators.

## What Kills This Strategy

- Bitcoin token-standard adoption stalls (currently in decline 2024 H2-2025).
- Single marketplace consolidation.
- Indexer convergence eliminates discrepancy arb.
- BTC L2 (Stacks, Babylon, Citrea) takes activity.

## Kill Criteria

- BRC-20 + Runes combined market cap below $200M.
- New-token launch frequency drops to <100/week.

## Advantages

- Decoupled from Ethereum DeFi.
- Fragmented marketplaces = persistent arb.
- Bitcoin-native users = different participant base.

## Disadvantages

- Bitcoin block confirmation lag (10-60 min) limits high-frequency arb.
- Most tokens are spam/rugs.
- Marketplace operational risk.

## Sources

- Casey Rodarmor, *Runes Protocol* documentation.
- Domo, *BRC-20 Standard* (March 2023 inception).
- UniSat / Magic Eden API documentation.
- Mempool.space Bitcoin monitoring.
- **YouTube: "Bitcoin Ordinals Explained" by various Bitcoin creators 2023-2024.**
- **YouTube: "Runes Launch Day" coverage by What Bitcoin Did (April 2024).**
- **YouTube: "BRC-20 Sniping Tutorial" series by Solana/Bitcoin crossover educators (2023-2024).**

## Related

[[nft-arbitrage]] · [[bitcoin-ordinals]] · [[fork-airdrop-triangulation]] · [[memecoin-sniping]] · [[liquidity-sniping]] · [[pump-fun-bonding-curve-sniping]]
