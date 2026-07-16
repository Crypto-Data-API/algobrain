---
title: "apxUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["APXUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://apyx.fi"
related: ["[[base]]", "[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[stablecoins]]"]
---

# apxUSD

**apxUSD** (ticker APXUSD) is a synthetic, dividend-backed dollar token issued by the **Apyx** protocol on **[[ethereum|Ethereum]]** (with a deployment on **[[base|Base]]**). It targets a soft peg of **1 apxUSD ≈ US$1**. Unlike fiat-reserve [[stablecoins]] such as [[usdc]] or [[usdt]], apxUSD is collateralized by **preferred equity issued by Digital Asset Treasuries (DATs)** — publicly listed companies that hold crypto on their balance sheets and pay monthly cash dividends on preferred shares. It is, in effect, a [[real-world-assets|RWA]] dollar backed by corporate preferred stock rather than Treasuries.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | APXUSD |
| **Price** | $0.890209 |
| **Peg target** | US$1.00 |
| **Market cap** | $355.61M |
| **Market-cap rank** | #125 |
| **24h volume** | $2.14M |
| **24h change** | +0.65% |
| **Circulating supply** | 399.47M APXUSD |
| **Total supply** | 399.47M APXUSD |
| **All-time high** | $1.11 (2026-03-23) |
| **All-time low** | $0.824964 (2026-06-18) |

Note: at the snapshot price of ~$0.89 apxUSD was trading meaningfully **below peg**, and its all-time low was set just days earlier on 2026-06-18 — a notable de-peg episode for a token marketed as a stable dollar (see [[stablecoins]] and the macro backdrop below).

---

## Architecture & how it works

Apyx describes itself as the first **dividend-backed stablecoin** protocol. The model uses **two tokens**:

- **apxUSD** — the synthetic dollar. It is claimed to be backed by **over 100% collateral in DAT preferred shares** and is designed for liquidity across DeFi and CeFi. apxUSD itself does **not** pay yield directly.
- **apyUSD** — an **ERC-4626 vault token**. Holders lock apxUSD to receive apyUSD, which accrues the dividend yield from the underlying preferred-share cash flows; apyUSD rises in value relative to apxUSD over time (an accruing savings wrapper).

**Collateral / reserve model:** Backing is **off-chain corporate preferred equity** issued by DAT companies — publicly listed firms holding crypto (e.g. SOL, BTC, ETH) on their balance sheets that pay monthly cash dividends on preferred shares. This is an [[real-world-assets|RWA]]-style design, but using *dividend-paying preferred stock* rather than the short-term Treasuries that RWA peers (e.g. tokenized T-bill funds) rely on. DeFi Development Corp. (Nasdaq: DFDV), a SOL treasury company, is cited as a core strategic partner.

**Peg / stability mechanism:** The peg is meant to be held by **over-100% collateralization** plus mint/redeem arbitrage against the DAT collateral basket. In practice the peg failed to hold at the snapshot (~$0.89), indicating that the redemption/arbitrage path was insufficient — or too slow/gated — to pull the secondary price back to $1 under stress.

**Yield source & distribution:** **Monthly cash dividends** paid by DAT issuers on their preferred equity. Apyx holds these dividend-paying shares as collateral and converts the cash flows into on-chain yield distributed to **apyUSD** holders (not apxUSD holders).

**Risk controls (per the protocol):** daily NAV reporting, auto-rebalancing on issuer-concentration and liquidity thresholds, stress testing across drawdown and rate-shock scenarios, and a protocol-owned liquidity buffer acting as extra overcollateralization.

**Redemption / minting:** mint/redeem flows run through the Apyx protocol against the DAT collateral basket; secondary exit is via on-chain liquidity (below). Redemption involves real-world securities, so it is operationally slower and more gated than a crypto-collateral or fiat coin.

---

## Tokenomics & supply

Circulating and total supply are equal at **399.47M APXUSD** — no locked overhang. Because backing is dividend-paying preferred equity, the protocol's effective collateral value is sensitive to DAT share prices and dividend continuity rather than to a static reserve. At the snapshot the ~$0.89 market price implied an ~11% discount to peg, i.e. the market was pricing in a backing or redemption discount versus the claimed >100% collateralization. The separate **apyUSD** vault token captures the dividend yield; apxUSD is the transactional/liquidity leg.

---

## Comparison vs peers

| Token | Issuer | Backing | Yield to holder | Peg at snapshot |
|---|---|---|---|---|
| **apxUSD** | Apyx | DAT preferred equity (dividends) | Via apyUSD vault | **~$0.89 (below peg)** |
| [[usdc]] | Circle | Fiat reserves (T-bills, cash) | No | On peg |
| [[dai]] | MakerDAO/Sky | Crypto + RWA overcollateralised | Via sDAI | On peg |
| [[ethena-usde\|USDe]] | Ethena | Crypto + delta-neutral hedge | Via sUSDe | On peg |

