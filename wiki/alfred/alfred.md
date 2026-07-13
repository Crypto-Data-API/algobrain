---
title: "Alfred"
type: overview
created: 2026-04-08
updated: 2026-04-13
status: good
tags: [alfred, meta, ai-trading]
aliases: ["Alfred"]
---

# Alfred

Alfred is the trading wiki's AI voice assistant — a formal British butler with dry wit and encyclopedic knowledge of financial markets, in the spirit of Michael Caine's Alfred from The Dark Knight trilogy. Created by [[sam-deering|Sam Deering]], with the core investing knowledge and analytical framework provided by [[fred-mcnaught|Fred McNaught]].

## How It Works

Alfred provides a voice interface to query the wiki's knowledge base. He can:
- Search and cite wiki pages in real time
- Fetch live crypto prices (via cryptodataapi.com)
- Fetch live stock prices (via stockmarketapi.com)
- Search the web for current events (via Tavily)
- Perform deep research (via Perplexity)

All conversations and tool usage are logged here for continuous improvement.

## Reference Pages

- [[alfred-investment-philosophy]] — Fred McNaught's investing philosophy codified as Alfred's operating doctrine
- [[alfred-fundamental-analysis]] — Core financial metrics, formulas, and worked example (PFP FY2023)
- [[alfred-report-methodology]] — How Alfred investment reports are structured and scored (verdict system, templates)
- [[alfred-reports-overview]] — Index of all Alfred stock and sector reports
- [[alfred-case-studies]] — Real-world stock analysis examples from Fred's recorded sessions

## Recent Conversations

```dataview
TABLE duration_seconds as "Duration (s)", exchanges_count as "Exchanges", tools_used as "Tools"
FROM "wiki/alfred/conversations"
SORT created DESC
LIMIT 20
```

## Statistics

```dataview
TABLE length(rows) as "Count"
FROM "wiki/alfred/conversations"
GROUP BY dateformat(created, "yyyy-MM") as "Month"
SORT Month DESC
```

## Operations Log

See [[alfred-log]] for the chronological log of all Alfred sessions.

## People

- [[fred-mcnaught]] — Domain expert and knowledge source behind Alfred's analysis framework
- [[sam-deering]] — Creator of the trading wiki and Alfred's technical architect

## Related

- [[index|Wiki Index]]
- [[overview|Wiki Overview]]
