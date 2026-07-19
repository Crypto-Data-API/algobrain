---
title: "Stablecoin Yield"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: excellent
tags: [crypto, defi, derivatives, risk-management, arbitrage]
aliases: ["Stablecoin Yield", "Stablecoin Farming", "Stablecoin Income", "Cash-and-Carry Stablecoin Yield"]
related: ["[[stablecoin-yields]]", "[[stablecoins]]", "[[defi-yield-farming]]", "[[delta-neutral-yield-farming]]", "[[funding-rate-arbitrage]]", "[[aave]]", "[[impermanent-loss]]", "[[smart-contract-risk]]", "[[stablecoin-depegs]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "Leveraged crypto longs and protocols persistently demand dollar liquidity (via perp funding, borrow markets, and money-market issuance), and the stablecoin holder is paid a real yield for supplying that dollar liquidity while bearing depeg, counterparty, and smart-contract risk."
data_required: [stablecoin-balances, lending-rates, funding-rates, protocol-tvl]
min_capital_usd: 1000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 1.5
expected_max_drawdown: 0.10
breakeven_cost_bps: 20
---

Stablecoin yield is the practice of earning income on dollar-pegged tokens (USDC, USDT, DAI, etc.) without taking directional crypto exposure. Capital is deployed into lending markets, money-market/treasury-backed stablecoins, stablecoin-pair liquidity pools, or delta-neutral basis trades to harvest a dollar yield. It is the crypto analogue of a cash-management / money-market strategy, with returns ranging from ~3–5% (low risk, treasury-backed) to 10–30%+ (active, higher risk), and the key discipline is matching the yield source to its true risk. See the broader concept page [[stablecoin-yields]] for the market context, and [[stablecoins]] for the instruments themselves.

> **The one-sentence thesis.** Crypto has a chronic structural shortage of dollars; the stablecoin holder is paid for supplying them, and every basis point of that yield is either real interest, real fees, or a payment for bearing a tail risk — there is no fourth source. The whole skill of the strategy is decomposing the quoted APY into those three buckets and refusing to confuse the third for the first two. As the desk maxim goes: *if you cannot name where the yield comes from, you are the yield.*

This page covers the **strategy** of sourcing yield across the risk spectrum. It is closely related to but distinct from [[delta-neutral-yield-farming]] (the market-neutral construction), [[funding-rate-arbitrage]] (the perp-basis leg), and [[defi-yield-farming]] (the broader incentive-farming family).

## Edge source

**Structural** and **risk-bearing** (see [[edge-taxonomy]]). Structural: crypto markets have a chronic, structural demand for *borrowed dollars* — leveraged longs pay funding to be long perps, traders pay to borrow stablecoins against crypto collateral, and protocols issue yield-bearing stablecoins backed by T-bills. The stablecoin holder sits on the supply side of all three. Risk-bearing: the yield is genuine compensation for accepting [[stablecoin-depegs|depeg risk]], counterparty/custodial risk (CeFi), and [[smart-contract-risk]] (DeFi) — it is not a free lunch.

| Edge dimension | Present? | Mechanism |
|---|---|---|
| Structural | Primary | Chronic crypto demand for borrowed dollars: perp [[funding-rate-arbitrage|funding]], stablecoin borrow markets, tokenized-T-bill float |
| Risk-bearing | Primary | Yield is compensation for depeg, smart-contract, counterparty/custodial, and regulatory tail risk |
| Analytical | Secondary | Decomposing real yield vs. emissions; pricing the expected loss of each venue |
| Informational | Weak | Edge in spotting protocol/reserve red flags early before others de-risk |
| Behavioral | Weak | Counterparty to yield-chasers who over-pay for headline APY without pricing tail risk |
| Latency | No | Position-horizon strategy; no speed advantage required |

## Why this edge exists

Who pays the yield, and why do they keep paying? Leveraged speculators pay positive perp **funding** because they want directional crypto exposure and are willing to bleak carry for it; borrowers pay **lending interest** because they want to short, lever, or avoid selling collateral for tax reasons; and tokenized-treasury issuers pass through the **risk-free rate** (minus a spread) because they earn the float. As long as crypto attracts leveraged demand for dollars and short-term rates are positive, the supply side earns a spread. The "edge" is structural and durable, but it compresses when leverage demand falls (funding goes flat/negative) and it inverts catastrophically during depegs and protocol failures — which is exactly when the risk premium is realized.

## Null hypothesis

Under no edge, the quoted APY is illusory: it is paid in an emissions token that depreciates faster than the yield accrues, or it is "compensation" for a depeg/insolvency tail whose expected loss exactly offsets the carry, leaving zero or negative risk-adjusted return. The honest test: decompose every basis point of yield into its source (real interest, real fees, or token emissions), subtract the annualized expected loss from depeg + smart-contract + counterparty risk, and ask whether the *net, risk-adjusted, after-tax* return beats short-dated T-bills. If you cannot name where the yield comes from, assume you are the yield.

## Rules

**Tiering by risk (allocate top-down):**
- **Tier 1 (3–5%):** Tokenized T-bill / money-market stablecoins and blue-chip lending ([[aave]], Compound) on USDC/USDT/DAI. Treat as crypto cash.
- **Tier 2 (5–12%):** Stablecoin-pair liquidity (e.g., USDC/USDT on a stable-optimized AMM) — minimal [[impermanent-loss]] because both legs track $1, plus fees and incentives.
- **Tier 3 (10–30%+):** Delta-neutral basis (long spot / short perp to harvest [[funding-rate-arbitrage|funding]]) and leveraged/looped lending — see [[delta-neutral-yield-farming]].

| Tier | Indicative APY | Yield source | Dominant risk | Behaves like |
|---|---|---|---|---|
| Tier 1 | ~3–5% | T-bill float pass-through; senior lending interest | Issuer/custody, regulatory, redemption gating | Crypto cash / money-market fund |
| Tier 2 | ~5–12% | Stable-pair AMM fees + incentives | One leg depegs (correlated IL), smart-contract, emission decay | Short-vol fee harvesting |
| Tier 3 | ~10–30%+ | Perp [[funding-rate-arbitrage|funding]] basis; looped/levered lending | Funding flips negative, liquidation cascade, exchange failure | Carry / short-tail insurance |

Allocation discipline: fill Tier 1 first (the liquid buffer), then add Tier 2/3 *only with capital you can afford to see impaired*. The blended book should be describable as "X% cash-like, Y% fee carry, Z% basis carry," and you should be able to state the realistic worst-case loss of each sleeve before sizing it.

**Entry:** Deploy only to audited, battle-tested protocols with deep TVL and a track record through at least one stress event. Diversify across issuers and chains.

**Exit / monitoring:** Continuously monitor the peg, the underlying yield source, and protocol health. Exit immediately on (a) a meaningful depeg, (b) a sustained negative/zero funding regime that erases the basis carry, (c) governance or oracle red flags, or (d) yield collapsing toward the risk-free rate while risk stays elevated.

**Sizing:** Cap exposure per protocol and per stablecoin issuer (e.g., ≤ 20–25% of the sleeve in any one venue/token). Keep a liquid Tier-1 buffer to redeploy or de-risk fast.

## Implementation pseudocode

```python
def allocate_stablecoin_yield(capital, risk_budget):
    rf = treasury_bill_rate()                    # benchmark hurdle
    book = {}
    for venue in audited_venues():
        gross = quoted_apy(venue)
        real  = gross - emissions_apy(venue)     # strip depreciating token rewards
        expected_loss = depeg_p(venue) + exploit_p(venue) + counterparty_p(venue)
        net = real - expected_loss
        if net > rf + risk_budget.min_spread:
            w = min(risk_budget.per_venue_cap,
                    tvl_liquidity_cap(venue))
            book[venue] = w
    rebalance(book)

def monitor(book):
    for venue, w in book.items():
        if peg_deviation(venue) > 0.5e-2 \
           or funding_rate(venue) <= 0 and is_basis_trade(venue) \
           or protocol_health_flag(venue):
            exit(venue)                          # de-risk first, ask later
```

## Indicators / data used

- Quoted APY decomposed into real interest/fees vs. emissions (the critical screen)
- Lending utilization and supply/borrow rates ([[aave]], Compound)
- Perpetual [[funding-rate-arbitrage|funding rates]] for delta-neutral basis carry
- Peg deviation / oracle prices for depeg monitoring ([[stablecoin-depegs]])
- Protocol TVL, audit status, and reserve attestations for treasury-backed coins
- Short-dated T-bill rate as the risk-free hurdle

## Example trade

A trader holds $50,000 in USDC. They split it: $30,000 into a tokenized-treasury stablecoin yielding ~4.8% (Tier 1), $10,000 supplied to an Aave USDC market at ~6% utilization-driven APY (Tier 1/2), and $10,000 into a delta-neutral basis trade — long $10K spot ETH, short an equal-notional ETH perp — capturing ~12% annualized funding while staying market-neutral (Tier 3). Blended gross ~6.7%. When ETH funding flips negative for several days, they unwind the basis leg, parking that $10K back in the treasury coin until funding normalizes. The Tier-1 core keeps paying through the cycle with negligible directional risk.

## Performance characteristics

The low-risk core behaves like crypto cash: steady ~3–5% with very low volatility, so risk-adjusted Sharpe can look high (1.5+) — but that number *understates the tail*, because the dominant risk is a rare, severe depeg/insolvency loss rather than day-to-day variance. Active Tier-2/3 sleeves add a few hundred bps of yield at the cost of fatter left tails and operational complexity. Realistic, sober expectation: low-risk core barely beats T-bills after costs and tax; the incremental yield above ~6–8% is almost entirely a payment for taking on depeg, counterparty, or smart-contract risk. Gas/transaction costs make small balances inefficient for active strategies.

## Capacity limits

The treasury-backed and major lending venues absorb large size (tens to hundreds of millions) with little rate impact. Stablecoin LP pools and delta-neutral basis are capacity-limited by pool depth and open interest: large supply compresses lending rates and pushes funding toward neutral, shrinking the very yield being harvested. Practical sleeve capacity before self-impact dominates is roughly tens of millions across diversified venues; concentrated single-protocol size erodes returns and concentrates tail risk.

| Sleeve | Capacity character | Self-impact mechanism |
|---|---|---|
| Tier 1 (T-bill stables, blue-chip lending) | Largest — tens to hundreds of $M | Supplying lowers utilization-driven lend rate slightly |
| Tier 2 (stable-pair LP) | Pool-depth bound — single-digit to low tens of $M per pool | Your liquidity dilutes the fee share per dollar |
| Tier 3 (perp basis) | Open-interest bound — varies by venue | Large short-perp flow pushes funding toward zero, killing the carry |

## What kills this strategy

From [[failure-modes]]: **depeg events** (the marquee risk — UST collapsed to ~$0 in May 2022; even USDC briefly hit ~$0.88 during the March 2023 SVB scare), **smart-contract exploits / protocol insolvency** (total loss of deployed capital), **counterparty/custodial failure** in CeFi yield products, **regulatory action** against an issuer, and **yield compression** when leverage demand evaporates and funding/lending rates collapse, leaving risk uncompensated. Reflexivity matters: stress hits the peg, the yield, and exit liquidity simultaneously.

| Failure mode | Worst-case loss | Historical reference | Mitigation |
|---|---|---|---|
| Algorithmic / under-collateralized depeg | ~100% of principal | UST → ~$0, May 2022 | Avoid algo-stables; hold only audited, reserve-backed coins |
| Fiat-reserve depeg (bank exposure) | Temporary; can recover | USDC ~$0.88 during March 2023 SVB scare | Diversify issuers; watch reserve composition/attestations |
| Smart-contract exploit | Up to 100% of deployed | Numerous DeFi hacks (bridges, lending forks) | Battle-tested protocols, deep TVL, audits, cover where possible |
| CeFi counterparty/custodial failure | Up to 100% (unsecured) | Centralized lender insolvencies, 2022 | Prefer non-custodial; cap per-counterparty exposure |
| Regulatory action on issuer | Redemption freeze / forced unwind | Ongoing issuer scrutiny | Track jurisdiction/issuer regulatory posture |
| Yield compression | Edge → 0, capital idle | Flat/negative funding regimes | Rotate to Tier 1 / T-bills when net yield ≤ risk-free |

Note the reflexive correlation: in a stress event the peg breaks, the yield collapses, *and* exit liquidity dries up at the same moment, so "I'll just exit if it depegs" is partly an illusion — by the time the peg visibly breaks, the exit is already crowded. This is why pre-set, conservative kill criteria matter more here than in most strategies.

## Kill criteria

- Any held stablecoin deviates more than 0.5% from peg for a sustained period → exit that venue.
- Net (real minus expected-loss) yield on a sleeve falls below the T-bill rate → redeploy to cash.
- Funding turns zero/negative for a basis trade for several consecutive days → unwind the basis leg.
- Single-venue exposure exceeds 25% of the sleeve → trim.
- Loss of a protocol's audit standing, reserve attestation, or a governance/oracle red flag → immediate de-risk.

## Advantages

- Dollar-neutral income — earns yield without taking directional crypto risk.
- Tiered structure lets the trader dial risk precisely from T-bill-like to aggressive.
- Structural, recurring demand for dollar liquidity makes the core edge durable.
- Composable: pairs naturally with [[delta-neutral-yield-farming]] and [[funding-rate-arbitrage]].

## Disadvantages

- "Yield" can be a disguised risk premium for rare, catastrophic depeg/insolvency tails.
- Smart-contract, counterparty, and regulatory risks can wipe out principal entirely.
- Quoted APYs are often inflated by depreciating emission tokens.
- Yields compress hard in low-leverage regimes; active strategies need constant monitoring.
- Gas/transaction costs and tax treatment erode returns on small balances.

## Getting the Data (CryptoDataAPI)

Per-protocol lending rates and TVL come from the protocols/DeFiLlama; [[cryptodataapi|CryptoDataAPI]] serves the stablecoin supply/flow layer, the funding rates behind the Tier-3 basis sleeve, and the depeg/security monitor behind the kill criteria.

**Live data:**
- `GET /api/v1/sentiment/stablecoins` — stablecoin market cap with 14d/90d flows precomputed (the dry-powder and sector-health gauge)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — cross-exchange funding: the viability check for the delta-neutral basis sleeve
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score: the automated watch behind the "exit on meaningful depeg / protocol red flag" rule
- `GET /api/v1/event/regime` — forward catalyst calendar including depeg-risk bias

**Historical data:**
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — daily stablecoin history (z-score the flows)
- `GET /api/v1/market-intelligence/stablecoin-history` — long-run stablecoin mcap timeseries
- `GET /api/v1/backtesting/funding` — Hyperliquid hourly funding since 2023-05 (Binance daily since 2026-03-30): the basis-carry replay

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/stablecoins"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the monitoring loop this strategy lives or dies on:

- **Basis-sleeve switch** — poll `GET /api/v1/derivatives/funding-rates` each funding interval; several consecutive zero/negative readings fire the "unwind the basis leg, park in Tier 1" rule automatically
- **Depeg monitor** — `GET /api/v1/security/regime` and `GET /api/v1/security/events` as the always-on tripwire; act on the score, don't wait to observe the peg break (by then the exit is crowded, per the reflexivity note above)
- **Dry-powder trend** — falling supply with negative 14d/90d flows in `GET /api/v1/sentiment/stablecoins` warns that leverage demand — the source of Tier-3 yield — is draining
- **Backtest** — replay the funding-carry sleeve on `GET /api/v1/backtesting/funding` (HL hourly since 2023-05) to estimate realistic carry net of flat/negative regimes; stablecoin-flow features backfill from the 365-day remote history
- **Tips** — the hurdle is always the T-bill rate: have the agent recompute net-of-expected-loss yield vs risk-free before every rebalance, per the null hypothesis above

## Sources

- [[stablecoin-yields]] (wiki concept page) — yield-source taxonomy and risk framing.
- Tether / Circle reserve attestations and tokenized-treasury (e.g., money-market stablecoin) documentation — Tier-1 yield mechanics.
- Aave and Compound protocol docs — lending-rate mechanics.
- Public post-mortems of the May 2022 UST depeg and March 2023 USDC depeg — tail-risk evidence.

## Related

- [[stablecoin-yields]]
- [[stablecoins]]
- [[defi-yield-farming]]
- [[delta-neutral-yield-farming]]
- [[funding-rate-arbitrage]]
- [[aave]]
- [[impermanent-loss]]
- [[smart-contract-risk]]
- [[stablecoin-depegs]]
- [[carry-trade]]
- [[risk-management]]
- [[edge-taxonomy]]
- [[failure-modes]]
