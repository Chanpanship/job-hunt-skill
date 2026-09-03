# job-hunt-agent

An agent skill for running a real job search end to end: gap analysis,
background building, a practice plan, resume tailoring, sourcing openings
across job boards, and a tracked application pipeline.

Works with Claude Code (auto-loads the skill), Codex CLI and others (they read
`AGENTS.md`).

## Layout
```
AGENTS.md                              entry point for non-Claude agents
.claude/skills/job-hunt/
  SKILL.md                             the 6-stage pipeline + hard rules
  references/                          one file per stage, loaded on demand
    intake.md  gap-analysis.md  background-building.md
    resume.md  sourcing.md  mass-apply.md  interview-prep.md
  scripts/
    jobs_db.py                         job + application tracker (CSV)
    ats_check.py                       resume ATS/content lint
  assets/resume-template.md            ATS-safe single-column template
demo/workspace/                        filled-in fictional example (see DEMO.md)
workspace/                             all of your actual data lives here
```

## See it work first
`DEMO.md` walks through a filled-in fictional case in `demo/workspace/`, with
real script output (including one place where the tooling's own metric rewards a
worse resume). Try:

```bash
python .claude/skills/job-hunt/scripts/ats_check.py demo/workspace/resume/v1-before.md --jd demo/workspace/jobs/jd/grabbish-mle.txt
```

## Start
In Claude Code, from this directory:

```bash
claude "help me start a job search - here's my resume: <path>"
```

In Codex CLI:

```bash
codex "read AGENTS.md, then start stage 0 of the job hunt with my resume at <path>"
```

## Tracker
```bash
python .claude/skills/job-hunt/scripts/jobs_db.py add --company "Acme" --title "ML Engineer" --source greenhouse --fit 82
```

```bash
python .claude/skills/job-hunt/scripts/jobs_db.py stats
```

## What it will not do
Submit applications, send messages, create accounts, solve CAPTCHAs, enter your
personal data into websites, or put a claim on your resume that you did not
make. It prepares everything; you press Send. This is deliberate - auto-submission
gets accounts banned and answers legal attestations only you may answer.

`workspace/` will contain personal data. Do not commit it to a public repo -
it is gitignored by default.