apxUSD is unique here in using **corporate preferred stock** as collateral — higher headline yield potential but materially more concentrated and credit-sensitive than Treasuries, crypto-overcollateral, or delta-neutral models. The below-peg print at the snapshot underscores that this exotic collateral carries real de-peg risk the fiat/crypto peers did not exhibit.

---

## How and where it trades & is used

apxUSD is an on-chain token; CoinGecko shows no major centralized-exchange listings. Liquidity is primarily **DEX-based on Ethereum and Base**. Reported 24h volume of ~$2.14M against a ~$356M market cap implies a **low turnover ratio**, so large redemptions or exits may move the price — consistent with the below-peg print at the snapshot. Composability is as a DeFi dollar (collateral/LP), but the persistent discount makes it a less reliable unit of account than peg-holding peers.

Contract addresses:

| Chain | Address |
|---|---|
| Ethereum | `0x98a878b1cd98131b271883b390f68d2c90674665` |
| Base | `0xd993935e13851dd7517af10687ec7e5022127228` |

---

## Narrative, category & catalysts

apxUSD rides the **DAT (Digital Asset Treasury)** and **RWA-yield** narratives — channelling the dividend cash flows of crypto-treasury companies into an on-chain dollar. Catalysts: (1) restoration of peg via demonstrated, smooth redemption at NAV; (2) DAT partners maintaining dividend payments and share value; (3) deeper liquidity/listings. The principal narrative risk is the inverse — the entire model depends on DAT solvency and dividend continuity, which are themselves leveraged to crypto prices in a bear regime.

---

## History / timeline

- **2026-03-23** — All-time high of **$1.11** (well above peg, likely a thin-market premium during launch).
- **2026-06-18** — All-time low of **$0.824964** recorded — an ~17.5% de-peg, a major, recent loss of peg for a token marketed as a stable dollar.
- **2026-06-21** — Snapshot: ~$0.89 (still ~11% below peg), $355.61M cap, rank #125.

The 2026-06-18 ATL and the still-discounted 2026-06-21 print together represent a **demonstrated, sustained de-peg**, not a fleeting wick — the key historical fact for this token.

---

## Risks

- **De-peg risk:** apxUSD traded near $0.89 at the snapshot with an ATL of $0.825 set on 2026-06-18 — a **demonstrated, recent and sustained loss of peg.** The current "Extreme Fear" backdrop (crypto Fear & Greed ~21) amplifies stress on thinly traded synthetic dollars.
- **Collateral risk:** backing is **DAT preferred equity**, an unusual and concentrated collateral type whose value depends on the issuers' digital-asset holdings, dividend continuity, and solvency. Dividend suspensions or DAT share drawdowns directly impair backing — and DAT firms are themselves levered to crypto prices.
- **Yield-source / counterparty risk:** yield rests entirely on monthly dividends from a small set of DAT issuers; a single issuer cutting or suspending its preferred dividend impairs both yield (apyUSD) and effective backing.
- **Redemption-gating risk:** redemption runs against real-world securities through the protocol; it is slower and more gated than crypto/fiat redemption, which is consistent with the peg failing to self-correct quickly.
- **Issuer / custodial risk:** the model relies on off-chain holding of preferred shares and on Apyx's NAV reporting; users must trust the protocol's accounting and custody of real-world securities.
- **Liquidity risk:** thin secondary liquidity makes orderly redemption difficult under stress.
- **Regulatory risk:** a token backed by dividend-paying preferred equity may raise securities-law questions in multiple jurisdictions.

---

## Trading / usage playbook

- **Do not treat as a $1 unit of account.** At the snapshot it traded ~11% below peg; mark positions to *market*, not to $1.
- **Discount-to-NAV is the key metric.** If the protocol's claimed >100% collateral is real and redemption works, the discount is a potential arb — but only if you can actually redeem at NAV; verify the redemption path and any gating first.
- **Track DAT partners.** Dividend continuity and share prices of DAT issuers (e.g. DFDV) are the leading indicators of backing health.
- **Yield lives in apyUSD, not apxUSD.** To earn the dividend yield you must lock into the apyUSD vault; bare apxUSD pays nothing and carries the de-peg risk.
- **Size for illiquidity.** ~$2.14M daily volume cannot absorb a large exit without moving price further from peg.

---

## Related

- [[stablecoins]] — overview of the stablecoin landscape
- [[real-world-assets]] — RWA / yield-bearing dollar context
- [[usdc]], [[usdt]], [[dai]] — fiat-reserve and crypto-collateralized peers
- [[ethena-usde]], [[usde]] — synthetic-dollar peers
- [[ethereum]], [[base]] — host chains
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description from Apyx ([https://apyx.fi](https://apyx.fi)). General market knowledge; no specific wiki source ingested yet for the dividend-backed mechanism.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
