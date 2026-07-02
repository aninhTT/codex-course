# Sharing — optional distribution (read only when asked)

Read this **only when the user wants to distribute** something — a single candidate, a shortlist, or a summary. Everything here is **opt-in**. Two rules always hold:

1. **Draft, then confirm.** Compose the message or doc, show it to the user, and get an explicit go-ahead **before** sending or posting anything. Never message a channel or person unprompted.
2. **Degrade gracefully.** Find connector tools by **suffix**, not a hardcoded prefix (see `references/connectors.md`). If the needed connector isn't present, say so and offer to save the content to a file in the workspace instead.

Pull the content from what already exists — the candidate files and `backlog.md` — so sharing never invents claims. Keep the plain-language pain points; never surface archetype labels.

---

## 1. Channel-ready post (one candidate)

A compact post for a team/topic channel. Keep it skimmable; lead with the pain in plain words.

```
🎯 AI use case: <plain title>

The pain: <one plain sentence — what's hard today, grounded in a real signal>
The idea: <2–3 sentences — what you'd build and where (the user's tools; default Claude)>
The payoff: <time saved / quality / consistency>
<optional, only if the rigor pass ran:> DVFR: Desirability 🟢 · Viability 🟢 · Feasibility 🟢 · Responsibility 🟡 (human review)

Try this to start:
"<a copy-paste-ready first prompt tailored to this use case>"
```

Leave hashtags/mentions to the user — ask if they want any, rather than inventing them.

## 2. DM summary (top picks)

A short direct message: the top few candidates as one-liners plus a pointer back to the backlog so the recipient can browse the rest.

```
Here are the AI use cases worth a look:

1. <title> — <plain pain point in a few words>
2. <title> — <plain pain point in a few words>
3. <title> — <plain pain point in a few words>

Full menu + details: <path to backlog.md (or the use-cases/ folder)>
```

To send a DM: resolve the recipient with the search-users tool (suffix `…__slack_search_users`), then send with `…__slack_send_message` — **after** the user confirms the drafted text. If a draft tool is available (`…__slack_send_message_draft`), prefer drafting.

## 3. Summary report (doc)

A shareable write-up generated from the backlog — useful for a teammate, a lead, or a wider audience. Save it to the workspace (or a path the user gives) and offer the file back.

```markdown
# AI use cases — <scope, e.g. "for the Support team"> · <date>

**Sources:** <what was scanned — e.g. "N meetings · N Slack threads · N email threads", or "from our conversation">
**Scope:** <personal | team:<name> | goal:<name>>

## What's showing up (signal summary)
- <top recurring pains/patterns, each with attribution — "from #channel", "from recurring 'weekly update' threads", etc.>

## Candidates
<group by audience if broader scope; otherwise a flat list. For each:>
### <title>
- **Pain:** <plain sentence>
- **Idea:** <what to build, where>
- **Evidence:** <the real signal>
- <optional, if scored:> **DVFR:** D 🟢 · V 🟢 · F 🟢 · R 🟡

## Where to start (top recommendations)
1. **<title>** — <why this one first: signal strength + DVFR if scored>
2. ...

## Parked (kept for later)
- **<title>** — <why parked / what would change the calculus>
```

The "Parked" section is where any not-now candidates live — there is no separate watch list.

---

**Reuse, don't duplicate.** The report's per-candidate detail should come straight from the candidate files (`use-cases/NNN-<slug>.md`); the recommendations ordering can reuse the rigor pass (`references/evaluation.md`) if the user ran it.
