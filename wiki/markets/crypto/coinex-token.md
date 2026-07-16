---
title: "CoinEx Token"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["CET", "CoinEx", "CoinEx Token"]
entity_type: protocol
headquarters: "Hong Kong"
website: "https://www.coinex.org/"
related: ["[[binance]]", "[[bnb]]", "[[centralized-exchange]]", "[[crypto-markets]]", "[[ethereum]]", "[[exchange-tokens]]"]
---

# CoinEx Token

**CoinEx Token** (CET, on [[ethereum|Ethereum]]) is the native [[exchange-tokens|exchange token]] of **CoinEx**, a global [[centralized-exchange|centralized cryptocurrency exchange]] launched in December 2017. Issued in January 2018, CET originally powered CoinEx Chain (a DEX-focused public chain whose mainnet launched in November 2019) and functions as the utility token of the CoinEx ecosystem — used for trading-fee discounts, ecosystem incentives, and participation in CoinEx platform activities. It is an ERC-20 token, listed in CoinGecko's Exchange-based Tokens and Ethereum Ecosystem categories.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | CET |
| **Price (USD)** | $0.01859 |
| **Market Cap** | $46.47M |
| **Market Cap Rank** | #482 |
| **24h Volume** | $50,751 |
| **24h Change** | -0.13% |
| **7d Change** | -0.33% |
| **Fully Diluted Valuation** | $46.47M |
| **All-Time High** | $0.150293 (2018-07-03), -87.6% |
| **All-Time Low** | $0.004107 (2018-12-15), +352.6% |
| **Categories** | Exchange-based Tokens, Ethereum Ecosystem |

Backdrop: the crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** in an "Established Bear Market." CET's daily turnover (~$51K) is extremely thin relative to its ~$46M cap — a hallmark liquidity risk for second-tier exchange tokens (see [[liquidity]], [[slippage]]). CET is essentially flat over the trailing week, an unusual stillness that reflects how little third-party price discovery the token sees.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.50B CET |
| **Total Supply** | ~2.50B CET |
| **Max Supply** | 10.00B CET |
| **Market Cap / FDV** | ~1.00 |

CET has a maximum supply of 10 billion tokens, of which roughly 2.5 billion (~25%) currently circulate. Because circulating equals total supply in the snapshot, market cap and FDV are aligned — but a large gap remains between circulating and *max* supply, a long-tail dilution consideration. CET's value mechanism is classic **exchange-token fee utility**: holders receive trading-fee discounts on CoinEx, and CET is used across the platform's promotions and ecosystem programs.

CoinEx has historically used token-burn mechanics to manage CET supply over time. Like the broader [[exchange-tokens]] cohort, CET's deflationary lever is meant to come from the exchange recycling a portion of its trading-fee revenue into buying back and burning tokens — the same conceptual model that [[bnb|BNB]] (Binance), OKB and BGB use at much larger scale. Contrast this with pure gas/utility tokens such as [[bitkub-coin|KUB]] whose burn is tied to chain usage rather than exchange revenue. CET's explicit current burn cadence and burn totals should be verified against CoinEx's own disclosures before relying on them.

### Burn / buyback vs peers

| Token | Exchange | Supply mechanic | Tie-in |
|---|---|---|---|
| **CET** | CoinEx | Periodic burns; ~25% of max circulating | Fee discount on CoinEx |
| [[bnb\|BNB]] | Binance | Quarterly auto-burn + real-time BEP-95 burn | Fee discount, BNB Chain gas |
| [[htx-dao\|HTX]] | HTX | 50% of quarterly revenue burned | Sole fee-offset token (25% discount) |
| [[bitmart-token\|BMX]] | BitMart | Buyback-and-burn (revenue-funded) | Fee discount on BitMart |

---

## Market Structure & Derivatives

CET's deepest liquidity is, by design, on the **CoinEx exchange** itself — the venue that issues, burns, and gives utility to the token. This makes **venue concentration the single most important risk**: a token whose primary market is its own issuing exchange has price discovery that is only as healthy as that exchange. The global ~$51K/day volume in the snapshot underscores how shallow third-party liquidity is. No significant regulated [[derivatives]] (perpetuals, funding, open interest) market for CET is listed in the snapshot, so CET effectively trades **spot-only**, concentrated on its home platform. Contract address on Ethereum: `0x081f67afa0ccf8c7b17540767bbe95df2ba8d97f`.

---

## Use Case / Narrative / Category

CET is a **mid-tier exchange utility token** — the same broad category as [[bnb|BNB]] (Binance) but at a far smaller scale and with weaker liquidity. The thesis is straightforward: if CoinEx grows trading volume and users, demand for fee-discounting CET and the burn program should support price; if CoinEx stagnates or faces regulatory/reputational problems, CET is the most direct casualty. It is a leveraged bet on the CoinEx exchange's franchise.

