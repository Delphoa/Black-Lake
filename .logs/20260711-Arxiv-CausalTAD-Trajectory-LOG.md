# Arxiv DEP Log: CausalTAD Trajectory

## Public-Safe Run Summary

- Deposit date: 2026-07-11
- Automation: Black Lake Arxiv DEP 1300
- Selected paper: CausalTAD: Causal Implicit Generative Model for Debiased Online Trajectory Anomaly Detection
- arXiv ID: 2412.18820v1
- DOI: 10.48550/arXiv.2412.18820
- Venue: 40th IEEE International Conference on Data Engineering (ICDE 2024), pages 4477-4490
- Authors: Wenbin Li; Di Yao; Chang Gong; Xiaokai Chu; Quanliang Jing; Xiaolei Zhou; Yuxuan Zhang; Yunxia Fan; Jingping Bi
- Source URLs: https://arxiv.org/abs/2412.18820 ; https://arxiv.org/html/2412.18820 ; https://arxiv.org/pdf/2412.18820 ; https://arxiv.org/e-print/2412.18820 ; https://github.com/LwbXc/CausalTAD
- Source-file policy: no `.source/` files deposited; public URLs and cache-derived review notes only.

## Random Selection Method

- Candidate enumeration: `rg --files -g "*.pdf"` against the local arXiv source archive.
- Paper unit rule: each unique PDF parent directory counted as one paper unit; nearby readme and metadata files were treated as supporting metadata.
- Candidate PDF count: 75,438.
- Candidate paper-unit count: 75,438.
- Random method: uniform PowerShell `Get-Random` selection of zero-based paper-unit index 68,925.
- Reselection count: 0.
- Exclusion count before acceptance: 0 duplicate or same-paper markers.

## Deduplication Validation

- Black-Lake scans: `.logs`, `.reports`, and `.lake-data` were scanned for arXiv ID `2412.18820`, DOI, normalized title, `CausalTAD`, and slug markers; no prior Arxiv DEP artifact was found.
- Automation memory: the two preceding run records were checked; neither referenced this paper.
- Black-Lake-Data checks: connected repository searches for the arXiv ID, exact title phrase, and `CausalTAD` returned no same-paper match.
- Same-paper 24-hour markers: none found for the arXiv ID, DOI, normalized title, or slug.
- Acceptance result: eligible on the first draw; no correction or backfill exception was used.

## Extraction and Review Summary

- Initial local unit: PDF and readme metadata were present.
- Extraction preflight: no usable local PDF text extractor was available.
- Network backfill: public arXiv HTML metadata and the TeX source package were fetched through the document-source-processing workflow.
- Final cache status: cached; HTML text and TeX source text present; PDF text absent.
- Primary evidence inspected: arXiv abstract/HTML, extracted TeX source including method, experiments, tables, limitations, and conclusion, plus the public author code repository README.
- Reproducibility boundary: no model training, dataset execution, table reproduction, or inference benchmarking was performed.

## Output Paths

- Log: `.logs/20260711-Arxiv-CausalTAD-Trajectory-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-CausalTAD-Trajectory-20260711/Report-Mark.md`
- DEP README: `.lake-data/DEP-E-20260711-CausalTAD Trajectory/README.md`
- DEP manuscript: `.lake-data/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md`

## Related DEP Entries

1. `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - overlap in road-network systems, online decision support, physical safety, and simulation-bound evidence.
2. `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` - overlap in debiasing, confounded evidence, distribution shift, and the need to distinguish robustness claims from controlled causal evidence.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260707-Tech Intel 1103/daily_research_findings_2026-07-07_1103.md` - overlap in structure-aware spatial evaluation, leakage control, and subgroup/distribution-shift generalization.

## Next-Review Questions

1. Can the ICDE result tables be reproduced from a pinned code commit after resolving the paper's Xi'an/Chengdu datasets versus the repository README's Xi'an/Porto description?
2. How does CausalTAD behave when road preference changes over time by hour, weekday, weather, congestion, or road closure rather than remaining static?
3. Would structure-aware spatial splits and real incident labels preserve the reported OOD advantage over VSAE, SAE, GM-VSAE, and DeepTEA?

## Challenges

1. Local PDF extraction was unavailable, so the review relied on public arXiv HTML and fetched TeX source for full-text evidence.
2. The public code repository's dataset description does not exactly match the paper's Xi'an and Chengdu experimental setup, limiting direct reproducibility claims.
3. The anomaly labels are synthetically generated detour and route-switch cases; no independent real-incident validation was available in the inspected evidence.
