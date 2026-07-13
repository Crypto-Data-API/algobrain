---
title: "Unity USD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["UUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://uusd.ai/"
related: ["[[stablecoins]]", "[[crypto-markets]]", "[[bnb]]", "[[usdc]]", "[[ethena-usde]]"]
---

# Unity USD

**Unity USD** (ticker **UUSD**) is a USD-pegged synthetic-dollar [[stablecoins|stablecoin]] built by **Anything Labs** on [[bnb|BNB Chain]], positioned as the settlement currency for an "AI agent economy." It targets a **1:1 peg to the US dollar** and, as of the snapshot below, trades essentially on peg at ~$0.998. UUSD's pitch is narrative-led: a programmable dollar designed to be spent, settled, and streamed by autonomous AI agents transacting on-chain, rather than a fiat-custody coin competing head-on with [[usdc]] or [[usdt]].

## Market data

| Field | Value |
|---|---|
| **Ticker** | UUSD |
| **Price** | $0.9980 |
| **Market cap** | $99.80M |
| **Market-cap rank** | #271 |
| **24h volume** | $1.07M |
| **24h change** | -0.14% |
| **Circulating supply** | 100.00M UUSD |
| **Total supply** | 100.00M UUSD |
| **All-time high** | $1.023 (2026-03-23) |
| **All-time low** | $0.9831 (2026-06-01) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Architecture & how it works

UUSD is described by its issuer as a **synthetic dollar** (CoinGecko categorises it under "Synthetic Asset / Synthetic Dollar"), intended as a programmable medium of value for autonomous AI agents transacting on-chain. Conceptually it sits nearer to synthetic-dollar designs like [[ethena-usde]] than to fiat-custody coins like [[usdc]] — though the **precise collateral set and stabilisation mechanism are not fully documented** in the data available to this wiki, and should be treated as unverified.

- **Collateral / reserve model:** The issuer (Anything Labs) has **not surfaced a transparent reserve attestation** to this wiki. There is no published proof-of-reserves, audited collateral basket, or itemised backing schedule available here. Synthetic dollars in this class are typically backed by some mix of crypto collateral and/or stablecoin reserves, but for UUSD the composition is unknown.
- **Peg / stability mechanism:** The peg is held in practice (recent range $0.9961–$1.00 at the snapshot) but the *mechanism* — whether by arbitrage against a redeemable reserve, an algorithmic supply controller, or pooled liquidity incentives — is not clearly specified. Absent a documented mint/redeem arbitrage path at $1.00, peg stability rests on market-maker support and secondary liquidity.
- **Mint / redeem & gating:** No clearly specified, transparent mint/redeem process is documented here. Without a verifiable redemption-at-NAV path, holders cannot independently confirm that supply is fully backed.
- **Yield source & distribution:** UUSD is the **base dollar token** and is **not marketed as a native yield-bearing/rebasing instrument** in available data. There is no documented staked variant or savings wrapper.

The honest summary: UUSD's market behaviour (tight peg, $100M cap) is observable, but its *backing and stabilisation internals are opaque* relative to better-documented peers. This opacity is itself the central fact for risk assessment.

## Tokenomics & supply

Circulating and total supply are equal at **100.00M UUSD**, i.e. there is no locked or non-circulating overhang. The round-number supply and $100M cap suggest a single managed issuance rather than organic, demand-driven minting. With price on peg, market cap tracks supply 1:1. No emission schedule, governance token, or fee-capture mechanism is documented to this wiki.

## Comparison vs peers

| Token | Issuer | Backing model | Yield to holder | Transparency |
|---|---|---|---|---|
| **UUSD** | Anything Labs | Synthetic dollar (undisclosed) | No | Low — no public attestation |
| [[ethena-usde\|USDe]] | Ethena | Crypto collateral + [[delta-neutral]] short hedge | Via staked sUSDe | High — public reserves dashboard |
| [[usdc]] | Circle | Fiat reserves (T-bills, cash) | No (base) | High — monthly attestations |
| [[usdt]] | Tether | Fiat + mixed reserves | No | Medium — quarterly attestations |

