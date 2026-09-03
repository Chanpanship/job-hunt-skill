#!/usr/bin/env python3
"""Lint a resume for ATS and content problems, and optionally against a JD.

  ats_check.py workspace/resume/acme-mle.md [--jd workspace/jobs/jd/acme.txt]

Exit code 1 if any ERROR is found. WARN and INFO are advisory.
This is a lint, not a judge: a clean run does not mean the resume is good.
"""
import argparse, os, re, sys
from collections import Counter

WEAK = ["responsible for", "helped with", "worked on", "assisted with",
        "various", "utilized", "team player", "hard worker", "detail-oriented",
        "self-starter", "go-getter", "think outside the box", "synergy",
        "passionate about", "results-driven", "dynamic",
        "references available upon request"]
SECTIONS = ["experience", "education", "skills"]
STOP = set("""a an the and or of to in for on with at by from as is are was were
be been being this that these those it its their his her they we you i not no
using use used via across into over under about we our my me will can also more
most than then there here who whom which what when where how all any each both
other same such only own so too very s t don now d ll m o re ve y
another similar etc including include includes work working works
role team teams company role responsibilities requirements qualifications
strong good great excellent ability able experience experienced years year
plus nice have has had must should would across within upon
you your yours candidate ideal preferred bachelor master degree
new take taken taking make makes making help helps helping
machine learning model models data
engineer engineers scientist scientists analyst manager developer
computer science statistics mathematics engineering field related equivalent
bachelor bachelors masters phd degree senior junior staff lead principal
""".split())
# "machine learning", "data pipeline" etc. are caught as bigrams instead - a
# unigram "data" or "model" is noise in almost every tech JD.


def flag(kind, msg, out):
    out.append((kind, msg))


def tokens(text):
    """Raw lowercase word stream, stopwords kept (needed for bigrams)."""
    return re.findall(r"[a-z][a-z+#.\-]{1,}", text.lower())


def proper_nouns(text):
    """Tech proper nouns in a JD: mid-line capitalised words and acronyms.

    Catches Docker / Kubernetes / Airflow / MLflow / PyTorch / SQL even when a
    JD names them exactly once, which is the normal case for a hard
    requirement. Skips line-initial and sentence-initial words, which are
    capitalised for grammar rather than because they are proper nouns.
    """
    hits = set()
    for line in text.splitlines():
        for m in re.finditer(r"\b([A-Z][A-Za-z+#.]+|[A-Z]{2,})\b", line):
            before = line[:m.start()].rstrip()
            if not before or before.endswith((".", "!", "?", ":", ";", "-")):
                continue
            w = m.group(1).rstrip(".").lower()
            if len(w) > 1 and w not in STOP:
                hits.add(w)
    return hits


def keyphrases(text):
    """Unigrams (stopwords removed) plus adjacent bigrams (any words).

    Bigrams let 'machine learning' and 'time series' count as keywords while
    the bare unigrams stay filtered out as noise.
    """
    tk = tokens(text)
    uni = [w for w in tk if w not in STOP and len(w) > 2]
    bi = [f"{a} {b}" for a, b in zip(tk, tk[1:])
          if not (a in STOP and b in STOP) and len(a) > 2 and len(b) > 2]
    return uni + bi


