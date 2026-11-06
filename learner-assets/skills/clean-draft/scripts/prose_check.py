#!/usr/bin/env python3
"""prose_check — a readability lint for drafts, especially AI-written ones.

It asks one question: can a reader read this once and understand it?
The rules are in ../SKILL.md. They adapt about 80% of Simplified Technical
English (ASD-STE100), plus bans on stock AI phrases, metaphor-heavy prose,
and filler openers and closers. It needs only the Python 3 standard library.

Two severities, because the rules are not equally mechanical:

  FAIL   a banned phrase, or a sentence past the hard ceiling. Unambiguous.
  WARN   long sentence, passive voice, nominalization, noun stack, vague
         status, plain-word swap, inline citation id. Heuristics: "look at this", not
         "rewrite this".

Usage:
  prose_check.py FILE [FILE ...]
  prose_check.py -                    # stdin
  prose_check.py --strict FILE        # warnings also fail
  prose_check.py --max-words 25 FILE  # soft sentence ceiling (default 25)
  prose_check.py --hard-words 40 FILE # hard sentence ceiling (default 40)
  prose_check.py --only fail FILE     # suppress warnings in the report
  prose_check.py --json FILE
  prose_check.py --quiet FILE         # summary line only

Exit: 0 clean (or warnings only) · 1 failures (or any finding with --strict)
      · 2 usage error

Escapes:
  <!-- prose-check: skip -->        on a line — exempt it
  <!-- prose-check: skip-file -->   in the first 20 lines — exempt the file

Not checked: code fences, inline code, URLs, headings, table separator rows.
"""

import argparse
import json
import re
import sys

# --------------------------------------------------------------------------
# FAIL — banned phrases. AI importance-signaling + mannered stock phrases +
# filler openers/closers. Matched case-insensitively on word boundaries.
# --------------------------------------------------------------------------

BANNED = [
    # AI tells — importance-signaling in place of saying the thing
    ("ai-tell", r"is the whole game"),
    ("ai-tell", r"the one thing to (?:understand|know|remember)"),
    ("ai-tell", r"and (?:it|this|that) is real\b"),
    ("ai-tell", r"the genuinely hard (?:one|part)"),
    ("ai-tell", r"here'?s the (?:thing|kicker|catch)"),
    ("ai-tell", r"it'?s worth (?:noting|calling out|flagging) that"),
    ("ai-tell", r"(?:this|that) is (?:huge|key|critical)\b[.!]"),
    ("ai-tell", r"let that sink in"),
    ("ai-tell", r"make no mistake"),
    ("ai-tell", r"the key (?:insight|takeaway) (?:is|here)"),
    ("ai-tell", r"(?:isn'?t|is not|it'?s not) just (?:a |an |about )?[\w-]+(?: [\w-]+)?\s*[,;—–-]+\s*(?:it'?s|it is)"),
    # Mannered prose — metaphor where a literal phrase exists
    ("mannered", r"earns? (?:its|their) keep"),
    ("mannered", r"a dial worth turning"),
    ("mannered", r"moves? the needle"),
    ("mannered", r"north[- ]star metric"),
    ("mannered", r"in the weeds"),
    ("mannered", r"(?:double|triple)[- ]click (?:on|into)"),
    ("mannered", r"boil(?:ing)? the ocean"),
    ("mannered", r"low[- ]hanging fruit"),
    ("mannered", r"secret sauce"),
    ("mannered", r"tip of the iceberg"),
    ("mannered", r"at the end of the day"),
    ("mannered", r"paints? a picture"),
    ("mannered", r"\bunlock(?:s|ed|ing)? (?:value|potential)"),
    ("mannered", r"\btapestry\b"),
    ("mannered", r"\bdelve\b"),
    # Filler openers / closers
    ("filler", r"^\W*(?:great|good) question"),
    ("filler", r"^\W*(?:bottom line|tl;?dr|in summary|to summarize|in conclusion)\s*:"),
    ("filler", r"let me know if you (?:want|need|have|'d like)"),
    ("filler", r"hope (?:this|that) helps"),
    ("filler", r"i hope this (?:email|message) finds you"),
]
BANNED = [(k, p, re.compile(r"(?<![\w-])" + p if not p.startswith("^") else p, re.I))
          for k, p in BANNED]

# --------------------------------------------------------------------------
# WARN — heuristics
# --------------------------------------------------------------------------

