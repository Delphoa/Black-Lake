# 2026-07-21 - Arxiv AMAD Anomaly Detection

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 0900` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260721-AMAD Anomaly/`.
- Action: randomly select one unused local arXiv paper unit, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *AMAD: Adversarial Multiscale Anomaly Detection on High-Dimensional and Time-Evolving Categorical Data*.
- arXiv ID: `1907.06582v1`.
- Published DOI: https://doi.org/10.1145/3326937.3341256.
- Canonical arXiv URLs: https://arxiv.org/abs/1907.06582 and https://doi.org/10.48550/arXiv.1907.06582.
- Run date: 2026-07-21; exact execution timestamp withheld.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, used-ID exclusion, then a uniform PowerShell `Get-Random` draw over eligible units.
- PDF candidates: 75,779.
- Unique PDF-parent units: 75,776.
- Used arXiv base IDs observed across the dedup corpus: 1,055.
- Units excluded by used arXiv ID: 248.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,343.
- Selected zero-based eligible index: 34,605.
- Duplicate rejections/reselections: 0.
- Selected paper: `1907.06582v1`, *AMAD: Adversarial Multiscale Anomaly Detection on High-Dimensional and Time-Evolving Categorical Data*.
- Randomness note: an initial enumeration attempt produced no usable selection record and was discarded before any paper was accepted; the reported linear-time eligible-unit draw is the sole accepted selection.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `.logs`, `.reports`, `.lake-data`, and `.staging` from fetched default-branch state.
- Matching keys: arXiv ID, arXiv DOI, published DOI, exact title, normalized title, `AMAD` title token, and `AMAD-Anomaly`-style slug variants.
- Exact ID/title/slug matches: 0.
- Public-safe 24-hour cutoff date: 2026-07-20.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible; no duplicate or recency marker required reselection.

## Source Integrity

- Initial state: `partial`; the existing PDF was valid, but full-paper HTML was absent.
- Repair: preserved the valid PDF and used a fresh one-paper repair staging target with one bounded request per companion artifact, a 200 MiB total ceiling, a 50 MiB partial ceiling, and a 180-second request timeout. Official arXiv full-paper HTML was unavailable, so the approved ar5iv full-paper fallback was used.
- PDF verification: 715,086 bytes, `%PDF-` header present, trailing `%%EOF` present. The repair-staging PDF hash matched the existing PDF hash, so the original file was retained.
- Full-paper HTML verification: 437,327 bytes, 47,873 body characters, a full-document marker, 71 heading/section markers, and seven paper-structure terms.
- Metadata HTML: 43,293 bytes; retained as metadata only.
- Source package: downloaded, 305,433 bytes, 14 archive entries.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance note, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, HTML, metadata, source package, extracted text, rendered pages, repair staging, and verification records remain in the private local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: complete eight-page PDF, approved full-paper HTML, arXiv metadata HTML, TeX/source package, canonical arXiv record, DLP-KDD accepted-paper page and workshop PDF, published DOI, official AMAD code repository at commit `0391c97dba2823608006180957f9330c5ec06791`, Tianchi dataset record, and three related DEP artifacts.
- Visual review: all eight PDF pages were rendered and inspected, including the architecture diagram, dataset table, instance/block result tables, ablation tables, block-size plot, and appendix.
- Technical scope: hierarchical feature/attribute/instance/block representations; self and relative attention; autoencoder and RNN generators; instance/block discriminators; compound anomaly scores; three datasets; seven baselines; ten-run comparisons; component ablations; and block-size sensitivity.
- Reproduction boundary: code and experiments were not run. The code release was inspected for implementation evidence only.
- Implementation caveat: the single-commit TensorFlow 1 code lacks an environment lock and tests, includes author-local paths, and exposes differences from the paper such as Adam optimizers in `model.py`, an example block size of 20, and additive instance representations where the paper specifies concatenation. Exact table reproduction is therefore unverified.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` - shares online generative anomaly scoring, temporal sequence modeling, normality assumptions, OOD risk, and synthetic-anomaly evaluation.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - links industrial fault monitoring to resource constraints, field shift, rare failures, and the gap between benchmark accuracy and deployment readiness.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260627-Tech Intel 1103/daily_research_findings_2026-06-27_1103.md` - its Kalman prototypical fault-detection finding connects scarce labels, nonstationary dynamics, state estimation, and infrastructure monitoring.

## Public Outputs

- `.logs/20260721-Arxiv-AMAD-Anomaly-LOG.md`
- `.reports/BL-Arxiv-AMAD-Anomaly-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-AMAD Anomaly/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-AMAD Anomaly/amad_anomaly_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; source documents withheld locally.
- Required validation: manuscript schema/headings, exactly three exercise paths, exact-three Report-Mark synthesis counts, title length/equality, DEP inventory, final attribution blocks, publication-index ownership, URL coverage, public-safe leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated/updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, repair artifacts, or other local source material.
- Blockers: none at drafting time.
