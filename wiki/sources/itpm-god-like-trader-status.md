---
title: "How to Achieve God Like Trader Status"
type: source
created: 2026-04-07
updated: 2026-06-12
status: good
tags: [itpm, education, portfolio-theory, risk-management, technical-analysis, fundamental-analysis, options, volatility, stocks]
aliases: ["God Like Trader Status", "ITPM God Like Trader"]
related: ["[[anton-kreil]]", "[[itpm]]", "[[long-short-equity]]", "[[options]]", "[[risk-management-overview]]", "[[implied-volatility]]", "[[calendar-spread]]", "[[tail-risk]]", "[[portfolio-theory]]"]
source_type: video
source_url: "https://www.youtube.com/watch?v=2poH1G7KlJA"
source_author: "Anton Kreil"
source_date: 2023-09-20
source_file: "r2://trader-wiki/transcripts/2023-09-20-how-to-achieve-god-like-trader-status.md"
confidence: medium
claims_count: 35
---

A seminar presented by [[anton-kreil]] in London (September 2023), his first public presentation since summer 2019. The video covers the full ITPM methodology for achieving top-tier trading performance, illustrated with real trade examples from the [[itpm]] Discord community (Society). It walks through portfolio construction, trade types, option structuring, risk management, business statistics, and the path to statistical significance. **Confidence note:** descriptions of the ITPM *methodology* (portfolio structure, option-spread mechanics, risk rules) are faithful summaries of what Kreil teaches and are marked [HIGH] as accurate records of his stated method — not as endorsements that the method is profitable. Self-reported *trade outcomes*, *return targets*, and *student case-study P&L* are marketing claims shown on Kreil's own slides/Discord and are marked [MEDIUM] (unverified, single-source, promotional).

## Key Claims

### Portfolio Construction and Trade Types

1. [HIGH] A model [[long-short-equity]] portfolio consists of 10 positions: 5 longs and 5 shorts, each with equal cash sizing (e.g., $10,000 each on a $100,000 account). (Source: [[anton-kreil]])

2. [HIGH] Long stock positions are replaced with long [[call-options|call options]] and short stock positions are replaced with long [[put-options|put options]], leveraging the [[volatility]] of the portfolio using [[equity-options|equity options]]. (Source: [[anton-kreil]])

3. [HIGH] The portfolio should contain multiple trade types simultaneously: **bread-and-butter trades** (20-60 day time horizon, targeting 15-50% moves), **hedges**, **tail risk trades**, and **pain trades**. (Source: [[anton-kreil]])

4. [HIGH] Net portfolio bias can be adjusted — e.g., 6 shorts and 4 longs when bearish — but hedges must be maintained to protect against being wrong on directional calls. (Source: [[anton-kreil]])

5. [HIGH] **Tail risk trades** involve putting a very small amount of money into a position that could move dramatically (e.g., stock going from $100 to $0). The key is a very low-cost entry for a potentially huge payoff. (Source: [[anton-kreil]])

6. [HIGH] **Pain trades** exploit consensus positioning where fundamentals have changed — you take the opposite side and benefit from maximum pain as the consensus unwinds. (Source: [[anton-kreil]])

### Real Trade Examples

7. [MEDIUM] **TLT Hedge (Nov-Dec 2022)**: A tactical hedge using a [[calendar-spread]] on TLT — buying Jan 2023 $99 strike calls and selling Dec 2022 $100 strike calls on a 2:1 ratio (60 vs 30 contracts). Net spend: $882. Scenario 1 (TLT to 110 before Dec expiry): 3.5:1 return ($31,500). Scenario 2 (credit first, then TLT to 110): 6.5:1 return ($57,000). (Source: [[anton-kreil]], timestamped Discord)

