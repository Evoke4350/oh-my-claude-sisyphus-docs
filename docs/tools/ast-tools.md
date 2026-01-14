---
layout: default
title: AST Tools
parent: Tools
nav_order: 3
---

# AST Tools

> **Relevant source files**
> * [README.md](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus/blob/main/README.md)

AST (Abstract Syntax Tree) tools provide structural code search and transformation using the ast-grep engine.

## Overview

AST tools enable pattern-based code operations that understand code structure:

| Tool | Description | Engine |
|------|-------------|--------|
| `ast_grep_search` | Pattern-based AST search | ast-grep |
| `ast_grep_replace` | Pattern-based AST transform | ast-grep |

## Why AST Tools?

Unlike text-based search (grep), AST tools understand code structure:

```typescript
// Text search: finds "foo" anywhere
grep "foo" src/

// AST search: finds only function calls named foo
ast_grep_search: $FOO($$$)
```

## Meta-Variables

AST patterns use special meta-variables for matching:

| Variable | Matches | Example |
|----------|---------|---------|
| `$NAME` | Single named node | `function $NAME()` matches any function name |
| `$$$` | Multiple nodes | `import $$$ from 'react'` matches any import |
| `$_` | Any single node | `const $_ = expr` matches any variable name |

### Meta-Variable Examples

```
# Match any function declaration
function $NAME($$$) { $$$ }

# Match any React component
function $NAME($$$): JSX.Element { $$$ }

# Match any const declaration with await
const $VAR = await $EXPR

# Match any import statement
import $$$ from '$MODULE'
```

## ast_grep_search

Search for code patterns using AST matching.

### Input Format

```typescript
{
  "pattern": "function $NAME($$$) { $$$ }",
  "languages": ["typescript", "javascript"],
  "paths": ["src/**/*.ts"],
  "exclude": ["**/*.test.ts"]
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `pattern` | `string` | AST pattern to match (required) |
| `languages` | `string[]` | Languages to search (default: auto-detect) |
| `paths` | `string[]` | Files/directories to search |
| `exclude` | `string[]` | Patterns to exclude |
| `include` | `string[]` | Patterns to include |

### Output Format

```typescript
[
  {
    "file": "src/auth/login.ts",
    "line": 10,
    "column": 0,
    "match": "function login(user: User): void {",
    "metaVars": {
      "NAME": "login"
    }
  },
  {
    "file": "src/auth/logout.ts",
    "line": 5,
    "column": 0,
    "match": "function logout(): void {",
    "metaVars": {
      "NAME": "logout"
    }
  }
]
```

### Supported Languages

| Language | Identifier |
|----------|------------|
| TypeScript | `typescript`, `ts` |
| JavaScript | `javascript`, `js` |
| Python | `python`, `py` |
| Rust | `rust`, `rs` |
| Go | `go` |
| Java | `java` |
| C/C++ | `c`, `cpp` |
| Ruby | `ruby`, `rb` |

### Usage Examples

**Find all functions with `user` parameter:**

```
ast_grep_search:
  pattern: function $NAME(user: $TYPE, $$$) { $$$ }
  languages: [typescript]
```

**Find all console.log calls:**

```
ast_grep_search:
  pattern: console.log($$$)
  languages: [typescript, javascript]
```

**Find all async functions without error handling:**

```
ast_grep_search:
  pattern: async function $NAME($$$) { $$$ }
  languages: [typescript]
