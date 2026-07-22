# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P02`
- Public-safe date: 2026-07-22
- Paper: *Building a Taiwanese Mandarin Spoken Language Model: A First Attempt*
- Identifier: `arXiv:2411.07111`; DOI: `10.48550/arXiv.2411.07111`
- URL: https://arxiv.org/abs/2411.07111

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 24,221 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Building-Taiwanese` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 3,214,205 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 270,616 bytes, 96,281 body characters, 2 document markers, 100 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-Building-Taiwanese-LOG.md`
- `.reports/BL-Arxiv-Building-Taiwanese-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-Building Taiwanese/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-Building Taiwanese/building_taiwanese_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260719-Business What If/business_what_if_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
