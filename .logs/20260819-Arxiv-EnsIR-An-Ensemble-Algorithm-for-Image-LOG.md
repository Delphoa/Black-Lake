# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P221`
- Public-safe date: 2026-08-19
- Paper: *EnsIR: An Ensemble Algorithm for Image Restoration via Gaussian Mixture Models*
- Identifier: `arXiv:2410.22959`; DOI: `10.48550/arXiv.2410.22959`
- URL: https://arxiv.org/abs/2410.22959

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,081 on draw 2.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `EnsIR-An-Ensemble-Algorithm-for-Image` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 18,376,565 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 0; sampled text inspection: true.
- Full-paper HTML: 668,793 bytes, 105,296 body characters, 96 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-EnsIR-An-Ensemble-Algorithm-for-Image-LOG.md`
- `.reports/BL-Arxiv-EnsIR-An-Ensemble-Algorithm-for-Image-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-EnsIR An Ensemble/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-EnsIR An Ensemble/ensir_an_ensemble_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Low-light Image/low_light_image_manuscript.md` - Low-light Image - DEP-E; overlap: algorithm, image.
2. `.lake-data/DEP-E/DEP-E-20260726-MoE3D Mixture of Experts/moe3d_mixture_of_experts_manuscript.md` - MoE3D Mixture of Experts - DEP-E; overlap: mixture.
3. `.lake-data/DEP-E/DEP-E-20260810-Knowledge Distilled/knowledge_distilled_manuscript.md` - Knowledge Distilled - DEP-E; overlap: ensemble.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
