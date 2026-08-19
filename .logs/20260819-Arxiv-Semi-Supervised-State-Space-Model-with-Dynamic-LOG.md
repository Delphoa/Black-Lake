# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P382`
- Public-safe date: 2026-08-19
- Paper: *Semi-Supervised State-Space Model with Dynamic Stacking Filter for Real-World Video Deraining*
- Identifier: `arXiv:2505.16811`; DOI: `10.48550/arXiv.2505.16811`
- URL: https://arxiv.org/abs/2505.16811

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 15,453 on draw 1.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: state space model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Semi-Supervised-State-Space-Model-with-Dynamic` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 6,949,062 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 313,034 bytes, 54,582 body characters, 41 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Semi-Supervised-State-Space-Model-with-Dynamic-LOG.md`
- `.reports/BL-Arxiv-Semi-Supervised-State-Space-Model-with-Dynamic-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Semi-Supervised/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Semi-Supervised/semi_supervised_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-SADD RNB/sadd_rnb_manuscript.md` - SADD RNB - DEP-E; overlap: semi-supervised.
2. `.lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md` - RawBMamba Review - DEP-E; overlap: state-space, filter, real-world.
3. `.lake-data/DEP-E/DEP-E-20260819-Out of Sight but Not Out/out_of_sight_but_not_out_manuscript.md` - Out of Sight but Not Out - DEP-E; overlap: video, dynamic.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
