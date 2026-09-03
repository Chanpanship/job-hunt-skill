# Stage 0 — Intake

## Goal
Produce `workspace/profile.md` and `workspace/target.md`. These are the single
source of truth; every later stage reads them instead of re-asking the user.

## Method
1. Ask the user for any existing resume/CV, LinkedIn export, or GitHub handle.
   Parse it. Parsing beats interviewing.
2. Fill in what you can. List the remaining unknowns.
3. Ask the unknowns in ONE batched message, max ~8 questions. Skip anything
   you can reasonably infer and mark it `(inferred)` in profile.md.

## profile.md template
```markdown
# Profile — <name>
Updated: <YYYY-MM-DD>

## Contact
Email / phone / city / LinkedIn / GitHub / portfolio

## Work authorization
Citizenship or PR status, visa needs per target country, notice period,
earliest start date

## Education
Degree, institution, dates, GPA (only if strong and the market expects it)

## Experience
For each role: employer, title, dates, 3–6 raw accomplishment notes with
numbers. Raw and verbose — tailoring happens later.

## Projects / publications / open source

## Skills
Tiered: expert (would defend in interview) / working / exposure only.
Never flatten these into one list on a resume.

## Constraints
Salary floor and target, remote/hybrid/onsite, industries to avoid, companies
to avoid (e.g. current employer or its clients), hours per week available for
job hunting and upskilling
```

## target.md template
```markdown
# Targets
Updated: <YYYY-MM-DD>

## Primary target
Role family, seniority, 2–3 example job titles, 5–10 example companies

## Secondary target (fallback)

## Geography
Cities / countries, visa feasibility per market

## Comp
Currency, base range, total-comp range, floor (walk-away number)

## Timeline
Target offer date, weekly application quota
```

## Sanity checks before leaving this stage
- Seniority claim vs years of relevant experience — flag a mismatch of >1 level.
- Visa feasibility per target market — flag markets that are effectively closed.
- Weekly quota vs available hours: a well-tailored application costs 30–60 min.
  If the quota exceeds available time, fix the quota now, not in stage 5.
