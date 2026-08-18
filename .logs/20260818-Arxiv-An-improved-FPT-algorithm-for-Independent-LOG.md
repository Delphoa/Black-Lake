# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P04`
- Public-safe date: 2026-08-18
- Paper: *An improved FPT algorithm for Independent Feedback Vertex Set*
- Identifier: `arXiv:1803.00937`; DOI: `10.48550/arXiv.1803.00937`
- URL: https://arxiv.org/abs/1803.00937

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,290 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `An-improved-FPT-algorithm-for-Independent` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 1; focus exclusions: 4; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 724,882 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 364,077 bytes, 45,113 body characters, 41 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-An-improved-FPT-algorithm-for-Independent-LOG.md`
- `.reports/BL-Arxiv-An-improved-FPT-algorithm-for-Independent-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-An improved FPT algorithm/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-An improved FPT algorithm/an_improved_fpt_algorithm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` - RLMF Uncertainty - DEP-E; overlap: feedback, set, independent.
2. `.lake-data/DEP-E/DEP-E-20260726-Compressed CSI Feedback/compressed_csi_feedback_manuscript.md` - Compressed CSI Feedback - DEP-E; overlap: feedback, set, independent.
3. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; overlap: feedback, set, independent.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
