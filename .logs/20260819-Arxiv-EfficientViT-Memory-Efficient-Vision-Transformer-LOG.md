# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P383`
- Public-safe date: 2026-08-19
- Paper: *EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention*
- Identifier: `arXiv:2305.07027`; DOI: `10.48550/arXiv.2305.07027`
- URL: https://arxiv.org/abs/2305.07027

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 52,745 on draw 13.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: memory, transformer.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `EfficientViT-Memory-Efficient-Vision-Transformer` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 9; source-gate exclusions: 0; reselections: 12.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,573,078 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 300,006 bytes, 59,542 body characters, 42 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-EfficientViT-Memory-Efficient-Vision-Transformer-LOG.md`
- `.reports/BL-Arxiv-EfficientViT-Memory-Efficient-Vision-Transformer-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-EfficientViT Memory/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-EfficientViT Memory/efficientvit_memory_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - AFIDAF Vision - DEP-E; overlap: vision, attention, efficientvit, group, transformer.
2. `.lake-data/DEP-E/DEP-E-20260806-Inception Transformer/inception_transformer_manuscript.md` - Inception Transformer - DEP-E; overlap: transformer, vision, group, attention, memory.
3. `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/heightformer_learning_manuscript.md` - HeightFormer Learning - DEP-E; overlap: transformer, vision, attention, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
