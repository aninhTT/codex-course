---
module: 9
lesson: 3
title: "Write A Durable Automation Prompt"
difficulty: intermediate
prerequisites: "9.02"
---

# Lesson 9.03: Write A Durable Automation Prompt

## Learn

An automation prompt has to survive without you sitting there to clarify every step. A durable prompt should say what Codex should check each time, what evidence it should use, what counts as important, what to report, and when to stop or ask for help.

Weak automation prompt:

```text
Check this every day.
```

Stronger automation prompt:

```text
Every weekday morning, review the files in this project for new unresolved action items. Report only items with an owner or due date. If nothing changed since the last run, say there is nothing to report. Do not edit files unless I explicitly ask in the thread.
```

Durable does not mean long. It means clear enough to run repeatedly.

## Practice

Try this in Codex:

```text
Help me draft a durable automation prompt for my chosen workflow. Include what to check, what evidence to use, what to report, what not to do, and when Codex should stop or ask me for input.
```

**Success criteria:** The learner has a prompt that can be tested manually before any scheduling happens.
