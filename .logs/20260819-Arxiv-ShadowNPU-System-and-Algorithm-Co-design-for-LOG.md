# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P148`
- Public-safe date: 2026-08-19
- Paper: *ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference*
- Identifier: `arXiv:2508.16703`; DOI: `10.48550/arXiv.2508.16703`
- URL: https://arxiv.org/abs/2508.16703

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 58,308 on draw 14.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ShadowNPU-System-and-Algorithm-Co-design-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 11; source-gate exclusions: 0; reselections: 13.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,369,934 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 14; sampled text inspection: true.
- Full-paper HTML: 403,527 bytes, 75,159 body characters, 43 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-ShadowNPU-System-and-Algorithm-Co-design-for-LOG.md`
- `.reports/BL-Arxiv-ShadowNPU-System-and-Algorithm-Co-design-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-ShadowNPU System and/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-ShadowNPU System and/shadownpu_system_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Co-design Hardware and/co_design_hardware_and_manuscript.md` - Co-design Hardware and - DEP-E; overlap: co-design, algorithm.
2. `.lake-data/DEP-E/DEP-E-20260819-Clo-HDnn A 4 66 TFLOPS W/clo_hdnn_a_4_66_tflops_w_manuscript.md` - Clo-HDnn A 4 66 TFLOPS W - DEP-E; overlap: on-device.
3. `.lake-data/DEP-E/DEP-E-20260819-APSQ Additive Partial Sum/apsq_additive_partial_sum_manuscript.md` - APSQ Additive Partial Sum - DEP-E; overlap: co-design, algorithm, inference.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
