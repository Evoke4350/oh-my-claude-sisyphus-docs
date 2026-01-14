---
layout: default
title: Frontend UI/UX Skill
parent: Skills System
nav_order: 5
---

# Frontend UI/UX Skill

Designer-turned-developer who crafts stunning UI/UX even without design mockups.

---

## Overview

| Property | Value |
|----------|-------|
| **Name** | frontend-ui-ux |
| **Type** | Enhancement skill (stackable) |
| **Purpose** | UI/UX design, visual aesthetics, component implementation |

The Frontend UI/UX skill brings a designer's eye to development. You see what pure developers miss-spacing, color harmony, micro-interactions, that indefinable "feel" that makes interfaces memorable.

```mermaid
flowchart TD
    Request["UI/UX Task"]
    Purpose["1. Purpose<br/>What problem? Who uses it?"]
    Tone["2. Tone<br/>Pick an extreme"]
    Constraints["3. Constraints<br/>Framework, performance"]
    Differentiation["4. Differentiation<br/>ONE memorable thing"]
    Implementation["5. Implement<br/>With precision"]
    Verify["6. Verify<br/>Functional & beautiful"]

    Request --> Purpose
    Purpose --> Tone
    Tone --> Constraints
    Constraints --> Differentiation
    Differentiation --> Implementation
    Implementation --> Verify
```

---

## Design Process

### Before Coding: Choose BOLD Direction

Commit to a **BOLD aesthetic direction** before writing any code.

#### 1. Purpose

- What problem does this solve?
- Who are the users?
- What context will it be used in?

#### 2. Tone (Pick an Extreme)

| Tone Option | Description |
|-------------|-------------|
| **Brutally minimal** | Extreme restraint, only essentials |
| **Maximalist chaos** | Rich, layered, abundant |
| **Retro-futuristic** | Nostalgic tomorrow, vintage tech |
| **Organic/natural** | Soft shapes, earth tones, flowing |
| **Luxury/refined** | Elegant, expensive, sophisticated |
| **Playful/toy-like** | Fun, colorful, approachable |
| **Editorial/magazine** | Typography-led, dramatic layouts |
| **Brutalist/raw** | Exposed structure, unpolished |
| **Art deco/geometric** | Patterned, ornamental, structured |
| **Soft/pastel** | Gentle, calming, dreamy |
| **Industrial/utilitarian** | Functional, stark, purposeful |

#### 3. Constraints

- Framework requirements (React, Vue, Angular)
- Performance budgets
- Accessibility standards
- Browser support

#### 4. Differentiation

- What's the ONE thing someone will remember?

> **Key**: Choose a clear direction and execute with precision. Intentionality > intensity.

---

## Aesthetic Guidelines

### Typography

Choose distinctive fonts.

**AVOID**: Arial, Inter, Roboto, system fonts, Space Grotesk.

Pair a characterful display font with a refined body font.

| Role | Examples |
|------|----------|
| **Display** | DM Serif Display, Playfair Display, Oswald, Righteous |
| **Body** | Source Sans Pro, Merriweather, JetBrains Mono, DM Sans |

### Color

Commit to a cohesive palette using CSS variables.

| Approach | Result |
|----------|--------|
| **Dominant + Sharp Accents** | High impact, memorable ✅ |
| **Evenly Distributed** | Timid, forgettable ❌ |

**AVOID**: Purple gradients on white (AI slop).

### Motion

Focus on high-impact moments:

| Priority | Technique |
|----------|-----------|
| **High** | One well-orchestrated page load with staggered reveals |
| **Medium** | Scroll-triggered animations |
| **Low** | Scattered micro-interactions |

Use CSS-only where possible. Use Motion library (React) when available.

### Spatial Composition

Break the grid:

- Unexpected layouts
- Asymmetry
- Overlapping elements
- Diagonal flow
- Grid-breaking elements
- Generous negative space OR controlled density

### Visual Details

Create atmosphere and depth:

- Gradient meshes
- Noise textures
- Geometric patterns
- Layered transparencies
- Dramatic shadows
- Decorative borders
- Custom cursors
- Grain overlays

**Never default to solid colors.**

---

## Anti-Patterns (NEVER)

| Anti-Pattern | Why |
|--------------|-----|
| Generic fonts (Inter, Roboto, Arial) | Boring, forgettable |
| Cliched color schemes (purple on white) | AI-generated appearance |
| Predictable layouts | No personality |
| Cookie-cutter design | Lacks character |
| Converging on common choices | Each design should be unique |

---

## Execution

Match implementation complexity to aesthetic vision:

| Vision | Implementation |
|--------|----------------|
| **Maximalist** | Elaborate code with extensive animations and effects |
| **Minimalist** | Restraint, precision, careful spacing and typography |

> **Interpret creatively and make unexpected choices that feel genuinely designed for the context.**

---

## Work Principles

| Principle | Action |
|-----------|--------|
| **Complete what's asked** | Execute the exact task. No scope creep. |
| **Leave it better** | Ensure project is in working state. |
| **Study before acting** | Examine existing patterns, git log first. |
| **Blend seamlessly** | Match existing code patterns. |
| **Be transparent** | Announce each step, explain reasoning. |

---

## Tech Stack

| Technology | Use For |
|------------|---------|
| **React** | Component-based UI |
| **Vue** | Progressive framework |
| **Angular** | Enterprise applications |
| **HTML/CSS/JS** | Lightweight implementations |
| **Tailwind CSS** | Utility-first styling |
| **CSS-in-JS** | Component-scoped styles |
| **Framer Motion** | React animations |

---

## Activation

### As a Skill

Stacks with other skills:

```
sisyphus + frontend-ui-ux
```

### Via Agent

Delegate to the Frontend Engineer agent:

```
Use frontend-engineer to create the login form
```

---

## See Also

- [Frontend Engineer Agent](../agents/task-execution/frontend-engineer.md) - Agent variant
- [Sisyphus Skill](sisyphus.md) - Multi-agent orchestration
- [Skills Overview](overview.md) - All available skills
