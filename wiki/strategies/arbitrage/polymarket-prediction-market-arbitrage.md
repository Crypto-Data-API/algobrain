---
title: "Polymarket Prediction Market Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, event-driven]
aliases: ["Prediction Market Arb", "Polymarket Triangulation", "Kalshi-Polymarket Spread"]
related: ["[[polymarket]]", "[[polymarket-vs-kalshi]]", "[[triangular-arbitrage]]", "[[event-driven-trading]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto, prediction-markets]
complexity: advanced
backtest_status: live
edge_source: [analytical, informational, structural]
edge_mechanism: "Prediction markets price probabilities of binary outcomes (election winners, economic prints, sports). Multiple venues quote the same event with different liquidity, regulatory access, and participant bases. Cross-venue triangulation, complementary-market arbitrage (YES + NO must = 100%), and reality-vs-market arbitrage all generate persistent edge."
data_required: [polymarket-orderbook, kalshi-orderbook, manifold-prices, prediction-it-history, real-world-data-feeds]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: low
expected_sharpe: 1.5
expected_max_drawdown: 0.2
breakeven_cost_bps: 50
decay_evidence: "Polymarket volume exploded 2024 ($3B election cycle); spreads compressed but reality-arb opportunities persist. Cross-venue arb gated by US regulatory restrictions on Polymarket."
---

# Polymarket Prediction Market Arbitrage

Trading the price discrepancies between binary-outcome **prediction markets** — primarily [[polymarket|Polymarket]] (crypto-native, on Polygon), **Kalshi** (CFTC-regulated US), **PredictIt** (academic/research), and **Manifold Markets** (play-money). The 2024 US election cycle pushed Polymarket volume past **$3 billion**; total prediction-market capitalization now matches mid-cap individual stocks. For sophisticated arbitrageurs the strategy stack includes:

1. **Cross-venue triangulation** — same event priced differently across venues.
2. **Complementary-pair arbitrage** — YES + NO on same outcome must sum to $1.00.
3. **Reality-vs-market arbitrage** — exploit systematic biases (favorite-longshot, partisan optimism).
4. **Multi-event basket arbitrage** — exploit logical contradictions across related events.

## Edge Source

**Analytical** + **informational** + **structural**.

- **Analytical:** Real-world probability modeling (election forecasts, economic data probability) is non-trivial.
- **Informational:** Pre-market data, polling, on-chain whale flows can predict resolution.
- **Structural:** Cross-venue trading is gated by KYC/jurisdiction; Polymarket excludes US users (officially); Kalshi doesn't accept crypto. Cross-venue arb requires multi-jurisdictional infrastructure.

## Why This Edge Exists

Prediction markets are early-stage. Liquidity is fragmented across venues:
- **Polymarket** — global crypto users; ~$200M-$1B daily volume on major elections.
- **Kalshi** — CFTC-regulated US fiat venue; smaller volume but better US institutional access.
- **PredictIt** — academic; capped at $850/event; mostly research.
- **Manifold** — play money; informational only.
- **Sports books (DraftKings, FanDuel)** — informally tradeable on related outcomes.

Different participant bases create different prices for identical events. Polymarket reportedly skewed Republican in 2024 (large Trump-friendly whales); Kalshi was more balanced. Spreads of 2-5% on identical events were common.

Counterparty: ideologically-driven retail bettors, casual users, partisan participants, low-volume contracts.

### Venue Comparison

| Venue | Regulation / status | Settlement asset | Resolution mechanism | US access | Role in the arb |
|-------|---------------------|------------------|----------------------|-----------|-----------------|
| **[[polymarket\|Polymarket]]** | Crypto-native (Polygon); CFTC 2022 settlement restricts US users | USDC | [[uma\|UMA]] optimistic oracle | Officially excluded | Deepest liquidity; on-chain transparency |
| **Kalshi** | CFTC-regulated DCM (US) | USD fiat | Internal / designated source | Yes (compliant) | Cleaner US institutional access; no crypto |
| **PredictIt** | Academic (CFTC no-action, contested) | USD | Internal | Yes, capped | $850/event cap; research-grade |
| **Manifold** | Play-money | Mana (no cash-out) | Creator/community | Yes | Informational price discovery only |
| **Sports books (DraftKings, FanDuel)** | State-licensed sportsbooks | USD | Official sports result | State-by-state | Informal cross-market on sports outcomes |

The arbitrage exists *because* these venues are not fungible: a crypto-settled, US-excluded venue and a fiat, CFTC-regulated venue cannot be costlessly netted, so identical events can carry persistent price gaps. See [[polymarket-vs-kalshi]] for the detailed venue split.

## Null Hypothesis

Under efficient, integrated markets every venue quoting the same binary event displays the same probability to within transaction costs (Polymarket: gas + spread, near-zero protocol fees; Kalshi: ~1-2¢ effective round trip), YES + NO always sums to $1.00 ± the bid-ask, and prices are calibrated — contracts priced at X¢ resolve YES X% of the time. Under that null, cross-venue "spreads" are untradeable noise inside cost bounds, the YES+NO basket never sums below ~$0.98 at executable size, and a buy-cheap/sell-rich rule nets zero after fees plus the cost of segregating capital across jurisdictions. The 2024 election cycle rejects the null on two counts: (1) Polymarket-Kalshi divergence of 3-7% persisted for **weeks** at executable size — far outside cost bounds, and directionally explained by venue demographics rather than random noise; (2) calibration studies of prediction markets document a persistent favorite-longshot bias (longshots overpriced), e.g. Page & Clemen (2013). If observed cross-venue spreads stay inside ~30 bp and YES+NO baskets never break $0.97 at size, the market has integrated and the edge is gone.

## Variants

| Variant | Description | Example |
|---------|-------------|---------|
| **Cross-venue arb** | Buy on cheaper venue, sell on richer | Trump win 50¢ Polymarket vs 53¢ Kalshi (Oct 2024) |
| **YES + NO arbitrage** | Sum must = $1.00; ~5% deviations occur in low-liquidity markets | Buy YES + NO when sum < $0.95 |
| **Conditional probability** | Markets like "Trump wins AND Republican Senate majority" can be cheaper than P(A) × P(B) implied by individual markets | 3-leg trades |
| **Reality-vs-market** | When polling/forecasting suggests systematic mispricing | Election-eve 2024: Polymarket Trump 60%, Nate Silver 51% |
| **Resolution-source arb** | Markets resolve based on "official source" — short delay between truth and resolution | Buy YES on confirmed event before resolution |
| **Whale-flow front-running** | Detect large whale entries/exits via on-chain data | Polymarket on-chain transparency enables this |

## Rules

1. **Universe screening:** identify same-event listings across Polymarket, Kalshi, PredictIt.
2. **Spread monitoring:** real-time order-book scanning for >50 bp deviations.
3. **Risk modeling:** estimate true probability via independent model; size by Kelly fraction.
4. **Multi-jurisdiction execution:** Polymarket via VPN/non-US entity; Kalshi via US compliant entity.
5. **Position management:** liquidity is thin; size carefully to avoid moving the market against yourself.
6. **Resolution monitoring:** watch for resolution-source disputes (occasional).

## Implementation Pseudocode

```python
on tick:
    for event in tracked_events:
        prices = {venue: orderbook.mid(event, venue) for venue in [polymarket, kalshi, manifold]}
        spread = max(prices.values()) - min(prices.values())
        if spread > min_threshold:
            cheap_venue = min(prices, key=prices.get)
            rich_venue = max(prices, key=prices.get)
            size = kelly_quarter(spread, vol_estimate)
            buy(event, cheap_venue, size)
            sell(event, rich_venue, size)
        # Check YES + NO
        yes_price = orderbook.mid(event + "_YES", polymarket)
        no_price = orderbook.mid(event + "_NO", polymarket)
        if yes_price + no_price < 0.95:
            buy(event + "_YES", polymarket, max_size)
            buy(event + "_NO", polymarket, max_size)
```

## Indicators / Data Used

- Polymarket Subgraph (on-chain real-time order book + resolution data).
- Kalshi API (institutional-tier required for full depth).
- Manifold Markets API (free, lower-quality price discovery).
- Real-world data feeds (polling aggregators, economic data calendars).
- On-chain whale flows on Polymarket (Dune dashboards).

## Example Trades

**2024 US Election cycle (peak Oct-Nov 2024).** Polymarket and Kalshi diverged 3-7% on Trump-win pricing for weeks. Sophisticated traders bought Trump on Kalshi (~50-53¢) and sold on Polymarket (~58-65¢) for ~5-12% spread. Cross-venue arb required US LLC for Kalshi + non-US entity (Cayman, BVI) for Polymarket.

**2024 Election Polymarket whale "Théo"** — Single user reportedly placed $35M+ on Trump win across multiple Polymarket positions. Triggered media speculation about manipulation; ultimately profitable as Trump won. Whale-flow detection became a tradable signal.

**FOMC meetings (recurring 2024-2025).** Polymarket lists "Fed cuts X bp" markets. Pre-meeting spread vs CME FedWatch implied probability often diverged 3-7%. Long the cheap side, hold to resolution = high-Sharpe carry.

**Economic data prints.** "Will US July CPI > 3.0%?" markets converge sharply at release. Pre-release spread vs Bloomberg consensus tradable.

**Sports outcomes (low-liquidity edge).** Specific basketball/football outcomes with low Polymarket volume vs DraftKings implied probability. Triangulation across regulated US sports book + Polymarket = single-game edge of 5-15% (rare but occurs).

## Costs and Frictions

The headline cross-venue "spread" is gross; the executable edge is what survives these:

| Cost / friction | Magnitude | Note |
|-----------------|-----------|------|
| **Bid-ask** | Polymarket near-zero protocol fee + spread; Kalshi ~1-2¢ effective round trip | Thin books widen this on low-liquidity events |
| **Gas / on-chain** | Polygon gas (low) | Negligible vs Ethereum but non-zero |
| **Capital segregation** | Large | Must hold balances on *both* venues across jurisdictions; cannot net — doubles deployed capital |
| **Jurisdiction / KYC** | Setup cost | US LLC for Kalshi + non-US entity (Cayman/BVI) for Polymarket |
| **FX / stablecoin** | USDC vs USD basis | Convert and bridge between fiat and crypto rails |
| **Resolution risk** | Tail | [[uma\|UMA]]-based disputes can delay or alter payout |
| **Time-to-resolution carry** | Opportunity cost | Capital locked until the event resolves |

Because legs sit on non-fungible venues, this is not a *riskless* arbitrage — it is a **convergence trade with execution and settlement risk**, closer to [[triangular-arbitrage]] across walled gardens than to a true two-sided lock.

## Performance Characteristics

> **No fabricated returns.** Figures below are self-reported / press-reported, not audited; returns are lumpy and concentrated around event cycles.

Specialist prediction-market trading desks reportedly earned 15-25% annualized on dedicated capital 2023-2024 (self-reported figures; no audited track records public). Sharpe 1.5-2.5 (frontmatter budgets `expected_sharpe: 1.5`, `expected_max_drawdown: 0.2`). Lumpy returns concentrated around major event cycles (elections, FOMC).

Reality-vs-market arb has historical 5-12% edge for sophisticated probabilists; harder than it sounds — requires actual modeling capability.

## Capacity Limits

Per-event $10K-$2M depending on event liquidity. Major US election: Polymarket capacity ~$50-200M during peak; Kalshi ~$10-50M.

## What Kills This Strategy

- Cross-venue regulatory crackdown (CFTC settled with Polymarket in January 2022 — $1.4M civil penalty and US-user restrictions; DOJ/FBI probe followed in November 2024).
- Liquidity migration to one dominant venue.
- Sophisticated market makers compress spreads.
- Resolution-source disputes (Polymarket UMA-based resolution has had disputes).

## Kill Criteria

Numerical conditions for retiring the strategy (see [[when-to-retire-a-strategy]]):

- **Spread compression:** cross-venue spread stays inside ~30 bp at executable size for a full major event cycle — the [[#Null Hypothesis|null]] is no longer rejected, edge gone.
- **YES+NO never breaks $0.97:** complementary-pair baskets stop offering sub-$0.97 entries at size — the within-venue mispricing has closed.
- **Regulatory elimination:** a major action removes a venue (e.g., Polymarket fully blocked or Kalshi enjoined), collapsing the two-sided structure.
- **Drawdown breach:** peak-to-trough exceeds the `expected_max_drawdown` budget of **20%**.
- **Resolution-source breakdown:** repeated [[uma\|UMA]] / resolution disputes make settlement unreliable enough that convergence can no longer be trusted.

## Advantages

- Decoupled from crypto beta and traditional markets.
- Recurring opportunities tied to news cycles.
- Highly transparent on-chain (Polymarket).

## Disadvantages

- Multi-jurisdiction infrastructure required.
- Resolution disputes possible.
- Low-liquidity contracts have wide bid-ask.

## Sources

- *Polymarket whitepaper* and protocol documentation.
- *Kalshi API documentation*.
- Forecasting Research Institute (FRI) — Reality-vs-market analysis.
- **YouTube: "Polymarket Trading Strategy" series** by various crypto educators 2024.
- **YouTube: "Coin Bureau" prediction market explainer (2024).**
- **YouTube: "Bankless" interview with Polymarket founder Shayne Coplan (2024).**
- *FT Alphaville* coverage of "Théo" whale and 2024 election speculation.
- Page & Clemen, *Do Prediction Markets Produce Well-Calibrated Probability Forecasts?* (Economic Journal, 2013).
- Verified via Perplexity (sonar), 2026-06-10: CFTC-Polymarket 2022 settlement confirmed resolved; Kalshi fiat-only funding confirmed for the period covered; "Insilico Capital" could not be verified and was removed.

## Related

- [[polymarket]] -- primary crypto-native venue
- [[prediction-markets]] -- the broader instrument category
- [[polymarket-vs-kalshi]] -- detailed venue comparison
- [[kalshi]] -- CFTC-regulated US venue
- [[triangular-arbitrage]] -- the multi-leg/complementary-pair analog
- [[event-driven-trading]] -- adjacent strategy family
- [[regulatory-arbitrage]] -- the jurisdiction split that creates the edge
- [[uma]] -- Polymarket's optimistic-oracle resolution layer
- [[when-to-retire-a-strategy]] -- kill-criteria methodology
- [[favorite-longshot-bias]] -- the calibration bias the reality-arb exploits
- [[shayne-coplan]] -- Polymarket founder
- [[crypto]] -- settlement rail (USDC on Polygon)
