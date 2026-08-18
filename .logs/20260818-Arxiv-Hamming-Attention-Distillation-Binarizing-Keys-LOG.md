# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P01`
- Public-safe date: 2026-08-18
- Paper: *Hamming Attention Distillation: Binarizing Keys and Queries for Efficient Long-Context Transformers*
- Identifier: `arXiv:2502.01770`; DOI: `10.48550/arXiv.2502.01770`
- URL: https://arxiv.org/abs/2502.01770

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,623 on draw 14.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: context.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Hamming-Attention-Distillation-Binarizing-Keys` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 13; source-gate exclusions: 0; reselections: 13.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 879,090 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 164,682 bytes, 44,200 body characters, 55 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Hamming-Attention-Distillation-Binarizing-Keys-LOG.md`
- `.reports/BL-Arxiv-Hamming-Attention-Distillation-Binarizing-Keys-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Hamming Attention/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Hamming Attention/hamming_attention_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: transformers, attention.
2. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md` - CLOVER Test Benchmark - DEP-E; overlap: long-context, keys.
3. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - VLM Probing - DEP-E; overlap: transformers, distillation, attention.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
