# Clean Draft Setup and Source

## Learner Route

1. Open the [Clean Draft marketplace entry](https://ai-marketplace-sbqrdzy4sa-uw.a.run.app/?tool=curated%3Askill%3Aclean-draft).
2. Sign in to your company GitHub account and check access to the [source folder](https://github.com/thumbtack/shared-skills/tree/main/users/tsalman/clean-draft).
3. Download or ask the tutor to copy the complete folder into `practice-workspace/downloads/clean-draft/`.
4. Inspect the instructions and checker. Confirm how to enable and select the skill in your desktop setup.
5. Keep the example unchanged. Create your own skill in a different folder after trying it.

The tutor can retrieve the folder through an authorized GitHub connection or an authenticated local download. A full repository clone is optional. Learners do not need to run Git commands.

Downloading only SKILL.md leaves out the checker. The package includes `README.md`, `SKILL.md`, `VERSION`, and `scripts/prose_check.py`.

## Included Course Copy

The course author retrieved the full package from the supplied GitHub source on November 6, 2026. Version: **1.1.0**. The unchanged copy lives in `learner-assets/skills/clean-draft/` for inspection and guided practice. See `learner-assets/skills/clean-draft-source.json` for file hashes and source URLs.

This copy is an example asset. Its presence does not automatically install it in every environment. If GitHub access is missing, use a tutor-led inspection and record the download as unfinished.

The authoring browser could not open the marketplace page. Its link comes from the course owner. The author retrieved the package through the authorized GitHub connection.

## What the Skill Does

The skill improves structure first, then sentences. It preserves facts and flags missing owners, dates, recommendations, or decisions. It returns the cleaned draft, gaps for the author, and a short change note. A review-only request returns suggested fixes without rewriting.

The checker flags readability concerns before and after. It needs Python 3 and does not fact-check the draft.

## Guided File-Based Run

If the skill is not installed, ask the tutor to read its SKILL.md and follow the workflow explicitly. Inspect the checker before executing it. A typical local check from the course root is:

```bash
python3 learner-assets/skills/clean-draft/scripts/prose_check.py practice-workspace/outputs/week-01-original.md
```

Run it again on the cleaned copy. If Python is unavailable, label the automated check incomplete and do the manual review.

## Limits for Course Use

Use Clean Draft for form and readability. Keep the course's separate evidence list for fact review. Do not treat the skill's instruction to shorten a draft as permission to remove required course steps or source attribution.
