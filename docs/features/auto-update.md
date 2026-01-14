---
layout: default
title: Auto-Update
parent: Features Overview
nav_order: 2
---

# Auto-Update System

Oh-my-claude-sisyphus includes a silent background auto-update system that keeps your installation current without interrupting your workflow.

## Overview

The auto-update system checks for updates at regular intervals and installs them automatically. Updates are rate-limited and concurrent-safe to prevent disruption.

## Features

| Feature | Description |
|---------|-------------|
| **Silent Operation** | Checks run in background, no prompts |
| **Rate-Limited** | Maximum once per 24 hours |
| **Concurrent-Safe** | Lock file prevents conflicts |
| **Cross-Platform** | Works on Windows, macOS, Linux |
| **Manual Control** | `/update` command for immediate check |

## Usage

### Automatic Updates

Updates happen automatically with no action required:

1. Background check runs (max once daily)
2. If update available, downloads and installs
3. Hooks reload on next Claude Code session
4. No restart or interruption

### Manual Update

Force an immediate update check:

```bash
/update
```

**Output:**
```
Checking for updates...
Current version: 2.0.1
Latest version: 2.0.2
Installing update...
Update complete! Changes:
- Fixed keyword detection issue
- Added new explore agent patterns
```

## Configuration

### Disable Auto-Update

**User-level** (`~/.claude/settings.json`):
```json
{
  "auto_update": false
}
```

### Adjust Check Interval

Modify the auto-update hook script:

**Location:** `~/.claude/sisyphus/hooks/auto-update.sh`

```bash
# Default: 86400 seconds (24 hours)
CHECK_INTERVAL=86400

# More frequent (6 hours)
CHECK_INTERVAL=21600

# Less frequent (7 days)
CHECK_INTERVAL=604800
```

## Architecture

```
┌─────────────────────────────────────┐
│     Claude Code Session Start        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Auto-Update Hook Trigger         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Check Lock File                  │
│     ~/.claude/.sisyphus/update.lock  │
└──────────────┬──────────────────────┘
               │
     ┌─────────┴─────────┐
     │                   │
     ▼                   ▼
┌─────────┐       ┌──────────────┐
│ Lock    │       │ No Lock      │
│ Exists  │       │ (Proceed)    │
└────┬────┘       └──────┬───────┘
     │                    │
     ▼                    ▼
┌─────────┐       ┌──────────────────┐
│ Skip    │       │ Check Last Run   │
│ Check   │       │ Timestamp        │
└─────────┘       └─────────┬────────┘
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
          ┌──────────────┐  ┌──────────────┐
          │ Within       │  │ Time to      │
          │ Interval     │  │ Check        │
          └──────┬───────┘  └──────┬───────┘
                 │                 │
                 ▼                 ▼
            ┌─────────┐     ┌──────────────┐
            │ Skip    │     │ Query npm    │
            │ Check   │     │ Registry     │
            └─────────┘     └──────┬───────┘
                                  │
                         ┌────────┴────────┐
                         │                 │
                         ▼                 ▼
                 ┌──────────────┐  ┌──────────────┐
                 │ Update       │  │ No Update    │
                 │ Available    │  │ Available    │
                 └──────┬───────┘  └──────────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Install      │
                 │ Update       │
                 └──────────────┘
```

## State Files

| File | Purpose |
|------|---------|
| `~/.claude/.sisyphus/update.lock` | Prevents concurrent updates |
| `~/.claude/.sisyphus/last-update` | Timestamp of last check |

## Troubleshooting

### Update Not Applying

**Check hook is installed:**
```bash
ls ~/.claude/sisyphus/hooks/auto-update.sh
```

**Verify hook is registered:**
```bash
cat ~/.claude/settings.json | grep auto-update
```

**Manually trigger update:**
```bash
/update
```

### Lock File Stuck

If updates are blocked due to stale lock:

```bash
rm ~/.claude/.sisyphus/update.lock
```

### Check Installed Version

```bash
npm list -g oh-my-claude-sisyphus
# OR
cat ~/.claude/sisyphus/VERSION
```

## Platform Differences

| Platform | Hook Type | Lock Location |
|----------|-----------|---------------|
| **Windows** | Node.js (.mjs) | `%APPDATA%\claude\.sisyphus\` |
| **macOS** | Bash (.sh) | `~/.claude/.sisyphus/` |
| **Linux** | Bash (.sh) | `~/.claude/.sisyphus/` |

## Security Considerations

The auto-update system:

1. Uses official npm registry only
2. Verifies package integrity
3. Requires manual intervention for major version bumps
4. Logs all update activity

## Related Documentation

- [Installation](getting-started/installation.md) - Initial setup
- [Hooks](hooks/) - Hook system architecture
- [Configuration](configuration/reference.md) - Configuration options
