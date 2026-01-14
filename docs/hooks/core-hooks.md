---
layout: default
title: Core Hooks
parent: Hook System Overview
nav_order: 2
---

# Core Hooks

> **Relevant source files**
> * [src/hooks/rules-injector/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/rules-injector/index.ts)
> * [src/hooks/sisyphus-orchestrator/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/sisyphus-orchestrator/index.ts)
> * [src/hooks/auto-slash-command/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/auto-slash-command/index.ts)
> * [src/hooks/keyword-detector/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/keyword-detector/index.ts)
> * [src/hooks/ralph-loop/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/ralph-loop/index.ts)
> * [src/hooks/todo-continuation/index.ts](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/src/hooks/todo-continuation/index.ts)

Core hooks provide orchestration, behavior enforcement, and task management for the Sisyphus multi-agent system.

## Overview

| Hook | Events | Purpose |
|------|--------|---------|
| **rules-injector** | UserPromptSubmit | Dynamic rules injection with glob matching |
| **sisyphus-orchestrator** | PreToolUse, PostToolUse, Stop | Enforce delegation and verification |
| **auto-slash-command** | UserPromptSubmit | Expand slash commands from skills/commands |
| **keyword-detector** | UserPromptSubmit | Detect magic keywords (ultrawork, search, analyze) |
| **ralph-loop** | Stop | Self-referential work until completion |
| **todo-continuation** | Stop | Ensure todo list completion |

## Rules Injector

The `rules-injector` hook automatically injects project-specific coding rules when files are accessed.

### Rule File Format

Rules are defined as markdown files with YAML frontmatter:

```markdown
---
globs: ["*.ts", "src/**/*.tsx"]
description: "TypeScript React component rules"
---

- Use functional components with hooks
- Prefer interface over type for object shapes
- Export components separately from utilities
```

### Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `globs` | `string[]` | Glob patterns to match against file paths |
| `description` | `string` | Human-readable rule description |
| `alwaysApply` | `boolean` | Inject regardless of file path match |

### Search Paths

Rules are searched in order of priority:

1. `~/.claude/rules/` - User-level rules
2. `.claude/rules/` - Project rules
3. `.github/instructions.md` - GitHub Copilot instructions (always applied)
4. `.cursor/rules` - Cursor IDE rules (if present)

### Session Caching

Each rule is injected once per session to avoid duplication. Cache is stored in:

```
.sisyphus/rules-injected.json
```

### Configuration

```json
{
  "disabled_hooks": ["rules-injector"]
}
```

---

## Sisyphus Orchestrator

The `sisyphus-orchestrator` hook enforces proper orchestrator behavior: delegation over direct implementation.

### Allowed Paths

Orchestrators can directly modify files only within `.sisyphus/`:

| Path Pattern | Allowed |
|--------------|---------|
| `.sisyphus/**` | Yes |
| `.claude/agents/**` | Yes |
| `.claude/commands/**` | Yes |
| Any other path | No - must delegate |

### Monitored Tools

| Tool | Action |
|------|--------|
| `Write`, `Edit`, `MultiEdit` | Warn if outside allowed paths |
| `Task` | Add verification reminder after completion |

### Verification Reminder

After Task tool completion, the hook injects:

```text
[VERIFICATION REQUIRED]
Before marking this task complete, verify:

1. [ ] FUNCTIONALITY: The requested feature works as specified
2. [ ] TESTS: All tests pass (if applicable)
3. [ ] ERRORS: No errors in the output
4. [ ] QUALITY: Code is clean and production-ready
```

### Boulder Continuation

When a boulder state (active plan) exists, the hook tracks progress:

```
State: Plan: feature-implementation | 3/5 done, 2 left
```

### Configuration

```json
{
  "disabled_hooks": ["sisyphus-orchestrator"]
}
```

---

## Auto Slash Command

The `auto-slash-command` hook detects and expands slash commands in user prompts.

### Command Sources

Commands are discovered from multiple locations:

| Location | Scope |
|----------|-------|
| `~/.claude/commands/` | Global user commands |
| `~/.claude/skills/*/SKILL.md` | Built-in skills |
| `.claude/commands/` | Project-specific commands |

### Command Format

