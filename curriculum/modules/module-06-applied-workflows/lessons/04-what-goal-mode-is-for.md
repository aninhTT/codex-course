---
module: 6
lesson: 4
title: "What Goal Mode Is For"
difficulty: beginner
prerequisites: "6.03"
---

# Lesson 6.04: What Goal Mode Is For

## Learn

Most Codex prompts are about the next useful step: explain this, plan this, change this file, summarize this folder. Goal mode is different. A Goal gives Codex a persistent objective to work toward across a longer task.

A normal prompt says: do this next thing.

A Goal says: keep working until this outcome is true, and check the evidence before calling it done.

That is why Goal mode is powerful for work where the path is uncertain but the finish line can still be checked. Codex can inspect, try an approach, review what happened, and continue from there without you retyping "keep going" after every step.

A strong Goal should include:

- **Outcome:** what should be true when the work is done
- **Evidence source:** what Codex should inspect to prove the outcome
- **Constraints:** what must stay true along the way
- **Boundaries:** which files, folders, tools, or sources Codex should use
- **Blocked stop condition:** when Codex should stop and explain what is missing

Goal mode is not background autonomy without boundaries. It is also not global memory, a project rule, or a replacement for reviewing Codex's work. A Goal belongs to the current thread, and it should stay specific enough that Codex can tell whether it succeeded.

Here are two non-technical examples:

```text
/goal Produce an evidence-backed audit of our onboarding workflow using the files in this workspace. End with a report that separates confirmed issues, unclear areas, missing evidence, and recommended next steps.
```

```text
/goal Build a verified market landscape for employee listening tools using public sources and the notes in this folder. End with a vendor table, source links, confidence levels, and open questions.
```

Goal mode is a poor fit when the task is small, vague, or impossible to verify. Do not use a Goal for one quick answer, a simple edit, a vague request like "make this better," a task with no evidence source, a task where Codex lacks access to the needed files or tools, or sensitive work where permissions and privacy boundaries are unclear.

The simplest test is this: if Codex cannot explain what "done," "blocked," and "uncertain" mean for the task, the Goal needs more shaping first.

## Practice

Try this in Codex:

```text
Teach me Goal mode using one non-technical example from my work. Explain when a normal prompt would be enough, when a Goal would be better, what evidence Codex would need, and what should make Codex stop instead of guessing.
```

**Success criteria:** The learner can explain the difference between a normal prompt and a Goal, and can name at least one task that is too vague or too small for Goal mode.
