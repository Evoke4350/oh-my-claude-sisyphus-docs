---
layout: default
title: Built-in Tools
parent: Tools Overview
nav_order: 4
---

# Built-in Tools

> **Relevant source files**
> * [README.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md)

Claude Code provides built-in tools for file operations, search, execution, organization, and web access.

## Overview

| Category | Tools |
|----------|-------|
| **File Operations** | Read, Write, Edit |
| **Search** | Glob, Grep |
| **Execution** | Bash |
| **Organization** | Task, TodoWrite |
| **Web** | WebSearch, WebFetch |

## File Operations

### Read

Read file contents from the filesystem.

**Input:**

```typescript
{
  "file_path": "/path/to/file.txt",
  "offset": 0,
  "limit": 1000
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | `string` | Yes | Absolute path to file |
| `offset` | `number` | No | Line number to start reading (default: 0) |
| `limit` | `number` | No | Maximum lines to read (default: all) |

**Output:**

File contents with line numbers:

```
     1	First line of file
     2	Second line of file
     3	Third line of file
```

**Use Cases:**

| Reading configuration files |
| Viewing source code |
| Examining documentation |

---

### Write

Create or overwrite a file with new content.

**Input:**

```typescript
{
  "file_path": "/path/to/file.txt",
  "content": "File contents here\nMultiple lines"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | `string` | Yes | Absolute path to file |
| `content` | `string` | Yes | Content to write |

**Output:**

```
File written successfully to /path/to/file.txt
```

**Use Cases:**

| Creating new files |
| Completely replacing file contents |
| Writing generated code |

---

### Edit

Replace specific text within a file.

**Input:**

```typescript
{
  "file_path": "/path/to/file.txt",
  "old_string": "text to replace",
  "new_string": "replacement text"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | `string` | Yes | Absolute path to file |
| `old_string` | `string` | Yes | Text to replace (must be exact) |
| `new_string` | `string` | Yes | Replacement text |

**Output:**

```
File edited successfully: 1 occurrence replaced
```

**Use Cases:**

| Updating specific lines |
| Fixing bugs in code |
| Modifying configuration values |

**Important:** The `old_string` must match exactly. If it appears multiple times, all occurrences are replaced unless more context is provided.

## Search Tools

### Glob

Find files by pattern matching.

**Input:**

```typescript
{
  "pattern": "**/*.ts",
  "path": "/project/src"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pattern` | `string` | Yes | Glob pattern |
| `path` | `string` | No | Directory to search (default: cwd) |

**Glob Patterns:**

| Pattern | Matches |
|---------|---------|
| `*.ts` | All `.ts` files in current directory |
| `**/*.ts` | All `.ts` files recursively |
| `src/**/*.test.ts` | Test files in src/ |
| `*.{ts,tsx}` | Files with either extension |

**Output:**

```
/path/to/file1.ts
/path/to/file2.ts
/path/to/subdir/file3.ts
```

**Use Cases:**

| Finding files by extension |
| Locating test files |
| Discovering configuration files |

---

### Grep

Search file contents for patterns.

**Input:**

```typescript
{
  "pattern": "function",
  "path": "/project/src",
  "file_pattern": "*.ts"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pattern` | `string` | Yes | Search pattern (regex) |
| `path` | `string` | No | Directory to search (default: cwd) |
| `file_pattern` | `string` | No | Filter files by glob pattern |

**Flags:**

| Flag | Description |
|------|-------------|
| `-i` | Case-insensitive search |
| `-v` | Invert match (show non-matching) |
| `-n` | Show line numbers |
| `-C` | Show context lines |

**Output:**

```
src/auth.ts:42:  function login(user: User) {
src/auth.ts:55:  function logout() {
src/utils.ts:10:  function formatDate() {
```

**Use Cases:**

| Finding function definitions |
| Locating specific strings |
| Searching for TODOs/FIXMEs |

## Execution Tools

### Bash

Execute shell commands.

**Input:**

```typescript
{
  "command": "ls -la",
  "timeout": 30000,
  "run_in_background": false
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `command` | `string` | Yes | Shell command to execute |
| `timeout` | `number` | No | Max duration in ms (default: 120000) |
| `run_in_background` | `boolean` | No | Run asynchronously (default: false) |

**Output:**

```
total 24
drwxr-xr-x  4 user  staff  128 Jan 13 10:00 .
drwxr-xr-x  3 user  staff   96 Jan 13 09:00 ..
-rw-r--r--  1 user  staff  256 Jan 13 10:00 file.txt
```

**Use Cases:**

| Running build commands |
| Executing tests |
| Package installation |

**Background Execution:**

Use `run_in_background: true` for long-running operations:

```typescript
{
  "command": "npm install",
  "run_in_background": true
}
```

## Organization Tools

### Task

Spawn a subagent for specialized work.

**Input:**

```typescript
{
  "agent": "oracle",
  "prompt": "Debug the authentication issue"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `agent` | `string` | Yes | Agent name (oracle, librarian, explore, etc.) |
| `prompt` | `string` | Yes | Task description |
| `model` | `string` | No | Override agent model |
| `background` | `boolean` | No | Run in background (default: false) |

**Available Agents:**

| Agent | Model | Best For |
|-------|-------|----------|
| `oracle` | Opus | Complex debugging, architecture |
| `librarian` | Sonnet | Documentation, research |
| `explore` | Haiku | Fast file searches |
| `frontend-engineer` | Sonnet | UI/UX work |
| `sisyphus-junior` | Sonnet | Focused task execution |

**Output:**

```
Subagent 'oracle' completed: [result details]
```

**Use Cases:**

| Delegating specialized tasks |
| Parallel processing |
| Using specific model capabilities |

---

### TodoWrite

Track task progress with todos.

**Input:**

```typescript
{
  "todos": [
    {
      "content": "Implement authentication",
      "status": "pending",
      "activeForm": "Implementing authentication"
    }
  ]
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `todos` | `Todo[]` | Yes | Array of todo items |

**Todo Schema:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | `string` | Yes | Task description |
| `status` | `string` | Yes | `pending`, `in_progress`, or `completed` |
| `activeForm` | `string` | Yes | Present tense form for display |

**Output:**

```
Updated todo list: 2 pending, 1 in_progress, 0 completed
```

**Use Cases:**

| Tracking multi-step tasks |
| Showing progress to users |
| Organizing complex work |

## Web Tools

### WebSearch

Search the web for current information.

**Input:**

```typescript
{
  "query": "Claude 4.5 release notes"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | `string` | Yes | Search query |

**Output:**

```
Search results for "Claude 4.5 release notes":

1. [Claude 4.5 Release](https://example.com/claude-4.5)
   Claude 4.5 includes improved reasoning...

2. [Model Updates](https://example.com/updates)
   Latest model family updates...
```

**Use Cases:**

| Finding current documentation |
| Researching APIs |
| Checking for known issues |

---

### WebFetch

Fetch and parse a web page.

**Input:**

```typescript
{
  "url": "https://example.com/docs/api.html",
  "return_format": "markdown"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | `string` | Yes | URL to fetch |
| `return_format` | `string` | No | `markdown` or `text` (default: markdown) |

**Output:**

```markdown
# API Documentation

Content of the fetched page...
```

**Use Cases:**

| Reading documentation |
| Extracting API specs |
| Analyzing web content |

## Tool Comparison

| Tool | Reads | Writes | Executes | Notes |
|------|-------|--------|----------|-------|
| Read | Yes | No | No | Line numbers included |
| Write | No | Yes | No | Overwrites entire file |
| Edit | Yes | Yes | No | Replaces specific text |
| Glob | No | No | No | File pattern matching |
| Grep | Yes | No | No | Content search |
| Bash | Yes | No | Yes | Shell command execution |
| Task | No | No | Yes | Subagent delegation |
| TodoWrite | No | Yes | No | Task tracking |
| WebSearch | Yes | No | No | Web search |
| WebFetch | Yes | No | No | Page retrieval |

## Best Practices

### File Operations

1. **Use Read before Edit** - Always read to verify current content
2. **Be specific with old_string** - Include enough context for unique matching
3. **Use Write for new files** - Edit requires file to exist

### Search Operations

1. **Glob for files, Grep for content** - Choose the right tool
2. **Use file_pattern with Grep** - Limit search scope
3. **Consider AST tools for code** - Structural search is more accurate

### Execution

1. **Use background for long tasks** - Install, build, test
2. **Set appropriate timeouts** - Default 2 minutes, max 10 minutes
3. **Check command exit codes** - Non-zero may indicate errors

### Subagents

1. **Choose the right agent** - Match agent to task type
2. **Provide clear prompts** - Include context and requirements
3. **Use background for independence** - Parallel subagents

## Error Handling

| Tool | Common Error | Resolution |
|------|--------------|------------|
| Read | File not found | Check file path |
| Write | Permission denied | Check directory permissions |
| Edit | old_string not found | Read file first, verify exact content |
| Bash | Command not found | Check PATH, install command |
| Task | Agent not found | Verify agent name spelling |
| WebSearch | Rate limited | Wait and retry |
| WebFetch | Invalid URL | Check URL format |

## Further Reading

- [LSP Tools](lsp-tools.md) - LSP operations reference
- [AST Tools](ast-tools.md) - Pattern-based code search
- [Tool Overview](overview.md) - Tool ecosystem overview
