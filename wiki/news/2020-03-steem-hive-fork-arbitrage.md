---
title: "Steem → Hive Fork Arbitrage (March 2020)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, history, hard-fork, airdrop, governance, dpos]
aliases: ["Steem Hive Fork", "Justin Sun Steemit Takeover", "Hive Airdrop"]
event_date: 2020-03-20
markets_affected: [crypto]
impact: high
verified: true
sources_count: 4
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]"]
---

# Steem → Hive Fork Arbitrage (March 2020)

On **March 20, 2020** (~14:00 UTC), the Steem community executed a contentious hard fork to **Hive**, distributing the new HIVE token 1:1 to existing STEEM holders — **except** the wallets controlled by Justin Sun (Tron founder, who had purchased Steemit Inc. in February) and the centralized exchanges (Binance, Huobi, Poloniex) that had collaborated with him in a stake-based 51% attack on the chain. The fork is the **canonical case study for "stake-based 51% attack triggers a defensive community fork"** and demonstrates how DPoS governance can be hijacked by a buyer with exchange relationships.

## Background

Steem was a DPoS (Delegated Proof of Stake) blockchain launched 2016 by Ned Scott and Dan Larimer (later of EOS) for content/social applications. The native STEEM token was used by 20 elected witnesses to validate blocks. **Steemit Inc.** held a "ninja-mined" stake (estimated tens of millions of STEEM, contemporaneously valued in single-digit-million USD) — controversially mined in the chain's first weeks before public launch.

On **February 14, 2020**, Justin Sun (Tron founder) acquired Steemit Inc. and its ninja-mined stake. Existing witnesses worried Sun would use the stake to vote himself into governance and migrate Steem onto Tron. On **February 24**, the existing top witnesses executed soft fork **0.22.2** to **freeze** Steemit's ninja-mined stake, citing community precedent that the stake was earmarked for development, not governance.

On **March 2, 2020**, Sun retaliated. He coordinated with **Binance** (CEO Changpeng Zhao confirmed publicly), **Huobi**, and **Poloniex** (which Sun himself had recently acquired). The exchanges used **customer-deposited STEEM** to vote in 20 Sun-aligned witnesses, replacing the existing witness set and reversing the soft fork. This was a textbook **stake-based 51% attack**, made possible because STEEM's DPoS model didn't distinguish exchange-custody stake from individual user stake.

The community organized a defensive hard fork: **Hive**, with a snapshot taken at the fork block on March 20, 2020. Hive distributed 1:1 HIVE to STEEM holders **except**:
- Sun's wallets and known associates.
- Wallets that had voted with the Sun-aligned witness set.
- The colluding exchange custodial wallets (Binance, Huobi, Poloniex) on the snapshot.

## The Trade

