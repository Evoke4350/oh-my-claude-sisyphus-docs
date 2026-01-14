---
layout: default
title: Project Configuration
parent: Configuration Reference
nav_order: 3
---

# Project Configuration

Project-specific configuration is managed through `.claude/` directory in your project root. This allows per-project customization without affecting global settings.

## Directory Structure

```
my-project/
├── .claude/
│   ├── CLAUDE.md           # Project context
│   ├── AGENTS.md           # Project-specific agents
│   ├── settings.json       # Project settings
│   ├── agents/             # Project agents
│   │   └── custom-agent.md
│   └── rules/              # Dynamic rules
│       ├── typescript.md
│       └── api-style.md
└── src/
```

## CLAUDE.md

Project context file that provides instructions specific to your codebase.

### Purpose

- Describe tech stack and architecture
- Define coding conventions
- Document special requirements
- Guide agent behavior

### Template

```markdown
# [Project Name]

## Tech Stack
- **Runtime:** Node.js, Bun, Python, etc.
- **Framework:** React, Express, Django, etc.
- **Database:** PostgreSQL, MongoDB, etc.
- **Testing:** Jest, Pytest, etc.

## Architecture
<!-- Directory structure and organization -->

## Conventions
<!-- Coding standards and patterns -->

## Special Notes
<!-- Workarounds, external deps, deployment -->
```

### Example: TypeScript Monorepo

```markdown
# My TypeScript Monorepo

## Tech Stack
- **Runtime:** Bun 1.0+
- **Frontend:** React 18 with TypeScript 5
- **Backend:** Express with TypeScript
- **Database:** PostgreSQL with Prisma ORM

## Architecture
```
src/
├── shared/       # Shared utilities and types
├── frontend/     # React application
├── backend/      # Express API
└── contracts/    # Shared type contracts
```

## Conventions
- Use functional components with hooks
- API routes in `/src/backend/routes/`
- Shared types in `/src/contracts/`
- Test files co-located: `Component.test.tsx`
- Prisma schema in `/prisma/schema.prisma`

## API Patterns
- All routes use `/api/v1/` prefix
- Response format: `{ data, error, meta }`
- Authentication via JWT in Authorization header

## Database
- All queries through Prisma
- Transactions for multi-step operations
- Soft deletes (deletedAt column)

## Special Notes
- ENV variables from `.env.local` (not in repo)
- Deploy via Docker to AWS ECS
- CI/CD through GitHub Actions
```

### Example: Python Project

```markdown
# Django API Project

## Tech Stack
- **Runtime:** Python 3.11
- **Framework:** Django 4.2
- **Database:** PostgreSQL
- **API:** Django REST Framework

## Architecture
```
src/
├── apps/          # Django apps
├── config/        # Settings modules
├── core/          # Shared utilities
└── static/        # Static assets
```

## Conventions
- Class-based views for complex logic
- Function-based views for simple CRUD
- Serializers in `serializers.py`
- URLs in `urls.py` per app
- Migrations for all schema changes

## Special Notes
- Use Celery for background tasks
- Redis for caching
- Sentry for error tracking
```

## AGENTS.md

Define project-specific agents or override global agents.

### Template

```markdown
# Project Agents

## Project-Specific Agents

### <agent-name>
<Description of agent's purpose>

### <agent-name>
<Description of agent's purpose>
```

### Example

```markdown
# Project Agents

## Project-Specific Agents

### prisma-expert
Specializes in Prisma ORM schema design, migrations, and query optimization.

### stripe-integrator
Expert in Stripe payment integration, webhook handling, and subscription management.
```

## settings.json

Override global settings for this project.

### Example

```json
{
  "agents": {
    "explore": {
      "model": "sonnet"
    }
  },
  "sisyphus": {
    "max_background_tasks": 3
  },
  "hooks": {
    "PostToolUse": [
      ".claude/hooks/custom-rule-injector.sh"
    ]
  }
}
```

### Use Cases

- Use different models for specific agents
- Adjust background task limits
- Add project-specific hooks
- Enable/disable features per project

## Rules Directory

Dynamic rules that inject based on file patterns.

### Rule File Format

```markdown
---
name: "rule-name"
triggers:
  - "*.ts"
  - "*.tsx"
---

# Rule Title

Rule content here...
```

### Example: TypeScript Style

**File:** `.claude/rules/typescript.md`

```markdown
---
name: "typescript-style"
triggers:
  - "*.ts"
  - "*.tsx"
---

# TypeScript Style Rules

When editing TypeScript files:
- Use interfaces for object shapes
- Prefer type over interface for unions/intersections
- Use const assertions for literal types
- Avoid any without explanatory comment
- Prefer explicit return types
```

### Example: API Route Style

**File:** `.claude/rules/api-routes.md`

```markdown
---
name: "api-route-style"
triggers:
  - "src/api/**/*.ts"
---

# API Route Rules

When editing API route files:
- All routes must have JSDoc comments
- Use async/await, not promises
- Validate request input with zod
- Return consistent response format
- Log errors with context
- Use 404 for missing resources
- Use 400 for validation errors
- Use 500 for unexpected errors
```

### Example: Test Style

**File:** `.claude/rules/test-style.md`

```markdown
---
name: "test-style"
triggers:
  - "*.test.ts"
  - "*.test.tsx"
  - "*.spec.ts"
---

# Test Style Rules

When writing tests:
- Use describe/it/test pattern
- Test one thing per test
- Use descriptive test names
- Mock external dependencies
- Clean up after each test
- Test error cases
```

## Custom Hooks

Project-specific hooks in `.claude/hooks/`.

### Example: Custom Rule Injector

**File:** `.claude/hooks/custom-injector.sh`

```bash
#!/bin/bash
# Custom context injector

FILE="$1"

# Inject database schema context for backend files
if [[ "$FILE" == src/backend/**/*.ts ]]; then
    echo "DATABASE_SCHEMA: $(cat prisma/schema.prisma)"
fi

# Inject API docs for route files
if [[ "$FILE" == src/api/**/*.ts ]]; then
    echo "API_DOCS: $(cat docs/api-reference.md)"
fi
```

## Per-Project Configuration Priority

```
1. .claude/settings.json (project settings)
2. ~/.claude/settings.json (user settings)
3. Built-in defaults
```

Project settings override user settings for conflicting options.

## Ignoring Files

Exclude files from context injection:

**File:** `.claudeignore`

```
# Ignore patterns
node_modules/
dist/
build/
*.min.js
*.min.css
.env
*.log
```

## Version Control

### Recommended .gitignore

```
# Project configuration (commit structure)
.claude/

# But ignore generated state
.claude/.sisyphus/
.claude/hooks/*.log

# Keep user config private
.claude/settings.json.local
```

### Commit Strategy

**Commit:** `.claude/CLAUDE.md`, `.claude/AGENTS.md`, `.claude/rules/`

**Don't Commit:** `.claude/settings.json` (contains preferences), `.claude/.sisyphus/` (runtime state)

## Best Practices

1. **Keep CLAUDE.md concise** - Focus on project-specifics
2. **Use rules for patterns** - Put repetitive rules in rules/
3. **Document conventions** - Help agents understand your style
4. **Version control context** - Commit CLAUDE.md for team
5. **Local settings** - Use settings.json for preferences

## Related Documentation

- [Configuration Reference](reference.md) - Full schema
- [Agent Customization](agent-customization.md) - Agent files
- [Context Injection](../features/context-injection.md) - How injection works
