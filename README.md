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

## Start

Point your agent at this folder, then talk to it in plain language:

> help me start a job search - here's my resume: `<path>`

**Claude Code (desktop app)** - open this folder as the project. The skill loads
by itself when you mention job hunting. Nothing to run.

**Claude Code (terminal)** - run `claude` from this directory.

**Codex CLI and others** - ask it to read `AGENTS.md` first.

From there it is a normal conversation: "find me openings in Singapore",
"tailor my resume for this posting", "how am I doing this week". State persists
in `workspace/`, so a later session resumes instead of re-interviewing you.

The two Python scripts bundled with the skill are called by the agent, not
by you.

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

## Where the line is

The skill will fill in an application for you - upload the resume, enter your
contact details, draft the free-text answers. It stops at the final
Submit button.

Two things it leaves to you, always:

- **The submit click.** An application cannot be withdrawn, and most job boards'
  terms ban automated submission and enforce it with account bans.
- **Legal attestations** - work authorization, visa status, criminal history,
  prior employment at the company. A wrong answer there can void an offer after
  you have signed, so they stay blank until you fill them.

It also will not create accounts, log in, handle credentials or payment details,
solve CAPTCHAs, or put a claim on your resume that you did not make.

This is a policy, not a capability limit - an agent with browser control can
obviously click Submit. Whether a given agent honours these files is up to that
agent.

## License

MIT - see `LICENSE`.