The Hive fork created a textbook **defensive-airdrop arbitrage** with a peculiar wrinkle: **only certain holders qualified**. Pre-snapshot accumulation was straightforward; the catch was holding STEEM on a self-custodial wallet (or an exchange that didn't collude) rather than on Binance/Huobi/Poloniex.

### Trade 1: Self-custody accumulation

1. Withdraw STEEM from Binance/Huobi/Poloniex pre-snapshot.
2. Hold on a self-custody wallet or on a non-colluding exchange (Bittrex, Upbit).
3. At snapshot, receive 1:1 HIVE.
4. Sell HIVE at launch on Binance (~$0.50); peaked ~$0.70 within 48 hours.

Holders who left STEEM on a colluding exchange initially received nothing. Binance and Huobi later (under community pressure) distributed Hive to their customers, but with a multi-week lag — capturing this lag was its own arb.

### Trade 2: Cross-exchange listing arb

Bittrex listed HIVE within hours of fork; Binance and Huobi delayed. STEEM holders who could move quickly between venues captured the early listing premium (~50-80% spread vs the eventual Binance listing).

### Trade 3: Short STEEM / long HIVE

The fork made STEEM the chain effectively controlled by Sun + Tron — viewed as captured by the community. The pair trade **short STEEM / long HIVE** worked over the following months: STEEM declined from ~$0.18 (March 2020) to ~$0.13 (June 2020); HIVE rallied from $0.20 launch to $0.70 in summer 2020 before fading.

### Trade 4: Stake-frozen wallet exploitation

Pre-fork, sophisticated parties identified wallets associated with the Sun-aligned witness vote. These were excluded from the Hive snapshot. Some of these stakes traded OTC at deep discounts (since they were known to be excluded) — informational arbitrage on snapshot eligibility lists.

## Price Action

| Date | STEEM | HIVE | Notes |
|------|-------|------|-------|
| Feb 14, 2020 | $0.22 | n/a | Sun acquires Steemit |
| Feb 24, 2020 | $0.20 | n/a | Soft fork freezes ninja-mine |
| Mar 2, 2020 | $0.16 | n/a | Sun's exchange-coordinated takeover |
| Mar 20, 2020 (fork) | $0.18 | $0.50 (Binance launch) | Hive launches |
| Mar 22, 2020 | $0.16 | $0.70 (peak) | Hive peak within 48h |
| Apr 1, 2020 | $0.10 | $0.30 | Settling |
| Aug 2020 | $0.30 | $0.70 | Both rally with crypto |
| Dec 2024 | $0.18 | $0.27 | Steady-state divergence |

Hive accumulated a ~$200M market cap at peak; Steem stalled around $80M and continued to decline relative to broader crypto.

## Was It Obvious?

**Yes, with caveats.** Once Sun's exchange-coordinated takeover happened on March 2, the probability of a defensive fork was very high — the community had been organizing since Feb 24. The 18-day window between takeover and fork gave traders ample time to position. The genuinely uncertain question was **snapshot eligibility** — exact rules were finalized only days before the fork.

## Who Made Money?

- **Self-custody STEEM holders.** Free 1:1 HIVE airdrop with eventual peak value 2-4x of pre-fork STEEM.
- **Bittrex and other neutral exchanges.** Captured first-listing volume.
- **Community-aligned witnesses.** Earned witness rewards on the new Hive chain.
- **Cross-exchange arbs.** Multi-week listing-lag spreads of 30-80% on Binance/Huobi vs Bittrex.
- **Short-STEEM macro traders.** Steem became a captured chain; long-term decline was predictable.

## Who Lost Money?

- **Customers of Binance / Huobi / Poloniex** initially excluded from the Hive snapshot. Most eventually received Hive (after weeks of community pressure), but at sub-launch prices.
- **Justin Sun.** His ninja-mined stake stayed on Steem (depreciating chain); he received zero Hive.
- **Steem-aligned long-only holders.** Steem's market cap stagnated while Hive captured most of the developer/user mindshare.
- **Poloniex** — reputational damage from the collusion lasted; trading volume declined through 2020-2021.

## Risks

1. **Snapshot eligibility ambiguity.** The rules for excluding "Sun-aligned wallets" were drafted by community consensus in real time. Wallets that participated in the witness vote (even unwittingly via exchange staking) were excluded. Traders had to research wallet provenance before holding STEEM.
2. **Exchange-credit asymmetry.** Binance, Huobi, Poloniex initially refused to credit Hive to customers. Community pressure forced reversal but with weeks of delay. Customers who couldn't withdraw STEEM during the contested period had no recourse.
3. **No replay protection between Steem and Hive technically existed**, but DPoS account-based architecture made cross-chain replay impractical (different witness set signatures).
4. **Stake-attack precedent risk.** The fact that exchange-custody stake was used in a 51% attack raised systemic concerns about *all* DPoS chains (EOS, Tron, BSC) — but trading derivatives on this systemic risk was not feasible.
5. **Hive itself faced 51% attack risk** if attackers acquired enough HIVE on the new chain — but post-fork the social cost of another attack was prohibitive.

## Lessons for Fork Arbitrage

1. **Defensive forks have asymmetric eligibility.** Unlike a standard hard fork (1:1 to all parent holders), defensive forks deliberately exclude attacker-aligned wallets. Snapshot mechanics matter critically — research before holding.
2. **Self-custody timing is a structural arb.** Holders on colluding exchanges may forfeit the airdrop. Withdrawals are time-pressured.
3. **Stake-based 51% attacks are a unique DPoS / PoS fork-arb trigger.** Subsequent events: Cosmos Hub debates, Tron migration concerns, Solana validator-cartel critiques. Any DPoS chain with concentrated exchange custody is vulnerable.
4. **Exchange-credit policy reverses under social pressure.** Binance and Huobi eventually credited Hive after community backlash. The lag was the arb window.
5. **Long-term, defensive forks tend to win.** Hive captured the developer/user mindshare; Steem became a depressed legacy chain. Pair-trading long-Hive / short-Steem worked for years.

## Aftermath

- **2020-2024:** Hive grew to ~30-40% greater market cap than Steem; community-led development continued.
- **Tron / Sun:** Sun reduced his Steem involvement; Steemit Inc. operated minimally; Steem TVL stagnated.
- **DPoS governance reform:** Several DPoS chains (EOS, Lisk) considered governance changes to prevent exchange-custody-based attacks; few implemented binding fixes.
- **Exchange custody governance:** Binance later announced policies preventing customer-stake voting in similar disputes — a direct response to the Steem fallout.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2022-05-terra-luna-2-fork-arbitrage]] · [[corporate-action-arbitrage]]

## Sources

- @theycallmedan and Hive community blog posts (March 2020).
- Justin Sun / Tron Foundation press release on Steemit acquisition (February 14, 2020).
- Changpeng Zhao (Binance) Twitter thread admitting customer-stake vote (March 4, 2020).
- *CoinDesk*: "Steem Block Producers Push 'Hive' Hard Fork to Counter Justin Sun" (March 17, 2020).
