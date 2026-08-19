# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P174`
- Public-safe date: 2026-08-19
- Paper: *Language model fusion for streaming end to end speech recognition*
- Identifier: `arXiv:2104.04487`; DOI: `10.48550/arXiv.2104.04487`
- URL: https://arxiv.org/abs/2104.04487

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,325 on draw 23.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: model, streaming.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Language-model-fusion-for-streaming-end-to` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 4; focus exclusions: 18; source-gate exclusions: 0; reselections: 22.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 263,450 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 127,874 bytes, 26,341 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Language-model-fusion-for-streaming-end-to-LOG.md`
- `.reports/BL-Arxiv-Language-model-fusion-for-streaming-end-to-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Language model fusion for/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Language model fusion for/language_model_fusion_for_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md` - Cued Speech MLLM Review - DEP-E; overlap: speech, recognition, fusion, language.
2. `.lake-data/DEP-E/DEP-E-20260723-Rethinking Facial Express/rethinking_facial_express_manuscript.md` - Rethinking Facial Expression Rec - DEP-E; overlap: recognition, language.
3. `.lake-data/DEP-E/DEP-E-20260816-Where Does Vision Meet/where_does_vision_meet_manuscript.md` - Where Does Vision Meet - DEP-E; overlap: fusion, language.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
