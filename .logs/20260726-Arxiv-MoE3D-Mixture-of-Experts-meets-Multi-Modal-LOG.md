# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P04`
- Public-safe date: 2026-07-26
- Paper: *MoE3D: Mixture of Experts meets Multi-Modal 3D Understanding*
- Identifier: `arXiv:2511.22103`; DOI: `10.48550/arXiv.2511.22103`
- URL: https://arxiv.org/abs/2511.22103

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,526 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MoE3D-Mixture-of-Experts-meets-Multi-Modal` slug; the 24-hour marker cutoff was 2026-07-25.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 24,735,348 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 255,561 bytes, 55,285 body characters, 53 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260726-Arxiv-MoE3D-Mixture-of-Experts-meets-Multi-Modal-LOG.md`
- `.reports/BL-Arxiv-MoE3D-Mixture-of-Experts-meets-Multi-Modal-20260726/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260726-MoE3D Mixture of Experts/README.md`
- `.lake-data/DEP-E/DEP-E-20260726-MoE3D Mixture of Experts/moe3d_mixture_of_experts_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - Spiking Pose Tracking - DEP-E; overlap: human, transformer, pose.
2. `.lake-data/DEP-E/DEP-E-20260726-MoGIC Boosting Motion/mogic_boosting_motion_manuscript.md` - MoGIC Boosting Motion - DEP-E; overlap: understanding, motion, visual.
3. `.lake-data/DEP-E/DEP-E-20260725-CLCI-Net Cross-Level/clci_net_cross_level_manuscript.md` - CLCI-Net Cross-Level - DEP-E; overlap: fusion, networks.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
