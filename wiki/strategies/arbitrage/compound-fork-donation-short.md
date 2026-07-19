---
title: "Compound-Fork Donation-Attack Systematic Short"
type: strategy
created: 2026-04-28
updated: 2026-07-19
status: excellent
tags: [arbitrage, crypto, defi, risk-management, ai-trading]
aliases: ["Compound Fork Short", "Donation-Attack Fade", "Empty-Market Short Pattern"]
related: ["[[ai-amplified-exploit-arbitrage]]", "[[smart-contract-vulnerability-taxonomy]]", "[[oracle-manipulation]]", "[[flash-loan-attacks]]", "[[2026-exploit-target-watchlist]]", "[[ai-vulnerability-discovery]]", "[[audit-recency-tvl-growth-short]]", "[[post-hack-incident-response-arb]]", "[[exploit-arb-implementation-guide]]", "[[donation-attacks]]"]
strategy_type: quantitative
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: paper-traded
edge_source: [structural, analytical]
edge_mechanism: "Compound v2 has a well-documented donation/empty-market vulnerability that has been exploited repeatedly: Hundred Finance (Apr 2023), Onyx Protocol (Nov 2023, again Sep 2024), Sonne Finance (May 2024, $20M), and recurring Venus Protocol incidents (Feb 2025 zkSync, Mar 2026 BNB Chain). Each fork inherits the vulnerability template; AI scanners catch the pattern reliably; teams continue shipping anyway. Short fork tokens during their first 6-12 months post-launch as a structural bet on the recurrence."
data_required: [compound-fork-discovery, defillama-tvl-time-series, fork-deployment-dates, perp-market-listings, halborn-trail-of-bits-audit-archives]
min_capital_usd: 50000
capacity_usd: 10000000
crowding_risk: low
expected_sharpe: 1.3
expected_max_drawdown: 0.20
breakeven_cost_bps: 100
decay_evidence: "Compound v3 explicitly redesigned to prevent donation attacks (single-collateral markets, donation-resistant accounting). New forks of Compound v3 should reduce risk; forks of v2 still ship with the bug. Pattern persists as long as v2 forks continue launching, which they do (Sonne, Mendi, Moonwell, Strike, Iron Bank, Hundred, etc. all v2-derived)."
---

# Compound-Fork Donation-Attack Systematic Short

A narrow but reliably-recurring [[arbitrage]] (directional short) strategy: short [[compound|Compound]]-fork tokens during their first 6-12 months post-launch as a bet on the well-documented donation-attack pattern recurring. Sub-strategy under [[ai-amplified-exploit-arbitrage]] but with a much sharper edge thesis — the bug is *known*, AI scanners *find* it, audit firms *warn* about it, and protocols *still ship it*. For the underlying vuln-class explanation, see [[donation-attacks]] and [[smart-contract-vulnerability-taxonomy]]; for the broader incident history, [[defi-hacks-and-exploits]].

This is the sharpest-thesis member of the exploit-arb family because it does not require predicting *that* a protocol is vulnerable — the vulnerability template is copied verbatim from a forked codebase whose exploit history is public. The trade is to monetize the gap between known risk and unchanged market pricing, a textbook [[limits-to-arbitrage]] situation kept open by the difficulty and reputational friction of systematically shorting small-cap protocol tokens.

## Edge Source

**Structural** + **analytical**.

- **Structural:** Compound v2's donation/empty-market vulnerability has been exploited multiple times. Each new fork inherits the template if not patched. Forks ship faster than they audit; the bug persists.
- **Analytical:** The exploit pattern is well-documented (Halborn published a definitive Sonne post-mortem). Future fork incidents are predictable in mechanism even if not in timing.

## Why This Edge Exists

The Compound v2 donation/empty-market vulnerability operates as follows:

1. Protocol creates a new market with zero existing liquidity.
2. Attacker deposits a small amount to seed the market.
3. Attacker "donates" a large amount of tokens directly to the underlying token contract (bypassing deposit accounting).
4. The cToken-to-underlying ratio becomes manipulated; vault-share price inflates.
5. Attacker borrows against inflated collateral from other (funded) markets in the protocol.
6. Attacker walks away with borrowed funds; cToken accounting is broken.

**Mitigation requires** transaction-batching the market creation + first deposit + collateral-factor adjustment into a single atomic transaction, OR restricting EXECUTOR_ROLE to a trusted multisig. Many forks ship without this discipline.

