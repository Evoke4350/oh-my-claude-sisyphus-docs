---
layout: default
title: SDK Usage
parent: Reference
nav_order: 2
---

# SDK Usage

Programmatic usage of oh-my-claude-sisyphus with the Claude Agent SDK.

## Overview

Oh-my-claude-sisyphus can be used programmatically via the `@anthropic-ai/claude-agent-sdk` package for advanced automation and integration scenarios.

## Installation

```bash
npm install oh-my-claude-sisyphus @anthropic-ai/claude-agent-sdk
```

## Basic Usage

### Create a Sisyphus Session

```typescript
import { createSisyphusSession } from 'oh-my-claude-sisyphus';

// Create a configured session
const session = createSisyphusSession({
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: 'claude-opus-4-5'
});
```

### Process a Prompt

```typescript
// Process prompt with Sisyphus enhancements
const processedPrompt = session.processPrompt(
  'ultrawork implement user authentication system'
);

console.log(processedPrompt);
// Output includes:
// - Activated skills (sisyphus + ultrawork)
// - Agent delegation plan
// - Todo list structure
```

### Execute Query

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk';

// Execute with Sisyphus configuration
for await (const message of query({
  prompt: session.processPrompt('refactor the API layer'),
  ...session.queryOptions
})) {
  console.log(message);
}
```

## Advanced Usage

### Custom Skill Activation

```typescript
const session = createSisyphusSession({
  skills: ['sisyphus', 'git-master', 'frontend-ui-ux']
});

// All three skills will be active
const result = await session.execute('Add dark mode component');
```

### Custom Agent Configuration

```typescript
const session = createSisyphusSession({
  agents: {
    oracle: {
      model: 'opus',
      promptAppend: 'Focus on security implications'
    },
    explore: {
      model: 'haiku',
      tools: ['Read', 'Grep', 'Glob']
    }
  }
});
```

### Background Task Management

```typescript
const session = createSisyphusSession({
  maxBackgroundTasks: 10
});

// Spawn background tasks
const taskId1 = await session.spawnBackgroundTask({
  agent: 'explore',
  task: 'Find all API endpoints'
});

const taskId2 = await session.spawnBackgroundTask({
  agent: 'librarian',
  task: 'Research authentication best practices'
});

// Wait for results
const results = await Promise.all([
  session.getTaskResult(taskId1),
  session.getTaskResult(taskId2)
]);
```

## Session Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `apiKey` | `string` | Required | Anthropic API key |
| `model` | `string` | `claude-opus-4-5` | Default model to use |
| `skills` | `string[]` | `[]` | Skills to activate |
| `agents` | `object` | `{}` | Agent configurations |
| `maxBackgroundTasks` | `number` | `5` | Max concurrent tasks |
| `todoEnforcement` | `boolean` | `true` | Enforce completion |
| `autoUpdate` | `boolean` | `true` | Enable auto-update |

## Skill Combinations

```typescript
// Execution + Enhancement
createSisyphusSession({
  skills: ['sisyphus', 'ultrawork', 'git-master']
});

// Planning + Guarantee
createSisyphusSession({
  skills: ['prometheus', 'ralph-loop']
});

// All layers
createSisyphusSession({
  skills: [
    'sisyphus',      // Execution
    'ultrawork',     // Enhancement
    'frontend-ui-ux', // Enhancement
    'ralph-loop'     // Guarantee
  ]
});
```

## Error Handling

```typescript
try {
  const result = await session.execute('complex task');
} catch (error) {
  if (error instanceof SisyphusError) {
    console.error('Sisyphus error:', error.message);
    console.error('Failed tasks:', error.failedTasks);
    console.error('Remaining todos:', error.remainingTodos);
  }
}
```

## State Management

### Save Session State

```typescript
const state = session.saveState();
fs.writeFileSync('.sisyphus/session.json', JSON.stringify(state, null, 2));
```

### Load Session State

```typescript
const state = JSON.parse(
  fs.readFileSync('.sisyphus/session.json', 'utf-8')
);
const session = createSisyphusSession({ state });
```

## Integration Examples

### With Express

```typescript
import express from 'express';
import { createSisyphusSession } from 'oh-my-claude-sisyphus';

const app = express();
const session = createSisyphusSession();

app.post('/api/task', async (req, res) => {
  const { task } = req.body;

  try {
    const result = await session.execute(task);
    res.json({ success: true, result });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

### With CLI Tool

```typescript
#!/usr/bin/env node
import { createSisyphusSession } from 'oh-my-claude-sisyphus';

const args = process.argv.slice(2);
const task = args.join(' ');

const session = createSisyphusSession();
const result = await session.execute(task);

console.log(result);
```

### With GitHub Actions

```yaml
- name: Run Sisyphus
  run: |
    node -e "
    const { createSisyphusSession } = require('oh-my-claude-sisyphus');
    const session = createSisyphusSession();
    session.execute('Review pull request for issues').then(console.log);
    "
```

## TypeScript Types

```typescript
import type {
  SisyphusSession,
  SisyphusSessionOptions,
  SisyphusResult,
  BackgroundTask,
  TodoItem,
  SkillName,
  AgentName
} from 'oh-my-claude-sisyphus';

// Type definitions available
const options: SisyphusSessionOptions = {
  apiKey: 'sk-ant-...',
  model: 'claude-opus-4-5',
  skills: ['sisyphus', 'ultrawork']
};

const session: SisyphusSession = createSisyphusSession(options);
```

## Best Practices

1. **API Key Security**
   ```typescript
   // Use environment variables
   const apiKey = process.env.ANTHROPIC_API_KEY;
   ```

2. **Error Recovery**
   ```typescript
   // Implement retry logic
   retry(() => session.execute(task), { maxAttempts: 3 });
   ```

3. **Resource Management**
   ```typescript
   // Clean up sessions
   const session = createSisyphusSession();
   try {
     await session.execute(task);
   } finally {
     await session.cleanup();
   }
   ```

4. **State Persistence**
   ```typescript
   // Save progress for long-running tasks
   session.on('progress', (state) => {
     saveState(state);
   });
   ```

## API Reference

### createSisyphusSession(options)

Creates a new Sisyphus session with the given options.

**Parameters:**
- `options: SisyphusSessionOptions` - Configuration options

**Returns:** `SisyphusSession`

### session.execute(task)

Executes a task using Sisyphus orchestration.

**Parameters:**
- `task: string` - Task description

**Returns:** `Promise<SisyphusResult>`

### session.processPrompt(prompt)

Processes a prompt to extract skill activation and task structure.

**Parameters:**
- `prompt: string` - Raw user prompt

**Returns:** `ProcessedPrompt`

### session.spawnBackgroundTask(options)

Spawns a background task.

**Parameters:**
- `options.agent: string` - Agent name
- `options.task: string` - Task description

**Returns:** `Promise<string>` - Task ID

## Related Documentation

- [Configuration Reference](configuration/reference.md) - Configuration options
- [Commands](commands/) - Slash command equivalents
- [Agents](agents/) - Agent specifications
