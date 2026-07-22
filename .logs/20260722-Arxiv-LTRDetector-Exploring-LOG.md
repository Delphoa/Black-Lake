# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P09`
- Public-safe date: 2026-07-22
- Paper: *LTRDetector: Exploring Long-Term Relationship for Advanced Persistent Threats Detection*
- Identifier: `arXiv:2404.03162`; DOI: `10.48550/arXiv.2404.03162`
- URL: https://arxiv.org/abs/2404.03162

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 31,905 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `LTRDetector-Exploring` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 1,998,471 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 378,806 bytes, 67,383 body characters, 2 document markers, 49 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-LTRDetector-Exploring-LOG.md`
- `.reports/BL-Arxiv-LTRDetector-Exploring-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-LTRDetector Exploring/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-LTRDetector Exploring/ltrdetector_exploring_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