**Recurring incidents:**
| Date | Protocol | Loss | Mechanism |
|------|----------|------|-----------|
| Apr 2023 | Hundred Finance | $7M | Empty market + donation |
| Nov 2023 | Onyx Protocol | $2.1M | Empty oPEPE market (known v2 precision/donation bug) |
| May 2024 | Sonne Finance | $20M | Permissionless EXECUTOR_ROLE; market creation + c-factor adjustment scheduled 2 days apart |
| Sep 2024 | Onyx Protocol (again) | ~$3.8M | Empty market (repeat incident) |
| Feb 2025 | Venus Protocol (zkSync deployment) | ~$0.7M net | Donation attack |
| Mar 2026 | Venus Protocol (BNB Chain, THE market) | ~$2.2M bad debt (~$3.7M gross) | Donation attack via supply-cap bypass (recurring; same protocol family) |

Counterparty: yield chasers allocating to high-APR Compound forks without modeling the inherited bug. Protocol teams that prioritize launch speed over audit discipline.

## Null Hypothesis

Under "no edge" conditions, Compound forks would either (a) not ship the bug (audit catches it), (b) be priced with an exploit-risk discount commensurate with historical frequency. Empirically, neither happens consistently — the forks ship vulnerable, and tokens trade at par with non-vulnerable peer protocols until an exploit lands.

A clean test: build a basket of v2-derived lending forks at TVL > $50M and compare their forward 12-month token returns against a matched set of v3-style / audited lending peers. Under the null the two baskets are statistically indistinguishable; the strategy is validated only if the fork basket shows the expected negative skew (rare large drops on exploit) net of carry.

## Why the Mispricing Persists

Three reasons the short edge is not competed away (the [[limits-to-arbitrage]] lens):

1. **Reputational and social friction.** Systematically shorting small DeFi protocols invites community backlash and is off-mandate for many funds, so the natural arbitrageur pool is thin.
2. **Carry uncertainty and timing.** The exploit can land any time in months 3-9 (or never within the window); the short must pay funding for an indeterminate hold, which deters momentum-style capital.
3. **Small-cap execution friction.** Fork tokens are $10-100M FDV with shallow perp books and occasional listing/delisting — large players cannot size in without moving the market or being trapped on exit.

## Rules

1. **Universe identification**: monitor new Compound v2 deployments via:
   - DeFiLlama "lending protocols" filter, sorted by launch date
   - Fork-of-Compound classification (manual; many use fork-recognition heuristics from explorer data)
   - Audit-firm public archives (Halborn, Trail of Bits, OpenZeppelin) — papers explicitly warning about the v2 fork class
2. **Filter to high-risk forks**: TVL > $50M; launched <12 months ago; no public audit explicitly addressing donation-attack mitigation; permissionless governance role for market creation/adjustment.
3. **Short the protocol token** if a perp market exists; size 0.1-0.3% of book per name to manage carry cost.
4. **Hold for 6-12 months or until exploit lands** — whichever comes first.
5. **Cover positions** when:
   - Protocol formally addresses the donation-attack pattern via audit + redeployment, OR
   - 12 months elapsed without incident (most fork incidents land in months 3-9), OR
   - Exploit lands and the loss is captured.
6. **Add new positions** as new forks launch.

## Implementation Pseudocode

```python
def monthly_compound_fork_review():
    new_forks = scan_compound_forks(launched_within_months=12)
    for fork in new_forks:
        if fork.tvl < 50_000_000:
            continue
        if fork.has_donation_attack_mitigation_audit():
            continue
        if not perp_market_exists(fork.token):
            continue
        if not currently_short(fork):
            target_size = 0.002 * limit  # 0.2% of book
            open_short(fork.token, target_size)
            log_position(fork, target_size, expected_carry=0.50, hold_months=12)

    for position in current_shorts:
        if position.protocol.formally_addressed_donation_attack():
            close_position(position, reason="mitigation deployed")
        elif position.months_held >= 12:
            close_position(position, reason="time stop")
        elif exploit_landed(position.protocol):
            close_at_post_exploit_low(position, capture_pnl)
```

## Indicators / Data Used

