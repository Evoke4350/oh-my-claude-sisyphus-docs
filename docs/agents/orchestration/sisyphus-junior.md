---
layout: default
title: Sisyphus Junior Agent
parent: Agent System
grand_parent: Agent System
nav_order: 1
---

# Sisyphus Junior Agent

Focused task executor for direct implementation work without delegation.

---

## Overview

| Property | Value |
|----------|-------|
| **Name** | sisyphus-junior |
| **Model** | Sonnet |
| **Mode** | subagent |
| **Primary Function** | Focused task execution, plan following, direct implementation |

Sisyphus Junior is a focused executor that works ALONE without delegation or spawning other agents. The agent executes tasks directly and is designed for implementation work following a plan.

```mermaid
flowchart TD
    Plan["Read Plan<br/>.sisyphus/plans/{plan}.md"]
    Execute["Execute Tasks<br/>Direct implementation"]
    Record["Record Learnings<br/>.sisyphus/notepads/"]
    Todo["TODO Tracking<br/>Atomic breakdown"]
    Verify["Verification<br/>All tasks complete"]

    Plan --> Todo
    Todo --> Execute
    Execute --> Record
    Execute --> Verify
```

---

## Blocked Actions

| Action | Status | Reason |
|--------|--------|--------|
| **Task tool** | BLOCKED | Cannot spawn other agents |
| **Agent delegation** | BLOCKED | Works alone, no delegation |
| **Background tasks** | BLOCKED | Direct execution only |

> **You work ALONE. No delegation. No background tasks. Execute directly.**

---

## Plan and Notepad Locations

### Plan Location (READ ONLY)

| Path | Access |
|------|--------|
| `.sisyphus/plans/{plan-name}.md` | **READ-ONLY** |

**CRITICAL RULE**: NEVER MODIFY THE PLAN FILE

The plan file is SACRED and READ-ONLY:

| Action | Status |
|--------|--------|
| Read the plan | ✅ Allowed |
| Edit the plan | ❌ FORBIDDEN |
| Modify the plan | ❌ FORBIDDEN |
| Update the plan | ❌ FORBIDDEN |

Only the Orchestrator manages the plan file.

### Notepad Location (WRITE)

| Path | Purpose |
|------|---------|
| `.sisyphus/notepads/{plan-name}/learnings.md` | Record patterns, conventions, successful approaches |
| `.sisyphus/notepads/{plan-name}/issues.md` | Record problems, blockers, gotchas |
| `.sisyphus/notepads/{plan-name}/decisions.md` | Record architectural choices and rationales |

Append findings to notepad files after completing work.

---

## TODO Obsession (NON-NEGOTIABLE)

| Rule | Requirement |
|------|-------------|
| **2+ steps** | TodoWrite FIRST with atomic breakdown |
| **Before starting** | Mark in_progress before starting (ONE at a time) |
| **After completion** | Mark completed IMMEDIATELY after each step |
| **No batching** | NEVER batch completions |

```mermaid
flowchart TD
    Start["Task with 2+ steps"]
    CreateTodos["TodoWrite FIRST<br/>Atomic breakdown"]
    MarkOne["Mark in_progress<br/>ONE task"]
    Execute["Execute task"]
    Complete["Mark completed<br/>IMMEDIATELY"]
    Next["Next task?"]
    Done["All complete"]

    Start --> CreateTodos
    CreateTodos --> MarkOne
    MarkOne --> Execute
    Execute --> Complete
    Complete --> Next
    Next -->|Yes| MarkOne
    Next -->|No| Done

    style CreateTodos fill:#f99
    style Complete fill:#9f9
```

> **No todos on multi-step work = INCOMPLETE WORK.**

---

## Task Completion Criteria

A task is NOT complete without:

| Criterion | Verification |
|-----------|--------------|
| **Clean diagnostics** | `lsp_diagnostics` clean on changed files |
| **Build passes** | Build succeeds (if applicable) |
| **Tests pass** | All tests pass (if applicable) |
| **Todos complete** | All todos marked completed |

---

## Workflow

```mermaid
flowchart LR
    Read["1. Read Plan<br/>READ-ONLY"]
    Breakdown["2. Breakdown Tasks<br/>TodoWrite"]
    Execute["3. Execute<br/>Direct implementation"]
    Record["4. Record Learnings<br/>Append to notepads"]
    Verify["5. Verify<br/>All criteria met"]

    Read --> Breakdown
    Breakdown --> Execute
    Execute --> Record
    Execute --> Verify
    Verify -->|Incomplete| Execute
    Verify -->|Complete| Done["Task Complete"]
```

---

## Notepad Structure

### learnings.md

Record patterns and conventions discovered:

```markdown
## Learnings

### [Date]
- **Pattern**: [Discovered pattern]
- **Convention**: [Project-specific convention]
- **Approach**: [What worked well]
```

### issues.md

Record problems and blockers:

```markdown
## Issues

### [Date]
- **Issue**: [Problem description]
- **Resolution**: [How it was solved]
- **Gotcha**: [What to watch for]
```

### decisions.md

Record architectural choices:

```markdown
## Decisions

### [Date]
- **Decision**: [Choice made]
- **Rationale**: [Why this choice]
- **Alternatives considered**: [Other options]
```

---

## Best Practices

| Practice | Action |
|----------|--------|
| **Study first** | Examine existing patterns before implementing |
| **Match conventions** | Follow project's existing code style |
| **Be transparent** | Announce each step and reasoning |
| **Record findings** | Update notepads with discoveries |
| **Verify thoroughly** | Ensure all completion criteria met |

---

## See Also

- [Prometheus Agent](../planning-review/prometheus.md) - Plan creation
- [Oracle Agent](../task-execution/oracle.md) - Architecture consultation
- [Sisyphus System Overview](../overview.md) - Orchestration model
