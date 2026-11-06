---
name: clean-draft
description: Clean up a draft so a busy reader can read it once and act on it. Use for AI-written text from Claude, Codex, ChatGPT, or any LLM, and for human drafts too. It restructures the draft to be decision-ready (recommendation first, fewer options, a clear ask) and rewrites sentences to be plain (short, one idea each, named actor, literal words, no AI filler or stock phrases). Includes a stdlib-only Python lint. Use when the user says "clean this up", "make this readable", "de-AI this", "tighten this draft", "this sounds like ChatGPT", "edit for clarity", "/clean-draft", or pastes a memo, PRD, RFC, status update, Slack post, email, or doc and asks to improve the writing. Do NOT use to fact-check, to add new content, or to translate.
---

# clean-draft

Make a draft legible. "Legible" means two things, and this skill checks both:

1. **Usable.** The reader can act on it without doing the writer's work. The recommendation comes first, the options are narrowed, and the ask is specific.
2. **Readable.** Each sentence says one thing, in plain words, the same way every time.

This skill edits form, not facts. Never add a claim, number, name, date, or decision that is not in the draft. If the draft lacks something a reader needs, such as an owner or a recommendation, flag the gap. Do not invent the missing piece.

## Workflow

1. **Get the draft and the audience.** If the user didn't name the audience, state your best guess in one line ("Assuming this goes to engineering leads.") and continue. The audience sets the level of detail and jargon.
2. **Lint the original.** Save the draft to a temp file and run the checker:
   ```bash
   python3 scripts/prose_check.py draft.md
   ```
   The checker returns `FAIL` lines for banned phrases and very long sentences, and `WARN` lines for heuristics. A warning means "look at this." It does not mean "rewrite this."
3. **Fix the structure first** with the usability rules below. Reorder, cut, and narrow before you edit sentences. Structure changes make many sentence edits unnecessary.
4. **Fix the sentences** with the readability rules below.
5. **Lint the rewrite.** Clear every `FAIL`. Clear each `WARN` unless the original wording is better. In that case, keep it and know why.
6. **Return the result** in this order:
   - The cleaned draft, ready to paste.
   - The **sources you moved out of the body**, only if any exist. Pair each one with the claim it supports.
   - A list of **gaps for the author**, only if any exist. These are things you could not fix without new facts: a missing owner, a missing date, no recommendation, an unclear ask.
   - One line on what changed, such as "Cut from 640 to 310 words; moved the recommendation to the top; split 9 long sentences."

If the user asks for a review only, skip the rewrite. Return the findings as quoted line → suggested fix pairs.

## Usability rules (structure)

**Lead with the point.** Put the recommendation and its reason first. Then give the alternative and what it costs. Background goes after, if it is needed at all.

**Propose; don't ask open questions.** Replace "When should we meet?" with "Tuesday 2pm or Wednesday 10am?" Replace "Thoughts?" with the specific decision you need.

**State a preference.** Replace "I'm fine with anything" with "I'd pick X, but Y also works."

**Narrow the options.** Give two or three options and say which one you'd pick. Every option names its cost. An option with no stated tradeoff isn't a real option.

**Make requests specific.** Replace "This feels off" with "This function does validation, transformation, and storage. Split it into three."

**Name the owner and the scope of every ask.** Replace "Please review" with "@name: sign off on section 3 and the rollback plan by Friday." For a revised doc, say what changed since the last version.

**Show the thing, not a verdict about it.** A summary of a change is not the change. Show edits as before → after. Quote the source instead of characterizing it.

**Length counts as correctness.** Over-length output is a defect, because every reader pays to summarize it. Cut restated background, throat-clearing, and the writer's reasoning. Do not cut the substance, the tradeoff, or the counter-argument. If one point needs more than three lines to justify, it may not be ready. Say so instead of writing more.

**Expand names on first use.** A ticket key, acronym, codename, or file name carries its title or expansion the first time it appears. Write "PROJ-275 (billing retry fix)," not "PROJ-275." If you don't know the expansion, flag it. A wrong expansion is worse than a bare acronym.

**Keep sources out of the body.** A draft for other readers carries no inline source links or ids, such as a meeting link after every section. One `Inputs:` line at the top is the most it carries. Move any inline sources you find into your reply, so the author can still check each claim. Keep links the reader needs to act, such as the doc they must sign off on.

**Use the right format.** Use bullets only for parallel or sequential items. Write reasoning as prose. Use tables when they replace a long comparison. Bold headers and lead-in labels only. Scattered bold inside sentences is a common sign of AI writing.

**End cleanly.** Do not close with "Let me know if you have questions," "Hope this helps," or a summary that repeats the body. End with the ask, or with nothing.