- **DeFiLlama lending category** with launch-date sort and fork-classification metadata
- **Halborn / OpenZeppelin / Trail of Bits public archives** — Compound-fork audit reports
- **Code4rena contest results** for new lending protocols
- **Etherscan / explorer APIs** — contract deployment history; specifically governance / EXECUTOR_ROLE configuration
- **Perp market listings**: Hyperliquid, Binance, Bybit, OKX
- **On-chain anomaly feeds** (Cyvers, Forta) for exit-trigger detection if exploit lands

## Example Trade

**Sonne Finance (May 2024, $20M, hypothetical short)**
- Late 2023: Sonne deployed on Optimism, Compound v2 fork.
- Early 2024: TVL ramped past $50M.
- May 2024: ~25 minutes after the donation attack launched, ~$20M was drained. SEAL contributor saved an additional $6.5M.
- *Trade*: short SONNE at $0.50 entry once TVL passed $50M and audit history was public; held through the exploit (prices approximate — SONNE traded roughly $0.50-0.75 in early 2024).
- *Outcome*: SONNE fell 70-80% on disclosure; covered at $0.15. ~70% return on the short leg over ~5 months.
- *Carry cost*: ~3% over the holding period (positive funding on the perp; cost bearable).

**Venus Protocol (recurring, 2025-2026)**
- Venus has had repeat donation-attack incidents across deployments: zkSync deployment, Feb 2025 (~$0.7M net loss); BNB Chain THE market, 15 March 2026 (~$2.2M bad debt, ~$3.7M gross).
- *Trade*: a persistent short XVS perp is the lower-conviction version of the playbook — both losses were small relative to Venus's TVL, so XVS drawdowns on disclosure were modest. The repeat incidents are better used as a screening signal (protocol family that keeps shipping the bug) than as a standalone short catalyst.

**Counter-example: Compound v3 (long-decile)**
- Compound v3 explicitly redesigned to prevent donation attacks (single-collateral markets).
- *Trade*: long COMP perp as fund hedge for the short basket of v2-fork shorts.

## Performance Characteristics

Estimated 12-month results for systematic basket (paper-traded, not yet live):
- Hit rate: ~30-50% of cohort experiences a donation-attack incident within 12 months
- Median return per hit position: ~50-80% (token typically down 50%+ on disclosure)
- Median return per non-hit position: -3% to -8% (carry cost over holding period)
- Combined expected return: ~10-20% annualized on capital deployed
- Sharpe estimate: 1.0-1.5 — narrow but reliable

## Capacity Limits

Capacity bounded by perp market depth on Compound-fork tokens. Most fork tokens are small-cap ($10-100M FDV); $5-20M short capacity per name. Strategy-level capacity: ~$10M deployed across baskets. Higher capacity requires accepting higher slippage on entry / exit.

## Key Risks

This is a *short* of a small-cap, smart-contract-bearing asset — the risk profile is distinct from the long exploit-arb edges:

- **Short-squeeze / execution risk:** small-cap fork perps can squeeze violently on a partnership announcement, listing, or short-covering cascade. Funding can flip sharply negative (you pay to hold the short). Use small per-name sizing (0.1-0.3% of book) and budget carry.
- **Smart-contract risk on the venue, not just the target:** the perp DEX (Hyperliquid, GMX) and any on-chain margin used carry their own [[smart-contract-vulnerability-taxonomy|smart-contract risk]]. A venue exploit can liquidate or freeze the hedge at the worst moment.
- **Cross-chain risk:** many forks deploy on L2s/alt-L1s (Optimism, zkSync, BNB Chain). If the short or collateral is bridged, a [[bridge]] / [[cross-chain]] exploit is an independent loss path uncorrelated with the thesis.
- **Silent-patch risk:** the protocol may quietly fix the donation vector without announcement — the short then bleeds carry with no payoff.
- **The bug never fires in-window:** historical hits cluster in months 3-9 but the distribution has a fat right tail; a 12-month time-stop can close before the exploit lands.

## What Kills This Strategy

- **Compound v3 / Aave V4 architecture displaces v2 forks**. New deployments are increasingly v3-style, reducing the vulnerable surface area over 2-3 year horizon.
- **Audit firms refuse v2-derived deployments**. Halborn / Trail of Bits decline to audit forks without donation-attack mitigation. Pattern: protocols self-mitigate or don't launch.
- **AI scanners integrated at deployment** catch the bug before launch (see [[ai-vulnerability-discovery]]).
- **Crowding** — currently low; could rise if other desks publish the strategy.

## Kill Criteria

