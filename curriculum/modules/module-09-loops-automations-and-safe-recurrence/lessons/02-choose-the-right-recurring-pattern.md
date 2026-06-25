---
module: 9
lesson: 2
title: "Choose The Right Recurring Pattern"
difficulty: intermediate
prerequisites: "9.01"
---

# Lesson 9.02: Choose The Right Recurring Pattern

## Learn

Different recurring patterns fit different jobs.

Use a normal prompt when the task is quick. Use a Goal when the task is longer but belongs in the current thread and has a checkable finish line. Use a thread automation when the same conversation should wake up and continue checking something. Use a standalone automation when each run should be independent or report separate findings.

For project work, also consider where it should run. A worktree can keep automation changes separate from unfinished local work. Running in the local project may be useful, but it can touch files you are actively editing.

## Practice

Try this in Codex:

```text
Help me choose the right recurring pattern for one workflow. Ask what should trigger it, how often it should run, whether it needs the same thread context, whether each run should be independent, and whether changes should happen in my local project or a separate worktree. Then recommend the safest pattern.
```

**Success criteria:** The learner chooses a recurring pattern based on context, independence, cadence, and review risk.
