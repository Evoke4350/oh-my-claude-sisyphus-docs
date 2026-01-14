---
layout: default
title: Command Reference
parent: Commands
nav_order: 2
---

# Command Reference

Complete reference for all twelve oh-my-claude-sisyphus slash commands.

## Orchestration Commands

### `/sisyphus <task>`

Activates the Sisyphus multi-agent orchestration mode for complex task execution.

**Description:** Sisyphus is the primary orchestration mode that coordinates multiple specialized agents to complete complex tasks. It manages todo lists, delegates to subagents, and verifies completion.

**Usage:**
```bash
/sisyphus <task description>
```

**Examples:**
```bash
/sisyphus refactor the authentication module
/sisyphus implement user registration with email verification
/sisyphus add pagination to the API endpoints
```

**Behavior:**
- Creates structured todo list for task tracking
- Delegates to specialized agents (oracle, librarian, explore, etc.)
- Enforces task completion before stopping
- Verifies all subagent claims

**Activates Skills:**
- sisyphus (primary execution)
- May trigger: git-master, frontend-ui-ux based on task type

**See Also:** [Agents Overview](../agents/overview.md)

---

### `/sisyphus-default`

Sets Sisyphus as the persistent default mode for all conversations.

**Description:** Makes Sisyphus orchestration active by default in all sessions without requiring explicit command invocation.

**Usage:**
```bash
/sisyphus-default
```

**Effect:**
- Sisyphus behaviors apply to all conversations
- Todo list enforcement is always active
- Agent delegation happens automatically based on task complexity
- Can be overridden by specific slash commands

**To Disable:** Remove or modify the default configuration in `~/.claude/settings.json`

---

### `/orchestrator <task>`

Activates master coordinator mode for complex multi-step tasks.

**Description:** The orchestrator skill focuses on delegation-only coordination, routing tasks to appropriate specialists while maintaining oversight.

**Usage:**
```bash
/orchestrator <task description>
```

**Examples:**
```bash
/orchestrator design and implement the payment flow
/orchestrator migrate the database and update all API calls
```

**Behavior:**
- Never implements directly
- Always delegates to subagents
- Coordinates parallel execution
- Validates subagent outputs

**Activates Skills:**
- orchestrator (primary)
- May combine with: ultrawork for parallel tasks

---

## Performance Commands

### `/ultrawork <task>`

Maximum performance mode with aggressive parallel agent execution.

**Description:** Activates parallel orchestration with extended thinking budgets and background task delegation. Designed for complex, multi-faceted tasks where speed is critical.

**Usage:**
```bash
/ultrawork <task description>
```

**Examples:**
```bash
/ultrawork refactor the entire API layer
/ultrawork implement user dashboard with charts and tables
```

**Behavior:**
- Aggressive parallel agent spawning
- Extended thinking budgets
- Background task delegation for frontend/librarian/explore
- Higher risk tolerance for faster iteration

**Activates Skills:**
- ultrawork (enhancement)
- sisyphus (execution)
- May combine with: git-master, frontend-ui-ux

**Magic Keywords:** `ultrawork`, `ulw`, `uw`

---

### `/deepsearch <query>`

Thorough multi-strategy codebase search across multiple sources.

**Description:** Launches parallel search agents with maximized tool access for comprehensive codebase exploration.

**Usage:**
```bash
/deepsearch <search query>
```

**Examples:**
```bash
/deepsearch API endpoints that handle user data
/deepsearch all files using deprecated functions
/deepsearch authentication flow implementation
```

**Behavior:**
- Parallel librarian and explore agent launch
- Full tool access (LSP, AST-grep, MCPs)
- No waiting during search execution
- Aggregates and synthesizes findings

**Tools Utilized:**
- LSP: symbol search, references, definitions
- AST-grep: pattern matching across 25+ languages
- MCPs: context7 (docs), websearch_exa, grep_app

**Activates Skills:**
- sisyphus (coordination)
- Enhanced search behavior

---

### `/analyze <target>`

Deep analysis and investigation with multi-phase expert consultation.

**Description:** Activates extended thinking with blocking expert consultation for debugging, architecture decisions, and complex problem-solving.

**Usage:**
```bash
/analyze <target>
```

**Examples:**
```bash
/analyze performance bottleneck in the database layer
/analyze why the tests are failing
/analyze authentication security vulnerabilities
```

**Behavior:**
- Extended thinking budget
- Proactive oracle invocation
- Blocking expert consultation (librarian, explore)
- Cross-validation of findings
- Evidence-based conclusions

**Analysis Phases:**
1. Problem decomposition
2. Expert consultation (oracle, librarian, explore)
3. Synthesis and cross-validation
4. Recommendation with trade-off analysis

**Activates Skills:**
- sisyphus (coordination)
- Enhanced analysis behavior

