---
layout: default
title: LSP Tools
parent: Tools
nav_order: 2
---

# LSP Tools

> **Relevant source files**
> * [README.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md)

LSP (Language Server Protocol) tools provide IDE-level code intelligence through integration with language servers.

## Overview

oh-my-claude-sisyphus includes 11 LSP operations for code analysis and refactoring:

| Category | Tools |
|----------|-------|
| **Analysis** | hover, goto_definition, find_references, document_symbols, workspace_symbols, diagnostics, lsp_servers |
| **Refactoring** | prepare_rename, rename, code_actions, code_action_resolve |

## Analysis Tools

### lsp_hover

Get type information, documentation, and function signatures at a cursor position.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "position": {
    "line": 42,
    "character": 10
  }
}
```

**Output:**

```typescript
{
  "contents": "string | number - The user ID",
  "range": {
    "start": { "line": 42, "character": 8 },
    "end": { "line": 42, "character": 14 }
  }
}
```

**Use Cases:**

- Understanding variable types
- Viewing function documentation
- Checking parameter types

---

### lsp_goto_definition

Jump to the definition of a symbol.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "position": {
    "line": 10,
    "character": 5
  }
}
```

**Output:**

```typescript
{
  "uri": "file:///path/to/definition.ts",
  "range": {
    "start": { "line": 5, "character": 0 },
    "end": { "line": 5, "character": 20 }
  }
}
```

**Use Cases:**

- Finding where functions are defined
- Locating class/interface declarations
- Navigating to imported modules

---

### lsp_find_references

Find all usages of a symbol across the codebase.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "position": {
    "line": 15,
    "character": 8
  }
}
```

**Output:**

```typescript
[
  {
    "uri": "file:///path/to/file.ts",
    "range": {
      "start": { "line": 15, "character": 8 },
      "end": { "line": 15, "character": 14 }
    }
  },
  {
    "uri": "file:///path/to/other.ts",
    "range": {
      "start": { "line": 3, "character": 10 },
      "end": { "line": 3, "character": 16 }
    }
  }
]
```

**Use Cases:**

- Impact analysis before refactoring
- Finding all callers of a function
- Identifying unused code

---

### lsp_document_symbols

Get a structured outline of symbols in a file.

**Input:**

```typescript
{
  "path": "/path/to/file.ts"
}
```

**Output:**

```typescript
[
  {
    "name": "UserService",
    "kind": "class",
    "range": { "start": {"line": 0}, "end": {"line": 50} },
    "children": [
      {
        "name": "login",
        "kind": "method",
        "range": { "start": {"line": 10}, "end": {"line": 20} }
      }
    ]
  }
]
```

**Symbol Kinds:**

| Kind | Description |
|------|-------------|
| `class` | Class declaration |
| `interface` | Interface declaration |
| `function` | Function declaration |
| `method` | Method declaration |
| `variable` | Variable declaration |
| `property` | Property declaration |

**Use Cases:**

- Understanding file structure
- Finding specific functions/classes
- Code navigation

---

### lsp_workspace_symbols

Search for symbols by name across the entire workspace.

**Input:**

```typescript
{
  "query": "AuthService"
}
```

**Output:**

```typescript
[
  {
    "name": "AuthService",
    "kind": "class",
    "path": "src/auth/AuthService.ts",
    "range": {
      "start": { "line": 0, "character": 0 },
      "end": { "line": 100, "character": 1 }
    }
  }
]
```

**Use Cases:**

- Finding where symbols are declared
- Locating specific classes/functions
- Cross-referencing symbols

---

### lsp_diagnostics

Get errors, warnings, and hints for a file.

**Input:**

```typescript
{
  "path": "/path/to/file.ts"
}
```

**Output:**

```typescript
[
  {
    "range": {
      "start": { "line": 10, "character": 5 },
      "end": { "line": 10, "character": 10 }
    },
    "severity": "error",
    "message": "Cannot find name 'User'"
  }
]
```

**Severity Levels:**

| Level | Description |
|-------|-------------|
| `error` | Errors that prevent compilation |
| `warning` | Potential issues |
| `information` | Info messages |
| `hint` | Suggestions |

**Use Cases:**

- Pre-commit validation
- Finding errors without building
- Code quality checks

---

### lsp_servers

List available language servers and their status.

**Input:**

```typescript
{}
```

**Output:**

```typescript
[
  {
    "name": "typescript-language-server",
    "running": true,
    "extensions": [".ts", ".tsx"],
    "priority": 10
  },
  {
    "name": "pylsp",
    "running": false,
    "extensions": [".py"]
  }
]
```

**Use Cases:**

- Verifying LSP server installation
- Checking which servers are active
| Troubleshooting LSP issues |

## Refactoring Tools

### lsp_prepare_rename

Validate a rename operation before executing it.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "position": {
    "line": 5,
    "character": 10
  }
}
```

**Output:**

```typescript
{
  "canRename": true,
  "placeholder": "currentName"
}
```

**Error Output:**

```typescript
{
  "canRename": false,
  "error": "Cannot rename language keywords"
}
```

