---
title: "Vampire Attack Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-07-19
status: excellent
tags: [arbitrage, defi, crypto, event-driven]
aliases: ["Vampire Mining", "Liquidity Vampire Arb", "Migration Farming"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [behavioral, structural, informational]
edge_mechanism: "Forked protocols subsidise migration with inflationary governance tokens; early LPs capture rewards before sell-pressure dilutes them, while incumbents are slow to defend their moat."
data_required: [dex-liquidity-snapshots, governance-token-emissions, vesting-schedules, on-chain-transfers]
min_capital_usd: 25000
capacity_usd: 5000000
crowding_risk: high
expected_sharpe: 1.4
expected_max_drawdown: 0.45
breakeven_cost_bps: 80
related: ["[[sushiswap]]", "[[uniswap]]", "[[airdrop-farming]]", "[[liquidity-mining]]", "[[curve-gauge-wars-arbitrage]]", "[[2020-09-sushiswap-vampire-attack]]"]
---

# Vampire Attack Arbitrage

Vampire attack arbitrage is the strategy of providing liquidity (or volume, or order flow) as a [[liquidity-provider|liquidity provider]] to a *forked* protocol that pays migrating users in inflationary governance tokens, capturing those rewards, and exiting before token emissions dilute the price. It is a DeFi-native [[event-driven-trading|event-driven]] / incentive-capture trade rather than a pure-math [[arbitrage]] — the "arbitrage" is between *quoted* subsidy APR and *steady-state* equilibrium APR. The original "vampire attack" — [[sushiswap|SushiSwap]] forking [[uniswap|Uniswap]] in August 2020 — drained over $1B in liquidity from Uniswap by paying SUSHI tokens to anyone who staked Uniswap LP tokens on SushiSwap. The same playbook has since been replayed at other layers of the stack: NFT marketplaces ([[blur|Blur]] vs [[opensea|OpenSea]], 2022-23) and, more loosely, perp-DEX incentive wars (e.g., [[hyperliquid|Hyperliquid]]'s points campaigns drawing flow from incumbents like [[gmx|GMX]] and the CEXs). Not all of these are strict code forks — the common element is paying users in tokens to migrate.

### Anatomy of a vampire attack

| Phase | What happens | Arber's action |
|-------|--------------|----------------|
| 1. Announcement | Fork declares it will subsidize migration from a named incumbent | Verify incentive + contracts |
| 2. Snapshot / staking window | Fork rewards holders of incumbent LP tokens at a snapshot block | Hold incumbent LP into snapshot |
| 3. Boosted emissions | Fork pays outsized token APR to bootstrap [[total-value-locked|TVL]] | Migrate, provide liquidity, harvest |
| 4. Migration | Liquidity drains from incumbent to fork | Stay in only while realized APR > hurdle |
| 5. Taper / cliff | Emissions step down; token price falls on sell-pressure | **Exit before the cliff** |
| 6. Steady state | APR normalizes to risk-adjusted equilibrium; late LPs diluted | Already gone |

## Edge source

Primarily **behavioral** and **structural** with an **informational** kicker. The behavioral edge is that retail LPs anchor to the incumbent and migrate slowly, leaving abnormal token-per-LP rewards on the table for early movers. The structural edge is that forks bootstrap liquidity by *subsidising* it with token inflation that is uneconomic in steady-state — early arbers harvest the subsidy and exit before the steady-state arrives. The informational edge is that announcements, snapshot dates, and emission schedules are public on-chain, but most users are not actively monitoring multiple competing protocols.

See [[edge-taxonomy]] for the full framework.

## Why this edge exists

A vampire attack only succeeds if the attacker overpays for liquidity in the short term. Whoever launches the fork is effectively printing equity (the governance token) to buy a market position. The losers are:

1. **The forked incumbent**, who cedes TVL and order flow.
2. **Late LPs on the new protocol**, who arrive after emissions taper and the token has dumped.
3. **Long-term token holders**, who eat the dilution.

The arbitrageur sits between (2) and (3): they show up early, harvest the token, and dump on the people in category (2) and (3). This is structurally similar to [[airdrop-farming]] but with a directional bet that liquidity *will* migrate and emissions *will* be paid in the meantime.

## Null hypothesis

Under random conditions, governance token emissions would be priced in immediately and the fork's APR would equal the risk-adjusted yield available elsewhere. In practice, new tokens trade at high IV, retail underestimates emission schedules, and there is a brief window — usually 2-8 weeks — where realised yield exceeds priced-in yield. The strategy fails (becomes a losing trade) once the token's market cap fully discounts future emissions, which historically coincides with the end of the "cliff" reward boost.

## Rules

### Entry
1. **Identify the fork.** Track new protocols that explicitly target an incumbent's liquidity (announcements on Twitter, governance forums, [[defillama|DefiLlama]] new-protocol feed).
2. **Verify the incentive.** Read the emission schedule. Is there a boosted period? A snapshot date? A cliff after which rewards taper?
3. **Verify the contract.** Audit status, multisig signers, timelock on emissions changes. Skip protocols where the team can mint at will.
4. **Position pre-snapshot.** If the fork rewards LPs on the incumbent at a snapshot date, hold incumbent LP tokens before that date.
5. **Migrate at launch.** Move liquidity to the fork as soon as rewards start.

### Exit
6. **Harvest aggressively.** Claim and sell tokens on every block where gas allows; do not stockpile.
7. **Exit liquidity before the boost ends.** Most vampire forks see TVL collapse 30-70% within 14 days of the boosted-emission period ending.
8. **Do not hold the governance token.** Treat it as a coupon, not an investment.

### Position sizing
- No more than 5% of book in any single fork (smart-contract risk is concentrated).
- Cap exposure to incumbent LP tokens during the snapshot window in case of incumbent defensive action (fee changes, blacklists, UI deprecation).

## Implementation pseudocode

```python
for fork in monitor_new_dex_forks():
    if not fork.has_audited_contracts(): continue
    if not fork.has_timelock(min_hours=24): continue

    schedule = fork.get_emission_schedule()
    apr_realised = estimate_apr(
        emissions_per_block=schedule.boost_emissions,
        token_price=oracle.spot(fork.token),
        target_tvl=schedule.target_tvl,
    )
    if apr_realised < HURDLE_APR + smart_contract_risk_premium:
        continue

    # Position before snapshot if applicable
    if fork.snapshot_date and now < fork.snapshot_date:
        provide_liquidity(incumbent=fork.target, size=allocation)

    # Migrate at launch
    if fork.launched and not migrated:
        unstake_from(fork.target)
        stake_in(fork)
        migrated = True

    # Harvest and dump
    if rewards_claimable(fork) > MIN_CLAIM_USD:
        token = harvest(fork)
        sell_immediately(token, venue=best_liquidity_venue(token))

    # Exit before boost taper
    if days_until(schedule.boost_end) < EXIT_BUFFER_DAYS:
        exit_liquidity(fork)
```

## Indicators / data used

- DEX TVL by protocol (DefiLlama, Dune dashboards)
- Token emission schedule from contract source / governance docs
- LP token balances at known snapshot blocks
- Real-time DEX liquidity for harvest dumping (avoid being your own [[slippage|slippage]])
- Funding rates / perp open interest on the new token (signals when the market is fully aware)

## Example trade

> Illustrative, round numbers — not a backtest. Applies the rules from this page to a hypothetical DEX vampire attack.

**Setup:** A new DEX ("ForkSwap") announces it will fork a major AMM and pay 10% of its total FSWAP token supply (100 million FSWAP) as boosted LP rewards over a 4-week boost window. Anyone staking LP tokens on the incumbent DEX before a snapshot block earns double FSWAP during the first week.

**An arber's action (pre-snapshot + migrate + harvest + exit):**

**Phase 1 — Pre-snapshot positioning (Day −3 to Day 0):**
- Deposit $50,000 USDC + $50,000 ETH into the incumbent DEX ETH/USDC pool.
- Receive incumbent LP tokens worth ~$100,000.
- Capital at risk: $100,000 (plus normal AMM impermanent-loss exposure during holding).

**Phase 2 — Migration (Day 1, launch):**
- ForkSwap launches. Arber stakes incumbent LP tokens on ForkSwap to earn boosted FSWAP.
- Emission rate during boost week: 5 FSWAP per block (~28,800 blocks/day × 5 = 144,000 FSWAP/day).
- Arber's share of total staked TVL at launch: ~2% (assuming $5M total TVL at launch, $100k is 2%).
- Daily FSWAP earned: 144,000 × 2% = **2,880 FSWAP/day**.

**Phase 3 — Harvest and dump (Days 1–7):**
FSWAP launches at $1.50 on thin trading; arber begins selling each day into whatever liquidity exists.

| Day | FSWAP token price | FSWAP earned | Sold | Revenue | Cumulative sold |
|-----|-------------------|-------------|------|---------|----------------|
| 1 | $1.50 | 2,880 | 2,880 | $4,320 | $4,320 |
| 2 | $1.20 | 2,880 | 2,880 | $3,456 | $7,776 |
| 3 | $0.90 | 2,880 | 2,880 | $2,592 | $10,368 |
| 4 | $0.70 | 2,880 | 2,880 | $2,016 | $12,384 |
| 5 | $0.55 | 2,880 | 2,880 | $1,584 | $13,968 |
| 6 | $0.40 | 2,880 | 2,880 | $1,152 | $15,120 |
| 7 | $0.30 | 2,880 | 2,880 | $864 | $15,984 |

**Phase 4 — Exit before boost taper (Day 7):**
- Arber unstakes from ForkSwap and withdraws $100,000 liquidity (assuming 2% IL from ETH price move = −$2,000).

**Round-trip P&L:**

| Item | Amount |
|------|--------|
| FSWAP harvest revenue (7 days) | +$15,984 |
| Gas (7 claim + dump cycles on Ethereum L1, ~$150/cycle) | −$1,050 |
| Harvest dump slippage (avg 8% on thin liquidity, estimated) | −$1,279 |
| Impermanent loss on underlying LP position | −$2,000 |
| Smart-contract audit premium (cost of time to verify) | N/A (time cost, not cash) |
| **Net P&L on $100,000 deployed for 7 days** | **+$11,655** |

Annualised: +$11,655 / $100,000 × (365/7) ≈ **607% APY** during the boost period. After the boost ends, APR collapses to equilibrium (~15-30% at steady-state TVL of $50M+), so the arber is already gone. The strategy captures this window systematically, not repeatedly from the same fork.

## Worked example

The case below is documented public history used to illustrate the playbook; the profit range is an order-of-magnitude characterization, not a recorded backtest.

### Historical vampire / migration campaigns

| Campaign | Attacker → incumbent | Date | Outcome / migration captured |
|----------|----------------------|------|------------------------------|
| SUSHI vampire | [[sushiswap]] → [[uniswap]] | Aug-Sep 2020 | >$1B liquidity drained; incumbent responded with UNI token |
| BLUR points | [[blur]] → [[opensea]] | 2022-23 | Blur took 70%+ of NFT volume within weeks |
| Perp-DEX points wars | e.g. [[hyperliquid]] → [[gmx]] / CEXs | 2023-24 | Order flow / points campaigns (not strict forks) |

**Blur vs OpenSea, Feb 2023.** Blur launched its NFT marketplace in October 2022 with a points-based airdrop targeting OpenSea's bidders and listers. The Season 1 BLUR airdrop occurred on 2023-02-14. An arber who:

- Listed and bid on blue-chip NFTs through Blur from Nov 2022 through Feb 2023 (zero-fee for the trader, but eligible for points)
- Claimed the BLUR airdrop on day one
- Sold BLUR within 48 hours of claim near the launch-day spike (BLUR briefly printed above $5 on thin early listings before settling near $1)

...realised a 5-figure to low 6-figure profit on essentially zero capital outlay (the NFTs were collateral, not consumed). Blur captured 70%+ of NFT trading volume within weeks, which was the structural goal of the attack. BLUR subsequently traded down to under $0.30 by 2024-2025 — exactly the dilution the strategy is designed to escape.

## Performance characteristics

- Typical realised APR during boost period: **80% – 800%** annualised (highly variable, depends on token price)
- Typical drawdown: **40-60%** if the new token dumps faster than rewards accrue
- Gross profit is concentrated in the first 14-30 days of any given fork
- Costs: gas (significant on Ethereum L1, ~$50-500 per migrate/harvest cycle), [[slippage|slippage]] on harvest dumps (5-15% on illiquid new tokens), opportunity cost of capital locked in incumbent before snapshot

Net of costs, the strategy looks like a series of small-cap altcoin shorts dressed up as yield farming. Across a disciplined rotation of forks, the estimated portfolio-level Sharpe is on the order of **1.0-1.5** (frontmatter assumes 1.4) — but the distribution is lumpy and dominated by a few first-mover events.

> These figures are *characterizations of the trade type*, not a backtest. Realized APR is dominated by the new token's price path, which is precisely what the strategy tries to escape by harvesting and dumping continuously.

### Cost stack

| Cost | Magnitude | Notes |
|------|-----------|-------|
| Gas (migrate / harvest cycles) | ~$50-500 per cycle on ETH L1 | Cheaper on L2s; can dominate small positions |
| Harvest-dump slippage | 5-15% on illiquid new tokens | You are selling into the thin market you helped create |
| Pre-snapshot opportunity cost | variable | Capital locked in incumbent LP awaiting snapshot |
| Smart-contract risk reserve | binary tail | Cannot be hedged; sized via position cap |
| Tax / accounting overhead | indirect | Many claim/dump events across jurisdictions |

## Capacity limits

- **Per fork: $1M – $5M** before harvest dumping crashes the very token you're farming.
- **Aggregate: $5M – $20M** assuming 5-10 active forks per year and rotation discipline.
- Beyond that, you ARE the price action, and the trade self-cannibalises.

## What kills this strategy

- **Saturation.** When every farmer arrives on day one, realised APR collapses to risk-adjusted equilibrium. See SUSHI Sep 2020 → CRV → COMP → 2021 farms: each successive vampire attack paid less than the last.
- **Incumbent counter-attacks.** [[uniswap|Uniswap]] launched UNI on 2020-09-17 partly to neutralise SushiSwap's vampire incentive. Future incumbents have done the same proactively.
- **Smart-contract exploit or governance failure.** A handful of SushiSwap-era forks had critical bugs or trust failures — YAM's rebase bug bricked its governance within 36 hours of launch (Aug 2020), and SushiSwap itself suffered a confidence crisis when founder "Chef Nomi" sold the dev-fund SUSHI in Sep 2020 (later returned).
- **Token price collapses faster than rewards accrue.** If you can't harvest and dump every block, the realised APR diverges from the quoted APR.
- **Regulatory action.** SEC has signalled that governance tokens may be securities; airdrop recipients may have tax/registration exposure (see [[howey-test]]).

See [[failure-modes]] for the broader catalogue.

## Kill criteria

- Realised APR (after harvest slippage and gas) falls below HURDLE_APR for 7 consecutive days → exit fork.
- Token price down >50% in 24h → exit fork (the boost is over).
- Aggregate strategy drawdown >25% over rolling 90 days → pause and review.
- Two consecutive forks fail to produce profit after fees → suspend strategy entirely; the meta is dead.

## Advantages

- Asymmetric upside in early stages of a fork war
- Mostly on-chain and observable; no information asymmetry needed
- Repeatable pattern with multiple historical case studies (SUSHI, BLUR, HYPE, dYdX)
- Composable with [[liquidity-mining]] and [[airdrop-farming]] strategies
- Capital is mostly stablecoins or blue-chip ETH, not the speculative token itself

## Disadvantages

- Smart-contract risk is binary and cannot be hedged
- Crowded — most opportunities are arbed within hours of announcement now
- Tax accounting nightmare (claims, dumps, multiple jurisdictions)
- Reputational risk: the strategy is parasitic by design and degrades the host protocol
- Requires constant monitoring; passive holders get diluted

## Sources

- See [[2020-09-sushiswap-vampire-attack]] for the canonical case study.
- Dune dashboards on Blur points and BLUR distribution.
- DefiLlama emissions tracker.

## Related

- [[sushiswap]]
- [[uniswap]]
- [[airdrop-farming]]
- [[liquidity-mining]]
- [[liquidity-provider]]
- [[curve-gauge-wars-arbitrage]]
- [[2020-09-sushiswap-vampire-attack]]
- [[token-unlock-arbitrage]]
- [[restaking-token-arbitrage]]
- [[arbitrage]]
- [[limits-to-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[mev-strategies]]
