# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P01`
- Public-safe date: 2026-08-10
- Paper: *Avatar V: Scaling Video-Reference Avatar Video Generation*
- Identifier: `arXiv:2606.13872`; DOI: `10.48550/arXiv.2606.13872`
- URL: https://arxiv.org/abs/2606.13872

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 46,098 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Avatar-V-Scaling-Video-Reference-Avatar-Video` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,979,116 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 31; sampled text inspection: true.
- Full-paper HTML: 239,715 bytes, 89,769 body characters, 230 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-Avatar-V-Scaling-Video-Reference-Avatar-Video-LOG.md`
- `.reports/BL-Arxiv-Avatar-V-Scaling-Video-Reference-Avatar-Video-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-Avatar V Scaling/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-Avatar V Scaling/avatar_v_scaling_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - AR-Drag Motion Control - DEP-E; overlap: video generation, motion alignment, autoregressive rollout.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave - DEP-E; overlap: video generation, geometric consistency, post-training.
3. `.lake-data/DEP-E/DEP-E-20260723-UnityShots Memory-Driven/unityshots_memory_driven_manuscript.md` - UnityShots Memory-Driven Multi-S - DEP-E; overlap: multi-shot video generation, temporal continuity, memory-guided generation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
