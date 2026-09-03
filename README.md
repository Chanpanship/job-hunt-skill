# job-hunt-skill

**English** · [简体中文](README.zh-CN.md)

An agent skill for running a real job search end to end: gap analysis against
real job descriptions, background building, a practice plan, resume tailoring,
sourcing openings across job boards, and a tracked application pipeline.

Works with Claude Code (auto-loads the skill), Codex CLI, and any other agent
that can read files and run Python (they read `AGENTS.md`).

## Install

**Per project** - clone anywhere and work inside it:

```bash
git clone https://github.com/Chanpanship/job-hunt-skill.git && cd job-hunt-skill
```

**Globally** - available in every session, from any directory:

```bash
git clone https://github.com/Chanpanship/job-hunt-skill.git /tmp/jhs && cp -r /tmp/jhs/.claude/skills/job-hunt ~/.claude/skills/
```

Skills are discovered from the working directory (`.claude/skills/`) or from
`~/.claude/skills/`. Claude Code picks the skill up when you mention job
hunting; other agents should be pointed at `AGENTS.md`.

Requires Python 3 (standard library only - no dependencies).

## See it work first

`DEMO.md` walks through a filled-in fictional case under `demo/workspace/`, with
real script output - including one place where the tooling's own metric rewards
a *worse* resume. Try:

```bash
python .claude/skills/job-hunt/scripts/ats_check.py demo/workspace/resume/v1-before.md --jd demo/workspace/jobs/jd/grabbish-mle.txt
```

That resume gets 1 error and 17 warnings. The tailored version built from the
same facts gets zero.

## Start

In Claude Code, from the project directory:

```bash
claude "help me start a job search - here's my resume: <path>"
```

In Codex CLI:

```bash
codex "read AGENTS.md, then start stage 0 of the job hunt with my resume at <path>"
```

Then just talk to it. State persists in `workspace/`, so a later session
resumes instead of re-interviewing you.

## The six stages

| Stage | Output |
|---|---|
| 0 Intake | `profile.md`, `target.md` - parsed from your resume where possible |
| 1 Gap analysis | requirement frequency across 5-10 real postings; gaps classed `wording` / `cheap` / `structural` |
| 2 Background + practice | dated `plan.md`; every item traced to a stage-1 gap |
| 3 Resume | one master resume, one tailored per application, ATS-linted |
| 4 Sourcing | `jobs.csv` with a 0-100 fit score per opening |
| 5 Applying | per-job packets: resume, cover letter, screening answers, filling guide |
| 6 Follow-up | weekly response-rate review with explicit decision rules |

## Tracker

```bash
python .claude/skills/job-hunt/scripts/jobs_db.py add --company "Acme" --title "ML Engineer" --source greenhouse --fit 82
```

```bash
python .claude/skills/job-hunt/scripts/jobs_db.py stats
```

Under 5% response after 30 applications and `stats` tells you to fix the resume
or the targeting rather than send more.

## What it will not do

Submit applications, send messages, create accounts, solve CAPTCHAs, enter your
personal data into websites, or put a claim on your resume that you did not
make. It prepares everything; you press Send.

This is deliberate. Auto-submission gets accounts banned, sends wrong-company
resumes, and answers legal attestations - work authorization, criminal history,
prior employment - that only you may answer.

## Privacy

`workspace/` holds your real resume, contact details and application history. It
is gitignored. Do not commit it, and think before putting the folder in a synced
cloud directory.

## License

MIT - see `LICENSE`.
