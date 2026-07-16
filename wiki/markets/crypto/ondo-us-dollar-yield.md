---
title: "Ondo US Dollar Yield"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, treasuries]
aliases: ["US Dollar Yield Token", "USDY"]
entity_type: protocol
founded: 2023
headquarters: "Ondo Finance (USA; USDY offered to non-US persons)"
website: "https://ondo.finance/usdy"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[janus-henderson-anemoy-treasury-fund]]", "[[ondo-finance]]", "[[real-world-assets]]", "[[stablecoins]]"]
---

# Ondo US Dollar Yield

**Ondo US Dollar Yield** (USDY) is a [[tokenized-treasuries|tokenized]] note issued by [[ondo-finance|Ondo Finance]] (ticker USDY; native on [[ethereum|Ethereum]], deployed across 12+ chains), secured by short-term [[treasury-bills|US Treasuries]] and bank demand deposits, that passes Treasury yield through to holders — an **accumulating** token whose price rises over time (~$1.14 by mid-2026) rather than pegging to $1. It is one of the largest [[tokenized-treasuries|tokenized-Treasury]] products (~$2.16B market cap, rank #42 as of June 2026) and matters to traders as the flagship **yield-bearing dollar** in the [[real-world-assets|RWA]] sector and as on-chain collateral spreading across a dozen chains.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (NAV/token)** | $1.14 — accumulating note; rises with accrued Treasury interest |
| **Market cap** | $2.16B |
| **Market-cap rank** | #42 |
| **24h volume** | $1.69M (thin secondary; hold-to-earn, not a trading vehicle) |
| **Circulating supply** | 1.896B USDY |
| **Total supply** | 1.896B USDY (MC/FDV = 1.00 — all minted tokens now circulating) |
| **Max supply** | None (mint/redeem) |
| **24h change** | −0.24% |
| **7d change** | +0.21% (≈ weekly Treasury carry) |
| **All-time high** | $1.26 (2024-03-27, thin-market dislocation) — currently −9.9% |
| **All-time low** | $0.9342 (2024-01-14) — currently +21.8% |

*Note: as a [[real-world-assets|RWA]] accumulating note, USDY's "price" tracks accrued [[treasury-bills|T-bill]] interest, not market discovery — small daily moves and a slowly rising fair value are expected. Macro backdrop: [[crypto-fear-and-greed-index|Fear & Greed]] 23 ("Established Bear Market") — USDY is uncorrelated to crypto risk sentiment; the ATH/ATL prints are thin-liquidity artifacts, not real depegs.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDY |
| **Market Cap** | $2.16B (2026-06-20; 1.896B circulating at $1.14) |
| **Market Cap Rank** | #42 (2026-06-20) |
| **Type** | [[tokenized-treasuries|Tokenized]] note: short-term [[treasury-bills|US Treasuries]] + bank demand deposits; yield accrues into token price |
| **Backing** | Bankruptcy-remote note with first-priority security interest over the underlying T-bills and bank deposits |
| **Eligibility** | Non-US persons; no qualified-purchaser requirement (unlike Ondo's [[ousg|OUSG]]) |
| **Chains** | [[ethereum|Ethereum]] (native) + Solana, Sui, Aptos, Arbitrum, Mantle, Noble/Cosmos, Stellar, Sei, Plume, Osmosis, Mantra — 12+ deployments |
| **Redemption** | Mint/redeem directly with Ondo; 40–50 day initial transfer lock on freshly minted tokens |
| **Website** | [https://ondo.finance/usdy](https://ondo.finance/usdy) |

---

## Overview

USDY (US Dollar Yield Token) is a tokenized note secured by short-term US Treasuries and bank demand deposits. Unlike fiat-pegged stablecoins, USDY is **accumulating**: the redemption value (and market price) rises as Treasury interest accrues — from ~$1.00 at the January 2024 launch to ~$1.11–1.13 by mid-2026. A rebasing wrapper (rUSDY) exists for integrations that prefer a $1 peg with growing balances.

USDY is structured as a bankruptcy-remote note with first-priority security interest over the underlying assets, offered to non-US individuals and institutions without qualified-purchaser status — the "retail-accessible" counterpart to Ondo's institutional [[ousg|OUSG]] fund. Growth in 2025–2026 was driven by multi-chain expansion (notably Solana, Sui, Aptos, Stellar, Plume) and integrations as collateral and treasury asset across DeFi, alongside the broader boom in Ondo's RWA stack (see [[ondo-finance]]).

---

## Mechanism & Backing

| Dimension | Detail |
|---|---|
| **Underlying assets** | Short-term [[treasury-bills|US Treasury bills]] plus bank demand deposits — the demand-deposit sleeve provides near-instant liquidity that a pure T-bill fund lacks |
| **Yield source** | The short-term Treasury rate, passed through by **NAV accrual**: the redemption value and market price rise as interest accrues (from ~$1.00 at the Jan-2024 launch toward ~$1.14 by mid-2026). Realized return tracks the prevailing T-bill yield net of fees (qualitative — not a fixed APY) |
| **Wrapper** | A **note** (debt instrument), not a money-market fund or equity — holders have a first-priority security interest over the collateral. A rebasing variant **rUSDY** keeps a $1 unit price with a growing balance for integrations that prefer a peg |
| **Custody** | Underlying T-bills and bank deposits held by third-party custodians/banks; structured as bankruptcy-remote from Ondo |
| **Redemption** | Direct mint/redeem with [[ondo-finance|Ondo]]; freshly minted tokens carry a 40–50 day initial transfer restriction before they are freely transferable |
| **KYC / permissioning** | Offered to **non-US persons** only; no qualified-purchaser gate (the key contrast with OUSG, which is qualified-purchasers-only) — this is the "general access" tier of Ondo's stack |
| **Regulatory wrapper** | Issued to non-US individuals/institutions; structured to sit outside US securities-registration requirements by excluding US persons |

> **Not a stablecoin:** USDY is yield-bearing and accumulating, so it is **not** $1-pegged. Compare pegged, no-yield [[stablecoins]] ([[first-digital-usd|FDUSD]], [[global-dollar|USDG]]) vs accumulating yield tokens (USDY, [[ousg|OUSG]], [[hashnote-usyc|USYC]]).

---

## Trading Relevance

- **Where it trades**: primarily minted/redeemed directly with Ondo; thin secondary markets on Uniswap V3 (Ethereum, vs USDT) and Orca (Solana). On-screen volume is small (~$0.1–10M/day) — this is a **hold-to-earn instrument, not a trading vehicle**.
- **Why traders care anyway**:
  - **Cash-management leg**: a way to keep on-chain dry powder earning ~Treasury yield between trades (non-US accounts only).
  - **RWA-narrative indicator**: USDY supply growth is a clean read on tokenized-Treasury demand, the core metric behind the [[narrative-trading]] RWA basket (ONDO, plus peers like BlackRock's BUIDL and [[janus-henderson-anemoy-treasury-fund|JTRSY]]).
  - **Collateral creep**: each new chain/perp-venue accepting USDY as margin deepens structural demand.
- **Risks**: not redeemable by US persons; 40–50 day initial transfer restrictions on minted tokens; issuer/structure risk (note, not a money-market fund); small secondary-market depth means exits at size go through redemption, not the order book.

---

## Tokenomics

See the **Market Data** block above for the authoritative supply/price/market-cap snapshot (2026-06-20: 1.896B USDY circulating, $1.14/token, $2.16B mcap, MC/FDV = 1.00). Structural notes:

- **Float caught up to supply**: at the April 2026 snapshot circulating was ~1.17B vs ~1.89B total (MC/FDV 0.62); by 2026-06-20 essentially all minted USDY is in circulation (MC/FDV 1.00).
- **No max supply**: tokens mint on subscription and burn on redemption, so float is a direct read on tokenized-Treasury demand.
- **Price History**: ATH $1.26 (2024-03-27) and ATL $0.9342 (2024-01-14) are **thin-market dislocations** near launch, not depegs — fair value simply tracks accrued [[treasury-bills|Treasury]] interest, ~$1.14 by mid-2026.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x96f6ef951840721adbf46ac996b59e0235cb985c` |
| Noble | `ausdy` |
| Sui | `0x960b531667636f39e85867775f52f6b1f220a058c4de786905bdf761e06a56bb::usdy::USDY` |
| Osmosis | `ibc/23104D411A6EB6031FA92FB75F227422B84989969E91DCAD56A535DD7FF0A373` |
| Mantle | `0x5be26527e817998a7206475496fde1e68957c5a6` |
| Solana | `A1KLoBrKBde8Ty9qtNQUtq3C2ortoC3u7twggz7sEto6` |
| Mantra | `ibc/6749D16BC09F419C090C330FC751FFF1C96143DB7A4D2FCAEC2F348A3E17618A` |
| Stellar | `USDY-GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6` |
| Arbitrum One | `0x35e050d3c0ec2d29d269a8ecea763a183bdf9a9d` |
| Plume Network | `0xd2b65e851be3d80d3c2ce795eb2e78f16cb088b2` |
| Sei V2 | `0x54cd901491aef397084453f4372b93c33260e2a6` |
| Aptos | `0xcfea864b32833f157f042618bd845145256b1bf4c0da34a7013b76e42daa53cc` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca (Solana) | USDY/USDC | Spot |
| Uniswap V3 (Ethereum) | USDY/USDT | Spot |

---

## Peer Comparison — yield-bearing tokenized dollars

| Product | Issuer | Wrapper | Access | Size (2026-06-20) | Yield to holder |
|---|---|---|---|---|---|
| **USDY** | [[ondo-finance|Ondo]] | Note (T-bills + bank deposits) | Non-US, general access | $2.16B (#42) | Yes (NAV accrual) |
| [[ousg|OUSG]] | Ondo | Fund (T-bills via [[blackrock|BUIDL]]) | Qualified purchasers | $479M (#106) | Yes (NAV accrual) |
| [[hashnote-usyc|USYC]] | [[circle|Circle]]/Hashnote | MMF (T-bills + repo) | Institutional | $3.07B (#31) | Yes (NAV accrual) |
| [[spiko-us-t-bills-money-market-fund|USTBL]] | Spiko | EU MMF | All investors (EU) | $170M (#191) | Yes (NAV accrual) |
| [[global-dollar|USDG]] | [[paxos|Paxos]] | Payment stablecoin | Broad | $2.81B (#33) | No (shared with distributors) |
| [[first-digital-usd|FDUSD]] | First Digital | Payment stablecoin | Broad | $352M (#127) | No |

> USDY's niche: it is the **most retail-accessible yield-bearing tokenized dollar** (no qualified-purchaser gate), at the cost of US-person exclusion and the longest list of chain deployments.

---

## Risks

- **Eligibility / US-person exclusion**: not redeemable or transferable by US persons; a compliance failure on holder eligibility is a structural risk.
- **Transfer lock**: 40–50 day initial restriction on freshly minted tokens limits short-horizon use and means newly subscribed capital is illiquid for over a month.
- **Issuer / structure risk**: USDY is a **note**, not a money-market fund — holders rely on Ondo's bankruptcy-remote structuring and first-priority security interest rather than fund-level regulatory protections.
- **Custodial / bank risk**: the demand-deposit sleeve carries uninsured bank-deposit exposure (cf. the [[usdc|USDC]]/SVB March-2023 episode); the T-bill sleeve carries custodian risk.
- **Liquidity / exit-at-size**: thin secondary depth (~$1.7M/day) means large exits go through redemption, not the order book — fine in calm markets, a constraint in stress.
- **Smart-contract / bridge risk**: 12+ chain deployments multiply contract and bridge attack surface.
- **Rates risk**: NAV accrual falls with Fed cuts, compressing the yield advantage over zero-yield [[stablecoins]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ondo.finance/](https://ondo.finance/) |
| **Twitter** | [@ondofinance](https://twitter.com/ondofinance) |
| **GitHub** | [https://github.com/ondoprotocol/tokenized-funds](https://github.com/ondoprotocol/tokenized-funds) |
| **Docs** | [https://docs.ondo.finance/general-access-products/usdy/basics](https://docs.ondo.finance/general-access-products/usdy/basics) |

---

## Related

- [[ondo-finance]]
- [[crypto-markets]]
- [[ethereum]]
- [[stablecoins]]
- [[real-world-assets]]
- [[janus-henderson-anemoy-treasury-fund]]
- [[narrative-trading]]

---

## Sources

- Ondo Finance — USDY: https://ondo.finance/usdy
- CoinGecko / cryptodataapi.com — Ondo US Dollar Yield, snapshot 2026-06-20 (price $1.14, 1.896B supply, $2.16B mcap, rank #42): https://www.coingecko.com/en/coins/ondo-us-dollar-yield
- CoinMarketCap — USDY: https://coinmarketcap.com/currencies/ondo-us-dollar-yield/
- Ondo docs — USDY basics: https://docs.ondo.finance/general-access-products/usdy/basics
- Web verification, 2026-06-10: market cap ~$2.1B, accumulating-note structure, multi-chain deployments confirmed.
- (Source: [[coingecko-top-1000-2026-04-09]])

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.26 (2024-03-27) |
| **Current vs ATH** | -10.18% |
| **All-Time Low** | $0.9342 (2024-01-14) |
| **Current vs ATL** | +21.44% |
| **24h Change** | +0.27% |
| **7d Change** | +0.11% |
| **30d Change** | +1.03% |
| **1y Change** | +4.85% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.27M |
| **Market Cap Rank** | #40 |
| **24h Range** | $1.13 — $1.14 |
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
