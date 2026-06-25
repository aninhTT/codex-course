# Troubleshooting

## Codex is being too broad

- Ask it to use only the files in the current lesson.
- Name the exact file or folder you want it to inspect.
- Ask it to explain before it edits.

## Codex is editing too much

- Ask for a proposal first instead of an edit.
- Tell Codex to make the smallest useful change.
- Review the diff or changed file before accepting it.

## A lesson prompt feels vague

- Ask Codex to restate the goal in plain language first.
- Ask what a good result should look like before starting.
- Reopen the module landing page and lesson file to anchor the task.

## I lost my place

- Open `learner-assets/artifact-tracker.md`.
- Open the current module `MODULE.md`.
- Ask Codex: "Based on the artifact tracker, what should I do next?"
- Ask Codex: "Give me a quick recap of where I am and the next sensible step."

## I switched projects and need to come back

- Return to the course project.
- Paste the summary you created before switching.
- Ask Codex: "I'm back in the course project. Based on this summary, help me resume the course."

## I am not sure which project to use

- Use the course project when you are taking lessons.
- Use `practice-workspace/` for guided exercises.
- Use `playground/` for experiments.
- Use a separate Codex project when the skill, prototype, or real-work task needs its own folder.
- Ask Codex: "Should this task happen in the current course folder, `playground/`, a separate project, or no project?"

## I am not sure how to ask Codex

- Use the beginner loop in `reference/codex-best-practices.md`: Ask, Inspect, Plan, Act, Review.
- Start with one small goal and name the file or folder Codex should use.
- If the task feels bigger than one step, ask Codex to plan first.

## The GitHub skill lesson feels advanced

- Focus on understanding the structure of the skill, not every detail.
- Use the `use-case` skill as inspiration, not as something to master fully.
- Ask Codex to summarize what matters for a beginner.

## Record & Replay is not available

- Use Lesson 7.04 and create a recording-level written walkthrough instead.
- Describe the start point, end point, changing inputs, sensitive information to avoid, and success check.
- Ask Codex to turn the walkthrough into a skill plan or draft skill.

## Sites or deployment feels risky

- Ask for a Sites-readiness review first.
- Ask Codex to distinguish local preview, saved version, and deployment before taking action.
- Do not deploy or widen access until the audience, content, secrets, and data handling are reviewed.

## Automations feel too powerful

- Stay in design mode and create an automation design card first.
- Test the automation prompt manually before scheduling anything.
- Include a stop condition, risk check, and first-run review plan.
