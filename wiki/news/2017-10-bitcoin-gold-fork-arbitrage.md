---
title: "Bitcoin Gold Fork Arbitrage (October 2017)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, history, bitcoin, arbitrage, event-driven]
aliases: ["BTG Fork", "Bitcoin Gold", "Equihash Bitcoin Fork"]
event_date: 2017-10-24
markets_affected: [crypto]
impact: medium
verified: true
sources_count: 4
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]", "[[replay-attack]]"]
---

# Bitcoin Gold Fork Arbitrage (October 2017)

On **October 24, 2017 at block 491,407**, Bitcoin Gold (BTG) hard-forked from Bitcoin with a single intended differentiator: **Equihash GPU-mineable proof-of-work** instead of Bitcoin's SHA-256 ASIC-dominated PoW. Every BTC holder received 1:1 BTG. The fork is the **canonical case of a "premine + low-hashrate" fork that arbitraged briefly profitably but ultimately collapsed under 51% attacks** — making it the structural counter-example to the [[2017-08-bitcoin-cash-fork-arbitrage|BCH 2017]] success.

## Background

Bitcoin Gold was launched by **Jack Liao** (Hong Kong-based mining hardware entrepreneur) and a small developer team. The motivation: Bitmain's near-monopoly on SHA-256 ASIC manufacturing was viewed as centralizing Bitcoin mining. Equihash (the same algorithm used by Zcash) was GPU-friendly and ASIC-resistant *at that time*.

