# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P386`
- Public-safe date: 2026-08-19
- Paper: *Road Curb Detection Using A Novel Tensor Voting Algorithm*
- Identifier: `arXiv:1911.12937`; DOI: `10.48550/arXiv.1911.12937`
- URL: https://arxiv.org/abs/1911.12937

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 6,776 on draw 19.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Road-Curb-Detection-Using-A-Novel-Tensor` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 16; source-gate exclusions: 0; reselections: 18.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,048,411 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 98,905 bytes, 29,760 body characters, 59 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Road-Curb-Detection-Using-A-Novel-Tensor-LOG.md`
- `.reports/BL-Arxiv-Road-Curb-Detection-Using-A-Novel-Tensor-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Road Curb Detection Using/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Road Curb Detection Using/road_curb_detection_using_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` - Multi-Point ISAC - DEP-E; overlap: voting, algorithm, detection.
2. `.lake-data/DEP-E/DEP-E-20260818-Mask Proposal Voting/mask_proposal_voting_manuscript.md` - Mask Proposal Voting - DEP-E; overlap: voting, detection.
3. `.lake-data/DEP-E/DEP-E-20260819-A Novel Learning/a_novel_learning_manuscript.md` - A Novel Learning - DEP-E; overlap: novel, algorithm, detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
