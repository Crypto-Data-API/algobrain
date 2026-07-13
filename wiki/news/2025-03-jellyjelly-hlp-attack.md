---
title: "JELLYJELLY HLP Attack — March 2025"
type: news
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [news, crypto, defi, hyperliquid, hlp, exploit, market-manipulation, oracle]
aliases: ["JELLYJELLY Incident", "HLP Manipulation Attack", "Hyperliquid Jelly Attack", "JELLY Attack March 2025"]
event_date: 2025-03-26
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 4
related: ["[[hyperliquid]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-vault-architecture]]", "[[hyperliquid-oracle-mechanics]]", "[[hyperliquid-liquidation-engine]]", "[[jelly-my-jelly]]", "[[oracle-risk]]", "[[market-manipulation]]", "[[hlp-cascade-alongside-playbook]]"]
---

# JELLYJELLY HLP Attack — March 2025

On **March 26, 2025**, a coordinated trader executed a multi-venue manipulation attack against [[hyperliquid]]'s [[hyperliquid-hlp-basis-arbitrage|HLP vault]] using the thinly-traded **JELLY (JELLYJELLY) perpetual** contract. The attacker opened an outsized **short** position (~**$4.1M** notional) on the JELLY perp on Hyperliquid, then **pumped JELLY spot up** on Solana DEXs (price spiked ~250–500%, above $0.05) to drive the oracle-fed mark price higher against their own short. The rising mark forced self-liquidation of the short, and HLP — as protocol-native liquidator of last resort — was forced to **absorb the underwater short** as JELLY kept climbing. HLP's peak mark-to-market loss reached **~$12M** (per Arkham/Kaiko/Oak Research analyses and HypurrScan dashboards), with the vault left holding a **~$15.3M short position**, before the Hyperliquid validator set intervened, delisted the JELLY perpetual, and **force-settled outstanding positions at $0.0095** — a level favorable to HLP. After settlement, HLP closed the episode with a **net profit of ~$700K** rather than a realized loss. The incident became a watershed event for on-chain perpetual exchange design — exposing structural vulnerabilities in oracle-based mark pricing, thin-pair listings, and protocol-native market makers.

## Background

**Hyperliquid** is a custom Layer-1 blockchain optimized for derivatives trading, launched on mainnet in 2023. It runs an on-chain central-limit order book (not an AMM) with sub-second block times and CEX-grade execution. By Q1 2025, Hyperliquid had become the dominant decentralized perpetual-futures venue, with daily volumes of $1-3B and over $300M in TVL.

**HLP (Hyperliquidity Provider)** is the protocol's own market-maker and liquidator vault, capitalized by USDC depositors. HLP automatically:

- Provides quotes on every Hyperliquid perpetual market.
- Takes the other side of liquidations (a "liquidator of last resort").
- Earns spread, taker rebates, liquidation bonuses, and funding-rate harvest.
- Distributes profits to depositors as ongoing yield (~25-60% APR through 2024).

By design, HLP is **the counterparty** when no other liquidity is available. This makes it highly profitable in normal markets — and structurally exposed to coordinated attacks that exceed its absorption capacity.

**JELLYJELLY** ([[jelly-my-jelly]]) is a Solana-based memecoin from the **Pump.fun** ecosystem, launched in early 2025. It has a fully-diluted supply of 1B tokens, a market cap in roughly the **$10-25M** range around the time of the attack, and shallow on-chain liquidity concentrated on Solana DEXs (primarily Raydium and Orca pools). Hyperliquid had listed a JELLY perpetual contract as part of its rapid memecoin-perp expansion strategy in early 2025.

The combination of (a) thin spot liquidity, (b) on-chain oracle price feed sourced from the same thin spot pools, and (c) HLP as forced counterparty created the attack surface.

## The Attack Mechanic

