# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`
- Public-safe run date: 2026-07-19
- Actor/tool: Codex
- Outcome: reviewed, validated, and prepared for submission
- Selected paper: *Multi-Agent VLMs Guided Self-Training with PNU Loss for Low-Resource Offensive Content Detection*
- Stable identifier: `arXiv:2511.13759v1`
- Canonical URL: https://arxiv.org/abs/2511.13759

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, then a uniform PowerShell `Get-Random` index over the raw unit list.
- PDF candidates: 75,778.
- Candidate paper units: 75,776.
- Selected one-based index: 25,453.
- Selected arXiv ID: `2511.13759`.
- Selected title: *Multi-Agent VLMs Guided Self-Training with PNU Loss for Low-Resource Offensive Content Detection*.
- Random selection succeeded on the first draw; randomness was not derived from machine, user, path, timezone, or timestamp data.

## Deduplication and Reselection

- Scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's private memory; and current Black-Lake-Data `.lake-data`, `.reports`, `.logs`, and `.staging` records.
- Keys: base/versioned arXiv ID, arXiv DOI, exact and normalized title, `MA-VLM`/`PNU` slug terms, artifact markers, and same-paper markers on or after the public-safe 24-hour cutoff date 2026-07-18.
- Prior used-paper match: none.
- Current-job match: none; this is the first accepted paper in the job-scoped set.
- Duplicate exclusions: 0.
- Reselections: 0.

## Source Integrity

- Initial classification: partial; a complete PDF was present but full-paper HTML was absent.
- Repair: one bounded direct-HTTPS attempt retrieved official arXiv full-paper HTML, metadata HTML, and the source package while preserving the existing valid PDF.
- PDF gate: 1,235,851 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML gate: 137,056 bytes, 37,347 body characters, `article` and LaTeXML document markers, 46 heading/section markers, and six paper-structure terms.
- Rejected-payload patterns: none.
- Unexpected partial files: 0.
- Extraction cache: `cached`; PDF, HTML, and source-package text extraction succeeded.
- Final source state: complete.
- Original PDF, HTML, metadata, source package, extracted text, and cache records were withheld locally.

## Public Outputs

- `.logs/20260719-Arxiv-MA-VLM-PNU-Moderation-LOG.md`
- `.reports/BL-Arxiv-MA-VLM-PNU-Moderation-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/ma_vlm_pnu_moderation_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` — model-specific VLM feedback loops and external-judge dependence.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` — soft targets, label-distribution mismatch, and uncertainty-aware rectification.
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` — conditional use of self-evaluation signals without allowing them to replace a primary task predicate.

## Submission Gate

- Allowlist: generated Markdown plus the required publication-index Markdown and dedup-index JSON only.
- `.source/` creation: prohibited and not performed.
- Source-document upload: none.
- Public sanitization: local paths, usernames, machine identifiers, workspace roots, timezone labels, and exact execution timestamps are withheld.