UUSD is the least transparent of this set and the only one whose backing cannot be independently verified from data available here. Its differentiator is positioning (AI-agent settlement rail) rather than a novel, documented collateral design.

## How / where it trades & is used

UUSD is a [[bnb|BNB Chain]] token with reported 24h volume of **~$1.07M** against a $100M market cap — modest turnover for its size, implying most supply is held rather than actively traded. The CoinGecko snapshot does not surface deep, named centralised-exchange order books, so liquidity is likely concentrated in a small number of on-chain pools (DEX AMM pairs on BNB Chain). The tight recent range ($0.9961–$1.00) suggests adequate stabilisation to date, but thin venues mean a large order could move price; **confirm pool depth before sizing.** Intended use is as a settlement/medium-of-exchange token for AI-agent applications within the Anything Labs ecosystem; DeFi composability beyond that (lending markets, collateral acceptance) is not documented here.

## Narrative, category & catalysts

UUSD belongs to two overlapping 2026 narratives: **synthetic dollars** (yield/derivative-backed alternatives to fiat coins) and the **"AI agent economy"** (autonomous on-chain agents that need a programmable dollar to transact). Catalysts that would matter for UUSD: (1) publication of a transparent reserve attestation or audited backing, which would materially de-risk the token; (2) real adoption of AI-agent applications settling in UUSD; (3) listings on deeper venues to improve liquidity. Conversely, the token is highly exposed to the AI-agent narrative fading.

## History / timeline

- **2026-03-23** — All-time high of **$1.023** recorded (mild above-peg print).
- **2026-06-01** — All-time low of **$0.9831** recorded — a roughly **-1.7%** dip below peg, the only flagged de-peg episode in available data.
- **2026-06-21** — Snapshot: ~$0.998, on peg, $99.80M cap, rank #271.

The 2026-06-01 low is a real, dated minor de-peg; it coincided with broad crypto weakness but recovered to peg by the snapshot.

## Risks

- **De-peg risk:** Has dipped to $0.983 (2026-06-01); synthetic-dollar pegs depend on the integrity of the (undisclosed) backing and on arbitrage that requires a credible redemption path.
- **Collateral / backing transparency risk:** Reserve composition and stabilisation mechanism are **not transparently documented** — a material unknown and the single largest risk factor here. Holders cannot verify full backing.
- **Yield-source / counterparty risk:** Not applicable as a yield token, but any collateral deployment (if it exists) is undisclosed, so counterparty exposure is unknowable.
- **Redemption-gating risk:** No documented redeem-at-NAV path; exit may depend entirely on secondary liquidity.
- **Issuer / smart-contract risk:** Single-issuer (Anything Labs) model; very low recent developer activity (1 commit in the last 4 weeks per prior data) is a maintenance flag.
- **Narrative / demand risk:** Value proposition is tied to the speculative "AI agent economy" theme; demand could evaporate if the narrative fades.
- **Liquidity risk:** Modest volume and concentrated venues raise slippage and exit risk.
- **Regulatory risk:** Synthetic dollars face uncertain regulatory classification.

## Platform & chain

Native chain: [[bnb|BNB Chain]].

| Chain | Contract |
|---|---|
| BNB Chain | `0x61a10e8556bed032ea176330e7f17d6a12a10000` |

## Trading / usage playbook

- **Treat as opaque collateral.** With no public attestation, do not assume full backing; size positions as you would an unverified synthetic dollar, not a fiat coin.
- **Check pool depth before entry/exit.** Thin BNB Chain liquidity means slippage on size; the ~$1.07M daily volume will not absorb a large redemption-style exit cleanly.
- **Monitor the peg band.** A break below the 2026-06-01 ATL ($0.9831) without a fundamental catalyst would be an early stress signal.
- **Watch for a reserve disclosure.** Publication of audited backing is the key catalyst that would re-rate the token's risk profile.
- **Not a yield play.** UUSD pays nothing to holders; there is no staking/savings variant to capture.

## See also

- [[stablecoins]] — category overview
- [[ethena-usde]] — peer synthetic dollar
- [[usdc]], [[usdt]] — fiat-backed peers
- [[bnb]], [[crypto-markets]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.
