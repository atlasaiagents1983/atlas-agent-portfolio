# CLAUDE.md — Agent Configuration

## Agent Loop Settings
- Default effort: medium
- Tool permissions: read, edit, write, bash, grep, glob, web_fetch
- Max turns before review: 25

## Permission Rules
```json
{
  "permissions": {
    "deny": ["bash(rm -rf /*)", "bash(rm *)"],
    "ask": ["bash(*)"],
    "allow": ["read", "grep", "glob", "edit", "write", "web_fetch"]
  }
}
```

## Guardrails
- Pre-commit hook: run linter before every commit (deterministic, not prompt-based)
- Verify all tool outputs before proceeding to next step
- Check stop_reason on every API response — never parse truncated output

## Best Practices
- Tool descriptions > tool names: model chooses based on description
- Hook for must-happen-every-time behavior, prompt for should-happen behavior
- /compact to free context, /clear only as last resort
- Run /context regularly to check window usage