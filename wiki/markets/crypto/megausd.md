---
title: "MegaUSD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["USDM", "USDm"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://megaeth.com/"
related: ["[[stablecoins]]", "[[ethena-usde]]", "[[usde]]", "[[megaeth]]", "[[crypto-markets]]"]
---

# MegaUSD

**MegaUSD** (ticker USDM, styled "USDm") is the native dollar stablecoin of the **MegaETH** blockchain. It targets a soft peg of **1 USDm ≈ US$1** and is **issued through Ethena's stablecoin stack** — i.e. it inherits the synthetic-dollar mechanism behind [[ethena-usde]] / [[usde]] rather than holding fiat reserves directly. USDm is designed to be the default settlement asset across wallets, apps, and on-chain services on [[megaeth]], the dollar rail for a chain marketing real-time (~10 ms) block times.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | USDM |
| **Price** | $0.999494 |
| **Peg target** | US$1.00 |
| **Market cap** | $221.09M |
| **Market-cap rank** | #166 |
| **24h volume** | $1.02M |
| **24h change** | +0.18% |
| **Circulating supply** | 221.37M USDM |
| **Total supply** | 221.37M USDM |
| **All-time high** | $1.047 (2026-06-14) |
| **All-time low** | $0.973885 (2026-06-14) |

At the snapshot USDm was holding its peg tightly (~$0.9995). Supply has grown sharply versus earlier in the year as MegaETH adoption expanded.

---

## Architecture & how it works

USDm is issued via **Ethena's** infrastructure, the same stack behind [[usde]] (USDe). The design is a **synthetic dollar**, not a fiat-custody coin.

- **Collateral / reserve model:** Ethena's design backs the token with crypto collateral (liquid staking assets and stablecoins) hedged by an offsetting **short perpetual-futures** position — a [[delta-neutral]] position — so the *dollar value* of the backing stays roughly constant regardless of the collateral's spot price. As a MegaETH-native deployment, USDm leans on this Ethena machinery rather than maintaining an independent reserve.
- **Peg / stability mechanism:** The peg is defended by the delta-neutral hedge (collateral gains/losses offset by the short) plus mint/redeem arbitrage through the Ethena stack. When USDm trades below $1, authorised parties can redeem against backing; when above, they can mint — this two-sided arbitrage is what tethers the secondary price to NAV.
- **Mint / redeem & gating:** Issuance and redemption are handled through the **Ethena issuance stack** and MegaETH integrations. Primary mint/redeem is typically permissioned (whitelisted minters); ordinary on-chain holders exit via **secondary liquidity** on MegaETH DEXs rather than redeeming directly.
- **Yield source & distribution:** In the Ethena model, yield comes from (1) **funding-rate / basis** income earned by the short perpetual-futures hedge and (2) **staking/yield** on the underlying collateral. Yield is typically passed to a **staked variant** (analogous to sUSDe) rather than to the base transactional token USDm — so simply holding USDm as a medium of exchange is not, by itself, yield-bearing. Ethena operates one of DeFi's largest synthetic-dollar systems (multi-billion-dollar TVL).

**MegaETH context:** MegaETH is marketed as a "real-time" Ethereum-secured chain targeting ~10 ms latency and up to 100,000 TPS with full EVM composability; USDm is the dollar rail for that high-throughput environment.

---

## Tokenomics & supply

