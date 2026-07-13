# Alfred

A voice + chat AI trading assistant, built on top of a persistent, compounding **trading wiki** — crypto, stocks, strategies, history, AI trading, market events, and more.

Two things live in this repo:

1. **The wiki** (`wiki/`) — a structured, interlinked markdown knowledge base maintained by an LLM agent (Claude Code) following the [LLM Wiki](https://github.com/tobi/llm-wiki) pattern. You feed it raw sources; it compiles them into durable, cross-referenced pages.
2. **Alfred** (`app/`) — a FastAPI service that answers trading questions over voice, chat, REST, and MCP, grounding its answers in the wiki plus live market-data tools. Deployed to Google Cloud Run.

## How It Works

You provide raw sources (articles, PDFs, videos, tweets, data files). The LLM reads them, extracts key information, and incrementally builds the wiki of interlinked markdown pages. Knowledge is compiled once and kept current — not re-derived on every query.

Alfred then sits in front of that knowledge base. Ask it a question by voice or text and it synthesises an answer from the wiki, live market data (crypto/stock prices, fundamentals, SEC filings, web/Perplexity search), conversation memory, and the LLM's own reasoning.

## Architecture

```
Cloudflare R2 (r2://trader-wiki/)  → Immutable source documents. The LLM reads but never modifies these.
wiki/                              → LLM-generated knowledge base (summaries, entities, concepts, strategies)
app/                               → Alfred FastAPI service (dashboard, chat, voice, REST API, MCP server)
tools/                             → Wiki CLI: ingest, search, lint, gap-finder, R2 sync, MCP server, converters
deploy/                            → GCP provisioning + smoke tests (Cloud Run, Vertex, Chroma VM)
docs/                              → Deployment plan and design docs
templates/                         → Page templates for consistent structure
CLAUDE.md                          → Schema governing LLM wiki behaviour and conventions
```

> `raw/` is a **local cache** (gitignored). Raw sources live in Cloudflare R2 and are fetched on demand with `python tools/raw_sync.py`. The master index is `wiki/sources/raw-source-index.md`.

## Alfred (the app)

`app/server.py` is a FastAPI server exposing:

| Surface | Endpoint | Notes |
|---------|----------|-------|
| Dashboard | `/dashboard` | Wiki graph view, feed, live activity (React/PixiJS) |
| Chat / voice UI | `/` | Browser chat + push-to-talk voice |
| Voice WebSocket | `/ws/voice` | Bidirectional STT → LLM + tools → TTS |
| Activity feed | `/ws/feed` | Live tail of wiki/log activity |
| Ask (REST) | `POST /api/chat` | `{message, history?}` → `{answer, tools, links, charts}` — full Alfred answer (costs a little) |
| Search (REST) | `GET /api/search` | In-memory BM25 wiki search (free, no LLM) |
| Read page | `GET /api/page/{name}` | Raw wiki page markdown |
| Remote MCP | `/mcp/` | Streamable HTTP; partner-safe tools `ask_alfred`, `search_wiki`, `read_wiki_page` |
| Graph / render / stats | `/api/graph`, `/api/render/{slug}`, `/api/stats` | Dashboard data |

**LLM providers** (`LLM_PROVIDER` in `app/config.py`): `gemini` (Gemini via Vertex AI — default, GCP-credit paid), `vertex` (Claude via Vertex, fallback if quota granted), `anthropic`, `openai`, `groq`.

**Voice:** STT via Deepgram; TTS via `edge` (free, default in cloud), `piper` (local, fastest), or `elevenlabs` (paid).

**Memory:** durable conversation memory in ChromaDB (local `PersistentClient`, or a remote Chroma server via `CHROMA_HOST`); MemPalace store for structured recall.

**Built-in data tools** (`app/tools/`): crypto prices, stock info, charts, SEC filing summaries, fundamental reports, Tavily web search, Perplexity research, FX cache.

**Auth** (`app/config.py`): unset = open (local dev). Set `ALFRED_AUTH_TOKEN` for the owner/dashboard cookie login (`/login`), and `ALFRED_API_TOKENS` (`label:token,label:token`) for partner API/MCP access via `Authorization: Bearer <token>` or `X-API-Key`.

### Run Alfred locally

```bash
pip install -r app/requirements.txt
cd app && python server.py          # serves http://localhost:8000
# Dashboard: http://localhost:8000/dashboard
```

Configure keys via `app/.env` (falls back to a parent `.env` for shared keys). See `app/config.py` for all variables.

## Deployment (Google Cloud Run)

Alfred is **live** on Cloud Run (project `venture-472911`, region `us-central1`), with:

- **Inference:** Gemini 2.5 Flash via Vertex AI (authenticated by the service account / ADC — no API key needed). Claude-on-Vertex stays wired as a fallback pending partner-model quota.
- **State:** wiki, reports, and graph cache on a GCS bucket mounted via GCS-FUSE; conversation memory on a Chroma server running on a micro Compute Engine VM (reached over Direct VPC egress).
- **Flags that matter:** `--no-cpu-throttling --min-instances 1` (background threads: graph build, feed loop, file watcher) and `--session-affinity` (voice/feed WebSockets).

Provisioning is idempotent in `deploy/provision.sh`; the full plan and credit coverage are in `docs/gcp-deployment-plan.md`. Smoke tests: `deploy/gemini_provider_test.py`, `deploy/vertex_smoke_test.py`.

> Deploy from **PowerShell, not Git Bash** (MSYS mangles `/data` mount paths). Deploys are **manual** from the local working tree (`gcloud run deploy --source app`), not wired to git.

### Tests

End-to-end tests in `tests/` exercise the deployed API:

```bash
ALFRED_AUTH_TOKEN=<token> pytest tests/ -v
# test_wiki_api.py = free; test_chat_api.py + test_mcp_api.py = small LLM cost
# target a remote deploy via ALFRED_BASE_URL / ALFRED_MCP_URL
```

## Maintaining the Wiki

The wiki is maintained by an LLM agent per the schema in `CLAUDE.md`. Key CLI helpers:

### Ingest a source
```bash
python tools/ingest.py article "https://example.com/article" "Article Title"
python tools/raw_sync.py upload raw/articles/2026-04-06-article-title.md   # → Cloudflare R2
# Then ask Claude: "Ingest source 2026-04-06-article-title"
```

### Search the wiki
```bash
python tools/search.py "bitcoin etf"
python tools/search.py --tag crypto --type concept
```

### Gap analysis (find & fill missing coverage)
```bash
python tools/gap_finder.py --topic "options trading" --deep   # Perplexity deep research (~$1)
python tools/gap_finder.py --topic "options trading"          # standard (~$0.03)
python tools/gap_finder.py --topic "options trading" --internal-only   # free
```

### Lint the wiki
```bash
python tools/lint.py
```

### Convert sources
```bash
python tools/pdf_to_markdown.py <path>   # PDFs (OpenDataLoader — preserves tables/headings)
python tools/convert.py <path>           # everything else (.docx, .pptx, .xlsx — MarkItDown)
```

### Wiki MCP server (local)
Exposes the wiki to Claude Code as MCP tools:
```bash
python tools/mcp_server.py
```
```json
{
  "mcpServers": {
    "trading-wiki": {
      "command": "python",
      "args": ["C:/websites/VENTURE/alfred/tools/mcp_server.py"]
    }
  }
}
```

## Wiki Categories

| Category | Description |
|----------|-------------|
| **Markets** | Crypto, Stocks, Forex, Commodities, Options, Futures, Bonds |
| **Strategies** | Technical, Fundamental, Quantitative, Algorithmic, Day/Swing/Position Trading + regime matrix & live journal |
| **Strategy development** | Methodology for *producing* strategies — edge taxonomy, hypothesis workflow, overfitting detection, failure modes |
| **Concepts** | Risk Management, Portfolio Theory, Market Microstructure, Indicators, Behavioral Finance, Backtesting, Anomalies |
| **Data sources** | Free, paid, alternative, crypto, options, macro, news data providers |
| **History** | Crashes, Bull/Bear Markets, Notable Trades, Market Evolution |
| **Entities** | Traders, Hedge Funds, Exchanges, Regulators, DeFi Protocols, Companies |
| **AI Trading** | ML Models, Trading Bots, Backtesting, AI infrastructure |
| **News** | Verified market-moving events with documented impact |
| **Education** | Books, Courses, Resources |

## Editing the wiki in Obsidian

The `wiki/` folder is an Obsidian vault. Recommended plugins: Dataview, Templater, Obsidian Git, Marp Slides (`.obsidian/community-plugins.json`).

## License

Private knowledge base and application. Not for redistribution.