# Vague status: the status vocabulary in SKILL.md replaces these.
VAGUE_STATUS = re.compile(
    r"\b(?:remains?|remained|remaining|stays?|is still|are still) "
    r"(?:open|unresolved|pending|tbd|outstanding|in flight)\b"
    r"|\bin flight\b|\bongoing\b", re.I)

# Nominalizations: verb disguised as noun, carried by a light verb.
NOMINALIZATION = re.compile(
    r"\b(?:make|makes|made|making|take|takes|took|give|gives|gave|provide|provides|"
    r"provided|perform|performs|performed|conduct|conducts|conducted|do|does|did|"
    r"carry out|carries out|have|has|reach|reached|come to|came to)\s+"
    r"(?:a |an |the |some |)"
    r"(?:decision|determination|review|analysis|assessment|evaluation|"
    r"recommendation|investigation|update|adjustment|modification|"
    r"implementation|consideration|selection|improvement|reduction|"
    r"conclusion|agreement|correction|discussion|confirmation)\b", re.I)

# Plain-word swaps.
PLAIN_WORDS = [
    (re.compile(r"\butiliz(?:e|es|ed|ing|ation)\b", re.I), "use"),
    (re.compile(r"\bleverag(?:e|es|ed|ing)\b(?! ratio)", re.I), "use"),
    (re.compile(r"\bfacilitat(?:e|es|ed|ing)\b", re.I), "help / run"),
    (re.compile(r"\bin order to\b", re.I), "to"),
    (re.compile(r"\bkick(?:s|ed|ing)? off\b", re.I), "start"),
    (re.compile(r"\bcircle back\b", re.I), "return to / follow up"),
    (re.compile(r"\bat this point in time\b", re.I), "now"),
    (re.compile(r"\bdue to the fact that\b", re.I), "because"),
    (re.compile(r"\b(?:robust|seamless(?:ly)?|comprehensive|crucial)\b", re.I), "say what it does"),
    (re.compile(r"\b(?:might|may|could) (?:potentially|possibly)\b", re.I), "pick one hedge"),
]

# Inline citation ids: machine ids that only the author can open. A draft
# for other readers keeps them out of the body (see SKILL.md, "Keep sources
# out of the body"). Ids inside inline code are mentions, not citations.
INLINE_CITE = re.compile(r"(?<![\w-])(?:granola|session):[A-Za-z0-9][A-Za-z0-9-]{3,}", re.I)

# Passive: be-verb + past participle, optional "by".
PASSIVE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
    r"(?:\w+ed|built|done|given|made|held|kept|known|left|led|lost|met|paid|"
    r"run|seen|sent|set|shown|spent|taken|told|understood|written|chosen|"
    r"driven|owned|split|cut|put)\b(?!\s+(?:to|that)\b)", re.I)
# Adjectival participles that read fine after "is".
PASSIVE_OK = re.compile(
    r"\b(?:is|are|was|were|be|been)\s+(?:blocked|done|paused|planned|"
    r"undecided|unverified|scoped|interested|based|located|supposed|"
    r"used to|related|required|expected|involved|concerned|tired|"
    r"focused|aligned|committed|staffed|confirmed|shipped|retired|"
    r"descoped|de-scoped|unstarted|unresolved|scheduled|set)\b", re.I)

# Noun stacks: ≥5 consecutive tokens with no function word or common verb.
FUNCTION_WORDS = set("""
a an the and or but nor so yet for of to in on at by with from into onto over
under about after before between through during without within via per as than
then that this these those it its is are was were be been being am has have had
do does did will would can could should may might must shall not no if when
while because since until unless where which who whom whose what how why all
any each every some most more less few many much one two three i you he she
we they me him her us them my your his our their there here also just only
very too still even own same other such both either neither
remains remain needs need owns own runs run moves move uses use gets get goes
go makes make takes take says say shows show keeps keep sets set targets target
stays stay depends depend blocks block covers cover holds hold leads lead
precedes precede proposes propose returns return reaches reach waits wait
""".split())
TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’/+.&-]*")
# Stack tokens keep punctuation so a comma, colon, paren or arrow breaks a run.
STACK_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’+&-]*|[,;:()\[\]—–→/·=\"“”]")
PUNCT_RE = re.compile(r"^[,;:()\[\]—–→/·=\"“”]$")
# Quoted or italicized spans are mentions, not uses — exempt from bans.
QUOTED_RE = re.compile(r"\"[^\"]*\"|“[^”]*”|(?<![*\w])\*(?!\*)[^*]+\*(?!\*)")
NOUN_STACK_MIN = 5

