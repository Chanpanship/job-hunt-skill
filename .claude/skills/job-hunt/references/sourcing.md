# Stage 4 — Sourcing openings

## Channels, in descending yield
1. **Referrals** — the user's own network. Always mine this first.
2. **Company career pages / ATS** — Greenhouse, Lever, Ashby, Workday,
   SmartRecruiters. Freshest listings, often days before the aggregators.
   Board URLs are predictable: `boards.greenhouse.io/<company>`,
   `jobs.lever.co/<company>`.
3. **Role-specific boards** — academic/research listings, quant boards, design
   boards, the YC job board for startups.
4. **Aggregators** — LinkedIn Jobs, Indeed, Glassdoor, Google Jobs.
5. **Regional**
   - China: BOSS直聘, 拉勾, 猎聘, 智联招聘, 前程无忧, 牛客 (校招), 实习僧
   - Singapore: MyCareersFuture, JobStreet, NodeFlair, Glints
   - SEA / ANZ: Seek, JobsDB
   - Japan: Wantedly, Bizreach, LinkedIn
   - Europe: Otta, Welcome to the Jungle, StepStone, Xing (DE)
6. **Feeds** — many boards expose RSS or an official API. Prefer those.

## How to fetch
- Prefer WebSearch / WebFetch, official APIs, and RSS.
- Use browser tools only for pages that genuinely need JS rendering, at human
  pace. Never solve a CAPTCHA. Never log in or create an account for the user.
  If a board is login-gated, hand the search string to the user instead.
- Respect robots.txt and terms of service. If a site prohibits automated access,
  say so and switch channel.

## Recording
Use `scripts/jobs_db.py add` — it dedupes on company + normalized title.
Columns: `id, date_found, company, title, location, remote, seniority, url,
source, salary, deadline, visa_sponsor, fit_score, status, notes`.

## Fit scoring (0-100)
| Dimension | Weight |
|---|---|
| Must-have skill overlap | 30 |
| Seniority match | 20 |
| Location / work-authorization feasibility | 20 |
| Comp within range | 15 |
| Company or domain interest | 10 |
| Referral path exists | 5 |

Bands: 80+ apply fully tailored · 60-79 apply with a light tailor · 40-59 only
if the pipeline is thin · under 40 skip. State the band when presenting jobs so
the user can prioritize.

## Red flags — surface them, do not filter silently
Upfront fees or training deposits; requests for bank details or full ID numbers
before an offer; recruiting conducted entirely over WhatsApp or Telegram; no
verifiable company web presence; comp far above market for the seniority;
a posting reposted continuously for months. Record in `notes` and mention it
when the user reviews the batch.
