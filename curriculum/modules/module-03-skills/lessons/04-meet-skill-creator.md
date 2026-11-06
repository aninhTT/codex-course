---
module: 3
lesson: 4
title: "Meet Skill Creator"
track: foundation
surfaces: [chatgpt-work, codex]
---

# Lesson 3.04: Meet Skill Creator

You can describe a workflow in ordinary language and let a skill help build its instructions.

## Learn

**Skill Creator** helps turn a workflow into a structured skill. It asks about the purpose, inputs, steps, output, and failure cases. You review what it proposes.

Start from the task you already completed. You know where the first draft missed the mark and which rules helped. That is better material than an abstract request to automate everything.

Look for a description that names the use case, steps another assistant could follow, and a checkable result. The creator handles the file format; you supply the work judgment.

## See It

Ask: “Help me make a skill for my team update. Show me a short plan before creating it.”

An illustrative outline might look like this:

```markdown
---
name: weekly-update-helper
description: Draft a team update from the requested reporting period’s notes.
---

1. Read the supplied notes and identify the reporting period.
2. Draft the decision needed, progress, blockers, and next steps.
3. Flag missing owners and dates. Save a draft for review.
```

This is a teaching example. Your creator plan should reflect your own sources and review rules.

## Practice

Your tutor guides one step at a time in Work or Codex. Continue the recommended team-update example, or adapt the steps to your saved workflow choice.

1. Find Skill Creator with the tutor. In Work, select @skill-creator when available. In Codex, select $skill-creator when available.

2. Give it your saved workflow brief. Ask for a small skill plan rather than a finished system.

3. Answer its questions and look at the proposed skill structure. Identify the purpose, method, and result.

4. Choose two improvements before saving the plan for the next lesson.

**Success criteria:** You used Skill Creator or a clearly labeled guided equivalent and reviewed a concrete skill plan.

## Challenge — Optional

Ask the creator to critique one instruction from your plan. Rewrite it so another assistant could follow it without asking what you meant.

**Success criteria:** Your revised instruction names an observable action or result.

## Quick Check

What did the assistant assume? Which fact or behavior did you verify yourself?

## Carry Forward

Bring the Skill Creator plan and the two improvements you identified.
