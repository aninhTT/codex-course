# The rigor pass — GenAI Starting Criteria + DVFR (optional)

Read this **only when the user wants to prioritize or justify** — compare candidates, decide what's worth doing first, or make the case to someone else. It is a **lens for ranking, never a gate.** Don't run it by default, and never use it to drop a candidate before the user has seen it. Every candidate still gets captured and shown; this just adds a structured opinion on top.

Record the result in the candidate's **DVFR block** (see `references/use-case-template.md`), and reflect the headline in the backlog if helpful.

## Step 1 — GenAI Starting Criteria (a quick fit signal)

A fast read on whether a candidate is the *kind of thing* GenAI is good at. Check it against four criteria — treat a strong fit as ~3 of 4, but this is a **signal, not a pass/fail threshold**:

| Criterion | Strong when… |
|-----------|--------------|
| **Routine workflow** | It happens on a predictable cadence with consistent structure |
| **Examples available** | Past versions, templates, or historical data exist to learn from |
| **Underutilized data** | Relevant data in chat, docs, email, files, or meetings isn't being systematically used |
| **Higher-value unlock** | Automating it frees the person for more valuable work |

A candidate that hits few of these isn't disqualified — it's just lower-leverage right now. Note it and let the user decide.

## Step 2 — DVFR (the four-dimension rubric)

One line per dimension, a traffic light + a short phrase. No paragraphs.

| Dimension | Question | Scoring |
|-----------|----------|---------|
| **Desirability** | Is there real evidence someone wants/needs this? | 🟢 Multiple signals · 🟡 Inferred need · 🔴 No clear demand |
| **Viability** | Will it create real value? | 🟢 Clear time/quality savings · 🟡 Likely but hard to quantify · 🔴 Effort may exceed benefit |
| **Feasibility** | Can it be built with the tools on hand? | 🟢 Buildable now as a chat / Project with current tools · 🟡 Needs a Skill, app, or extra setup/connectors · 🔴 Missing data access or infrastructure |
| **Responsibility** | Is it safe and appropriate? | 🟢 Low risk, no sensitive data · 🟡 Needs guardrails or human review · 🔴 PII / bias / oversight concerns |

**Feasibility ties to the build, not a tool brand.** Express it in terms of the build type from *Pick the build* and the tools the user actually has (default: Claude — Chat, Projects, Cowork, Claude Code). Only call something 🔴 when a genuinely missing tool, data source, or access is required — not because a particular vendor product isn't named.

## Using the result

- **Rank, don't filter.** Use the scores to suggest an order ("strongest first: …") or a top-N, always leaving the full menu intact.
- **Honesty over fluency.** A 🟡 or 🔴 is useful information; don't inflate scores to make a candidate look better.
- **Pair with the gut-check.** Before recommending a hands-off build (a Skill or a schedule), apply the framework's gut-check — *"can you tell when it's wrong without redoing it yourself?"* If not, keep a human in the loop regardless of the scores.
