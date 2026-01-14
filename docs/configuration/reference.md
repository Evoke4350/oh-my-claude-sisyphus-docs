---
layout: default
title: Configuration Reference
parent: Configuration Reference
nav_order: 1
---

# Configuration Reference

Complete reference for all oh-my-claude-sisyphus configuration options.

## Configuration Files

### User-Level Configuration

**Location:** `~/.claude/settings.json`

Applies to all Claude Code sessions globally.

### Project-Level Configuration

**Location:** `.claude/settings.json` (project root)

Overrides user-level settings for the current project.

### Priority Order

1. Project `.claude/settings.json` (highest)
2. User `~/.claude/settings.json` (fallback)

## Configuration Schema

### Root Schema

```json
{
  "$schema": "./assets/oh-my-claude-sisyphus.schema.json",
  "auto_update": true | false,
  "background_notifications": true | false,
  "sisyphus": {
    "max_background_tasks": 5,
    "background_execution": true,
    "todo_enforcement": true
  },
  "agents": {
    "<agent-name>": {
      "model": "opus" | "sonnet" | "haiku",
      "enabled": true | false,
      "prompt_append": "Additional instructions..."
    }
  },
  "hooks": {
    "<event-name>": [
      "~/.claude/sisyphus/hooks/<hook-name>.sh"
    ]
  },
  "skills": {
    "<skill-name>": {
      "enabled": true | false
    }
  }
}
```

## Configuration Options

### Auto-Update

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `auto_update` | `boolean` | `true` | Enable automatic update checks |

**Example:**
```json
{
  "auto_update": true
}
```

### Background Notifications

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `background_notifications` | `boolean` | `true` | Enable desktop notifications |

**Example:**
```json
{
  "background_notifications": true
}
```

### Sisyphus Settings

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `max_background_tasks` | `number` | `5` | Maximum concurrent background tasks |
| `background_execution` | `boolean` | `true` | Enable background task execution |
| `todo_enforcement` | `boolean` | `true` | Require all todos to complete |

**Example:**
```json
{
  "sisyphus": {
    "max_background_tasks": 10,
    "background_execution": true,
    "todo_enforcement": true
  }
}
```

## Agent Configuration

### Agent Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `model` | `string` | Varies | Model: `opus`, `sonnet`, `haiku` |
| `enabled` | `boolean` | `true` | Agent availability |
| `prompt_append` | `string` | `null` | Additional system prompt text |
| `description` | `string` | Varies | Agent description |
| `tools` | `string[]` | All | Allowed tools |

### Available Agents

| Agent | Default Model | Purpose |
|-------|---------------|---------|
| `oracle` | `opus` | Architecture, debugging |
| `librarian` | `sonnet` | Documentation, research |
| `explore` | `haiku` | Fast codebase search |
| `sisyphus-junior` | `sonnet` | Focused execution |
| `frontend-engineer` | `sonnet` | UI/UX work |
| `document-writer` | `haiku` | Technical docs |
| `multimodal-looker` | `sonnet` | Visual analysis |
| `momus` | `opus` | Plan review |
| `metis` | `opus` | Pre-planning |
| `prometheus` | `opus` | Strategic planning |
| `qa-tester` | `sonnet` | CLI/service testing |

### Agent Configuration Example

```json
{
  "agents": {
    "oracle": {
      "model": "opus",
      "enabled": true,
      "prompt_append": "Always consider security implications."
    },
    "explore": {
      "model": "haiku",
      "enabled": true
    },
    "document-writer": {
      "enabled": false
    }
  }
}
```

## Hooks Configuration

### Hook Events

| Event | Description |
|-------|-------------|
| `UserPromptSubmit` | Before prompt is processed |
| `PreToolUse` | Before tool execution |
| `PostToolUse` | After tool execution |
| `Stop` | When user attempts to stop |

### Hook Format

```json
{
  "hooks": {
    "UserPromptSubmit": [
      "~/.claude/sisyphus/hooks/keyword-detector.sh",
      "~/.claude/sisyphus/hooks/auto-slash-command.sh"
    ],
    "PostToolUse": [
      "~/.claude/sisyphus/hooks/rules-injector.sh"
    ],
    "Stop": [
      "~/.claude/sisyphus/hooks/todo-continuation.sh",
      "~/.claude/sisyphus/hooks/ralph-loop.sh"
    ]
  }
}
```

### Available Hooks

| Hook | Event | Purpose |
|------|-------|---------|
| `keyword-detector` | UserPromptSubmit | Magic keyword detection |
| `auto-slash-command` | UserPromptSubmit | Slash command expansion |
| `rules-injector` | PostToolUse | Rule file injection |
| `sisyphus-orchestrator` | PreToolUse, PostToolUse | Delegation enforcement |
| `todo-continuation` | Stop | Task completion enforcement |
| `ralph-loop` | Stop | Self-referential loop |
| `edit-error-recovery` | PostToolUse | Edit failure recovery |
| `think-mode` | UserPromptSubmit | Extended thinking |

## Skills Configuration

### Skill Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `enabled` | `boolean` | `true` | Skill availability |

### Available Skills

| Skill | Purpose |
|-------|---------|
| `sisyphus` | Multi-agent orchestration |
| `orchestrator` | Complex task coordination |
| `ultrawork` | Maximum performance mode |
| `ralph-loop` | Self-referential completion loop |
| `frontend-ui-ux` | UI/UX design expertise |
| `git-master` | Git workflow expertise |

### Skills Configuration Example

```json
{
  "skills": {
    "ultrawork": {
      "enabled": true
    },
    "git-master": {
      "enabled": false
    }
  }
}
```

## Complete Example

### Minimal Configuration

```json
{
  "auto_update": true
}
```

### Typical Configuration

```json
{
  "$schema": "./assets/oh-my-claude-sisyphus.schema.json",
  "auto_update": true,
  "background_notifications": true,
  "sisyphus": {
    "max_background_tasks": 5,
    "background_execution": true,
    "todo_enforcement": true
  },
  "agents": {
    "oracle": {
      "model": "opus"
    },
    "explore": {
      "model": "haiku"
    }
  },
  "hooks": {
    "UserPromptSubmit": [
      "~/.claude/sisyphus/hooks/keyword-detector.sh"
    ],
    "Stop": [
      "~/.claude/sisyphus/hooks/todo-continuation.sh"
    ]
  }
}
```

## IDE Support

### JSON Schema

Configuration files can reference the JSON schema for autocomplete and validation:

```json
{
  "$schema": "./assets/oh-my-claude-sisyphus.schema.json"
}
```

**Schema location:** `~/.claude/sisyphus/assets/oh-my-claude-sisyphus.schema.json`

### Validation

The schema provides:
- Property autocomplete
- Type checking
- Enum validation (agents, hooks, skills)
- Default value hints

## Related Documentation

- [Agent Customization](agent-customization.md) - Editing agent definitions
- [Project Configuration](project-config.md) - CLAUDE.md setup
- [Migration Guide](migration.md) - From oh-my-opencode