def main():
    p = argparse.ArgumentParser(description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("resume")
    p.add_argument("--jd", help="plain-text job description to compare against")
    p.add_argument("--max-words", type=int, default=650,
                   help="approx one page = 650 words (default), two = 1200")
    args = p.parse_args()

    if not os.path.exists(args.resume):
        sys.exit(f"no such file: {args.resume}")
    text = open(args.resume, encoding="utf-8").read()
    low = text.lower()
    out = []

    # --- blocking content errors -------------------------------------------
    for ph in re.findall(r"\[(?:METRIC\?|TODO|USER:[^\]]*|X+)\]", text):
        flag("ERROR", f"unfilled placeholder: {ph}", out)
    for m in re.findall(r"\b(?:XX|TBD|LOREM|COMPANY_NAME|<[a-z_]+>)\b", text,
                        re.I):
        flag("ERROR", f"template leftover: {m}", out)

    # --- ATS structure ------------------------------------------------------
    missing = [s for s in SECTIONS if s not in low]
    if missing:
        flag("ERROR", "missing standard section heading(s): " + ", ".join(missing),
             out)
    if re.search(r"^\s*\|.*\|", text, re.M):
        flag("ERROR", "markdown table detected - many ATS parsers mangle tables",
             out)
    if re.search(r"<(img|table|div|td)\b", text, re.I):
        flag("ERROR", "raw HTML layout tag detected", out)
    if re.search(r"!\[[^\]]*\]\(", text):
        flag("WARN", "image in resume - ensure no content lives only in it", out)
    emoji = re.findall(r"[\U0001F300-\U0001FAFF✀-➿]", text)
    if emoji:
        flag("WARN", f"{len(emoji)} emoji/dingbat character(s) - strip for ATS",
             out)
    if re.search(r"\t", text):
        flag("WARN", "tab characters - use plain spaces", out)

    # --- dates --------------------------------------------------------------
    styles = {
        "Mon YYYY": len(re.findall(r"\b[A-Z][a-z]{2}\.? ?\d{4}\b", text)),
        "MM/YYYY": len(re.findall(r"\b\d{1,2}/\d{4}\b", text)),
        "YYYY-MM": len(re.findall(r"\b\d{4}-\d{2}\b", text)),
    }
    used = [k for k, v in styles.items() if v]
    if len(used) > 1:
        flag("WARN", "mixed date formats: " + ", ".join(used), out)
    if not used:
        flag("WARN", "no recognizable date ranges found", out)

    # --- contact ------------------------------------------------------------
    if not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text):
        flag("ERROR", "no email address found", out)
    if not re.search(r"(\+?\d[\d\s().-]{7,}\d)", text):
        flag("INFO", "no phone number found (fine in some markets)", out)

    # --- privacy ------------------------------------------------------------
    if re.search(r"\b[STFG]\d{7}[A-Z]\b", text):
        flag("ERROR", "looks like a full NRIC/FIN - remove from resume", out)
    if re.search(r"\b\d{3}-\d{2}-\d{4}\b", text):
        flag("ERROR", "looks like a US SSN - remove from resume", out)
    if re.search(r"\b\d{17}[\dXx]\b", text):
        flag("ERROR", "looks like a PRC ID number - remove from resume", out)

    # --- writing quality ----------------------------------------------------
    for w in WEAK:
        n = low.count(w)
        if n:
            flag("WARN", f'weak phrase x{n}: "{w}"', out)
    bullets = [l.strip() for l in text.splitlines()
               if re.match(r"^\s*[-*+•]\s+\S", l)]
    if bullets:
        nometric = [b for b in bullets
                    if not re.search(r"\d|percent|%|\bx\b", b, re.I)]
        if len(nometric) > len(bullets) / 2:
            flag("WARN", f"{len(nometric)}/{len(bullets)} bullets have no number",
                 out)
        longb = [b for b in bullets if len(b.split()) > 32]
        for b in longb[:5]:
            flag("WARN", f"bullet over 32 words: {b[:60]}...", out)
        firsts = Counter(b.split()[1].lower().rstrip(",.")
                         for b in bullets if len(b.split()) > 1)
        for verb, n in firsts.items():
            if n >= 3:
                flag("WARN", f'"{verb}" starts {n} bullets - vary the verbs', out)
    else:
        flag("WARN", "no bullet lines detected", out)
    if re.search(r"\bI\b|\bmy\b", text):
        flag("INFO", "first person used - resumes conventionally omit it", out)

    # --- length -------------------------------------------------------------
    wc = len(re.findall(r"\S+", text))
    if wc > args.max_words:
        flag("WARN", f"{wc} words (~{wc / 650:.1f} pages) vs target "
                     f"{args.max_words}", out)

    # --- JD requirement coverage --------------------------------------------
    if args.jd:
        if not os.path.exists(args.jd):
            sys.exit(f"no such JD file: {args.jd}")
        jd = open(args.jd, encoding="utf-8").read()
        # first line is the job title - pure noise as keywords
        jd_body = "\n".join(jd.splitlines()[1:])
        jw = Counter(keyphrases(jd_body))
        rw = set(keyphrases(text))
        cands = [w for w, n in jw.most_common(120) if n >= 2]
        # hard requirements are often named once - keep tech proper nouns
        cands += sorted(proper_nouns(jd_body) - set(cands))
        # drop a unigram already covered by a surviving bigram
        bigram_parts = {p for c in cands if " " in c for p in c.split()}
        cands = [c for c in cands if " " in c or c not in bigram_parts]
        missing_kw = [w for w in cands if w not in rw]
        covered = len(cands) - len(missing_kw)
        print(f"JD requirement terms present: {covered}/{len(cands)}"
              f" ({covered / max(len(cands), 1):.0%})")
        if missing_kw:
            print("  absent: " + ", ".join(missing_kw[:25]))
        print("  NOT a score to maximise. A resume that falsely claims every"
              " term scores 100% and fails the interview. For each absent"
              " term the only valid moves are: (a) the user genuinely has it and"
              " the resume undersells it -> add real evidence; (b) the user"
              " does not have it -> leave it absent, it is a stage-2 gap." + "\n")

    errs = [m for k, m in out if k == "ERROR"]
    for kind in ("ERROR", "WARN", "INFO"):
        for k, m in out:
            if k == kind:
                print(f"{kind:5} {m}")
    if not out:
        print("no issues found (lint only - this is not a quality judgement)")
    print(f"\n{len(errs)} error(s), "
          f"{len([1 for k, _ in out if k == 'WARN'])} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
