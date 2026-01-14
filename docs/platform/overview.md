---
layout: default
title: Platform Overview
parent: Platform
nav_order: 1
---

# Platform Overview

Oh-my-claude-sisyphus supports Windows, macOS, and Linux with platform-specific differences in installation, hooks, and configuration.

## Quick Reference

| Platform | Installation | Hook Type | Shell | State Location |
|----------|--------------|-----------|-------|----------------|
| **Windows** | npm | Node.js (.mjs) | PowerShell/CMD | `%APPDATA%\claude\.sisyphus\` |
| **macOS** | curl or npm | Bash (.sh) | zsh/bash | `~/.claude/.sisyphus/` |
| **Linux** | curl or npm | Bash (.sh) | bash/zsh | `~/.claude/.sisyphus/` |

## Installation

### Windows

**Recommended:** npm installation

```powershell
npm install -g oh-my-claude-sisyphus
```

**Requirements:**
- Node.js 20+
- PowerShell 5.1+ or Windows Terminal

**Post-Install:**
```powershell
# Verify installation
claude --version

# Check hooks
ls $env:USERPROFILE\.claude\sisyphus\hooks\
```

---

### macOS

**Option 1:** curl (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/install.sh | bash
```

**Option 2:** npm

```bash
npm install -g oh-my-claude-sisyphus
```

**Requirements:**
- Bash or zsh
- Xcode Command Line Tools (for LSP)

**Post-Install:**
```bash
# Verify installation
claude --version

# Check hooks
ls ~/.claude/sisyphus/hooks/
```

---

### Linux

