---
layout: default
title: Migration Guide
parent: Configuration Reference
nav_order: 4
---

# Migration Guide

Guide for migrating from oh-my-opencode to oh-my-claude-sisyphus.

## Overview

Oh-my-claude-sisyphus is a port of oh-my-opencode adapted for Claude Code's native agent system. This guide helps you transition.

## Key Differences

### Architecture

| Aspect | oh-my-opencode | oh-my-claude-sisyphus |
|--------|---------------|----------------------|
| Runtime | Bun | Node.js |
| Plugin System | OpenCode | Claude Code |
| Master Agent | Swappable | Skills-based |
| Models | Multi-provider | Claude-only |
| Agents | TypeScript config | Markdown files |
| Hooks | JavaScript | Shell scripts |

### Model Mapping

| Agent | oh-my-opencode | oh-my-claude-sisyphus |
|-------|---------------|----------------------|
| Oracle | GPT-5.2 | Claude Opus |
| Librarian | Claude Sonnet / Gemini | Claude Sonnet |
| Explore | Grok / Gemini Flash | Claude Haiku |
| Prometheus | Planning System | Claude Opus |
| Momus | GPT-5.2 | Claude Opus |
| Metis | Claude Opus | Claude Opus |

## Installation Migration

### Remove oh-my-opencode

```bash
# Uninstall OpenCode plugin
opencode plugin remove oh-my-opencode

# Remove configuration
rm -rf ~/.config/opencode/oh-my-opencode.json
```

### Install oh-my-claude-sisyphus

```bash
# Via npm
npm install -g oh-my-claude-sisyphus

# Via curl
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/install.sh | bash
```

## Configuration Migration

### Config File Location

| File | oh-my-opencode | oh-my-claude-sisyphus |
|------|---------------|----------------------|
| User config | `~/.config/opencode/oh-my-opencode.json` | `~/.claude/settings.json` |
| Project config | `.opencode/oh-my-opencode.json` | `.claude/settings.json` |
| Context | `.opencode/CLAUDE.md` | `.claude/CLAUDE.md` |

### Migrating Settings

**oh-my-opencode config:**
```json
{
  "disabled_agents": ["document-writer"],
  "agents": {
    "oracle": {
      "model": "openai/gpt-5.2"
    }
  }
}
```

**oh-my-claude-sisyphus equivalent:**
```json
{
  "agents": {
    "oracle": {
      "model": "opus"
    },
    "document-writer": {
      "enabled": false
    }
  }
}
```

### Configuration Mapping

| oh-my-opencode | oh-my-claude-sisyphus |
|---------------|----------------------|
| `disabled_mcps` | Not applicable |
| `disabled_agents` | `agents.{name}.enabled: false` |
| `disabled_hooks` | Remove from hooks array |
| `agent.model` | `model: "opus"\|"sonnet"\|"haiku"` |
| `auto_update` | `auto_update` (same) |

## Agent Migration

### Agent Definitions

**oh-my-opencode** (TypeScript):
```typescript
{
  name: "oracle",
  model: "openai/gpt-5.2",
  systemPrompt: "...",
  tools: ["read", "grep", "bash"]
}
```

**oh-my-claude-sisyphus** (Markdown):
```markdown
---
name: oracle
model: opus
tools: Read, Grep, Bash
---

# Oracle

System prompt here...
```

### Custom Agents

If you had custom agents in oh-my-opencode:

1. Create new file in `~/.claude/agents/your-agent.md`
2. Convert config to frontmatter
3. Convert system prompt to markdown
4. Update model references

## Hook Migration

### Hook Format

**oh-my-opencode** (JavaScript):
```javascript
export async function postToolUse(context) {
  const { tool, result } = context;
  // Hook logic
  return { modified: false };
}
```

**oh-my-claude-sisyphus** (Shell):
```bash
#!/bin/bash
TOOL_NAME="$1"
TOOL_RESULT="$2"

# Hook logic
echo "Additional context"
```

### Hook Events Mapping

| oh-my-opencode | oh-my-claude-sisyphus |
|---------------|----------------------|
| `tool.execute.before` | `PreToolUse` |
| `tool.execute.after` | `PostToolUse` |
| `chat.message` | `UserPromptSubmit` |
| `session.error` | Various error hooks |

### Hook Location

**oh-my-opencode:** Inline in config or package hooks

**oh-my-claude-sisyphus:** `~/.claude/sisyphus/hooks/`

## Command Migration

### Slash Commands

