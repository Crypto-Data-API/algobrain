---
title: "Points Farming"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [crypto, defi, points, airdrops, loyalty, sybil, protocols, farming, token-generation-event, expected-value]
aliases: ["Points Meta", "Loyalty Points Farming", "Points Season", "Pre-TGE Farming"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: intermediate

backtest_status: untested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [informational, risk-bearing, behavioral]
edge_mechanism: "Protocols hand out proprietary points to bootstrap TVL, liquidity, and attention before a token exists; the points farmer supplies that capital and activity in exchange for a lottery ticket on future token dilution, and is paid an expected-value premium for bearing conversion uncertainty, lockup, and Sybil-disqualification risk the protocol offloads onto early users."

# Data and infrastructure requirements
data_required: [points-balance, program-tvl, token-price-post-tge, fdv, unlock-schedule, opportunity-yield, gas-cost]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: high

# Performance expectations (net of opportunity cost, gas, and conversion risk)
expected_sharpe: 0.7
expected_max_drawdown: 0.40
breakeven_cost_bps: 60

# Decay history
decay_evidence: "Points-to-token conversions ranged from spectacular (Hyperliquid HYPE, Nov 2024, ~$1,000s per active user) to disappointing (multiple 2024 L2/DeFi programs converted at low ratios or dumped post-TGE). Per-point value has compressed as every protocol copied the points playbook and farmers spread thin across dozens of concurrent programs; 2024-2025 Sybil purges (e.g. LayerZero) zeroed large cohorts."

# Kill criteria (numeric — see [[when-to-retire-a-strategy]])
kill_criteria: |
  - modelled EV per program < opportunity yield on the same capital for 30+ days
  - Sybil-disqualification probability on the wallet cluster > 30%
  - protocol misses a credibly-signalled TGE window by > 6 months (dead-money flag)
  - post-TGE tokens realise < 25% of pre-TGE modelled value across last 3 harvests
  - capital lockup extends beyond the modelled farming horizon without a yield offset

related: ["[[airdrop-farming]]", "[[restaking-strategies]]", "[[defi-yield-farming]]", "[[expected-value]]", "[[kelly-criterion]]", "[[hyperliquid]]", "[[ethena-usde]]", "[[eigenlayer]]", "[[funding-rate-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Points Farming

Points farming is the practice of deploying capital and on-chain activity into pre-token crypto protocols to accumulate proprietary "points" that are expected to convert into a governance token at a future token generation event (TGE). Since 2023, protocols have used points instead of direct token rewards to bootstrap TVL and attention while deferring the TGE — [[eigenlayer]] restaking points, Blast points/gold, [[ethena-usde|Ethena]] sats/shards, and [[hyperliquid]] points are the canonical programs. The correct way to run it is as an **expected-value portfolio**: points are lottery tickets with an unknown conversion ratio, and the only durable edge is disciplined EV sizing net of opportunity cost, dilution, and Sybil risk — not "farm everything."

## Edge source

Mapping to [[edge-taxonomy]]:

- **Informational (primary).** The edge is *selection*: identifying which programs will (a) actually TGE, (b) convert points into meaningful allocation, and (c) hold value post-launch. This requires reading each program's mechanics, backer quality, TVL trajectory, and points-emission schedule better than the crowd.
- **Risk-bearing (secondary).** The farmer is paid an EV premium for bearing conversion uncertainty (ratio unknown until TGE), capital lockup/illiquidity, and Sybil-disqualification risk that the protocol deliberately offloads onto early users.
- **Behavioural (tertiary).** Protocols exploit farmer FOMO — leaderboards, multipliers, referral loops — to extract more TVL and activity than the eventual airdrop justifies. The disciplined farmer's edge is *not* being the one who overpays; the marginal farmer chasing a top-of-leaderboard rank usually does.

There is **no latency or analytical-pricing edge**. Points balances and rules are public; the edge is EV discipline and selection.

## Why this edge exists / who's on the other side

- **The protocol** gets cheap, sticky TVL, liquidity, and a decentralised holder base in exchange for future token dilution — a trade it is happy to make because the tokens it hands out did not exist before and cost it nothing but future float.
- **VCs and the team** get a bootstrapped network and regulatory optics (a "community distribution") that improve the token's launch narrative.
- **Later token buyers** on the open market absorb the tokens farmers were allocated — the farmer's exit liquidity.
- **The over-eager marginal farmer** who deploys more capital and burns more gas than the EV justifies subsidises the disciplined farmer's better selection.

The protocol is buying growth with future dilution; the farmer is selling early capital and activity for a claim on that dilution. The transfer only pays the farmer who sizes by EV, not the one who chases points for their own sake.

## Null hypothesis

Under no edge, points have zero net value after costs:

- Modelled EV per program ≈ 0 once opportunity yield, gas, and lockup are subtracted.
- The points-to-token ratio is unknowable ex ante, so expected allocation value equals the risk-free deployment of the same capital.
- Post-TGE tokens dump to their dilution-adjusted fair value immediately, erasing any "allocation" premium.
- Sybil detection makes multi-wallet farming EV ≤ single-wallet EV (extra wallets add cost and disqualification risk without adding expected allocation).

The record is mixed, which is exactly why EV discipline matters. Some programs (Hyperliquid) massively rejected the null — active users received five-figure allocations. Many others confirmed it — points converted at low ratios or the token dumped below the yield the same capital would have earned in a stablecoin vault. The **base-rate EV across all programs, net of costs and Sybil risk, is far lower than the survivorship-biased highlight reel suggests.** A points book whose modelled, cost-corrected EV per program sits below opportunity yield for 30+ days is living in the null world.

## Rules

### Entry

1. **EV gate.** Only enter a program whose modelled `EV = p(TGE) × p(eligible | TGE) × E[allocation_value] − gas − lockup_opportunity_cost` exceeds the opportunity yield on the same capital (e.g. ~5-15% from [[funding-rate-arbitrage]] or a stablecoin vault). See [[expected-value]].
2. **Backer/mechanics filter.** Credible backers, a live product, a plausible token, and a points schedule that is not already so diluted that late entry earns dust.
3. **TVL-share sizing.** Points typically accrue per-dollar-per-day; your expected allocation is roughly your share of total program point-days. Enter early enough (and before the crowd) that your share is meaningful.
4. **Genuine, non-Sybil activity.** One well-behaved primary wallet doing real, diverse activity beats a Sybil cluster the protocol can detect and zero.
5. **Lockup check.** Confirm whether deposited capital is locked/illiquid during the farming window and price that opportunity cost in.

### Exit / harvest

1. **TGE claim** — claim promptly (claim windows are finite), then decide sell-vs-hold on the token's fundamentals and unlock schedule.
2. **EV compression** — if modelled EV drops below opportunity yield (points over-diluted, TGE delayed indefinitely), withdraw and redeploy.
3. **Sell discipline** — for heavily-diluted tokens with large VC unlock cliffs, sell into TGE liquidity; hold only where fundamentals and float genuinely warrant it.
4. **Dead-money flag** — a program that misses a credibly-signalled TGE by > 6 months is treated as capital drag; exit.

### Sizing

- **EV-weighted across 5-10 programs** — diversify because most individual programs disappoint; the portfolio, not any single ticket, is the strategy.
- **Cap per program** ≤ 20% of the farming sleeve.
- **Dilution haircut** — discount headline "points value" estimates heavily for unlock cliffs and post-TGE sell pressure.
- **Fractional-Kelly** on the EV estimate given how wide and fat-tailed the outcome distribution is (see [[kelly-criterion]]).

## Implementation pseudocode

```python
# points_farm.py — EV-gated allocation across concurrent points programs
OPPORTUNITY_APR   = 0.10     # what the same capital earns risk-adjusted elsewhere
EV_MARGIN         = 0.05     # require modelled EV to beat opportunity by >=5%
MAX_PER_PROGRAM   = 0.20
SYBIL_KILL_P      = 0.30     # disqualification prob that voids a wallet cluster
DILUTION_HAIRCUT  = 0.50     # discount headline allocation for unlocks/sell pressure

def program_ev(p_tge, p_eligible, exp_alloc_value_usd, capital,
               horizon_yrs, gas_usd):
    gross = p_tge * p_eligible * exp_alloc_value_usd * (1 - DILUTION_HAIRCUT)
    opp_cost = capital * OPPORTUNITY_APR * horizon_yrs
    return (gross - opp_cost - gas_usd) / capital     # EV as return on capital

def decide(prog, book):
    # prog: name, p_tge, p_eligible, exp_alloc_value_usd, capital, horizon_yrs,
    #       gas_usd, sybil_p, tge_overdue_months, last3_realisation_ratio
    pos = book["positions"].get(prog.name)

    if prog.sybil_p > SYBIL_KILL_P:
        return {"action": "AVOID", "program": prog.name, "reason": "sybil risk"}
    if pos and prog.tge_overdue_months > 6:
        return {"action": "EXIT", "program": prog.name, "reason": "dead money"}

    ev = program_ev(prog.p_tge, prog.p_eligible, prog.exp_alloc_value_usd,
                    prog.capital, prog.horizon_yrs, prog.gas_usd)

    if pos:
        if ev < OPPORTUNITY_APR:        # compressed below opportunity cost
            return {"action": "WITHDRAW", "program": prog.name, "reason": "EV compressed"}
        return {"action": "HOLD", "program": prog.name}

    if ev - OPPORTUNITY_APR < EV_MARGIN:
        return {"action": "SKIP", "program": prog.name, "reason": "EV below hurdle"}
    size = min(MAX_PER_PROGRAM * book["sleeve_capital"], prog.capital)
    return {"action": "ENTER", "program": prog.name, "notional": size,
            "wallet": "single-genuine", "reason": f"EV {ev*100:.1f}%"}
```

## Indicators / data used

- **Points balance & accrual rate** — from the protocol dashboard; your share of total point-days ≈ your expected allocation share.
- **Program TVL & points-emission schedule** — rising TVL against a fixed points pool dilutes per-dollar accrual.
- **p(TGE) and TGE timeline** — from team signalling, backer behaviour, and comparables.
- **Comparable conversion ratios** — historical points→FDV realisations for similar programs (heavily survivorship-biased; discount).
- **FDV / unlock schedule** — the dilution haircut; large VC cliffs mean the "allocation value" evaporates at unlock.
- **Opportunity yield** — the risk-adjusted return the same capital earns elsewhere (funding-arb, stablecoin vault) — the EV hurdle.
- **Post-TGE token price/liquidity** — to time the sell (CryptoDataAPI, see below).

Points balances and program TVL come from protocol dashboards; CryptoDataAPI values and times the resulting token.

## Example trade

**Setup (2026-04-19):** farmer allocates **$50,000** across three EV-screened programs, each modelled before entry.

1. **$20,000** into a restaking LRT (ether.fi-style) for dual [[eigenlayer|EigenLayer]] + LRT points. Modelled `p(TGE)=0.9`, `p(eligible)=0.95`, `E[alloc]=$3,500`, 4-month horizon. Base yield ~5% offsets most opportunity cost → **modelled EV ≈ +11% on the $20k**. Enter.
2. **$15,000** bridged to an L2 points program. Modelled `p(TGE)=0.6`, `p(eligible)=0.7`, `E[alloc]=$2,000` after 50% dilution haircut, no base yield, 6-month lockup at ~10% opportunity cost. **Modelled EV ≈ +3%** — marginal; size at half-cap.
3. **$15,000** into a stablecoin-synth program (Ethena-style sats). Modelled EV positive and the capital earns base yield while farming → enter.

**Harvest (4-6 months):** Program 1 TGEs; points → tokens worth **$3,200** (near model). Program 2 TGEs but converts below model and dumps → tokens worth **$900** vs $2,000 expected. Program 3 pending. Realised so far: **$4,100 on $50k** deployed over ~5 months (~9.8% period return, ~20% annualised) **plus** ~$1,500 of base yield earned while farming.

**Net after costs:** subtract ~$300 gas/bridge and the opportunity cost already netted → **net ~+$5,300 on $50k over ~5 months** — but note Program 2 alone would have been *EV-negative net of costs* had base yield not partly offset it, which is exactly why the EV gate and diversification matter. A farmer who instead chased the highest-leaderboard-rank program with the whole $50k and got Sybil-flagged would be down gas with zero allocation.

## Performance characteristics (realistic cost overlay)

The old "10-100%+ returns" framing is survivorship bias. Cost-corrected, portfolio-level:

| Metric | Value | Note |
|---|---|---|
| Median program outcome | slight loss to modest gain | Most programs disappoint; the portfolio is carried by the top 1-2. |
| Portfolio net return | 5-25% per cycle | Highly regime- and selection-dependent; not annualised-stable. |
| Expected Sharpe | ~0.7 | Wide, fat-tailed, positively-skewed outcome distribution. |
| Max drawdown | up to 40% | Sybil purge + dead-money programs + TGE dumps in a bad cycle. |
| Breakeven cost budget | ~60 bps of capital | Gas, bridge, and lockup opportunity cost. |

**Cost overlay (never naive):**

- **Opportunity cost (dominant)** — the same capital could earn ~5-15% risk-adjusted (funding-arb, stablecoin vault). Every point-farm must clear that hurdle; most barely do net of dilution.
- **Gas & bridge fees** — deposits, activity, claims, and withdrawals across chains; tens to low-hundreds of dollars per program.
- **Lockup illiquidity** — capital locked pre-TGE cannot rotate to a better opportunity; a real, often-ignored cost.
- **Sybil-disqualification probability** — multi-wallet clusters carry a nonzero chance of a zeroed allocation.
- **Dilution / unlock cliffs** — headline "allocation value" is pre-dilution; large VC unlocks and TGE sell pressure routinely halve or worse the realised value — hence the 50% haircut in the model.
- **Smart-contract risk** — pre-TGE protocols are newer and less audited.

## Capacity limits

Individually small. Because points accrue per-dollar of TVL, deploying more capital into one program raises your allocation share **sublinearly** — many programs cap multipliers or use diminishing curves, and a whale deposit simply dilutes the per-dollar point rate for everyone (including yourself). Practical per-program capacity for an operator is **low hundreds of thousands to a few million** before your own size erodes point-per-dollar and draws Sybil/greylist attention. `capacity_usd` of $5M reflects a diversified farmer spread across many concurrent programs; a single mega-deposit into one program is self-defeating.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Sybil crackdown (Failure Mode #7, operational).** Protocols hire analytics firms (Nansen, Chaos Labs) and run clustering; flagged clusters get zeroed. 2024-2025 purges wiped large cohorts.
2. **Low conversion / TGE dump (Failure Mode #5, regime change).** Points convert at a low ratio, or the token dumps below the yield the capital would have earned elsewhere.
3. **Crowding (Failure Mode #4).** Every protocol copied the points playbook; farmers spread thin across dozens of programs, compressing per-point value.
4. **No TGE / rug (Failure Mode #6, tail).** The protocol never launches a token, or rugs — gas and lockup are sunk.
5. **Opportunity cost bleed.** The single most common quiet failure: capital tied up in EV-marginal programs that never beat the risk-free deployment.
6. **Tax/accounting drag.** Points→token receipts are taxable income at FMV; tracking across programs erodes net returns.

## Kill criteria

Pause or exit a program on any of:

1. **Modelled EV < opportunity yield for 30+ days.**
2. **Sybil-disqualification probability on the wallet cluster > 30%.**
3. **TGE missed by > 6 months** past a credible signal (dead-money flag).
4. **Last 3 harvests realised < 25% of modelled value** (model is broken — recalibrate or stop).
5. **Lockup extends beyond the modelled horizon** without a yield offset.

Re-enter only when a fresh EV model clears the hurdle. See [[when-to-retire-a-strategy]].

## Advantages

- **Stackable** — points accrue *on top of* base yield from staking/lending/LP, so a well-chosen program is nearly free optionality.
- **Asymmetric upside** — the occasional Hyperliquid-scale conversion pays for many misses.
- **Early access / alpha** — deep familiarity with new protocols before the crowd.
- **Portfolio-diversifiable** — running 5-10 programs smooths the fat-tailed single-program outcome.
- **Low minimum** — works from a couple thousand dollars.

## Disadvantages

- **Uncertain conversion** — the points-to-token ratio is revealed only at TGE; many disappoint.
- **Opportunity cost** — capital could earn guaranteed yield; EV-marginal programs quietly lose to it.
- **Sybil risk** — multi-wallet farming is increasingly detected and zeroed.
- **Lockup / illiquidity** — pre-TGE capital cannot rotate to better opportunities.
- **Dilution & dumps** — headline allocation value is routinely halved by unlock cliffs and TGE sell pressure.
- **Protocol risk** — pre-TGE protocols are newer and less audited.
- **Survivorship bias** — the highlight reel massively overstates the base-rate EV.

## Sources

- [[hyperliquid]] — HYPE (Nov 2024), the canonical large-conversion points program.
- [[eigenlayer]] — restaking points → EIGEN; the program that popularised the points meta.
- [[ethena-usde]] — sats/shards → ENA; a points program with a genuine underlying yield.
- LayerZero / assorted 2024-2025 L2 & DeFi points programs — Sybil purges and low-conversion disappointments (contemporaneous coverage).
- [[airdrop-farming]] — the predecessor strategy; points formalise and defer the same airdrop dynamic.
- [[restaking-strategies]] — a primary source of dual-layer (protocol + LRT) points.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not track proprietary points balances (those live on protocol dashboards) — it is used to **value and time the resulting token** and to screen new launches.

**Live data:**
- `GET /api/v1/coins/search?q=<protocol>` — locate the token once a TGE is announced
- `GET /api/v1/coins/{symbol}` — token profile (market cap, supply) for the airdropped token
- `GET /api/v1/market-data/ticker/price?symbol=<TOKEN>USDT` — current price for sell-timing
- `GET /api/v1/dex/new-pools` — newest multi-chain launches (early TGE liquidity)
- `GET /api/v1/dex/trending` — trending DEX pools (post-TGE liquidity/volume)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=<TOKEN>USDT&interval=1h&limit=500` — post-TGE price path (dump vs hold decision)
- `GET /api/v1/backtesting/klines` — deep archive for comparable post-TGE token behaviour

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/coins/search?q=ethena"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-coins]], [[cryptodataapi-dex]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **TGE watch** — `GET /api/v1/coins/search?q=<protocol>` + `GET /api/v1/dex/new-pools` catch the token and its first liquidity the moment a TGE lands
- **Sell-timing** — hourly `GET /api/v1/market-data/klines?symbol=<TOKEN>USDT&interval=1h` drives the dump-vs-hold branch; `GET /api/v1/event/calendar` (unlock filter) flags the cliff dates that routinely halve realised value
- **Regime gate** — `GET /api/v1/quant/market` — points convert into far less USD when the TGE lands in a bear state; feed the regime into the conversion-value haircut of the EV model
- **Backtest** — comparable post-TGE price paths from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d to 2017-08) calibrate the base-rate conversion haircut; points balances themselves have no API history — archive the protocol dashboards yourself
- **Tips** — respect `new_listing` flags on TGE tokens (thin history distorts signals); pull supply/dilution from `GET /api/v1/coins/{symbol}` at decision time, not from the announcement thread

## Related

- [[airdrop-farming]] — the predecessor / sibling strategy.
- [[restaking-strategies]] — dual-layer points source.
- [[defi-yield-farming]] — the base yield points farming layers on.
- [[expected-value]] / [[kelly-criterion]] — the sizing framework this strategy lives or dies by.
- [[hyperliquid]] / [[ethena-usde]] / [[eigenlayer]] — canonical programs.
- [[funding-rate-arbitrage]] — a common opportunity-cost benchmark for the EV gate.
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]] — methodology.
