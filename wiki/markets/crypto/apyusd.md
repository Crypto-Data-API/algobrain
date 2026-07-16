---
title: "apyUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["APYUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://apyx.fi"
related: ["[[crypto-markets]]", "[[depeg]]", "[[ethena-usde]]", "[[ethereum]]", "[[morpho]]", "[[pendle]]", "[[stablecoins]]"]
---

# apyUSD

**apyUSD** (ticker **APYUSD**; native chain [[ethereum|Ethereum]], also on Base) is a **yield-bearing** ERC-4626 vault token issued by the **Apyx** protocol. It wraps **apxUSD**, a USD-denominated [[stablecoins|stablecoin]] backed by **preferred-equity shares of Digital Asset Treasury (DAT) companies**. The underlying apxUSD targets a **1:1 dollar peg**; apyUSD is its interest-accruing wrapper, so its **redemption rate (and market price) rises above $1 over time** as the dividend yield from the DAT preferred shares compounds — it is **not** a $1 unit and a price above $1 is expected behaviour, not a de-pegged dollar. The yield model is therefore **real-world-asset (RWA) dividend income**, distinct from CDP, fiat-reserve, or delta-neutral-carry designs.

## Market data

| Field | Value |
|---|---|
| **Ticker** | APYUSD |
| **Price** | $1.22 (yield-accruing wrapper, not a $1 unit) |
| **Market cap** | $156.57M |
| **Market-cap rank** | #203 |
| **24h volume** | $549.06K |
| **24h change** | +1.26% |
| **Circulating supply** | 128.20M APYUSD |
| **Total supply** | 128.20M APYUSD |
| **All-time high** | $1.52 (2026-03-23) |
| **All-time low** | $1.064 (2026-06-05) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*
>
> *Disclaimer: figures are a point-in-time snapshot and not investment advice. Verify live data and the protocol's own attestations before trading.*

## Architecture — How Apyx Works

apyUSD is the **savings wrapper** in a two-token system, structurally like Maker's sDAI or Ethena's sUSDe (see [[ethena-usde]]):

- **apxUSD** — the $1-pegged base dollar, backed by **preferred equity shares of Digital Asset Treasury (DAT) companies** (publicly-listed firms that hold crypto on their balance sheets and issue preferred stock paying cash dividends). Custody of the underlying preferred-share collateral is provided by **Anchorage Digital** and **BitGo**, both regulated custodians.
- **apyUSD** — minted by depositing apxUSD into the Apyx ERC-4626 yield vault. The vault collects cash dividends paid by the DAT preferred shares and distributes that income by **increasing the apyUSD→apxUSD exchange rate** over time. Holders earn passively; no staking or manual claiming.

### Peg, NAV & redemption

apxUSD's $1 peg is anchored to the **net asset value** of the preferred-share collateral and 1:1 redemption against it. Because yield accrues into the redemption rate, **apyUSD's market price trades above $1 and drifts upward** (snapshot ~$1.22, ATH $1.52). Redemption is to apxUSD (and ultimately to the dollar value of the underlying preferred-share dividends), **not** directly to fiat at $1 per token — so the relevant "peg" question for apyUSD is whether its market price tracks the vault's true NAV exchange rate, while for apxUSD it is whether the base dollar holds $1.

### Yield source & distribution

The yield is **RWA dividend income** — cash dividends from DAT-company preferred equity — net of fees, compounded into the redemption rate. This is a fundamentally different (and more credit-exposed) source than T-bill pass-throughs, CDP stability fees, or funding-rate carry: it depends on issuers actually *paying* their preferred dividends, which can be suspended.

## Tokenomics & Supply

- **Circulating / total supply:** ~128.20M APYUSD (fully circulating). ~$156.57M market cap, rank #203 — the largest of this cohort by cap.
- apyUSD is **mint-on-deposit / burn-on-redeem** against apxUSD; there is no fixed cap, and the unit count is roughly stable while the *per-token value* grows with accrued yield.
- The two-token split cleanly separates the **dollar unit (apxUSD)** from the **yield-bearing claim (apyUSD)**.

## Comparison vs Peer Stablecoins

| Feature | **Apyx (apyUSD)** | [[ethena-usde\|Ethena sUSDe]] | Maker sDAI | Ondo USDY |
|---|---|---|---|---|
| Unit type | Yield wrapper (price > $1) | Yield wrapper (price > $1) | Yield wrapper (price > $1) | Yield wrapper (price > $1) |
| Base dollar | apxUSD | USDe | DAI | USD reserve |
| Backing | DAT-company **preferred equity** | Crypto + delta-neutral hedge | Crypto/RWA CDPs | Short-term Treasuries |
| Yield source | RWA preferred **dividends** | Funding-rate carry | DSR / RWA | T-bill interest |
| Custody | Anchorage, BitGo | On/off-exchange | On-chain | Regulated custodian |
| Composability | [[pendle\|Pendle]], [[morpho\|Morpho]] | Broad | Broad | Growing |
| Key risk | Dividend suspension / equity credit | Negative funding | Oracle/governance | Treasury/issuer |

