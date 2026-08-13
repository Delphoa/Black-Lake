# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260811-BB3E2A1B`
- Deployment item ID: `BLAD-2200-20260811-BB3E2A1B-P06`
- Public-safe date: 2026-08-11
- Paper: *RGB-T Semantic Segmentation with Location, Activation, and Sharpening*
- Identifier: `arXiv:2210.14530`; DOI: `10.1109/TCSVT.2022.3208833`
- URL: https://arxiv.org/abs/2210.14530

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,442 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RGB-T-Semantic-Segmentation-with-Location` slug; the 24-hour marker cutoff was 2026-08-10.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 9,694,057 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 648,483 bytes, 76,585 body characters, 40 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260811-Arxiv-RGB-T-Semantic-Segmentation-with-Location-LOG.md`
- `.reports/BL-Arxiv-RGB-T-Semantic-Segmentation-with-Location-20260811/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/README.md`
- `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/rgb_t_semantic_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: segmentation, semantic.
2. `.lake-data/DEP-E/DEP-E-20260725-CLCI-Net Cross-Level/clci_net_cross_level_manuscript.md` - CLCI-Net Cross-Level - DEP-E; overlap: segmentation.
3. `.lake-data/DEP-E/DEP-E-20260730-SOC Semantic-Assisted/soc_semantic_assisted_manuscript.md` - SOC Semantic-Assisted - DEP-E; overlap: segmentation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
