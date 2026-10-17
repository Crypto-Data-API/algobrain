---
title: "Bittensor Subnet Rotation"
type: strategy
created: 2026-04-19
updated: 2026-10-17
status: good
tags: [crypto, defi, bittensor, ai-trading, momentum, algorithmic]
aliases: ["dTAO Subnet Rotation", "Alpha Rotation"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [informational, behavioral]
edge_mechanism: "Subnet emission share on Bittensor reallocates block-by-block via dTAO bonding curves; most market participants cannot price the subnet-fundamentals signal fast enough, so rotation between alpha tokens captures the share-gain before the bonding curve prices it in."
data_required: [bittensor-alpha-prices, subnet-emission-share, validator-hotkey-activity, subnet-github-activity, subnet-off-chain-revenue]
min_capital_usd: 5000
capacity_usd: 2000000
crowding_risk: medium
breakeven_cost_bps: 50
related: ["[[bittensor]]", "[[dtao]]", "[[bittensor-subnets]]", "[[alpha-token-arbitrage]]", "[[tao-validator-delegation]]", "[[momentum]]"]
gates:
  - id: subnet_depth_500tao
    role: universe
    rule: "Active subnets whose alpha bonding-curve pool holds more than about 500 TAO"
    runnable: false
    note: "No Bittensor subnet, alpha-pool or Subtensor data is served. Needs taostats, dtao.gg or a Subtensor RPC."
  - id: emission_momentum
    role: entry
    rule: "Emission-share momentum = share now / share 7 days ago - 1 (composite weight 0.40)"
    runnable: false
    note: "Subnet emission shares are not served (taostats or Subtensor)."
  - id: alpha_price_momentum
    role: entry
    rule: "Alpha-price momentum = alpha price now / alpha price 7 days ago - 1 (weight 0.20)"
    runnable: false
    note: "Subnet alpha-token prices are not served; only TAO itself is."
  - id: revenue_growth
    role: entry
    rule: "Off-chain revenue or usage growth for subnets that report it (weight 0.15)"
    runnable: false
    note: "Subnet revenue comes from each subnet's own dashboards; not served."
  - id: validator_dispersion
    role: entry
    rule: "Number of active validators submitting distinct weight vectors (weight 0.15)"
    runnable: false
    note: "Validator weight data is a Subtensor read; not served."
  - id: github_activity
    role: entry
    rule: "Weekly or 30-day commit count on the subnet repo (weight 0.10)"
    runnable: false
    note: "Not served; needs the GitHub API."
  - id: top_decile_long
    role: entry
    rule: "Rank subnets on the weighted composite and stake into the top decile; unstake or avoid the bottom decile"
    runnable: false
    input: derived
    inputs: [emission_momentum, alpha_price_momentum, revenue_growth, validator_dispersion, github_activity]
    note: "Every component is unserved."
  - id: weekly_rebalance
    role: entry
    rule: "Rebalance weekly by default"
    runnable: true
    input: position
  - id: event_override
    role: entry
    rule: "Allow intraday overweights on subnet owner announcements, major commits or integration wins"
    runnable: false
    note: "Subnet-level announcements are not served; a news judgement."
  - id: position_caps
    role: sizing
    rule: "At most 15% of the alpha allocation per subnet; the strategy is 5-15% of crypto NAV"
    runnable: true
    input: position
  - id: tao_beta_hedge
    role: sizing
    rule: "Hedge the alpha book's TAO exposure with a TAO perp short during rebalances and leg gaps"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/funding-rates?coin=TAO&limit=24
    field: history[].funding_rate
    replay: /api/v1/backtesting/funding?symbol=TAO&exchange=hyperliquid&grain=hourly&start={start}
    replay_field: data[].funding_rate
    note: "From the AI-agent workflow. Hourly funding is the hedge's carry; the TAO exposure comes from the position record and the TAO mark from assets[].mark_price on /hyperliquid/open-interest."
  - id: regime_cut_gross
    role: filter
    rule: "Cut gross rotation exposure when strong_trend_bear or vol_spike becomes likely: alpha tokens do not survive a TAO cascade unhedged"
    runnable: partial
    endpoint: /api/v1/quant/coins/TAO
    field: regime.label
    replay: /api/v1/quant/history?scope=TAO&start={start}
    replay_field: entries[].regime_label
    note: "From the AI-agent workflow, which names /quant/market for the trigger and /quant/coins/TAO for the TAO-specific read; it sets no probability cutoff or cut size."
  - id: exit_rank_bottom_half
    role: exit
    rule: "Exit when the subnet's composite rank falls out of the top half"
    runnable: false
    input: derived
    inputs: [top_decile_long]
    note: "The composite is unserved."
  - id: exit_thin_curve
    role: exit
    rule: "Exit when bonding-curve depth drops below 2x the intended exit size"
    runnable: false
    note: "Alpha-pool depth is not served."
  - id: exit_red_flags
    role: exit
    rule: "Exit on red flags: validator collusion signals, subnet owner wallet dumping, GitHub abandonment"
    runnable: false
    note: "Subtensor and GitHub reads, plus a judgement; none is served."
  - id: kill_vs_benchmark
    role: stop
    rule: "Kill switch: rolling 90-day return below -30% against an equal-weighted alpha benchmark"
    runnable: partial
    input: position
    note: "The strategy's own return is in the position record; the equal-weighted alpha benchmark needs alpha prices, which are not served."
  - id: kill_slippage_200bp
    role: stop
    rule: "Kill switch: average realised slippage per rebalance above 200 bp"
    runnable: true
    input: position
  - id: kill_protocol_change
    role: stop
    rule: "Kill switch: a governance change that invalidates the dTAO mechanism"
    runnable: false
    note: "A judgement on Opentensor governance; not served."
---

# Bittensor Subnet Rotation

Subnet rotation is a Bittensor-specific strategy that reallocates capital across subnet **alpha tokens** in response to changes in each subnet's block-to-block emission share. Post-[[dtao]] (Feb 2025) emission share is market-determined via alpha bonding curves, which makes it a high-frequency observable. The thesis is that alpha-token prices do not fully reflect emission-share momentum in real time -- a momentum-style rotation strategy that stakes into subnets gaining share and unstakes from subnets losing share should extract positive return relative to a static alpha-basket benchmark.

## Edge Source

This strategy maps to two categories in the [[edge-taxonomy]]:

1. **Informational edge** -- the dataset (subnet-by-subnet emission share, alpha pool depth, root validator weights, off-chain subnet revenue) is mostly on-chain and free, but it requires dedicated pipelines to consume. Most retail holders stake-and-hold a single subnet; most institutions do not allocate to Bittensor at all. The data-to-action gap is real.
2. **Behavioral edge** -- dTAO is a market-based emission system, and markets under-react to shifts in the underlying cash-flow (emissions-share) signal. Classical momentum anomalies show up in alpha-token-land for the same reasons they show up in equity factor investing.

## Why This Edge Exists

1. **Block-frequency allocation**. Subnet emissions reallocate every 12 seconds. No human trader is integrating that signal; most are checking dashboards once a day.
2. **Narrative lag**. Alpha token prices on bonding curves adjust to pool depth, not to off-chain narrative. A subnet that ships a major integration (a partnership, a validated benchmark win) sees emission share rise before the price fully re-rates.
3. **Small dedicated pool of quants**. The number of desks running systematic Bittensor strategies is tiny (tens, not thousands). Crowding risk is medium, not high.
4. **Structural beta**: compute and data subnets (Chutes, Celium, Basilica, Data Universe, Masa) capture emission share during periods when the off-chain crypto compute narrative strengthens. Rotation captures beta to the current "which subnet category does the market care about" regime.

## Null Hypothesis

Under a no-edge null, alpha tokens are random walks on their bonding curves and rotation trades bleed on bonding-curve slippage and dTAO staking/unstaking round-trip costs. Backtests should be compared against an equal-weight alpha-basket benchmark and a buy-and-hold-TAO benchmark to separate strategy alpha from beta.

## Rules

### Universe

All active subnets with alpha pool TAO depth > some threshold (e.g. 500 TAO of TAO-denominated liquidity in the bonding curve) to avoid slippage-prohibitive low-cap subnets.

### Signals

For each subnet N at each rebalance:

1. **Emission-share momentum** -- `(share_now / share_7d_ago) - 1`. High momentum → overweight.
2. **Alpha-price momentum** -- `(alpha_price_now / alpha_price_7d_ago) - 1`. Cross-check with emission momentum.
3. **Off-chain revenue / usage** -- for subnets with measurable revenue (compute subnets: Chutes, Celium, Basilica; data subnets: Data Universe, Masa), track revenue growth. Overweight revenue-growing subnets.
4. **Validator-set dispersion** -- number of active validators submitting distinct weight vectors. Broader validator participation is a quality signal.
5. **GitHub activity** -- weekly commit count on the subnet repo. Dead repos are red flags.

### Composite Score and Selection

Compute a composite rank across the universe using the above signals. Go long the top decile (stake TAO into those subnets' alpha pools); either unstake or avoid the bottom decile. Optional short leg: sell alpha of the worst subnets into the bonding curve.

### Rebalance Frequency

- **Weekly** rebalance is the default. Alpha bonding curves have finite liquidity; more frequent rebalancing pays more slippage.
- **Event-driven overrides**: subnet owner announcements, major commits, integration wins -- allow intraday overweight triggers.

### Position Sizing

- Per-subnet cap: 15% of alpha allocation to prevent single-subnet blowup.
- Overall strategy allocation: a fraction of a broader crypto book; 5-15% of crypto NAV is typical for a specialist.

### Exits

Exit a position when:
- Composite rank falls out of the top half.
- Bonding curve depth drops below 2× intended exit size (can't exit cleanly).
- Subnet exhibits specific red flags: validator collusion signals, subnet owner wallet dumping, GitHub abandonment.

## Implementation Pseudocode

```python
def subnet_rotation_rebalance():
    subnets = fetch_active_subnets(min_tao_depth=500)
    for subnet in subnets:
        subnet.emission_momentum_7d = emission_share_change(subnet, days=7)
        subnet.alpha_momentum_7d = alpha_price_change(subnet, days=7)
        subnet.revenue_growth = offchain_revenue_growth(subnet)  # None for most
        subnet.validator_dispersion = count_distinct_validators(subnet)
        subnet.github_commits_30d = github_activity(subnet)
        subnet.composite = rank_composite(
            emission_mom=0.40,
            alpha_mom=0.20,
            revenue=0.15,
            validators=0.15,
            github=0.10,
            subnet=subnet,
        )

    ranked = sorted(subnets, key=lambda s: s.composite, reverse=True)
    top_decile = ranked[: len(ranked) // 10]
    bottom_decile = ranked[-len(ranked) // 10 :]

    target_positions = {s: alloc / len(top_decile) for s in top_decile}

    for position in current_positions():
        target = target_positions.get(position.subnet, 0)
        if target == 0 and position.subnet in bottom_decile:
            unstake(position.subnet, position.alpha_amount)
        elif target != position.alloc:
            rebalance_to(position.subnet, target)

    for subnet, target in target_positions.items():
        if subnet not in [p.subnet for p in current_positions()]:
            stake_tao(subnet, target * nav)
```

## Data Sources

- **[[taostats]] (taostats.io)** -- canonical on-chain analytics: emission shares, validator hotkeys, alpha prices
- **[[dtao-gg|dtao.gg]]** -- purpose-built dTAO dashboard with rotation leaderboards
- **GitHub API** -- subnet repo activity
- **Subnet-specific dashboards / docs** -- for off-chain revenue (Chutes usage stats, Celium GPU metrics)
- **Bittensor SDK (`bt-cli` and `bittensor-python`)** -- direct on-chain reads

## Example Trade

**March 2026 -- Chutes (SN64) emission-share surge**

1. **Signal**: between March 3 and March 10, SN64's emission share rose from ~8.1% to ~11.4% as Chutes announced expanded GPU partnerships. Alpha-64 price rose ~22% over the same window -- less than the emission-share move implied.
2. **Action**: rotation strategy stakes additional TAO into SN64, receiving alpha-64 at the then-current bonding-curve price.
3. **Subsequent weeks**: by April 1, emission share had stabilized at ~12.5% and alpha-64 price had caught up, trading ~48% above the March 10 level.
4. **Outcome**: the rotation captured the lagging price move plus accrued alpha-64 dilution.

This is a stylized example. Actual rotations require cleaner entry/exit rules and produce smaller per-trade gains at higher frequency.

## Performance Characteristics

No published audited track record for systematic dTAO rotation strategies exists as of April 2026. Public prop shops running this (handful of Bittensor-native teams) report discretionary returns in the 40-120% range over 2025 on small capital, but those numbers mix rotation with outright alpha-token directional bets and are not audited.

## Capacity Limits

- **Per-subnet bonding-curve depth** is the binding constraint. Most alpha pools have $1-10M TAO-denominated depth; a single $500K rebalance can move the curve 5-10%.
- **Strategy-wide capacity**: realistically $1-2M across 8-15 active subnet positions before slippage dominates returns.
- Not an institutional-scale strategy. It is a retail and small-fund strategy.

## What Kills This Strategy

1. **Crowding** -- if too many quants run the same rotation, the lead-lag between emission share and alpha price collapses.
2. **Protocol changes** -- the Opentensor Foundation can (and has) changed dTAO parameters. Any change to the alpha bonding curve formula or emission-share calculation invalidates historical backtests.
3. **Subnet spam** -- a flood of registration-for-emissions subnets makes the universe harder to clean. Mitigate with minimum-depth filters.
4. **Alpha-pool rug** -- a subnet owner who exits their own alpha in size can crash the bonding curve. Position-size discipline is the only defense.
5. **TAO drawdown correlation** -- alpha tokens are TAO-denominated. A 50% TAO drawdown drags all alpha tokens down with it, rotation alpha or not.

## Kill Criteria

- Rolling 90-day return < -30% vs equal-weighted alpha benchmark.
- Average realized slippage per rebalance > 200 bps (indicates capacity breach).
- Protocol-level governance change that invalidates the dTAO mechanism.

## Advantages

- Captures a genuinely novel alpha source unavailable in traditional markets.
- Low infrastructure requirements relative to pure on-chain HFT.
- Asymmetric upside if Bittensor subnet economics mature: alpha tokens with real revenue may re-rate hard.

## Disadvantages

- Small capacity.
- Operational complexity (validator key management, chain interaction, subnet monitoring).
- Execution slippage on bonding curves.
- Single-protocol dependency on Bittensor not going to zero.

## Getting the Data (CryptoDataAPI)

The core rotation signals — subnet emission shares, alpha bonding-curve prices, validator activity — come from **taostats.io / dtao.gg / Subtensor RPC**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the TAO market layer around the strategy: TAO price and klines for the denominating asset, TAO perp funding for hedging the strategy's unavoidable TAO beta, and regime context for the "a 50% TAO drawdown drags all alpha down" kill risk.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TAOUSDT` — TAO spot price (the unit every alpha position is denominated in)
- `GET /api/v1/derivatives/funding-rates?coin=TAO` — cross-exchange TAO perp funding: the carry on a TAO-beta hedge
- `GET /api/v1/coins/search?q=TAO` — TAO profile and market-cap context

**Historical data:**
- `GET /api/v1/backtesting/klines` — TAO OHLCV archive (Binance spot 1h/4h/1d and Hyperliquid daily, from listing) for TAO-beta and drawdown-correlation studies
- `GET /api/v1/backtesting/funding` — TAO funding history (Hyperliquid hourly, from listing) for hedge-cost modelling

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=TAO"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the market-layer half of this strategy end-to-end (the emission-share signal itself still needs a taostats/Subtensor feed):

- **TAO-beta hedge** — `GET /api/v1/derivatives/funding-rates?coin=TAO` + `GET /api/v1/market-data/ticker/price?symbol=TAOUSDT`: size and carry-cost a TAO perp short against the alpha book's TAO exposure during rebalances and leg gaps.
- **Regime gate** — `GET /api/v1/quant/market`: cut gross rotation exposure when `strong_trend_bear`/`vol_spike` probabilities rise — alpha tokens are TAO-denominated, so rotation alpha does not survive a TAO cascade unhedged.
- **Kill-risk monitor** — `GET /api/v1/quant/coins/TAO` (per-coin probability matrix, Pro): the machine-readable version of the TAO-drawdown kill criterion.
- **Backtest** — the TAO legs replay from `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) and `GET /api/v1/backtesting/funding` (Hyperliquid hourly funding, from TAO's listing — not the 2023-05 archive start); emission-share history must come from taostats — CDA holds no Subtensor data.
- **Tips** — respect `insufficient_history` flags on TAO derivatives data; the rotation signal updates block-by-block (12s), so pair CDA's cached hourly `GET /api/v1/daily` context with a direct Subtensor subscription for the alpha side.

## Related

- [[bittensor]] -- protocol overview
- [[dtao]] -- the market-allocation mechanism that enables this strategy
- [[bittensor-subnets]] -- subnet landscape
- [[alpha-token-arbitrage]] -- a complementary bonding-curve arbitrage strategy
- [[tao-validator-delegation]] -- yield-bearing alternative for passive TAO holders
- sector-momentum-screen, [[momentum]] -- sibling momentum strategies in other asset classes

## Sources

- taostats.io documentation and on-chain data (authoritative)
- dtao.gg subnet rotation leaderboards
- Opentensor Foundation dTAO specification (2024 Q4 / 2025 Q1)
- Messari "Bittensor's dTAO Upgrade" (2025) and Delphi Digital Bittensor coverage
