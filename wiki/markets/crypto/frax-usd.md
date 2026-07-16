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

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