Circulating and total supply are equal at **221.37M USDM** — no locked overhang. Supply expanded sharply through 2026 as MegaETH usage grew, which is consistent with a chain-native settlement dollar that is minted on demand as on-chain activity scales. With price on peg, market cap (~$221M, rank #166) tracks supply directly. There is no fixed max supply; issuance is elastic to demand via the Ethena mint path.

---

## Comparison vs peers

| Token | Issuer / chain | Backing model | Yield to base holder | Notes |
|---|---|---|---|---|
| **USDm** | Ethena stack / MegaETH | Crypto collateral + delta-neutral short hedge | No (yield via staked variant) | Chain-native settlement dollar |
| [[usde\|USDe]] | Ethena / multi-chain | Same delta-neutral synthetic-dollar model | No (sUSDe earns) | The flagship the USDm stack derives from |
| [[usdc]] | Circle / multi-chain | Fiat reserves (T-bills, cash) | No | Fiat-custody, attested |
| [[dai]] | MakerDAO/Sky | Crypto + RWA overcollateralised | No (sDAI earns) | Decentralised CDP model |

USDm's distinguishing feature versus USDe is *deployment context* — it is the default dollar of one specific high-performance chain — rather than a different backing mechanism. It inherits both the advantages (delta-neutral stability, derivative yield) and the failure modes (funding-rate dependence) of the Ethena design.

---

## How and where it trades & is used

USDm is native to MegaETH; CoinGecko shows no major centralized-exchange listings. Liquidity is concentrated in **MegaETH-native DEXs and apps**. Reported 24h volume of ~$1.02M against a ~$221M market cap is a low turnover ratio, typical of a young chain-native stablecoin used mainly for **in-ecosystem settlement** (payments, trading collateral, app balances) rather than cross-venue speculation. DeFi composability is concentrated within the MegaETH ecosystem.

Contract address:

| Chain | Address |
|---|---|
| MegaETH | `0xfafddbb3fc7688494971a79cc65dca3ef82079e7` |

---

## Narrative, category & catalysts

USDm sits at the intersection of two themes: **synthetic dollars** (Ethena-style, derivative-backed) and **new-L1 ecosystem dollars** (a stablecoin tightly coupled to one chain's growth). Catalysts: (1) MegaETH mainnet adoption and TPS delivery — more activity drives organic USDm demand; (2) a staked/savings variant launching to capture Ethena-style yield for holders; (3) external CEX/DEX listings to broaden liquidity. Key risk to the narrative is the funding-rate environment — Ethena-style yield depends on positive perpetual funding, which the current bearish backdrop pressures.

---

## History / timeline

- **2026 (H1)** — Supply grew sharply as MegaETH adoption expanded; rank climbed to #166.
- **2026-06-14** — Both the all-time high (**$1.047**) and all-time low (**$0.973885**) were recorded **on the same day** — a roughly ±2.5% intraday volatility spike around the peg. This is a real, dated single-day dislocation (likely a thin-liquidity event), not a sustained de-peg; price was back at ~$0.9995 by the 2026-06-21 snapshot.
- **2026-06-21** — Snapshot: ~$0.9995, on peg, $221.09M cap, rank #166.

---

## Risks

- **De-peg risk:** as an Ethena-style synthetic dollar, USDm is exposed to the same failure modes as [[usde]] — sustained **negative funding rates** can erode the backing yield, and sharp collateral drawdowns can stress the hedge. The current "Extreme Fear" backdrop (crypto Fear & Greed ~21, BTC ≈ $64,568) is the kind of environment where funding can turn negative. The 2026-06-14 intraday low ($0.9739) shows the peg can dislocate on thin liquidity.
- **Collateral / hedge risk:** reliance on perpetual-futures hedging introduces exchange counterparty risk and execution risk on the [[delta-neutral]] position.
- **Yield-source / counterparty risk:** the backing yield is derivative income from centralised perp venues; venue insolvency, socialised losses, or a prolonged negative-funding regime impair the model.
- **Redemption-gating risk:** primary redemption is permissioned through the Ethena stack; ordinary holders rely on MegaETH secondary liquidity, which can thin out under stress.
- **Issuer risk:** USDm inherits dependence on Ethena's issuance infrastructure and on MegaETH itself; problems at either layer propagate to the token.
- **Chain / smart-contract risk:** MegaETH is a new, high-throughput chain; concentration on a single nascent network adds liquidity and technical risk.
- **Regulatory risk:** synthetic dollars relying on derivatives income face evolving regulatory scrutiny.

---

## Trading / usage playbook

- **Use as a MegaETH settlement dollar**, not a yield instrument — base USDm pays nothing; look for a staked variant if it launches.
- **Watch funding rates.** Prolonged negative perpetual funding is the canonical stress signal for any Ethena-style dollar; it erodes backing yield and can pressure the peg.
- **Mind thin liquidity.** The 2026-06-14 single-day ±2.5% swing shows the peg can gap on low volume; size exits to available DEX depth on MegaETH.
- **Bridge/venue caution.** With liquidity concentrated on one young chain, plan exit routes (DEX depth, bridges) before sizing in.

---

## Related

- [[ethena-usde]], [[usde]] — the issuing synthetic-dollar protocol and its flagship token
- [[ethena]] — issuer
- [[delta-neutral]] — the hedging mechanism
- [[stablecoins]] — landscape overview
- [[megaeth]] — host chain
- [[usdc]], [[usdt]], [[dai]] — peer dollars
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description from MegaETH ([https://megaeth.com/](https://megaeth.com/)) and Ethena stack documentation. General market knowledge; no specific wiki source ingested yet for the MegaETH/Ethena issuance details.
