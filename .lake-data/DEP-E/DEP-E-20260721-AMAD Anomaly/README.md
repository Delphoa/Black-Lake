# DEP-E-20260721-AMAD Anomaly

#anomaly-detection #multiscale-learning #categorical-data #adversarial-autoencoder #time-series #industrial-monitoring #research-review

Public-safe DEP-E context: this entry preserves a source-grounded review of arXiv `1907.06582v1`, *AMAD: Adversarial Multiscale Anomaly Detection on High-Dimensional and Time-Evolving Categorical Data*. The review covers hierarchical representations, adversarial reconstruction, instance- and block-level scoring, reported experiments, implementation evidence, limitations, and concrete bridges to exactly three existing DEP entries. All original and repaired source documents remain in the private local archive.

## Contents

- `README.md` - DEP inventory, public context, summary, relevance, and attribution.
- `amad_anomaly_manuscript.md` - schema-complete manuscript research artifact with evidence ledger, critical review, implementation paths, and replication notes.

No `.source/` directory exists. No PDF, HTML, metadata page, source package, dataset, extracted text, render, cache, or private verification file is deposited.

## Summary of Items

### `README.md`

Defines the DEP-E package, identifies the two generated Markdown artifacts, records the source-withholding boundary, and provides a final attribution map for every public research and repository source used.

### `amad_anomaly_manuscript.md`

Reviews AMAD's four-level representation path from categorical feature IDs through attributes, instances, and sequential blocks. It traces the paper's attention, autoencoder, RNN, discriminator, and compound-loss design; transcribes the dataset and result tables; distinguishes author claims from reviewer interpretation; inspects the official code at a pinned commit; and proposes bounded implementations and validation exercises.

## Insights and Relevance

AMAD's lasting design insight is not merely the use of an adversarial autoencoder. It is the decision to score the same event stream at two resolutions while allowing block state to influence instance representation. That creates a concrete bridge between point anomalies and collective anomalies. The paper's evidence is useful but narrower than its deployment framing: all evaluation anomalies are constructed, test sets are balanced, thresholds appear selected from the test scores, the industrial baseline pipeline uses a different representation, and the released code does not cleanly match the paper. The three related DEP entries sharpen those boundaries through causal/OOD trajectory scoring, field-oriented fault detection, and scarce-label nonstationary diagnosis.

## Attribution Block

- Source URL: https://arxiv.org/abs/1907.06582
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Canonical arXiv metadata, authorship, submission date, abstract, and stable identifier.
- Source URL: https://arxiv.org/pdf/1907.06582
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Canonical paper PDF; inspected locally and withheld from the repository.
- Source URL: https://ar5iv.labs.arxiv.org/html/1907.06582
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Approved full-paper HTML fallback used after the official arXiv HTML endpoint was unavailable; local copy withheld.
- Source URL: https://arxiv.org/e-print/1907.06582
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Official TeX/source endpoint; local source package inspected and withheld.
- Source URL: https://doi.org/10.48550/arXiv.1907.06582
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: arXiv-issued DOI.
- Source URL: https://doi.org/10.1145/3326937.3341256
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Published ACM DOI exposed by the paper.
- Source URL: https://dlp-kdd.github.io/dlp-kdd2019/accept.html
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Official DLP-KDD 2019 accepted-paper listing.
- Source URL: https://dlp-kdd.github.io/dlp-kdd2019/assets/pdf/a7-gao.pdf
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Workshop-hosted paper PDF used as public corroboration.
- Source URL: https://github.com/pkumc/AMAD
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Author-attributed official implementation repository; inspected but not executed.
- Source URL: https://github.com/pkumc/AMAD/commit/0391c97dba2823608006180957f9330c5ec06791
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Sole observed repository commit used to pin the implementation inspection.
- Source URL: https://tianchi.aliyun.com/dataset/27665
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Public dataset record named by the paper and code documentation; dataset contents were not downloaded.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Related DEP bridge on online generative anomaly detection, OOD shift, and synthetic anomaly labels.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Related DEP bridge on industrial fault detection, field shift, and deployment constraints.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Related DEP bridge; finding 10 covers Kalman prototypical few-shot fault detection under nonstationarity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Live repository submission and attribution authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md`; `amad_anomaly_manuscript.md`
  - Notes: Live related-repository layout authority read before using its DEP entry.
- Withheld local source files: `1907.06582.pdf`, `1907.06582.html`, `1907.06582.abs.html`, and `1907.06582.source.tar`.
  - Applies to: `amad_anomaly_manuscript.md`
  - Notes: Inspected as private evidence; paths withheld, no `.source/` directory created, and no source file uploaded.
