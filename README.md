# Atlas AI Agent Portfolio

## Sancar Dumlupinar — AI Agent Engineer

**Fountain Hills, AZ** · sancardumlupinar@hotmail.com · [linkedin.com/in/sancardumlupinar](https://linkedin.com/in/sancardumlupinar)

---

Production AI agent engineer. I build systems that run 24/7 with zero human intervention — not demos, not tutorials. Real clients, real revenue, real automation.

**Hiring manager:** This repo is proof of work. Every file is a piece of a system I designed, deployed, and operate.

---

## What's Here

| File | What It Proves |
|------|---------------|
| `ARCHITECTURE.md` | I design multi-agent systems with routing, fallback chains, and safety rules |
| `config/hermes-config.yaml` | I configure production agent infrastructure (scrubbed of secrets) |
| `cron/x-intel-sweep.py` | I build automated intelligence pipelines that run on schedule |
| `mcp/server-inventory.md` | I integrate 5+ MCP servers for browser, search, docs, and git automation |
| `CLAUDE.md` | I understand agent guardrails, permission models, and context management |

---

## Live Production Systems

### Atlas AI Agents (Jul 2025 — Present)
Deployed AI agent automation for restaurants and clinics:
- **Missed call recovery** — Agent answers, books, and confirms appointments
- **Review monitoring + response** — Cron-based review aggregation and AI-generated replies
- **HR onboarding automation** — New hire paperwork, training scheduling, compliance tracking
- **QuickBooks reporting** — Automated daily/weekly financial summaries
- **Social media scheduling** — Cross-platform content publishing

### Architecture
```
Hermes Agent (orchestrator)
  ├── sub-agents (delegated tasks)
  ├── MCP servers (tools: browser, github, firecrawl, context7, exa)
  ├── cron jobs (scheduled intelligence sweeps)
  └── config.yaml (model routing, fallback chain, safety rules)
```

### Key Design Decisions
- **GPT-5.5 by default**, cheap model fallback chain to avoid surprise bills
- **Sonnet manually invoked only** — never in fallback, never automatic
- **Crons use GPT-5.5** — never Sonnet after a $20 overnight bleed incident
- **READ-ONLY browser rule** — Atlas reads but never interacts on social platforms
- **Snapshot before change** — Every config change is preceded by a backup

---

## Certifications
- **Claude Certified Architect (Foundations)** — In progress
- **AI for Everyone** — deeplearning.ai
- **Google Project Management Certificate**
- **Blockchain Program** — Cornell University

---

## Currently
- Building AI agent systems for SMB clients in Phoenix metro
- Studying for CCA certification (5 domains, 60q, proctored)
- Available for AI Agent Engineer / Forward Deployed Engineer roles — remote or Phoenix