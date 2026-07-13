---
title: "Stablecoin Pair Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, defi, mean-reversion, event-driven]
aliases: ["Stablecoin Depeg Arb", "USDC Arb", "Stable Pair Trade", "Stable Basis Arb"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, defi]
complexity: intermediate
backtest_status: paper-traded
edge_source: [structural, behavioral]
edge_mechanism: "Stablecoins are designed to peg to $1 via different mechanisms (reserves, over-collateralization, algorithmic). Temporary depegs from panic, banking issues, or redemption frictions revert when the redemption mechanism re-asserts itself."
data_required: [stable-prices, curve-3pool, redemption-status, reserve-attestations, banking-status]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 1.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 20
decay_evidence: "Major depeg events ~1-2 per year; profile depends on banking/regulatory environment."
related: ["[[funding-rate-arbitrage]]", "[[lst-depeg-arbitrage]]", "[[depeg-risk]]", "[[curve-finance]]", "[[2022-05-terra-luna-depeg-arb]]", "[[circle]]", "[[tether]]", "[[makerdao]]", "[[ethena]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[cross-chain-contagion-hedge]]", "[[ai-amplified-exploit-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[2017-2020-tether-banking-premium]]", "[[2020-03-dai-black-thursday]]", "[[2023-02-busd-wind-down]]", "[[2026-04-kelp-stable-sympathy-depeg]]", "[[stablecoin-depeg-history]]"]
---

# Stablecoin Pair Arbitrage

Stablecoin pair arbitrage exploits temporary deviations between fiat-pegged stablecoins (USDC, USDT, DAI, FRAX, USDe) when one breaks its peg due to redemption stress, banking risk, or collateral concerns. The canonical trade is the **March 10–13, 2023 USDC/SVB weekend**, when USDC fell to **$0.8774** on Saturday March 11 and recovered to ~$1.00 by Monday afternoon after the FDIC backstop announcement — yielding ~14 cents per dollar in 48 hours for the patient buyer.

> **Companion strategy**: this page focuses on **fiat-backed stablecoins** where the peg-restoration path is the banking system reopening. For **synthetic / algorithmic / over-collateralized** stables (sUSDe, GHO, crvUSD, FRAX hybrid, sDAI, Ethena white-labels) where the peg-restoration mechanism is internal to the protocol — perp funding, collateral health, AMM bands — see [[synthetic-stablecoin-depeg-arbitrage]]. The two strategies are complements: same conceptual edge (mean-reversion on peg deviations) but different mechanism-specific break modes, monitoring, and execution paths. Run both for full-spectrum stable-depeg coverage. **For tactical execution detail across both — how to maximize profit once you've decided to enter (7 distinct profit-capture methods including risk-free redemption arb, leveraged borrow-and-redeem, AMM band capture, options skew) — see [[stablecoin-depeg-profit-capture]].**

## Edge Source

**Structural** + **behavioral** (see [[edge-taxonomy]]). Different stablecoins use different mechanisms to maintain their peg:

- **Fiat-backed (USDC, USDT, BUSD):** 1:1 cash/T-bill reserves; redemption requires KYC and banking infrastructure
- **Over-collateralized (DAI, LUSD):** crypto collateral (typically 150%+) with on-chain liquidation
- **Algorithmic (FRAX hybrid, ex-UST):** mix of collateral + market mechanism

When the redemption channel jams (banking holiday, exchange halts withdrawals, oracle failure), price can deviate sharply from $1. Capital that can wait through the friction collects the spread.

## Why This Edge Exists

Crypto markets trade 24/7 but stablecoin redemptions clear on banking-system schedules (T+1, business days only). Friday-evening crises that can't be redeemed until Monday create windows where panic sellers meet only patient bidders. Plus:

- Many DeFi protocols are forced to swap at any price (oracle liquidations, automated treasury ops)
- Retail panic sellers have no fundamental view, only "get out"
- Exchange withdrawal halts trap supply, forcing on-chain selling
- Cross-stablecoin arb on [[curve-finance]] 3pool is the primary venue and depth/imbalance signals are public

## Null Hypothesis

If all stablecoins were instantly redeemable 1:1 with no friction, the cross-spread would oscillate within fee bands (~5–10 bps). Multi-percent deviations lasting hours-to-days reject that null.

