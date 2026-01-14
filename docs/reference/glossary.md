---
layout: default
title: Glossary
parent: Reference
nav_order: 1
---

# Glossary

Terminology and concepts used in oh-my-claude-sisyphus.

## A

### Agent
A specialized AI assistant with focused expertise and tools. Agents are spawned by the orchestrator to handle specific tasks.

**Examples:** oracle, librarian, explore, frontend-engineer

**See:** [Agents](agents/)

---

### Agent Delegation
The process of the orchestrator assigning work to specialized subagents via the Task tool.

---

### AGENTS.md
Project-specific agent definitions file. Defines or overrides agent behavior for a specific project.

**Location:** `.claude/AGENTS.md` or `~/.claude/AGENTS.md`

---

## B

### Background Execution
Asynchronous agent spawning where tasks run independently and notify upon completion.

**See:** [Background Execution](features/background-execution.md)

---

### Background Task
A task executed with `run_in_background=true` that runs independently of the main conversation flow.

**Limit:** Maximum 5 concurrent background tasks

---

### Boulder
Metaphor for the work that must be completed. From the Greek myth of Sisyphus, "the boulder never stops" represents persistent work until completion.

---

### Boulder State
The persistent state of an active plan, including tasks, progress, and notes.

**Location:** `~/.claude/.sisyphus/boulder.json`

---

## C

### CLAUDE.md
Project context file that provides instructions specific to a codebase.

**Location:** `.claude/CLAUDE.md` or `~/.claude/CLAUDE.md`

**See:** [Project Configuration](configuration/project-config.md)

---

### Context Injection
Automatic loading of project-specific instructions and rules based on file access patterns.

**See:** [Context Injection](features/context-injection.md)

---

## E

### Enhanced Mode
Behavior modifications triggered by magic keywords: ultrawork, search, or analyze.

---

### Execution Layer
The primary skill layer that determines how work is executed.

**Skills:** sisyphus, orchestrator, prometheus

---

## G

### Guarantee Layer
Optional skill layer that ensures completion.

**Skill:** ralph-loop

---

## H

### Hook
A script that executes at specific points during a Claude Code session.

**See:** [Hooks](../hooks/)

---

## K

### Keyword Detection
Automatic detection of trigger words (ultrawork, search, analyze) that activate enhanced modes.

**See:** [Magic Keywords](features/magic-keywords.md)

---

### Keyword Mode
An enhanced orchestration mode activated by detecting specific keywords in the user prompt.

---

## M

### Magic Keyword
A word that, when detected in a prompt, activates specialized orchestration behavior.

**Examples:** `ultrawork`, `search`, `analyze`

---

### Master Agent
In Claude Code, the fixed primary agent that coordinates all work. Unlike OpenCode, this cannot be swapped.

---

### Model Routing
The process of selecting the appropriate Claude model (opus, sonnet, haiku) based on task complexity.

---

## O

### Oracle
The specialized agent for architecture analysis and complex debugging.

**Model:** Claude Opus

---

### Orchestrator
The coordinator agent that delegates work to specialists without implementing directly.

---

## P

### Parallel Execution
Running multiple agents simultaneously to complete independent tasks faster.

---

### Primary Agent
The main Claude instance that handles user interaction and coordinates subagents.

---

## R

### Ralph Loop
Self-referential development loop that continues until all tasks are verified complete.

**Named for:** Ralph Waldo Emerson's quote on persistence

**See:** [ralph-loop command](commands/reference.md#ralph-loop-task)

---

### Rules File
Markdown file with YAML frontmatter that defines injection triggers and content.

**Location:** `.claude/rules/*.md`

---

## S

### Skill
A behavior injection that modifies how the primary agent operates.

**See:** [Skills](../skills/)

---

### Skill Activation
The process of invoking skills to modify agent behavior.

**Types:** Explicit (slash command), Automatic (keyword detection), Judgment-based (Claude decides)

---

### Skill Composition
Stacking multiple skills to combine their capabilities.

**Formula:** `[Execution] + [Enhancement] + [Guarantee]`

---

### Skill Layers
The three categories of skills: Execution, Enhancement, and Guarantee.

---

### Slash Command
A command starting with `/` that activates specific behaviors or skills.

**Examples:** `/sisyphus`, `/ultrawork`, `/plan`

**See:** [Commands](commands/)

---

### Subagent
An agent spawned by the primary agent to handle specific tasks.

---

### Sisyphus
The primary multi-agent orchestration mode. Named for the Greek mythological figure condemned to roll a boulder eternally.

---

### Sisyphus Junior
A focused execution agent for direct task implementation.

**Model:** Claude Sonnet

---

## T

### Task
A unit of work tracked in the todo list. Can be pending, in_progress, or completed.

---

### Todo Continuation
Enforcement mechanism that prevents session termination while incomplete tasks remain.

---

## U

### Ultrawork
Maximum performance mode with aggressive parallel agent execution.

**Magic Keywords:** `ultrawork`, `ulw`, `uw`

**See:** [Magic Keywords](features/magic-keywords.md#ultrawork-mode)

---

## V

### Verification
The process of validating that subagent claims and work are correct.

---

## Common Phrases

### "The boulder never stops"
A motto representing persistent work until completion. From the Sisyphus myth, adopted by the project.

---

### "Cannot stop until verified done"
The Ralph Loop principle that all todos must be complete before a session can end.

---

### "Delegate, don't implement"
The orchestrator's guiding principle to always assign work to specialists.

---

### "Trust but verify"
The approach to subagent work: use their output but validate with own tools.

---

## Model Terms

### Opus
The largest Claude model. Best for complex reasoning, architecture, and debugging.

**Cost:** Highest | **Speed:** Slowest

---

### Sonnet
The balanced Claude model. Good for implementation and analysis.

**Cost:** Medium | **Speed:** Medium

---

### Haiku
The smallest Claude model. Best for simple lookups and formatting.

**Cost:** Lowest | **Speed:** Fastest

---

## Related Documentation

- [Commands Reference](commands/reference.md) - All slash commands
- [Agents](agents/) - Agent specifications
- [Configuration](configuration/) - Configuration options