```

## ast_grep_replace

Transform code using AST pattern matching and replacement.

### Input Format

```typescript
{
  "pattern": "console.log($MSG)",
  "replacement": "logger.info($MSG)",
  "languages": ["typescript"],
  "paths": ["src/**/*.ts"],
  "dryRun": false
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `pattern` | `string` | AST pattern to match (required) |
| `replacement` | `string` | Replacement pattern (required) |
| `languages` | `string[]` | Languages to transform |
| `paths` | `string[]` | Files/directories to transform |
| `exclude` | `string[]` | Patterns to exclude |
| `dryRun` | `boolean` | Preview changes without writing |

### Output Format

```typescript
{
  "changes": [
    {
      "file": "src/utils/logger.ts",
      "line": 5,
      "original": "console.log('User logged in')",
      "replacement": "logger.info('User logged in')"
    }
  ],
  "totalFiles": 1,
  "totalChanges": 3
}
```

### Usage Examples

**Replace var with const:**

```
ast_grep_replace:
  pattern: var $NAME = $VALUE
  replacement: const $NAME = $VALUE
  languages: [javascript, typescript]
```

**Convert function to arrow function:**

```
ast_grep_replace:
  pattern: function $NAME($$$) { return $RET; }
  replacement: const $NAME = ($$$) => $RET
  languages: [typescript]
```

**Add type annotation to function parameters:**

```
ast_grep_replace:
  pattern: function $NAME($ARGS) { $$$ }
  replacement: function $NAME($ARGS: any) { $$$ }
  languages: [typescript]
```

## Pattern Syntax

### Function Matching

```
# Function with any name
function $NAME($$$) { $$$ }

# Async function
async function $NAME($$$) { $$$ }

# Arrow function
const $NAME = ($$$) => { $$$ }

# Function with specific return type
function $NAME($$$): Promise<$RET> { $$$ }
```

### Class Matching

```
# Class declaration
class $NAME { $$$ }

# Class with extends
class $NAME extends $PARENT { $$$ }

# Class method
class $CLASS { $METHOD($$$) { $$$ } }
```

### Variable Matching

```
# Const declaration
const $NAME = $VALUE

# Let declaration
let $NAME = $VALUE

# Destructuring
const { $PROP } = $OBJ
```

### Import/Export Matching

```
# Named import
import { $NAMES } from '$MODULE'

# Default import
import $NAME from '$MODULE'

# Export
export { $NAMES }
export default $NAME
```

### Expression Matching

```
# Binary expression
$LEFT + $RIGHT

# Call expression
$FUNC($$$)

# Await expression
await $EXPR

# Template literal
`$TEXT`
```

## Common Patterns

### Finding Unused Code

```
# Find functions without calls
ast_grep_search:
  pattern: function $NAME($$$) { $$$ }
  exclude: ['**/*.test.ts']
```

### Finding Anti-Patterns

```
# Find any type
ast_grep_search:
  pattern: $NAME: any
  languages: [typescript]

# Find console.log
ast_grep_search:
  pattern: console.log($$$)
  languages: [typescript, javascript]
```

### Refactoring Patterns

```
# Replace double quotes with single quotes
ast_grep_replace:
  pattern: "$TEXT"
  replacement: '$TEXT'

# Extract object property
ast_grep_replace:
  pattern: const $NAME = obj.$PROP
  replacement: const { $PROP: $NAME } = obj
```

## Tool Reference

| Aspect | ast_grep_search | ast_grep_replace |
|--------|-----------------|------------------|
| Modifies files | No | Yes |
| Returns matches | Yes | Yes |
| Dry-run mode | N/A | Yes |
| Pattern required | Yes | Yes |
| Meta-variables | Yes | Yes |

## Integration with Other Tools

AST tools complement other search tools:

| Tool | Best For |
|------|----------|
| `Grep` | Text-based search, fast scanning |
| `Glob` | File pattern matching |
| `ast_grep_search` | Structural code search |
| `lsp_find_references` | Symbol usage with LSP accuracy |

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Parse error | Invalid syntax in file | Fix file syntax first |
| Pattern error | Invalid AST pattern | Check pattern syntax |
| No matches | Pattern doesn't match | Verify pattern and language |

## Configuration

```json
{
  "astTools": {
    "maxResults": 100,
    "timeout": 30000,
    "defaultLanguages": ["typescript", "javascript"]
  }
}
```

## Further Reading

- [LSP Tools](lsp-tools.md) - LSP operations reference
- [Built-in Tools](built-in-tools.md) - Native Claude Code tools
- [Tool Overview](overview.md) - Tool ecosystem overview
- [ast-grep documentation](https://ast-grep.github.io/) - Official ast-grep docs
