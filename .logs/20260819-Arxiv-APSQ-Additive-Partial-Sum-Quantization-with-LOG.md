# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P168`
- Public-safe date: 2026-08-19
- Paper: *APSQ: Additive Partial Sum Quantization with Algorithm-Hardware Co-Design*
- Identifier: `arXiv:2505.03748`; DOI: `10.48550/arXiv.2505.03748`
- URL: https://arxiv.org/abs/2505.03748

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 51,344 on draw 11.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `APSQ-Additive-Partial-Sum-Quantization-with` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 8; source-gate exclusions: 0; reselections: 10.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 695,596 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 203,689 bytes, 42,596 body characters, 44 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-APSQ-Additive-Partial-Sum-Quantization-with-LOG.md`
- `.reports/BL-Arxiv-APSQ-Additive-Partial-Sum-Quantization-with-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-APSQ Additive Partial Sum/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-APSQ Additive Partial Sum/apsq_additive_partial_sum_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Gen-NeRF Efficient and/gen_nerf_efficient_and_manuscript.md` - Gen-NeRF Efficient and - DEP-E; overlap: algorithm-hardware, co-design.
2. `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md` - Schwarz Neural Inference - DEP-E; overlap: additive, partial.
3. `.lake-data/DEP-E/DEP-E-20260819-Anisotropic/anisotropic_manuscript.md` - Anisotropic - DEP-E; overlap: additive.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
