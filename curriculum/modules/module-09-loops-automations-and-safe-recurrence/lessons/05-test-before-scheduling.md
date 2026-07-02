---
module: 9
lesson: 5
title: "Schedule A Safe Loop"
difficulty: intermediate
prerequisites: "9.04"
---

# Lesson 9.05: Schedule A Safe Loop

## Learn

Test the automation prompt manually before scheduling it. A manual test helps confirm that Codex uses the right evidence, produces a reviewable output, respects boundaries, and knows when there is nothing to report.

The first few scheduled runs should also be reviewed closely in the destination app or artifact. If the output is noisy, vague, too broad, or too eager to edit files, refine the prompt or cadence before trusting it.

In this course, you should schedule one safe loop so the concept becomes real. Keep it read-only or report-only. It should not send, post, archive, delete, publish, or modify a source of truth without your explicit approval.

## Practice

Try this in Codex:

```text
Run a manual test of this automation design card. If the test is safe and useful, help me schedule one recurring loop. Keep it read-only or report-only, include a clear cadence, and require my explicit approval before any send/post/archive/delete/publish/modify action. After scheduling, tell me what was scheduled, when it will run, where I should review output, and how I can pause, edit, or delete the loop.
```

**Success criteria:** The learner schedules one safe recurring loop and knows how to review, pause, edit, or delete it.
