---
title: "Governance & Restitution Arbitrage"
type: strategy
created: 2026-04-28
updated: 2026-06-20
status: excellent
tags: [arbitrage, crypto, defi, risk-management, event-driven, ai-trading]
aliases: ["Governance-Vote Arb", "Restitution-Claim Arb", "Bridge-Token Discount Arb", "Hack Restitution Arb"]
related: ["[[ai-amplified-exploit-arbitrage]]", "[[post-hack-incident-response-arb]]", "[[2026-exploit-target-watchlist]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-vulnerability-discovery]]", "[[bankruptcy-claim-arbitrage]]", "[[fork-airdrop-triangulation]]", "[[governance-attacks]]", "[[defi-hacks-and-exploits]]", "[[2022-10-mango-markets-exploit]]", "[[2022-04-beanstalk-governance-attack]]", "[[2023-03-euler-finance-exploit]]", "[[2021-08-poly-network-exploit]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: live
edge_source: [analytical, informational]
edge_mechanism: "Post-exploit governance windows create predictable trading patterns. Note: DeFi OTC claim markets are thin to non-existent compared to bankruptcy claim trading — recovery in DeFi typically happens fast (weeks) via direct treasury reimbursement or not at all. Real edges: (a) governance-vote uncertainty arb on protocol-native tokens during decision windows, (b) bridge-token discount arb when wrapped tokens trade below canonical until recapitalization, (c) sympathy-depeg arb on competitor tokens during contagion. Counterparty is forced sellers, panicked LST/LRT holders, and slow-moving market makers."
data_required: [governance-forum-monitoring, on-chain-vote-tracking, otc-claim-quotes, snapshot-vote-data, restitution-distribution-schedules, bridge-token-vs-canonical-spreads]
min_capital_usd: 100000
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: 1.2
expected_max_drawdown: 0.30
breakeven_cost_bps: 100
decay_evidence: "Strategy is less crowded than incident-response arb because OTC claim trading requires desk relationships and longer holding period. Cetus 2025 (frozen-fund vote arb) and Euler 2023 (restitution-claim arb) are recent canonical cases — each yielded 50-100%+ on the relevant leg. Edge persists because governance outcomes are illiquid to price."
---

# Governance & Restitution Arbitrage

The days-2-through-weeks-8 playbook for trading the governance-vote and restitution waterfall after major crypto exploits. Sub-strategy of [[ai-amplified-exploit-arbitrage]].

> **Important reality check (added 2026-04-28):** Initial drafts of this page assumed an active OTC market for DeFi exploit claims trading at 20-40c → 60-90c, paralleling FTX/Mt. Gox bankruptcy claim trading. **Primary-source research (Perplexity verification, April 2026) found this market does not meaningfully exist for DeFi.** Recovery in DeFi typically happens fast via direct treasury reimbursement (Euler weeks, Wormhole hours via Jump recap) or not at all (Beanstalk total loss; KelpDAO ongoing). Found Network is not active for DeFi-specific claims; major OTC desks (Wintermute, Cumberland, Galaxy) do not publicly quote DeFi claims as a product line. **The real edges in this category are governance-vote uncertainty (on protocol-native tokens), bridge-token discount arb (wrapped tokens below canonical), and sympathy-depeg arb on competitors during contagion.** This page has been updated to reflect that.

The three sub-trades that *do* work in practice:
- (a) **Governance-vote uncertainty arb** — trade the protocol-native token during the post-exploit governance decision window (pause / refund / fork / no-action).
- (b) **Bridge-token discount arb** — wrapped/bridged tokens trade below canonical until recapitalization (Wormhole/Ronin/Multichain pattern).
- (c) **Sympathy-depeg arb on competitors** — when one LRT/stable/protocol-class member is hit, others trade weak in sympathy regardless of direct exposure.

Cetus (2025), Wormhole (2022), Beanstalk (2022 — total-loss reference), Euler (2023), and KelpDAO (April 2026) are the canonical case-study set.

## Where this sits in the arbitrage family

This is an event-driven [[arbitrage]] strategy — the crypto-native analogue of risk-arbitrage's legal/regulatory event sub-family, where the "deal" is a governance vote or recapitalization rather than a merger. It shares the short-volatility, binary-outcome profile of merger-arbitrage (collect on the high-base-rate good outcome, take a large loss on the tail), but trades on-chain governance and bridge mechanics instead of antitrust and proxy votes.

| Dimension | Governance & restitution arb (this page) | [[bankruptcy-claim-arbitrage]] | merger-arbitrage / risk-arbitrage |
|---|---|---|---|
| Event | DeFi exploit → governance vote / recap | CeFi bankruptcy (FTX, Celsius, Mt. Gox) | Announced M&A |
| Instrument | Protocol-native token, bridge/wrapped token, sympathy peers | Tradeable bankruptcy claims (real OTC market) | Target equity (± acquirer short) |
| Claim market | Thin to non-existent for DeFi (see reality check) | Deep, multi-year secondary market | n/a |
| Hold | Days to ~16 weeks | Months to years | Weeks to months |
| Tail loss | Vote/recap fails → −30% to −80% | Lower recovery than priced | Deal break → fall to undisturbed price |
| Edge type | Analytical + informational | Analytical (recovery modeling) | Analytical + risk-bearing |

The persistence of the edge is a [[limits-to-arbitrage]] story: governance outcomes are illiquid to price, holding periods are long and uncertain, and the reputational/ethical friction of trading victim losses keeps the competitor set small.

## Edge Source

**Analytical** + **informational**.

- **Analytical:** Restitution outcomes are illiquid to price. Markets gravitate toward 20-40c on the dollar by reflex; analytical work (forum reading, governance-token concentration, attacker negotiation history) frequently shows much higher expected recovery. The mispricing is structural, not random.
- **Informational:** Forum posts, governance-team Twitter, attacker on-chain behavior (returning funds, mixing, holding) all leak information about likely vote outcomes. Skilled monitoring beats the consensus claim-quote.

## Why This Edge Exists

1. **Forced sellers.** Hack victims often need liquidity *now* — they've lost capital, may face margin calls or LP redemptions, and don't have appetite to wait 4-12 weeks for a vote that might fail. They sell into thin OTC markets at 20-40c on the dollar.
2. **Forum/vote informational asymmetry.** Reading governance forums (Discourse, Snapshot, Tally), monitoring large-holder voting patterns, and tracking attacker on-chain behavior (whitehat-style return moves vs Tornado-Cash deposits) gives a much better estimate of vote outcome than the OTC market price.
3. **Timing-of-distribution discount.** Even when restitution probability is high, distribution can take 4-16 weeks. Markets discount this aggressively; capital with patience captures the spread.
4. **Bridge-token sub-case**: when a bridge is exploited, the wrapped tokens (e.g., wBTC on the bridge, USDC.e on the bridge) trade at a discount to the canonical token because the bridge's reserve is now a fractional reserve. The discount converges to zero only when the protocol recapitalizes.

Counterparty list:

- Hack victims dumping IOU/claim positions for immediate liquidity.
- Retail / fund holders exiting at "first sale wins" prices on Snapshot-traded tokens.
- Wrapped/bridged-token holders selling at depeg without modeling recapitalization probability.
- Other arb desks unwilling to commit capital for 4-16 weeks at uncertain outcomes.

## Null Hypothesis

If markets priced post-exploit outcomes efficiently, the protocol-native token would gap once to the probability-weighted outcome on disclosure and then drift randomly; bridge-token discounts would equal (1 − p_recap) × loss-given-failure with no excess convergence return; and competitor tokens would move only in proportion to verified direct exposure. Under that null, buying governance-window dips, discounted wrapped tokens, or sympathy-depegged competitors earns zero after the ~100 bps cost stack and the ~15% total-loss tail — the apparent edge would just be tail-risk premium. The 2021-2026 case set (Wormhole 24h reconvergence, Euler full return, Cetus freeze-and-restitute, KelpDAO sympathy depegs) shows repeated overshoot-and-revert beyond what tail-loss compensation explains. But each new event must be tested against the null that the entry price already reflects the true failure probability: Beanstalk (2022) and Multichain (2023) are the events where the null held and buyers of the dip took total or near-total losses.

## Variants

| Variant | Time horizon | Capital required | Edge mechanism |
|---------|-------------|-----------------|----------------|
| **Governance-vote uncertainty arb** | days 2-30 | low ($100K-$10M) | Protocol-native token mispriced during governance decision window |
| **Bridge-token discount arb** | hours-weeks | medium ($1M-$50M) | Wrapped tokens trade below canonical until recapitalization |
| **Sympathy-depeg arb on competitors** | hours-weeks | medium ($1M-$30M) | Class-wide tokens (other LRTs, other stables, other AMM forks) trade weak in sympathy without direct exposure |
| ~~Restitution-claim arb~~ | n/a | n/a | **Not active for DeFi** — see reality check above. Bankruptcy-claim arb (FTX/Celsius/Mt Gox) is a separate strategy: see [[bankruptcy-claim-arbitrage]] |

## Rules

### Sub-strategy A: Governance-Vote Arb

1. **Identify the vote.** Within 24-48h of a major exploit, the protocol team typically posts a governance proposal: pause, refund, fork, attacker-bounty, or asset-freeze.
2. **Read the forum thread.** Protocol Discourse, Snapshot, Tally, governance Discord. Look for:
   - Team's stated preference (often signals likely outcome).
   - Major holder positions (whales who can swing the vote).
   - Procedural details — quorum, voting period length, timelock.
3. **Estimate vote probability.** Convert forum sentiment + large-holder stake distribution + historical-precedent into a probability (e.g., Cetus 2025: large pre-vote signal from Sui Foundation → 80%+ approval probability).
4. **Compare to market price of frozen-IOU**: if (probability × full-recovery-value) >> market IOU price, buy.
5. **Position size limited to** the amount you can hold through a -100% stop (vote could fail; attacker could refuse to negotiate).
6. **Exit on vote resolution** or pre-vote price re-pricing.

### Sub-strategy B: Restitution-Claim Arb

> **Historical template only.** Per the reality check above, a liquid OTC market for DeFi exploit claims does not meaningfully exist (verified April 2026); DeFi recovery is fast treasury reimbursement or total loss. These rules are preserved as the template that *would* apply if such a market develops, and as the working playbook for the adjacent [[bankruptcy-claim-arbitrage]] (FTX / Celsius / Mt. Gox), where claim markets are real.

1. **Wait for the OTC market to develop** — usually 1-4 weeks post-exploit. Found Network, individual broker desks, sometimes on-chain (e.g., FTX claim trading on Found Network during 2023-2024).
2. **Estimate expected restitution.** Components:
   - Treasury / protocol reserves available to pay claims.
   - Insurance coverage (Nexus Mutual, Sherlock, etc.).
   - Attacker-returned funds (some incidents: 100%; many: 0%).
   - Whitehat / restitution-bounty terms.
   - Time-to-distribution (4-16 weeks typical).
3. **Buy OTC claims at quote ≤ 0.5 × expected restitution.**
4. **Hold to distribution.** Most claim arb is held to maturity; secondary sales are possible but at further discounts.
5. **Tax-efficient structuring.** Coordinate with tax counsel — claim purchases vs original-loss treatment differs by jurisdiction. (See [[tax-implications-trading]].)

### Sub-strategy C: Bridge-Token Discount Arb

1. **Identify the wrapped token** (e.g., USDC.e on Polygon post-Multichain hack, wETH on a compromised bridge).
2. **Estimate recapitalization probability and timeline.** Bridge protocols differ enormously: Wormhole (Jump Trading recapitalized in days); Ronin (Sky Mavis raised funds in weeks); Multichain (no recapitalization, total loss).
3. **Buy the wrapped token at ≥ 30% discount to canonical** if recapitalization probability > 50% and timeline < 3 months.
4. **Hedge directional risk** by shorting the canonical token (or at least the asset class — e.g., short BTC perp if buying wBTC at discount).
5. **Exit on either** (a) recapitalization announcement, or (b) protocol formally announces no recapitalization (hard stop).

## Implementation Pseudocode

```python
on governance_proposal_posted(protocol, proposal):
    forum_sentiment = analyze_discourse(protocol.forum, proposal)
    whale_stakes = on_chain_voting_power(protocol.governance_token)
    historical_pass_rate = governance_history(protocol)
    
    p_pass = bayesian_combine([forum_sentiment, whale_stakes, historical_pass_rate])
    market_iou_price = quote_from_otc_or_snapshot(protocol)
    fair_value = p_pass * full_recovery_value(proposal)
    
    if market_iou_price < 0.5 * fair_value:
        buy_iou(protocol, size=min(0.3 * limit, 0.05 * iou_market_depth))
        exit_when(vote_resolved or price >= 0.9 * fair_value or stop_loss=-50%)

on otc_claim_quote_received(protocol, exploit_event, quote):
    expected_restitution = estimate_recovery([
        treasury_funds(protocol),
        insurance_coverage(protocol, exploit_event),
        attacker_returned_funds(exploit_event),
        bounty_terms(exploit_event)
    ])
    time_to_distribution = estimate_timeline(protocol.governance, exploit_event)
    discount_factor = 0.95 ** time_to_distribution.weeks
    fair_value = expected_restitution * discount_factor
    
    if quote < 0.5 * fair_value:
        buy_claim(otc_desk, protocol, size=min(0.2 * limit, quote.max_size))
        hold_until_distribution()

on bridge_exploit(bridge, wrapped_tokens):
    p_recap = estimate_recapitalization(bridge.team, bridge.backers)
    timeline = estimate_recap_timeline(bridge)
    
    for wt in wrapped_tokens:
        canonical = wt.canonical_pair
        discount = 1 - (wt.price / canonical.price)
        if discount > 0.30 and p_recap > 0.5 and timeline < 90_days:
            long(wt, size=0.2 * limit)
            short(canonical, size=0.2 * limit * 0.8)  # imperfect hedge
            exit_when(discount < 0.05 or recap_failed)
```

## Indicators / Data Used

- **Governance forums**: Discourse (Beanstalk, Aave, Compound, Lido, Frax, Maker), Snapshot.org, Tally.xyz, Commonwealth.im, Cosmos Hub forum.
- **On-chain vote tracking**: Tally (Aave, Compound), Snapshot subgraph, raw governance contract event logs.
- **OTC claim markets**: Found Network (https://found.network), individual broker quotes (BitOTC, FBG, Wintermute OTC, Cumberland OTC), occasional secondary listings on Snapshot.
- **Bridge-recapitalization tracking**: protocol Twitter, team Discord, backer (e.g., Jump for Wormhole) public statements.
- **Insurance coverage**: Nexus Mutual cover marketplace, Sherlock public dashboard, InsurAce.
- **Snapshot vote data**: real-time vote tally, top-voter addresses, voting-power-by-address.

## Example Trades

**Cetus (Sui, May 22 2025) — validator-freeze + governance uncertainty arb.** $223M drained via the `checked_shlw` overflow flaw; **$62M bridged to Ethereum, $162M frozen by permissionless validator action** (each validator independently chose to block transactions from two attacker addresses; this was *not* a snapshot governance vote as previously stated). Cetus subsequently proposed a community vote for a protocol upgrade returning frozen funds via treasury + Sui Foundation loan.
- *Direct trade window*: SUI down ~12% intraday on disclosure; CETUS down 60-70%. Short SUI perp on first credible report; cover within 24-48h as scope clarified. ~7-12% on the perp leg.
- *Validator-freeze decision uncertainty (T+1 to T+3 days)*: brief uncertainty discount on SUI as market priced whether validators would actually act; reverted as freeze was confirmed.
- *Sector*: Aptos modest inflow as Move-VM risk-rotation candidate.
- **No documented OTC claim market** for Cetus victims; recovery happened via Cetus treasury restitution mechanism, not secondary claim trading.
- Sources: Quill Audits, Dedaub, Cyfrin, BlockSec, Binance.

**Balancer (multi-chain, November 3 2025) — DAO-treasury restitution canonical case.** $128.64M drained via `_upscaleArray`/`mulDown` rounding error in 65+ micro-swaps within `batchSwap`. Recovery: BIP-908 passed Feb 10, 2026 (3 months post-exploit); 10% bounty (cut from initial 20% offer); 90% to victims via DAO treasury.
- *Direct trade window*: PeckShield real-time tracking ramped $70M → $128M within minutes. BAL down 20-30%; recovered ~50% within 72h. Short-and-cover captured the overshoot.
- *Governance window (Nov 2025 - Feb 2026)*: BAL traded weak through 3-month vote uncertainty; rallied on BIP-908 passage. Long-BAL into the vote was a viable position-trade for those with conviction the DAO would approve restitution.
- *Sector*: Curve, Uniswap (rival AMMs) saw modest inflow.
- **No documented OTC claim market** for Balancer victims; recovery via DAO-treasury distribution post-vote.
- Sources: Check Point Research, Halborn, Rekt News, BIP-908 Snapshot.

**Euler Finance (March 2023) — voluntary-return case.** $197M donation-attack.
- Initial: EUL token down 50%+ on disclosure.
- Negotiation phase (~3 weeks): attacker (self-identified as "Jacob") progressively returned funds after on-chain communication and apparent OFAC pressure.
- Final: 100% returned. EUL recovered.
- *Trade*: directly long EUL once on-chain return signals were clear (typically days 5-14 of negotiation). ~50-100% on the directional leg over weeks.
- **No documented secondary claim market** — protocol governance authorized direct treasury reimbursement to whitelisted victim addresses; settlement was on-chain.
- Sources: Chainalysis, Elliptic.

**KelpDAO / LayerZero (April 2026) — bridge-discount + sympathy-depeg canonical case.** $290M via 1-of-1 DVN compromise; rsETH stolen, immediately collateralized on Aave/Compound/Euler for $236M borrow. Aave Guardian froze rsETH within 90 minutes; Circle reportedly froze attacker USDC (Aave freeze confirmed by multiple post-mortems; the Circle freeze is less consistently documented). **$15B TVL drain across DeFi within 48h.** LayerZero post-mortem identified mechanism as RPC poisoning + DDoS forcing failover to corrupted nodes.
- *Bridge-discount window*: rsETH dislocated from canonical ETH price during the freeze window — short window but high-magnitude depeg.
- *Sympathy-depeg arb*: other LRTs (eETH, ezETH, weETH) traded weak even without direct exposure. Long the strongest LRT / short the weakest pair-trade worked in the 48h freeze window.
- *Sector rotation*: Across (intent-based bridge with zero major exploits) saw inflows; LayerZero apps with multi-DVN configs were re-rated relative to 1-of-1 DVN configs.
- *Aave bad debt overhang*: $123.7M-$230.1M depending on socialization model; AAVE token traded weak through resolution debate.
- Sources: Galaxy Research, Elliptic.

**Poly Network (August 2021) — early canonical case.** $611M stolen; "Mr. White Hat" returned funds within 2 weeks.
- Initial: claim markets barely existed yet (early DeFi); but bridge-token discount was extreme. Wrapped-asset prices on Poly Network bridges traded at 10-30c on the dollar.
- Resolution: full return of funds within 13 days; Poly Network paid the attacker $500K bounty.
- *Trade*: long bridged tokens at extreme discount; settled at par. Multi-x returns for those who acted in the first 24h.

**Beanstalk (April 2022) — total-loss reference case.** $182M flash-loan governance attack.
- Attacker drained the protocol's governance treasury via flash-loaned voting power. Funds went to Tornado Cash; no recovery.
- *Trade*: BEAN token was liquidated; no recovery vote could be held; no restitution. Total loss.
- *Lesson*: when the attack is on the governance mechanism itself, restitution arb has no edge — there's nothing to vote on. **This is the bear case** for the strategy: ~15% of major exploits resolve this way.

**Wormhole (February 2022) — bridge recapitalization canonical case.** $325M drained; **Jump Crypto recapitalized within 24 hours**, replacing the stolen ETH. Jump subsequently executed a "counter-exploit" on Oasis Protocol to recover $140M from the original attacker's vault positions.
- *Trade*: Wormhole-wrapped wETH on Solana traded briefly at ~$2,200 vs canonical ETH at $2,800-$3,000. Discount closed within 24h on Jump's announcement.
- *Result*: ~25% return on bridge-token discount arb in <24h. Required quick reaction and confidence in Jump's commitment.

**Ronin (March 2022) — slow recapitalization case.** $625M validator-key compromise.
- Sky Mavis (Ronin's parent) raised $150M to partially recapitalize over ~6 months.
- *Trade*: bridge tokens on Ronin (e.g., wETH-Ronin) traded at significant discount; full recap took longer than expected.
- *Lesson*: bridge-token discount arb works only when (a) recap is announced and credible, (b) timeline is bounded. Open-ended losses are not arbable.

## Recovery-path reference (canonical cases)

The single most predictive variable is the *recovery mechanism* — it determines both the upside and the tail. Drawn from the documented cases above (sources cited per case and in Sources):

| Event | Year | Recovery mechanism | Outcome | Tradeable leg |
|---|---|---|---|---|
| Wormhole | 2022 | Backer recap (Jump, ~24h) | Full | Bridge-token discount (closed <24h) |
| Ronin | 2022 | Slow backer recap (Sky Mavis, ~6mo) | Partial / slow | Bridge discount — only after credible, bounded recap |
| Poly Network | 2021 | Attacker voluntary return (~13d) | Full | Bridge-token deep discount → par |
| Euler | 2023 | Attacker return → treasury reimbursement (~3wk) | Full | Long protocol token on return signals |
| Cetus | 2025 | Validator freeze + treasury/foundation loan | Restituted | Validator-freeze uncertainty; short-then-cover SUI |
| Balancer | 2025 | DAO-treasury vote (BIP-908, ~3mo) | 90% to victims | Governance-window long into the vote |
| KelpDAO / LayerZero | 2026 | Guardian freeze + bad-debt socialization debate | Mixed / ongoing | Bridge discount + sympathy-depeg pair trade |
| Beanstalk | 2022 | Governance treasury drained; funds to Tornado Cash | **Total loss** | None — the null held; dip-buyers lost everything |
| Multichain | 2023 | No recapitalization | **Total loss** | None — open-ended loss is not arbable |

The two total-loss rows are the strategy's reason for sizing discipline: roughly ~15% of major events resolve with no recovery, and on those the dip is a trap, not an entry. This is the same short-volatility asymmetry that governs merger-arbitrage deal breaks — size off the tail, not the headline overshoot.

## Performance Characteristics

**Updated 2026-04-28** based on Perplexity primary-source verification: prior estimates assumed active OTC claim trading that does not exist for DeFi. Revised distribution across major 2022-2025 incidents focuses on the three sub-trades that actually work in practice (governance-vote uncertainty arb on protocol tokens, bridge-token discount arb, sympathy-depeg arb):

- Median return on capital deployed per event (governance-window directional): ~15-25%.
- 75th percentile: ~50-70% (Wormhole-style bridge-discount, Cetus-style validator-freeze).
- 25th percentile: ~0-5% (slow events with limited dislocation).
- Tail-loss events (vote fails, recap fails, total loss): ~15% of events. Loss typically -30% to -60% on the leg.

Sharpe estimate: ~1.0-1.4. **Lower than initially claimed** because the strategy does not have access to bankruptcy-style structured claim markets at deep discounts; instead it relies on directional positioning during governance-decision windows and contagion overshoots, which are noisier than a deep-discount claim purchase that resolves to par.

For a higher-Sharpe related strategy with structured claim markets, see [[bankruptcy-claim-arbitrage]] (Mt. Gox / FTX / Celsius / Voyager / BlockFi) — which has years of secondary trading data.

## Capacity Limits

Per-event capacity bounded by:
- OTC claim market depth (typically $5-30M for major events).
- IOU/snapshot-traded volumes (typically $1-10M, sometimes more if listed on a major venue).
- Bridge-token AMM depth (varies widely; $1-50M).

Strategy-level capacity: ~$100M deployed across the strategy at current event frequency.

## What Kills This Strategy

- **Insurance markets mature.** If Nexus Mutual / Sherlock / re-insurance scale up, victim losses are absorbed by insurance payouts and the OTC claim market shrinks.
- **Standardized restitution mechanics.** If protocols adopt automatic insurance / treasury-funded restitution, the governance-vote uncertainty disappears.
- **Regulatory action.** OFAC sanctions on hacked-asset trading make IOU/claim trading legally hazardous in major jurisdictions.
- **OTC desk consolidation.** If a small number of desks corner claim trading, retail/mid-size capital is squeezed out.
- **Faster distributions.** If protocols adopt 1-week distribution cycles instead of 4-16 weeks, the time-discount edge compresses.

## Kill Criteria

- Drawdown > 30% over rolling 6 months.
- Average per-event extracted value drops below 1% of capital deployed for two consecutive quarters.
- Major regulatory action against trading hacked-asset claims in your jurisdiction.
- Insurance penetration on top-50 DeFi protocols exceeds 80% (signal that the OTC market is no longer the primary recovery path).

## Advantages

- Higher Sharpe than incident-response arb (longer holding period, analytical edge).
- Less crowded (requires desk relationships and patience; not retail-friendly).
- Asymmetric: bounded downside on each position (max -50% to -80%); large upside on positive outcomes (100-300%).
- Recurring opportunity (multiple major events per year, each with multiple sub-legs).

## Disadvantages

- Capital lockup of 4-16 weeks per restitution position.
- Requires OTC desk relationships (not accessible to all participants).
- Reputational and ethical concerns about profiting from victim losses (some LPs explicitly prohibit; some jurisdictions raise legal questions).
- Tail-risk events (governance vote fails, attacker disappears with funds, bridge fails to recapitalize) produce sharp adverse moves.
- Tax treatment varies by jurisdiction; specialist counsel needed.

## Sources

- [[ai-amplified-exploit-arbitrage]] — hub strategy.
- [[bankruptcy-claim-arbitrage]] — adjacent strategy (Mt. Gox / FTX / Celsius / Voyager) with similar mechanics.
- Public exploit post-mortems for Cetus (May 2025), Balancer (Nov 2025), Euler (Mar 2023), Poly Network (Aug 2021), Wormhole (Feb 2022), Ronin (Mar 2022), Beanstalk (Apr 2022).
- Found Network claim-trading data for FTX / Celsius / Voyager (parallel mechanics).
- Cetus governance forum, Sui Foundation public statements (May 2025).
- Balancer Snapshot vote records (Nov 2025).
- Verified via Perplexity (sonar), 2026-06-10: KelpDAO/LayerZero April 2026 exploit confirmed (~$290-292M rsETH via compromised 1-of-1 DVN; Aave froze rsETH/wrsETH/WETH markets; ~$15B DeFi TVL drain). Balancer v2 exploit Nov 3 2025 (~$128M) confirmed. Citations: sigintzero.com/blog/kelp-dao-292m-layerzero-dvn-exploit, hypernative.io (KelpDAO observation-layer post-mortem), chainalysis.com/blog/kelpdao-bridge-exploit-april-2026, galaxy.com/insights/research/kelpdao-layerzero-exploit-defi. BIP-908 passage details per Balancer Snapshot records (not independently re-verified in this pass).

## Related

[[arbitrage]] · [[arbitrage-overview]] · risk-arbitrage · merger-arbitrage · [[event-driven-trading]] · [[limits-to-arbitrage]] · [[ai-amplified-exploit-arbitrage]] · [[post-hack-incident-response-arb]] · [[2026-exploit-target-watchlist]] · [[smart-contract-vulnerability-taxonomy]] · [[ai-vulnerability-discovery]] · [[bankruptcy-claim-arbitrage]] · [[fork-airdrop-triangulation]] · [[fork-futures-spot-basis]] · [[governance-attacks]] · [[defi-hacks-and-exploits]] · [[2022-10-mango-markets-exploit]] · [[2022-04-beanstalk-governance-attack]] · [[2023-03-euler-finance-exploit]] · [[2021-08-poly-network-exploit]]
