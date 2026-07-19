# 2026-07-19 - Arxiv DEP: Device Tuning MTL

- Actor/tool: Codex scheduled research workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/`.
- Action: Uniformly selected, source-repaired, verified, reviewed, synthesized, and prepared a DEP-E research deposit for *Device Tuning for Multi-Task Large Model*.
- Inputs: Verified complete arXiv PDF, approved full-paper HTML fallback, TeX/source archive, metadata, official workshop record, focused implementation search, successor publication context, and exactly three related Black Lake DEP entries. Original source documents and derivatives were withheld locally.
- Outputs: `.reports/BL-Arxiv-Device-Tuning-MTL-20260719/Report-Mark.md`, `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/README.md`, `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`, `.lake-data/DEP-E/.index/pubs-index.md`, and `.staging/arxiv-dep-dedup-index.json`.
- Outcome: Deposited directly to the Black Lake default branch and announced in `#black-lake-artifacts`.
- Primary artifact commit: [`557cf5d`](https://github.com/Delphoa/Black-Lake/commit/557cf5d31ed0032be314e19a7f58108a1b9a0eaa).
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784449256573979.
- Blockers: None.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` over the local archive.
- Candidate unit: Unique PDF parent directory.
- PDF candidates: 75,778.
- Candidate paper units: 75,776.
- Random method: PowerShell `Get-Random` selected one uniform zero-based index over all candidate units, followed by identity and dedup validation.
- Selected zero-based index: 74,319.
- Selected paper: *Device Tuning for Multi-Task Large Model*.
- Selected arXiv ID: `2302.10820v1` (base ID `2302.10820`).
- DOI: `10.48550/arXiv.2302.10820` (arXiv-issued).
- Exclusions: 0.
- Duplicate rejections and reselections: 0.
- Dedup scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`; automation memory; substantive Black-Lake-Data records; and active worktrees for a same-paper marker within 24 hours.
- Dedup result: No arXiv ID, DOI, normalized-title, slug, artifact, memory, companion-repository, or recent-worktree match. Generic Black-Lake-Data title-term hits were metadata-only and the exact ID/title searches were clear.

## Source Integrity Gate

- Initial classification: `partial`; the existing PDF was complete, but full-paper HTML was absent and the README contained only brief metadata.
- Existing PDF: 290,141 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Repair strategy: Public unauthenticated HTTPS with one active owner, a 32 MB target ceiling, a 16 MB partial ceiling, two-attempt cap, and no automatic restart.
- Repair result: The valid PDF was preserved. Metadata HTML, an approved ar5iv full-paper HTML fallback, and the official TeX/source package were collected locally.
- Full-paper HTML: 77,672 bytes; 18,911 body characters after script/style removal; document markers present; 30 heading/section markers; five paper-structure terms.
- TeX/source archive: 4,510,675 bytes; valid archive listing with 10 entries.
- Partial files: 0.
- Local records refreshed: README, attribution/provenance, preflight manifest, machine-readable summary, and verification report.
- Final classification: `complete`; review began only after the verification gate passed.

## Extraction Cache

- Preflight: `pypdf` available; preferred `pdftotext`, PyMuPDF, PyPDF2, and pdfminer backends unavailable.
- Initial cache lookup: Miss.
- Mode: `missing-only`; network disabled because the repaired paper unit was locally complete.
- PDF extraction: `pypdf`, status `ok`, 17,777 text bytes; fallback reason `pdftotext unavailable`.
- HTML extraction: `html-regex`, status `ok`, 19,172 text bytes.
- Source extraction: `tarfile`, status `ok`, 35,052 text bytes.
- Extraction command elapsed: 0.352 seconds.
- Final cache status: `cached`; the public cache summary passed the public-safety validator with zero findings.

## Evidence and Related DEP Validation

- Paper evidence: Full four-page PDF, full-paper HTML, complete TeX/source, equations, Figures 1-2, Tables 1-2, references, and metadata were inspected. All PDF pages were rendered for visual review; nonfatal font-substitution warnings did not obscure the figures or tables.
- External primary context: The official DAI 2023 accepted-paper list confirms the workshop appearance. A later CVPR Workshops paper by overlapping authors was inspected as related successor context, not as evidence for the selected paper.
- Code availability: The paper, arXiv record, workshop page, and focused GitHub searches exposed no author-linked implementation, configuration, checkpoint, or data manifest. Two global arXiv-ID code hits were third-party index/unrelated files.
- Core reported result: Table 1 reports 70.6% ImageNet-1k top-1 at 2.2M parameters, 0.8 percentage points above the best listed same-scale baseline.
- Principal evidence gap: The paper claims a multi-task, device-cloud, communication-efficient framework but reports no task inventory, multi-task metrics, gradient-normalization specification, training recipe, FLOPs, latency, memory, energy, communication bytes, or ablation.
- Related DEP 1: `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md` - same edge/cloud split boundary with explicit latency, bandwidth, and privacy measurements.
- Related DEP 2: `.lake-data/DEP-A/DEP-A-20260716-K Token Merging/2604.15153-whitepaper-review.md` - direct sequence/embedding compression neighbor with measured compression-quality tradeoffs.
- Related DEP 3: `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - compact vision neighbor separating FLOP reductions from realized device efficiency.

## Submission Gate

- Public-output allowlist: Exactly the generated `.logs`, `.reports`, DEP-E Markdown/README, publication index, and dedup JSON paths for this run.
- Source-upload denylist: PDFs, HTML, metadata pages, TeX/source archives, cache records, extracted source text, temporary renderings, local archive paths, and `.source/` directories.
- Public safety: No local absolute path, username, home directory, drive path, machine name, exact execution timestamp, or local timezone label is permitted.
- Source policy: Source files were retained locally and withheld. No `.source/` directory was created.
- Staged allowlist: Passed with exactly seven public artifact/index paths and zero source-file or derivative paths.
- Repository submission: Direct default-branch push succeeded and the remote head matched the primary artifact commit.
- Slack notification: Delivered after repository submission with public URLs and repository-relative paths only.

## Next-Review Questions

1. What exact task set, loss functions, gradient-normalization rule, shared parameters, and task-specific parameters define the claimed multi-task training procedure?
2. Does halving the token sequence reduce end-to-end device latency, peak memory, energy, and transmitted bytes at matched accuracy once pooling, serialization, networking, and cloud decoding are counted?
3. Can the Table 1 and Table 2 points be reproduced under one disclosed ImageNet recipe with matched data augmentation, resolution, pretraining, optimizer, epochs, and hardware?

## Challenges

1. The pooling operator, split point, compression payload, gradient-balancing method, and training configuration are underspecified, preventing faithful implementation.
2. The only reported experiment is ImageNet-1k classification, so the paper's multi-task and cross-domain generalization language is not empirically demonstrated.
3. Parameter counts and top-1 accuracy do not establish communication or systems efficiency, and no official code or checkpoint was found to fill the measurement gap.