# --------------------------------------------------------------------------
# Structure
# --------------------------------------------------------------------------

FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+")
TABLE_SEP_RE = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
TABLE_ROW_RE = re.compile(r"^\s*\|")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
FRONTMATTER_RE = re.compile(r"^---\s*$")
SKIP_LINE_RE = re.compile(r"<!--\s*prose-check:\s*skip\s*-->", re.I)
SKIP_FILE_RE = re.compile(r"<!--\s*prose-check:\s*skip-file\s*-->", re.I)

INLINE_CODE_RE = re.compile(r"`[^`]*`")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->")
EMPH_RE = re.compile(r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1")
CITE_PAREN_RE = re.compile(r"\((?:[^()]*(?:granola:|session:|slack|linear|ts \d))[^()]*\)", re.I)
# Sentence end: . ! ? followed by space + capital/quote/digit, or end of text.
# Avoid splitting on e.g., i.e., vs., v4.1, initials.
ABBREV_RE = re.compile(r"\b(?:e\.g|i\.e|vs|etc|approx|incl|cf|Mr|Ms|Dr|St|No)\.$", re.I)


def clean(text):
    text = HTML_COMMENT_RE.sub(" ", text)
    text = CITE_PAREN_RE.sub(" ", text)
    text = INLINE_CODE_RE.sub(" CODE ", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = URL_RE.sub(" URL ", text)
    text = EMPH_RE.sub(r"\2", text)
    text = BULLET_RE.sub("", text)
    text = re.sub(r"^\s*>\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text):
    out, start = [], 0
    for m in re.finditer(r"[.!?]+[\"'”’)]*(?=\s+[\"'“‘(]?[A-Z0-9*]|\s*$)", text):
        chunk = text[start:m.end()]
        if ABBREV_RE.search(chunk.rstrip("\"'”’)")):
            continue
        out.append(chunk.strip())
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    # A middot or " · " separates fragments in index-style lines.
    final = []
    for s in out:
        final.extend(p.strip() for p in re.split(r"\s·\s", s) if p.strip())
    return final


def word_count(sentence):
    return len(TOKEN_RE.findall(sentence))


def noun_stacks(sentence):
    tokens = STACK_TOKEN_RE.findall(sentence)
    run, hits = [], []
    for t in tokens + [""]:
        low = t.lower().strip(".")
        is_break = (not t or PUNCT_RE.match(t) or low in FUNCTION_WORDS or low.endswith("ing")
                    or (low.endswith("ed") and len(low) > 4) or low.isdigit()
                    or t in ("CODE", "URL"))
        if is_break:
            # Proper-noun runs (Online Services SRE) are names, not stacks.
            if len(run) >= NOUN_STACK_MIN and sum(1 for w in run if w[:1].islower()) >= 2:
                hits.append(" ".join(run))
            run = []
        else:
            run.append(t)
    return hits


def units(lines):
    """Yield (lineno, text) prose units: a paragraph, list item, or table cell."""
    in_fence = False
    in_front = False
    buf, buf_line = [], None

    def flush():
        nonlocal buf, buf_line
        if buf:
            yield_val = (buf_line, " ".join(buf))
            buf, buf_line = [], None
            return yield_val
        return None

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if i == 1 and FRONTMATTER_RE.match(line):
            in_front = True
            continue
        if in_front:
            if FRONTMATTER_RE.match(line):
                in_front = False
            continue
        if FENCE_RE.match(line):
            r = flush()
            if r:
                yield r
            in_fence = not in_fence
            continue
        if in_fence or SKIP_LINE_RE.search(line):
            r = flush()
            if r:
                yield r
            continue
        if not line.strip() or HEADING_RE.match(line) or re.match(r"^\s*(?:---+|\*\*\*+)\s*$", line):
            r = flush()
            if r:
                yield r
            continue
        if TABLE_ROW_RE.match(line):
            r = flush()
            if r:
                yield r
            if not TABLE_SEP_RE.match(line):
                for cell in line.strip().strip("|").split("|"):
                    if cell.strip():
                        yield (i, cell)
            continue
        if BULLET_RE.match(line):
            r = flush()
            if r:
                yield r
        if not buf:
            buf_line = i
        buf.append(line)
    r = flush()
    if r:
        yield r


def check_text(text, max_words, hard_words):
    """Return findings for one prose unit."""
    findings = []
    raw = HTML_COMMENT_RE.sub(" ", text)
    unquoted = QUOTED_RE.sub(" QUOTE ", raw)

    for kind, pat_src, pat in BANNED:
        target = clean(unquoted) if pat_src.startswith("^") else unquoted
        m = pat.search(target)
        if m:
            findings.append(("FAIL", kind, m.group(0).strip()))

    cleaned = clean(raw)
    cleaned_uq = clean(unquoted)
    for sentence in split_sentences(cleaned):
        n = word_count(sentence)
        if n > hard_words:
            findings.append(("FAIL", "sentence-length", "%d words: %s" % (n, abbrev(sentence))))
        elif n > max_words:
            findings.append(("WARN", "sentence-length", "%d words: %s" % (n, abbrev(sentence))))
        for stack in noun_stacks(sentence):
            findings.append(("WARN", "noun-stack", stack))

    for m in VAGUE_STATUS.finditer(cleaned_uq):
        findings.append(("WARN", "vague-status", "%s — use Done/In progress/Blocked/Undecided/Not started/Unverified" % m.group(0)))
    for m in NOMINALIZATION.finditer(cleaned_uq):
        findings.append(("WARN", "nominalization", m.group(0)))
    for pat, swap in PLAIN_WORDS:
        m = pat.search(cleaned_uq)
        if m:
            findings.append(("WARN", "plain-word", "%s → %s" % (m.group(0), swap)))
    cites = INLINE_CITE.findall(INLINE_CODE_RE.sub(" ", raw))
    if cites:
        findings.append(("WARN", "inline-cite", "%s — move sources to your reply" % ", ".join(cites)))
    for m in PASSIVE.finditer(cleaned_uq):
        if not PASSIVE_OK.match(cleaned_uq, m.start()):
            findings.append(("WARN", "passive", m.group(0)))
    return findings


def abbrev(s, n=90):
    return s if len(s) <= n else s[: n - 1] + "…"


def check_file(name, content, args):
    lines = content.splitlines()
    if any(SKIP_FILE_RE.search(l) for l in lines[:20]):
        return {"file": name, "skipped": True, "findings": [], "sentences": 0}
    results, sentences = [], 0
    for lineno, text in units(lines):
        sentences += len(split_sentences(clean(text)))
        for sev, kind, detail in check_text(text, args.max_words, args.hard_words):
            results.append({"line": lineno, "severity": sev, "rule": kind, "detail": detail})
    return {"file": name, "skipped": False, "findings": results, "sentences": sentences}


def main():
    ap = argparse.ArgumentParser(description="Readability lint for drafts (see SKILL.md).")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--max-words", type=int, default=25)
    ap.add_argument("--hard-words", type=int, default=40)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--only", choices=["fail", "warn"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    reports = []
    for f in args.files:
        try:
            content = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        except OSError as e:
            print("prose_check: %s" % e, file=sys.stderr)
            return 2
        reports.append(check_file("<stdin>" if f == "-" else f, content, args))

    fails = sum(1 for r in reports for x in r["findings"] if x["severity"] == "FAIL")
    warns = sum(1 for r in reports for x in r["findings"] if x["severity"] == "WARN")
    sentences = sum(r["sentences"] for r in reports)

    if args.json:
        print(json.dumps({"fails": fails, "warns": warns, "sentences": sentences,
                          "reports": reports}, indent=2, ensure_ascii=False))
    else:
        for r in reports:
            if r["skipped"]:
                print("%s: skipped (skip-file)" % r["file"])
                continue
            if args.quiet:
                continue
            for x in r["findings"]:
                if args.only == "fail" and x["severity"] != "FAIL":
                    continue
                if args.only == "warn" and x["severity"] != "WARN":
                    continue
                print("%s:%d: %s [%s] %s" % (r["file"], x["line"], x["severity"],
                                              x["rule"], x["detail"]))
        rate = (warns / sentences * 100) if sentences else 0
        print("prose_check: %d fail, %d warn across %d sentences (%.0f warn per 100)"
              % (fails, warns, sentences, rate))

    if fails or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
