---
title: "Frax USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["FRXUSD", "Frax USD", "frxUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://frax.com"
related: ["[[crypto-markets]]", "[[dai]]", "[[ethereum]]", "[[frax]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]"]
---

# Frax USD

**Frax USD** (ticker **FRXUSD** / frxUSD) is a fiat-redeemable, fully-collateralized US-dollar stablecoin issued by the **Frax Finance** protocol, pegged 1:1 to USD. It launched as the redesigned, cash-equivalent-backed successor to Frax's earlier **partially-algorithmic FRAX** stablecoin, and is deployed natively across [[ethereum|Ethereum]], Fraxtal (Frax's own L2), and a broad set of L2 and alt-L1 chains (Arbitrum, Base, Optimism, Solana, BNB Chain, Polygon, and more).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | FRXUSD |
| **Price** | $1.000000 |
| **Market cap** | $115.8M |
| **Market-cap rank** | #241 |
| **24h volume** | $3.92M |
| **24h change** | +0.05% |
| **Circulating supply** | 115.83M FRXUSD |
| **Total supply** | 115.83M FRXUSD |
| **All-time high** | $1.007 |
| **All-time low** | $0.97622 |

Circulating supply equals total supply (market-cap / FDV ≈ 1.00), consistent with a fully-collateralized mint-and-redeem model.

---

## Architecture: Peg & Backing Mechanism

Frax USD is a **fiat-collateralized (cash-equivalent-backed) stablecoin** targeting a 1:1 USD peg. It is the product of Frax's pivot away from its historical **partial-algorithmic** design (where FRAX was backed by a mix of collateral and the FXS seigniorage token) toward **full collateralization** — a response to the broader 2022–2023 loss of confidence in algorithmic stablecoins after the Terra/UST collapse.

