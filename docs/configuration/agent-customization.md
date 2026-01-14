---
layout: default
title: Agent Customization
parent: Configuration
nav_order: 2
---

# Agent Customization

Agents are defined as markdown files in `~/.claude/agents/`. Customize agent behavior by editing these files.

## Agent File Location

**User-Level Agents:**
```
~/.claude/agents/
├── oracle.md
├── librarian.md
├── explore.md
├── sisyphus-junior.md
├── frontend-engineer.md
├── document-writer.md
├── multimodal-looker.md
├── momus.md
├── metis.md
├── prometheus.md
└── qa-tester.md
```

**Project-Level Agents:**
```
.claude/agents/
└── custom-agent.md
```

Project-level agents override user-level agents with the same name.

## Agent File Format

### Frontmatter Section

YAML frontmatter defines agent metadata:

```markdown
---
name: oracle
description: Architecture and debugging expert
model: opus
tools: Read, Grep, Glob, Bash, Edit, LSP
color: "#9B59B6"
---

# System Prompt

Agent instructions go here...
```

### Frontmatter Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | Agent identifier |
| `description` | `string` | Yes | What the agent does |
| `model` | `string` | No | `opus`, `sonnet`, `haiku` |
| `tools` | `string[]` | No | Allowed tools (comma-separated) |
| `color` | `string` | No | Hex color for UI display |
| `disable` | `boolean` | No | If `true`, agent is unavailable |

## Creating Custom Agents

### Example: Database Architect

**File:** `~/.claude/agents/database-architect.md`

```markdown
---
name: database-architect
description: PostgreSQL expert for schema design and optimization
model: opus
tools: Read, Grep, Glob, Bash, Edit
color: "#3498DB"
---

# Database Architect

You are a PostgreSQL expert specializing in:
- Schema design and normalization
- Query optimization
- Index strategies
- Migration planning

## Approach

1. **Analyze Current State**
   - Examine existing schema
   - Review query patterns
   - Identify bottlenecks

2. **Design Recommendations**
   - Propose schema changes
   - Suggest indexes
   - Plan migrations

3. **Implementation**
   - Write migration SQL
   - Update ORM models
   - Add query optimizations

## Best Practices

- Always use transactions for schema changes
- Create indexes before bulk data loads
- Use EXPLAIN ANALYZE for query planning
- Consider read replica patterns for scaling
```

### Example: Security Auditor

**File:** `~/.claude/agents/security-auditor.md`

```markdown
---
name: security-auditor
description: Security expert for code review and vulnerability assessment
model: opus
tools: Read, Grep, Glob, Bash, Edit
color: "#E74C3C"
---

# Security Auditor

You identify security vulnerabilities in:
- Authentication flows
- Authorization checks
- Input validation
- Data handling
- API security

## Review Checklist

- [ ] SQL injection risks
- [ ] XSS vulnerabilities
- [ ] CSRF protection
- [ ] Secrets in code
- [ ] Insecure dependencies
- [ ] Authorization bypass
```

## Modifying Built-in Agents

### Changing Model

**File:** `~/.claude/agents/explore.md`

```markdown
---
model: sonnet  # Changed from haiku
---
```

### Adding Tools

**File:** `~/.claude/agents/oracle.md`

```markdown
---
tools: Read, Grep, Glob, Bash, Edit, LSP, WebSearch, WebFetch
---
```

### Appending Instructions

**File:** `~/.claude/agents/oracle.md`

```markdown
---
# existing frontmatter
---

# Oracle

## Standard Instructions

[...existing content...]

## Project-Specific Additions

When analyzing this codebase:
- Always check for enterprise patterns in `/src/enterprise/`
- Consider legacy compatibility requirements
- Review the authentication adapter in `/src/auth/`
```

## Agent Model Selection

| Model | Cost | Speed | Best For |
|-------|------|-------|----------|
| **opus** | High | Slow | Complex reasoning, architecture |
| **sonnet** | Medium | Medium | Implementation, analysis |
| **haiku** | Low | Fast | Simple lookups, formatting |

### When to Use Each Model

```
┌─────────────────────────────────────────────┐
│ Task Complexity                             │
├─────────────────────────────────────────────┤
│ High ──► opus (architecture, debugging)     │
│ Medium ─► sonnet (implementation, docs)     │
│ Low ───► haiku (searches, formatting)       │
└─────────────────────────────────────────────┘
```

## Tool Permissions

### Available Tools

| Tool | Description |
|------|-------------|
| `Read` | Read file contents |
| `Write` | Create new files |
| `Edit` | Modify existing files |
| `Bash` | Execute shell commands |
| `Grep` | Search file contents |
| `Glob` | Find files by pattern |
| `LSP` | Language server operations |
| `WebSearch` | Search the web |
| `WebFetch` | Fetch web pages |
| `Task` | Spawn subagents |

### Restricting Tools

```markdown
---
tools: Read, Grep, Glob
---
```

This agent can only read and search, not write or execute.

## Project-Specific Agents

Create project-specific agents in `.claude/agents/`:

**Structure:**
```
my-project/
├── .claude/
│   ├── agents/
│   │   ├── api-specialist.md
│   │   └── frontend-validator.md
│   └── CLAUDE.md
└── src/
```

These agents are only available when working in this project.

## Agent Testing

### Test Agent Behavior

```bash
# In Claude Code:
> Use the database-architect agent to review the schema
```

### Verify Agent Loading

```bash
# List available agents
ls ~/.claude/agents/

# Check project-specific agents
ls .claude/agents/
```

## Best Practices

1. **Clear Purpose** - Define specific expertise in description
2. **Appropriate Model** - Match model to task complexity
3. **Minimal Tools** - Only grant tools the agent needs
4. **Structured Instructions** - Use headings for clarity
5. **Examples** - Include examples of expected output

## Common Customizations

### Make Explore Faster

```markdown
---
model: haiku
tools: Read, Grep, Glob
---
```

### Make Oracle More Thorough

```markdown
---
model: opus
tools: Read, Grep, Glob, Bash, Edit, LSP, WebSearch, WebFetch
---

# Oracle

## Extended Analysis Mode

For complex issues:
1. Identify all potential root causes
2. Analyze each independently
3. Cross-reference for common factors
4. Prioritize by likelihood and impact
```

### Add Domain Expertise

```markdown
---
name: rust-expert
description: Rust language specialist
model: opus
---

# Rust Expert

Expert in:
- Ownership and borrowing
- Unsafe code patterns
- Async/await with tokio
- Macro system
- Cargo workspace management
```

## Related Documentation

- [Configuration Reference](reference.md) - Configuration schema
- [Project Configuration](project-config.md) - CLAUDE.md setup
- [Agents](../agents/) - Built-in agent documentation
