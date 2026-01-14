---
layout: default
title: Background Execution
parent: Features Overview
nav_order: 4
---

# Background Execution

Background execution enables parallel agent spawning and asynchronous task management, allowing complex workflows to complete multiple independent tasks simultaneously.

## Overview

The background execution system manages asynchronous agent delegation, handling concurrency limits, notification delivery, and result aggregation.

## Capabilities

| Feature | Description |
|---------|-------------|
| **Parallel Agents** | Spawn multiple agents simultaneously |
| **Concurrency Limit** | Maximum 5 concurrent background tasks |
| **Notifications** | Desktop alerts when tasks complete |
| **Result Polling** | Automatic result retrieval |
| **Error Handling** | Individual task failure isolation |

## Using Background Execution

### Via Task Tool

Background tasks are spawned using the `run_in_background` parameter:

```javascript
Task(tool="explore", run_in_background=true, task_id="search-1")
Task(tool="librarian", run_in_background=true, task_id="docs-1")
Task(tool="oracle", run_in_background=true, task_id="arch-1")
```

### Via Slash Commands

Some commands automatically use background execution:

```bash
/ultrawork refactor the API layer
# Automatically spawns background agents:
# - frontend-engineer (UI updates)
# - librarian (API docs research)
# - explore (pattern matching)
```

## Concurrency Limits

| Setting | Default | Description |
|---------|---------|-------------|
| **Max Concurrent** | 5 | Maximum background tasks |
| **Queue Size** | Unlimited | Pending tasks when limit reached |

When the limit is reached:
- New tasks queue until slot available
- Priority: FIFO (first-in, first-out)
- Active tasks complete before queued tasks start

## Background Task Types

### Recommended for Background

| Task Type | Example |
|-----------|---------|
| **File searches** | `explore` finding all usages |
| **Documentation** | `librarian` researching APIs |
| **LSP operations** | `lsp_workspace_symbols` across large codebase |
| **AST searches** | `ast_grep_search` for patterns |
| **Web fetching** | `webReader` for external docs |

### Not Recommended for Background

| Task Type | Reason |
|-----------|--------|
| **File edits** | Should see results immediately |
| **Build commands** | Need to monitor output |
| **Tests** | Require immediate attention to failures |
| **Git operations** | State changes need verification |

## Notification System

Background tasks trigger notifications when complete:

**macOS:**
```bash
# Native notification center
📬 "Background task 'search-1' complete"
```

**Linux:**
```bash
# libnotify / notify-send
📬 "Background task 'search-1' complete"
```

**Windows:**
```bash
# Windows notification system
📬 "Background task 'search-1' complete"
```

**Disable Notifications:**
```json
// ~/.claude/settings.json
{
  "background_notifications": false
}
```

## Result Retrieval

### Polling for Results

Results are automatically polled when available:

```javascript
// Background task completes
// System automatically retrieves results
// Results available via TaskOutput
```

### Manual Result Check

Use task_id to retrieve results:

```javascript
TaskOutput(task_id="search-1")
```

## State Management

Background task state is tracked in:

**Location:** `~/.claude/.sisyphus/background-tasks/`

**Files:**
```
background-tasks/
├── active.json          # Currently running tasks
├── completed.json       # Finished tasks (results)
└── failed.json          # Failed tasks (errors)
```

**State Transition:**
```
pending → running → completed
                     ↘ failed
```

## Error Handling

Individual task failures don't stop other tasks:

```javascript
// Task 1 fails
TaskOutput(task_id="search-1")
// { status: "failed", error: "..." }

// Task 2 succeeds independently
TaskOutput(task_id="docs-1")
// { status: "completed", result: "..." }
```

**Error Information:**
- Task ID preserved
- Error message captured
- No retry (manual relaunch required)

## Ultrawork Background Pattern

Ultrawork mode uses aggressive background execution:

```
┌─────────────────────────────────────────┐
│         Ultrawork Activation             │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
┌─────────────┐  ┌─────────────┐
│ Foreground  │  │ Background  │
│ Primary     │  │ Agents      │
│ Work        │  │             │
└─────────────┘  └─────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│ Librarian │ │ Explore   │ │ Frontend  │
│ (docs)    │ │ (search)  │ │ (UI)      │
└───────────┘ └───────────┘ └───────────┘
```

**Background Tasks in Ultrawork:**
1. `librarian` - Documentation research
2. `explore` - Multiple pattern searches
3. `frontend-engineer` - Parallel UI development

## Platform Differences

| Platform | Implementation | Limit |
|----------|---------------|-------|
| **Windows** | Node.js child_process | 5 |
| **macOS** | Bash background jobs | 5 |
| **Linux** | Bash background jobs | 5 |

## Configuration

### Adjust Concurrency Limit

**Via settings:**
```json
// ~/.claude/settings.json
{
  "sisyphus": {
    "max_background_tasks": 10
  }
}
```

### Disable Background Execution

```json
// ~/.claude/settings.json
{
  "sisyphus": {
    "background_execution": false
  }
}
```

## Troubleshooting

### Tasks Not Starting

**Check active task count:**
```bash
cat ~/.claude/.sisyphus/background-tasks/active.json
```

**Wait for slot or reduce concurrency:**
```bash
# Kill stuck tasks
rm ~/.claude/.sisyphus/background-tasks/active.json
```

### Notifications Not Appearing

**macOS:**
```bash
# Check notification permissions
# System Settings → Notifications → Terminal
```

**Linux:**
```bash
# Install notify-send
sudo apt install libnotify-bin
```

### Stale Task State

**Clear background state:**
```bash
rm -rf ~/.claude/.sisyphus/background-tasks/
```

## Best Practices

1. **Identify Independent Tasks** - Only parallelize truly independent work
2. **Use Descriptive Task IDs** - `task_id="search-auth-patterns"` not `task_id="t1"`
3. **Monitor Completion** - Check `TaskOutput` before using results
4. **Handle Failures** - Don't assume all background tasks succeed
5. **Respect Limits** - Don't spawn more than 5 parallel tasks

## Related Documentation

- [Magic Keywords](magic-keywords/) - Ultrawork activation
- [Commands](commands/reference.md) - Slash commands using background
- [Hooks](hooks/) - Background notification hook