### Reserve / issuance model
- **Enshrined custodians** — Governance-approved custodians ("enshrined custodians") mint and redeem frxUSD against **off-chain reserves held in cash and cash-equivalents** (e.g. short-dated US Treasuries / tokenized T-bill exposure such as BlackRock BUIDL-style instruments, per Frax's public design). This off-chain reserve is the backbone of the 1:1 peg.
- **On-chain stability layer** — Frax pairs the off-chain reserve with on-chain mechanisms — **AMOs (Algorithmic Market Operations)** and protocol-controlled liquidity historically associated with the Frax ecosystem — to keep frxUSD usable, deeply liquid, and tightly pegged across DeFi without breaking full backing.
- **Redemption & gating** — frxUSD is **fiat-redeemable 1:1 via approved custodians**; this primary channel is permissioned (institutional/custodian onboarding), while secondary on-chain access is open. The tight historical band (ATH $1.007, ATL $0.97622) reflects an arbitrage-enforced peg.

frxUSD sits in the Frax stablecoin stack alongside the protocol's **yield-bearing variant (sfrxUSD)** — which passes reserve/T-bill yield to holders — and the [[frax|FRAX/FXS]] governance and utility token. No specific third-party reserve attestation is named in the source data.

---

## Tokenomics & Supply

frxUSD supply is **fully reserve-backed and elastic**: circulating equals total (market-cap/FDV ≈ 1.00), expanding when custodians mint against new reserves and contracting on redemption. There is no fixed max supply, no emissions, and — unlike the legacy FRAX — no algorithmic seigniorage backing the dollar itself. The Frax ecosystem's value-accrual and governance run through the [[frax|FRAX]] token and veFXS-style staking, while frxUSD is the neutral dollar unit and sfrxUSD is its yield-bearing wrapper. At ~$116M cap, frxUSD is a mid-small stablecoin but a core primitive within the Frax/Fraxtal economy.

---

## Comparison vs Competitor Stablecoins

| Stablecoin | Issuer | Backing | Peg type | Yield variant |
|---|---|---|---|---|
| **frxUSD** | Frax Finance | Off-chain cash + T-bills via custodians + on-chain AMOs | Hard (redeemable via custodians) | sfrxUSD |
| [[usdc\|USDC]] | Circle | Cash + T-bills | Hard (redeemable) | none (native) |
| [[dai\|DAI]] | MakerDAO/Sky | Crypto + RWA collateral (CDP) | Soft (CDP), PSM-assisted | sDAI |
| [[paypal-usd\|PYUSD]] | Paxos (PayPal) | Cash + T-bills | Hard (redeemable) | none |
| USDe (Ethena) | Ethena | Delta-hedged crypto (synthetic) | Soft (synthetic) | sUSDe |

frxUSD's distinguishing trait is its **hybrid model** — off-chain full collateralization plus on-chain AMO liquidity management and a deeply multi-chain footprint anchored to its own Fraxtal L2. Its weakness versus [[usdc|USDC]] is scale and the trust legacy of Frax's earlier algorithmic design.

---

## How & Where It Trades / Is Used

frxUSD is multi-chain by design, with contract deployments on Ethereum (`0xcacd6fd266af91b8aed52accc382b4e165586e29`), **Fraxtal** (Frax's own L2), and dozens of other networks. Liquidity is concentrated in **DeFi** — AMM pools (e.g. Curve-style stable pools and DEXs such as Orca on Solana) and lending markets — rather than centralized order books. Reported 24h volume is ~$3.92M against a ~$115.8M cap. Primary use cases are as a **DeFi unit of account, collateral, yield base (via sfrxUSD), and a bridge-friendly dollar** across the Frax/Fraxtal ecosystem.

---

## Narrative, Category & Catalysts

frxUSD sits in the **fully-collateralized DeFi-native dollar** category, with a distinctive **vertically-integrated ecosystem** angle (its own Fraxtal L2, AMO liquidity, and yield wrapper). Catalysts: growth of Fraxtal and the Frax ecosystem, adoption of sfrxUSD as a yield-bearing dollar, RWA/T-bill reserve expansion, and a regulatory environment that increasingly favors fully-reserved (vs algorithmic) stablecoins. Counter-trends: competition from much larger [[usdc|USDC]] and yield-bearing rivals (sDAI, sUSDe), liquidity fragmentation across chains, and lingering market memory of the legacy partial-algorithmic FRAX. In the current **Extreme Fear / bottoming-accumulation** regime (Fear & Greed 21), fully-collateralized dollars like frxUSD tend to be used as a **risk-off parking asset** within DeFi, with sfrxUSD offering yield on idle balances.

---

## History / Timeline

- **2020–2021** — Frax launches as the first **fractional-algorithmic** stablecoin (original FRAX), partly backed by collateral and partly by the FXS token's market value.
- **2022–2023** — Following the Terra/UST collapse and the broad repricing of algorithmic-stablecoin risk, Frax governance moves to **fully collateralize** the system.
- **2024–2025** — Frax introduces the redesigned dollar stack: **frxUSD** (fully-collateralized dollar) and **sfrxUSD** (yield-bearing), backed by cash and tokenized T-bill exposure via enshrined custodians, and deploys natively on **Fraxtal** and across many chains.
- **2026** — frxUSD trades at $1.000000 with a ~$116M cap (#241), supply fully backed (circulating = total).

*(Specific launch dates beyond the general phases above are not independently sourced in the market data block.)*

---

## Risks

- **De-peg risk** — historically tight (~$0.976–$1.007), but any stablecoin can wobble during liquidity crunches; cross-chain deployments add bridge/representation risk on non-native chains.
- **Issuer / custodial / reserve-counterparty risk** — reserves are held off-chain by governance-approved custodians; holders depend on the integrity and solvency of those custodians and on Frax governance.
- **Redemption-gating risk** — primary 1:1 redemption is permissioned (custodian onboarding); retail typically exits via secondary DeFi liquidity rather than direct redemption.
- **Smart-contract & governance risk** — the on-chain stability mechanisms (AMOs, protocol-controlled liquidity) and governance decisions can affect peg behavior; the legacy of Frax's earlier partial-algorithmic model is a reminder that the design has evolved under stress.
- **Regulatory risk** — fiat-backed stablecoins face evolving reserve-disclosure and licensing regimes (e.g. US/EU stablecoin frameworks).
- **Liquidity fragmentation** — supply spread across many chains can thin out depth on any single venue.

---

## Trading Playbook

- **Parking + yield** — hold frxUSD as a risk-off dollar; wrap into **sfrxUSD** to earn reserve/T-bill yield on idle balances in DeFi.
- **Peg reads** — treat the $0.976–$1.007 band as the historical envelope; only a sustained, widening discount tied to custodian/reserve doubt signals a genuine [[stablecoin|depeg]].
- **Chain awareness** — prefer native deployments (Ethereum/Fraxtal); on bridged chains, account for bridge/representation risk and thinner depth.
- **Ecosystem dependence** — frxUSD's utility is tightly tied to Fraxtal/Frax; weigh ecosystem health alongside reserve quality.

---

## Related

- [[stablecoin]] / [[stablecoins]] — category overview
- [[frax]] — Frax ecosystem governance/utility token
- [[usdc]] — fiat-backed peer
- [[dai]] — decentralized, crypto-overcollateralized peer
- [[gusd|GUSD]], [[agora-dollar|AUSD]] — other USD stablecoin peers
- [[ethereum]], [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FRXUSD |
| **Market Cap Rank** | #246 |
| **Market Cap** | $109.94M |
| **Current Price** | $0.9998 |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed Stablecoin |
| **Website** | [https://frax.com](https://frax.com) |

---

## Overview

Frax USD (frxUSD) is a fiat-redeemable, fully-collateralized stablecoin issued by the Frax Finance Protocol. It operates using a hybrid model where governance-approved enshrined custodians mint and redeem frxUSD backed by cash-equivalent reserves, while advanced onchain mechanisms developed by the Frax Finance Protocol ensure stability, security, and seamless usability across DeFi and traditional financial systems.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 109.96M FRXUSD |
| **Total Supply** | 109.96M FRXUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $109.94M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.01 (2025-05-30) |
| **Current vs ATH** | -0.70% |
| **All-Time Low** | $0.9762 (2025-02-17) |
| **Current vs ATL** | +2.38% |
| **24h Change** | +0.03% |
| **7d Change** | +0.04% |
| **30d Change** | +0.02% |
| **1y Change** | -0.09% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xcacd6fd266af91b8aed52accc382b4e165586e29` |
| Arbitrum One | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Plume Network | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Unichain | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Sonic | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Linea | `0xc7346783f5e645aa998b106ef9e7f499528673d8` |
| Fraxtal | `0xfc00000000000000000000000000000000000001` |
| Polygon Pos | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Sei V2 | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Binance Smart Chain | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Aurora | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Berachain | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Polygon Zkevm | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Ink | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Scroll | `0x397f939c3b91a74c321ea7129396492ba9cdce82` |
| Abstract | `0xea77c590bb36c43ef7139ce649cfbcfd6163170d` |
| Movement | `0xe067037681385b86d8344e6b7746023604c6ac90ddc997ba3c58396c258ad17b` |
| Mode | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| X Layer | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Solana | `GzX1ireZDU865FiMaKrdVB1H6AE8LAqWYCg6chrMrfBw` |
| Base | `0xe5020a6d073a794b6e7f05678707de47986fb0b6` |
| Blast | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Stable | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Optimistic Ethereum | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Aptos | `0xe067037681385b86d8344e6b7746023604c6ac90ddc997ba3c58396c258ad17b` |
| Zksync | `0xea77c590bb36c43ef7139ce649cfbcfd6163170d` |
| Avalanche | `0x80eede496655fb9047dd39d9f418d5483ed600df` |
| Katana | `0x80eede496655fb9047dd39d9f418d5483ed600df` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | GZX1IREZDU865FIMAKRDVB1H6AE8LAQWYCG6CHRMRFBW/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://frax.com](https://frax.com) |
| **Twitter** | [@fraxfinance](https://twitter.com/fraxfinance) |
| **Telegram** | [fraxfinance](https://t.me/fraxfinance) (13,555 members) |
| **Discord** | [https://discord.com/invite/fraxfinance](https://discord.com/invite/fraxfinance) |
| **GitHub** | [https://github.com/FraxFinance](https://github.com/FraxFinance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.12M |
| **Market Cap Rank** | #246 |
| **24h Range** | $0.9994 — $1.00 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
