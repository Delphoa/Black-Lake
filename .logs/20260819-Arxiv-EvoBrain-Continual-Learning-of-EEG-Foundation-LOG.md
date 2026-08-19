# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P304`
- Public-safe date: 2026-08-19
- Paper: *EvoBrain: Continual Learning of EEG Foundation Models Across Heterogeneous BCI Tasks*
- Identifier: `arXiv:2606.01767`; DOI: `10.48550/arXiv.2606.01767`
- URL: https://arxiv.org/abs/2606.01767

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 58,084 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: continual learning.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `EvoBrain-Continual-Learning-of-EEG-Foundation` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 5; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 12,341,916 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 578,101 bytes, 114,335 body characters, 95 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-EvoBrain-Continual-Learning-of-EEG-Foundation-LOG.md`
- `.reports/BL-Arxiv-EvoBrain-Continual-Learning-of-EEG-Foundation-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-EvoBrain Continual/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-EvoBrain Continual/evobrain_continual_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260816-EEGFormer Towards/eegformer_towards_manuscript.md` - EEGFormer Towards - DEP-E; overlap: eeg, foundation.
2. `.lake-data/DEP-E/DEP-E-20260819-Few-Shot Continual/few_shot_continual_manuscript.md` - Few-Shot Continual - DEP-E; overlap: continual, foundation, tasks.
3. `.lake-data/DEP-E/DEP-E-20260811-Parameterizing Context/parameterizing_context_manuscript.md` - Parameterizing Context - DEP-E; overlap: continual, tasks.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
