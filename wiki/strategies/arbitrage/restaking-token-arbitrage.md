---
title: "Restaking Token Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, defi, ethereum, crypto]
aliases: ["LRT Arbitrage", "Restaking Triangle", "EigenLayer LRT-LST Arb"]
related: ["[[lst-depeg-arbitrage]]", "[[triangular-arbitrage]]", "[[multi-leg-arbitrage]]", "[[crypto-spot-perp-futures-triangle]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [structural, analytical, risk-bearing]
edge_mechanism: "EigenLayer's restaking creates a stack: ETH → LST (stETH/cbETH) → LRT (eETH/ezETH/rsETH/pufETH) → AVS yield. Each layer adds slashing risk and points-farming optionality. Layers depeg from each other when redemption rails differ in latency or when restaking-protocol incentives shift. Triangulation across the LRT stack was highly profitable for specialist desks in 2024-2025."
data_required: [lrt-pool-reserves, eigenlayer-restaking-quotas, lrt-protocol-tvl, points-multiplier-schedules]
min_capital_usd: 100000
capacity_usd: 1000000000
crowding_risk: high
expected_sharpe: 1.5
expected_max_drawdown: 0.3
breakeven_cost_bps: 25
decay_evidence: "Strategy emerged 2024 with EigenLayer launch; matured rapidly. Most pure-arb opportunities compressed by Q2 2024; remaining alpha in points-farming and AVS-specific basis trades."
---

# Restaking Token Arbitrage

The arbitrage strategy emerging from **Ethereum [[restaking]] infrastructure**: triangulating between **ETH, Liquid Staking Tokens (LSTs)** like stETH/cbETH/rETH, **Liquid Restaking Tokens (LRTs)** like eETH (Ether.fi), ezETH (Renzo), rsETH (Kelp), pufETH (Puffer), and the underlying **AVS (Actively Validated Service)** yields they accrue. It is a [[triangular-arbitrage]] / [[multi-leg-arbitrage]] variant where the "legs" are different wrappers of the *same* underlying ETH, related to but distinct from [[lst-depeg-arbitrage]] (which trades the LST-vs-ETH peg). The category barely existed before 2024 — EigenLayer opened restaking deposits in mid-2023 and completed its full mainnet launch (operators + AVSs) in **April 2024** — but by late 2024 had attracted $15B+ TVL and generated outsized arbitrage P&L for sophisticated DeFi traders, concentrated in the Q1-Q2 2024 points-farming boom.

### The restaking stack at a glance

| Layer | Examples | Adds | Redemption rail | Liquid venue |
|-------|----------|------|-----------------|--------------|
| ETH | ETH | base asset | n/a | everywhere |
| LST | stETH, cbETH, rETH | staking yield + slashing | ~1-15 day exit queue | Curve, Balancer |
| LRT | eETH, ezETH, rsETH, pufETH | restaking yield + extra slashing + points | protocol-specific, ~7-30 days | Pendle, Curve, Balancer |
| AVS yield | EigenDA, Eigen rewards, AVS tokens | service rewards | claim-dependent | on-chain |

The further down the stack, the higher the yield, the higher the slashing exposure, and the *slower and more idiosyncratic* the redemption — which is exactly the friction that creates (and limits) the arbitrage.

## Edge Source

**Structural** + **analytical** + **risk-bearing**.

- **Structural:** Each layer of the restaking stack has different liquidity, redemption mechanics, and yield-accrual schedules.
- **Analytical:** Modeling AVS rewards (fluctuating + future), EigenLayer points multipliers (changes weekly), and LRT-protocol token-distribution schedules.
- **Risk-bearing:** Slashing risk compounds across each layer; total slashing exposure can exceed 5% of position.

## Why This Edge Exists

The restaking stack:

```
ETH (32 ETH per validator)
  ↓ stake
LST (stETH/cbETH/rETH) — Lido/Coinbase/Rocket Pool
  ↓ deposit into EigenLayer (restake)
LRT (eETH/ezETH/rsETH/pufETH) — Ether.fi/Renzo/Kelp/Puffer
  ↓ delegate to AVS
AVS yield (EigenDA, Eigen rewards, AVS-specific tokens)
```

Each layer:
1. **Adds yield** but also slashing risk.
2. **Has different liquidity venues** (LSTs on Curve/Balancer; LRTs on Pendle/Curve).
3. **Has different redemption rails** (LST: 1-15 day exit queue; LRT: protocol-specific, often 7-30 days).
4. **Has different points/rewards schedules** (EigenLayer points; LRT-protocol points; AVS rewards).

The triangle: same underlying ETH at different layers, different prices, different yield expectations. Arbitrage emerges when:
- Points-farming hype temporarily inflates one LRT vs another.
- AVS rewards are launched on one LRT but not yet others.
- Withdrawal-queue congestion temporarily depegs one LRT.
- One LRT launches its native token (Eigen, Ether.fi ETHFI, Renzo REZ) and inflates value.

Counterparty: long-only LRT holders chasing points without rebalancing; index-fund-like flows into one LRT but not others.

## Null Hypothesis

Under no-edge conditions, observed LRT-LRT and LRT-LST spreads are not mispricings but fair compensation for real risk and friction differences: slashing exposure, redemption-queue latency (7-30 days locks capital through exactly the events that cause depegs), smart-contract risk per protocol, and points/airdrop option value. The null says the 25-150 bp dispersion is an equilibrium risk premium — buying the "cheap" LRT systematically loads the riskiest protocol (adverse selection), convergence events are survivorship-biased anecdotes, and depeg buys are knife-catching where occasional Renzo-style governance shocks (ezETH April 2024) wipe out accumulated convergence gains. Testable: across all LRT pairs, entering at >25 bp dispersion and holding to convergence or 30 days should earn ≈ 0 after borrow costs, gas, and slashing-loss reserves. The 2024 record rejects the null — convergence hit rates ran well above coin-flip and depegs reverted within days because the underlying is identical ETH with mechanically arbitrageable (if slow) redemption — but the null becomes more plausible every quarter as dispersion compresses toward the 10 bp kill threshold.

## Variants

| Variant | Description | Holding Period |
|---------|-------------|----------------|
| **LRT-LRT pair trade** | Long the cheaper LRT, short the more expensive | Days-weeks |
| **LRT-LST basis trade** | Long ETH/LST short LRT (or vice versa) when basis dislocates | 1-4 weeks |
| **Pre-launch token farming** | Hold LRT pre-airdrop, sell native token at launch | 3-12 months |
| **AVS-specific basis** | Long LRT delegated to high-reward AVS, short LRT not delegated | 1-3 months |
| **Cross-chain LRT bridge arb** | Same LRT on different chains (Ether.fi on Mainnet vs L2s) | Hours-days |
| **Pendle PT/YT arb on LRT** | Trade principal-token vs yield-token on Pendle for LRT positions | Weeks-months |

## Rules

1. **Map the LRT universe** with weights, AVS exposures, points multipliers.
2. **Compute relative-value scores** across LRTs daily.
3. **Identify pair-trade or triangle opportunity** (typically dispersion of 25-150 bp).
4. **Execute pair**:
   - Long underpriced LRT.
   - Short overpriced LRT (or borrow + short via Aave).
   - Hedge ETH beta if needed.
5. **Monitor unlocks**: LRT-protocol native-token unlocks reset the trade.
6. **Exit on convergence** or major catalyst (token launch, AVS launch).

## Implementation Pseudocode

```python
lrts = {"eETH": ether_fi, "ezETH": renzo, "rsETH": kelp, "pufETH": puffer}
on tick:
    eth_price = oracle.eth_usd()
    for lrt, protocol in lrts.items():
        observed = market.price(lrt)
        nav = compute_nav(lrt, eth_price, protocol.exit_queue, protocol.avs_rewards)
        deviation = (observed - nav) / nav
        store(lrt, deviation, t=now)
    
    pair_opportunity = pair_trade_solver(deviations)
    if pair_opportunity.spread > 25bp:
        long(pair_opportunity.cheap)
        short(pair_opportunity.expensive)
        target_close_at = projected_convergence(pair_opportunity)
```

## Indicators / Data Used

- LRT TVL by protocol (DefiLlama).
- EigenLayer restaking quotas (Eigenfoundation data).
- Points-multiplier announcements (LRT-protocol blogs).
- AVS reward distributions (on-chain trackers).
- Pendle PT/YT pool reserves.
- Curve / Balancer LRT pool reserves.
- Native LRT-token unlock schedules.

## Example Trades

The events below are documented and (where noted) Perplexity-verified; per-trade gain figures are practitioner-reported approximations illustrating the mechanics, not a backtest.

**eETH vs ezETH dispersion (Q1-Q2 2024).** Both were ETH-denominated LRTs but Ether.fi (eETH) had earlier mover advantage and higher TVL ($3B vs $2B). At one point ezETH traded at -1.2% vs eETH despite identical underlying. Long ezETH / short eETH; converged within 3 weeks for ~80 bp net.

**LRT pre-launch points trade (2024).** EigenLayer points were tradable pre-launch on Whales Market and other OTC pre-market venues; quoted prices fluctuated widely through 2024. Restakers accumulated points by holding LRTs; resold pre- or at-launch. Significant alpha for those who farmed across multiple LRTs.

**Renzo REZ launch arbitrage (April 2024).** Renzo announced REZ token launch with airdrop to ezETH holders. Pre-launch, ezETH rallied 3-5% on airdrop anticipation. REZ listed on Binance 2024-04-30 around $0.26 and fell ~40% to ~$0.16 within days of listing, continuing to decline over subsequent months. The package — hold ezETH into the airdrop snapshot, sell the rally, short REZ at listing via perps — paid on both legs (the REZ short alone returned ~40% unlevered within days).

**ezETH depeg, April 2024.** Renzo airdrop/tokenomics disappointment caused ezETH to depeg from 1.0 ETH to ~0.94 ETH on deep venues on 2024-04-23/24, with far lower wicks on thin leveraged pools as liquidations cascaded. Specialist DeFi funds bought ezETH at the depeg; converged within 5 days for ~6% gain.

**Pendle ezETH PT/YT trade (multiple).** Pendle's principal-token (PT) vs yield-token (YT) split on ezETH allowed traders to lock fixed yield (PT) or speculate on future yield (YT). YT often overpriced on launch; PT shorts paid persistently.

## Performance Characteristics

2024-2025 dedicated restaking-arb desks reported 30-80% annualized returns (heavily concentrated in Q1-Q2 2024 when the category was new). Sharpe 1.5-2.5 net of points-farming overhead.

By Q4 2024, returns compressed to 8-15% annualized as the strategy matured.

> These are *practitioner-reported, recollection-based figures for a brand-new category*, not a controlled backtest of this page's rules. Treat them as directional: the alpha was real and large early, and has compressed sharply — the [[decay-evidence|decay]] is the headline fact, not the peak number.

### Cost stack

| Cost | Magnitude | Notes |
|------|-----------|-------|
| Borrow cost (short leg via Aave) | varies with utilization | The short leg of an LRT-LRT pair can be expensive/illiquid |
| Gas | per leg / per rebalance | Multi-leg + frequent monitoring |
| Redemption-queue latency cost | 7-30 days locked | Capital trapped through exactly the depeg events |
| Slashing-loss reserve | tail (can exceed 5% across layers) | Compounds down the stack |
| Smart-contract / governance risk | binary tail | Per-protocol; e.g. ezETH governance shock, April 2024 |

## Capacity Limits

Per-trade capacity bound by LRT pool depth ($50-500M typical). Strategy-level capacity ~$1B for the most sophisticated multi-LRT operators.

| Scope | Capacity | Binding constraint |
|-------|----------|--------------------|
| Single LRT-LRT pair | $50-500M | Pool depth + short-side borrow availability |
| Pendle PT/YT leg | pool-dependent | Pendle pool reserves |
| Multi-LRT operator (strategy-level) | ~$1B | Aggregate pool depth + redemption rails |

## What Kills This Strategy

- LRT consolidation (currently 8-12 viable LRTs; could shrink to 3-5).
- AVS reward stabilization (less volatile yield surface).
- Native EigenLayer token launch (October 2024) reduced points-farming optionality.
- Sequencer-aware execution improvements compress dispersion.

## Kill Criteria

- LRT-pair dispersion below 10 bp for 90 consecutive days.
- TVL flow becomes uniform across LRTs (cross-LRT weekly net-flow dispersion < 10% of mean for a full quarter).
- Rolling 6-month Sharpe < 0.5 net of costs.
- A realized slashing event exceeding 2% of any held LRT's NAV (re-underwrite the entire risk model before re-entering).

## Advantages

- Highly profitable in 2024 (exceptionally strong risk-adjusted months during the Q1-Q2 2024 boom).
- Multi-leg structure provides natural hedges — most legs are wrappers of the same ETH, so directional ETH beta is small.
- Stack of sub-strategies (points, AVS, native tokens, basis) gives diversification within one mandate.
- Convergence is *mechanically* anchored: the underlying is identical ETH, so depegs are arbitrageable given enough redemption patience.
- Observable on-chain (TVL, pool reserves, unlock schedules) — limited information asymmetry needed.

## Disadvantages

- Slashing-risk compounding across layers (total exposure can exceed 5% of position).
- Operational complexity (multi-protocol, multi-chain monitoring; points multipliers change weekly).
- Strategy dependent on EigenLayer / restaking continued growth — a category-level [[decay-evidence|decay]] risk.
- Redemption-queue latency (7-30 days) locks capital through precisely the events that cause depegs.
- Crowded and compressing: pure-arb dispersion has fallen toward the 10 bp kill threshold; remaining alpha is in harder sub-strategies (points, AVS basis).
- Governance/tokenomics shocks (e.g. ezETH, April 2024) can wipe out accumulated convergence gains — knife-catching risk on depeg buys.

## Sources

- EigenLayer whitepaper (2023) and mainnet launch documentation (April 2024).
- Ether.fi, Renzo, Kelp, Puffer protocol documentation.
- DefiLlama LRT category tracking.
- Pendle Finance PT/YT documentation.
- Various LRT-arb practitioner blogs (Wave Financial, MEV-research).
- Verified via Perplexity (sonar), 2026-06-10: REZ listed on Binance 2024-04-30 at ~$0.2638 and fell to ~$0.16 post-listing (corrected an earlier erroneous "$2.00 launch price" figure on this page). Citations: fxstreet.com/cryptocurrencies/news/renzos-rez-dips-after-airdrop-and-binance-listing-202404302338, coingecko.com/en/coins/renzo.

## Related

[[lst-depeg-arbitrage]] · [[triangular-arbitrage]] · [[multi-leg-arbitrage]] · [[crypto-spot-perp-futures-triangle]] · [[restaking]] · [[airdrop-farming]] · [[points-farming]] · [[liquidity-provider]] · [[arbitrage]] · [[limits-to-arbitrage]] · [[pendle-pt-yt-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]] · [[2022-06-steth-depeg]]