**Magic Keywords:** `analyze`, `investigate`

---

## Planning Commands

### `/plan <description>`

Start planning session with Prometheus for strategic planning.

**Description:** Prometheus conducts interview-style requirement gathering and creates comprehensive work plans before implementation.

**Usage:**
```bash
/plan <feature or system description>
```

**Examples:**
```bash
/plan user authentication system with OAuth
/plan real-time notification system
```

**Behavior:**
- Interviews user about requirements
- Explores constraints and preferences
- Creates structured implementation plan
- Identifies hidden requirements and risks

**Output:**
- Comprehensive work plan
- Task breakdown with dependencies
- Risk assessment
- Recommended execution order

**Activates Skills:**
- prometheus (primary execution)

**See Also:** `/review` for plan evaluation

---

### `/review [plan-path]`

Review a plan with Momus for critical evaluation.

**Description:** Momus provides critical analysis of plans, identifying flaws, feasibility issues, and overlooked requirements.

**Usage:**
```bash
/review [plan-path]
```

**Examples:**
```bash
/review
/review .sisyphus/plans/authentication-plan.md
```

**Behavior:**
- Critical evaluation of plan structure
- Feasibility assessment
- Risk identification
- Suggests improvements
- Challenges assumptions

**Review Focus:**
- Completeness
- Logical consistency
- Technical feasibility
- Risk assessment
- Missing requirements

**Activates Skills:**
- momus (primary execution)

---

### `/prometheus <task>`

Strategic planning with interview workflow (alias for /plan).

**Description:** Direct invocation of Prometheus skill for strategic planning tasks.

**Usage:**
```bash
/prometheus <task description>
```

**Behavior:** Identical to `/plan`

**When to Use:**
- Need structured planning before implementation
- Complex feature with many dependencies
- Want to explore multiple approaches
- Require comprehensive documentation

---

## Loop Commands

### `/ralph-loop <task>`

Self-referential development loop until task completion.

**Description:** Ralph Loop ensures continuous work until the task is verified complete. The system prevents stopping with incomplete todos.

**Usage:**
```bash/ralph-loop <task description>
```

**Examples:**
```bash
/ralph-loop fix the failing tests
/ralph-loop implement OAuth integration completely
```

**Behavior:**
- Cannot stop until all todos complete
- Self-verification of completion
- Continues through failures
- Enforces "THE BOULDER NEVER STOPS" principle

**Completion Criteria:**
- Zero pending/in_progress tasks
- All functionality working
- Tests passing (if applicable)
- Zero unaddressed errors

**Activates Skills:**
- ralph-loop (guarantee layer)
- sisyphus (execution)

**To Cancel:** Use `/cancel-ralph`

---

### `/cancel-ralph`

Cancel active Ralph Loop.

**Description:** Stops the Ralph Loop enforcement mechanism, allowing normal session termination.

**Usage:**
```bash
/cancel-ralph
```

**Effect:**
- Disables todo continuation enforcement
- Allows session to stop with incomplete tasks
- Resets Ralph Loop state

**When to Use:**
- Task needs to be paused
- Changing direction mid-task
- External blockers prevent completion

---

## Maintenance Commands

### `/update`

Check for and install oh-my-claude-sisyphus updates.

**Description:** Manually trigger update check and installation. The system also includes silent auto-update.

**Usage:**
```bash
/update
```

**Behavior:**
- Checks npm registry for new versions
- Downloads and installs updates
- Reports changes in new version
- No restart required (hooks update on next session)

**Auto-Update:**
- Automatic checks every 24 hours
- Rate-limited to prevent disruption
- Concurrent-safe with lock file
- Cross-platform support

**See Also:** [Auto-Update Feature](../features/auto-update.md)

---

## Command Quick Reference

| Command | Category | Skills Activated | Parallel |
|---------|----------|------------------|----------|
| `/sisyphus` | Orchestration | sisyphus | As needed |
| `/sisyphus-default` | Orchestration | sisyphus | N/A |
| `/orchestrator` | Orchestration | orchestrator | Yes |
| `/ultrawork` | Performance | ultrawork + sisyphus | Aggressive |
| `/deepsearch` | Search | sisyphus (enhanced) | Yes |
| `/analyze` | Analysis | sisyphus (enhanced) | No |
| `/plan` | Planning | prometheus | No |
| `/review` | Planning | momus | No |
| `/prometheus` | Planning | prometheus | No |
| `/ralph-loop` | Loop | ralph-loop + sisyphus | As needed |
| `/cancel-ralph` | Loop | (disables) | N/A |
| `/update` | Maintenance | N/A | N/A |

---

## Related Documentation

- [Magic Keywords](../features/magic-keywords.md) - Keyword-based command alternatives
- [Skills](../skills/) - Built-in skill documentation
- [Hooks](../hooks/) - Lifecycle hooks that support commands
