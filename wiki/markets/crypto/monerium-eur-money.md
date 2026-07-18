---
title: "Monerium EURe"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, euro, forex, stablecoins]
aliases: ["EURE", "EURe", "Monerium EUR emoney"]
entity_type: protocol
headquarters: "Reykjavik, Iceland / EEA"
website: "https://monerium.com/tokens/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[euro]]", "[[forex]]", "[[gnosis-chain]]", "[[mica]]", "[[stablecoin]]"]
---

# Monerium EURe

**Monerium EURe** (ticker **EURE**) is a fully-regulated, fiat-backed [[euro]] [[stablecoin]] issued by Monerium ehf., the first company authorized to issue **electronic money (e-money) on public blockchains** under European Economic Area (EEA) financial regulation. EURe is a redeemable on-chain claim on euros held 1:1 in segregated, safeguarded accounts — a regulatory model (the **e-money / EMI** wrapper) distinct from the commercial-paper or offshore-reserve structures common to USD stablecoins. It is deployed primarily on [[ethereum|Ethereum]], [[gnosis-chain|Gnosis Chain]] (xDai), and Polygon. EURe ranks **#689** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

EURe trades at approximately **$1.15** because it is pegged to the **euro (EUR)**, not the US dollar. The ~$1.15 USD quote simply reflects the prevailing EUR/USD exchange rate — one EURe ≈ one euro ≈ $1.15. This is the intended [[forex]] peg, **not a [[depeg]]**: against its actual reference asset (the euro) EURe holds at ~€1.00. Market capitalization is roughly **$26.89M** (rank #689), with the token essentially flat over recent sessions (24h -0.08%, 7d -0.85%).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EURE |
| **Peg** | 1 EURe ≈ 1 EUR (euro, not USD) |
| **Issuer** | Monerium (licensed EMI under EEA regulation) |
| **Backing** | 1:1 segregated/safeguarded euro reserves |
| **Market Cap Rank** | #689 |
| **Market Cap** | $26,893,779 |
| **Current Price** | $1.15 (≈ €1.00 at prevailing EUR/USD) |
| **24h / 7d Change** | -0.08% / -0.85% |
| **Categories** | Stablecoins, DeFi, EUR Stablecoin, E-money token, Polygon/Gnosis Chain/Ethereum Ecosystem, Fiat-backed Stablecoin |
| **Website** | [https://monerium.com/tokens/](https://monerium.com/tokens/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Monerium is, to date, the only company authorized to issue money on blockchains under EEA financial regulation, and its e-money tokens are aligned with the EU's Markets in Crypto-Assets ([[mica|MiCA]]) framework for **e-money tokens (EMTs)**. The company has issued EUR, USD, GBP, and ISK as e-money tokens on Ethereum, and EUR on Algorand; **EURe** (the euro token) is by far the most widely used. Monerium also operates a gateway for instant transfers of EUR between traditional bank accounts (via SEPA) and blockchain wallets or smart contracts, effectively bridging the regulated banking rails to on-chain [[defi]]. The company was founded in 2015 by repeat entrepreneurs (including Jón Helgi Egilsson, a former chairman of the Central Bank of Iceland's supervisory board) and is backed by investors including Taavet+Sten, Crowberry Capital, Consensys, and Algorand.

Because Monerium is a regulated EMI, EURe is **electronic money** in the legal sense: every token in circulation is matched 1:1 by euros held in segregated, safeguarded accounts that are bankruptcy-remote from the issuer. This is a stronger holder protection than the typical fiat-backed stablecoin structure, where reserves may include commercial paper, money-market funds, or offshore deposits.

---

## Architecture — How the EMI Stablecoin Works

EURe is built around a **regulatory wrapper plus a 1:1 reserve**, not an algorithm or a crypto-collateral vault. The pipeline:

1. **Onboarding & KYC.** A user opens a Monerium account, completes KYC/AML, and links a wallet address. Unlike most stablecoins, the holder of record is a verified account holder, not an anonymous address.
2. **Mint via SEPA inflow.** When the user sends euros to their Monerium IBAN (a real bank account number), Monerium mints an equal amount of EURe directly to the user's chosen on-chain address. Issuance is 1:1 — €1 in = 1 EURe out.
3. **Safeguarding.** The incoming euros are held in **segregated client accounts** at partner banks. Under the EMI safeguarding regime, these funds are ring-fenced from Monerium's own balance sheet and are bankruptcy-remote: if Monerium failed, client euros are not part of the insolvency estate.
4. **On-chain use.** EURe is a standard ERC-20-style token, freely transferable and composable in [[defi]] — swappable on DEXs, usable as collateral, and acceptable in smart contracts.
5. **Redemption via SEPA outflow.** The user (or any whitelisted account holder) burns EURe and Monerium pays out euros to their bank account over SEPA. Redemption at par is the legal entitlement of an e-money holder, which is the ultimate anchor of the peg.

The peg therefore rests on **legal redeemability at par plus full reserves**, not on market arbitrage alone. The EMI model means each token is a direct liability of a supervised institution, closer in spirit to a tokenized bank deposit than to a synthetic dollar.

### Peg Mechanism — Why the USD Price Is ~$1.15

EURe is a **euro-denominated** stablecoin. Its target is parity with the euro (1 EURe = €1.00), not the US dollar. When quoted in USD, the price floats with the EUR/USD foreign-exchange rate:

- A ~$1.15 USD quote means EUR/USD ≈ 1.15 — i.e. the euro is worth about $1.15 at the time of the snapshot.
- A move in the USD quote (e.g. to $1.12 or $1.18) usually reflects a move in **EUR/USD**, not a failure of the peg.
- To assess peg health, measure EURe **against the euro**, where it should sit at ~€1.00.

This makes EURe a useful instrument for euro-denominated [[defi]], EUR/USD [[forex]] exposure on-chain, and SEPA-to-crypto settlement. Holders take on **currency risk** (EUR/USD fluctuation) exactly as they would holding physical euros.

---

## Tokenomics & Backing

| Metric | Value |
|---|---|
| **Circulating Supply** | ~24.7M EURe |
| **Max Supply** | Unlimited (minted/burned 1:1 against euro deposits/redemptions) |
| **Reserve Model** | 1:1 segregated, safeguarded euro balances (EMI safeguarding) |
| **Market Cap / FDV Ratio** | ~1.00 |

EURe has no speculative tokenomics or emissions — supply expands and contracts directly with deposits and redemptions, like any e-money float. Its value is anchored entirely by the redemption guarantee and the regulatory safeguarding regime rather than by an algorithmic or crypto-collateral mechanism. There is **no separate governance token**: Monerium is a regulated company, not a DAO, so monetary policy and reserve management are governed by the EMI license and EEA supervision rather than by on-chain voting.

---

## Comparison vs Other Euro Stablecoins

EURe competes in the small but strategically important **MiCA-era euro stablecoin** segment. The USD stablecoin market dwarfs it (USDT ≈ $186B, USDC ≈ $74.8B as of 2026-06-22), so euro stablecoins are an early adoption theme driven by European regulation rather than scale.

| Token | Issuer | Wrapper / Reserve | Distinguishing trait |
|---|---|---|---|
| **EURe** (Monerium) | Monerium ehf. (EMI) | E-money; 1:1 safeguarded euro accounts | First EMI to issue e-money on public chains; SEPA mint/redeem; multi-chain |
| **[[circle|EURC]]** (Circle) | Circle | MiCA EMT; cash & short T-bills | Backed by the USDC issuer; widest exchange distribution of any EUR stablecoin |
| **EURS** (STASIS) | STASIS | Fiat-backed euro reserves | One of the earliest euro stablecoins (2018); audited reserves |
| **agEUR / EURA** ([[angle-protocol|Angle]]) | Angle Protocol | Decentralized, over-collateralized / reserve-backed | DeFi-native euro unit; not an EMI e-money token |

EURe's edge is the **regulatory wrapper itself**: as an EMI-issued e-money token with native SEPA rails, it is positioned for compliant European payments and institutional settlement, whereas EURC competes on raw liquidity and exchange listings, and agEUR competes on DeFi composability.

---

## How & Where It Trades / Where It's Used

- **On/off-ramp.** The primary rail is Monerium itself: euros in/out over **SEPA** against on-chain mint/burn, with a real IBAN per account. This is the deepest and most reliable liquidity path — redemption at par directly with the issuer.
- **DEX liquidity.** Secondary trading is mainly on **Uniswap V3** (Ethereum) and on Gnosis Chain, where EURe is a staple euro unit for the Gnosis/Circles ecosystem. On-chain DEX depth is thin relative to USD stablecoins; large swaps can slip.
- **Use cases.** Euro-denominated payments and payroll, SEPA-to-DeFi bridging, on-chain settlement for European businesses, and EUR collateral or quote-asset in DeFi protocols deployed on Gnosis Chain.

---

## Narrative, Category & Catalysts

EURe sits at the intersection of three themes: **regulated stablecoins**, **MiCA implementation**, and **on-chain euro payments**. Catalysts to watch:

- **MiCA rollout.** [[mica|MiCA]]'s e-money-token rules give compliant euro EMTs a regulatory moat in the EU and pressure non-compliant issuers; Monerium's EMI status is directly aligned with this regime.
- **Institutional euro settlement.** Growth in tokenized euro payments, treasury operations, and on-chain payroll would expand EURe float.
- **Gnosis Chain ecosystem.** EURe is a default euro unit in parts of the Gnosis/Circles ecosystem; ecosystem growth lifts organic demand.
- **EUR/USD macro.** Because EURe is euro exposure, broad demand for euro-denominated on-chain cash tracks EUR/USD sentiment and European rate policy.

---

## History / Timeline

- **2015** — Monerium founded in Iceland.
- **2019** — Monerium becomes the first company authorized to issue e-money on a blockchain under EEA regulation (authorized as an EMI in Iceland, passportable across the EEA).
- **2022-09-06** — EURe records its all-time low USD quote of **$0.9520** (reflecting EUR/USD weakness near parity, not a peg break vs the euro).
- **2026-01-27** — EURe records its all-time high USD quote of **$1.21** (reflecting a stronger EUR/USD).

*(All dated price extremes above are from the market-data snapshot; they reflect EUR/USD movement, not euro-peg deviation.)*

---

## Risks & Considerations

- **FX / currency risk:** USD-based holders are exposed to EUR/USD swings. This is inherent to a euro asset and is **not** a stablecoin failure.
- **Depeg (vs euro) risk:** Distinct from FX, a true depeg would be EURe trading away from €1.00 — historically rare given full reserves and at-par redemption, but possible under operational or reserve stress.
- **Issuer / regulatory risk:** Holder protection depends on Monerium retaining its EMI license and on the safeguarding regime functioning as designed.
- **Reserve-counterparty risk:** Safeguarded euros sit at partner banks; a partner-bank failure or access disruption is a (mitigated, ring-fenced) counterparty exposure.
- **Liquidity:** On-chain DEX liquidity (primarily Uniswap V3 on Ethereum) is thin relative to USD stablecoins; large swaps can slip. Redemption via Monerium (SEPA) is the primary fiat off-ramp.
- **Smart-contract risk:** Standard exposure to the EURe token contracts across Ethereum, Gnosis Chain (xDai), and Polygon.

---

## Trading / Usage Playbook

- **As euro cash on-chain:** Use EURe to hold or transact euros in DeFi without USD exposure; treat the USD quote as EUR/USD, not as peg health.
- **For FX exposure:** Long EURe ≈ long EUR/USD; size positions against expected European rate / macro moves.
- **For settlement:** Prefer the Monerium SEPA rail for large mints/redemptions (par, no slippage); use DEXs only for small/instant swaps where thin depth is acceptable.
- **Peg monitoring:** Watch EURe vs €1.00 (not vs $1) and reserve/attestation disclosures; a sustained discount to the euro — not a falling USD quote — is the real warning sign.

*This is not investment advice; figures above are point-in-time market data, not a valuation.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 24.74M EURE |
| **Total Supply** | 24.78M EURE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $28.92M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.21 (2026-01-27) |
| **Current vs ATH** | -3.61% |
| **All-Time Low** | $0.9520 (2022-09-06) |
| **Current vs ATL** | +22.62% |
| **24h Change** | +0.05% |
| **7d Change** | +0.69% |
| **30d Change** | +0.52% |
| **1y Change** | +6.85% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3231cb76718cdef2155fc47b5286d82e6eda273f` |
| Xdai | `0xcb444e90d8198415266c6a2724b7900fb12fc56e` |
| Polygon Pos | `0x18ec0a6e18e5bc3784fdd3a3634b31245ab704f6` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X3231CB76718CDEF2155FC47B5286D82E6EDA273F/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://monerium.com/tokens/](https://monerium.com/tokens/) |
| **GitHub** | [https://github.com/monerium/smart-contracts](https://github.com/monerium/smart-contracts) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 48 |
| **GitHub Forks** | 23 |
| **Pull Requests Merged** | 16 |
| **Contributors** | 4 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.12M |
| **Market Cap Rank** | #667 |
| **24h Range** | $1.17 — $1.17 |
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
- [[ethereum]]
- [[gnosis-chain]]
- [[stablecoin]]
- [[euro]]
- [[forex]]
- [[depeg]]
- [[defi]]
- [[mica]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
