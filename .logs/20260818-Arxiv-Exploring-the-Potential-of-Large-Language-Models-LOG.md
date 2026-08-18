# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P09`
- Public-safe date: 2026-08-18
- Paper: *Exploring the Potential of Large Language Models (LLMs) in Learning on Graphs*
- Identifier: `arXiv:2307.03393`; DOI: `10.48550/arXiv.2307.03393`
- URL: https://arxiv.org/abs/2307.03393

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,234 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Exploring-the-Potential-of-Large-Language-Models` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 720,560 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 381,713 bytes, 114,383 body characters, 71 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Exploring-the-Potential-of-Large-Language-Models-LOG.md`
- `.reports/BL-Arxiv-Exploring-the-Potential-of-Large-Language-Models-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Exploring the Potential/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Exploring the Potential/exploring_the_potential_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-LTRDetector Exploring/ltrdetector_exploring_manuscript.md` - LTRDetector Exploring Review - DEP-E; overlap: exploring, potential.
2. `.lake-data/DEP-E/DEP-E-20260810-Exploring Self-supervised/exploring_self_supervised_manuscript.md` - Exploring Self-supervised - DEP-E; overlap: exploring, potential.
3. `.lake-data/DEP-E/DEP-E-20260729-Link Prediction on Latent/link_prediction_on_latent_manuscript.md` - Link Prediction on Latent - DEP-E; overlap: graphs, potential.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
