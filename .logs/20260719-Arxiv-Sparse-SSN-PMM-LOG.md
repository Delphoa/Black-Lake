# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P03`
- Public-safe run date: 2026-07-19
- Actor/tool: Codex
- Outcome: reviewed, validated, and prepared for submission
- Selected paper: *A sparse semismooth Newton based proximal majorization-minimization algorithm for nonconvex square-root-loss regression problems*
- Stable identifier: `arXiv:1903.11460v3`
- Canonical URL: https://arxiv.org/abs/1903.11460

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, then a uniform PowerShell `Get-Random` index over the raw unit list.
- PDF candidates: 75,778.
- Candidate paper units: 75,776.
- Selected one-based index: 47,418.
- Selected arXiv ID: `1903.11460`.
- Random selection succeeded on the first draw; randomness was not derived from machine, user, path, timezone, or timestamp data.

## Deduplication and Reselection

- Scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's private memory; current Black-Lake-Data relevant records; and the current-job selected-paper set.
- Keys: base/versioned arXiv ID, arXiv DOI, exact and normalized title, `Sparse-SSN-PMM` terms, artifact markers, and same-paper markers on or after the public-safe 24-hour cutoff date 2026-07-18.
- Prior used-paper match: none.
- Current-job match: none; the paper is distinct from P01 and P02.
- Duplicate exclusions: 0.
- Reselections: 0.

## Source Integrity

- Initial classification: partial; a complete PDF was present but full-paper HTML was absent.
- Repair: official arXiv HTML returned 404; one bounded attempt retrieved an approved ar5iv full-paper fallback, official metadata HTML, and the source package while preserving the existing PDF.
- PDF gate: 379,514 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML gate: 3,784,125 bytes, 178,602 body characters, document markers present, 68 heading/section markers, and seven paper-structure terms.
- Rejected-payload patterns: none.
- Unexpected partial files: 0.
- Extraction cache: `cached`; PDF, HTML, and source-package text extraction succeeded.
- Final source state: complete.
- Original PDF, HTML, metadata, source package, extracted text, and cache records were withheld locally.

## Public Outputs

- `.logs/20260719-Arxiv-Sparse-SSN-PMM-LOG.md`
- `.reports/BL-Arxiv-Sparse-SSN-PMM-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/sparse_ssn_pmm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` - SCAD/MCP sparse regression, local-solution theory, and optimizer governance.
2. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` - proximal regularization geometry, exact convergence, and approximate-solver error floors.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - low-rank-plus-sparse decomposition, ADMM inner optimization, and the boundary between convex and heuristic stages.

## Submission Gate

- Allowlist: generated Markdown plus the required publication-index Markdown and dedup-index JSON only.
- `.source/` creation: prohibited and not performed.
- Source-document upload: none.
- Public sanitization: local paths, usernames, machine identifiers, workspace roots, timezone labels, and exact execution timestamps are withheld.