## Readability rules (sentences)

These rules adapt about 80% of Simplified Technical English (ASD-STE100), the standard for aircraft maintenance manuals. They keep its sentence-level clarity and drop the rules that make memos stiff.

1. **One word, one meaning.** Use a term the same way every time. Never swap in a synonym for variety.
2. **One idea per sentence. Aim for 20 words; 25 is the ceiling.** If "and" joins two claims, write two sentences.
3. **Name the actor. Use the active voice.** Write "Priya owns the rollout," not "The rollout is owned." If the draft never says who acts, flag that gap.
4. **Use verbs, not nouns made from verbs.** Write "decide," not "make a decision on." Write "review," not "conduct a review of."
5. **Say it literally.** If a plain phrase exists, use it instead of a metaphor. Write "the change that matters most," not "the needle-mover."
6. **Write full sentences.** Keep articles and connecting words. Brevity comes from saying fewer things, not from dropping "the."

Smaller rules:

- **Put conditions before instructions.** Write "If the cutover fails, roll back," not "Roll back if the cutover fails."
- **Say what is true.** Use "not X but Y" only when the reader probably believes X.
- **Use plain words.** Write *use* (not utilize or leverage), *start* (not kick off), *help* (not facilitate), *to* (not in order to), *because* (not due to the fact that).
- **Keep identifiers exact.** Never simplify a proper name, ticket key, or term of art.

### Status words

In status updates, use one of these words and include what it requires. Avoid "remains open," "ongoing," and "in flight." They fit every row below, so they tell the reader nothing.

| Word | Means | Must include |
|---|---|---|
| Done | Shipped and accepted | A link or proof |
| In progress | Someone is working on it | The owner |
| Blocked | Can't move until something happens | The blocker |
| Undecided | Waiting on a decision | Who decides |
| Not started | Planned, no work yet | Nothing extra |
| Unverified | Reported, not confirmed | Who reported it |

If the draft doesn't contain the required detail, flag it as a gap for the author.

## AI tells to remove

These phrases add no meaning, and readers recognize them as machine-written. The checker fails on most of them.

- **Importance signaling:** "Here's the thing," "It's worth noting that," "The key insight is," "Make no mistake," "This is huge." Say the point itself.
- **Stock metaphors:** "move the needle," "low-hanging fruit," "north star," "unlock value," "delve," "tapestry," "at the end of the day."
- **Filler openers and closers:** "Great question," "I hope this email finds you well," "In summary:", "Hope this helps," "Let me know if you'd like."
- **Empty intensifiers:** "robust," "seamless," "comprehensive," "crucial." Say what the thing does.
- **Contrast framing nobody asked for:** "This isn't just X, it's Y." Say Y.
- **Hedge stacks:** "might potentially," "could possibly help to." Pick one word, or state the claim and its confidence plainly.

## Where the rules stop

- **Keep the author's voice and position.** Directness and disagreement come from what is said, not from sentence length. Never soften a disagreement to meet a style rule.
- **Telegraphic is not plain.** "Pilot scope/acceptance · Admin or greenfield" is short, but the reader has to fill in the meaning. Write full sentences.
- **Don't split a claim from its condition** just to get under 25 words.
- **Narrowing options is good; hiding what you cut is not.** If you drop options from the draft, mention them in the change line.
- **Don't trade accuracy for confidence.** If the draft hedges because the facts are uncertain, keep the uncertainty and state it once, plainly. Don't turn a guess into a firm claim.
- **The checker flags; you judge.** To exempt a line on purpose, add `<!-- prose-check: skip -->` to it.

## Checker reference

`scripts/prose_check.py` requires Python 3 only (standard library).

```bash
python3 scripts/prose_check.py FILE            # report; exit 1 on any FAIL
python3 scripts/prose_check.py -               # read stdin
python3 scripts/prose_check.py --strict FILE   # warnings also fail
python3 scripts/prose_check.py --max-words 20 FILE --hard-words 30
python3 scripts/prose_check.py --json FILE
python3 scripts/prose_check.py --only fail -   # FAIL lines only, from stdin
```

Exit codes: 0 means no `FAIL`, 1 means at least one `FAIL` (or any finding with `--strict`), and 2 means a bad file or flag.

Rule tags in the output: `ai-tell`, `mannered`, `filler` (FAIL); `sentence-length` (FAIL past 40 words, WARN past 25); `passive`, `nominalization`, `noun-stack`, `vague-status`, `plain-word`, `inline-cite` (WARN). `inline-cite` flags `granola:` and `session:` ids in the body. The checker skips code fences, inline code, URLs, and headings.
