# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P04`
- Public-safe date: 2026-08-10
- Paper: *VITATECS: A Diagnostic Dataset for Temporal Concept Understanding of Video-Language Models*
- Identifier: `arXiv:2311.17404`; DOI: `10.48550/arXiv.2311.17404`
- URL: https://arxiv.org/abs/2311.17404

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,791 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `VITATECS-A-Diagnostic-Dataset-for-Temporal` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,571,741 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 187,407 bytes, 52,479 body characters, 73 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-VITATECS-A-Diagnostic-Dataset-for-Temporal-LOG.md`
- `.reports/BL-Arxiv-VITATECS-A-Diagnostic-Dataset-for-Temporal-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-VITATECS A Diagnostic/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-VITATECS A Diagnostic/vitatecs_a_diagnostic_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - VLM Probing - DEP-E; overlap: vision-language models, diagnostic evaluation, model behavior.
2. `.lake-data/DEP-E/DEP-E-20260730-SOC Semantic-Assisted/soc_semantic_assisted_manuscript.md` - SOC Semantic-Assisted - DEP-E; overlap: language-guided video understanding, temporal grounding, semantic object tracking.
3. `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md` - CFE2 Search Explanations - DEP-E; overlap: counterfactual construction, factor isolation, diagnostic explanations.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
