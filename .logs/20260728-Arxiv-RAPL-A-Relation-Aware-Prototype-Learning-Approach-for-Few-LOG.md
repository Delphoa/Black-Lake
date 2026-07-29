# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P04`
- Public-safe date: 2026-07-28
- Paper: *RAPL: A Relation-Aware Prototype Learning Approach for Few-Shot Document-Level Relation Extraction*
- Identifier: `arXiv:2310.15743`; DOI: `10.48550/arXiv.2310.15743`
- URL: https://arxiv.org/abs/2310.15743

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75825 PDFs and 75822 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 21451.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RAPL-A-Relation-Aware-Prototype-Learning-Approach-for-Few` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 725942 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 24.
- Full-paper HTML: 745411 bytes, 43789 body characters, 25 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-RAPL-A-Relation-Aware-Prototype-Learning-Approach-for-Few-LOG.md`
- `.reports/BL-Arxiv-RAPL-A-Relation-Aware-Prototype-Learning-Approach-for-Few-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-RAPL Relation-Aware/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-RAPL Relation-Aware/rapl_relation_aware_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; overlap: all, average, document.
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` - ViT Semantic Robustness - DEP-E; overlap: document, extraction, how.
3. `.lake-data/DEP-E/DEP-E-20260722-Few shot Multi label/few_shot_multi_label_manuscript.md` - Few shot Multi label Review - DEP-E; overlap: few-shot classification, sparse labels, prototype generalization.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
