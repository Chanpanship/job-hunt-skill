#!/usr/bin/env python3
"""Job pipeline store: two CSVs under workspace/jobs/.

  jobs_db.py add --company X --title Y [--url ... --location ... --source ...
                 --salary ... --deadline YYYY-MM-DD --seniority ... --remote ...
                 --visa-sponsor yes|no|unknown --fit N --notes ...]
  jobs_db.py log <job_id> --status applied [--notes ...] [--resume <path>]
  jobs_db.py list [--status S] [--min-fit N] [--company X]
  jobs_db.py stats

Dedupes on company + normalized title. Idempotent: re-adding an existing job
prints its id and changes nothing.
"""
import argparse, csv, os, re, sys
from datetime import date

ROOT = os.environ.get("JOBHUNT_WORKSPACE", "workspace")
JOBS_DIR = os.path.join(ROOT, "jobs")
JOBS = os.path.join(JOBS_DIR, "jobs.csv")
APPS = os.path.join(JOBS_DIR, "applications.csv")

JOB_COLS = ["id", "date_found", "company", "title", "location", "remote",
            "seniority", "url", "source", "salary", "deadline", "visa_sponsor",
            "fit_score", "status", "notes"]
APP_COLS = ["date", "job_id", "company", "title", "status", "resume_version",
            "notes"]
STATUSES = ["found", "applied", "screening", "interview", "offer", "rejected",
            "ghosted", "withdrawn"]


def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[\(\[].*?[\)\]]", " ", s)          # drop parentheticals
    s = re.sub(r"\b(senior|sr|junior|jr|staff|lead|principal|i{1,3}|iv|[0-9])\b",
               " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def read(path, cols):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [{c: r.get(c, "") for c in cols} for r in csv.DictReader(f)]


def write(path, cols, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def cmd_add(a):
    rows = read(JOBS, JOB_COLS)
    key = (norm(a.company), norm(a.title))
    for r in rows:
        if (norm(r["company"]), norm(r["title"])) == key:
            print(f"duplicate: {r['id']}  {r['company']} / {r['title']}")
            return 0
    new_id = f"J{max([int(r['id'][1:]) for r in rows] or [0]) + 1:04d}"
    rows.append({
        "id": new_id, "date_found": a.date or date.today().isoformat(),
        "company": a.company, "title": a.title, "location": a.location or "",
        "remote": a.remote or "", "seniority": a.seniority or "",
        "url": a.url or "", "source": a.source or "", "salary": a.salary or "",
        "deadline": a.deadline or "", "visa_sponsor": a.visa_sponsor or "unknown",
        "fit_score": str(a.fit) if a.fit is not None else "",
        "status": "found", "notes": a.notes or "",
    })
    write(JOBS, JOB_COLS, rows)
    print(f"added {new_id}  {a.company} / {a.title}")
    return 0


def cmd_log(a):
    if a.status not in STATUSES:
        sys.exit(f"status must be one of: {', '.join(STATUSES)}")
    rows = read(JOBS, JOB_COLS)
    hit = next((r for r in rows if r["id"] == a.job_id), None)
    if not hit:
        sys.exit(f"no such job id: {a.job_id}")
    hit["status"] = a.status
    write(JOBS, JOB_COLS, rows)
    apps = read(APPS, APP_COLS)
    apps.append({"date": a.date or date.today().isoformat(), "job_id": a.job_id,
                 "company": hit["company"], "title": hit["title"],
                 "status": a.status, "resume_version": a.resume or "",
                 "notes": a.notes or ""})
    write(APPS, APP_COLS, apps)
    print(f"{a.job_id} -> {a.status}")
    return 0


def cmd_list(a):
    rows = read(JOBS, JOB_COLS)
    if a.status:
        rows = [r for r in rows if r["status"] == a.status]
    if a.company:
        rows = [r for r in rows if norm(a.company) in norm(r["company"])]
    if a.min_fit is not None:
        rows = [r for r in rows
                if r["fit_score"].isdigit() and int(r["fit_score"]) >= a.min_fit]
    rows.sort(key=lambda r: -int(r["fit_score"] or 0))
    if not rows:
        print("(no matching jobs)")
        return 0
    print(f"{'id':6}{'fit':5}{'status':11}{'company':24}{'title':38}deadline")
    for r in rows:
        print(f"{r['id']:6}{r['fit_score'] or '-':5}{r['status']:11}"
              f"{r['company'][:23]:24}{r['title'][:37]:38}{r['deadline']}")
    return 0


def cmd_stats(_a):
    rows = read(JOBS, JOB_COLS)
    if not rows:
        print("(pipeline empty)")
        return 0
    by_status, by_source = {}, {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        s = r["source"] or "unknown"
        d = by_source.setdefault(s, [0, 0])
        d[0] += 1
        if r["status"] not in ("found", "applied", "ghosted"):
            d[1] += 1
    applied = sum(v for k, v in by_status.items() if k != "found")
    responded = sum(v for k, v in by_status.items()
                    if k in ("screening", "interview", "offer"))
    print(f"total tracked: {len(rows)}   applied: {applied}")
    for k in STATUSES:
        if by_status.get(k):
            print(f"  {k:11}{by_status[k]}")
    if applied:
        print(f"response rate: {responded / applied:.1%}")
        if applied >= 30 and responded / applied < 0.05:
            print("  ! under 5% after 30+ applications -> fix resume/targeting, "
                  "not volume (see references/mass-apply.md)")
    print("\nby source (applied / responded):")
    for s, (n, resp) in sorted(by_source.items(), key=lambda x: -x[1][0]):
        print(f"  {s:20}{n:4}{resp:6}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("--company", required=True)
    a.add_argument("--title", required=True)
    for o in ("url", "location", "source", "salary", "deadline", "seniority",
              "remote", "notes", "date", "visa-sponsor"):
        a.add_argument(f"--{o}")
    a.add_argument("--fit", type=int)
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("log")
    l.add_argument("job_id")
    l.add_argument("--status", required=True)
    l.add_argument("--notes")
    l.add_argument("--resume")
    l.add_argument("--date")
    l.set_defaults(func=cmd_log)

    s = sub.add_parser("list")
    s.add_argument("--status")
    s.add_argument("--company")
    s.add_argument("--min-fit", type=int)
    s.set_defaults(func=cmd_list)

    sub.add_parser("stats").set_defaults(func=cmd_stats)

    args = p.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