---

## Valuation Framing

Exchange tokens are best understood as **call options on their host exchange's volume and revenue**, not as protocols with independent cash flows. CET has no fee-revenue accrual to holders and no on-chain yield; its only fundamental anchor is (1) the fee discount it confers to CoinEx traders and (2) the size and credibility of CoinEx's revenue-funded burn. A reasonable qualitative valuation lens for CET is therefore:

- **Volume proxy** — does CoinEx spot/derivatives volume justify a ~$46M token cap? At ~$51K/day token turnover, the *token* is far less liquid than the exchange, so any re-rating depends on the exchange, not the token's own float.
- **Burn coverage** — how much CET does revenue actually retire per quarter relative to the ~2.5B circulating? Unverified burn cadence means the deflation thesis cannot be priced with confidence.
- **Peer multiple** — CET trades at a fraction of [[bnb|BNB]]'s or [[htx-dao|HTX]]'s implied volume multiple, which is consistent with CoinEx being a smaller, lower-profile venue. There is no obvious mispricing signal here; the discount reflects franchise scale and liquidity.

This is qualitative framing, not a price target — see valuation.

## Peer Comparison

| Token | Exchange | Mkt-cap rank | Mkt cap | 24h vol | vs ATH | Mcap/FDV |
|---|---|---|---|---|---|---|
| **CET** | CoinEx | #482 | ~$46M | ~$51K | -87.6% | ~1.00 |
| [[bitmart-token\|BMX]] | BitMart | #262 | ~$106M | ~$9.7M | -49.7% | ~0.53 |
| [[htx-dao\|HTX]] | HTX | #53 | ~$1.56B | ~$11.9M | -54.1% | ~0.91 |
| [[bnb\|BNB]] | Binance | top-5 | (mega-cap) | (deep) | — | ~1.00 |

CET is the smallest and least liquid of the listed [[exchange-tokens]] cohort: its daily volume is two-to-three orders of magnitude thinner than BMX or HTX despite a similar single-digit-cent price profile. Among second-tier CEX tokens it is closest in spirit to a "home-venue-only" token.

---

## Notable History

- **Issued:** January 2018; CoinEx Chain mainnet launched November 2019.
- **All-Time High:** $0.1503 (2018-07-03), shortly after launch — CET is currently down roughly 88% from that peak.
- **All-Time Low:** $0.004107 (2018-12-15), during the depths of the 2018 bear market.
- The token has spent most of its life as a small-cap exchange token, tracking CoinEx's fortunes and broad crypto cycles.

> *Notable corporate events (security incidents, regulatory matters, burn announcements) will be added through the wiki's source ingestion workflow as relevant articles are processed. CoinEx has faced security incidents in the past; verify specifics against primary sources before citing.*

---

## Risks

- **Exchange counterparty risk:** CET's value is inseparable from CoinEx's solvency, security, and operations. A hack, insolvency, or major outage at CoinEx would directly impair CET (see [[centralized-exchange]]).
- **Regulatory risk:** CoinEx operates globally and has faced regulatory scrutiny in multiple jurisdictions; enforcement, geo-restrictions, or banking access loss would hit CET hard.
- **Venue concentration / liquidity risk:** primary market is the issuing exchange; ~$51K daily volume means severe [[slippage]] on size.
- **Dilution:** circulating supply is far below the 10B max; future emissions or unlocks are a long-tail overhang, partly offset by burns.
- **Macro / regime risk:** in "extreme fear" (F&G 23) and an established bear market, illiquid small-cap exchange tokens are highly vulnerable.

---

## Reference Data

| Metric | Value |
|---|---|
| **All-Time High** | $0.150293 (2018-07-03) |
| **All-Time Low** | $0.004107 (2018-12-15) |
| **Native Chain** | Ethereum (ERC-20); historically CoinEx Chain |
| **Ethereum Contract** | `0x081f67afa0ccf8c7b17540767bbe95df2ba8d97f` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.coinex.org/](https://www.coinex.org/) |
| **Twitter** | [@coinexcom](https://twitter.com/coinexcom) |
| **Telegram** | [CoinExOfficialEN](https://t.me/CoinExOfficialEN) |
| **GitHub** | [https://github.com/coinexchain/dex-manual](https://github.com/coinexchain/dex-manual) |

---

## Related

- [[exchange-tokens]] — token category
- [[centralized-exchange]] — host venue type
- [[bnb]] — flagship exchange-token peer
- [[binance]] — largest CEX
- [[htx-dao]] — exchange-token peer (HTX)
- [[bitmart-token]] — exchange-token peer (BMX)
- [[bitkub-coin]] — exchange/gas token peer
- [[ethereum]] — host chain
- [[liquidity]] · [[slippage]] · valuation · [[derivatives]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko markets snapshot.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
