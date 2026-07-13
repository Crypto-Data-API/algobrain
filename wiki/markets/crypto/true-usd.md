---
title: "TrueUSD"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, regulation, stablecoin]
aliases: ["TUSD", "TrueCoin"]
entity_type: protocol
founded: 2018
headquarters: "Issuer: Techteryx Ltd. (BVI); originally TrustToken/TrueCoin, San Francisco"
website: "https://tusd.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoins]]", "[[stablecoin]]", "[[usdc]]", "[[usdt]]", "[[first-digital-usd]]", "[[stablecoin-depegs]]", "[[real-world-assets]]"]
---

# TrueUSD

**TrueUSD** (TUSD) is a USD-pegged fiat-backed [[stablecoin]] launched in March 2018 by TrustToken (TrueCoin LLC) and sold to the offshore entity **Techteryx** in December 2020, issued primarily on [[ethereum|Ethereum]] and Tron. Once a top-3 stablecoin by Binance volume, TUSD is now primarily a **counterparty-risk case study**: an SEC fraud settlement (2024), a ~$456M reserve shortfall quietly bailed out by Justin Sun (revealed 2025), and ongoing litigation against its Hong Kong trustee First Digital Trust make it one of the most-watched depeg/blowup candidates among traders. See [[stablecoin-depegs]].

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $0.9976 (≈24bp below peg) |
| **Market cap** | $493.1M |
| **Market-cap rank** | #105 |
| **24h volume** | $17.27M |
| **24h change** | −0.05% |
| **7d change** | −0.16% |
| **Circulating / total supply** | 494.52M TUSD |
| **Max supply** | None (mint/burn on demand) |
| **All-time high** | $1.62 (2018-08-26, early illiquidity) |
| **All-time low** | $0.8835 (2020-03-12, COVID crash) |

