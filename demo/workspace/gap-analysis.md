# Gap analysis - Machine Learning Engineer II, Singapore (DEMO)
Based on 1 posting in this demo (the real thing uses 5-10):
demo/workspace/jobs/jd/grabbish-mle.txt

## Requirement table
| Requirement | User status | Evidence in profile | Gap class |
|---|---|---|---|
| 3+ yrs production ML | partial | 4 yrs, but titled Analyst; 1 model in prod | wording |
| Strong Python + SQL | have | daily, ~40-table reporting layer | none |
| Time series forecasting at scale | have | Prophet, 31% -> 22% MAPE, 3 categories | wording |
| Airflow / orchestrator | have | productionised ETL, 6h/wk -> 15min | wording |
| A/B testing | have | 1.4M-user test, +2.1% conversion | wording |
| Docker / K8s / CI-CD | missing | "exposure only" | cheap |
| Spark / distributed | missing | none | cheap |
| MLflow / tracking | missing | "exposure only" | cheap |
| PyTorch (nice) | partial | FYP LSTM autoencoder, not production | wording |
| E-commerce domain (nice) | have | current employer is a marketplace | none |
| CS/Eng degree | have | BEng EE, NTU | none |

## Verdict
- **Apply now:** forecasting-heavy MLE roles at marketplaces. The Prophet +
  Airflow + A/B combination is exactly this JD's core, and it is currently
  buried under an "Analyst" title. That is a wording gap and it is free to fix.
- **The real blocker is the deployment stack**, not the modelling: Docker, K8s,
  CI/CD, Spark, MLflow. All five are absent, and they appear as hard
  requirements. Class `cheap` only because one containerised, CI-tested,
  MLflow-tracked project closes all of them credibly in ~4 weeks.
- **Title risk:** "Data Analyst" gets screened out of MLE pipelines by keyword
  before a human reads the bullets. Cannot be renamed (never falsify a title),
  so it must be offset by a Projects section that reads as engineering.
- **Do not** claim K8s/Spark/MLflow to raise keyword coverage. Note that in this
  demo the dishonest v1 resume scores *higher* on coverage (58%) than the honest
  tailored v2 (42%). Coverage is a checklist, not a score.
