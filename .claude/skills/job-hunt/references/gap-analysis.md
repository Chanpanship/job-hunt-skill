# Stage 1 — Gap analysis

Do not analyze gaps against your general sense of the market. Analyze against
real, current postings.

## Method
1. Pull 5–10 live JDs matching `target.md` (stage 4 tooling, or ask the user to
   paste them). Save raw text under `workspace/jobs/jd/`.
2. Extract from each: required years, must-have hard skills, nice-to-haves,
   domain knowledge, credentials, seniority signals.
3. Tally frequency across postings. A requirement in 8/10 postings is a real
   gate; one in 2/10 is noise.
4. Score the user per requirement: `have / partial / missing`.

## Output — `workspace/gap-analysis.md`
```markdown
# Gap analysis — <target role>
Based on N postings (list them with links and dates)

## Requirement frequency table
| Requirement | Appears in | User status | Evidence in profile | Gap class |
|---|---|---|---|---|

Gap class:
- `none`
- `wording` — user has it but the resume doesn't say it (fix in stage 3, free)
- `cheap` — closeable in <4 weeks (a project, a cert, a refresher)
- `structural` — needs months or a job change (years of experience, a domain)

## Verdict
- Ready to apply now for: ...
- Apply while closing wording gaps: ...
- Not competitive yet, and why: ...
- Recommended target adjustment, if any (one paragraph, no hedging)
```

## Common failure to avoid
Labelling a gap `cheap` when it is `structural`. A weekend project does not
substitute for "5 years of production Kubernetes". Being honest here is the
whole value of this stage.