8. [MEDIUM] **Credit Suisse Bankruptcy Trade (Dec 2022 - Mar 2023)**: A tail risk trade structured as a put calendar spread on the ADR. Long June $1.50 puts (400 contracts at $0.15), short March $1.50 puts (200 contracts at $0.05), 2:1 ratio. Net spend: $5,000. The stock collapsed from $3.30 to $0.85-$0.88 when UBS was forced to take over Credit Suisse. Most traders achieved 6:1 to 10:1 returns. (Source: [[anton-kreil]], timestamped Discord)

9. [MEDIUM] **Carvana Pain Trade (May 2023)**: Identified when the stock was ~$15, down 99% from $350. Short interest was 40%+ of float. Fundamentals were turning but market sentiment remained extremely bearish. Traders used turbocharged [[call-options|call option]] structures and exited around $50-55 when the company reported. (Source: [[anton-kreil]], timestamped Discord)

### Option Structuring

10. [HIGH] The primary option structures used are **calendar spreads**: buy a longer-dated option and sell a shorter-dated option, typically on ratios (2:1), aiming to collect a credit on the short leg first. (Source: [[anton-kreil]])

11. [HIGH] In a call spread, sell a higher strike; in a put spread, sell a lower strike. Inversions are possible but rare. Ratios and credits provide the ability to be **agnostic** — making money regardless of when the move happens. (Source: [[anton-kreil]])

12. [HIGH] If the short leg expires worthless (credit collected) and the long leg then moves in your favor, the payoff approximately doubles compared to the immediate-move scenario. (Source: [[anton-kreil]])

### Risk Management

13. [HIGH] **Preventative risk management**: Option structures themselves are part of risk management — knowing all outcomes at every price at every moment means you never need to panic. Position sizing starts at 6-7% net spend per position during mentoring programs. (Source: [[anton-kreil]])

14. [HIGH] **Diversification**: Never put more than 10% of your money in a single position. No YOLO trades. (Source: [[anton-kreil]])

15. [HIGH] **Stagger option expiries**: Cannot have too many options expiring in one month — expiry concentration creates excessive risk. If too many are out of the money at once, the portfolio takes a large hit. (Source: [[anton-kreil]])

16. [HIGH] **Reactive risk management**: How to handle positions that move against you or in your favor — adjusting, rolling, limiting losses. This can only be taught via mentoring, not video series. (Source: [[anton-kreil]])

17. [HIGH] When approaching monthly options expiry (third Friday), plan weeks in advance. The goal is to bank profit at each expiry — "you are not allowed to bank a loss." If a position is winning, book it. If it could go further, book the profit and roll the trade out 3 months. (Source: [[anton-kreil]])

### The Business of Trading

18. [MEDIUM] [[sharp-ratio|Sharpe ratio]] target: minimum 3 when trading options — taking 20% risk to make 60-80% return. (Source: [[anton-kreil]] — vendor performance target, aspirational)

19. [MEDIUM] Anything under $2 million is a "small account." Target returns of 50-100% per year on smaller accounts trading options. (Source: [[anton-kreil]] — vendor performance target)

20. [MEDIUM] Underlying portfolio volatility target: 20-25% annualized. Options leverage this by 3-4x, producing expected returns of 50-100%. (Source: [[anton-kreil]] — vendor performance target)

21. [MEDIUM] Key performance statistics to target: absolute return 50-100%+, win/loss rate 60/40 (ideally 65/35), R-core (dollar winners / dollar losers) minimum 1.5, average days in trade 20-25. (Source: [[anton-kreil]] — vendor performance target)

22. [HIGH] Statistical significance requires a minimum of 150 trades over at least one year. Without this, you cannot claim consistency or "god-like trader status." (Source: [[anton-kreil]] — methodology assertion, consistent with sampling principles)

### The 80/20 Rule

23. [HIGH] Trade ideas must be rooted in [[fundamental-analysis|fundamentals]] with [[technical-analysis]] and price action in the minority — technicals are used only for timing. (Source: [[anton-kreil]])

### Process and Consistency

24. [HIGH] Retail traders are "chaotic" — getting trade ideas from CNBC/Bloomberg paid interviews, Wall Street Bets, copy trading, and confusing trading with investing. Professional traders use a **repeatable, high-quality systematic process**. (Source: [[anton-kreil]])