**Option 1:** curl (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claude-sisyphus/main/scripts/install.sh | bash
```

**Option 2:** npm

```bash
npm install -g oh-my-claude-sisyphus
```

**Requirements:**
- Bash or zsh
- Build tools for LSP servers

**Post-Install:**
```bash
# Verify installation
claude --version

# Check hooks
ls ~/.claude/sisyphus/hooks/
```

## Hook Implementation

### Windows Hooks

**Type:** Node.js (.mjs)

**Location:** `%USERPROFILE%\.claude\sisyphus\hooks\`

**Execution:** Via Node.js runtime

**Example:**
```javascript
// keyword-detector.mjs
#!/usr/bin/env node
const fs = require('fs');
const prompt = process.argv[2];

// Keyword detection logic
if (prompt.includes('ultrawork')) {
  console.log('ULTRAWORK_MODE:true');
}
```

---

### Unix Hooks (macOS/Linux)

**Type:** Bash (.sh)

**Location:** `~/.claude/sisyphus/hooks/`

**Execution:** Via bash shell

**Example:**
```bash
#!/bin/bash
# keyword-detector.sh
PROMPT="$1"

# Keyword detection logic
if [[ "$PROMPT" =~ ultrawork ]]; then
  echo "ULTRAWORK_MODE:true"
fi
```

---

### Cross-Platform Hooks

For maximum compatibility, hooks use POSIX-compliant bash syntax:

```bash
#!/usr/bin/env bash
# This works on macOS, Linux, and Windows (WSL/Git Bash)

# Use [[ ]] instead of [ ]
if [[ "$VAR" == "value" ]]; then
  # ...
fi

# Use printf instead of echo
printf "%s\n" "$OUTPUT"
```

## Configuration Locations

### User Configuration

| Platform | Configuration File |
|----------|-------------------|
| **Windows** | `%USERPROFILE%\.claude\settings.json` |
| **macOS** | `~/.claude/settings.json` |
| **Linux** | `~/.claude/settings.json` |

### State Files

| Platform | State Directory |
|----------|-----------------|
| **Windows** | `%APPDATA%\claude\.sisyphus\` |
| **macOS** | `~/.claude/.sisyphus/` |
| **Linux** | `~/.claude/.sisyphus/` |

### Agent Definitions

| Platform | Agents Directory |
|----------|------------------|
| **Windows** | `%USERPROFILE%\.claude\agents\` |
| **macOS** | `~/.claude/agents/` |
| **Linux** | `~/.claude/agents/` |

## Path Handling

### Windows Paths

**Use:** Backslashes or forward slashes

```powershell
# Both work
C:\Users\Username\.claude\agents\oracle.md
C:/Users/Username/.claude/agents/oracle.md
```

**In Config Files:** Use forward slashes for compatibility

```json
{
  "hooks": {
    "PostToolUse": [
      "C:/Users/Username/.claude/sisyphus/hooks/rules-injector.mjs"
    ]
  }
}
```

---

### Unix Paths (macOS/Linux)

**Use:** Forward slashes with tilde expansion

```bash
~/.claude/agents/oracle.md
```

**In Config Files:** Use `$HOME` or absolute paths

```json
{
  "hooks": {
    "PostToolUse": [
      "/home/username/.claude/sisyphus/hooks/rules-injector.sh"
    ]
  }
}
```

## LSP Server Support

### Prerequisites

| Platform | Installation |
|----------|--------------|
| **Windows** | Install via npm or specific installers |
| **macOS** | `brew install <package>` |
| **Linux** | System package manager or npm |

### Common LSP Servers

| Language | Windows | macOS | Linux |
|----------|---------|-------|-------|
| **TypeScript** | `npm install -g typescript-language-server` | `npm install -g typescript-language-server` | `npm install -g typescript-language-server` |
| **Python** | `pip install python-lsp-server` | `brew install python-lsp-server` | `pip install python-lsp-server` |
| **Go** | `go install golang.org/x/tools/gopls` | `go install golang.org/x/tools/gopls` | `go install golang.org/x/tools/gopls` |
| **Rust** | `rustup component add rust-analyzer` | `rustup component add rust-analyzer` | `rustup component add rust-analyzer` |

## Notifications

### Windows

**System:** Windows Notification Center

**Requirements:**
- Windows 10/11

**Configuration:**
```json
{
  "background_notifications": true
}
```

---

### macOS

**System:** Notification Center

**Requirements:**
- macOS 10.10+

**Terminal Notification Permission:**
```
System Settings → Notifications → Terminal
```

---

### Linux

**System:** libnotify

**Requirements:**
- `libnotify-bin` package

**Install:**
```bash
# Debian/Ubuntu
sudo apt install libnotify-bin

# Fedora
sudo dnf install libnotify

# Arch Linux
sudo pacman -S libnotify
```

## Auto-Update

### Windows

**Method:** Node.js child process

**Lock File:** `%APPDATA%\claude\.sisyphus\update.lock`

---

### Unix (macOS/Linux)

**Method:** Bash background job

**Lock File:** `~/.claude/.sisyphus/update.lock`

---

### Cross-Platform

Both platforms use the same update logic:

1. Check lock file
2. Verify time since last check
3. Query npm registry
4. Install update if available
5. Update lock file timestamp

## Troubleshooting

### Windows

**Hooks not executing:**
```powershell
# Check Node.js is available
node --version

# Verify hook permissions
Get-Acl $env:USERPROFILE\.claude\sisyphus\hooks\*.mjs

# Test hook manually
node $env:USERPROFILE\.claude\sisyphus\hooks\keyword-detector.mjs "test prompt"
```

**Path issues:**
```powershell
# Use forward slashes in config
# Or escape backslashes
"C:\\Users\\Username\\.claude\\hooks"
```

---

### macOS

**Hooks not executing:**
```bash
# Check bash is available
which bash

# Verify hook permissions
ls -l ~/.claude/sisyphus/hooks/

# Make executable
chmod +x ~/.claude/sisyphus/hooks/*.sh
```

**zsh-specific:**
```bash
# Add to ~/.zshrc for alias support
export PATH="$HOME/.claude/sisyphus/bin:$PATH"
```

---

### Linux

**Hooks not executing:**
```bash
# Check bash is available
which bash

# Verify hook permissions
ls -l ~/.claude/sisyphus/hooks/

# Make executable
chmod +x ~/.claude/sisyphus/hooks/*.sh
```

**Distribution-specific:**
```bash
# Debian/Ubuntu - install build tools
sudo apt install build-essential

# Fedora - install build tools
sudo dnf groupinstall "Development Tools"

# Arch Linux - install base tools
sudo pacman -S base-devel
```

## Performance Considerations

| Platform | Background Tasks | LSP Startup | File Watching |
|----------|------------------|-------------|---------------|
| **Windows** | Slower spawn | Moderate | WSL recommended |
| **macOS** | Fast spawn | Fast | Native supported |
| **Linux** | Fastest spawn | Fastest | Native supported |

## Platform-Specific Tips

### Windows

- Use Windows Terminal for best experience
- Consider WSL2 for development
- Install Git for Windows for bash utilities
- Enable Developer Mode for additional features

### macOS

- Install Xcode Command Line Tools
- Use Homebrew for LSP servers
- Consider iTerm2 for advanced terminal features
- Enable key repeating in System Settings

### Linux

- Use distribution packages when available
- Configure systemd for background services
- Use tmux or screen for persistent sessions
- Install shell integrations (zsh-autosuggestions, etc.)

## Related Documentation

- [Installation](getting-started/installation.md) - Detailed install guide
- [Configuration Reference](configuration/reference.md) - Configuration options
- [Hooks](../hooks/) - Hook system documentation