**Key technical features:**
- Hard fork from BTC at block 491,407 (October 24, 2017, ~07:18 UTC).
- 1:1 BTG airdrop to BTC holders at snapshot.
- Equihash PoW (n=144, k=5 — a custom variant designed to differ from Zcash's parameters).
- Difficulty adjustment using DigiShield v3 (every block) — different from BTC's 2,016-block adjustment.
- **Premine of 100,000 BTG** (8,000 to a "team fund" + 100,000 retained as "post-mine" for development) — controversial from launch.
- **Replay protection** via SIGHASH_FORK_ID (similar to BCH).

## The Trade

The setup was structurally similar to BCH 2017 but with weaker fundamentals:

```
Pre-fork: 1 BTC = $5,500
Post-fork: 1 BTC + 1 BTG = total value
```

### Trade 1: Long BTC into the fork, sell BTG immediately

Pre-fork BTC traded $5,500-5,800. Post-fork:
- BTC = $5,400-5,600.
- BTG launched on Bitfinex futures at $300-400 (highly speculative pre-fork pricing).
- BTG actual launch (Oct 24): $470 on first listings.
- BTG within 7 days: $130-150.

A trader who held BTC through the fork and sold BTG at the $470 peak captured ~7-8% on BTC value. Selling at the $300 average launch was still 5-6% over a few hours.

### Trade 2: Short BTG futures / IOU pre-fork (where available)

Pre-fork derivative markets for BTG were **thin** — most exchanges hesitated to list IOUs given the premine concerns. **Bitfinex** ran a chain-split token (BT1/BT2) mechanism similar to the BCH precedent; some implied pre-fork BTG pricing was visible. Where IOU exposure was available, sophisticated desks shorted speculative IOU prints in the $300+ range expecting realistic values of $30-100, and covered post-fork at $50-150. This was a smaller, less-developed analog of what would later become the [[fork-futures-spot-basis|fork-IOU basis trade]] mature at ETHW.

### Trade 3: Cross-exchange listing arbitrage

- **Bitfinex** and **Bittrex** listed BTG immediately on October 24.
- **Coinbase** did not credit BTG to customers — citing the premine as a security/scam concern.
- **Bittrex** later delisted BTG entirely after the May 2018 51% attack.
- **Binance** listed BTG within 48 hours.

The Coinbase non-credit cost their retail customers ~5-10% on their BTC value — though Coinbase customers who knew about the fork could withdraw BTC pre-fork to a self-custody wallet and capture BTG independently.

### Trade 4: Mining-difficulty arbitrage

BTG's difficulty adjustment was per-block (DigiShield v3), so hashrate fluctuations rapidly priced into mining profitability. In the first 48 hours, BTG mining was 5-10x more profitable than Zcash mining (similar Equihash variant). GPU miners who pivoted captured 200-500% APY for 1-2 weeks before difficulty caught up.

## Price Action

| Date | BTC | BTG | BTC+BTG | Notes |
|------|-----|-----|---------|-------|
| Oct 23, 2017 | $5,580 | $400 (futures) | $5,980 | Pre-fork |
| Oct 24, 2017 (fork) | $5,520 | $470 (launch peak) | $5,990 | Snapshot |
| Oct 31, 2017 | $6,400 | $145 | $6,545 | BTC rallying; BTG fading |
| Dec 2017 | $14,000 | $290 | $14,290 | Crypto-bull resurrects BTG briefly |
| May 2018 | $9,000 | $50 | — | After 51% attack |
| End 2024 | $94,000 | $25 | — | BTG faded to obscurity |

Total BTG market cap at fork: ~$8B implied (16.7M circulating × $470 launch). This collapsed to ~$2B within a week, ~$500M within 6 months, and to <$300M by 2024.

## The 51% Attack (May 2018)

On **May 16-19, 2018**, an attacker rented Equihash hashrate (estimated $200k cost via NiceHash) and overwhelmed BTG's network for 4 days. They executed double-spend attacks on **Bittrex** and **Binance**, stealing approximately:

- **Bittrex: ~12,200 BTG (~$2.3M)**
- **Binance: smaller amount, contained quickly**
- **Total estimated theft: ~388,000 BTG (~$18M)** based on multiple double-spends across exchanges

Aftermath:
- **Bittrex delisted BTG** on September 14, 2018.
- BTG required all exchanges to wait **50 confirmations** for deposits (vs ~6 for major chains) — a major UX hit.
- A second 51% attack hit BTG in **January 2020** (~7,000 BTG / ~$70k stolen).

## Was It Obvious?

**The fork itself: yes — well-telegraphed since July 2017.** The community had ~3 months notice. Bitfinex pre-fork futures were liquid. The technical specifications were public.

**The premine controversy: yes.** Coinbase and several other major exchanges flagged it pre-launch.

**The 51% attack risk: predictable but not pre-priced.** Equihash hashrate was small relative to Zcash; BTG had ~3% of Zcash's hashrate at peak. Renting that much hashrate cost ~$200k; the double-spend payout potential was multi-million-dollar. Sophisticated security researchers warned about this from launch, but the IOU market did not fully price it.

## Who Made Money?

- **Self-custody BTC holders.** 1:1 BTG airdrop with peak value of ~$470. Largest aggregate winner cohort.
- **GPU miners pivoting from Zcash** in first 1-2 weeks. 200-500% APY on diverted hashrate before difficulty caught up.
- **Pre-fork BTG-IOU shorts** (where listings existed, primarily Bitfinex). Realistic strategy but thin liquidity capped per-desk extraction.
- **51% attackers (May 2018).** ~$18M from double-spends on Bittrex and other exchanges.
- **Cross-exchange arbs.** Coinbase non-credit + Bittrex delay created multi-week 5-15% spreads.

## Who Lost Money?

- **Bitfinex BTG-IOU longs.** Bought at $300-400 expecting BCH-style outcome; lost 80-90%.
- **Coinbase customers** who didn't understand BTC withdrawal mechanics. Did not receive BTG.
- **BTG launch buyers** at $470. Lost 70%+ within 30 days.
- **Bittrex** customers and the exchange itself — ~$2.3M lost in May 2018 51% attack; delisting destroyed remaining customer holdings.
- **GPU miners who didn't pivot quickly.** BTG mining profitability collapsed within 2 weeks.
- **The BTG team.** The premine concerns and 51% attacks destroyed the project's credibility.

## Risks

1. **Premine controversy.** 100,000 BTG (~$50M at peak) held by the team raised "exit-scam" concerns. This is the canonical premine-risk fork case.
2. **51% attack risk on low-hashrate Equihash.** Realized in May 2018. Any small-PoW fork has this risk; BTG validated it.
3. **Exchange-credit asymmetry.** Coinbase non-credit cost customers; Bittrex delayed credit cost trust.
4. **Replay protection delay.** BTG launched with SIGHASH_FORK_ID but exchange implementation lagged. Some early withdrawals had [[replay-attack]] issues.
5. **Difficulty whiplash.** BTG's per-block DigiShield v3 made mining-profitability a moving target. GPU miners who didn't optimize promptly missed the window.
6. **Long-tail listing destruction.** Bittrex's 2018 delisting demonstrated that fork tokens can lose their primary venue, leaving holders stranded on smaller exchanges.

## Lessons for Fork Arbitrage

1. **Premine = exchange-listing risk.** Any fork with a non-trivial premine should be assumed to have delayed/blocked listings on Coinbase, Kraken, and other regulator-friendly exchanges. Adjust position size accordingly.
2. **Low-hashrate forks have 51% attack risk that materially affects long-term holdings.** Equihash/RandomX/Scrypt forks at <10% of their parent algorithm's network hashrate are vulnerable. Any such fork should have a "disaster pricing" element in pre-fork IOU shorts.
3. **Pre-fork IOU markets often over-price small forks.** Bitfinex BTG-IOU at $300-400 vs realistic $30-80. The pattern recurs (ETHW, BSV) — the reverse-IOU short is consistently the highest-Sharpe fork-arb trade for small fork events.
4. **Mining-difficulty arbitrage windows are 1-2 weeks for new forks.** GPU miners who pivot quickly capture massive APY; the window closes as difficulty adjusts and competition arrives. Speed matters.
5. **The BCH 2017 success does not generalize.** BTG, BSV, BCD, and most other 2017-2018 forks underperformed the BCH playbook. BCH worked because of community support + miner buy-in + immediate exchange listing — most other forks lacked all three.

## Aftermath

- **2017-2018:** BTG traded $50-300; volatile but on a multi-month decline.
- **May 2018:** First 51% attack; Bittrex delisting.
- **2019-2020:** Second 51% attack; BTG continues to exist with marginal mining and trading volume.
- **2021-2024:** BTG's market cap stays in the $50-200M range despite broader crypto bull markets. The chain remains operational but commercially insignificant.
- **Hashrate-rental risk:** BTG demonstrated that **NiceHash-style hashrate rental is a structural threat to small PoW chains**. This is a recurring concern for ETC, ZEC, RVN, and other small-hashrate chains.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2018-11-bitcoin-cash-sv-fork-arbitrage]] · [[2022-09-ethereum-merge-fork-arbitrage]] · [[replay-attack]] · [[failure-modes]]

## Sources

- Bitcoin Gold whitepaper / GitHub (Jack Liao et al., 2017).
- Bittrex: "Bitcoin Gold Wallet Status" updates (October 2017 - September 2018).
- *CoinDesk*: "Bitcoin Gold Hit by 51% Attack" (May 24, 2018).
- Coinbase blog: "On the Bitcoin Gold (BTG) Hard Fork" (October 2017).
