# 2026-07-20 - Arxiv AR-Drag Motion Control

- Actor/tool: Codex scheduled `Black Lake Arxiv DEP 1100` workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/`.
- Action: select one unused local arXiv paper unit uniformly at random, enforce the complete-source gate, review it source-first, connect it to exactly three verified DEP entries, and prepare public-safe research artifacts.
- Paper: *Real-Time Motion-Controllable Autoregressive Video Diffusion*.
- arXiv ID: `2510.08131v3`.
- Canonical URLs: https://arxiv.org/abs/2510.08131 and https://doi.org/10.48550/arXiv.2510.08131.
- Run date: 2026-07-20.
- Result: complete research deposit prepared for direct submission.

## Random Selection

- Method: `rg --files -g "*.pdf"` enumerated PDFs; each unique PDF-parent directory was one paper unit; normalized arXiv identifiers were derived from filenames, folder names, and nearby metadata; PowerShell `Get-Random` made one uniform zero-based draw over units remaining after identifier deduplication.
- PDF candidates: 75,778.
- Unique PDF-parent units: 75,776.
- Used normalized identifiers observed across Black Lake artifacts, automation memory, and relevant Black-Lake-Data records: 1,007.
- Units excluded by used identifier: 222.
- Identifier-incomplete units withheld: 0.
- Eligible units: 75,554.
- Selected zero-based eligible index: 14,671.
- Duplicate rejections and reselections: 0.
- Selected paper: `2510.08131v3`, *Real-Time Motion-Controllable Autoregressive Video Diffusion*.

## Deduplication and Recency Validation

- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; this automation's memory; and fetched `Black-Lake-Data` `.lake-data` and `.reports` records.
- Matching keys: base/versioned arXiv ID, arXiv-issued DOI, exact and normalized title, and `AR-Drag`/motion-control slug variants.
- Exact ID, DOI, title, or slug matches representing prior deposits: 0.
- Public-safe 24-hour cutoff date: 2026-07-19.
- Same-paper or same-unit markers on or after the cutoff: 0.
- Acceptance decision: eligible on the first draw.

## Source Integrity

- Initial state: `partial`; the existing PDF passed validation, but full-paper HTML was absent.
- Repair: review remained paused while a one-paper bounded repair reused the valid PDF and fetched official full-paper HTML, metadata HTML, and the arXiv source package. The repair used a 200 MB target ceiling, a 50 MB partial ceiling, one attempt per artifact, no credentials, and a dedicated local staging target.
- PDF verification: 34,931,055 bytes, `%PDF-` header present, trailing `%%EOF` present, SHA-256 unchanged from the initial unit.
- Full-paper HTML verification: 356,542 bytes, 88,798 body characters, a full-document marker, 63 heading/section markers, and eight configured paper-structure terms.
- Metadata HTML: 42,779 bytes; metadata only.
- Source package: 32,494,867 bytes with 34 readable entries.
- Partial files after repair: 0.
- Final source state: `complete`.
- Local records updated: paper README, attribution/provenance record, machine-readable CSV summary, and JSON verification report.
- Source locality: PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, renders, caches, and verification records remain in the local archive. No source file is included in this repository deposit.

## Evidence Review

- Inspected: complete v3 PDF, official full-paper HTML, metadata HTML, TeX/source package, 20-page PDF structure, equations, Algorithms 1-2, Listings 1-2, Tables 1-3, Figures 1-6, data appendix, limitations, ethics and reproducibility statements, arXiv metadata, official project page, ICLR 2026 poster record, and bounded release searches.
- Principal reported result: on a 206-clip author-curated benchmark, Table 1 reports AR-Drag at 0.44-second first-frame latency, FID 28.98, FVD 187.49, aesthetic quality 4.07, motion smoothness 0.9948, and motion consistency 4.37, the strongest displayed value in every column.
- Ablation boundary: removing RL worsens FID to 31.65 and motion consistency to 4.12; removing Self-Rollout worsens FID to 38.13 and FVD to 353.75. These are source-reported point estimates, not independent replications.
- Review boundary: no model training, video generation, benchmark, latency measurement, or human evaluation was rerun. The public project page exposes qualitative material but no official code repository was established; the paper says code is in supplementary materials.

## Exactly Three Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - shares few-step video-diffusion distillation and training-time auxiliary structure, but targets geometric consistency rather than interactive motion trajectories.
2. `.lake-data/DEP-A/DEP-A-20260716-PackForcing Video/2603.25730-whitepaper-review.md` - shares autoregressive video generation, bounded KV history, and exposure to long-horizon error accumulation; it makes cache governance explicit.
3. `.lake-data/DEP-A/DEP-A-20260717-ISPA Video Memory/2607.00712-whitepaper-review.md` - shares autoregressive-video KV-state constraints and tests 1.3B-to-14B models; it reframes historical context as instance-specific parameter state.

## Public Outputs

- `.logs/20260720-Arxiv-AR-Drag-Motion-Control-LOG.md`
- `.reports/BL-Arxiv-AR-Drag-Motion-Control-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Do AR-Drag's quality, motion, and 0.44-second first-frame results persist across multiple seeds, held-out datasets, resolutions, longer streams, and non-H20 hardware?
2. How much of the motion-consistency gain survives evaluation with trajectory trackers and human raters independent of the reward model used during training?
3. What failure rate appears under occlusion, abrupt direction changes, out-of-distribution subjects, and deliberately non-physical trajectories?

## Challenges

1. The selected archive unit lacked full-paper HTML and had to be repaired and reverified before synthesis could begin.
2. Motion Consistency is computed with the proposed reward model, so reward/evaluator dependence complicates an independent controllability claim.
3. The paper reports detailed settings and supplementary pseudocode but does not expose dataset provenance, seed variance, or a clearly established public implementation sufficient for end-to-end reproduction.

## Validation and Submission Controls

- Public-output policy: repository-relative paths and public URLs only; source documents and derived source caches are withheld locally.
- Required validation: manuscript schema and title/H1 contract, exact-three log and Synthesis Note counts, Python mock-up syntax, short-description length, publication-index ownership, final attribution blocks, URL coverage, public-safety leak scan, staged allowlist, and zero source files.
- Submission policy: stage only the five generated or updated Markdown files listed above; reject PDFs, HTML, archives, caches, extracted source text, rendered images, or any other source material.
- Blockers: none at drafting time.
