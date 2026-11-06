---
module: 9
lesson: 3
title: "Plan a build before changing files"
track: extension
surfaces: [chatgpt-work, codex]
---

# Lesson 9.03: Plan a build before changing files

Use a short plan to catch the wrong assumptions before Codex builds them.

## Learn

A **build plan** names the goal, features, expected files, assumptions, and review checks. Use Plan mode when available, or request the plan in ordinary language.

The plan should be small enough to understand. If it adds a database, sign-in, or live connections you did not need, remove them from the first version.

Ask about tradeoffs that affect the user, such as whether data survives closing the page. You can leave persistence out of a prototype, but it should be a conscious choice.

## See It

“Plan a local dashboard with a priority list and owner filter. Use sample data. Show the files, preview steps, and checks before building.”

## Practice

Your tutor guides one step at a time in Work or Codex. Continue the recommended team-update example, or adapt the steps to your saved workflow choice.

1. Write your own build request with the user, job, screen, features, sample data, and things to leave out.

2. Use Plan mode in Codex or ask for a plan. Review its assumptions and expected file changes.

3. Remove one unnecessary feature and clarify one behavior a user might misunderstand.

4. Save the plan and decide how you will test each promised feature.

**Success criteria:** You reviewed a bounded build plan and defined observable feature checks.

## Challenge — Optional

Ask Codex to identify the riskiest assumption in the plan. Design a small test for it before the full build.

**Success criteria:** The test would tell you whether the assumption holds.

## Quick Check

What did the assistant assume? Which fact or behavior did you verify yourself?

## Carry Forward

Bring the reviewed build plan and feature checks to implementation.
