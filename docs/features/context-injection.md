---
layout: default
title: Context Injection
parent: Features Overview
nav_order: 3
---

# Context Injection

Context injection automatically loads project-specific instructions and agent definitions into your Claude Code sessions, providing relevant context without manual prompting.

## Overview

The context injection system monitors file reads and automatically injects relevant documentation, rules, and agent definitions based on your current working directory and accessed files.

## Injection Sources

### CLAUDE.md

Project-level context file that provides instructions specific to your codebase.

**Search Locations (in order):**

1. `.claude/CLAUDE.md` (project root)
2. `CLAUDE.md` (project root)
3. `~/.claude/CLAUDE.md` (user-level fallback)

**Purpose:** Project-specific context that applies to all work in this directory.

**Example CLAUDE.md:**
```markdown
# Project Context

This is a TypeScript monorepo using:
- Bun runtime
- React for frontend
- PostgreSQL database

## Conventions
- Use functional components
- All API routes in /src/api
- Tests alongside source files

## Architecture
- /src/shared - shared utilities
- /src/api - API routes
- /src/components - React components
```

---

### AGENTS.md

Agent definitions and capabilities for the current project.

**Search Locations (in order):**

1. `.claude/AGENTS.md` (project root)
2. `AGENTS.md` (project root)
3. `~/.claude/AGENTS.md` (user-level fallback)

**Purpose:** Defines project-specific agents or overrides global agent behavior.

**Example AGENTS.md:**
```markdown
# Project Agents

## Project-Specific Agents

### database-architect
Expert in PostgreSQL optimization and schema design.
```

---

### Rules Injection

Dynamic rule loading from `.claude/rules/` directory.

**Search Location:**
- `.claude/rules/*.md` (project root)

**File Format:** Rules files use YAML frontmatter for metadata:

```markdown
---
name: "typescript-style"
triggers:
  - "*.ts"
  - "*.tsx"
---

# TypeScript Style Rules

- Use interfaces for object shapes
- Prefer const assertions
- No any types without comment
```

**Triggers:**
| Trigger Type | Example |
|--------------|---------|
| File pattern | `*.ts`, `*.tsx` |
| Directory | `src/api` |
| Path pattern | `**/test/**` |

---

## Injection Flow

```
File Read/Edit
     │
     ▼
Path Extraction
     │
     ├─► Project Root Detection
     │        │
     │        ├─► .claude/CLAUDE.md?
     │        ├─► CLAUDE.md?
     │        └─► ~/.claude/CLAUDE.md?
     │
     ├─► Rules Detection
     │        │
     │        └─► .claude/rules/*.md (matching path)
     │
     └─► Agent Detection
              │
              └─► .claude/AGENTS.md? / AGENTS.md?
```

---

## Automatic Injection Triggers

Context is injected on these events:

| Event | What Triggers |
|-------|---------------|
| **File Read** | Any file via Read tool |
| **File Edit** | Any file via Edit tool |
| **Session Start** | Working directory detected |
| **Directory Change** | New project root detected |

---

## Project Root Detection

The system identifies project roots by:

1. Looking for `.claude/` directory
2. Checking for `CLAUDE.md` or `AGENTS.md`
3. Searching for `package.json`, `Cargo.toml`, `go.mod`
4. Git repository root (`.git/` directory)

**Example:**
```bash
# Working in: ~/projects/my-app/src/components/
# Detected root: ~/projects/my-app/
# Injects: ~/projects/my-app/.claude/CLAUDE.md
```

---

## Rules Matching

Rules files are matched against accessed file paths:

**Example rules structure:**
```
.claude/
├── rules/
│   ├── typescript.md      # Triggers: *.ts, *.tsx
│   ├── api-routes.md      # Triggers: src/api/**
│   └── test-style.md      # Triggers: **/*.test.ts
└── CLAUDE.md
```

**Matching behavior:**
- Multiple rules can match a single file
- All matching rules are injected
- Rules inject before tool execution completes

---

## Disabling Context Injection

### Per-Session

Claude respects explicit instructions not to use context:

```bash
# Don't use project context for this task
Ignore CLAUDE.md and just implement the function
```

### Per-Project

**Option 1:** Remove context files
```bash
rm .claude/CLAUDE.md
rm .claude/AGENTS.md
```

**Option 2:** Disable hooks
```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": []
  }
}
```

---

## Priority Order

When multiple context sources exist:

1. **Project CLAUDE.md** (highest priority)
2. **Project AGENTS.md**
3. **Matching rules files** (in alphabetical order)
4. **User-level CLAUDE.md** (fallback)

Project-level context always overrides user-level context.

---

## Best Practices

### CLAUDE.md Structure

```markdown
# [Project Name]

## Tech Stack
- List frameworks, runtimes, databases

## Architecture
- Directory structure
- Module organization

## Conventions
- Coding standards
- File naming
- Testing approach

## Special Notes
- Workarounds for known issues
- External dependencies
- Deployment considerations
```

### Rules File Organization

```
.claude/
└── rules/
    ├── language-specific.md    # TypeScript, Python, etc.
    ├── directory-specific.md   # API routes, components
    ├── test-coverage.md        # Test style rules
    └── security.md            # Security requirements
```

### Minimal Context

Keep context focused and concise:

- **Do:** Include architecture and conventions
- **Don't:** Duplicate general knowledge
- **Do:** Highlight project-specific patterns
- **Don't:** Include generic tutorials

---

## Troubleshooting

### Context Not Injecting

**Verify files exist:**
```bash
ls .claude/CLAUDE.md
ls .claude/AGENTS.md
```

**Check hook is registered:**
```bash
cat ~/.claude/settings.json | grep rules-injector
```

**Verify file permissions:**
```bash
chmod +r ~/.claude/sisyphus/hooks/rules-injector.sh
```

### Wrong Context Injecting

**Check working directory:**
```bash
pwd
```

**Verify project root detection:**
```bash
ls -la .claude/
git rev-parse --show-toplevel
```

---

## Related Documentation

- [Configuration Reference](configuration/reference.md) - Configuration options
- [Project Configuration](../configuration/project-config/) - CLAUDE.md setup
- [Hooks](hooks/) - Hook system architecture
- [Core Hooks](../hooks/core-hooks/) - Detailed hooks documentation