| oh-my-opencode | oh-my-claude-sisyphus | Notes |
|---------------|----------------------|-------|
| `/sisyphus` | `/sisyphus` | Same |
| `/ultrawork` | `/ultrawork` | Same |
| `/plan` | `/plan` | Same |
| `/review` | `/review` | Same |
| `/prometheus` | `/prometheus` | Same |
| `/ralph` | `/ralph-loop` | Renamed |
| `/search` | `/deepsearch` | Renamed |

## Tool Migration

### Tool Availability

| Tool | oh-my-opencode | oh-my-claude-sisyphus |
|------|---------------|----------------------|
| Read | ✅ | ✅ |
| Write | ✅ | ✅ |
| Edit | ✅ | ✅ |
| Bash | ✅ | ✅ |
| Grep | ✅ | ✅ |
| Glob | ✅ | ✅ |
| LSP | ✅ | ✅ (real LSP) |
| AST-grep | ✅ | ✅ |
| WebSearch | ✅ | ✅ |
| Task | ✅ | ✅ |

### LSP Tools

**oh-my-opencode:** Simulated LSP

**oh-my-claude-sisyphus:** Real LSP integration

Available LSP tools:
- `lsp_hover`
- `lsp_goto_definition`
- `lsp_find_references`
- `lsp_document_symbols`
- `lsp_workspace_symbols`
- `lsp_diagnostics`
- `lsp_rename`
- `lsp_code_actions`

## Workflow Changes

### Agent Swapping → Skills

**oh-my-opencode:**
```bash
# Switch master agent
switchMaster('prometheus')
```

**oh-my-claude-sisyphus:**
```bash
# Use skill (context preserved)
/plan design the system

# Or let Claude auto-detect
Design the authentication system
```

### Background Tasks

**oh-my-opencode:**
```javascript
backgroundTask(agent, task, options)
```

**oh-my-claude-sisyphus:**
```javascript
Task(agent, task, run_in_background=true)
```

## Mental Model Shift

### From: Agent Switching

```
┌───────────────┐
│ Switch Master │
└───────┬───────┘
        │
    ┌───┴───┐
    │       │
    ▼       ▼
┌─────┐ ┌─────┐
│ A   │ │ B   │
└─────┘ └─────┘
```

### To: Skill Composition

```
┌───────────────┐
│ Same Master   │
└───────┬───────┘
        │
    ┌───┴─────┐
    │ Skills  │
    └─┬─┬─┬─┬─┘
      │ │ │ │
      ▼ ▼ ▼ ▼
   Skills stack
```

## Common Migration Tasks

### Preserve Your Prompts

1. **Export oh-my-opencode agent prompts:**
   ```bash
   cat ~/.config/opencode/agents/*.md
   ```

2. **Create matching Claude agents:**
   ```bash
   # For each custom agent
   vi ~/.claude/agents/my-agent.md
   ```

3. **Update model references:**
   - GPT-5.2 → opus
   - Grok → haiku
   - Gemini → sonnet

### Migrate Configuration

```bash
# Convert oh-my-opencode config
cat ~/.config/opencode/oh-my-opencode.json

# Create Claude settings
vi ~/.claude/settings.json
```

### Update Project Files

```bash
# Rename directory
mv .opencode .claude

# Update CLAUDE.md references
# (no changes needed for content)
```

## Compatibility Notes

### What's Different

| Feature | Change |
|---------|--------|
| Multi-provider | Claude-only now |
| Interactive Bash + Tmux | Standard Bash |
| 22 hooks | 18 hooks (streamlined) |
| Per-model concurrency | Single pool |

### What's the Same

| Feature | Status |
|---------|--------|
| Multi-agent orchestration | ✅ Same |
| Todo continuation | ✅ Same |
| Background execution | ✅ Same |
| Context injection | ✅ Same |
| Magic keywords | ✅ Same |
| Slash commands | ✅ Same |

## Post-Migration Checklist

- [ ] Install oh-my-claude-sisyphus
- [ ] Migrate configuration settings
- [ ] Recreate custom agents
- [ ] Update project `.claude/` directories
- [ ] Test slash commands
- [ ] Verify agents are accessible
- [ ] Check hooks are firing
- [ ] Validate context injection

## Getting Help

If you encounter issues during migration:

1. Check this documentation
2. Review [Configuration Reference](reference.md)
3. Compare with [oh-my-opencode docs](https://github.com/code-yeongyu/oh-my-opencode)
4. Open an issue on GitHub

## Related Documentation

- [Configuration Reference](reference.md) - Full configuration schema
- [Agent Customization](agent-customization.md) - Creating agents
- [Project Configuration](project-config.md) - Project setup
