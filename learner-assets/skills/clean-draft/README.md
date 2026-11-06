# clean-draft

This skill turns a draft into something a busy reader can read once and act on. It works on text from Claude, Codex, ChatGPT, or any other LLM, and on human drafts too.

The skill makes two passes:

- **Structure.** It puts the recommendation first, narrows the options, names an owner for each ask, and cuts what the reader doesn't need.
- **Sentences.** It writes one idea per sentence in plain words, names who acts, and removes stock AI phrases such as "Here's the thing," "move the needle," and "Hope this helps."

It edits form, not facts. If the draft is missing an owner, a date, or a recommendation, the skill flags the gap and does not invent one.

## Use it

Paste a draft and ask your agent to clean it up:

- "Clean up this draft for the eng leads: …"
- "De-AI this Slack post."
- "Review this PRD for readability. Don't rewrite it; list the fixes."

You get back the cleaned draft, a short list of gaps for the author, and one line on what changed.

## The checker

`scripts/prose_check.py` is a readability lint. It uses only the Python 3 standard library, so you don't need to install anything. You can run it on its own:

```bash
python3 scripts/prose_check.py my-draft.md
pbpaste | python3 scripts/prose_check.py -
```

It reports `FAIL` for banned phrases and sentences over 40 words. It reports `WARN` for long sentences, passive voice, vague status words, and wordy phrasing. Warnings are prompts to look, not orders to rewrite.

### Interface other skills rely on

memory-kit's `/outbox` calls the checker (see `users/tsalman/memory-kit/skills/outbox/SKILL.md`, "Writing check"). It relies on these:

- The path `scripts/prose_check.py`, inside an installed `clean-draft` folder.
- `-` to read stdin, and `--only fail`.
- Exit codes: 0 means no `FAIL`, 1 means at least one `FAIL`, and 2 means a bad file or flag.

If you change any of these, bump `VERSION` and update memory-kit's outbox "Writing check" in the same pull request.

## Where the rules come from

The sentence rules adapt about 80% of Simplified Technical English (ASD-STE100), the plain-language standard for aircraft maintenance manuals. The structure rules come from the idea of computational kindness in *Algorithms to Live By*: the writer does the narrowing work so each reader doesn't have to.
