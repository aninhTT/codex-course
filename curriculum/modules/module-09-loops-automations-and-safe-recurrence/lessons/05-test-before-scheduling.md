---
module: 9
lesson: 5
title: "Test Before Scheduling"
difficulty: intermediate
prerequisites: "9.04"
---

# Lesson 9.05: Test Before Scheduling

## Learn

Test the automation prompt manually before scheduling it. A manual test helps confirm that Codex uses the right evidence, produces a reviewable output, respects boundaries, and knows when there is nothing to report.

The first few scheduled runs should also be reviewed closely. If the output is noisy, vague, too broad, or too eager to edit files, refine the prompt or cadence before trusting it.

Live scheduling is optional in this course. The learning goal is safe design.

## Practice

Try this in Codex:

```text
Run a manual test of this automation design card without scheduling it. Tell me what output it would produce, whether the prompt is too broad or risky, and what I should adjust before any real automation run.
```

**Success criteria:** The learner tests the automation idea manually and can name at least one thing they would review before scheduling.
