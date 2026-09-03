# Stage 5 — Applying at volume

## The boundary
**Filling is allowed. Submitting is not.**

May do: open the posting, upload the prepared resume, fill the ordinary fields
(name, contact, education, work history, links), draft the free-text answers,
and save a draft where the site supports it.

Must not do: click the final Submit / Apply / Send control; answer a legal
attestation (work authorization or visa status, criminal history, prior
employment at this company, protected-characteristic self-ID) even when
`profile.md` seems to contain the answer; create an account; log in or enter
credentials; enter payment details or a full government ID number; solve a
CAPTCHA.

Leave the form filled and the attestations blank, list exactly what is
outstanding, and let the user review and press Submit. State this once when the
stage starts.

Why the line sits here rather than at "no browser use": an application cannot be
withdrawn, most boards' terms ban automated submission and enforce it with
account bans, bulk automation is how wrong-company resumes get sent, and a
wrong answer on an attestation can void an offer after signing. None of that is
solved by the agent being more careful.

This is a policy, not a capability limit. Whether a given agent honours it is up
to that agent.

## Batch workflow
Work in batches of 5-10, highest fit_score first. For each job produce
`workspace/outreach/<company>-<role>/`:

- `resume.pdf` plus its `.md` source
- `cover-letter.md` — only where it gets read (startups, EU, academia, and any
  posting that asks for one). Skip it for large-ATS applications that do not.
- `answers.md` — drafts for the posting's screening questions, with anything
  only the user can answer marked `[USER: ...]`
- `submit.md` — the URL, what to upload, field-by-field values, and attention
  points (deadline, referral contact, portfolio link)

Then present a compact table: company · role · fit · deadline · what is ready ·
what needs the user. The user submits and reports the outcome.

## Volume that actually works
- 10-20 well-tailored applications per week beats 100 generic ones. Response
  rates on untailored mass applications are typically low single digits.
- Cap one application per company per role family per 6 weeks. Faster reads as
  spam.
- Apply within 72 hours of a posting going live where possible; many roles fill
  from the first week's pool.

## Cover letter
Three paragraphs, under 250 words.
1. The specific role, and the single strongest reason the user fits — one
   concrete piece of evidence, not adjectives.
2. The most relevant accomplishment with its number, connected to something real
   about *this* company's problem.
3. Logistics: availability, work authorization if it is an advantage, one close.

Never: "I am writing to express my interest", "passionate about", "dynamic team
player", or a restatement of the resume. If the letter would work for any
company with the name swapped, it is not finished.

## Referral and cold outreach drafts
Under 120 words: who you are, the one relevant thing, the specific role and its
req ID, one small ask ("would you be open to referring me / a 15-minute chat?").
Attach nothing unrequested. Claude drafts; the user sends.

## Tracking and the weekly review
Log every submission: `scripts/jobs_db.py log <job_id> --status applied`.
Statuses: `found -> applied -> screening -> interview -> offer -> rejected ->
ghosted` (ghosted = no reply after 21 days).

Each week compute applications sent, response rate overall and by source,
response rate by resume version, and median days to first response.

Decision rules:
- Under 5% response after 30 applications → the resume or the targeting is
  wrong. Go back to stage 3, then stage 1. Do not just send more.
- Screens but no onsites → interview performance. Return to the stage-2 plan.
- Onsites but no offers → depth and closing. Run mock loops.
