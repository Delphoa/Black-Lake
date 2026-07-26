# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P01`
- Public-safe date: 2026-07-26
- Paper: *Compressed CSI Feedback With Learned Measurement Matrix for mmWave Massive MIMO*
- Identifier: `arXiv:1903.02127`; DOI: `10.48550/arXiv.1903.02127`
- URL: https://arxiv.org/abs/1903.02127

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 18,733 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Compressed-CSI-Feedback-With-Learned-Measurement` slug; the 24-hour marker cutoff was 2026-07-25.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 546,334 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 4; sampled text inspection: true.
- Full-paper HTML: 339,642 bytes, 29,567 body characters, 28 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260726-Arxiv-Compressed-CSI-Feedback-With-Learned-Measurement-LOG.md`
- `.reports/BL-Arxiv-Compressed-CSI-Feedback-With-Learned-Measurement-20260726/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260726-Compressed CSI Feedback/README.md`
- `.lake-data/DEP-E/DEP-E-20260726-Compressed CSI Feedback/compressed_csi_feedback_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Acoustic Phase Retrieval - DEP-E; overlap: recovery, problem.
2. `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md` - SMES Expert Sparsity - DEP-E; overlap: sparsity, sparse.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: compression, sparse.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
