---
layout: default
title: Quick Start
parent: Getting Started
nav_order: 3
---

# Quick Start

> **Relevant source files**
> * [README.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md)
> * [CLAUDE.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/CLAUDE.md)
> * [commands/](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/tree/main/commands)

This page provides basic usage examples for oh-my-claude-sisyphus. Learn how to use slash commands, invoke agents, and use magic keywords for faster development workflows.

For installation instructions, see [Installation](./installation.md). For configuration details, see [Configuration](./configuration.md).

## Starting Claude Code

After installation, start Claude Code:

```bash
claude
```

You should see the Sisyphus system prompt loaded, indicating the multi-agent system is active.

**Sources:** [README.md L200-L220](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L200-L220)

## Slash Commands

Slash commands provide quick access to specialized modes and features.

### Orchestration Commands

#### /sisyphus

Activate Sisyphus multi-agent orchestration mode for a task:

```bash
# In Claude Code
/sisyphus refactor the authentication module

# Result: Sisyphus will coordinate agents to:
# 1. Analyze current auth implementation (Explore)
# 2. Research best practices (Librarian)
# 3. Design new architecture (Oracle)
# 4. Implement the refactor (Frontend Engineer + Sisyphus Junior)
# 5. Update documentation (Document Writer)
```

**Sources:** [commands/sisyphus.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/sisyphus.md)

#### /sisyphus-default

Set Sisyphus as your permanent default mode:

```bash
/sisyphus-default

# All subsequent prompts will use Sisyphus orchestration
# without needing the /sisyphus prefix
```

**Sources:** [commands/sisyphus-default.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/sisyphus-default.md)

### Enhancement Commands

#### /ultrawork

Activate maximum performance mode with parallel agent execution:

```bash
/ultrawork implement user dashboard with charts

# Result: Multiple agents work in parallel:
# - Explore searches for existing dashboard code
# - Librarian researches charting libraries
# - Oracle designs the component architecture
# - Frontend Engineer implements components
# - Document Writer writes documentation
```

**Sources:** [commands/ultrawork.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/ultrawork.md)

#### /deepsearch

Perform a thorough multi-strategy codebase search:

```bash
/deepsearch API endpoints that handle user data

# Result: Explore agent uses multiple search strategies:
# - Filename patterns (*user*, *api*, *endpoint*)
# - Content searches (function definitions, route handlers)
# - AST-based searches (API decorators, route definitions)
```

**Sources:** [commands/deepsearch.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/deepsearch.md)

#### /analyze

Perform deep analysis and investigation:

```bash
/analyze performance bottleneck in the database layer

# Result: Oracle agent performs:
# - Architecture analysis
# - Query pattern examination
# - Index usage review
# - Bottleneck identification
# - Optimization recommendations
```

**Sources:** [commands/analyze.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/analyze.md)

### Planning Commands

#### /plan

Start a planning session with Prometheus:

```bash
/plan implement user authentication with OAuth

# Result: Prometheus will:
# 1. Interview you about requirements
# 2. Identify hidden requirements (Metis)
# 3. Create comprehensive work plan
# 4. Plan can be reviewed by Momus
# 5. Execute with Sisyphus
```

**Sources:** [commands/plan.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/plan.md)

#### /review

Review a plan with Momus:

```bash
/review .claude/plans/authentication-plan.md

# Result: Momus provides:
# - Critical evaluation of plan feasibility
# - Risk identification
# - Missing requirement detection
# - Improvement suggestions
```

**Sources:** [commands/review.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/review.md)

#### /prometheus

Strategic planning with interview workflow:

```bash
/prometheus design a microservices architecture

# Result: Prometheus conducts:
# - Requirement gathering interview
# - Constraint identification
# - Comprehensive planning
# - Risk assessment
```

**Sources:** [commands/prometheus.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/prometheus.md)

### Execution Commands

#### /ralph-loop

Start a self-referential development loop until task completion:

```bash
/ralph-loop fix all failing tests

# Result: Sisyphus will:
# 1. Identify failing tests
# 2. Diagnose root causes
# 3. Implement fixes
# 4. Verify fixes
# 5. Continue until all tests pass
# 6. The loop does not stop until completion
```

**Sources:** [commands/ralph-loop.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/ralph-loop.md)

#### /cancel-ralph

Cancel an active Ralph Loop:

```bash
/cancel-ralph
```

**Sources:** [commands/cancel-ralph.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/cancel-ralph.md)

### Maintenance Commands

#### /update

Check for and install updates:

```bash
/update

# Result:
# 1. Checks for new releases
# 2. Downloads latest version
# 3. Installs updates
# 4. Preserves your configurations
```

**Sources:** [commands/update.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/commands/update.md)

## Magic Keywords

Magic keywords can be used anywhere in your prompt to activate special modes:

| Keyword | Effect |
|---------|--------|
| `ultrawork`, `ulw`, `uw` | Activates parallel agent orchestration |
| `search`, `find`, `locate` | Enhanced search mode |
| `analyze`, `investigate` | Deep analysis mode |

**Examples:**

```bash
# These work in normal prompts without slash commands:
> ultrawork implement user authentication with OAuth
> find all files that import the utils module
> analyze why the tests are failing
```

