# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260801-A1ED7FC9`
- Deployment item ID: `BLAD-2200-20260801-A1ED7FC9-P02`
- Public-safe date: 2026-08-01
- Paper: *Controlling Decision Drift in Multimodal Sentiment Analysis with Missing Modalities*
- Identifier: `arXiv:2605.16889`; DOI: `10.48550/arXiv.2605.16889`
- URL: https://arxiv.org/abs/2605.16889

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,626 on draw 1 for this slot.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Controlling-Decision-Drift-in-Multimodal-Sentiment-Analysi` slug; the 24-hour marker cutoff was 2026-07-31.
- Duplicate exclusions: 0; source-gate exclusions: 0; metadata exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,850,422 bytes with valid `%PDF-` header and trailing `%%EOF`; pages: 9; extracted text characters: 49,365.
- Full-paper HTML: 157,997 bytes, 45,653 body characters, 46 heading/section markers, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260801-Arxiv-Controlling-Decision-Drift-in-Multimodal-Sentiment-Analysi-LOG.md`
- `.reports/BL-Arxiv-Controlling-Decision-Drift-in-Multimodal-Sentiment-A-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-Controlling Decision/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-Controlling Decision/controlling_decision_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - CorrKD Missing Modal - DEP-E; concrete overlap: analysis, missing, modalities, modality, multimodal.
2. `.lake-data/DEP-E/DEP-E-20260725-Removal then Selection A/removal_then_selection_a_manuscript.md` - Removal then Selection A - DEP-E; concrete overlap: analysis, decision, drift, missing, modalities.
3. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; concrete overlap: analysis, decision, drift, missing, multimodal.

Only generated Markdown and the required dedup JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
