# Atlas Multi-Agent System Architecture

## Overview

Atlas is a production multi-agent system running on **Hermes Agent (v0.19.0 Quicksilver)**. It operates 24/7 via cron jobs, scheduled intelligence sweeps, and on-demand client automation.

```
                    ┌─────────────────────────┐
                    │    Hermes Agent Core     │
                    │  (atlas-business profile)│
                    └──────────┬──────────────┘
                               │
               ┌───────────────┼───────────────────┐
               │               │                    │
        ┌──────▼──────┐  ┌────▼────┐  ┌───────────▼──┐
        │   Cron Jobs  │  │  Agent  │  │    MCP       │
        │  (scheduled) │  │  Loop   │  │   Servers    │
        └──────┬──────┘  └────┬────┘  └───────┬──────┘
               │               │               │
               ▼               ▼               ▼
     ┌─────────────────┐ ┌─────────┐ ┌─────────────────┐
     │ X Intel Sweep   │ │ Sub-    │ │ Playwright      │
     │ Business Learn  │ │ agents  │ │ GitHub          │
     │ Job Hunt Scan   │ │         │ │ Firecrawl       │
     │ ...             │ │         │ │ Context7        │
     └─────────────────┘ └─────────┘ │ Exa             │
                                      └─────────────────┘
```

## Model Routing

```
Default:      GPT-5.5 (OpenAI Codex)
Fallback:     DeepSeek V4 Flash → Gemini 3.1 Flash Lite → GPT-4.1 Mini
Manual only:  Claude Sonnet 4.6 (client-facing work)
  /model:     Claude Opus 4.7 (high-stakes reasoning)
Cron jobs:    GPT-5.5 by default (never Sonnet — $20 bleed incident 2026-04)
```

**Design rationale:** The fallback chain is cheap models only. Sonnet and Opus never enter automatic routing. This prevents bill shock while maintaining capability.

## Cron Job Pipeline

| Job | Schedule | Purpose | Model |
|-----|----------|---------|-------|
| X Intel Daily | Every 3h | Monitor 30 AI/business accounts for signal | grok-4.3 |
| Atlas Learning Loop | Daily 4am | Research SMB marketing, AI case studies | GPT-5.5 |
| AZ Sports Licensing | Weekly | Monitor AZ sports/event licensing | GPT-5.5 |
| Job Hunt X Scan | Every 6h | Search X for real remote job postings | grok-4.3 |

## Security & Safety Rules

1. **READ-ONLY on social platforms** — Atlas monitors X but never posts, likes, follows, or DMs
2. **READ-ONLY on GHL** — Atlas reads client data but never edits contacts, changes settings, or modifies widgets without per-action approval
3. **Snapshot before change** — Every config change is preceded by a backup of the current state
4. **EXISTS/DIFFERENT/MISSING reconciliation** — Before edits, verify what exists, what changed, and what's missing
5. **Cross-profile write guard** — Tool refuses to modify another Hermes profile without explicit user direction

## Sub-Agent Architecture

Sub-agents (via `delegate_task`) handle parallel workstreams:

```
Parent Agent (Hermes)
  ├── sub-agent 1: Research client, gather data
  ├── sub-agent 2: Generate report, compile findings
  └── sub-agent 3: Verify results, cross-reference
```

Limits: max 3 concurrent sub-agents, max spawn depth 1 (no nested delegation).

## MCP Server Toolset

| Server | Tools | Purpose |
|--------|-------|---------|
| Playwright | 24 | Browser automation, web interaction, scraping |
| GitHub | 26 | Repo management, PRs, issues, code search |
| Firecrawl | 25 | Web scraping, crawl, structured extraction |
| Context7 | 2 | Library documentation, code reference |
| Exa | 2 | Neural web search, content retrieval |

## Key Files

| Path | Purpose |
|------|---------|
| `~/.hermes/profiles/atlas-business/config.yaml` | Hermes configuration, model routing, MCP servers |
| `~/.hermes/profiles/atlas-business/cron/` | Cron job definitions and state |
| `~/.hermes/profiles/atlas-business/skills/` | Skill library (35+ skills) |
| `~/.hermes/profiles/atlas-business/memories/` | Persistent memory and user profile |

## Version History

- **Hermes v0.19.0 Quicksilver** — Current
- **Profile:** atlas-business (default), ai-opportunity (secondary)
- **Tool limit:** 80 tools per session
- **Plugin:** hermes-lcm (low cost mode)