**Sources:** [CLAUDE.md L200-L250](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/CLAUDE.md#L200-L250)

## Agent Invocation

You can explicitly request specific agents:

### Manual Agent Invocation

```bash
# Architecture decisions
Use the oracle agent to design a scalable API architecture

# Documentation research
Have the librarian find all documentation about React hooks

# Codebase search
Ask explore to find all TypeScript files that import React

# UI implementation
Use frontend-engineer to create a responsive navigation component

# Technical writing
Have document-writer update the README with new features

# Visual analysis
Use multimodal-looker to analyze the Figma mockup
```

**Sources:** [README.md L300-L400](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L300-L400)

### Agent Capabilities

| Agent | Model | Best For |
|-------|-------|----------|
| **Oracle** | Opus | Complex debugging, architecture decisions |
| **Librarian** | Sonnet | Finding documentation, GitHub research |
| **Explore** | Haiku | Quick file searches, pattern matching |
| **Frontend Engineer** | Sonnet | UI components, styling, accessibility |
| **Document Writer** | Haiku | README files, API docs, comments |
| **Multimodal Looker** | Sonnet | Screenshots, diagrams, mockups |
| **Prometheus** | Opus | Strategic planning, comprehensive plans |
| **Momus** | Opus | Plan review, feasibility assessment |
| **Metis** | Opus | Pre-planning, hidden requirements |
| **Sisyphus Junior** | Sonnet | Focused execution, plan following |

**Sources:** [README.md L300-L400](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L300-L400)

## Common Workflows

### Feature Development

```bash
# Start with planning
/plan implement user profile management

# Review the plan (optional)
/review .claude/plans/user-profile-plan.md

# Execute with Sisyphus
/sisyphus implement the user profile feature

# Or use ultrawork for parallel execution
/ultrawork implement user profile with avatar upload
```

### Bug Fixing

```bash
# Deep analysis first
/analyze investigate the login bug

# Let Sisyphus orchestrate the fix
/sisyphus fix the authentication issue

# Or use Ralph Loop for persistent fixing
/ralph-loop fix all failing tests
```

### Documentation

```bash
# Let Document Writer handle it
Have document-writer create API documentation for the user module

# Or use Sisyphus for comprehensive docs
/sisyphus update README with new features and setup instructions
```

### Codebase Exploration

```bash
# Quick search
find all components using React hooks

# Deep search
/deepsearch database connection patterns in the codebase

# Analysis
/analyze the project's dependency tree and identify unused packages
```

### UI Development

```bash
# Always use Frontend Engineer for visual changes
Use frontend-engineer to create a dark mode toggle

# Combine with git-master for atomic commits
ultrawork create a responsive dashboard with charts and proper git commits
```

**Sources:** [README.md L400-L500](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L400-L500)

## Skill Combinations

Skills work in composable layers:

### Execution Layer (Pick One)

* `sisyphus` - Multi-agent orchestration
* `orchestrator` - Master coordinator
* `prometheus` - Strategic planning

### Enhancement Layer (Stack Multiple)

* `ultrawork` - Maximum performance
* `git-master` - Git expert
* `frontend-ui-ux` - UI/UX design

### Guarantee Layer (Optional)

* `ralph-loop` - Ensures completion

### Combination Examples

```bash
# Feature development with git expertise
"Add dark mode with proper commits"
→ sisyphus + frontend-ui-ux + git-master

# Maximum performance refactoring
"ultrawork: refactor the entire API layer"
→ ultrawork + sisyphus + git-master

# Plan then implement
"Plan auth system, then implement it completely"
→ prometheus (first) → sisyphus + ralph-loop (after)

# Persistent bug fixing
"Fix this bug, don't stop until it's done"
→ sisyphus + ralph-loop
```

**Sources:** [README.md L200-L280](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L200-L280)

## Project-Specific Usage

### Using .claude/CLAUDE.md

Create project-specific instructions in `.claude/CLAUDE.md`:

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

When I ask for features, follow these conventions automatically.
```

Now all agents will respect your project conventions.

**Sources:** [README.md L500-L550](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L500-L550)

### Team Collaboration

For team projects, commit `.claude/` to version control:

```bash
git add .claude/
git commit -m "Add team configuration and conventions"
```

Team members will have access to the same agents, commands, and project context.

## Tips and Best Practices

### Start with Planning

For complex tasks, start with `/plan`:

```bash
/plan implement a real-time chat feature
```

Prometheus will create a comprehensive plan that Sisyphus can execute.

### Use the Right Agent

* **Architecture questions** → Oracle
* **Documentation needs** → Librarian or Document Writer
* **Code searches** → Explore
* **UI changes** → Frontend Engineer
* **Visual analysis** → Multimodal Looker

### Leverage Magic Keywords

Use magic keywords for quick mode activation:

```bash
# Instead of /ultrawork
ultrawork implement the payment flow

# Instead of /deepsearch
find all database migrations

# Instead of /analyze
analyze the performance issue
```

### Trust the Orchestrator

Let Sisyphus delegate automatically:

```bash
# Good: Let Sisyphus decide
/sisyphus implement user authentication

# Less optimal: Micromanaging
Use oracle to design auth, then frontend-engineer to build it
```

**Sources:** [README.md L400-L500](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md#L400-L500)

## Next Steps

After mastering the basics:

1. **Architecture**: Understand system design. See [Architecture](../architecture/).
2. **Agents**: Learn about specialized agents. See [Agents](/agents/).
3. **Hooks**: Learn about lifecycle hooks. See [Hooks](../hooks/).
4. **Skills**: Learn about composable skills. See [Skills](../skills/).
5. **Commands**: Learn about all slash commands. See [Commands](../commands/).
