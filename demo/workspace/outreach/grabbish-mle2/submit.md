# Submit packet - Grabbish / Machine Learning Engineer II (J0001)
Deadline: 2026-09-20 · Fit 84 · Source: Greenhouse

## Claude prepared
- [x] `../../resume/v2-tailored-grabbish-mle.md` -> export to
      `Li-Wei-Machine-Learning-Engineer.pdf` (ats_check: 0 errors)
- [x] `cover-letter.md`
- [x] `answers.md`

## You submit
URL: https://boards.greenhouse.io/grabbish/jobs/1

| Field | Value |
|---|---|
| Resume | Li-Wei-Machine-Learning-Engineer.pdf |
| Cover letter | paste `cover-letter.md` |
| Work authorization | [USER: select "Singapore PR - no pass required"] |
| Earliest start date | [USER: 1 month from offer] |
| Expected salary | [USER: your call. target.md says 8.5-11k, floor 8k. Consider giving a range, not a number] |
| How did you hear about us | Company careers page |
| Referral | [USER: you flagged an ex-colleague here - ask them BEFORE submitting; an internal referral outranks a cold apply] |

## Attention points
- Apply within 72h - posted 2026-08-30.
- The JD's hard requirements you do not meet: Docker/K8s, CI/CD, Spark, MLflow.
  Do not claim them. `answers.md` handles this honestly by pointing at the
  in-progress forecast-service project instead.
- After submitting, run:
  `python .claude/skills/job-hunt/scripts/jobs_db.py log J0001 --status applied --resume v2-tailored`
