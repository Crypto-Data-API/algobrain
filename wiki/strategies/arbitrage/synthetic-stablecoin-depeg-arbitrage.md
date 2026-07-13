---
title: "Synthetic Stablecoin Depeg Arbitrage"
type: strategy
created: 2026-04-28
updated: 2026-06-20
status: excellent
tags: [arbitrage, crypto, defi, mean-reversion, risk-management, event-driven]
aliases: ["sUSDe Depeg Arb", "GHO Depeg Arb", "crvUSD Depeg Arb", "Synthetic Stable Arb", "Mechanism-Specific Stable Arb"]
related: ["[[stablecoin-pair-arbitrage]]", "[[lst-depeg-arbitrage]]", "[[depeg-risk]]", "[[ai-amplified-exploit-arbitrage]]", "[[cross-chain-contagion-hedge]]", "[[post-hack-incident-response-arb]]", "[[2026-exploit-target-watchlist]]", "[[ethena-usde]]", "[[curve-finance]]", "[[makerdao]]", "[[ethena]]", "[[funding-rate-arbitrage]]", "[[2022-05-terra-luna-depeg-arb]]", "[[2023-03-usdc-svb-depeg]]", "[[stablecoin-depeg-profit-capture]]", "[[2017-2020-tether-banking-premium]]", "[[2020-03-dai-black-thursday]]", "[[2023-02-busd-wind-down]]", "[[2026-04-kelp-stable-sympathy-depeg]]", "[[stablecoin-depeg-history]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto, defi]
complexity: advanced
backtest_status: paper-traded
edge_source: [structural, behavioral, analytical]
edge_mechanism: "Synthetic and algorithmic stablecoins (sUSDe, GHO, crvUSD, FRAX, USDe, sDAI) maintain peg via mechanism-specific paths — delta-neutral perp baskets, over-collateralization with soft-liquidation, hybrid backing — that have distinct break modes from fiat-backed stables. Contagion events trigger cross-mechanism repricing. Each break-mode is mechanically predictable; the trade is to long the cheap stable when the break-mode is solvable and short when it's structural."
data_required: [stable-prices-by-venue, sUSDe-funding-rate-history, gho-aave-collateral-utilization, crvusd-llamma-band-depth, frax-collateral-ratio, curve-3pool-and-extended-pool-imbalances, perp-funding-rates-eth-btc, lending-protocol-bad-debt]
min_capital_usd: 50000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 1.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 30
decay_evidence: "Synthetic stablecoin TVL grew from <$1B in 2023 to $10B+ by Q1 2026; depeg events are mechanism-specific and recurring. Strategy may compress as protocols mature redemption mechanisms — but new synthetic mechanisms (Ethena white-labels jupUSD/USDm/suiUSDe; future protocols) keep the universe expanding faster than each individual mechanism gets robust."
---

# Synthetic Stablecoin Depeg Arbitrage

A mechanism-aware extension of [[stablecoin-pair-arbitrage]] focused on **synthetic, algorithmic, and over-collateralized stablecoins** (sUSDe, GHO, crvUSD, FRAX hybrid, sDAI, sFRAX, white-label deployments). Where the canonical fiat-backed-stable arb (USDC/SVB-style) bets on banking-system reopening, this strategy bets on **mechanism-specific peg-restoration paths** under a wider variety of stress events: perp funding inversions, oracle decoupling, governance-vote uncertainty, contagion cascades from major exploits. Sub-strategy under [[cross-chain-contagion-hedge]] for the contagion vector; standalone for the mechanism-specific vectors.

> **Important distinction from [[stablecoin-pair-arbitrage]]**: that page covers fiat-backed stables (USDC, USDT, BUSD) where the peg-restoration path is *banking-system schedule* (T+1, business days). This page covers synthetic stables where the peg-restoration path is *mechanism-internal* — perp funding rates, collateral ratios, AMM-style liquidations, governance interventions. Different mechanism = different break modes = different trades. Run both strategies; they're complements, not duplicates.

**Where this sits in the basket.** This strategy is one node in the [[trading-strategy-baskets|crypto strategy basket]]: it shares the exploit-aggregator and oracle-monitoring infrastructure with [[ai-amplified-exploit-arbitrage]], [[cross-chain-contagion-hedge]], and [[post-hack-incident-response-arb]]; it shares the [[funding-rate]]/[[hyperliquid]] hedge rails with [[funding-rate-arbitrage]] and the [[hyperliquid-perp-trading-map]] strategies; and the *capture* toolkit (how to maximize P&L once a depeg is verified tradeable) lives in [[stablecoin-depeg-profit-capture]]. Classification (this page) → capture (that page) → portfolio overlay ([[cross-chain-contagion-hedge]]).

## Edge Source

**Structural** + **behavioral** + **analytical**.

- **Structural:** each synthetic stablecoin has a published peg-restoration mechanism. When the mechanism stresses (negative perp funding for sUSDe; collateral health for GHO; AMM band exit for crvUSD), peg deviation is mechanically predictable.
- **Behavioral:** retail panic sells synthetic stables at deep discounts during contagion events even when the underlying mechanism is solvent. Forced sellers (LP redemptions, leveraged liquidations) compound the deviation.
- **Analytical:** mechanism-by-mechanism modeling distinguishes "solvable" depegs (mean-reversion trade) from "structural" depegs (don't catch falling knife). Edge is in the model, not in the speed.

## Why This Edge Exists

Three reinforcing structural facts:

1. **Synthetic-stable TVL has scaled fast** without a corresponding rise in arbitrageur sophistication. sUSDe alone passed $5B by Q1 2026 (Ethena governance Jan-Feb 2026 update); white-label deployments (jupUSD on Solana, USDm on MegaETH, suiUSDe on Sui) crossed $100M combined in Q1 2026. The stress-trade window is wider than for fiat-backed stables because more of the holder base is unsophisticated.

2. **Mechanism break-modes are documented but not systematically priced**. The perp-funding dependency of sUSDe is publicly disclosed (Ethena's whitepaper). The LLAMMA soft-liquidation in crvUSD is published. But the market doesn't reliably distinguish "sUSDe depeg from negative funding (will recover when funding normalizes)" from "sUSDe depeg from collateral compromise (won't recover)." Both look the same on the price chart in the first hours.

3. **Contagion cascades create cross-mechanism deviations**. KelpDAO (Apr 2026, ~$290M direct loss) triggered a ~$13B TVL drain across DeFi over the following days. During the freeze window, multiple synthetic stables traded weak in sympathy without direct exposure (GHO, crvUSD, sUSDe all saw 30-100bp deviations not justified by their own mechanism state). This is the exploit-cluster overlap: the trade is identical structurally to the LRT sympathy-depeg in [[cross-chain-contagion-hedge]], applied to stable-asset cluster.

Counterparty: panic sellers; LP redemption forced selling; leveraged sUSDe positions getting liquidated; uninformed retail.

## Variant Map by Mechanism

| Stablecoin | Mechanism | Primary break mode | Tradable depeg signal |
|-----------|-----------|--------------------|----------------------|
| **USDe / sUSDe** (Ethena) | Delta-neutral basket: long ETH/BTC spot + short equivalent perp; collects funding | Negative perp funding for extended periods (mechanism pays out, drains backing); secondary: counterparty risk on perp venues | sUSDe < $1.00 *and* [[funding-rate]] negative *and* reserve fund solvent |
| **GHO** (Aave) | Over-collateralized minting against Aave deposits (USDC, ETH, etc.); GHO Stability Module (GSM, a PSM-style USDC swap facility) as backstop | Aave collateral health stress + GSM utilization spike during lending-protocol contagion | GHO 30-80 bp below peg *and* GSM non-empty *and* Aave governance functioning |
| **crvUSD** (Curve) | Over-collateralized via LLAMMA AMM-based soft-liquidation; collateral price enters "liquidation band," gradually swaps into crvUSD | Sharp collateral price drops causing band exhaustion; or LLAMMA AMM oracle stress | crvUSD > 50 bp below peg *and* LLAMMA band has remaining depth |
| **FRAX** (hybrid) | Mix of collateral-backed + algorithmic; CR (collateral ratio) adjusted by governance | Collateral ratio governance lag + algorithmic-portion stress | FRAX off par *and* CR > target *and* governance responsive |
| **sFRAX** (yield-bearing FRAX) | FRAX deposited in revenue-sharing vault | Same as FRAX + smart-contract risk on the staking layer | sFRAX/FRAX ratio dislocated *and* FRAX peg intact |
| **sDAI** (yield-bearing DAI) | DAI deposited in MakerDAO DSR | DAI peg + DSR vault risk | sDAI/DAI off NAV *and* [[makerdao]] DSR funded |
| **jupUSD / USDm / suiUSDe** (Ethena white-labels) | Ethena's delta-neutral mechanism deployed on different chains | Same as sUSDe + per-chain integration risk + thinner per-deployment audit coverage | White-label < $1.00 *and* parent sUSDe healthy *and* chain integration sound |
| **USDC.e (bridged USDC)** | Bridge-wrapped USDC; not native | Bridge compromise — wrapped trades discount until canonical bridge recapitalizes | USDC.e > 5% discount to canonical *and* recap credible |

**Don't trade**: pure-algorithmic stables with no collateral backing (UST 2022 model). Death spiral is not arbitrable. See [[2022-05-terra-luna-depeg-arb]] for the counter-example and [[stablecoin-depeg-profit-capture]] for the seven-method capture toolkit that layers on top of any tradeable classification here.

## Mechanism Health Gate (decision table)

Each variant has a single hard "structural vs solvable" gate. This is the most important table on the page — it converts the variant map into a go/no-go decision. If the gate condition is breached, the depeg is structural: do not long, close any existing position.

| Variant | Solvable (trade) when | Structural (skip / close) when | Key feed |
|---------|----------------------|--------------------------------|----------|
| sUSDe negative funding | Reserve fund solvent; negative-funding streak < ~14 days | Reserve fund draining fast; streak > 14 days | Ethena reserve disclosure + [[funding-rate]] streak |
| GHO lending contagion | GSM/PSM non-empty (< 85% utilization); Aave bad-debt ratio < 5% | GSM exhausted; bad-debt ratio > 5%; governance frozen | Aave PSM utilization + bad-debt tracker |
| crvUSD AMM band | LLAMMA band depth > ~10%; [[curve-finance]] functioning | Band exhausted; LLAMMA insolvent | LLAMMA band depth (Curve subgraph) |
| FRAX hybrid | CR adjustment lag only; governance responsive | Algorithmic portion unbacked; CR collapsing | FRAX CR + governance forum |
| Sympathy (cluster) | No direct exposure to exploited asset; oracle median unchanged | Direct collateral exposure to the exploit | Exploit aggregator + exposure map |
| Bridge-wrapped | Recap credible (major app, diversified backing) | No recap path (niche app; Multichain precedent) | Bridge config + recap announcement |

## Variant: Negative Perp Funding (sUSDe-class)

The Ethena delta-neutral mechanism collects positive perp funding when long-spot / short-perp positions earn yield. **When funding turns negative for sustained periods** (multi-day to multi-week), the mechanism *pays out* funding rather than collecting; backing erodes; sUSDe peg comes under pressure.

**Trigger conditions for negative funding episodes:**
- Bear-market regimes where perp longs unwind (longs pay shorts → funding inverts)
- Specific market stress events (post-FTX 2022; certain cycles in 2023-24)
- Protocol-specific events disrupting the perp basket (exchange downtime, listing issues)

**Trade structure:**
1. Monitor sUSDe peg vs USDC on Curve (sUSDe should trade ~$1.00-1.05 under positive funding due to embedded yield).
2. When sUSDe deviates 50-150bp from peg AND funding is negative AND Ethena's reserve fund is reported solvent → buy the depeg.
3. Hedge backing-asset exposure: short ETH perp on Hyperliquid in proportion to sUSDe's ETH-perp basket, since you're effectively long ETH-perp-funding via your sUSDe long.
4. Exit when peg restored OR funding normalizes positive OR Ethena reserve depletion concerns escalate.
5. **Don't trade if Ethena reserve fund is depleting fast** — that's a structural break, not a mean-reversion.

## Variant: Lending-Protocol Contagion (GHO-class)

GHO is minted by depositing collateral (USDC, ETH, etc.) into Aave and minting GHO against the deposit. The peg is maintained by the GHO Stability Module (GSM — a PSM-style USDC swap facility, referred to as "PSM" below) and Aave governance interest-rate adjustments.

**Trigger conditions for GHO depeg:**
- Aave-broad contagion (KelpDAO Apr 2026 caused Aave bad debt $123-230M)
- PSM utilization spike (PSM is exhausted; new GHO minting rate adjusts but lag exists)
- Aave governance vote uncertainty (rare interest-rate adjustments create stress)
- Smart contract risk on Aave Safety Module

**Trade structure:**
1. Monitor GHO peg + Aave PSM utilization + Aave bad-debt levels.
2. When GHO trades 30-80bp below peg AND PSM is non-empty AND Aave governance is functioning → buy.
3. Hedge: short AAVE token if contagion spillover is the trigger; long-GHO / short-AAVE captures the basis.
4. Exit when peg restored OR PSM is exhausted (structural break) OR Aave governance fails (catastrophic).

## Variant: AMM Band Stress (crvUSD-class)

crvUSD's LLAMMA mechanism gradually swaps collateral into crvUSD as collateral price drops. Under sharp price moves, the band can exhaust faster than rebalance, creating temporary peg deviations.

**Trigger conditions for crvUSD depeg:**
- Sharp ETH price drops (rapid LLAMMA-band exhaustion)
- Curve pool composition stress (3pool imbalance)
- Smart contract risk on Curve

**Trade structure:**
1. Monitor crvUSD peg + LLAMMA band depth + Curve 3pool composition.
2. When crvUSD trades >50bp below peg AND LLAMMA band has remaining depth AND Curve protocol is functioning → buy.
3. Exit when band rebalances OR position size exceeds Curve liquidity OR catastrophic Curve event.

## Variant: Contagion-Driven Sympathy Depeg

When a major DeFi exploit lands, multiple synthetic stables trade weak in sympathy without direct exposure. KelpDAO (Apr 2026) is the canonical case.

**Trigger conditions:**
- Major exploit ($100M+) on a composable DeFi protocol (LRT, lending, bridge)
- Any protocol with cross-collateral exposure to the affected asset

**Trade structure:**
1. On exploit alert, monitor synthetic stables (GHO, crvUSD, sUSDe, jupUSD) for sympathy depegs.
2. Distinguish: is the depeg justified by direct exposure (avoid) or sympathy (trade)?
3. Buy sympathy depegs at >30bp deviation; size cheap-to-carry; expect 24-72h mean reversion as scope clarifies.
4. Combine with [[cross-chain-contagion-hedge]] basket — the stable-leg of that strategy.

## Variant: Bridge-Wrapped Stable Discount

When a bridge is exploited, wrapped versions of stablecoins on that bridge trade at discount until the bridge is recapitalized.

**Trigger conditions:**
- Major bridge exploit (Wormhole 2022, Ronin 2022, Multichain 2023, KelpDAO 2026)
- Any wrapped stable on the affected bridge

**Trade structure:**
1. Identify wrapped stable (e.g., USDC.e on a compromised bridge) trading at >5% discount to canonical USDC.
2. Estimate bridge recapitalization probability and timeline.
3. Long the wrapped stable; hedge canonical USDC short or hold cash.
4. Exit on recapitalization announcement or formal failure.
5. **Floor case**: if bridge fails to recapitalize, position pays nothing (Multichain 2023 precedent).

## Null Hypothesis

If synthetic stablecoins were efficiently priced relative to mechanism state, depeg events would price in immediately and converge to a fair-value point reflecting the probability of mechanism failure. Empirically, deviations persist for hours to days post-trigger; fair-value re-pricing happens slowly. The lag is the alpha.

A clean test: track the time between depeg trigger event (e.g., funding inversion for sUSDe; KelpDAO disclosure for sympathy depegs) and peg restoration (or formal mechanism failure). If the lag is consistently <30 minutes, edge is gone. As of April 2026, observed lags average 4-72 hours. Edge persists.

## Rules

1. **Identify the depeg's mechanism trigger.** Use the variant map above to classify: funding-driven? collateral-driven? AMM-band? sympathy? bridge?
2. **Verify the mechanism is solvable.** Check reserve fund (Ethena), PSM utilization (GHO), LLAMMA band (crvUSD), Aave governance (AAVE), bridge recap probability (wrapped stables). If solvable → trade. If structural → skip.
3. **Buy the depeg at scaled-in entries.** 25% at first 30bp threshold; 50% at 60bp; final 25% reserved for capitulation.
4. **Hedge backing-asset exposure** if applicable (short ETH perp for sUSDe; short AAVE for GHO contagion; short Curve-3pool LP exposure for crvUSD).
5. **Exit triggers**:
   - Peg restored within 30bp of $1.00
   - Mechanism stabilized (positive funding restored; PSM refilled; LLAMMA rebalanced; bridge recapitalized)
   - **Stop-out**: depeg deepens past entry by 2x AND mechanism is materially impaired
6. **Never long a structural break.** Mechanism failure (Ethena reserve depleted; Aave PSM exhausted; LLAMMA insolvent; bridge failed to recap) → close at any cost, do not add.

## Implementation Pseudocode

```python
def synthetic_stable_depeg_arb():
    # Real-time peg monitoring
    pegs = {
        "sUSDe": peg_via_curve("sUSDe/USDC"),
        "USDe": peg_via_curve("USDe/USDC"),
        "GHO": peg_via_balancer("GHO/USDC"),
        "crvUSD": peg_via_curve("crvUSD/USDC"),
        "FRAX": peg_via_curve("FRAX/USDC"),
        "sDAI": peg_via_lookup("sDAI/DAI"),
        "jupUSD": peg_via_jupiter("jupUSD/USDC"),
        "suiUSDe": peg_via_cetus("suiUSDe/USDC"),
    }
    
    for stable, peg in pegs.items():
        deviation = abs(peg - 1.0)
        if deviation < 0.003:
            continue  # too tight
        
        mechanism = classify_mechanism(stable)
        trigger = identify_trigger(stable, mechanism)
        
        if trigger.is_structural:
            log_skip(stable, "structural break")
            continue
        
        # Mechanism-specific health check
        if mechanism == "ethena_delta_neutral":
            if not ethena_reserve_solvent():
                continue
            if perp_funding_negative_for_days() > 14:
                continue  # mechanism stress too long
        
        if mechanism == "aave_overcollateralized":
            if aave_psm_utilization() > 0.85:
                continue  # PSM exhaustion risk
            if aave_bad_debt_ratio() > 0.05:
                continue  # contagion structural
        
        if mechanism == "curve_llamma":
            if llamma_band_depth() < 0.10:
                continue  # band exhaustion risk
        
        if mechanism == "bridge_wrapped":
            if not bridge_recap_credible():
                continue  # bridge failed to recap
        
        # Execute the trade
        size = scaled_in_size(deviation, capital, mechanism)
        long_stable(stable, size, peg)
        hedge_backing_asset(stable, mechanism, size)
        
        monitor_for_peg_restoration_or_mechanism_failure(stable)
```

## Indicators / Data Used

The four signal families are **peg** (deviation trigger), **[[funding-rate]]** (sUSDe mechanism health + hedge carry), **[[open-interest]]** (flow confirmation), and **oracle/mechanism state** (the structural-vs-solvable gate). Peg, funding, and OI are available cross-venue through aggregators such as cryptodataapi.com (REST/WS); mechanism-state feeds (reserve disclosures, PSM utilization, LLAMMA band depth) are protocol-specific and require subgraph/RPC reads.

| Data | Source |
|------|--------|
| **Stable peg prices** | Curve pool reads (3pool + extended pools); Balancer pool reads (GHO); Cetus / Jupiter pools (white-labels); CEX spot prices; cryptodataapi.com multi-venue spot |
| **sUSDe / Ethena mechanism health** | Ethena governance forum (gov.ethenafoundation.com); reserve fund disclosures; perp funding history (HL hourly, Binance 8h, Deribit; or cryptodataapi.com funding feed) |
| **[[open-interest]] (flow confirmation)** | Exchange APIs; [[coinglass]]; cryptodataapi.com — confirms a sympathy depeg is real selling, not a thin-pool print |
| **GHO / Aave health** | Aave dashboard; PSM utilization; bad-debt tracker (forked Dune dashboard) |
| **crvUSD / LLAMMA state** | Curve frontend (crvusd.curve.fi); LLAMMA band depth; Curve subgraph |
| **FRAX collateral ratio** | Frax frontend; governance forum; CR adjustments |
| **Aave / Compound bad debt** | Aave / Compound dashboards; Tenderly free tier; Dune free tier |
| **Bridge recap status** | Protocol Twitter / Discord; recap announcements; bridge reserves |
| **Exploit alerts (sympathy trigger)** | Multi-source aggregator: PeckShield / BlockSec / Cyvers / ChainAegis / Forta (per [[exploit-arb-implementation-guide]]) |
| **Curve 3pool / extended pool composition** | Curve subgraph (free); Dune dashboards |
| **Funding rates** | Exchange websockets (HL, Binance, Bybit, Deribit) |
| **CEX deposit/withdrawal status** | Exchange announcements; status pages |

## Example Trade — sUSDe Negative Funding Episode (hypothetical)

**Setup**: Q3 2025 bear-market cycle; ETH down 25% in 4 weeks; perp longs unwinding; ETH funding inverts to -50bp annualized for 3 consecutive days.

**Observation**: sUSDe drops from $1.04 (peg-with-yield-premium) to $0.985 over 48h. Curve sUSDe/USDC pool composition skews 70% sUSDe (signal of selling pressure).

**Mechanism check**:
- Ethena reserve fund: $25M, solvent ✓
- Funding-payout streak: 3 days, manageable ✓
- Backing assets (ETH/BTC spot): no compromise ✓
- Whale liquidation events: limited ✓
- → Trade is mechanism-temporary, not structural.

**Trade**:
1. Buy 1,000,000 sUSDe at $0.99 ($990K cost).
2. Hedge backing-asset exposure: short ETH perp on Hyperliquid sized to sUSDe's ~50% ETH-perp basket weight ($500K notional ETH short).
3. Hold 7 days through funding normalization.

**Outcome**: Funding turns positive Day 5; sUSDe recovers to $1.02 by Day 7. Curve pool rebalances to 50/50.

**P&L**:
- Long sUSDe: +$30K (0.99 → 1.02)
- Short ETH perp: -$5K (small adverse move; partial hedge cost)
- Net: +$25K on $990K capital ≈ 2.5% in 7 days

## Example Trade — KelpDAO Sympathy Depeg (April 2026, hypothetical)

**Setup**: Apr 18 2026, 17:35 UTC. KelpDAO exploit confirmed via PeckShield + BlockSec + Cyvers (multi-source). $290M loss; Aave Guardian freezes rsETH within 90 min.

**Observation**: GHO trades from $1.001 to $0.992 over the next 6 hours (sympathy-depeg from Aave bad-debt overhang). crvUSD trades from $1.000 to $0.996. sUSDe holds peg (no direct Ethena exposure).

**Mechanism check** (GHO):
- Aave PSM utilization: 60% (well within capacity) ✓
- Aave bad-debt: $123M projected (within tolerance pre-resolution) ✓
- Aave governance functioning ✓
- → GHO depeg is sympathy, not structural.

**Trade** (GHO leg):
1. Buy 2,000,000 GHO at $0.992 ($1.984M cost).
2. No directional hedge (long-only mean-reversion play).
3. Hold 24-72 hours through Aave bad-debt resolution.

**Outcome**: Aave Guardian + Circle freezes contain damage; Aave governance proposes bad-debt socialization; GHO recovers to $0.999 within 48 hours.

**P&L**:
- Long GHO: +$14K (0.992 → 0.999)
- Net: ~+0.7% in 48 hours on $1.98M capital

(Modest per-event return; capacity-friendly basket trade across multiple synthetic stables.)

## Example Trade — Bridge-Wrapped USDC Discount (KelpDAO contagion, April 2026, hypothetical)

**Setup**: KelpDAO exploit triggers LayerZero-app-wide freezes. Some LayerZero-bridged USDC.e on certain L2s trades at $0.985 (1.5% discount) during freeze window.

**Mechanism check**:
- Affected bridge: LayerZero-style 1-of-1 DVN (compromised by KelpDAO mechanism) — bridge config questioned
- Recap probability: HIGH for major LayerZero apps with diversified backing; LOW for niche apps
- Timeline: typically 24-72h for major-app recap

**Trade** (only on major-app wrapped USDC):
1. Buy 1,000,000 USDC.e at $0.985 ($985K cost).
2. Hedge: short equivalent canonical USDC at $1.00 ($1M short notional).
3. Hold until recap announcement.

**Outcome**: Major LayerZero apps with multi-DVN configs are unaffected (re-rated); 1-of-1 DVN wrapped stables remain discount until protocol announcement. If app announces recap, USDC.e converges to canonical within 6-24 hours.

**P&L** (if recap successful): +$15K on $985K = ~1.5% return in 24-72h.
**P&L** (if no recap, e.g., Multichain-style): -100% on the long leg; short hedge offsets to ~zero net.

## Performance Characteristics

Estimated 12-month results across the variant set (paper-traded, projection):

| Variant | Hit-rate | Per-event return | Sharpe est | Capacity |
|---------|----------|------------------|------------|----------|
| Negative funding (sUSDe) | ~3-5x/year | ~2-5% per event | 1.4-1.8 | $20-30M |
| Lending contagion (GHO) | ~2-3x/year | ~1-3% per event | 1.0-1.4 | $30-50M |
| AMM band stress (crvUSD) | ~1-2x/year | ~1-2% per event | 1.0-1.3 | $20-30M |
| Sympathy depeg (cluster) | ~3-5x/year (with major exploits) | ~0.5-2% per event | 1.2-1.6 | $30-50M (basket) |
| Bridge-wrapped discount | ~1-2x/year | ~5-25% per event (or -50%) | 1.5-2.0 | $10-30M |

Combined Sharpe estimate: 1.3-1.7 (frontmatter carries the 1.5 midpoint). Slightly below fiat-backed-stable arb's per-event Sharpe (~1.8+) and well below [[stablecoin-pair-arbitrage]]'s textbook USDC/SVB per-event return (15.7% in 52h), but with materially more frequent opportunities, at the cost of higher per-event volatility and longer holding periods.

## Capacity Limits

Per-variant capacity bounded by:
- **Curve / Balancer pool depth** for the specific synthetic stable (typically $10-50M before slippage)
- **Wrapped stable on-chain liquidity** for bridge variants (typically $5-30M)
- **Funding-rate execution depth** for sUSDe-style hedges (Hyperliquid + Binance combined: $50M+)

Strategy-level capacity: ~$100M deployed across the variant set at current liquidity. Higher capacity feasible via direct OTC purchases from Ethena / Aave / Curve / Frax desks.

## What Kills This Strategy

- **Mechanism robustness improves** — Ethena raises reserve fund (current $25M+); Aave restructures PSM; Curve LLAMMA tuned. Each robustness step compresses depeg windows.
- **Synthetic-stable consolidation** — if 2-3 protocols dominate (Ethena + Aave + Maker), variant set shrinks; alpha-per-variant compresses with crowding.
- **Mean-reversion arbitrageurs scale** — current spreads (4-72h reversion) compress as more capital enters.
- **Major mechanism failure** (one of the variants experiences a death spiral comparable to UST 2022) — triggers regulatory scrutiny; restricts new launches; shrinks the universe.
- **Crowding** — currently low; if research notes / Dune dashboards publish per-variant signals widely, edge compresses.

## Kill Criteria

- Drawdown > 25% over rolling 12 months.
- Average monthly return < 30bp over 4 consecutive quarters.
- Major synthetic-stable mechanism failure (death spiral) — pause and reassess.
- Regulatory action specifically against synthetic stables in your jurisdiction.

## Advantages

- **Mechanism-aware** — the trade is calibrated to the specific peg-restoration mechanism rather than generic mean-reversion.
- **Diversified across variants** — basket of 5+ different mechanisms reduces single-protocol idiosyncratic risk.
- **Asymmetric on bridge / sympathy variants** — bounded entry-cost vs 5-25% upside.
- **Pairs with [[cross-chain-contagion-hedge]]** — the sympathy-depeg variant is the stable-leg of that strategy.
- **Capacity** — strategy-level $100M deployable.

## Disadvantages

- **Mechanism-specific data work** — each variant requires its own monitoring + risk model.
- **Structural-break tail risk** — wrong call on "structural vs solvable" can produce large losses (UST 2022 reference).
- **Multi-day holding periods** — capital lockup compounds with multi-variant deployment.
- **Counterparty risk varies by mechanism** — Ethena reserve, Aave Safety Module, Curve smart contract.
- **Cross-chain integration risk** — white-label deployments (jupUSD, USDm, suiUSDe) carry per-deployment audit risk on top of mechanism risk.

---

## Implementation Plan

### Phase 1: Data setup (Weeks 1-2)

**Free-tier components** (zero cost):

| Component | Free implementation |
|-----------|--------------------|
| Curve pool monitoring | Curve subgraph (The Graph free tier) + free RPC reads |
| Balancer pool monitoring (GHO) | Balancer subgraph + free RPC |
| Ethena reserve disclosure | Scrape `gov.ethenafoundation.com` quarterly + Twitter alerts |
| Aave dashboard (PSM, bad-debt) | Aave public dashboard + free Dune fork |
| crvUSD LLAMMA state | Curve frontend / subgraph |
| Funding rate history | HL websocket (free) + Binance API + Deribit public API |
| Exploit alerts (sympathy trigger) | Shared aggregator from [[exploit-arb-implementation-guide]] (Nitter RSS for PeckShield/BlockSec/Cyvers + Forta free tier) |
| Storage | Supabase free tier (500MB Postgres) or SQLite |
| Cron / monitoring | GitHub Actions (free) + Oracle Cloud ARM free VM |

**Total monthly cost**: $0 (free-tier path).

### Phase 2: Real-time peg monitor (Weeks 2-3)

```
┌─ MULTI-VARIANT PEG MONITOR ────────────────────────────────┐
│  Subscribe to free RPC websocket events for:              │
│  • Curve sUSDe/USDC, USDe/USDC, crvUSD/USDC, FRAX/USDC    │
│  • Balancer GHO/USDC                                      │
│  • Curve 3pool composition                                │
│  • White-label pools on Solana (Jupiter), Sui (Cetus)     │
│  Compute deviations vs 30-day rolling baseline            │
│  Alert thresholds: 30bp (sympathy) / 50bp (mechanism)     │
└────────────────────┬───────────────────────────────────────┘
                     ▼
┌─ MECHANISM HEALTH CHECK (on alert) ───────────────────────┐
│  • Ethena reserve solvency check                          │
│  • Aave PSM utilization                                   │
│  • crvUSD LLAMMA band depth                               │
│  • Funding-rate streak detection                          │
│  • Aave bad-debt projection                               │
└────────────────────┬───────────────────────────────────────┘
                     ▼
┌─ TRADE ROUTING (manual approval for first 6mo) ───────────┐
│  • If mechanism solvable: buy depeg + appropriate hedge   │
│  • If structural: skip; alert for manual review           │
│  • Position sizing: scaled-in by deviation                │
└────────────────────────────────────────────────────────────┘
```

### Phase 3: Execution wiring (Weeks 3-4)

**Venues**:
- **Curve / Convex / Balancer (on-chain)** — for spot stable depegs requires on-chain wallet. Gas cost ~$50-200/month.
- **Hyperliquid + Binance perps** — for backing-asset hedges (ETH perp, AAVE perp, CRV perp, FRX perp).
- **Curve / Balancer LP positions** for some variant captures.
- **Direct CEX spot** (Coinbase, Kraken) for redemption-eligible stables — useful for fiat-backed cross-checks.

**API access**: free for all; trading capital is the only spend.

### Phase 4: Per-variant calibration (Weeks 4-8)

For each variant, build a risk model:
1. **sUSDe (Ethena)**: maintain history of funding-rate streaks; flag negative streaks >3 days; check reserve fund status.
2. **GHO (Aave)**: monitor PSM utilization; track Aave bad-debt; flag spillover signals.
3. **crvUSD (Curve)**: monitor LLAMMA band depth; track ETH price velocity; flag band exhaustion conditions.
4. **FRAX hybrid**: monitor CR; track governance proposals; flag CR-adjustment lag.
5. **Sympathy basket**: integrate with exploit aggregator; route confirmed alerts to depeg-buy logic.
6. **Bridge-wrapped**: integrate with bridge-config monitor (per [[multi-dvn-bridge-config-arbitrage]]).

### Phase 5: Live monitoring + iteration (ongoing)

**Operational checklist (daily)**:
- [ ] Review peg deviations >30bp on watchlist
- [ ] Spot-check mechanism health for any flagged stable
- [ ] Confirm position sizing within target weights

**Operational checklist (weekly)**:
- [ ] Update Ethena reserve solvency check
- [ ] Re-run risk-model calibration on prior week's data
- [ ] Review held positions vs exit criteria

**Operational checklist (monthly)**:
- [ ] Variant-set review (any new synthetic stables to add?)
- [ ] Performance attribution by variant
- [ ] Calibrate trigger thresholds based on observed false-positive rate

### Setup time + cost summary

| Item | Cost |
|------|------|
| Setup time | ~120-200 hours |
| Free-tier infra (monthly) | $0-50 (gas only if doing on-chain) |
| Paid-tier upgrades (when capital >$10M) | $1-3K/month |
| Trading capital | $20-50M target deployed |
| Time to first PnL | ~2-6 months (events more frequent than #2 or #4) |

### Where to upgrade to paid

- **Capital >$10M**: paid Cyvers + BlockSec for sub-5-sec sympathy-depeg alerts.
- **Curve / Balancer at-scale execution**: paid Tenderly tier ($100-500/mo) for accurate bad-debt simulation.
- **Multi-chain coverage**: paid Alchemy ($49+/mo) for reliable cross-chain RPC.

## Sources

- Ethena governance forum: `gov.ethenafoundation.com`
- Ethena USDe / sUSDe documentation: `ethena.fi`
- Aave V3 / GHO documentation: `aave.com/help`
- crvUSD documentation: `resources.curve.finance`
- Frax governance forum: `gov.frax.finance`
- Curve Finance subgraph (The Graph)
- Per-incident post-mortems: KelpDAO (Apr 2026), USDC SVB (Mar 2023), stETH depeg (Jun 2022), Terra/UST (May 2022)
- Verified via Perplexity (sonar), 2026-06-10: KelpDAO/rsETH bridge exploit April 2026 confirmed, ~$290-292M loss, used as Aave collateral causing bad-debt risk, ~$13B DeFi TVL drain in following days. Citations: chainalysis.com/blog/kelpdao-bridge-exploit-april-2026, galaxy.com/insights/research/kelpdao-layerzero-exploit-defi, halborn.com/blog/post/explained-the-kelp-dao-hack-april-2026
- [[stablecoin-pair-arbitrage]] — fiat-backed companion strategy
- [[cross-chain-contagion-hedge]] — sympathy-depeg integration
- [[ai-amplified-exploit-arbitrage]] — hub strategy

## Related

[[stablecoin-pair-arbitrage]] · [[lst-depeg-arbitrage]] · [[depeg-risk]] · [[ai-amplified-exploit-arbitrage]] · [[cross-chain-contagion-hedge]] · [[post-hack-incident-response-arb]] · [[2026-exploit-target-watchlist]] · [[ethena-usde]] · [[curve-finance]] · [[makerdao]] · [[ethena]] · [[funding-rate-arbitrage]] · [[2022-05-terra-luna-depeg-arb]] · [[2023-03-usdc-svb-depeg]] · [[2022-06-steth-depeg]] · [[exploit-arb-implementation-guide]] · [[multi-dvn-bridge-config-arbitrage]]
