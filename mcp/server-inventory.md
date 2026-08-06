# MCP Server Inventory — Atlas Production Toolset

## Overview

Atlas uses 5 Model Context Protocol (MCP) servers that extend Hermes Agent with real capabilities — browser automation, GitHub operations, web scraping, documentation retrieval, and neural search.

All servers run via `npx` (Node.js package runner) and are defined in `config/hermes-config.yaml`.

---

## 1. Playwright MCP — Browser Automation

**Tools:** 24 (navigate, click, type, screenshot, network, fill forms, evaluate JS)

**Purpose:** Full browser control — Atlas can interact with web pages like a human instead of just reading HTML.

**Production use cases:**
- Navigate to competitor websites and extract pricing/features
- Verify client web presence across platforms
- Fill and submit forms (job applications, client onboarding)
- Monitor live dashboard data

**Example:**
```python
# Atlas commands the browser to navigate, click, and extract data
# 24 tools handle everything from navigation to network request inspection
```

**Cost:** Free (no API key required)

---

## 2. GitHub MCP — Repository Management

**Tools:** 26 (repos, issues, PRs, commits, search, branches, reviews)

**Purpose:** Atlas can read, create, and manage GitHub repositories without leaving the agent loop.

**Production use cases:**
- Create issues and PRs directly from agent conversations
- Read repository code for analysis or troubleshooting
- Search code across repos for patterns or vulnerabilities
- Manage branches and review PRs

**Example:**
```python
# Atlas creates an issue, pushes code, opens a PR, and requests review
# All from within the agent — no context switching to browser
```

**Auth:** GitHub personal access token (connected to `atlasaiagents1983` account)

---

## 3. Firecrawl MCP — Web Scraping & Crawling

**Tools:** 25 (scrape, crawl, search, extract, map, monitor, parse)

**Purpose:** Extract clean content from any website — full crawls, structured data extraction, and change monitoring.

**Production use cases:**
- Scrape lead data from directories
- Crawl competitor sites for market research
- Extract structured data (pricing, features, team info) with JSON schema
- Monitor competitor websites for changes

**Example:**
```python
# Firecrawl extracts structured data from competitor sites
# Schema: { "pricing": "...", "features": ["..."], "team_size": N }
```

**Cost:** Free tier (500 credits/month)

---

## 4. Context7 MCP — Documentation Retrieval

**Tools:** 2 (resolve library ID, query docs)

**Purpose:** Inject real, version-specific library documentation into agent context. Stops code hallucinations.

**Production use cases:**
- Query exact API signatures for any library
- Get version-specific code examples
- Reduce hallucinated APIs by verifying against real docs

**Example:**
```python
# Before writing code with a library:
context7.resolve_library_id("Next.js", "How to use server actions")
context7.query_docs("/vercel/next.js", "server actions with form")
# Now the code uses real, current API signatures
```

**Auth:** Context7 API key (free tier: 1,000 queries/month)

---

## 5. Exa MCP — Neural Search

**Tools:** 2 (web search, web fetch)

**Purpose:** Semantic web search — understands intent, not just keywords. Better than Google for finding people, companies, and niche content.

**Production use cases:**
- Find hiring managers and decision makers
- Search for specific company information
- Retrieve clean page content without ads/modals

**Example:**
```python
# Exa understands: "find SaaS companies hiring remote CSMs in Phoenix"
# Returns semantically relevant results, not just keyword matches
```

**Auth:** Exa API key (free tier: 1,000 searches/month, 150 unauthenticated/day)

---

## Architecture Pattern

```
User Request
     │
     ▼
Hermes Agent (orchestrator)
     │
     ├── Playwright → "Navigate to page, click button, extract data"
     ├── GitHub     → "Push code, create PR, review changes"
     ├── Firecrawl  → "Crawl competitor site, extract pricing"
     ├── Context7   → "Query React 19 API docs before writing code"
     └── Exa        → "Find companies hiring for X role"
```

Each server is independently enabled/disabled in config. This keeps the toolset modular — add or remove servers without affecting the rest of the system.