Per community reconstructions and on-chain forensics ([HypurrScan](https://hypurrscan.io), Solscan), the attack proceeded roughly as follows:

### Step 1 — Build large short position on Hyperliquid
The attacker opened a very large **short** on the JELLY perpetual on Hyperliquid (~**$4.1M** notional, leveraged size much larger). On a thin-pair perpetual, a short of this size effectively forced HLP onto the long side via market-making — Hyperliquid's organic taker flow could not absorb a position that scale.

### Step 2 — Pump spot JELLY on Solana
With the perp short established, the attacker (or coordinated wallets) **bought** large quantities of JELLY spot on Solana DEXs (primarily Raydium AMM pools). Because spot liquidity was shallow, the purchases drove the spot price **up** sharply within minutes (a spike of roughly 250–500%, taking the price above $0.05).

### Step 3 — Oracle median follows
Hyperliquid's [[hyperliquid-oracle-mechanics|oracle for JELLY]] was sourced (per Hyperliquid documentation) from a median of multiple spot venues — but those venues were dominated by the same Solana DEX pools the attacker was pumping. The oracle median rose sharply.

### Step 4 — Mark price rises, attacker's short faces liquidation
As the oracle moved, the perp's mark price followed it up. The attacker's own large short position became liquidatable. **This is the inversion that made the attack work**: the attacker *wanted* their short to be liquidated, because the position was so large that liquidation would force HLP — not external takers — to absorb it at the now-distressed mark.

### Step 5 — HLP forced to absorb the short side at elevated prices
With the attacker's short liquidated and no organic counterparty near the manipulated price, HLP took on the position as last-resort liquidator. HLP was now sitting on a large **short** JELLY position (~$15.3M notional) acquired at the artificially-inflated price — and JELLY was still being pumped.

### Step 6 — Mark keeps rising → HLP underwater
With JELLY spot continuing higher, HLP's short went deeply underwater. Peak mark-to-market loss on HLP's position reached an estimated **~$12M** (per Arkham, Kaiko, Oak Research, and on-chain trackers). At the extreme, had JELLY's mark continued to climb, HLP's losses on the ~$15.3M short could have run materially higher.

```
Time T0: Attacker SHORT perp (HLP de facto LONG-side maker)
Time T1: Attacker PUMPS spot → oracle rises
Time T2: Mark rises → attacker's short liquidates
Time T3: HLP absorbs the short at inflated mark
Time T4: Spot keeps rising → HLP short underwater (~$12M peak loss)
Time T5: Validator intervention → perp delisted, positions force-settled at $0.0095
```

The attack required no exploit of code — it was a pure economic / oracle-design attack, comparable in mechanism to the [[mango-markets-2022-exploit|Mango Markets manipulation]] by Avraham Eisenberg in October 2022.

## Hyperliquid's Response

The response unfolded over several hours:

1. **Detection.** Community traders and HLP-watchers (Twitter/X accounts tracking [[hyperliquid-vault-architecture|HLP positioning]] in real time) flagged the rapidly growing HLP loss within an hour of the attack initiating.
2. **Validator coordination.** The Hyperliquid validator set — a small group at the time (approximately 4-16 validators, per Hyperliquid disclosures) — coordinated off-chain on whether to intervene.
3. **Perp delisting.** The validator set voted to **delist the JELLYJELLY perpetual** entirely. Outstanding positions were force-settled.
4. **Settlement price.** Per Hyperliquid's post-mortem, open JELLY positions were force-settled at **$0.0095** — a price favorable to HLP (well below the pumped level). This effectively **clawed back the manipulation losses** rather than allowing HLP to crystallize the ~$12M paper loss.
5. **Net result for HLP.** Far from a loss, HLP closed the episode with a **net profit of ~$700K** after the $0.0095 settlement — the intervention turned a ~$12M peak unrealized loss into a small realized gain.
6. **Communication.** Hyperliquid published a post-mortem on Twitter/X and via governance channels within ~24-48 hours, framing the event as a manipulation attempt rather than an exploit, and announcing structural changes.

## Lessons Baked Into the Response

Hyperliquid implemented several immediate and follow-on changes:

| Change | Description |
|--------|-------------|
| **Tighter listing criteria** | New perp listings require minimum spot liquidity floors, market-cap minimums, and multi-venue oracle sources. Pump.fun-style memecoins under a threshold no longer auto-qualify. |
| **Position-size limits per market** | Max open interest caps per pair, scaled by thin-pair liquidity. Prevents a single trader from sizing larger than HLP's safe absorption capacity. |
| **HLP exposure caps per asset** | HLP's vault now has hard limits on how much it will absorb in any single thin-pair before circuit-breakers engage. |
| **Manual oracle anomaly review** | Oracle moves exceeding configured thresholds within short windows can trigger trading halts pending review. |
| **Liquidator routing changes** | Liquidations on thin-pair perps may now route through TWAP windows rather than instantaneous fills against HLP. |

These changes are documented in Hyperliquid's post-incident communications and in subsequent governance/listing documentation.

## Why Validator Intervention Was Controversial

The decision to **force-settle** open positions and unwind the attacker's gains drew sharp criticism from parts of the crypto community on neutrality grounds:

- **Pro-intervention argument:** HLP is depositor capital; allowing a coordinated manipulation to crystallize a ~$12M loss would have set a precedent that thin-pair attacks are profitable, encouraging copycat attacks that could ultimately destroy HLP and the entire protocol. Validator intervention is a legitimate emergency power.
- **Anti-intervention argument:** "Code is law" — the attacker did not exploit a smart-contract bug; they used the rules as written. Intervening sets the precedent that Hyperliquid validators can reverse trades when outcomes are unfavorable to the protocol. This makes Hyperliquid less neutral than CEX competitors and contradicts the value proposition of decentralized derivatives.
- **Comparisons drawn:** The intervention was compared to (a) [[the-dao-hack-2016|The DAO hard fork]] (Ethereum 2016), (b) Binance's "rollback" comments after the 2019 hack (never executed), and (c) FTX's special exemptions for Alameda. Critics argued any of these compromises ultimately erode trust in venue neutrality.

The controversy did not appear to damage Hyperliquid's growth trajectory — TVL and volumes continued to climb through Q2 2025 — but it remains a point of governance discussion.

## What This Means for HLP Depositors

For users considering [[hyperliquid-hlp-basis-arbitrage|HLP as a yield strategy]]:

- HLP's risk profile is **not infinite-tail-risk** in practice — the validator backstop limits maximum loss in extreme manipulation scenarios.
- However, this protection is **discretionary**, not contractual. It depends on validator coordination and willingness to intervene. Future events may not be handled the same way.
- **Monitor new listings.** Each thin-pair listing is a new attack surface. HLP depositors should track which perps go live and reduce exposure during periods of aggressive memecoin-perp expansion.
- **Adverse selection concentration.** HLP profits from many small uninformed flows but takes concentrated losses from a few sophisticated attacks. The risk distribution is fat-tailed.
- **Withdraw lockups matter.** HLP has multi-day withdrawal queues. Depositors cannot escape mid-attack.

## What This Means for HL Traders

For active traders on Hyperliquid:

- **Thin-pair perps remain risky to long** — even after the listing-criteria tightening, smaller-cap perps have wider effective spreads, slippage, and oracle-manipulation risk.
- **Oracle manipulation isn't theoretical.** Any perpetual sourced from on-chain oracles with shallow underlying liquidity can be moved by a sufficiently capitalized attacker. Position sizing on such pairs should reflect this.
- **Watch HLP positioning.** When HLP is heavily on one side of a thin-pair, that side is structurally vulnerable. Trading *with* HLP on these pairs is risky; trading *against* it can be lucrative if you can identify the inflection.
- **Validator backstop is for the protocol, not for you.** If you are caught long the wrong side of a manipulation, you may be force-settled at unfavorable prices. The intervention protects HLP first.

## What This Means for the Broader Ecosystem

The JELLYJELLY attack established a **manipulation playbook** that other protocols must defend against:

- **GMX (Arbitrum/Avalanche)** — uses a similar GLP/JLP vault structure as protocol-native counterparty. GMX has historically been vulnerable to oracle-arbitrage attacks (the September 2022 AVAX manipulation cost GLP ~$565K) and has progressively tightened position limits and oracle sourcing.
- **JLP (Jupiter Perps, Solana)** — Solana-native counterpart to HLP. JLP runs Pyth oracles which are more robust than thin DEX-pool feeds, but is exposed to similar dynamics on smaller-cap listings.
- **dYdX v4** — uses Chainlink oracles with deeper aggregation; less directly exposed but still must police listings.
- **Aevo, Drift, Vertex** — broadly the same architectural pattern; each has its own listing-criteria controversies.

The event also influenced **listing governance** across the DEX-perp sector. Several venues introduced explicit "thin-pair attack" risk disclosures and tightened minimum-liquidity listing thresholds in Q2-Q3 2025.

## Connection to Other Oracle-Manipulation Events

The JELLYJELLY attack fits into a multi-year lineage of [[oracle-risk|oracle-manipulation incidents]]:

| Date | Event | Mechanism | Loss |
|------|-------|-----------|------|
| Oct 2022 | **Mango Markets exploit** (Avraham Eisenberg) | Long MNGO perp, pumped MNGO spot, used inflated mark as collateral, drained treasury | ~$117M |
| Sep 2022 | **GMX AVAX oracle arb** | Arbitraged stale Chainlink price vs CEX price | ~$565K |
| Apr 2023 | **Hundred Finance** | Manipulated HND collateral price | ~$7M |
| Various 2023 | Multiple mid-cap perp DEX pair-specific attacks | Thin-pair spot dump → oracle move | $1-10M each |
| Nov 2024 | **Polter Finance** | Oracle manipulation via pool drain on Fantom | ~$12M |
| 2024 | **Mai Capital / multiple Curve-related oracle attacks** | LP-token mispricing | Various |
| **Mar 2025** | **JELLY (JELLYJELLY) HLP attack** | Short perp → pump spot → oracle rise → HLP forced absorption | ~$12M peak (reversed; HLP +~$700K after $0.0095 settlement) |

The recurring pattern: **shallow on-chain oracle sources + protocol-native counterparty + outsized position = exploitable.** Each event drives an iteration of defensive design (deeper oracle aggregation, position limits, manual review thresholds), but new venues frequently re-introduce the vulnerability when chasing listing breadth.

The JELLYJELLY incident is notable for being one of the few where the protocol's emergency intervention **prevented the attacker from capturing meaningful profit**, distinguishing it from the Mango precedent (where Eisenberg withdrew a substantial fraction before negotiations).

## Sources

- Arkham Intelligence — "JELLYJELLY Exploit on Hyperliquid" research note ([info.arkm.com](https://info.arkm.com/research/jellyjelly-exploit-on-hyperliquid)).
- Kaiko Research — "DeFi Faces New Test as Low-Liquidity Token Gets Manipulated."
- Oak Research — "Hyperliquid JELLY Attack: Context, Vulnerability, Team, Solution."
- Hyperliquid governance and post-mortem posts on Twitter/X (March 2025).
- HypurrScan ([https://hypurrscan.io](https://hypurrscan.io)) — on-chain HLP position tracking and historical PnL.
- Solscan / Solana DEX trade data showing the JELLY spot pump.
- Comparative coverage of the [[mango-markets-2022-exploit|Mango Markets exploit]] for historical mechanism parallel.
- [[hyperliquid-hlp-basis-arbitrage]] — strategy page referencing this incident.
- [[jelly-my-jelly]] — token entity page.

> **Note:** Figures verified against Arkham, Kaiko, and Oak Research analyses (June 2026): attack date March 26, 2025; attacker short ~$4.1M; HLP peak unrealized loss ~$12M on a ~$15.3M short; validator force-settlement at $0.0095; HLP net result ~+$700K. The token-spike magnitude (~250–500%) and market cap (~$10–25M) vary slightly by source.

## Related

[[hyperliquid]] · [[hyperliquid-hlp-basis-arbitrage]] · [[hyperliquid-vault-architecture]] · [[hyperliquid-oracle-mechanics]] · [[hyperliquid-liquidation-engine]] · [[jelly-my-jelly]] · [[oracle-risk]] · [[market-manipulation]] · [[hlp-cascade-alongside-playbook]] · [[mango-markets-2022-exploit]] · [[avraham-eisenberg]] · [[the-dao-hack-2016]] · [[liquidation-cascade-arbitrage]] · [[2026-04-06-hyperliquid-volume-surge]]
