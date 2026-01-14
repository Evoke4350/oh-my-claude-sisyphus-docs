---
layout: default
title: Commands Overview
nav_order: 1
---

# Commands Overview

Oh-my-claude-sisyphus provides twelve slash commands that enable powerful multi-agent orchestration capabilities. These commands activate specialized skills and workflows optimized for different task types.

## Command Categories

### Orchestration Commands

| Command | Purpose |
|---------|---------|
| `/sisyphus` | Activate the primary multi-agent orchestration mode |
| `/sisyphus-default` | Set Sisyphus as the persistent default mode |
| `/orchestrator` | Complex multi-step task coordination |

### Performance Commands

| Command | Purpose |
|---------|---------|
| `/ultrawork` | Maximum performance mode with parallel agent execution |
| `/deepsearch` | Thorough multi-strategy codebase search |
| `/analyze` | Deep analysis and investigation |

### Planning Commands

| Command | Purpose |
|---------|---------|
| `/plan` | Start planning session with Prometheus |
| `/review` | Review a plan with Momus |
| `/prometheus` | Strategic planning with interview workflow |

### Loop Commands

| Command | Purpose |
|---------|---------|
| `/ralph-loop` | Self-referential development loop until completion |
| `/cancel-ralph` | Cancel active Ralph Loop |

### Maintenance Commands

| Command | Purpose |
|---------|---------|
| `/update` | Check for and install updates |

## Skill Activation Model

Commands in oh-my-claude-sisyphus follow an intelligent skill activation model. Skills are composable and stack based on task requirements:

```
[Execution Layer] + [Enhancement Layer] + [Guarantee Layer]
```

| Layer | Skills | Purpose |
|-------|--------|---------|
| **Execution** | sisyphus, orchestrator, prometheus | Primary work mode |
| **Enhancement** | ultrawork, git-master, frontend-ui-ux | Additional capabilities |
| **Guarantee** | ralph-loop | Ensures completion |

## Usage Pattern

Commands can be used in three ways:

### 1. Explicit Slash Commands

```bash
# Direct activation
/sisyphus refactor the authentication module

# With task specification
/ultrawork implement user dashboard with charts
```

### 2. Magic Keywords

```bash
# Keywords work in normal prompts
ultrawork implement user authentication

# No slash required
find all files that import the utils module
```

### 3. Skill Stacking

```bash
# Multiple capabilities combined
/sisyphus Add dark mode with proper git commits
# Activates: sisyphus + frontend-ui-ux + git-master
```

## Command vs Magic Keyword

| Aspect | Slash Command | Magic Keyword |
|--------|---------------|---------------|
| **Activation** | Explicit `/command` | Keyword in prompt |
| **Priority** | Always takes precedence | Secondary to slash |
| **Visibility** | Clear intent shown | Implicit activation |
| **Use Case** | Deliberate mode selection | Natural workflow |

## See Also

- [Command Reference](reference/) - Detailed command documentation
- [Magic Keywords](/features/magic-keywords/) - Keyword-based activation
- [Skills](../skills/) - Built-in skill documentation
