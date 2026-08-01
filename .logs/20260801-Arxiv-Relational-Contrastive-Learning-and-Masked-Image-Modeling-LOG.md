# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260801-A1ED7FC9`
- Deployment item ID: `BLAD-2200-20260801-A1ED7FC9-P03`
- Public-safe date: 2026-08-01
- Paper: *Relational Contrastive Learning and Masked Image Modeling for Scene Text Recognition*
- Identifier: `arXiv:2411.11219`; DOI: `10.48550/arXiv.2411.11219`
- URL: https://arxiv.org/abs/2411.11219

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 24,396 on draw 1 for this slot.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Relational-Contrastive-Learning-and-Masked-Image-Modeling` slug; the 24-hour marker cutoff was 2026-07-31.
- Duplicate exclusions: 0; source-gate exclusions: 0; metadata exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,104,961 bytes with valid `%PDF-` header and trailing `%%EOF`; pages: 13; extracted text characters: 73,220.
- Full-paper HTML: 443,328 bytes, 85,470 body characters, 60 heading/section markers, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260801-Arxiv-Relational-Contrastive-Learning-and-Masked-Image-Modeling-LOG.md`
- `.reports/BL-Arxiv-Relational-Contrastive-Learning-and-Masked-Image-Mod-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-Relational Contrastive/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-Relational Contrastive/relational_contrastive_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md` - Pixel-Point Transfer - DEP-E; concrete overlap: contrastive, image, learning, recognition, relational.
2. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; concrete overlap: image, learning, masked, scene, text.
3. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave - DEP-E; concrete overlap: image, learning, modeling, scene, text.

Only generated Markdown and the required dedup JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