- Drawdown > 20% over rolling 12 months.
- Hit rate drops below 20% over 4 consecutive quarters.
- Major regulatory action specifically targeting fork shorts.
- v3-style architecture reaches >80% of new lending protocol launches.

## Advantages

- **Narrow but reliable** — fewer trades, but each is high-confidence.
- **Pattern recurrence is well-documented** — Halborn / Trail of Bits / Code4rena have explicit warnings; bug is in literature.
- **Cheap-to-carry** — small per-position sizes; bounded carry cost.
- **Asymmetric** — bounded carry vs 50-80% upside on exploit.

## Disadvantages

- **Capacity-limited** — small-cap perp markets cap position size.
- **Reputational** — systematic shorting of small-cap protocols is high-friction.
- **False-positive risk** — protocol may patch the bug without public announcement; short pays carry without payoff.
- **Smaller-cap perp execution risk** — wide spreads, occasional venue listing/delisting.

## Sources

- Halborn post-mortem on Sonne Finance (May 2024): `halborn.com/blog/post/explained-the-sonne-finance-hack-may-2024`
- Halborn post-mortem on Venus Protocol (March 2026): `halborn.com/blog/post/explained-the-venus-protocol-hack-march-2026`
- BlockSec analysis of the Venus THE-market donation attack (March 2026): `blocksec.com/blog/venus-thena-donation-attack`
- rekt.news, "Venus Protocol — Rekt 4" (March 2026): `rekt.news/venus-protocol-rekt4`
- Venus Governance, "Multi-chain patch fix for THE market donation attack" (community.venus.io)
- Hundred Finance exploit analysis (April 2023)
- Verified via Perplexity (sonar), 2026-06-10 — Venus Feb 2025 (zkSync, ~$716K net) and Mar 2026 (BNB Chain THE market, ~$2.15M bad debt) incidents confirmed against the above citations.
- [[smart-contract-vulnerability-taxonomy]] — donation-attack class
- [[oracle-manipulation]] — adjacent vector that often overlaps in fork attacks
- [[ai-amplified-exploit-arbitrage]] — hub strategy

## Getting the Data (CryptoDataAPI)

The fork universe and donation-attack-mitigation check come from DeFiLlama fork classification + audit archives + explorer `EXECUTOR_ROLE` config — off-API. CryptoDataAPI serves the small-cap perp short and the exploit exit-trigger.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding to budget the fork-token short carry
- `GET /api/v1/derivatives/open-interest` — thin fork-token perp depth / crowding (drives 0.1-0.3% per-name sizing)
- `GET /api/v1/security/regime` + `GET /api/v1/security/events` — detect when a donation attack lands on a shorted fork
- `GET /api/v1/dex/security/{chain}/{address}` — contract screening for the fork's config

**Historical data:**
- `GET /api/v1/backtesting/funding` — carry-drag archive
- `GET /api/v1/security/regime/{symbol}` — per-symbol 60d security overlay (Pro+)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/security/events"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] handles execution and the exit trigger; the fork universe is built off-API:

- **Signal (off-API core)** — the fork classification and donation-attack-mitigation check come from DeFiLlama + audit archives + explorer `EXECUTOR_ROLE`/multisig config; not served here.
- **Execution + carry** — `GET /api/v1/derivatives/funding-rates` / `/derivatives/open-interest` size the small-cap perp short (0.1-0.3% per name) and budget carry.
- **Exit trigger** — `GET /api/v1/security/regime` / `/security/events` fire when a donation attack lands so you cover at the post-exploit low.
- **Backtest** — `GET /api/v1/backtesting/funding` for carry; incident dates come from the off-API post-mortem record.
- **Tip** — fork perps are thin and squeeze violently; watch OI/funding and never market-order the entry.

## Related

[[arbitrage]] · [[limits-to-arbitrage]] · [[ai-amplified-exploit-arbitrage]] · [[smart-contract-vulnerability-taxonomy]] · [[donation-attacks]] · [[defi-hacks-and-exploits]] · [[oracle-manipulation]] · [[flash-loan-attacks]] · [[2026-exploit-target-watchlist]] · [[ai-vulnerability-discovery]] · [[audit-recency-tvl-growth-short]] · [[post-hack-incident-response-arb]] · [[bridge]] · [[cross-chain]] · [[multi-dvn-bridge-config-arbitrage]] · [[cross-chain-contagion-hedge]] · [[compound]]
