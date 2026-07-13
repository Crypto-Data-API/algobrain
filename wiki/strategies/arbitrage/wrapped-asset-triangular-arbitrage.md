---
title: "Wrapped Asset Triangular Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, defi, crypto, bitcoin, ethereum]
aliases: ["WBTC Arb", "Synthetic Asset Triangulation", "Cross-Wrapper Arbitrage"]
related: ["[[triangular-arbitrage]]", "[[multi-leg-arbitrage]]", "[[cross-chain-arbitrage]]", "[[lst-depeg-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[arbitrage]]", "[[limits-to-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [structural, analytical, risk-bearing]
edge_mechanism: "The same underlying asset (BTC, ETH, USDC) trades as multiple wrapped variants (WBTC, renBTC, tBTC, sBTC; ETH/wstETH/cbETH/rETH; USDC/USDC.e/axlUSDC) — each with its own custody model, peg mechanism, and liquidity venue. Wrappers depeg from underlying when redemption rails become impaired or when one wrapper's custodian faces solvency questions."
data_required: [wrapper-pool-reserves, custodian-attestations, redemption-status, multi-chain-prices]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 1.2
expected_max_drawdown: 0.4
breakeven_cost_bps: 30
decay_evidence: "Major wrapped-asset depegs are recurring 1-3 times per year. WBTC-BTC stayed near peg until BitGo-Justin Sun controversy August 2024 caused ~-1% depeg lasting 1-2 months; renBTC traded ~-19% to BTC when Ren protocol wound down December 2022."
---

# Wrapped Asset Triangular Arbitrage

Trading the price dislocations between **the same underlying asset wrapped in different tokens**. Bitcoin alone has had at least **8 separate wrapped variants** on Ethereum (WBTC, renBTC, tBTC, sBTC, hBTC, imBTC, pBTC, BTCB) — each with its own custody model and peg risk. Same applies to ETH (wstETH, cbETH, rETH, frxETH, ankrETH, sfrxETH), USDC (USDC, USDC.e, axlUSDC, USDC.poly, USDC.bsc), and USDT (USDT, USDT.e, USDT.poly, USDT.tron). When one wrapper's custodial mechanism is questioned, it depegs against the others — creating an arbitrage triangle.

## Edge Source

**Structural** + **analytical** + **risk-bearing**.

- **Structural:** Each wrapper has different redemption rails — some atomic on-chain, some require custodian KYC processes that take days.
- **Analytical:** Modeling the actual recovery probability and timing of a depegged wrapper is hard.
- **Risk-bearing:** The wrapper might never re-peg if the custodian is genuinely insolvent.

## Why This Edge Exists

For each "wrapped" token to maintain its peg, three conditions must hold:

1. **Reserve backing** — custodian holds 1:1 underlying asset.
2. **Open redemption** — anyone can swap wrapper for underlying without friction.
3. **Active arbitrage** — counter-traders capture small deviations and snap back to peg.

When any condition breaks (custodian solvency questioned, redemption frozen, arb-bot infrastructure fails), the wrapper depegs. Examples:

| Wrapper | Custodian | Major Depeg Event |
|---------|-----------|-------------------|
| WBTC | BitGo (later questioned BitGo-Justin Sun JV) | August 2024: ~-1% on Justin Sun ownership concerns, persisting 1-2 months; re-widened on Coinbase's WBTC delisting notice (Nov 2024) |
| renBTC | Ren protocol | November-December 2022: ~-19% as Ren wound down post-Alameda collapse |
| tBTC | Threshold Network | Multiple <0.5% wobbles 2020-2024 |
| HBTC | Huobi | 2022-2023: persistent -1-3% discount on Huobi solvency questions |
| BTCB | Binance | November 2022: -3% briefly during FTX week |
| stETH | Lido | June 2022: -6.5% during 3AC/Celsius forced selling |
| cbETH | Coinbase | Persistent -0.5-2% based on Coinbase regulatory risk |
| USDC.e | (bridged USDC) | Multiple -1-5% deviations vs native USDC during bridge issues |

Counterparty: long-only holders forced to exit one wrapper specifically; arbitrage bots without infrastructure for the specific custodian/chain.

## Null Hypothesis

Under no-edge conditions, a wrapper's discount is an unbiased market estimate of expected custodial loss: a token trading at -19% has roughly a 19% probability-weighted shortfall in redemption value, and buying every depegged wrapper earns zero in expectation — the renBTC-style permanent impairments exactly offset the WBTC-style recoveries. Small deviations (<30 bp) are just noise inside the redemption-cost band (mint/burn fees, gas, bridge fees, KYC delay carry), and the apparent "snap-back yield" is compensation already claimed by whoever bears the redemption friction. The test: across the full historical set of depeg events (not just the survivors), compute the recovery-weighted return of mechanically buying every wrapper that breaches the threshold — if it is not significantly positive after impairments like renBTC and the dead Huobi/bridge wrappers are included, the strategy is selection bias on events that happened to mean-revert. Genuine edge requires demonstrating that the custody-risk model prices recovery probability *better* than the market discount does.

## Triangular Trade Structure

Pre-depeg state (BTC example):
```
1 BTC = 1 WBTC = 1 renBTC = 1 tBTC = 1 hBTC (parity)
```

Depeg state (e.g. December 2022 renBTC wind-down):
```
1 BTC = 1 WBTC = 1 tBTC, but 1 renBTC = ~0.81 BTC (~19% discount)
```

Arbitrage trade:
1. **Buy renBTC at ~81% of BTC value.**
2. **Attempt redemption via Ren protocol** (the failing custodial leg) while the bridge still operates.
3. If redemption succeeds: capture the ~19% discount on the redeemed value.
4. If redemption fails: hold renBTC for potential recovery or sale — accepting that the discount can become a permanent impairment.

Triangulation across wrappers:
```
USDC → renBTC (cheap) → bridge to BTC → sell BTC → USDC (more)
```

## Rules

### Entry
1. Maintain monitoring on all major wrapper-pegs (WBTC, renBTC, tBTC, sBTC, stETH, cbETH, USDC variants).
2. Monitor custodian solvency signals: attestation cadence, audit reports, social media, regulator actions.
3. When deviation > 30 bp + custodial-risk premium AND the redemption rail is verified still operational:
   - Buy depegged wrapper.
   - Attempt redemption (immediate).
   - Hedge underlying exposure if redemption deferred.
4. **Gate on the rail, not the discount**: only enter if the bridge/redemption mechanism is confirmed live. A larger discount with a frozen rail is a trap, not an opportunity (renBTC after shutdown).

### Exit
1. **Redemption success** — burn the wrapper, receive native underlying, sell, realize the discount. This is the clean exit.
2. **Re-peg in secondary market** — if redemption is slow but the market re-converges (WBTC after BitGo reassurance), sell the wrapper back at/near parity.
3. **Cut on confirmed insolvency** — if attestations or on-chain reserves reveal genuine under-collateralization, exit at any bid rather than hold for a recovery that will not come.

### Position Sizing
- Size limit ~5-10% of fund per single wrapper — depeg events can be permanent (renBTC).
- Scale inversely with `custody_risk_score`: the higher the modeled impairment probability, the smaller the clip, because the deviation is then compensation for real loss, not mispricing.
- Cap aggregate exposure to any single custodian (BitGo, Coinbase, Lido) across wrappers — multiple wrappers can share one point of failure.

## Implementation Pseudocode

```python
wrappers = {"WBTC": btc_oracle, "renBTC": btc_oracle, "tBTC": btc_oracle,
            "stETH": eth_oracle, "cbETH": eth_oracle}

on tick:
    for wrapper, underlying in wrappers.items():
        observed_price = market.price(wrapper)
        underlying_price = oracle.price(underlying)
        deviation = (observed_price - underlying_price) / underlying_price
        custody_risk_score = custody_risk_model(wrapper)
        if deviation < -30bp - custody_risk_score:
            # depegged wrapper available cheap
            size = sizing(deviation, custody_risk_score)
            buy(wrapper, size)
            attempt_redemption(wrapper, size)
            if redemption_failed:
                hedge_underlying(short_size=size)
```

## Indicators / Data Used

- Curve / Uniswap pool reserves (for stETH, USDC variants).
- BitGo / Tether / Circle attestation reports.
- DefiLlama wrapper TVL tracking.
- Custodian Twitter / news monitoring.
- Bridge status feeds (LayerZero, Wormhole, Ronin).
- Coinbase / Binance custody disclosures.

## Example Trades

**WBTC depeg, August 2024.** BitGo announced a joint venture with Tron's Justin Sun for WBTC custody. Crypto community concerned. WBTC traded at up to ~-1% to BTC, with the discount persisting roughly 1-2 months (and re-widening when Coinbase announced WBTC delisting in November 2024). Merchants and funds that bought WBTC at a -0.5 to -1% discount and redeemed via BitGo (which honored redemptions throughout) captured ~0.3-0.8% net per cycle on size.

**renBTC wind-down, November-December 2022.** Ren Protocol's operations were Alameda-funded. After the FTX collapse on Nov 11, Ren had no funding to continue; the team announced a sunset of Ren 1.0 and urged users to bridge back to native BTC before shutdown. The renBTC discount to BTC widened to ~19% at the worst. Specialist DeFi funds bought discounted renBTC and bridged back to native BTC while the gateway still operated, capturing 10-19% per unit; holders who missed the redemption window were left with a stranded, deeply impaired token. Ren 1.0 officially shut down in December 2022.

**stETH depeg, June 2022 (covered separately):** Long stETH at 0.935 → hold to Shapella (April 2023) → +7% convergence. See [[2022-06-steth-depeg]].

**USDC.e / native USDC, August 2023:** USDC bridged to Avalanche (USDC.e) traded at -0.5-1% to native USDC after Circle introduced direct native USDC issuance on Avalanche. Bridge tokens slowly depegged as users migrated to native. Arbs profited from converting USDC.e via bridges.

**BUSD post-Paxos halt, February 2023:** NYDFS ordered Paxos to stop minting BUSD on February 13, 2023. BUSD initially held peg but slowly drifted as Binance and others migrated. Arbs short-BUSD-long-USDC made small but durable returns over 12 months as BUSD wound down.

## Performance Characteristics

Small but persistent edge: 5-15% annualized for dedicated wrapper-arb desks. Sharpe ~1.0-1.5. Lumpy returns concentrated around major depeg events (3-5 per year typical). The return distribution is the defining feature: a long tail of small redemption-arb captures (0.3-0.8% per WBTC-style cycle) plus a small number of large captures around genuine wind-downs (10-19% on the renBTC bridge-back) — offset by the rare but total loss when a wrapper is permanently impaired and never re-pegs. This is *not* a risk-free arbitrage; it is a custody-risk-bearing trade dressed in arbitrage clothing (see Null Hypothesis above and [[limits-to-arbitrage]]).

### Outcome taxonomy (why the edge is real but bounded)

| Outcome type | Example | Typical capture | Frequency |
|---|---|---|---|
| Temporary discount, custodian honors redemption | WBTC Aug 2024 (-1%) | +0.3 to +0.8% per cycle | Most common |
| Wind-down with working bridge | renBTC late 2022 (-19%) | +10 to +19% if you bridge before shutdown | Rare, lucrative |
| Slow migration to native issuance | USDC.e, BUSD post-Paxos | Small, durable spread over months | Occasional |
| **Permanent impairment** | renBTC for those who missed the window | **Total loss on the position** | The tail risk |

### Cost / friction stack

| Friction | Nature | Effect |
|---|---|---|
| Mint/burn + custodian fees | Per-redemption | Sets the ~30 bp no-trade band |
| Gas + bridge fees | Multi-chain hops | Eats small deviations entirely |
| KYC / redemption delay carry | Days of underlying exposure | Must be hedged or it becomes directional |
| Custody-risk premium | The whole point | The deviation must exceed it to be edge, not noise |

## Capacity Limits

Per-event $5-200M depending on wrapper liquidity and the depth of the redemption rail. Strategy-level capacity ~$500M dedicated capital across all wrappers, but this is *theoretical* capacity — in practice it is gated by (i) how much of the depegged wrapper actually exists and is for sale at the discount, (ii) the throughput of the redemption/bridge mechanism during stress (often the bottleneck, since the same stress that creates the depeg congests the bridge), and (iii) how fast the custodian processes large redemptions. A renBTC-style wind-down has microscopic effective capacity because the bridge is being shut down precisely when you want to use it.

## What Kills This Strategy

- Native multi-chain issuance (Circle CCTP eliminates USDC bridge variants).
- Wrapper consolidation (BTC wrapper market consolidated to ~5 viable wrappers post-2022).
- Improved custodian transparency reduces depeg frequency.
- Redemption-rail standardization.
- **Selection-bias collapse**: if the desk's apparent edge was only ever recovery survivors (WBTC) while ignoring the permanently impaired (renBTC), the realized edge across the *full* event set is near zero. See [[failure-modes]] and the Null Hypothesis.
- **Adverse selection at redemption**: the wrappers that depeg most are the ones most likely to *fail* redemption — buying the cheapest wrapper is often buying the one whose custodian is actually insolvent.

## Kill Criteria

- Average deviation across major wrappers below 5 bp for 90 days.
- No major depeg events in 18 months.
- Realized recovery-weighted return (including impairments) negative over a rolling 12-month window — the signal that the custody-risk model is mispricing recovery probability.
- Any single permanent-impairment loss exceeding 2x the trailing 12-month profit from the strategy.

## Advantages

- Decoupled from broad crypto beta (driven by idiosyncratic custody events, not market direction).
- Recurring opportunities (3-5 depegs per year).
- Natural hedge: long depegged wrapper + redemption arb is largely market-neutral *when redemption works*.
- High Sharpe in the recovery-dominated regimes because winners are frequent and losers are (usually) bounded.

## Disadvantages

- Permanent-depeg risk (renBTC) — the canonical total-loss tail.
- Custodian / regulatory headline risk drives the events but is unpredictable in timing.
- Complex multi-chain infrastructure required (bridges, custodian KYC desks, oracles per wrapper).
- Adverse selection: the deepest discount often signals genuine insolvency, not a buying opportunity.
- Returns are lumpy and event-driven — long stretches of nothing, making capital allocation awkward.
- Survivorship/selection bias makes naive backtests look far better than the live, full-event-set reality.

## Sources

- BitGo / Circle / Tether attestation reports.
- Ren Protocol post-mortem, December 2022.
- Lido stETH community analyses, June 2022.
- DefiLlama wrapper TVL dashboards.
- BlockSec / PeckShield wrapper-risk analyses.
- Verified via Perplexity (sonar), 2026-06-10: WBTC max discount ~1% post-BitGo/Sun announcement, persisting 1-2 months (protos.com, nydig.com, bitgo.com blog); renBTC discount ~19% during late-2022 wind-down; stETH ~7% discount June 2022.

## Related

[[arbitrage]] · [[triangular-arbitrage]] · [[multi-leg-arbitrage]] · [[cross-chain-arbitrage]] · [[lst-depeg-arbitrage]] · [[stablecoin-pair-arbitrage]] · [[2022-06-steth-depeg]] · [[2022-11-ftx-collapse-arbitrage]] · [[limits-to-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]]
