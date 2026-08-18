# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P03`
- Public-safe date: 2026-08-18
- Paper: *L-CAD: Language-based Colorization with Any-level Descriptions using Diffusion Priors*
- Identifier: `arXiv:2305.15217`; DOI: `10.48550/arXiv.2305.15217`
- URL: https://arxiv.org/abs/2305.15217

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 30,543 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `L-CAD-Language-based-Colorization-with-Any` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,908,322 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 246,271 bytes, 51,098 body characters, 60 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-L-CAD-Language-based-Colorization-with-Any-LOG.md`
- `.reports/BL-Arxiv-L-CAD-Language-based-Colorization-with-Any-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-L-CAD Language-based/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-L-CAD Language-based/l_cad_language_based_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-Weak Diffusion Priors/weak_diffusion_priors_manuscript.md` - Weak Diffusion Priors - DEP-E; overlap: priors, diffusion.
2. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: diffusion, priors.
3. `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` - AR-Drag Motion Control - DEP-E; overlap: diffusion, descriptions.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
