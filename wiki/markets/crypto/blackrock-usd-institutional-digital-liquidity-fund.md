---
title: "BlackRock USD Institutional Digital Liquidity Fund"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, ethereum, regulation]
aliases: ["BUIDL", "BlackRock BUIDL"]
entity_type: protocol
founded: 2024
headquarters: "New York, USA (BlackRock); tokenized via Securitize"
website: "https://securitize.io/blackrock/buidl"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[blackrock]]", "[[securitize]]", "[[hashnote-usyc]]", "[[tokenized-treasuries]]", "[[real-world-assets]]", "[[ousg]]", "[[treasury-bills]]"]
---

# BlackRock USD Institutional Digital Liquidity Fund

**BlackRock USD Institutional Digital Liquidity Fund** (BUIDL) is [[blackrock|BlackRock's]] tokenized money market fund, launched March 2024 on [[ethereum]] with [[securitize|Securitize]] as transfer agent and tokenization platform. It holds cash, U.S. [[treasury-bills|Treasury bills]] and repo, pays a daily-accrued dividend in new tokens, and maintains a $1.00 NAV. BUIDL was the flagship [[tokenized-treasuries|tokenized-Treasury]] product that legitimized the [[real-world-assets|RWA]] sector — the largest such fund through most of 2024–2025 (~$2.9B peak) — before being overtaken by [[hashnote-usyc|Circle's USYC]] in early 2026, largely because USYC offered more frictionless use as derivatives collateral.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $1.00 (flat NAV; dividends paid as new tokens) |
| **Market cap (= AUM on-chain)** | $2.384B |
| **Market-cap rank** | #40 |
| **24h volume** | $0 (permissioned; no secondary market) |
| **24h / 7d change** | 0.00% / 0.00% (price is constant by design) |
| **Circulating / total supply** | 2.384B BUIDL |
| **Max supply** | None (mints with subscriptions) |
| **All-time high / low** | $1.00 / $1.00 (stable-NAV token) |