## How & Where It Trades / Is Used

apyUSD is **composable across DeFi rather than centrally listed**: it integrates with [[pendle|Pendle]] for yield tokenization/trading (splitting into PT/YT to lock or speculate on the yield) and with [[morpho|Morpho]] for use as lending collateral. Reported 24h volume is **~$549K** — modest but the deepest of this cohort — and liquidity is concentrated in on-chain DeFi venues. Pricing is driven by the underlying NAV exchange rate plus secondary supply/demand; **thin pools can produce temporary premiums or discounts to fair (NAV) value**, so confirm pool depth on Pendle/DEXs before sizing.

## Narrative / Category & Catalysts

apyUSD sits at the intersection of two hot narratives: **yield-bearing dollars** and **tokenised RWA / Digital Asset Treasuries**. DAT companies (crypto-on-balance-sheet firms) have proliferated, and their preferred stock offers a real dividend stream that Apyx packages into an on-chain dollar — a genuinely differentiated yield source. Catalysts: growth of the DAT sector and its preferred issuance, deeper Pendle/Morpho integrations, demand for non-crypto-correlated stablecoin yield, and clearer regulatory treatment of tokenised equity. The dominant risk-narrative is that DAT preferred equity is **credit- and equity-linked** — in a bottoming/Extreme-Fear crypto market (Fear & Greed 21, as of 2026-06-22), DAT-company balance sheets and dividend capacity are exactly what comes under stress, so the yield's quality is regime-sensitive.

## History / Timeline

- **2026-03-23** — Recorded **all-time high of $1.52** (wrapper price reflecting peak accrued yield / premium).
- **2026-06-05** — Recorded **all-time low of $1.064**, i.e. the wrapper *compressed* toward its base — a reminder that the apyUSD price can fall (relative to its prior level) if NAV falls or the premium unwinds, even though it stays above $1.
- **2026-06-21** — Snapshot: apyUSD ~$1.22, market cap ~$156.57M, rank #203, 24h volume ~$549K, 24h +1.26%. Trading as a healthy yield wrapper above $1.

## Risks

- **Collateral / credit risk:** Backed by DAT-company **preferred equity** — credit, dividend-suspension, and mark-to-market risk on those shares flows straight into the peg and yield. This is materially riskier and less liquid than T-bill or fiat backing, and is **correlated to crypto** because DAT firms hold crypto on their balance sheets.
- **Yield-source / counterparty risk:** The yield depends on issuers actually paying preferred dividends; a suspension cuts the yield and can impair NAV.
- **Valuation / NAV risk:** Market price can diverge from the true exchange rate if the vault's underlying assets are mispriced or illiquid — the apyUSD premium/discount is itself a risk.
- **Custodial risk:** Reliance on **Anchorage Digital** and **BitGo** for collateral custody — a custodian failure threatens the backing.
- **Redemption-gating risk:** Exit is to apxUSD then to the dollar value of preferred-share dividends, not instant fiat — redemption can lag if the underlying RWA is illiquid.
- **Smart-contract / integration risk:** ERC-4626 vault plus [[pendle|Pendle]] and [[morpho|Morpho]] integrations add composability and exploit surface.
- **De-peg risk on apxUSD:** If the base apxUSD loses its dollar peg, apyUSD's value falls proportionally (the ATL $1.064 shows the wrapper has compressed before). See [[depeg]].
- **Regulatory risk:** Tokenised equity-backed dollars sit in an unsettled securities/stablecoin regulatory area.

## Trading / Usage Playbook

- **Never read apyUSD's >$1 price as a depeg** — it is an accruing wrapper. Judge it against its NAV exchange rate, and judge *apxUSD* against $1.
- **Understand you are taking RWA equity-credit risk, not cash risk.** The yield is DAT preferred dividends; treat it like a credit instrument that can be impaired.
- **Use Pendle PT/YT to express a view:** buy PT to lock a fixed rate, YT to lever the yield — but only after confirming pool depth.
- **Check the premium/discount to NAV before entering;** thin pools can leave you buying a temporary premium that mean-reverts.
- **Mind the crypto correlation** of the DAT collateral — this is not a defensive, market-neutral dollar in a downturn.

## Platform & chain

Native chain: [[ethereum|Ethereum]]. Also on Base.

| Chain | Contract |
|---|---|
| Ethereum | `0x38eeb52f0771140d10c4e9a9a72349a329fe8a6a` |
| Base | `0x2c271ddf484ac0386d216eb7eb9ff02d4dc0f6aa` |

## See also

- [[stablecoins]] — category overview
- [[ethena-usde]] — peer yield-bearing synthetic dollar (sUSDe analogue)
- [[pendle]], [[morpho]] — DeFi integrations
- [[depeg]] — peg-failure mechanics
- [[crypto-markets]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