```markdown
<!-- command-name.md -->
---
name: command-name
description: Brief description
---

Command template text here.
$ARGUMENTS are replaced with user input.
```

### Detection Pattern

Slash commands are detected when:

```
/command-name [arguments...]
```

### Example Built-in Commands

| Command | Description |
|---------|-------------|
| `/sisyphus` | Activate multi-agent orchestration |
| `/ultrawork` | Maximum performance parallel mode |
| `/plan` | Start planning session with Prometheus |
| `/ralph-loop` | Start self-referential work loop |

### Configuration

```json
{
  "disabled_hooks": ["auto-slash-command"]
}
```

---

## Keyword Detector

The `keyword-detector` hook detects magic keywords that activate enhanced modes.

### Supported Keywords

| Keyword Type | Triggers | Aliases |
|--------------|----------|---------|
| `ultrawork` | Parallel agent orchestration | `ulw` |
| `ultrathink` | Extended thinking mode | `think` |
| `search` | Enhanced search mode | `find`, `locate`, `where is` |
| `analyze` | Deep analysis mode | `investigate`, `examine`, `why is` |

### Priority Order

Keywords are checked in priority order:

1. `ultrawork` - Highest priority
2. `ultrathink`
3. `search`
4. `analyze`

### Code Block Filtering

Keywords in code blocks are ignored to prevent false positives:

```
```python
def search(data):  # Ignored - inside code block
    pass
```
```

### Configuration

```json
{
  "disabled_hooks": ["keyword-detector"]
}
```

---

## Ralph Loop

The `ralph-loop` hook implements self-referential development: the agent continues working until a completion promise is detected.

### State Storage

State is stored in `.sisyphus/ralph-state.json`:

```json
{
  "active": true,
  "iteration": 3,
  "max_iterations": 10,
  "completion_promise": "TASK_COMPLETE",
  "started_at": "2025-01-13T10:00:00Z",
  "prompt": "Fix the authentication bug",
  "session_id": "abc123"
}
```

### Completion Detection

The loop stops when:

1. `<promise>TASK_COMPLETE</promise>` is detected in transcript
2. `max_iterations` is reached
3. User explicitly cancels with `/cancel-ralph`

### Activation

Via slash command:

```
/ralph-loop Fix the authentication bug
```

Or via prompt:

```
ralph-loop: Fix the authentication bug
```

### Configuration

```json
{
  "disabled_hooks": ["ralph-loop"]
}
```

---

## Todo Continuation

The `todo-continuation` hook prevents stopping when incomplete tasks remain.

### Todo Locations

The hook searches for todos in:

| Location | Format |
|----------|--------|
| `~/.claude/todos/` | Session-specific JSON |
| `.sisyphus/todos.json` | Project todos |
| `.claude/todos.json` | Alternative project location |

### Todo Format

```json
{
  "todos": [
    {
      "content": "Implement user authentication",
      "status": "in_progress",
      "priority": "high",
      "id": "task-1"
    },
    {
      "content": "Write unit tests",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

### Status Values

| Status | Description |
|--------|-------------|
| `pending` | Not started |
| `in_progress` | Currently being worked on |
| `completed` | Finished |
| `cancelled` | Cancelled (not counted as incomplete) |

### Continuation Message

When incomplete tasks are detected:

```
[SYSTEM REMINDER - TODO CONTINUATION]
Incomplete tasks remain in your todo list. Continue working on the next pending task.
```

### Configuration

```json
{
  "disabled_hooks": ["todo-continuation"]
}
```

## Hook Reference Table

| Hook | Events | State File | Configurable |
|------|--------|------------|--------------|
| rules-injector | UserPromptSubmit | `.sisyphus/rules-injected.json` | Yes |
| sisyphus-orchestrator | PreToolUse, PostToolUse, Stop | None | Yes |
| auto-slash-command | UserPromptSubmit | None | Yes |
| keyword-detector | UserPromptSubmit | None | Yes |
| ralph-loop | Stop | `.sisyphus/ralph-state.json` | Yes |
| todo-continuation | Stop | `.sisyphus/todos.json` | Yes |

## Further Reading

- [Context Recovery](context-recovery.md) - Context window management
- [Quality Hooks](quality-hooks.md) - Validation and code quality
- [Environment Hooks](environment-hooks.md) - Environment adaptation