For a flat-NAV fund the only meaningful market figure is **supply ≈ AUM**: ~$2.38B at this snapshot, up from the prior ~$1.7B reporting low — i.e. BUIDL has reaccumulated assets even after losing the #1 tokenized-Treasury spot to [[hashnote-usyc|USYC]]. On-chain price/volume are uninformative here because the token never trades secondary; flows happen through [[securitize|Securitize]] subscription/redemption. Macro backdrop: "Established Bear Market", Fear & Greed ~23 — a regime in which institutional cash parking in tokenized T-bills tends to be resilient.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BUIDL |
| **Type** | Tokenized money market fund (RWA / tokenized T-bills); stable $1.00 NAV, dividends paid as new tokens |
| **AUM** | ~$2.38B (on-chain supply, June 2026 CoinGecko snapshot, rank #40); Securitize platform ~$2.5B across 4 RWA products (RWA.xyz, 2026-06-09). Prior trough ~$1.7B per Jan 2026 reports |
| **Sector** | Tokenized U.S. Treasury market totals ~$14.8B (June 2026); BUIDL is #2 behind USYC (~$2.9B) |
| **Manager / Platform** | BlackRock (manager), Securitize (tokenization + transfer agent), BNY Mellon (custody/admin) |
| **Chains** | Ethereum (native) + BNB Chain, Solana, Avalanche, Arbitrum, Optimism, Aptos, Polygon |
| **Minimum** | Institutional / qualified purchasers via Securitize (initially $5M minimum) |
| **Categories** | Real World Assets (RWA), Tokenized Treasuries, multi-chain |
| **Website** | [https://securitize.io/blackrock/buidl](https://securitize.io/blackrock/buidl) |

---

## Overview

BUIDL invests 100% of assets in cash, U.S. Treasury bills, and repurchase agreements. Unlike NAV-accrual tokens (USYC, USDY), BUIDL keeps a **flat $1.00 price** and distributes yield as a monthly dividend airdrop of new tokens accrued daily — which is why its on-chain "price history" is a flat line and secondary-market volume is near zero. Subscription/redemption runs through Securitize, with a USDC instant-redemption facility provided by Circle.

### Timeline & 2025–2026 developments

- **2024-03** — Launch on Ethereum; within weeks BUIDL became the largest tokenized Treasury fund, validating the RWA thesis (and was itself seeded into protocols like Ondo's OUSG as underlying).
- **2024–2025** — Expanded to seven additional chains (Solana, Avalanche, Aptos, Arbitrum, Optimism, Polygon, BNB Chain); AUM peaked around **$2.88B in 2025** (AMINA Bank ranking).
- **Collateral adoption** — BUIDL accepted as off-exchange/derivatives collateral via custodians and prime brokers (Crypto.com and Deribit announced acceptance in 2024–2025), part of the broader trend of yield-bearing margin.
- **2026-01** — **Lost the #1 spot to Circle's USYC** (~$1.68B vs $1.69B on Jan 22, 2026, then diverging): commentary attributed the flip to a mechanical advantage — USYC's instant, permissionless-feeling mint/redeem loop against USDC suits high-velocity exchange collateral better than BUIDL's institutional subscription flow.
- **2026-06** — Tokenized Treasury market at **$14.79B distributed value** (RWA.xyz, 2026-06-09); Securitize platform total ~$2.5B.

---

## Mechanism & Backing

| Dimension | BUIDL design |
|---|---|
| **Underlying assets** | 100% cash, short-dated U.S. [[treasury-bills|Treasury bills]], and overnight repo — a tokenized money-market fund, not a fractional-reserve stablecoin |
| **Wrapper** | A BVI/Securitize-administered fund; tokens are **securities**, sold only to qualified purchasers under Reg D / Reg S exemptions |
| **Yield source / NAV** | Income from the T-bill/repo book accrues daily; rather than letting NAV drift, BUIDL **distributes yield monthly as new tokens** ("rebasing-by-airdrop"), holding a flat $1.00 unit price. Net yield to holders tracks short [[treasury-bills|T-bill]] rates minus fund fees (qualitative — see fund docs for current rate) |
| **Custody / admin** | BlackRock is the manager; [[securitize|Securitize]] is tokenization agent and transfer agent; BNY Mellon provides custody and fund administration; PwC audits |
| **Redemption** | Subscriptions/redemptions at $1.00 NAV via Securitize; **Circle operates a USDC instant-redemption smart contract** giving near-real-time off-ramp to USDC |
| **KYC / permissioning** | Transfers restricted to whitelisted, Securitize-KYC'd wallets; an on-chain allowlist enforces this at the token-contract level. Not holdable by retail or anonymous wallets |
| **Min investment** | Institutional ($5M initial minimum at launch) |

Because the token is a permissioned security with a smart-contract allowlist, it cannot circulate freely on DEXs — its "liquidity" is the subscription/redemption pipe plus the Circle USDC facility, not an order book. This is the standard architecture across institutional [[tokenized-treasuries]] (BUIDL, [[ousg|OUSG]], BENJI, [[hashnote-usyc|USYC]]).

---

## Trading Relevance

- **Not directly tradable** — permissioned, KYC'd institutional token with ~zero secondary volume. Its importance to traders is as a **sector barometer and narrative driver**.
- **RWA narrative anchor**: BUIDL's launch (March 2024) ignited the RWA basket ([[narrative-trading]]) — ONDO, plus tokenization-adjacent names, repriced on every BlackRock tokenization headline. BlackRock CEO Larry Fink's "tokenization of all assets" statements remain a recurring catalyst for the basket.
- **Flow signal**: BUIDL AUM growth = institutional cash parking on-chain; contractions can signal redemptions toward T-bill alternatives or risk-on rotation into crypto proper.
- **Competitive watch**: the BUIDL vs USYC race is the cleanest read on whether tokenized collateral standardizes around BlackRock/Securitize or Circle rails — relevant to COIN/CRCL equities and the USDC ecosystem.

---

## Peer Comparison — institutional tokenized Treasury funds

| Fund | Issuer / platform | Underlying | NAV model | Permissioning | Approx. size |
|---|---|---|---|---|---|
| **BUIDL** | BlackRock / [[securitize|Securitize]] | T-bills, cash, repo | Flat $1.00, yield as new tokens | Qualified purchasers, allowlist | ~$2.38B (#40) |
| [[hashnote-usyc|USYC]] | Circle (ex-Hashnote) | T-bills / reverse repo | NAV-accrual (price drifts up) | Permissioned | ~$2.9B (#1) |
| [[ousg|OUSG]] | Ondo Finance | Holds BUIDL/MMFs underneath | NAV-accrual | Permissioned | Large |
| BENJI | Franklin Templeton | Govt MMF | $1.00, on-ledger shares | Registered '40-Act fund | Large |
| [[janus-henderson-anemoy-treasury-fund|JTRSY]] | Anemoy / [[centrifuge|Centrifuge]] | 0–3m T-bills | NAV-accrual | Pro investors | ~$0.87B (#75) |

BUIDL's distinguishing features are the BlackRock brand, BNY Mellon custody, multi-chain reach (8 chains), and the Circle USDC instant-redemption rail. Its disadvantage vs [[hashnote-usyc|USYC]] is that the flat-NAV + monthly-airdrop design is clunkier as high-velocity derivatives collateral than a continuously accruing NAV token.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x7712c34205737192402172409a8f7ccef8aa2aec` |
| Binance Smart Chain | `0x2d5bdc96d9c8aabbdb38c9a27398513e7e5ef84f` |
| Solana | `GyWgeqpy5GueU2YbkE8xqUeVEokCMMCEeUrfbtMw6phr` |
| Avalanche | `0x53fc82f14f009009b440a706e31c9021e1196a2f` |
| Arbitrum One | `0xa6525ae43edcd03dc08e775774dcabd3bb925872` |
| Optimistic Ethereum | `0xa1cdab15bba75a80df4089cafba013e376957cf5` |
| Aptos | `0x50038be55be5b964cfa32cf128b5cf05f123959f286b4cc02b86cafd48945f89` |
| Polygon PoS | `0x2893ef551b6dd69f661ac00f11d93e5dc5dc0e99` |

---

## Exchange Listings

None — BUIDL is a permissioned security token; transfers restricted to whitelisted Securitize-KYC'd wallets. Liquidity is via Securitize subscription/redemption and Circle's USDC redemption facility.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Fund page** | [https://securitize.io/blackrock/buidl](https://securitize.io/blackrock/buidl) |
| **Twitter** | [@BlackRock](https://twitter.com/BlackRock) |

---

## Risks

| Risk | Assessment |
|---|---|
| **Issuer / manager** | Low — BlackRock (manager) + BNY Mellon (custody) + PwC (audit) is about as strong a TradFi stack as exists in crypto |
| **Underlying credit / duration** | Low — short U.S. T-bills and repo; minimal duration and effectively sovereign credit |
| **Smart-contract / custody** | Moderate — allowlist contract, multi-chain bridges, and the Circle USDC redemption contract are code that can fail or be exploited; cross-chain deployments widen the surface |
| **Regulatory** | Moderate — a tokenized security; treatment of tokenized MMFs as collateral and across jurisdictions is still evolving |
| **Liquidity / redemption** | Moderate — par redemption depends on T-bill market liquidity and the Securitize/Circle pipes; instant USDC redemption is capped by the facility's available USDC |
| **De-peg** | Low for the NAV itself, but the USDC redemption leg inherits any [[usdc|USDC]] de-peg risk |
| **Competitive / flow** | Real — already lost the #1 spot to [[hashnote-usyc|USYC]]; AUM is sensitive to collateral-standard winner-take-most dynamics |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[blackrock]] — manager (also issuer of IBIT/ETHA ETFs)
- [[securitize]] — tokenization + transfer agent
- [[hashnote-usyc]] — the competitor that overtook it
- [[ousg]] — Ondo fund that holds BUIDL as underlying
- [[janus-henderson-anemoy-treasury-fund]] — peer tokenized-Treasury fund
- [[tokenized-treasuries]], [[real-world-assets]], [[treasury-bills]]
- [[tether-gold]] — fellow RWA token
- [[circle]] / [[usdc]]
- [[narrative-trading]] — RWA basket

---

## Sources

- Securitize, BlackRock BUIDL fund page — https://securitize.io/blackrock/buidl
- RWA.xyz tokenized Treasuries dashboard (snapshot 2026-06-09) — https://app.rwa.xyz/treasuries
- CryptoSlate, "BlackRock just lost control of the $10B tokenized treasury market to Circle" (Jan 2026) — https://cryptoslate.com/blackrock-just-lost-control-of-the-10b-tokenized-treasury-market-to-circle-for-one-simple-mechanical-reason/
- AMINA Bank, "Top 10 tokenization platforms of 2025" — https://aminagroup.com/research/top-10-tokenization-platforms-of-2025/
- Arkham Research, "Total value of tokenized U.S. Treasuries now more than $10B" — https://info.arkm.com/research/the-total-value-of-tokenized-u-s-treasuries-is-now-more-than-10b
- CoinGecko top-1000 snapshot (2026-04-09), original auto-generated data
- Verified via Perplexity sonar, 2026-06-10
