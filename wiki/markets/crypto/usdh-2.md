---
title: "USDH"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoin, defi]
aliases: ["USDH", "Native USDH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nativemarkets.com"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[stablecoins]]", "[[treasury-bonds]]"]
---

# USDH

**USDH** is a **fiat-backed digital dollar [[stablecoin|stablecoin]]** built natively for [[hyperliquid|Hyperliquid]] (chain: [[hyperliquid|HyperEVM]]). It is designed by **Native Markets** and issued by **Bridge Building Inc**, and aims to be the credible, ecosystem-aligned native dollar for the Hyperliquid / HyperEVM ecosystem. Unlike a [[synthetic-dollar]] minted against crypto, USDH is **fully reserved by cash and short-term US-government instruments**, redeemable 1:1.

> **Subject note / disambiguation:** "USDH" is a name shared by several unrelated projects (historically Hubble Protocol's USDH on Solana, among others). *This* page is specifically the **Native Markets / Bridge Building USDH for Hyperliquid**, the winner of Hyperliquid's native-stablecoin ticker process. Do not conflate it with other USDH coins.

What makes USDH distinctive is not its reserve model — fully-reserved fiat dollars are well-trodden — but its **ecosystem-alignment economics**: Native Markets programmatically routes 50% of gross revenue to the Hyperliquid Assistance Fund to buy back [[hyperliquid|HYPE]], turning the stablecoin's float into a flywheel for the host chain. This is the "Aligned Quote Asset" thesis: the native dollar of a venue should recycle its reserve income back into that venue rather than to an external issuer.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* USDH trades at **$0.999769** (rank **#792**, market cap **$21,354,683**, 24h **-0.02%**, 7d **+0.02%**) — effectively **on-peg at $1.00**. The negligible 24h/7d moves and tight trading range are exactly what you want from a fully-reserved fiat-backed dollar, indicating a healthy peg.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDH |
| **Market Cap Rank** | #792 |
| **Market Cap** | $21,354,683 |
| **Current Price** | $0.999769 |
| **Peg Status** | On-peg (~$1.00) |
| **Categories** | Stablecoins, USD Stablecoin, Hyperliquid Ecosystem, HyperEVM Ecosystem |
| **Website** | [https://nativemarkets.com](https://nativemarkets.com) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Architecture — How USDH Works

USDH is a **fully-reserved fiat-backed stablecoin** — the same conservative archetype as [[usdc|USDC]] — but engineered specifically as Hyperliquid's native quote dollar with revenue recycled to the host ecosystem.

### Backing and reserves
USDH is **fully reserved** by GENIUS-ready assets such as cash, short-term [[treasury-bonds|US Treasuries]], repurchase (repo) agreements, money-market funds investing in Treasuries and repo (e.g., BlackRock TTTXX), and tokenized versions of the same (e.g., [[blackrock-buidl|BlackRock BUIDL]] or Superstate USTB) — i.e., it is partly an on-chain [[real-world-assets|RWA]] dollar. Custody is segregated: cash sits at US-regulated banks, TradFi investment assets are custodied at JP Morgan Chase, and cryptoassets are held in Bridge's MPC infrastructure provisioned by Fireblocks. **BPM**, a top-40 San Francisco accounting firm, reviews and attests to the 1:1 backing of USDH's reserves each month (see [[stablecoin-attestations]]).

### Mint / redeem and peg maintenance
Because reserves are held 1:1 in cash and cash-equivalents, the peg is maintained by **direct primary-market issuance and redemption at par**: authorised parties mint USDH by delivering dollars and redeem USDH for dollars, and arbitrageurs close any secondary-market gap. The arbitrage loop is the hard peg enforcer — below $1, buy and redeem; above $1, mint and sell. At **$0.999769** on 2026-06-22 the token is trading essentially at par, and the tight 24h range ($0.9984–$1.00) confirms a healthy peg.

### Yield / revenue model
Unlike a pure pass-through reserve coin, USDH's reserve income is captured at the issuer level and *recycled*: the float earns the T-bill/repo/money-market yield, and Native Markets directs that revenue per the alignment policy below rather than distributing it pro-rata to every holder. Holders therefore get a stable dollar plus indirect ecosystem benefit (HYPE buybacks) rather than a direct yield stream.

### Ecosystem alignment ("Aligned Quote Asset")
Native Markets contributes **50% of gross revenue** to the Hyperliquid Assistance Fund so the protocol can buy back [[hyperliquid|HYPE]]; the remainder funds growth of USDH and the Hyperliquid ecosystem. As specified by the Aligned Quote Asset ("AQA") protocol primitive, the Assistance Fund contribution is made programmatically, on-chain — the structural feature that differentiates USDH from a generic fiat dollar parachuted onto Hyperliquid.

---

## Comparison vs Peer Stablecoins

| Dimension | **USDH** (Native/Bridge) | [[usdc\|USDC]] (Circle) | [[ethena-usde\|USDe]] (Ethena) | [[usdu\|USDU]] (Unitas) |
|---|---|---|---|---|
| **Peg model** | Fiat, 1:1 reserve | Fiat, 1:1 reserve | Synthetic, delta-neutral | Fiat/RWA, 1:1 reserve |
| **Backing** | Cash + T-bills + repo + tokenized MMFs | Cash + short T-bills | Crypto + perp shorts | Cash + short T-bills |
| **Reserve income** | Recycled → HYPE buybacks | Retained by Circle | Funding → sUSDe | To holders |
| **Native venue** | Hyperliquid / HyperEVM | Multi-chain | Multi-chain | Solana / BNB |
| **Transparency** | Monthly BPM attestation | Monthly attestation | On-chain reserves dashboard | On-chain proof-of-reserves |
| **Differentiator** | Ecosystem-aligned (AQA) | Scale / liquidity | Crypto-native yield | Real-yield to holder |

USDH's nearest functional comparison is USDC (same fully-reserved fiat model); its strategic comparison is to other *native venue dollars*, where its AQA revenue-recycling is the distinguishing feature.

---

## How & Where It Trades / Is Used

- **Primary venue:** native to [[hyperliquid|Hyperliquid / HyperEVM]] (contract `0x111111a1a0667d36bd57c0a9f569b98057111111`), used as a quote and collateral asset within that ecosystem.
- **Composability:** as the ecosystem-aligned dollar, USDH is designed to be the default quote/collateral currency across HyperEVM DeFi — order-book quoting, lending, and AMM pairs — concentrating its utility (and its risk) inside Hyperliquid.
- **Liquidity:** ~$10.83M 24h volume against a ~$21.4M cap is unusually high turnover for a coin this size, reflecting active use as a Hyperliquid quote asset rather than a passive store of value. No major centralized-exchange listings were found in CoinGecko data; liquidity is on-chain/native.

---

## Narrative / Category & Catalysts

USDH rides two converging narratives: the **fiat-backed RWA-dollar** theme (reserve income from T-bills) and the **"native quote asset"** theme — the idea that a major trading venue should run its own aligned dollar rather than rent liquidity from an external issuer. Catalysts:

- **Hyperliquid growth = USDH demand:** USDH float scales with Hyperliquid trading activity and HyperEVM DeFi adoption; the AQA buyback flywheel ties USDH success to HYPE.
- **Stablecoin regulation (GENIUS-ready framing):** USDH explicitly markets reserves as "GENIUS-ready," positioning it for compliant US stablecoin regimes — a tailwind if such rules formalize.
- **Native-dollar trend:** if the "every major venue runs its own aligned stablecoin" thesis spreads, USDH is an early reference implementation.
- **Concentration is the flip side:** the same tight coupling that drives demand also means Hyperliquid-specific stress feeds straight back into USDH liquidity.

---

## History / Timeline

- **2025-10-10** — Both the recorded all-time high ($1.11) and all-time low ($0.7169) print on this date per CoinGecko data — an early, illiquid launch-window range; the wide spread on a single day reflects thin price discovery before liquidity deepened, not a sustained de-peg.
- **2026-04-09** — Captured in the wiki via the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); page created.
- **2026-06-22** — Market-data refresh: price $0.999769, cap ~$21.35M, rank #792, on-peg with a tight $0.9984–$1.00 range.
- **2026-06-23** — Page expanded to `excellent`.

> Note: only wiki-verified dates are listed; further dated launch/funding milestones are not yet ingested from a primary source.

---

## Risks

- **Reserve / counterparty risk** — dependence on banks, JP Morgan custody and tokenized-Treasury issuers (BlackRock, Superstate); a custodian or issuer failure could impair backing.
- **Off-chain dependency** — redemption at par relies on off-chain banking rails and the issuer honouring redemptions; banking disruptions are the classic fiat-backed [[depeg]] trigger (cf. USDC during the March 2023 SVB episode; see [[stablecoin-depegs]]).
- **Attestation vs. audit** — monthly attestations are reviews, not full audits; reserve transparency is only as good as the attestor's scope.
- **Concentration / ecosystem risk** — USDH is tightly coupled to Hyperliquid; stress in that single venue affects demand and liquidity, and a HyperEVM smart-contract or oracle failure would hit USDH directly.
- **Regulatory risk** — yield-bearing/ecosystem-revenue mechanics and the reserve composition sit within evolving stablecoin and securities frameworks.
- **Macro backdrop** — at the 2026-06-23 snapshot the market is in **Extreme Fear (F&G 21)**, market-health 29/100, long-horizon regime **bottoming / accumulation**; fully-reserved fiat dollars are defensive here, but a venue as cyclical as Hyperliquid can see USDH turnover fall sharply in risk-off conditions.

---

## Trading / Usage Playbook

- **Use it as Hyperliquid's quote dollar, not a yield instrument.** Holders do not receive direct reserve yield (that is recycled to HYPE buybacks); the value proposition is a stable, ecosystem-aligned unit of account on HyperEVM.
- **Par enforcement is via authorised-party arbitrage.** The tight $0.9984–$1.00 range shows the loop works at current liquidity; in stress, watch whether redemption stays live before assuming hard par.
- **HYPE-linked exposure:** USDH adoption indirectly bids HYPE via the Assistance Fund; traders bullish on Hyperliquid may view USDH growth as a leading indicator.
- **Concentration discipline:** because USDH lives almost entirely inside Hyperliquid, treat venue risk (HyperEVM contract/oracle, exchange operational risk) as part of holding the dollar.

> *Not financial advice. Even fully-reserved fiat stablecoins can de-peg on banking-rail or custodian stress.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 21.36M USDH |
| **Total Supply** | 100.09B USDH |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $100.10B |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.11 (2025-10-10) |
| **Current vs ATH** | -10.19% |
| **All-Time Low** | $0.7169 (2025-10-10) |
| **Current vs ATL** | +39.36% |
| **24h Change** | -0.02% |
| **7d Change** | +0.02% |

---

## Platform & Chain Information

**Native Chain:** Hyperevm

### Contract Addresses

| Chain | Address |
|---|---|
| Hyperevm | `0x111111a1a0667d36bd57c0a9f569b98057111111` |
| Hyperliquid | `0x54e00a5988577cb0b0c9ab0cb6ef7f4b` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://nativemarkets.com](https://nativemarkets.com) |
| **Twitter** | [@nativemarkets](https://twitter.com/nativemarkets) |
| **Telegram** | [nativemarkets](https://t.me/nativemarkets) (525 members) |
| **GitHub** | [https://github.com/native-markets](https://github.com/native-markets) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $10.83M |
| **Market Cap Rank** | #787 |
| **24h Range** | $0.9984 — $1.00 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[hyperliquid]]
- [[stablecoins]]
- [[stablecoin-attestations]]
- [[stablecoin-depegs]]
- [[treasury-bonds]]
- [[real-world-assets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and Native Markets / Bridge Building public documentation; market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.