25. [HIGH] Consistent high-quality input produces consistent high-quality output. The process must be followed without deviation — deviating from the taught process is when performance deteriorates. (Source: [[anton-kreil]])

26. [HIGH] US Stock Market provides the best opportunity set with the most consistent [[volatility]] across all asset classes. (Source: [[anton-kreil]])

27. [HIGH] Trading vs investing distinction: traders operate on 20-60 day time horizons, realize profits regularly, can make money in up/down/sideways markets. Investors hold for years with unrealized (mark-to-market) P&L and suffer periodic 50%+ drawdowns. (Source: [[anton-kreil]])

### Mentoring Case Studies

28. [MEDIUM] **Gunter** (Switzerland): Starting equity $100K, booked $280K winners / $200K losers = $80K net profit (~88% return), 60/40 win rate, 90 trades over ~6 months. Not yet statistically significant. (Source: [[anton-kreil]] — self-reported student case study, unverified, promotional)

29. [MEDIUM] **Phil** (Austria): Starting equity $100K, made $62K over 16 weeks on Thailand mentoring program. (Source: [[anton-kreil]] — self-reported student case study, unverified)

30. [MEDIUM] **Daa** (Belgium): Starting equity $123K, made $72K, 65/35 win rate. Described as having natural talent from day one. (Source: [[anton-kreil]] — self-reported student case study, unverified)

31. [MEDIUM] **Sean** (Florida, USA): Made $140K in 16 weeks on $100K+ account, later reached $188K. Initially made errors from bad habits that had to be corrected through mentoring. (Source: [[anton-kreil]] — self-reported student case study, unverified)

32. [MEDIUM] **Richard**: $80K profit on a $225K account in less than 20 weeks. (Source: [[anton-kreil]] — self-reported student case study, unverified)

### Goldman Sachs Culture

33. [MEDIUM] At Goldman Sachs in the 2000s (pre-Volcker rule), the job of a prop trader was to "bank money every day" — keep the cash register ringing. "You're not allowed to book a loss." This mentality transfers to retail trading. (Source: [[anton-kreil]] — self-reported recollection)

### Macro Framework

34. [MEDIUM] Different business cycles favor different asset classes, but the core methodology of how traders make money has remained the same for decades. (Source: [[anton-kreil]])

35. [MEDIUM] In Q4 2022, Kreil identified that the market bottom in October was being missed by bearish retail and institutional short interest, leading to the TLT hedge strategy and the subsequent pivot to identifying pain trades as the market broadened from Magnificent 7 into other sectors. (Source: [[anton-kreil]] — self-reported, after-the-fact narrative)

## Entities Mentioned

- [[anton-kreil]] — presenter, former Goldman Sachs/Lehman/JP Morgan trader, ITPM founder
- [[itpm]] — Institute of Trading and Portfolio Management
- [[goldman-sachs]] — investment bank where Kreil started in 2000
- [[lehman-brothers]] — investment bank (Kreil moved there 2004)
- [[jp-morgan]] — investment bank
- [[credit-suisse]] — subject of tail risk trade, collapsed March 2023
- [[ubs]] — forced acquirer of Credit Suisse
- [[carvana]] — subject of pain trade, stock recovered from $3.50 area
- [[edward-shek|Edward Shek]] — ITPM senior mentor, introduced Kreil at the seminar

## Concepts Referenced

- [[long-short-equity]], [[calendar-spread]], [[tail-risk]], [[pain-trade]]
- [[options]], [[call-options]], [[put-options]], [[implied-volatility]]
- [[sharp-ratio]], [[risk-management-overview]], [[portfolio-theory]]
- [[fundamental-analysis]], [[technical-analysis]]
- [[equity-curve]], [[compounding]]

## Sources

- Direct presentation by [[anton-kreil]] at ITPM London seminar, September 2023
- Timestamped Discord screenshots from ITPM Society server (Nov 2022 - May 2023)
