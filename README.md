# Oh My Claude Sisyphus Documentation

Multi-agent orchestration system for Claude Code.

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000 in your browser.

## Deploy to GitHub Pages

1. Push this repository to GitHub
2. Go to Settings > Pages
3. Set Source to "GitHub Actions"
4. The site will be deployed automatically

## Structure

```
docs/
├── index.md                 # Home page
├── getting-started/         # Installation & configuration
├── architecture/            # Core system architecture
├── agents/                  # Multi-agent system
├── hooks/                   # Lifecycle hooks
├── tools/                   # LSP, AST, built-in tools
├── skills/                  # Builtin skills
├── commands/                # Slash commands
├── features/                # Key features
├── configuration/           # Configuration reference
├── platform/                # Platform-specific behavior
├── development/             # Build & CI/CD
└── reference/               # API reference & glossary
```

## Disclaimer

This documentation is an independent community resource. It is not affiliated with, endorsed by, or associated with the oh-my-claude-sisyphus, oh-my-opencode, or OpenCode projects.
