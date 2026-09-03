# Demo walkthrough

All company names below are fictional or deliberately garbled placeholders.
A fictional candidate ("Li Wei", a Singapore data analyst trying to move into
ML engineering) with a filled-in `demo/workspace/`. Nothing here touches your
real `workspace/`.

Everything below is real output from the scripts in this repo, not a mockup.

## 1. The state directory after stages 0-5

```
demo/workspace/
  profile.md      target.md      gap-analysis.md      plan.md
  jobs/jd/grabbish-mle.txt       jobs/jobs.csv        jobs/applications.csv
  resume/v1-before.md            resume/v2-tailored-grabbish-mle.md
  outreach/grabbish-mle2/        submit.md  cover-letter.md
```

## 2. Resume lint, before vs after

```bash
python .claude/skills/job-hunt/scripts/ats_check.py \
  demo/workspace/resume/v1-before.md --jd demo/workspace/jobs/jd/grabbish-mle.txt
```
v1 (a typical bad resume): **1 error, 17 warnings** - a markdown table ATS
parsers mangle, mixed date formats, 14 dead phrases ("responsible for",
"passionate about", "references available upon request"), 6/6 bullets with no
number, three bullets starting "Worked on".

```bash
python .claude/skills/job-hunt/scripts/ats_check.py \
  demo/workspace/resume/v2-tailored-grabbish-mle.md --jd demo/workspace/jobs/jd/grabbish-mle.txt
```
v2 (tailored from the same facts): **0 errors, 0 warnings**, exit 0.

### The interesting part
v2 scores *lower* on JD requirement coverage than v1: **42% vs 58%**. v1 wins
that number by listing Kubernetes, Spark and MLflow in a skills table when the
profile says "exposure only". This is why the tool prints the coverage as a
checklist and explicitly says it is not a score to maximise, and why
`references/resume.md` forbids optimising it. A resume that claims every term
scores 100% and fails the interview.

## 3. Pipeline tracking

```bash
JOBHUNT_WORKSPACE=demo/workspace python .claude/skills/job-hunt/scripts/jobs_db.py list
JOBHUNT_WORKSPACE=demo/workspace python .claude/skills/job-hunt/scripts/jobs_db.py stats
```
7 tracked, 5 applied, 40% response, broken down by source. `J0006 CryptoQuant
Global` is in there at fit 30 with a scam flag in `notes` (Telegram-only
recruiting, bank details requested pre-offer) - the skill surfaces those rather
than silently dropping them.

## 4. What an application packet looks like
`demo/workspace/outreach/grabbish-mle2/` - `submit.md` is a field-by-field
filling guide with `[USER: ...]` on everything only the candidate may answer
(work authorization, salary expectation, start date). Claude does not submit it.

Read `cover-letter.md` for the tone the skill aims at: it names the gap
(no production Kubernetes/Spark) instead of papering over it.

## 5. Things the demo deliberately shows going *wrong*
- Coverage metric rewarding a dishonest resume (above).
- `plan.md` has an "Explicitly NOT in this plan" section killing 60 hours of
  LeetCode, because this target screens on ML system design and SQL instead.
- `gap-analysis.md` refuses to call the deployment gap `wording`, and states the
  fallback target if the project does not ship.

## Reset the demo
```bash
rm -rf demo/workspace/jobs/*.csv
```
