# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P07`
- Public-safe date: 2026-08-15
- Paper: *Hierarchical Perceptual Noise Injection for Social Media Fingerprint Privacy Protection*
- Identifier: `arXiv:2208.10688`; DOI: `10.48550/arXiv.2208.10688`
- URL: https://arxiv.org/abs/2208.10688

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,302 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Hierarchical-Perceptual-Noise-Injection-for` slug; the 24-hour marker cutoff was 2026-08-14.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 15,921,830 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 338,007 bytes, 73,966 body characters, 76 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260815-Arxiv-Hierarchical-Perceptual-Noise-Injection-for-LOG.md`
- `.reports/BL-Arxiv-Hierarchical-Perceptual-Noise-Injection-for-20260815/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260815-Hierarchical Perceptual/README.md`
- `.lake-data/DEP-E/DEP-E-20260815-Hierarchical Perceptual/hierarchical_perceptual_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260814-A Survey of Trustworthy/a_survey_of_trustworthy_manuscript.md` - A Survey of Trustworthy - DEP-E; overlap: protection, privacy.
2. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: hierarchical, perceptual, injection, noise, privacy.
3. `.lake-data/DEP-E/DEP-E-20260809-CDGraph Dual Conditional/cdgraph_dual_conditional_manuscript.md` - CDGraph Dual Conditional - DEP-E; overlap: social, privacy.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
