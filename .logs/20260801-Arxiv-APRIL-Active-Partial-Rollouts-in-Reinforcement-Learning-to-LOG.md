# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260801-A1ED7FC9`
- Deployment item ID: `BLAD-2200-20260801-A1ED7FC9-P10`
- Public-safe date: 2026-08-01
- Paper: *APRIL: Active Partial Rollouts in Reinforcement Learning to Tame Long-tail Generation*
- Identifier: `arXiv:2509.18521`; DOI: `10.48550/arXiv.2509.18521`
- URL: https://arxiv.org/abs/2509.18521

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 37,526 on draw 1 for this slot.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `APRIL-Active-Partial-Rollouts-in-Reinforcement-Learning-to` slug; the 24-hour marker cutoff was 2026-07-31.
- Duplicate exclusions: 0; source-gate exclusions: 0; metadata exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 17,579,105 bytes with valid `%PDF-` header and trailing `%%EOF`; pages: 24; extracted text characters: 75,469.
- Full-paper HTML: 246,993 bytes, 80,441 body characters, 105 heading/section markers, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260801-Arxiv-APRIL-Active-Partial-Rollouts-in-Reinforcement-Learning-to-LOG.md`
- `.reports/BL-Arxiv-APRIL-Active-Partial-Rollouts-in-Reinforcement-Learn-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-APRIL Active Partial/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-APRIL Active Partial/april_active_partial_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - AR-Drag Motion Control - DEP-E; concrete overlap: generation, learning, partial, rollout.
2. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; concrete overlap: learning, long-tail, rollout, rollouts.
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` - RLMF Uncertainty - DEP-E; concrete overlap: active, learning, reinforcement.

Only generated Markdown and the required dedup JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
