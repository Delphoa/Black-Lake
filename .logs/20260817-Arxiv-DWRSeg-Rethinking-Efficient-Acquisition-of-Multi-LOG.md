# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P08`
- Public-safe date: 2026-08-17
- Paper: *DWRSeg: Rethinking Efficient Acquisition of Multi-scale Contextual Information for Real-time Semantic Segmentation*
- Identifier: `arXiv:2212.01173`; DOI: `10.48550/arXiv.2212.01173`
- URL: https://arxiv.org/abs/2212.01173

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 36,401 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `DWRSeg-Rethinking-Efficient-Acquisition-of-Multi` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,914,063 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 195,645 bytes, 43,490 body characters, 41 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-DWRSeg-Rethinking-Efficient-Acquisition-of-Multi-LOG.md`
- `.reports/BL-Arxiv-DWRSeg-Rethinking-Efficient-Acquisition-of-Multi-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-DWRSeg Rethinking/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-DWRSeg Rethinking/dwrseg_rethinking_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: segmentation, semantic, real-time.
2. `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/rgb_t_semantic_manuscript.md` - RGB-T Semantic - DEP-E; overlap: segmentation, semantic.
3. `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/dehomogenized_3d_topology_manuscript.md` - 3D Dehomogenization - DEP-E; overlap: multi-scale, information.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
