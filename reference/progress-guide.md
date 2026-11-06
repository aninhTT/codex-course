# Save and Resume Course Progress

The tutor saves your place after teaching a section or checking an activity. The output tracker holds the locations of your work.

## For Tutors

Read `learner-assets/progress.json` at the start. If it does not exist, check the output tracker and ask about prior work before creating fresh progress.

For a new learner, copy `learner-assets/progress-template.json` to `learner-assets/progress.json`. Save the learner's name, role, surface, chosen workflow, and current position. Never initialize learner progress during course authoring.

After a section:

1. Read the latest progress file so unrelated updates remain intact.
2. Update only the completed section and current position. Keep each challenge separate.
3. Record output paths or links, evidence checked, and any unresolved issue.
4. Save safely. When possible, write a temporary file in the same folder and replace the old file only after the new JSON parses.

Allowed section statuses are `not_started`, `in_progress`, `passed`, `blocked`, `fallback`, and `skipped`. Mark Practice passed only after checking its success criteria. A blocked download and a successful guided run can coexist in the notes.

## Returning Learners

Welcome them by name, show their last result and next activity, and offer to continue. Challenges and skipped lessons do not lock the next module.

If an older progress file uses a different title for the same number, use `curriculum/revision-notes.md` to map the topic. Preserve prior evidence and ask the learner to review the affected status. Do not mark new material passed automatically.

Compare saved lesson keys with the current index. Add missing lessons, including 1.05, as not started without resetting existing entries. Preserve the learner's chosen workflow. Add the recommended-example and opportunity-note fields only when missing.

## Uploaded Courses and Moving Tasks

Write progress beside the extracted course materials if the task can edit them. At a stopping point, provide the latest progress file for download. The original ZIP and another computer do not update automatically.

If writable files are unavailable, keep an explicit recap in the conversation and provide progress JSON as a downloadable file when possible. Explain that persistence is not verified. Do not claim a save happened without a real file result.

Bring the course, saved progress, relevant outputs, and source links when starting elsewhere. Keep conversation history and file access separate.
