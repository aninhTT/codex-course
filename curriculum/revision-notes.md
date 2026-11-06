# November 2026 Course Revision

This revision is for everyday employees using Work and Codex. Modules 1–8 form an activity-based foundation. Module 9 adds deeper Codex building. Module 10 supports longer work in Work or Codex.

## Topic Locations Changed

| Earlier topic | Current location |
| --- | --- |
| Welcome and Codex versus chat | Welcome and Module 1: Chat, Work, and Codex. |
| Projects as folders and first file work | Module 2: projects, sources, instructions, first update, and handoff. |
| Use-case skill as the first example | Optional reference; Module 3 now starts with Clean Draft. |
| First practical and custom skill | Module 3: plan, build, and test one weekly-update skill on two inputs. |
| Recorded workflows in Module 7 | Foundation Module 4. |
| Scheduled work in Module 9 | Foundation Module 5. |
| Space and Pages | New foundation Module 6. |
| Work documents, slides, and spreadsheets | New foundation Module 7. |
| Sites in Module 8 | Foundation Module 8, with a direct prompt-built route. |
| Local prototype in Module 4 | Optional Module 9. |
| Goals in Module 5 | Optional Module 10. |
| Starter kit and power-user system map | Foundation checkpoint in 8.05 and optional maintenance in 10.05. |

Use `curriculum/course-index.json` for current lesson numbers. Resolve older lesson references by topic. Do not assume the same number means the same lesson.

## Language and Practice Changes

Lessons now use Learn, See It, guided Practice, and optional Challenge. The tutor demonstrates a concrete example, gives one step at a time, checks results, and saves progress. Learners can carry a real recurring workflow across modules or use the sample weekly update.

The original use-case source package and local starter app remain available. The course includes Clean Draft, its checker, and a source record. Supporting guides, the tracker, tutor instructions, and pilot plan follow the new path.

## Validation Boundaries

Author checks cover lesson structure, links, module counts, source package integrity, readability, and sample calculations. Live learner installation, account access, recording, schedules, Space, and deployment still need a pilot in the intended workspace.

## Shared-Surface Teaching Revision

The tutor now runs in Work or Codex. Work is the recommended starting point for most non-engineering employees; Codex remains supported for the full foundation and recommended for technical work. START-HERE.md provides both startup routes.

Lesson 1.04 now guides connection setup and verifies retrieval. Thumbtack has enabled Computer Use for the intended learner environment. The course uses the current AI Expectations link.

| Lesson number | Updated activity |
| --- | --- |
| 3.03 | Study and run Clean Draft, with a customization challenge. |
| 3.04 | Meet Skill Creator and review a real skill plan. |
| 3.05 | Build a focused custom workflow skill. |
| 4.04 | Connect the captured step to draft preparation. |
| 9.05 | Inspect GitHub and choose a prototype handoff. |

Keep older completion evidence when migrating progress. A previous 3.04 Clean Draft run does not automatically complete the new Skill Creator activity.

## Teaching Reference

The course owner requested closer alignment with the [Claude course](https://github.com/aninhTT/claude-course). These lessons informed the activity design:

- [Connecting Your Tools](https://github.com/aninhTT/claude-course/blob/main/modules/01-fundamentals/lessons/02-connecting-your-tools.md): practical setup and test queries.
- [Copy Your First Skill](https://github.com/aninhTT/claude-course/blob/main/modules/03-skills-primer/lessons/03-copy-your-first-skill.md): retrieve, inspect, run, compare, and customize Clean Draft.
- [Meet Skill Creator](https://github.com/aninhTT/claude-course/blob/main/modules/03-skills-primer/lessons/04-meet-the-skill-creator-skill.md): use the creator before building from scratch.
- [Artifacts 101](https://github.com/aninhTT/claude-course/blob/main/modules/04-artifacts/lessons/01-artifacts-101.md): choose an audience, create an output, find it, edit it, and decide whether to share.
- [Independent activity](https://github.com/aninhTT/claude-course/blob/main/modules/02-cowork/lessons/03-your-solo-cowork-activity.md): let the learner direct a real task.
- [Scheduling skills](https://github.com/aninhTT/claude-course/blob/main/modules/06-intermediate-skills/lessons/02-scheduling-and-automating.md): schedule a useful existing method and inspect the saved task.

Product controls, invocation methods, sharing, and scheduling guidance follow OpenAI documentation and the course owner's environment. Claude-specific videos, commands, and capability claims are not copied into learner instructions.

## Author Checks and Live Pilot

Run `python3 scripts/verify_course.py` for index consistency, teaching structure, links, video placement, progress-template consistency, Clean Draft source integrity, and sample calculations. Run the included readability checker on authored Markdown.

Run `python3 scripts/package_course.py` to build the uploadable ZIP. Verify the extracted copy as well as the source folder. The package excludes saved learner progress and generated output files.

A live pilot in both Work and Codex is still needed for account sign-in, recording controls, actual schedules, shared Pages, and deployment. Static author checks do not establish that those account-specific actions work.

## Connected Example and Discovery Activity

The weekly team update is the recommended example. It connects the first draft, Clean Draft, custom skill, recording, schedule, Page, work files, and team Site. Learners can choose another workflow and adapt the same activities. See reference/team-update-example.md for exact handoffs.

New Lesson 1.05 follows Connect Your Tools. It reviews the learner’s last seven days of calendar, Granola, and Linear activity to suggest three to five source-backed AI tasks. Google Calendar is now part of the setup examples. This adds one lesson without renumbering other modules. Preserve existing learner progress; add 1.05 as not started when migrating.
