# Stage 2 — Background building + practice plan

Every item must trace to a specific gap in `gap-analysis.md`. If it doesn't,
cut it. Generic advice ("contribute to open source", "build a portfolio") is a
failure of this stage.

## Priority order
1. **Wording gaps** — free, same-day, highest ROI. Handle in stage 3.
2. **Portfolio evidence** — one substantial, verifiable artifact beats five
   tutorials. It must be public, runnable/readable, and describable in 2 minutes.
3. **Domain credibility** — a writeup, a talk, a paper reproduction, a Kaggle
   placement, a public dataset analysis in the target industry.
4. **Certifications** — only where the market actually gates on them (cloud,
   security, some finance/healthcare roles). Otherwise low ROI.
5. **Network** — 3–5 warm contacts per target company beats 100 cold applies.
   Referral hit rates are typically an order of magnitude better.

## Project selection rubric
Score candidates 1–5 on: closes a listed gap; verifiable by a stranger;
finishable in the available weeks; interesting enough to actually finish; hard
to fake. Pick the highest total, not the most impressive-sounding.

## Practice plan
Calibrate to the target; don't default to LeetCode.
- **Big-tech SWE**: algorithms heavy. ~150 curated problems chosen by pattern,
  not volume: arrays/hashing, two pointers, sliding window, stack, binary
  search, linked list, trees, tries, heap, backtracking, graphs, 1-D and 2-D DP,
  intervals, greedy, bit manipulation. Add system design for mid-level and up.
- **Data/ML**: SQL drills, applied ML cases, stats/experimentation, ML system
  design, one end-to-end reproducible project.
- **Data engineering**: SQL, pipeline and data modelling design, one streaming
  project.
- **PM / analyst / non-engineering**: case frameworks, metrics trees,
  storytelling. Algorithm drilling is wasted time here.

Practice rules that matter more than the problem list:
- Separate timed and untimed sessions. Interviews are timed.
- Spaced repetition: re-solve anything that needed a hint at +3 and +10 days.
- Talk out loud from week one. Silent solving does not transfer.
- Track first-attempt pass rate per pattern; drill the worst pattern, not the
  next problem in the list.

## Output — `workspace/plan.md`
```markdown
# Plan — <start date> to <end date>
Available: <N> h/week

## Week 1 (<absolute dates>)
- [ ] <action> — closes gap: <gap> — <hours>h — done when: <observable check>

## Weekly cadence
Applications: N/week · Practice: N h · Project: N h · Outreach: N contacts

## Checkpoints
Week 2 / 4 / 8: what must be true, and what to change if it isn't
```
Absolute dates, never "week 1" alone. Every task needs a done-when condition.
