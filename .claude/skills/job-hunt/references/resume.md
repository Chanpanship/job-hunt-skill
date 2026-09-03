# Stage 3 — Resume

## Two-layer model
- `workspace/resume/master.md` — everything, unbounded length, never sent out.
- `workspace/resume/<company>-<role>.md` — a tailored subset. One page for <10
  years experience, two pages max otherwise. Academic CVs are exempt.

Tailoring means *selecting and rewording what exists*, never adding what doesn't.

## Bullet formula
`<Strong verb> <what> <how/with what>, <quantified outcome>`

- Lead with the outcome where the outcome is the impressive part.
- One metric per bullet minimum where a metric plausibly exists. If the user has
  not given a number, write `[METRIC?]` and ask before sending. Never estimate a
  number on the user's behalf.
- Cut: "responsible for", "helped with", "various", "utilized", "team player",
  adverbs, and any bullet that describes the job description rather than the
  user's own work.
- 3–5 bullets for the most recent role, 2–3 for older ones, 1–2 beyond ~8 years.

## Tailoring procedure
1. Extract the JD's must-haves (reuse the stage-1 extraction).
2. For each must-have, find the strongest evidence in `master.md`.
3. Order the resume so the top third of page one covers the JD's top 3 gates.
4. Mirror the JD's own terminology where it is honest to do so — ATS and human
   screeners both keyword-match. Write "Kubernetes (K8s)" if the JD says
   Kubernetes and the user wrote K8s.
5. Drop anything irrelevant to this JD, however proud the user is of it.
6. Run `scripts/ats_check.py --jd <jd file>` on it. Fix every ERROR.

**Do not optimise the keyword-coverage number.** It is a checklist, not a
score: a resume that falsely claims every term in the JD scores 100% and then
fails the screen. A *worse* resume routinely outscores a better one by listing
tools the user has only read about. For each absent term, either the user
really has it and the resume undersells it (add real evidence), or they do not
(leave it absent - it is a stage-2 gap, not a wording gap).

Start from `assets/resume-template.md` if the user has no existing layout.

## ATS mechanics
- Single column. No tables, text boxes, headers/footers, or images carrying
  content. Two-column layouts and sidebars get mangled by many parsers.
- Standard section names: Experience, Education, Skills, Projects.
- Dates as `Mon YYYY - Mon YYYY`, consistent everywhere.
- Submit PDF unless the posting asks for .docx. Filename:
  `Firstname-Lastname-Role.pdf`.
- Never put content only in a graphic. Never white-text keyword-stuff — it is
  detected and it gets candidates blacklisted.

## Region conventions
- **US/Canada**: no photo, no DOB, no marital status, no full street address
  (city + state is enough). No "References available on request".
- **UK/EU**: no photo in the UK; photo and DOB are normal in parts of the EU.
- **Singapore / SEA**: nationality or PR status is commonly expected; expected
  salary is usually asked in the form, not the resume. A full NRIC/FIN number
  should never appear on a resume.
- **China (中文简历)**: 照片、出生年月、政治面貌、籍贯 are conventional for many
  domestic employers; keep an English version in parallel for MNCs. 应届生 put
  education first; 社招 put experience first.
- **Japan**: 履歴書 and 職務経歴書 are separate documents with fixed formats.

Ask which market before choosing conventions. Do not silently apply US norms to
a non-US application.

## Review checklist (run before every send)
- [ ] Every claim traceable to `profile.md`
- [ ] No `[METRIC?]` placeholders left
- [ ] Contact details correct, email professional
- [ ] The company and role named in the file are the right ones — this is the
      number-one bug in mass applications
- [ ] Consistent tense: past for past roles, present for current
- [ ] Consistent bullet punctuation
- [ ] Spellcheck run, including the company's own name
- [ ] One page unless justified
- [ ] Renders correctly as a PDF (check the PDF, not the markdown)
