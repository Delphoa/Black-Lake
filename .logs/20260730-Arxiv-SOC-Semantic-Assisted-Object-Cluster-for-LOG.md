# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260730-2FDDC232`
- Deployment item ID: `BLAD-2200-20260730-2FDDC232-P10`
- Public-safe date: 2026-07-30
- Paper: *SOC: Semantic-Assisted Object Cluster for Referring Video Object Segmentation*
- Identifier: `arXiv:2305.17011`; DOI: `10.48550/arXiv.2305.17011`
- URL: https://arxiv.org/abs/2305.17011

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 40,440 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `SOC-Semantic-Assisted-Object-Cluster-for` slug; the 24-hour marker cutoff was 2026-07-29.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,459,492 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 517,283 bytes, 54,157 body characters, 97 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260730-Arxiv-SOC-Semantic-Assisted-Object-Cluster-for-LOG.md`
- `.reports/BL-Arxiv-SOC-Semantic-Assisted-Object-Cluster-for-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-SOC Semantic-Assisted/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-SOC Semantic-Assisted/soc_semantic_assisted_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - AR-Drag Motion Control - DEP-E; overlap: video, alignment.
2. `.lake-data/DEP-E/DEP-E-20260726-MoE3D Mixture of Experts/moe3d_mixture_of_experts_manuscript.md` - MoE3D Mixture of Experts - DEP-E; overlap: multi-modal, understanding.
3. `.lake-data/DEP-E/DEP-E-20260728-Multi-step Problem/multi_step_problem_manuscript.md` - Multi-step Problem - DEP-E; overlap: supervision, problem.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
