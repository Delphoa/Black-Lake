# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P01`
- Public-safe date: 2026-07-25
- Paper: *NeMO: Neural Map Growing System for Spatiotemporal Fusion in Bird's-Eye-View and BDD-Map Benchmark*
- Identifier: `arXiv:2306.04540`; DOI: `10.48550/arXiv.2306.04540`
- URL: https://arxiv.org/abs/2306.04540

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 30,208 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `NeMO-Neural-Map-Growing-System-for` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,012,777 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 573,168 bytes, 66,549 body characters, 44 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-NeMO-Neural-Map-Growing-System-for-LOG.md`
- `.reports/BL-Arxiv-NeMO-Neural-Map-Growing-System-for-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-NeMO Neural Map Growing/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-NeMO Neural Map Growing/nemo_neural_map_growing_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: bird, s-eye-view, perception, segmentation.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - iKalibr Calibration - DEP-E; overlap: spatiotemporal, systems.
3. `.lake-data/DEP-E/DEP-E-20260723-Rethinking Facial Express/rethinking_facial_express_manuscript.md` - Rethinking Facial Expression Rec - DEP-E; overlap: datasets, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