**Use Cases:**

- Safety check before renaming
| Checking if rename is valid |

---

### lsp_rename

Rename a symbol across the entire workspace.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "position": {
    "line": 5,
    "character": 10
  },
  "newName": "NewClassName"
}
```

**Output:**

```typescript
{
  "changes": {
    "file:///path/to/file.ts": [
      {
        "range": {
          "start": { "line": 5, "character": 8 },
          "end": { "line": 5, "character": 18 }
        },
        "newText": "NewClassName"
      }
    ],
    "file:///path/to/other.ts": [
      {
        "range": { "start": {"line": 3}, "end": {"line": 3} },
        "newText": "NewClassName"
      }
    ]
  }
}
```

**Workflow:**

1. Use `lsp_prepare_rename` to validate
2. Use `lsp_rename` with new name
3. LSP calculates all workspace changes
4. Apply changes atomically

**Use Cases:**

| Renaming functions across files |
| Changing class names |
| Refactoring variable names |

---

### lsp_code_actions

Get available quick fixes and refactorings for a code location.

**Input:**

```typescript
{
  "path": "/path/to/file.ts",
  "range": {
    "start": { "line": 10, "character": 0 },
    "end": { "line": 10, "character": 20 }
  }
}
```

**Output:**

```typescript
[
  {
    "kind": "quickfix",
    "title": "Add missing import",
    "edit": { /* workspace edit */ }
  },
  {
    "kind": "refactor.extract.function",
    "title": "Extract to function",
    "edit": { /* workspace edit */ }
  }
]
```

**Action Kinds:**

| Kind | Description |
|------|-------------|
| `quickfix` | Fix errors or warnings |
| `refactor` | General refactoring |
| `refactor.extract` | Extract method/variable |
| `refactor.inline` | Inline variable/method |
| `refactor.rewrite` | Rewrite structure |
| `source` | Source-level actions |

**Use Cases:**

| Discovering available fixes |
| Finding refactoring opportunities |
| Organizing imports |

---

### lsp_code_action_resolve

Execute a specific code action.

**Input:**

```typescript
{
  "codeAction": {
    "kind": "quickfix",
    "title": "Add missing import"
  }
}
```

**Output:**

```typescript
{
  "edit": {
    "changes": {
      "file:///path/to/file.ts": [
        {
          "range": { "start": {"line": 0}, "end": {"line": 0} },
          "newText": "import { User } from './types';\n"
        }
      ]
    }
  }
}
```

**Use Cases:**

| Applying quick fixes |
| Executing refactorings |
| Auto-fixing diagnostics |

## LSP Server Configuration

### Configuration File

Configure LSP servers in `~/.claude/config.json`:

```json
{
  "lsp": {
    "typescript-language-server": {
      "command": ["typescript-language-server", "--stdio"],
      "extensions": [".ts", ".tsx", ".js", ".jsx"],
      "priority": 10,
      "disabled": false
    },
    "pylsp": {
      "command": ["pylsp"],
      "extensions": [".py"],
      "priority": 5,
      "env": {
        "PYTHONPATH": "/usr/lib/python3.11/site-packages"
      }
    },
    "rust-analyzer": {
      "command": ["rust-analyzer"],
      "extensions": [".rs"],
      "disabled": false
    }
  }
}
```

### Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `command` | `string[]` | Command and arguments to start server |
| `extensions` | `string[]` | File extensions this server handles |
| `priority` | `number` | Server priority when multiple match |
| `env` | `object` | Environment variables for server process |
| `initialization` | `object` | LSP initialization options |
| `disabled` | `boolean` | Disable this server |

### Server Priority

When multiple servers match a file extension, the highest priority wins:

```json
{
  "lsp": {
    "typescript-language-server": {
      "extensions": [".ts"],
      "priority": 10
    },
    "vtsls": {
      "extensions": [".ts"],
      "priority": 20
    }
  }
}
```

In this example, `vtsls` (priority 20) wins over `typescript-language-server` (priority 10).

## Tool Reference Table

| Tool | LSP Method | Modifies Code | Server Required |
|------|------------|---------------|-----------------|
| lsp_hover | textDocument/hover | No | Yes |
| lsp_goto_definition | textDocument/definition | No | Yes |
| lsp_find_references | textDocument/references | No | Yes |
| lsp_document_symbols | textDocument/documentSymbol | No | Yes |
| lsp_workspace_symbols | workspace/symbol | No | Yes |
| lsp_diagnostics | textDocument/diagnostic | No | Yes |
| lsp_servers | - | No | No |
| lsp_prepare_rename | textDocument/prepareRename | No | Yes |
| lsp_rename | textDocument/rename | Yes | Yes |
| lsp_code_actions | textDocument/codeAction | No | Yes |
| lsp_code_action_resolve | codeAction/resolve | Yes | Yes |

## Further Reading

- [AST Tools](ast-tools.md) - Pattern-based code search and transform
- [Built-in Tools](built-in-tools.md) - Native Claude Code tools reference
- [Tool Overview](overview.md) - Tool ecosystem overview
