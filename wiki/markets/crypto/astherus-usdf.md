---
title: "Aster USDF"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["Astherus USDF", "USDF", "asUSDF"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.asterdex.com/en/usdf"
related: ["[[asterdex]]", "[[bnb]]", "[[crypto-markets]]", "[[delta-neutral]]", "[[ethena-usde]]", "[[stablecoins]]", "[[usde]]", "[[usdt]]"]
---

# Aster USDF

**Aster USDF** (ticker **USDF**) is a **yield-bearing dollar [[stablecoins|stablecoin]]** issued by **Aster** (formerly **Astherus**), a decentralized perpetual-futures exchange ([[asterdex|AsterDEX]]), primarily on **[[bnb|BNB Chain]]**. It targets a peg of **1 USDF ≈ US$1** and is convertible with **[[usdt|USDT]] at a 1:1 ratio**. Deposited USDT is deployed into **[[delta-neutral]]** positions that back USDF and generate funding/basis yield, which is distributed through the staked variant **asUSDF**. Mechanically it is the same synthetic-dollar family as [[ethena-usde|Ethena's USDe]] — a hedged, derivatives-funded dollar — but issued by and native to a perp DEX.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | USDF |
| **Price** | $0.997274 |
| **Peg target** | US$1.00 (1:1 with USDT) |
| **Market cap** | $114.54M |
| **Market-cap rank** | #245 |
| **24h volume** | $79,298 |
| **24h change** | -0.03% |
| **Circulating supply** | 114.85M USDF |
| **Total supply** | 114.85M USDF |
| **All-time high** | $1.046 (2025-10-10) |
| **All-time low** | $0.798494 (2025-10-10) |

USDF traded near peg at the snapshot (~$0.9973). Its ATH and ATL were both stamped on the same day (2025-10-10), reflecting an extreme intraday print to ~$0.80 — a sharp, brief de-peg early in its history. The broader tape on 2026-06-21 was Extreme Fear (Fear & Greed 21; [[bitcoin|BTC]] ~$64,568), a backdrop in which funding-rate-funded synthetic dollars warrant extra scrutiny.

> *Informational only, not investment advice. Synthetic / delta-neutral dollars carry funding-rate and venue risk and have de-pegged before.*

---

## Architecture — How It Works

USDF is a **yield-bearing synthetic stablecoin** backed by [[usdt|USDT]] deployed into hedged positions:

1. **Mint.** Users mint USDF by depositing USDT 1:1; they can convert back to USDT 1:1 through the Aster protocol.
2. **Hedge (the backing).** The deposited USDT funds are used to open and maintain **[[delta-neutral]]** positions — typically a long spot/collateral leg hedged with an offsetting **short perpetual-futures** position — so the *dollar value* of the backing stays roughly stable regardless of which way the market moves.
3. **Yield source.** The delta-neutral structure earns **funding-rate / basis income** from the short perpetual positions (plus any collateral yield). When perp funding is positive, shorts are paid — this is the engine. It is the same mechanism as [[ethena-usde|Ethena USDe]].
4. **Yield distribution.** **asUSDF** is the staked version: holders stake USDF into asUSDF to receive the accrued yield. Base USDF held in a wallet does **not** auto-accrue — yield is opt-in via staking, which keeps the base token a clean $1 unit.

**Redemption:** 1:1 convertibility back to USDT through the Aster protocol; secondary exit via on-chain liquidity.

Aster ([[asterdex|AsterDEX]]) is the perpetual-DEX issuer (MEV-aware trading, high-leverage "Simple Mode" and pro tools), backed by **YZi Labs** (formerly Binance Labs); USDF is its native collateral/savings dollar and a way to retain trader balances and earn the funding spread on idle margin.

---

## Tokenomics & Supply

USDF supply is **demand-driven and fully reserve-matched** in design: circulating supply equals total supply (114.85M) — every USDF is minted against $1 of deposited USDT, which is then hedged. There is no separate inflationary token; the value flow is the **funding spread** captured by the delta-neutral book, routed to **asUSDF** stakers. Net new USDF therefore tracks how much trader/depositor capital Aster can attract into the hedged dollar. The 1:1 circulating/total ratio is consistent with a mint-and-redeem reserve model rather than a pre-mined supply.

---

## Comparison vs Peer Synthetic / Yield Dollars

| Stablecoin | Backing / yield engine | Issuer | Yield delivery | Key risk |
|---|---|---|---|---|
| **USDF** (this page) | USDT → [[delta-neutral]] perp hedge; funding/basis | Aster ([[asterdex|AsterDEX]] perp DEX) | Stake → asUSDF | Funding-rate flip; venue/issuer concentration |
| **[[ethena-usde]] (USDe)** | Crypto collateral → delta-neutral perp hedge; funding | Ethena | Stake → sUSDe | Funding-rate flip; exchange/custody risk (larger, more battle-tested) |
| **[[usdt]] (Tether)** | Fiat + mixed reserves | Tether | None (no native yield) | Reserve transparency; centralization |
| **[[dai]] (DAI/USDS)** | Over-collateralized CDP (crypto + RWA) | Sky/Maker | sDAI savings rate | Collateral & governance |

USDF's closest analog is unambiguously **[[ethena-usde|USDe]]** — same delta-neutral funding-capture design — but USDF is smaller, newer, and tied to a single perp venue (Aster). USDe is the more liquid, more diversified incumbent of the category.

---

## How & Where It Trades / Is Used

USDF is concentrated in the **[[bnb|BNB Chain]] ecosystem and within Aster's own venue**; CoinGecko shows no major external centralized-exchange listings. Liquidity is on-chain plus 1:1 convertibility against USDT. Reported 24h volume of ~$79K against a ~$115M market cap is **low**, indicating USDF is held mostly as **Aster trading margin / yield collateral** rather than actively traded spot — i.e. it functions as the savings/margin dollar inside the Aster perp ecosystem.

Contract address:

| Chain | Address |
|---|---|
| BNB Chain | `0x5a110fc00474038f6c02e89c707d638602ea44b5` |

---

## Narrative, Category & Catalysts

- **Category:** yield-bearing synthetic / delta-neutral dollar — the [[ethena-usde|USDe]] playbook applied as a perp-DEX-native dollar.
- **Bull catalysts:** sustained positive perp funding (widens the yield); Aster/AsterDEX trading-volume growth pulling more capital into USDF margin; asUSDF yield attracting deposits; YZi Labs/Binance-ecosystem distribution.
- **Bear catalysts:** sustained **negative funding** (erodes yield and can stress backing); a perp-venue outage or insolvency breaking the hedge; thin liquidity amplifying any de-peg; competition from larger USDe.

---

## History / Timeline

| Date | Event |
|---|---|
| 2025-10-10 | All-time high **$1.046** *and* all-time low **$0.798494** stamped same day — a sharp, brief intraday de-peg to ~$0.80 early in USDF's history. |
| 2026-06-21 | Trades ~$0.997274, rank #245, ~$114.5M cap; near peg, thin volume (~$79K/24h). |

*The 2025-10-10 ~$0.80 print is a real, recorded severe de-peg event — the standout cautionary data point on this token.*

---

## Risks

- **De-peg risk:** USDF printed as low as ~$0.80 on 2025-10-10 — a demonstrated severe de-peg event. Thin secondary liquidity and the current Extreme-Fear regime (Fear & Greed 21) keep this risk live.
- **Funding-rate / yield-source risk:** the [[delta-neutral]] yield engine depends on positive perpetual funding; sustained negative funding erodes yield and can stress the backing — the classic synthetic-dollar failure mode shared with [[usde]].
- **Counterparty / venue risk:** the hedge relies on perpetual-futures venues; an exchange or Aster-platform failure threatens the backing.
- **Issuer / custodial risk:** USDF backing depends on Aster's management of the delta-neutral book and its 1:1 USDT reserves.
- **Redemption-gating risk:** par redemption runs through the Aster protocol; if that path is paused or congested, holders depend on thin secondary liquidity to exit.
- **Concentration risk:** supply, liquidity, and the hedge are all concentrated on one chain and one venue.
- **Regulatory risk:** derivatives-funded yield dollars issued by a perp DEX face evolving regulatory scrutiny.

---

## Trading / Usage Playbook

- **Use case:** USDF is best used *inside* Aster as yield-bearing margin — stake to asUSDF to capture the funding spread on idle collateral. As a standalone held dollar it offers little versus deeper stables.
- **What to watch:** perpetual funding rates (the yield engine — negative funding is the warning sign); the USDF secondary price vs $1 (de-peg signal given thin liquidity); Aster/AsterDEX platform health and volume; the USDT reserve/convertibility path.
- **Risk-off framing:** in Extreme Fear, perp funding can turn negative for extended stretches; that is exactly when synthetic-dollar yield compresses and de-peg risk rises. Treat USDF as a venue-specific yield product, not a safe-haven dollar, and prefer redeeming to USDT over selling into thin liquidity.

---

## Related

- [[ethena-usde]], [[usde]] — flagship delta-neutral synthetic dollar (closest analog)
- [[delta-neutral]] — the hedging mechanism
- [[asterdex]] — the issuing perp DEX (Aster / Astherus)
- [[usdt]] — the 1:1 backing/convertibility asset
- [[stablecoins]] — landscape overview
- [[usdc]], [[dai]] — peer dollars
- [[bnb]] — host chain
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description and USDF whitepaper from Aster ([https://docs.asterdex.com/product/usdf-stablecoin](https://docs.asterdex.com/product/usdf-stablecoin)). General market knowledge; no specific wiki source ingested yet beyond the CoinGecko snapshot.

## See Also

- [[crypto-markets]]
- [[bnb]]

---
