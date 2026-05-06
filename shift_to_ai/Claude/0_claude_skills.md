# Claude Skills 
- "skills" are Markdown-based instruction files designed to automate repetitive tasks
- skills remain dormant until Claude identifies a matching request, which helps conserve context space and improves efficiency
- Users can categorize these files as personal settings for individual workflows or project-level assets that apply to an entire repository or team

## 🔹 Problem

* Repeating instructions to Claude:

  * Coding standards
  * PR review format
  * Commit message style
* Leads to inefficiency and wasted context

---

## 🔹 Solution: Skills

* **Skill = Markdown file (`.md`)**
* Teaches Claude how to perform a task **once**
* Automatically applied when relevant

---

## 🔹 What are Agent Skills?

* Agent Skills are Folder containing:

  * Instructions
  * Scripts
  * Resources

* Agents can discover these folders to:

  * Be more accurate
  * Be more efficient

---

## 🔹 How Skills Work

1. Claude reads user request
2. Matches it with skill descriptions
3. Activates relevant skills
4. Applies instructions automatically

---

## 🔹 Skill Structure

* `skill.md` file contains:

  * **Name**
  * **Description** → used for matching
  * **Instructions**

---

## 🔹 Skill Match Example

```
name: pr-review
description: reviews pull requests for code quality. Use when reviewing PRs or checking code changes
```
When you ask claude to review a PR, It matches your request against available skill descriptions and finds this one.
Claude reads your request 
"can you review the pull request on branch example-skill-demo"
compares it to all available skill descriptions and activates the one which matches.

## 🔹 Storage Locations

### 1. Personal Skills

* Path: `~/.claude/skills`
* Scope: Across all projects
* Use cases:

  * Commit message style
  * Documentation format
  * Code explanation preferences

---

### 2. Project Skills

* Path: `./.claude/skills` (inside root directory of repo)
* Scope: Shared with team
* Use cases:

  * Coding standards
  * PR review guidelines
  * Brand/design rules

---

## 🔹 Skills vs Other Customizations

### Skills

* Auto-triggered
* Task-specific
* Loaded only when needed
* Efficient (doesn't fill context)

---

### claude.md

* Always loaded in every conversation
* For global rules
* Example:

  * Always use TypeScript strict mode

---

### Slash Commands

* Manual trigger required
* Example:

  * `/review-pr`

---

## 🔹 When to Use Skills

Use for repeated, task-specific instructions:

* Code review standards
* Commit message formats
* Documentation styles
* Design/brand guidelines

---

## 🔹 Key Benefit

* Avoid repetition
* Save context space
* Improve consistency

---

## 🔹 Rule of Thumb

> If you explain something to Claude repeatedly → it should be a **Skill**
