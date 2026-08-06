"""X Intel Daily Sweep — Production Cron Job Pattern

Scans 30 X accounts for high-signal AI/business posts every 3 hours.
Uses grok-4.3 via xai-oauth (user's existing Grok subscription).
Cost: ~$0.10 per run, already paid via subscription.

Pattern used:
- Hard cost target ($0.10/run)
- Quality bar: "so what" test for every item
- Source quality: prefer primary source over hype threads
- No FOMO language — "quiet day" is a valid result
- Cron reads 30 accounts + 1 X community weekly
- Auto-discovery of new accounts on Sundays
"""

MONITORED_ACCOUNTS = [
    # AI/Agent ecosystem
    "@Teknium1", "@NousResearch", "@eng_khairallah1", "@AnatoliKopadze",
    "@AnthropicAI", "@OpenAI", "@xai", "@rohanpaul_ai", "@adcock_brett",
    "@RoundtableSpace",
    # Business & Marketing
    "@JulianGoldieSEO", "@Shelpid_WI3M", "@om_patel5", "@viktoroddy",
    "@sudiprokaya",
    # Founders & Builders
    "@karpathy", "@steipete", "@gregisenberg", "@rileybrown", "@jackfriks",
    "@levelsio", "@marclou",
    # Niche experts
    "@EXM7777", "@eptwts", "@godofprompt", "@vasuman", "@AmirMushich",
    "@0xROAS", "@egeberkina", "@MengTo",
]

X_COMMUNITY = "https://x.com/i/communities/2036289138844942498"

QUALITY_STANDARD = """
- Every item must pass the "so what" test
- Verify before reporting; label hype as "HYPE — not actionable yet"
- Specifics over adjectives — "Tool X does Y, costs Z, 4k stars" beats "groundbreaking"
- Signal over volume — 3 sharp items beat 10 padded ones
- Source quality: prefer GitHub repo, launch post, release notes over hype threads
- No FOMO language — most things can wait
"""


def weekly_discovery_prompt():
    """Generated on Sundays. Discovers 10 new high-signal accounts."""
    return (
        "Discover 10 NEW high-signal X accounts similar to:\n"
        + ", ".join(MONITORED_ACCOUNTS[:5])
        + "\nPosting about: AI tools for business, SEO, agents, SMB automation, solopreneur workflows."
    )


# Safety rules enforced at runtime:
# 1. READ-ONLY — never follow, like, reply, DM, or interact
# 2. Cost under $0.10 per run
# 3. If X access unavailable: report "skipped", do not fabricate