The ~24bp discount to $1.00 at this snapshot is notable for a fiat-backed stablecoin and consistent with TUSD's status as a depeg-watch candidate; the broader market sat at an "Established Bear Market" with a Fear & Greed reading near 23.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TUSD |
| **Sector** | Fiat-backed USD stablecoin |
| **Rank tier** | #105 (~$493M cap / ~494.5M circulating supply, June 2026 snapshot) |
| **Genesis** | 2018-03-05 |
| **Issuer** | Techteryx Ltd. (acquired TUSD operations from TrueCoin, Dec 2020) |
| **Chains** | Ethereum, Tron, BNB Chain, Avalanche + others (12 chains claimed) |
| **Peg mechanics** | 1:1 USD claim; Chainlink Proof-of-Reserve attestations |
| **Website** | [https://tusd.io/](https://tusd.io/) |

---

## Overview

TUSD was the first USD stablecoin with live on-chain attestations by an independent accounting firm and the first to integrate Chainlink Proof of Reserve for minting. It has been listed on 100+ trading venues and is live on 12 chains including Ethereum, TRON, Avalanche, and BSC. The Commonwealth of Dominica granted TUSD statutory status as an authorized digital currency on October 7, 2022. In 2023 Binance briefly made TUSD its flagship zero-fee BTC pair, pushing volumes to the top of the stablecoin league tables before that role passed to [[first-digital-usd|FDUSD]].

---

## Mechanism & Backing

| Dimension | TUSD design (and where it broke) |
|---|---|
| **Peg target** | 1:1 USD; mint/redeem at par against fiat with whitelisted partners |
| **Reserves (claimed)** | Cash and cash-equivalents held in escrow accounts via third-party trustees |
| **Reserves (actual, per litigation)** | By Sept 2024 the SEC alleged **~99% of reserves were in a speculative offshore fund**; ~$456M later found routed via trustee First Digital Trust into Aria Commodities DMCC, a Dubai trade-finance firm — i.e. illiquid, not 1:1 cash |
| **Attestation** | Chainlink Proof-of-Reserve feed for minting; independent accounting attestations historically marketed as a differentiator. The reserve scandal shows attestation/PoR can lag or fail to capture custody-layer misappropriation |
| **Redemption** | Par redemption to whitelisted users; peg has held since 2024 **only because of Justin Sun's ~$500M loan**, not because reserves were liquid |
| **Custody / trustee** | First Digital Trust (Hong Kong) — now the defendant in Techteryx/Sun litigation |
| **Regulatory wrapper** | Authorized digital currency in the Commonwealth of Dominica (2022); not a US-registered security. Operated by an offshore BVI issuer |

**De-peg mechanics:** unlike NAV-accrual [[tokenized-treasuries]], TUSD has no yield buffer — its peg depends purely on reserve liquidity and redeemability. The episode is a textbook illustration that "attested 1:1" does not equal "redeemable 1:1" when custody is captured. See [[real-world-assets]] and [[stablecoin-depegs]].

---

## Major News & Events

- **Sep 24, 2024 — SEC fraud settlement.** The SEC charged TrueCoin LLC and TrustToken with fraudulent and unregistered sales of investment contracts tied to TUSD. The complaint alleged that by March 2022 more than half a billion dollars of TUSD reserves had been put into a speculative offshore fund, and that **by September 2024 99% of TUSD reserves were invested in that fund** while the companies kept marketing the coin as 1:1 dollar-backed. TrueCoin and TrustToken settled without admitting or denying, paying **$163,766 each** in civil penalties plus $340,930 disgorgement (TrueCoin). (Source: SEC press release 2024-145)
- **Apr 2025 — Justin Sun bailout revealed.** Hong Kong court filings showed that ~**$456M of TUSD reserves** had been routed — via trustee **First Digital Trust (FDT)** — into **Aria Commodities DMCC**, a Dubai trade-finance firm controlled by Matthew Brittain, leaving reserves illiquid. **Justin Sun lent Techteryx ~$500M** to keep redemptions whole. Sun's public accusations that FDT was "insolvent" triggered a ~9% depeg of FDT's own stablecoin [[first-digital-usd|FDUSD]] in April 2025. (Sources: CoinDesk, The Block)
- **Oct 17, 2025 — Dubai worldwide freezing order.** Dubai's Digital Economy Court (Justice Michael Black KC) upheld a worldwide freezing order over the **$456M** linked to Aria, finding Techteryx had shown "serious issues to be tried" and a credible constructive-trust claim, pending Hong Kong proceedings. (Source: CoinDesk, Nov 2025)
- **Nov 2025 — Sun escalates.** Sun publicly doubled down on fraud allegations against First Digital Trust and urged Hong Kong regulators to act and reform trust law.

---

## Trading Relevance

- **Why traders watch it:** TUSD is a live experiment in stablecoin counterparty risk. The peg has held only because of a billionaire backstop, not reserve quality — making TUSD (and its Curve/Uniswap pools) a venue for **depeg speculation** and a leading indicator for contagion into Tron-ecosystem assets and FDUSD. See [[stablecoin-depegs]].
- **Where it trades:** Binance, Bitget, KuCoin, Upbit (spot); Uniswap V2/V3, Sushiswap. Liquidity is thin relative to peak (24h volume ~$17M, June 2026 snapshot) — exits in size are slow during stress.
- **Signals:** discount/premium to $1.00 on Binance TUSD/USDT, Chainlink PoR feed anomalies, Hong Kong/Dubai court rulings, and any Justin Sun headline (he is simultaneously lender of last resort and the loudest public accuser of its trustee).
- **Structural take:** supply has been roughly flat near ~$500M since 2024; TUSD has lost the growth war to [[usdt]], [[usdc]] and FDUSD and its remaining use is legacy pairs and Tron-ecosystem plumbing.

---

## Peer Comparison — fiat-backed USD stablecoins

| Stablecoin | Issuer | Backing model | Reserve quality | Yield to holder | Relative size |
|---|---|---|---|---|---|
| [[usdt]] (USDT) | Tether | Cash, T-bills, BTC, gold, secured loans | Mixed; large T-bill book | No | #1 by far |
| [[usdc]] (USDC) | Circle | Cash + short T-bills (Circle Reserve Fund) | High, regulated | No (paid to Circle) | #2 |
| [[first-digital-usd|FDUSD]] (FDUSD) | First Digital | Cash + T-bills (FDT custody) | Questioned (FDT litigation) | No | Mid |
| **TUSD** | Techteryx | Claimed cash; **reserves found illiquid** | **Compromised; Sun-backstopped** | No | #105, ~$493M |

Versus yield-bearing alternatives ([[ylds|YLDS]], [[ousg|OUSG]], BUIDL, [[usx|USX]]/eUSX), TUSD pays nothing and carries materially higher counterparty risk — its only remaining edge is legacy listing breadth and Tron-ecosystem plumbing.

---

## Platform & Chain Information

| Chain | Address |
|---|---|
| Ethereum | `0x0000000000085d4780b73119b644ae5ecd22b376` |
| Tron | `TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4` |
| BNB Beacon | `TUSDB-888` |
| BNB Smart Chain | `0x40af3827f39d0eacbf4a168f8d4ee67c121d11c9` |
| Avalanche | `0x1c20e891bab6b1727d14da358fae2984ed9b59eb` |

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://tusd.io/](https://tusd.io/) |
| **Twitter** | [@tusdio](https://twitter.com/tusdio) |
| **Telegram** | [TUSDofficial_EN](https://t.me/TUSDofficial_EN) (5,660 members, April 2026) |
| **Discord** | [https://discord.com/invite/tusdio](https://discord.com/invite/tusdio) |
| **GitHub** | [https://github.com/trusttoken/trueUSD](https://github.com/trusttoken/trueUSD) |
| **Whitepaper** | [TrueUSD whitepaper (Feb 2026)](https://tusd.io/docs/trueusd-white-paper-202602.pdf) |

---

## Developer Activity (April 2026 snapshot)

| Metric | Value |
|---|---|
| **GitHub Stars** | 320 |
| **GitHub Forks** | 131 |
| **Pull Requests Merged** | 1,039 |
| **Contributors** | 28 |

---

## Risks

| Risk | Assessment |
|---|---|
| **Reserve / custodial** | **Severe.** Reserves were found routed into an illiquid Dubai trade-finance vehicle via trustee First Digital Trust; peg solvency currently depends on Justin Sun's loan, not on liquid backing |
| **De-peg** | **Elevated.** Trades at a persistent small discount; any Sun-withdrawal or adverse court ruling could break par. Contagion channel into [[first-digital-usd|FDUSD]] and Tron assets |
| **Regulatory / legal** | **High.** SEC fraud settlement (2024); active Hong Kong + Dubai litigation; offshore BVI issuer with limited recourse |
| **Counterparty concentration** | A single billionaire (Sun) is simultaneously lender of last resort and the loudest public accuser of the trustee — a fragile, conflicted arrangement |
| **Liquidity** | Secondary depth far below peak; large exits slow under stress |

---

## Related

- [[stablecoins]], [[stablecoin]], [[stablecoin-depegs]], [[stablecoin-supply]]
- [[usdt]], [[usdc]], [[first-digital-usd]] — competing USD stablecoins
- [[ylds]], [[ousg]] — yield-bearing dollar alternatives
- [[real-world-assets]], [[tokenized-treasuries]]
- [[ethereum]], [[crypto-markets]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (market data tables above)
- [SEC press release 2024-145 — Charges against TrustToken and TrueCoin](https://www.sec.gov/newsroom/press-releases/2024-145)
- [CoinDesk — Justin Sun bailed out TUSD as $456M reserves were stuck in limbo (Apr 2, 2025)](https://www.coindesk.com/markets/2025/04/02/tron-s-justin-sun-bailed-out-tusd-as-stablecoin-s-usd456m-reserves-were-stuck-in-limbo)
- [CoinDesk — Dubai court freezes $456M linked to Techteryx bailout (Nov 12, 2025)](https://www.coindesk.com/policy/2025/11/12/dubai-court-freezes-usd456m-linked-to-justin-sun-s-bailout-of-trueusd-issuer-techteryx)
- [The Block — FDUSD depegs 9% after Sun raises First Digital solvency concerns](https://www.theblock.co/post/349289/tron-justin-sun-trueusd-fiduciary-insolvent-techteryx-tusd-first-digital-aria)
- Perplexity sonar verification attempt + WebSearch verification, 2026-06-10