## Rules

### Entry

1. **Trigger:** A stablecoin trades >50 bps off peg AND a clear catalyst exists (banking issue, depeg, exchange halt).
2. **Verify the depeg is temporary:** Check redemption channel status (Circle attestations, Tether banking, Maker collateral health).
3. **Avoid algorithmic stables in death spirals** (UST May 2022 was a value trap, not an arb).
4. **Long the cheap stable, short the expensive stable** (e.g., Long USDC at $0.88, short USDT at $1.02 = ~14 cents spread).
5. **Sizing:** Cap at depth available without >0.5% slippage on Curve 3pool.

### Exit

1. **Peg restoration** within 30 bps of $1.00 → close
2. **Redemption** via official channel (Circle USDC redemption, Tether USDT redemption) when channel reopens
3. **Catalyst resolution** (FDIC announcement, banking partner replacement, audit publication)
4. **Stop-out** if depeg deepens past entry by 2x AND the redemption mechanism is materially impaired (run, don't add)

### Position Sizing

Critical to avoid full-portfolio exposure to a single stable. Cap each stable at 25% of arb capital. For depegs, use scaling-in: enter 25% of position at first threshold, add to 50% at deeper thresholds, reserve final 25% for capitulation lows.

## Implementation Pseudocode

```python
def stablecoin_pair_arb():
    prices = {"USDC": p_usdc(), "USDT": p_usdt(), "DAI": p_dai(),
              "FRAX": p_frax(), "USDe": p_usde()}

    # find widest spread
    cheapest = min(prices, key=prices.get)
    richest  = max(prices, key=prices.get)
    spread   = prices[richest] - prices[cheapest]

    if spread > 0.005 and redemption_channel_ok(cheapest):
        notional = sizing_function(curve_3pool_depth())

        long_leg  = buy(cheapest, notional)
        short_leg = sell(richest, notional)             # via Curve swap or borrow+sell

        while spread > 0.0005:
            if redemption_open(cheapest):
                redeem(cheapest, long_leg)              # convert to USD via issuer
            wait()
        unwind_both()
```

## Indicators / Data Used

- **Spot stable prices:** Coinbase, Kraken, Binance, Curve TWAP
- **[[curve-finance]] 3pool composition:** % USDC / % USDT / % DAI (imbalance signals stress)
- **Issuer attestations:** Circle (monthly), Tether (quarterly)
- **Banking news:** SVB, Signature, Silvergate health (proxy for USDC, USDT, BUSD reserves)
- **Maker DAO Peg Stability Module (PSM) utilization** — backstop signal for DAI
- **CEX deposit/withdrawal status** — exchange halts indicate stress
- **Tether premium** — historically 10–15% premium on Bitfinex during 2018–2020 banking issues

## Example Trade — USDC/SVB Weekend (March 10–13, 2023)

| Date / Time (UTC) | USDC | USDT | DAI | Event |
|------|------|------|-----|-------|
| Fri Mar 10, 14:00 | 0.998 | 1.001 | 0.997 | SVB closed by California regulator |
| Fri Mar 10, 22:00 | 0.97 | 1.005 | 0.97 | Circle confirms $3.3B at SVB |
| Sat Mar 11, 02:00 | 0.92 | 1.013 | 0.93 | Asian session panic |
| Sat Mar 11, 12:00 | **0.8774** | **1.025** | 0.885 | Capitulation low |
| Sun Mar 12, 22:00 | 0.97 | 1.008 | 0.97 | Fed/FDIC/Treasury joint statement: depositors made whole |
| Mon Mar 13, 16:00 | 0.999 | 1.001 | 0.999 | Peg restored, Circle redemptions reopen |

**The trade:**

1. **Entry Sat Mar 11, 12:00:** Buy 1,000,000 USDC at $0.88 = $880,000 cost. Simultaneously short 1,000,000 USDT at $1.02 = $1,020,000 proceeds.
2. **Net capital outlay:** ~$880K long + collateral for short leg.
3. **Hold through weekend.** USDC oracles get pummeled; many DeFi protocols pause.
4. **Exit Mon Mar 13, 16:00:** USDC back to $0.999, USDT at $1.001. Close both legs.
5. **P&L:**
   - Long USDC: +$119K (0.88 → 0.999)
   - Short USDT: +$19K (1.02 → 1.001 — covered cheaper)
   - **Total: ~$138K on $880K capital ≈ 15.7% in 52 hours**
6. **Alternative:** Skipped the short and just held redemption-eligible USDC, redeemed via Circle Mon afternoon at $1.00. Same upside, no leg risk.

## Performance Characteristics

- **Win rate:** Very high (~90%+) for fiat-backed stables when redemption channels remain open
- **Sharpe (per opportunity):** 3.0+, but opportunity is intermittent (1–2 major events/year)
- **Drawdown risk:** Concentrated in catastrophic failures (UST May 2022 went from $1 → $0.10 → $0; was NOT an arb)
- **Tether premium history:** 2018-2020 Tether routinely traded at 10–15% premium on Bitfinex due to banking restrictions; arb harvested by USD on-ramp specialists
- **Best market conditions:** Banking crises, regulatory scares, single-issuer FUD with healthy redemption channel
- **Worst conditions:** Algorithmic-stable death spirals (UST), regulatory shutdown (BUSD Feb 2023)

> **No fabricated returns.** The percentages above (≈14–16% on the USDC/SVB weekend, ~9% Tether premium) are documented historical events with dated, cited sources, not projected returns. A *typical* depeg arb is far smaller — most deviations are sub-percent and revert within fee bands. Treat the headline events as the rare fat tail, not the base case.

## Execution Venues and Paths

The same conceptual trade can be expressed several ways, with very different cost and risk profiles. Choosing the path is half the strategy.

| Path | Mechanism | Cost drivers | Leg risk | When to use |
|---|---|---|---|---|
| **Issuer redemption** | Buy cheap stable, redeem 1:1 via issuer (Circle/Tether/Paxos) | KYC, banking T+N, gas | None (hard floor at redemption) | When you are a redemption-eligible counterparty and the channel is open |
| **Curve 3pool swap** | Swap cheap → rich stable on [[curve-finance]] | Pool fee, slippage, gas | Low (atomic on-chain) | Fast on-chain capture, depth permitting |
| **Long/short pair** | Buy cheap stable, short rich stable | Borrow cost, funding, two legs | Moderate ([[leg-risk]]) | When redemption is closed but reversion expected |
| **Leveraged borrow-and-redeem** | Borrow against cheap stable, redeem, repeat | Interest, liquidation risk | Higher | High-conviction, deep-channel events |
| **Options skew** | Express via puts/calls on the depeg | Premium, IV | Defined | When you want defined downside |

For the full tactical menu — seven distinct profit-capture methods including risk-free redemption arb, leveraged borrow-and-redeem, AMM band capture, and options skew — see [[stablecoin-depeg-profit-capture]]. On-chain legs that touch the public mempool should route through Flashbots to avoid sandwiching; see [[mev-execution-guide]].

## Cost-Aware Breakeven

The strategy's `breakeven_cost_bps` is ~20 bps round-trip (frontmatter). A trade is only worth doing when the expected reversion exceeds the stacked costs below.

| Cost | Typical magnitude | Notes |
|---|---|---|
| Curve 3pool swap fee | ~1–4 bps (varies by pool config) | Per leg |
| Slippage | Scales with size vs. pool depth | Cap size at <0.5% slippage |
| Gas (Ethereum mainnet) | Flat per tx; large at congestion | Cheaper on L2s |
| Borrow/funding (short or levered legs) | Spikes during stress | Can dominate in a crisis |
| Redemption friction | Time (T+N), KYC | "Cost" is duration risk, not bps |

Sub-percent deviations rarely clear these costs after slippage; the durable opportunities are the multi-percent, catalyst-driven events in the table below.

## Historical Depeg Events

| Event | Stable | Depeg low | Recovery time | Trade outcome |
|-------|--------|-----------|---------------|---------------|
| Black Thursday Mar 12, 2020 | DAI | $1.10 (ABOVE peg, vault crisis) | 1 week | Short DAI worked; long worked through PSM later |
| Tether banking 2017–2019 | USDT | $0.91 (Oct 2018) | Days–weeks | 9% spread captured by Bitfinex on-rampers |
| UST collapse May 2022 | UST | $0.00 | Never | NOT an arb — death spiral |
| USDN 2022–23 | USDN (Waves) | ~$0.78 (Apr 2022), slid below $0.20 by 2023 | Permanent | Death spiral |
| USDC SVB Mar 11, 2023 | USDC | **$0.8774** | 48 hours | Textbook arb (~14% in 2 days) |
| BUSD wind-down Feb 2023 | BUSD | $0.998 | Slow drain | Not really a depeg, slow redemption |
| FRAX SVB co-move Mar 11, 2023 | FRAX | $0.88 | 48 hours | Same as USDC (FRAX backed by USDC) |
| USDR Oct 11, 2023 | USDR (real estate-backed) | $0.50 | Permanent | Death spiral |
| sUSD Apr–May 2025 | sUSD (Synthetix) | $0.83 (Apr), deeper lows ~$0.68 (May) | Months | Slow recovery through SIP-420 backstop measures |

## Capacity Limits

- [[curve-finance]] 3pool depth: $200M–$1B; single trades >$10M start to move price meaningfully
- Issuer redemption speed: Circle (T+1), Tether (T+0 to T+3), MakerDAO PSM (instant up to limits)
- Single-event capacity: ~$50M before slippage and queueing dominate

## What Kills This Strategy

- **Permanent depeg:** Death spiral (UST, USDR) — the cheap stable goes to zero
- **Redemption channel closure:** Issuer suspends redemptions or banking partner fails permanently
- **Regulatory action:** SEC declaring a stable a security mid-trade (BUSD)
- **Smart contract failure** in DAI/FRAX collateral systems
- **Crowding:** Major arbitrageurs (Jane Street, Cumberland, market-making desks) close spreads in minutes for known issuers

## Kill Criteria

- Spread widens beyond entry by 2x AND issuer redemption channel is suspended
- Issuer audit reveals materially under-collateralized reserves
- Lead banking partner formally fails with no replacement on horizon
- On-chain governance multisig compromised
- Position size exceeds 5% of pool depth

## Advantages

- **Clear price target:** $1.00, by definition
- **High Sharpe** when opportunities arise
- **Issuer redemption** provides a non-market exit route
- **Short timeframe:** typical resolution in 24–96 hours
- **Composable:** can lever via [[aave]] / [[maker]] PSM
- **Asymmetric:** the long leg has a hard floor at the redemption price (if redemption works)

## Disadvantages

- **Catastrophic failure mode:** algorithmic-stable death spirals are uninsurable
- **Banking-system dependency:** the redemption arb only works if banks are open
- **Issuer counterparty risk** (Circle, Tether, Paxos)
- **Regulatory tail:** US/EU stablecoin laws can wind down an issuer overnight (BUSD, Feb 2023)
- **Crowding:** professional market makers compress spreads quickly on known issuers
- **DeFi venue risk:** Curve / Uniswap pool exploits could vaporize position
- **Oracle risk:** lending protocols may not recognize the new fair price during the depeg

## Sources

- Circle quarterly reserve attestations (Grant Thornton/Deloitte)
- Tether quarterly attestations (BDO Italia)
- MakerDAO governance and PSM analytics
- FDIC press releases (March 12, 2023 SVB resolution)
- Curve Finance subgraph + on-chain analytics
- Stablecoin price data: [[crypto-data-sources]] (exchange APIs, Curve TWAP, Coinglass)

## Related

- [[funding-rate-arbitrage]], [[lst-depeg-arbitrage]], [[synthetic-stablecoin-depeg-arbitrage]], [[stablecoin-depeg-profit-capture]]
- [[depeg-risk]] — the broader risk framework
- [[liquidation-cascade-arbitrage]] — depegs and cascades often co-occur in the same crisis
- [[mev-execution-guide]] — protect on-chain legs from sandwiching
- [[2022-05-terra-luna-depeg-arb]] — counterexample (UST failed, not an arb)
- [[curve-finance]], [[circle]], [[tether]], [[makerdao]], [[ethena]]
- [[cross-chain-arbitrage]] — bridges create their own stablecoin price gaps
- [[crypto-data-sources]] — where to source stable prices, attestations, and pool data
- [[edge-taxonomy]], [[failure-modes]], [[leg-risk]]
