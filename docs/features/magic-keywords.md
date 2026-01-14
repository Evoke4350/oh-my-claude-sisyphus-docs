---
layout: default
title: Magic Keywords
parent: Features
nav_order: 1
---

# Magic Keywords

Magic keywords enable special modes without explicit slash commands. Simply include these keywords anywhere in your prompt to activate enhanced orchestration behaviors.

## Overview

The keyword detector analyzes user prompts before Sisyphus processing, identifying trigger words that indicate intent and required optimization strategy. Detection occurs at the request ingestion phase.

## Available Keywords

| Keyword | Effect | Aliases |
|---------|--------|---------|
| **ultrawork** | Maximum parallel execution mode | `ulw`, `uw` |
| **search** | Enhanced search mode | `find`, `locate` |
| **analyze** | Deep analysis mode | `investigate` |

## Detection Flow

```
User Prompt
    │
    ▼
Keyword Detection
    │
    ├── ultrawork detected? ──► Parallel Agent Orchestration
    ├── search detected? ─────► Enhanced Search Mode
    ├── analyze detected? ────► Deep Analysis Mode
    └── none? ────────────────► Standard Mode
```

## Ultrawork Mode

### Activation Keywords

- `ultrawork`
- `ulw`
- `uw`

### Behavior Changes

| Aspect | Standard | Ultrawork |
|--------|----------|-----------|
| Agent Delegation | On-demand | Aggressive parallel |
| Background Tasks | Conservative | Extensive |
| Thinking Budget | Default | Extended |
| Exploration | Single angle | Multi-angle |
| Risk Tolerance | Measured | Higher |

### Examples

```bash
# Explicit keyword usage
ultrawork implement user authentication system

# Prefix style
ulw: refactor the API layer

# Inline style
Add a dashboard with charts (uw) for the analytics

# Combined with task
uw implement dark mode across all components
```

### Parallel Execution Pattern

When ultrawork is detected:

1. Frontend and backend work proceed in parallel
2. Multiple explore agents search different patterns simultaneously
3. Librarian research runs in background
4. Background notifications track completion

---

## Search Mode

### Activation Keywords

- `search`
- `find`
- `locate`

### Behavior Changes

| Aspect | Standard | Search Mode |
|--------|----------|-------------|
| Search Scope | Single tool | All search tools |
| Execution | Sequential | Parallel |
| Citation | Optional | Required |
| Sources | Local only | Local + external |

### Examples

```bash
# Direct search
find all files that import the utils module

# Search request
search for API endpoints handling user data

# Locate usage
locate all instances of deprecated functions

# Combined with context
search the codebase for authentication patterns
```

### Search Strategy

Parallel search agents access all available tools:

| Agent | Tools | Output |
|-------|-------|--------|
| **Librarian** | context7, websearch_exa, grep_app | External docs, web results |
| **Explore** | LSP symbols, AST-grep, grep_app | File paths, line numbers |

---

## Analyze Mode

### Activation Keywords

- `analyze`
- `investigate`

### Behavior Changes

| Aspect | Standard | Analyze Mode |
|--------|----------|--------------|
| Thinking Budget | Default | Extended |
| Oracle | On failure | Proactive |
| Expert Mode | Background | Blocking |
| Evidence | Optional | Required |

### Examples

```bash
# Analysis request
analyze performance bottleneck in database queries

# Investigation
investigate why tests are failing in CI

# Deep dive
analyze the authentication flow for security issues

# Root cause
investigate memory leak in worker process
```

### Analysis Workflow

1. **Problem Decomposition** - Identify unknowns and scope
2. **Expert Consultation** - Oracle, Librarian, Explore (blocking)
3. **Synthesis** - Cross-validate findings
4. **Recommendation** - Proposed solutions with trade-offs

---

## Keyword Precedence

When multiple keywords appear in a prompt:

1. **Ultrawork** (highest priority)
2. **Analyze** (medium priority)
3. **Search** (lowest priority)

Example:
```bash
# This activates ultrawork mode only
ultrawork: analyze the codebase and find all bugs

# Search and analyze keywords ignored
```

---

## Multi-Language Support

Keywords work across multiple languages:

| Keyword | English | Korean | Japanese |
|---------|---------|--------|----------|
| **Ultrawork** | `ultrawork`, `ulw`, `uw` | - | - |
| **Search** | `search`, `find` | `찾아` | `検索` |
| **Analyze** | `analyze`, `investigate` | `분석` | `調査` |

---

## Disabling Keyword Detection

To disable the keyword detector, modify your configuration:

**User-level** (`~/.claude/settings.json`):
```json
{
  "hooks": {
    "UserPromptSubmit": []
  }
}
```

**Project-level** (`.claude/settings.json`):
```json
{
  "hooks": {
    "UserPromptSubmit": []
  }
}
```

---

## Slash Commands vs Keywords

| Aspect | Slash Command | Magic Keyword |
|--------|---------------|---------------|
| Activation | Explicit `/command` | Keyword in prompt |
| Priority | Always wins | Secondary |
| Visibility | Clear in history | Implicit |
| Use Case | Intentional mode | Natural workflow |

**Recommended:** Use slash commands for deliberate mode selection, keywords for natural conversation flow.

---

## Related Documentation

- [Commands Overview](commands/overview.md) - Slash command reference
- [Command Reference](commands/reference.md) - Detailed command docs
- [Hooks](hooks/) - Keyword detector implementation
